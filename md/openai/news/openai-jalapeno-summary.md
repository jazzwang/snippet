# OpenAI Jalapeño 推論晶片技術摘要

## 2026-08-31

> 來源：[SemiAnalysis — OpenAI Jalapeño: Better Than Nvidia Blackwell](https://newsletter.semianalysis.com/p/openai-jalapeno-better-than-nvidia)
> 日期：2026-08-25

## 一、概述

OpenAI 與 Broadcom 合作，從零開始設計了一款專為 LLM 推論打造的自研 ASIC 晶片——**Jalapeño**。該晶片於 Hot Chips 2026 正式亮相，並在 SemiAnalysis 的 InferenceX 基準測試中，在多項開源模型上**超越了 NVIDIA、AMD 及 Google 的所有現有晶片**。

關鍵里程碑：
- **2024 年中**：團隊組建、設計啟動
- **2025 年 11 月**：完成 CoWoS tape-out（流片）
- **約 16 個月**：從初始團隊到製造流片，開發週期極快
- **2027 年**：計劃逐步量產，大部分產能排定於 2027 年底

## 二、硬體規格亮點

| 項目 | 規格 |
|------|------|
| **製程** | TSMC N3P |
| **封裝** | Reticle-size 計算核心 + N3E I/O chiplet（CoWoS） |
| **算力（B0 stepping）** | 13.4 PFLOPs（MXFP4） |
| **記憶體** | HBM4（可能由 Samsung 供應） |
| **記憶體頻寬** | **15.4 TB/s**（HBM4 pin speed 達 10Gbps，略高於 NVIDIA Rubin 的 9.6Gbps） |
| **TDP** | 700W（遠低於 Rubin 的 900–1,150W） |
| **Scale-up I/O** | 32 lanes 800G SerDes（24 lanes 用於機架內 local，8 lanes 用於跨機架 global） |
| **Scale-up 域** | Local：128 XPU/機架；Global：2,048 XPU/16 機架 |
| **系統 I/O** | PCIe Gen 5 連接 x86 主機 CPU |
| **B0 改進** | 相較 A0 stepping，perf/W 提升約 **25%** |

### 與競品比較

- **HBM 頻寬/瓦特**：業界最高
- **FLOPs/瓦特**：業界最高，可與 1,800W Rubin Max-Q 相媲美
- Jalapeño 是 HBM4 的早期採用者，領先 Google TPU 和 AWS Trainium

## 三、架構設計特色

### 3.1 核心架構：消除固定延遲

Jalapeño 的設計核心理念是**消除 KV Cache 與權重的記憶體搬移開銷以及固定延遲**，使其即使在小 batch 或小維度下也能逼近理論 roofline 效能。

- **Out-of-Order (OoO) 核心 + L1 Cache**：有別於業界常見的軟體管理式 scratchpad + async DMA，Jalapeño 使用硬體 cache 層級，避免 barrier latency 等固定開銷
- **Slice 架構**：核心與 HBM 被劃分為 slice，每個核心 slice 對其對應的 HBM slice 擁有低延遲本地存取路徑
- **專用 Collective Network**：slice 間同步透過高頻寬專用集體通訊網路完成
- **小矩陣維度支援**：相較 TPU/Trainium/Etched 的大型脈動陣列，Jalapeño 支援較小矩陣形狀，避免 tiling 和 padding 低效問題
- **Weight-Stationary Systolic Array**：使用 MXFP 數值格式，類似 TPU 但更靈活
- **Prefetching 機制**：依賴良好的預取策略來確保記憶體請求及時到達

### 3.2 不採用 Prefill-Decode 分離（PDD）

OpenAI 刻意選擇**不將 prefill 和 decode 分配到不同晶片池**，理由包括：

- 真實流量的 input/output 比例會持續變動（知識→推理→Agent 三個模型時代）
- 固定的異構硬體分配在流量變化時會導致效率低落
- 分離會破壞 KV Cache 的局部性，需額外網路傳輸
- 推測性解碼（speculative decoding）需要極低延遲的 draft-verifier 耦合，分離反而不利
- 同質化池使得所有裝置在任何時刻都可服務任何請求，提升**全局利用率**

### 3.3 簡化 NoC 與記憶體子系統

相較 NVIDIA 和 Google 複雜的記憶體層級，Jalapeño 的簡化 NoC 和記憶體子系統帶來巨大的功耗節省和效能增益。

## 四、軟體堆疊

### 4.1 Gluon 程式語言

- 基於 **Triton** 建構，保留 SPMD 程式設計模型
- 提供低層級程式設計抽象（類似 PTX 指令層級）
- 核心創新：**Linear Layouts** — OpenAI 發明的 layout 代數系統
  - 數學化定義硬體資源到 tensor 元素的映射
  - 支援可證正確的 layout 轉換和最佳化 memory swizzling
- 每個 Gluon 程式映射為 **persistent thread**，由程式設計師而非硬體排程器分配工作

### 4.2 Kernel 開發方式

- **類組語手寫 kernel**：每個 kernel 手動調優，部分可達 ~3,000 行
- 搭配正確性檢查和自訂 sanitizer
- 早期為人機協作，後期大量使用**內部版本的 Codex** 自動生成 kernel
- **Megakernel（"Gigakernel"）設計**：單一 megakernel 在裝置上循環執行，減少 CPU 開銷和啟動時間

### 4.3 AI 輔助晶片設計

- AI 輔助設計帶來 **SIMD 面積減少 8%** 和**矩陣引擎面積減少 10%**
- 同時改善了時序和功耗表現
- 內部 serving 引擎代號：**Teacup**
- 模擬器 **ChiliSim**：與實際硬體精度在 **5% 以內**

## 五、效能表現

### 5.1 核心指標：Tokens/MW（每兆瓦 token 吞吐量）

OpenAI 以 **perf/W（每瓦效能）** 為首要設計目標，因為資料中心目前受限於電力而非預算。

> 引用 Jensen Huang：「如果你有 1 GW 的電力，那麼每瓦吞吐量就是營收。」

### 5.2 InferenceX 基準測試結果（8k input / 1k output）

| 測試項目 | 結果 |
|----------|------|
| **DeepSeek R1** | 低併發（concurrency 1）達 **>700 tok/s/user** |
| **Kimi K2.5** | 達近 **700 tok/s/user**，為次佳晶片的 **9 倍以上** |
| **GPT-OSS** | iso-interactivity throughput/MW 近乎 GB200 最高點的 **2 倍**，concurrency 1 點的 **50 倍以上** |
| **GPT-OSS / Kimi K2.5** | 約 **1,400 tok/s/user** |
| **Codex 內部模型** | TPOT 達 **1.2ms** |

### 5.3 關鍵對比

- **vs NVIDIA Blackwell（GB200）**：在幾乎所有場景的 perf/W 上勝出
- **vs NVIDIA Vera Rubin**：STP 輸出 token throughput/MW **超越 Vera Rubin 的 MTP 結果**
- **vs Vera Rubin perf/TCO**：兩者接近，但 Jalapeño 是**未使用推測性解碼**的結果；啟用後預計再降 **3–5 倍**成本
- 所有結果均為 **Single Token Prediction（STP）**，無推測性解碼、無 PDD
- GSM8k 評估結果與 NVIDIA 晶片持平

### 5.4 開發速度

- A0 stepping 流片後僅 **3 個月 bring-up** 即產出優異結果
- **不到 2 週**即在特定互動性指標上實現 **2 倍以上吞吐量提升**
- **8 天內**從 TP8 擴展到 **TP32**（全機架規模配置）
- Codex 在無 kernel 工程師介入的情況下，快速產出功能完備且高效的 MLA kernel

## 六、系統架構

### 機架配置

| 組件 | 說明 |
|------|------|
| **Katsu**（主機 tray） | 每機架 16 個，每個含 2x AMD EPYC Turin CPU + 1.5TB DRAM + SSD |
| **Vindaloo**（ASIC tray） | 每機架 16 個，每個含 **8 顆 Jalapeño**（共 128 顆/機架） |
| **Chana**（switch tray） | 每機架 8 個（6 local + 2 global），使用 Broadcom Tomahawk 6 |
| **功耗** | 主機機架 ~50kW（生產 31kW），ASIC 機架 ~130kW，**合計 ~160kW** |
| **合作夥伴** | Celestica（系統設計） |

### 網路拓撲

- **Local domain**（128 XPU/機架）：每 XPU 4.8Tb/s 單向頻寬，全互連至 6 顆 102.4T TH6 交換器，被動銅纜背板
- **Global domain**（2,048 XPU/16 機架）：每 XPU 1.6Tb/s 單向頻寬，8-rail 架構，使用 1.6T 收發器 + **光學電路交換器（OCS）**
- 銅纜背板總計：每 XPU 64 差分對，每機架 8,192 差分對

## 七、注意事項與限制

1. **所有數據由 OpenAI 提供**，SemiAnalysis 在實驗室現場驗證但未跑完整 InferenceX 全套
2. **尚無 AgentX 結果**：AgentX（長上下文、多輪對話）更能反映真實生產負載
3. **僅測試 8k1k 場景**，這比 AgentX 的多輪長上下文場景更容易調優
4. **公平性考量**：Jalapeño 使用 HBM4，更公平的比較對象是同樣使用 HBM4 的 Vera Rubin 而非 Blackwell
5. **尚未測試前沿大模型**：如 DeepSeek V4 Pro、Kimi K3 等更大模型尚未在 Jalapeño 上測試
6. **量產時程**：目前僅有工程樣品，距離大規模部署仍需時日

## 八、產業影響

- **CUDA 護城河受到威脅**：OpenAI 從零開始的軟體堆疊能如此快速地 bring-up 新模型，表明 CUDA 生態的壁壘正在動搖
- **硬軟體協同設計的勝利**：前沿 AI 實驗室的自研 ASIC 團隊在硬軟體協同設計上可以超越成熟的商用晶片廠商
- **從零開始反而是優勢**：無需顧慮向後相容性，可做 clean-sheet 架構決策
- **AI 加速晶片設計已成現實**：16 個月的開發週期證明 AI 確實能加速晶片設計流程
- **反例**：Meta 和 Microsoft 的 AI ASIC 專案儘管起步更早，但並未取得類似突破
- OpenAI 下一個目標是 **100MW 部署規模**，主要挑戰將從軟體轉向硬體部署與運維
- 網路互連僅佔系統總成本約 **10%**，為未來 10–20 兆參數模型或 2–4 百萬 token 上下文視窗保留了彈性

---

*本摘要基於 SemiAnalysis 於 Hot Chips 2026 發表的深度分析報告整理。*
