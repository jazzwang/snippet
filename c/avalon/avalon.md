# Avalon

- Git Repo
  - https://github.com/freriadoc/Avalon

> [!TIP]
> Fast fork of llama.cpp designed for Qwen3.8-Flash-Next

## 2026-11-01

- Tool: Pi Agent + llama.cpp/unsloth/Qwen3.5-9B

> [!NOTE]
> 根據 https://github.com/freriadoc/Avalon 內容撰寫一篇技術報告，採用繁體中文（台灣用詞）撰寫，包括 step-by-step 測試步驟，存成 Avalon.md

## Avalon 技術報告

**Qwen3.8-Flash-Next 專用的高性能推理引擎**

### 摘要

Avalon 是從 [llama.cpp](https://github.com/ggml-org/llama.cpp) 分叉出的專有推理引擎，專為 [Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next) 125B MoE 模型設計。該模型擁有 512 個專家、10 個活性專家、48 層結構。Avalon 的核心設計理念是在單一消費級 GPU 上運行，並將專家權重放在系統 RAM 中，以最大化硬體資源利用率。

#### 關鍵成就

- **98 tokens/s** 在 AMD RX 7900 XT (PCIe 3.0, Ryzen 7 3800XT, 64 GB DDR4)
- **16 GB RAM 足夠**：即使伺服器限制 14 GB，89 GiB 模型仍能達到 90 tokens/s
- 使用 **MTP (Multi-Token Prediction)** 可達 **98.4 tokens/s** (短提示，暖快取)
- 在相同硬體上比 Strata 快 **44%** (短提示) 和 **30%** (250k 填充)

### 硬體架構設計

#### 測試環境規格

| 組件 | 規格 | 用途 |
|------|------|------|
| CPU | AMD Ryzen 7 3800XT (Zen 2, 2019), 8 核心 | 計算 GPU 未持有的專家 |
| RAM | DDR4-3200, 雙通道 (33–35 GB/s), 64 GB (16 GB 足夠) | 儲存所有 GPU 未持有的專家 |
| GPU | AMD Radeon RX 7900 XT 20 GB (RDNA3, 2022), ROCm | 儲存密集權重、KV Cache 和最熱專家快取 |
| 匯流排 | PCIe 3.0 x16 (~14 GB/s) | 專家從 RAM 複製到 GPU 的通道 |

#### 記憶體配置

- 模型大小：~89 GiB
- GPU 持有：~4.6 GiB 密集權重 + 9–14 GiB 專家快取
- RAM 持有：剩餘專家（記憶體映射，不足時從磁碟重新讀取）
- **16 GB RAM 足夠**：模型記憶體映射，超出部分從磁碟重新讀取

### 核心設計理念

#### 1. 榨乾硬體每一滴水

- RAM、VRAM、CPU、PCIe 連結和 GPU 應全天候满载運作
- **無 VRAM 閒置**：任何階段不需要的資料立即返回專家快取
- **資源共享**：
  - 計算緩衝區在階段間借給快取，圖形需要時收回
  - 填充預取位元組從快取借用
  - KV Cache 超出當前上下文的區域歸快取所有，直到上下文在那裡增長
  - 外部預留緩存是計算而非猜測
- **並行處理**：CPU 計算缺失專家，GPU 計算快取的專家
- **預取優化**：填充時 PCIe 連結預取下一批專家，生成時攜帶分派器移送到 GPU 的專家，快取填充

#### 2. 與 AI 協同優化

- **巨觀優化**、架構設計、RAM/CPU/PCIe/GPU 工作流程來自作者 30 年優化經驗
- **AI 角色**：
  1. 構建模擬器、基準測試和儀表測量，使每個決策精確
  2. **所有微優化**、GPU 核心和 CPU 核心完全由 **Claude Opus 5.5** 撰寫，作者導航
- **分工**：作者是駕駛員，AI 是引擎，其餘是車身

### 效能測試

#### 測試條件

- **量化**：IQ3_KS hybrid (2–4 bit 專家，困惑度接近 Unsloth UD-IQ4_XS)
- **解碼**：貪婪解碼，512 tokens
- **MTP**：MTP 猜測解碼，2 個草稿 token
- **統計**：最佳情況為 3 個答案的平均值，其他行為 2 次運算的中位數

#### 測試結果 (AMD RX 7900 XT)

| 情境 | 生成 (無 MTP) | 生成 (MTP) | 填充 (無 MTP / MTP) |
|------|--------------|-----------|-------------------|
| 32k 上下文，短提示，暖快取 | 66.1 t/s | **98.4 t/s** | — |
| 32k 上下文，32k 填充 | 62.3 t/s | 88.0 t/s | 1,854 / 1,680 t/s |
| 256k 上下文，131k 填充 | 60.5 t/s | 88.0 t/s | 1,693 / 1,521 t/s |
| 256k 上下文，250k 填充 | 57.3 t/s | 81.1 t/s | 1,491 / 1,342 t/s |

> 註：t/s = tokens per second

#### 專家跳過優化

- **機制**：驗證時每個 token 僅路由到 rank 7 或更低的遺失專家被跳過（預設開啟）
- **參數**：`GGML_CUDA_MOE_TAIL_SKIP=0` 可關閉
- **效能影響**：開啟時 98.4 t/s，關閉時 90.7 t/s（短提示）
- **品質影響**：GSM8K 測試結果相同

#### 與 Strata 比較（相同機器）

| 引擎 | 短提示 (無 MTP / MTP) | 256k 上下文 250k 填充 (無 MTP / MTP) | 最大填充 |
|------|---------------------|-----------------------------------|---------|
| **Avalon** | **66.1 / 98.4** | **57.3 / 81.1** | **1,854** |
| Strata v0.2.9 (HIP) | 51.1 / 68.4 | 48.3 / 62.6 | 1,453 |

- 同一天、相同協議、都開啟尾跳過
- Strata 服務 ISTA 的 IQ3_S 模型（我們的專家來源）
- 自帶草稿器

#### NVIDIA RTX 4090 (CUDA) 測試

- 硬體：RTX 4090 24 GB (PCIe 4.0 x16), AMD EPYC 7443 (24 核心)
- 峰值 VRAM：~23.5 GiB of 24

| 情境 | Avalon | Strata v0.2.9 |
|------|--------|--------------|
| 32k 上下文，短提示，MTP | **141.9 t/s** | 141.4 t/s |
| 32k 上下文，短提示，無 MTP | 98.0 t/s | 101.5 t/s (僅後綴草稿器) |
| 32k 上下文，19k 提示後，MTP / 填充 | **137.7** / 3,113 | 130.8 / 3,422 |
| 256k 上下文，128k 填充，MTP / 填充 | **132.6** / 3,130 | 123.6 / 4,312 |
| 256k 上下文，250k 填充，MTP / 填充 | 123.8 / 2,986 | 128.5 / 4,319 |

> 註：Avalon 的核心仍針對 RDNA3 調整，Strata 在該卡上的填充更快

#### 用戶回報（未驗證）

| 機器 | 測量結果 |
|------|---------|
| **Radeon AI PRO R9700 32 GB** (RDNA4, gfx1201), Xeon, 64 GB RAM, Linux | 262k 上下文，MTP: **86.6 t/s**, 填充 4k/16k/32k: 1,522 / 1,906 / 1,803 t/s; Strata 31.0 t/s |
| **RX 7900 XTX 24 GB**, Ryzen 9 5900X, PCIe 4.0, 64 GB DDR4-3200, Linux | 131k 上下文，填充 2,024–2,043 t/s, 生成 112.9–122.8 t/s (中位數 116.5) |
| **RX 7900 XTX 24 GB**, Ryzen 7 5800X3D, 64 GB RAM, Windows 11 | 32k 上下文，MTP, 快取溫暖：83.6–92.2 t/s |
| **Radeon Pro W7800 48 GB** (RDNA3, 70 CUs) | 單卡：無 MTP 58 t/s，有 MTP 87 t/s; 雙卡（所有專家在 VRAM）：46 和 70 t/s |

### 品質評估

#### 困惑度測試 (Perplexity)

- 測試資料：8 × 4,096 tokens 的外文文本（《戰爭與和平》、《悲慘世界》、SQLite 和 CPython 來源）
- 越低越好

| 量化 | 英文 | 法文 | 程式碼 |
|------|------|------|-------|
| Unsloth UD-Q4_K_XL (104 GB) | 1.316 | 3.581 | 1.325 |
| Unsloth UD-IQ4_XS | 1.401 | 3.841 | 1.343 |
| **Avalon IQ3_KS hybrid** | **1.443** | **3.857** | **1.331** |
| ISTA GSQ-RCO IQ3_S (Strata) | 1.469 | 3.932 | 1.338 |
| AtomicChat AD-4.27bpw | 1.509 | 4.073 | 1.347 |
| ISTA GSQ-RCO IQ3_XXS | 1.596 | 4.294 | 1.364 |

#### 量化方法

- **混合量化**：保留 ISTA 的專家，使用重要性矩陣重新量化 27 層的 up/gate 張量從原始 BF16 權重
- **KV Cache**：q8_0 / q4_0 在 32 上下文中比 f16 增加 0.016 KL 分數

### 記憶體配置 (VRAM)

完整 256k 上下文可容納：
- MTP 草稿模型
- KV Cache (q8_0 / q4_0)
- 專家快取
- 總 VRAM 需求：< 19.7 GiB

### 安裝與編譯

#### 前置條件

- CMake 3.20 或更高版本
- 支援的 GPU 平台（ROCm、CUDA、OpenVINO 等）
- Git

#### 快速開始（Linux）

```bash
## 克隆倉庫
git clone https://github.com/freriadoc/Avalon.git
cd Avalon

## 編譯（根據平台）
cmake -B build -S . -DGGML_BACKEND=metal    # macOS
cmake -B build -S . -DGGML_BACKEND=cuda     # NVIDIA GPU
cmake -B build -S . -DGGML_BACKEND=rocm     # AMD GPU (ROCm)
cmake -B build -S . -DGGML_BACKEND=vulkan   # Vulkan 後端

## 編譯
cmake --build build -j $(nproc)

## 執行
./build/llama-server [參數]
```

#### Windows 安裝

- 參考 [ppkrol/Avalon_windows](https://github.com/ppkrol/Avalon_windows) 移植版本
- 需要 Windows 11 和相應的編譯工具鏈

#### Docker 使用

```bash
## AMD GPU (ROCm)
docker pull freriadoc/avalon:rocm
docker run -it --device /dev/kfd --device /dev/dri --group-add video freriadoc/avalon:rocm

## NVIDIA GPU (CUDA)
docker pull freriadoc/avalon:cuda
docker run -it --gpus all freriadoc/avalon:cuda
```

### 使用範例

#### 基本使用

```bash
./build/llama-server -m model.Qwen3.8-Flash-Next-Avalon-GGUF/qwen3.8-flash-next-avalon-IQ3_KS.gguf -n 512 --color
```

#### MTP 猜測解碼

```bash
./build/llama-server -m model.Qwen3.8-Flash-Next-Avalon-GGUF/qwen3.8-flash-next-avalon-IQ3_KS.gguf -n 512 --mtp-draft-tokens 2
```

#### 專家預取優化

```bash
## 設定專家預取
export GGML_SCHED_PREFETCH_EXPERTS=6
./build/llama-server -m model.Qwen3.8-Flash-Next-Avalon-GGUF/qwen3.8-flash-next-avalon-IQ3_KS.gguf -n 512
```

#### 記憶體上限設定

```bash
## 限制 GPU 記憶體使用
export GGML_CUDA_MOE_MAX_CACHE=14  # 14 GB 專家快取
./build/llama-server -m model.Qwen3.8-Flash-Next-Avalon-GGUF/qwen3.8-flash-next-avalon-IQ3_KS.gguf -n 512
```

#### 專家跳過優化

```bash
## 預設開啟（跳過 rank 7 或更低的專家）
export GGML_CUDA_MOE_TAIL_SKIP=1
./build/llama-server -m model.Qwen3.8-Flash-Next-Avalon-GGUF/qwen3.8-flash-next-avalon-IQ3_KS.gguf -n 512

## 關閉專家跳過
export GGML_CUDA_MOE_TAIL_SKIP=0
./build/llama-server -m model.Qwen3.8-Flash-Next-Avalon-GGUF/qwen3.8-flash-next-avalon-IQ3_KS.gguf -n 512
```

#### CPU 專家快取覆蓋

```bash
## 設定 CPU 專家快取覆蓋
./build/llama-server -m model.Qwen3.8-Flash-Next-Avalon-GGUF/qwen3.8-flash-next-avalon-IQ3_KS.gguf -n 512 --moe-cache-cpu-overlap 2
```

### 環境變數參數

| 參數 | 說明 | 預設值 |
|------|------|--------|
| `GGML_CUDA_MOE_TAIL_SKIP` | 是否跳過低 rank 專家 | 1 (開啟) |
| `GGML_SCHED_PREFETCH_EXPERTS` | 專家預取數量 | 自動 |
| `GGML_CUDA_MOE_MAX_CACHE` | GPU 專家快取大小 (GiB) | 自動 |
| `GGML_SCHED_PREFETCH_EXPERTS` | 專家預取延遲 | 自動 |

### 效能優化建議

#### 1. 記憶體配置優化

- **16 GB RAM 足夠**：模型記憶體映射，超出部分重新讀取
- 使用 NVMe SSD 可提升填充性能
- 限制 RAM 使用可避免交換（swapping）

#### 2. GPU 記憶體管理

- 充分利用 VRAM，避免閒置
- 專家快取自動管理，不需手動配置
- 峰值 VRAM 使用約 23.5 GiB (24 GB 卡)

#### 3. 專家分佈策略

- GPU 持有：密集權重 + 最熱專家快取
- RAM 持有：剩餘專家
- PCIe 3.0  bottlenecks 需留意

#### 4. 預取優化

- 填充階段：PCIe 連結預取下一批專家
- 生成階段：分派器管理專家移動
- 延遲最小化

### 相容性

#### 支援的 GPU 平台

- **AMD ROCm** (首選，針對 RDNA3 優化)
- **NVIDIA CUDA** (支援，但核心針對 RDNA3 調整)
- **OpenVINO** (Intel 平台)
- **Vulkan** (跨平台)
- **SYCL** (Intel OneAPI)

#### 模型支援

- Qwen3.8-Flash-Next (125B MoE) 為主要目標
- GGUF 格式量化支援
- 混合量化 (IQ3_KS)

### 未來方向

- 支援更多模型架構
- 擴展至其他量化格式
- 優化 PCIe 5.0 平台
- 支援更多 GPU 架構（RDNA4, CUDA 新世代）

### 參考資源

1. [Avalon GitHub](https://github.com/freriadoc/Avalon)
2. [Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)
3. [Avalon GGUF 模型](https://huggingface.co/freriadoc/Qwen3.8-Flash-Next-Avalon-GGUF)
4. [Strata 對比測試](https://github.com/Niko1221/Strata)
5. [Windows 移植版本](https://github.com/ppkrol/Avalon_windows)

### 授權

Avalon 基於 llama.cpp 分叉，請參閱原始倉庫的授權文件。

**報告日期**: 2026 年 11 月 1 日
**版本**: 1.0
**作者**: 根據 freriadoc/Avalon 技術文件整理

--------

- 緣起：看到這個影片，用 NotebookLM 生成報告
  - title: "Avalon Just Beat Strata by 47% on AMD (9x Faster)"
  - source: https://www.youtube.com/watch?v=0F63pTS8Gt0
  - created: 2026-11-01

## 破解 AMD 顯卡效能密碼：Avalon 如何以 47% 增幅超越 Strata？底層技術與 Benchmark 實測全解析

### 1. 引言：AMD 玩家的宿命痛點與 Avalon 的震撼登場

對於廣大 AMD 顯卡玩家來說，購買 RX 7900 XT 或 RX 7800 系列時，往往是被其極具誠意的硬體規格所吸引——高達 20GB 的 VRAM 與每秒數百 GB 的記憶體頻寬。然而，當玩家興高采烈地準備在在地端執行大型語言模型（LLM）推論時，現實卻給了一記重拳：受限於成熟度較低的 ROCm 軟體棧、缺乏精細調校的核心（Kernels），以及整體遠落後於 NVIDIA CUDA 的生態體系，推論速度往往只能在 **9 tokens/s** 左右艱難爬行。

這種「硬體強悍、軟體拖累」的宿命痛點，在 2026 年 10 月 22 日迎來了戲劇性的轉折。GitHub 開發者 Freya 發布了一份簡潔的 Readme 測試數據，介紹了一款名為 **Avalon** 的推論引擎。在極具年代感的 2020 年 B450 主機板與一張二手（歐元折算約 500 歐元）AMD RX 7900 XT 顯卡上，Avalon 跑出了高達 **91 tokens/s** 的驚人成績，直接擊敗了當時被公認為 AMD 平台優化頂峰的專用推論引擎 Strata（61.9 tokens/s），實現了 47% 的巨幅效能成長。

> 💡 **核心懸念**
> 一款基於 Llama.cpp 分支改編的引擎，究竟如何在一張二手顯卡與舊型 PCIe 3.0 主機板上實現高達 47% 的超越？這 91 tokens/s 的數據背後，究竟是底層記憶體架構與 SIMD 核心編程的真實突破，還是特定測試條件下的鏡花水月？本文將為您深度拆解 Avalon 的底層優化機制與硬體極限。

### 2. Avalon 的前世今生：開源社群的「復仇之戰」與 AI 賦能開發

要理解 Avalon 的震撼感，必須回溯至 2026 年 10 月 6 日發生的一場「前傳故事」。當時專門針對混合專家模型（MoE）與 AMD 硬體進行優化的專用引擎 Strata 發布了一項測試報告：在 12GB VRAM 的 RTX 3060 上執行 Qwen 模型，Strata 跑出了 41.6 tokens/s，而原生的 Llama.cpp 僅有 **9.1 tokens/s**。高達 4.5 倍的巨大鴻溝，幾乎宣告了通用型引擎 Llama.cpp 在 MoE 架構下的潰敗。

然而，短短兩週之後，Avalon 的登場上演了一齣精彩的開源「復仇之戰」——一個源自 Llama.cpp 的分支引擎，在相同測試基礎上直接逆襲並超越了 Strata 達 47%。

技術上，Avalon 專案於 10 月 9 日以 MIT 授權條款開源，它並非完全原創的全新引擎，而是一部集開源社群大成的「重混（Remix）」作品：

*   **Llama.cpp（2024 年 10 月初版本）**：作為 Avalon 底層架構與通用張量運算的分支起點。
*   **Boon Llama.cpp**：貢獻了第一代專家快取（Expert Cache）的基礎邏輯。
*   **eKlama.cpp**：提供了 Avalon 所採用的高效率模型壓縮格式（Compression Types）。
*   **Strata**：Avalon 在 Readme 中明確致敬 Strata，吸收了其「專家排序檔（Expert Ranking File）」與「快取預載機制（Cache Pre-loading）」的架構思維。

這形成了一個深具啟發性的開源循環：Strata 汲取 Llama.cpp 的養分，而 Avalon 身為 Llama.cpp 的分支，又將 Strata 的精髓反哺融入。

更具話題性的是其開發模式。擁有 30 年效能優化經驗的作者 Freya 透露，Avalon 所有 GPU ROCm Kernels 與 CPU 微優化核心編程，完全是由 **Claude Opus 5.5** 協助編寫與編譯完成的。作者本人僅擔任「駕駛員（Driver）」，而 AI 模型則是「引擎（Engine）」。我們正在見證由 AI 幫忙編寫底層優化核心、用來高速執行 AI 模型的新紀元。

不過，Avalon 採取了極度激進的單一模型特化策略：它全盤針對 **Qwen 38B Flash Next** 模型進行底層佈局微優化，其採用的自訂資料型態甚至無法被原生 Llama.cpp 載入；若嘗試執行其他模型，其行為將退回到原生 Llama.cpp 的普通水準。

### 3. 測試平台與硬體極限約束分析

為了解解析 Avalon 的速度突破，必須深入還原其測試所使用的「平民化」硬體環境。Avalon 的所有優化技巧，皆是針對該平台的硬體瓶頸進行極限擠壓的結果。

| 硬體組件與配置規格 | 實測頻寬與架構極限瓶頸限制 |
| :--- | :--- |
| **顯示卡 (GPU)**<br>AMD Radeon RX 7900 XT (20GB VRAM) | 2022 年底上市（發售價 $899，二手價約 €500–€590）。採用 RDNA3 架構，具備 84 個 Compute Units (CU)，理論記憶體頻寬為 **800 GB/s**。 |
| **中央處理器 (CPU)**<br>AMD Ryzen 7 3800XT (8 核 16 執行緒) | 2020 年 7 月發售的 Zen 2 架構處理器，負責處理 Cache Miss 時的平行算力與記憶體排程。 |
| **主機板 (Motherboard)**<br>AMD B450 主機板 | 雖然 CPU 支援 PCIe 4.0，但 B450 晶片組限制總線僅能以 **PCIe 3.0 x16** 運作，實測 Payload 有效傳輸頻寬極限僅約 **14 GB/s**。 |
| **系統記憶體 (System RAM)**<br>64GB DDR4-3200 (雙通道) | 規格理論頻寬為 51.2 GB/s，但作者實測系統真實記憶體匯流排吞吐量極限僅約 **33–35 GB/s**。 |

### 4. 解密 Qwen 38B Flash Next：MoE 模型的記憶體牆（Memory Wall）挑戰

Qwen 38B Flash Next 雖然名稱帶有「8B」，但其真實規模極為龐大且複雜：

1.  **模型規模**：採用混合專家（Mixture of Experts, MoE）架構，包含 125B 參數的動態專家模型（Active Model）以及一個獨立於顯卡外、高達 51B 參數的外部尋找表（Lookup Table），總參數量達 **177B**，磁碟檔案大小約為 **89 GB**。
2.  **專家結構**：模型包含 48 層（Layers），每層配置 512 個專家，全模型共有 $48 \times 512 = 24,576$ 個專家。
3.  **單一 Token 權重存取量**：在推論生成每個 Token 時，路由（Router）會從每層挑選出 10 個專家進行計算，意味著單一 Token 必須呼叫 **480 個專家**（48 層 × 10 專家/層）。
4.  **記憶體讀取量換算**：以 Avalon 採用的 3.4 bits/parameter 精度計算，生成 **每個 Token 必須從記憶體中讀出約 1 GB 的專家權重**。

在現代 GPU 具備每秒數百兆次浮點運算（TFLOPS）能力的情形下，計算能力絕非瓶頸；**能否以每秒上千 GB 的速度將這 1 GB 的專家權重餵給 GPU**，才是決定推論速度的「記憶體牆（Memory Wall）」關鍵。

我們可以透過硬體頻寬來算推論速度的理論上限：

*   **極限情境 A：專家權重全數存於系統 DDR4 RAM（34 GB/s）**
    $$\text{單 Token 讀取時間} = \frac{1\text{ GB}}{34\text{ GB/s}} \approx 29.4\text{ ms}$$
    在不計算 GPU 運算延遲的前提下，理論推論速度上限被硬性鎖死在 **34 tokens/s**。
*   **極限情境 B：專家權重必須跨越 PCIe 3.0 匯流排（14 GB/s）**
    $$\text{單 Token 讀取時間} = \frac{1\text{ GB}}{14\text{ GB/s}} \approx 71.4\text{ ms}$$
    理論速度極限將驟降至僅 **14 tokens/s**。

然而，Avalon 在關閉推測解碼時已能跑出 **62.4 tokens/s**（相當於每 Token 僅耗時 16 ms）。在 16 ms 內，34 GB/s 的系統 RAM 最多只能提供約 0.54 GB 的資料量。這意味著**至少有一半以上的專家權重必須直接存取自 VRAM（800 GB/s）**。

由於 Qwen 的專家總容量高達約 47 GB，而 RX 7900 XT 僅有 20GB VRAM，扣除基礎模型權重後，VRAM 僅能容納約 **9 至 14 GB 的專家（約占總量的 20%–30%）**。所幸，專家在處理自然語言時的呼叫頻率呈極度不均勻的帕累托分佈（八二法則），少數熱門專家承擔了絕大多數的查詢需求。因此，只要將熱門專家快取在 VRAM 中（Expert Cache），維持極高的命中率（Hit Rate），就能突破 DDR4 RAM 的實體速度天花板。

### 5. Avalon 的核心優化雙雄：動態 VRAM 快取與高效推測解碼

Avalon 能將效能推升 47%，主要歸功於兩大核心底層優化技術：

#### 優化一：動態 VRAM 空間利用與 CPU/GPU 平行計算 (Parallel Compute)

*   **極致榨乾 VRAM 空間**：Avalon 採取了極為激進的記憶體配置策略。它將階段性任務間未使用的計算緩衝區（Compute Buffers）、對話尚未延伸到的 KV Cache 空閒區域，全部借調給 Expert Cache 使用。對於記憶體安全預留量，Avalon 放棄了傳統粗略估算的方式，精確計算出只需留存 **400MB**，其餘空間全部用於快取專家。
*   **非同步流水線處理（Asynchronous Pipelining）**：在執行推論時，GPU 負責計算當前已載入 VRAM 的專家權重；與此同時，8 個 CPU 核心則同步並行處理發生的快取未命中（Cache Miss），負責從 RAM 讀取權重並進行運算。當動態評估發現「將未命中的專家透過 PCIe 載入 VRAM 計算」比「直接在 CPU 上計算」更快時，引擎會動態切換通道。

在不開啟推測解碼的條件下，Strata 跑出 49 tokens/s，而 Avalon 跑出 **62.4 tokens/s**（提升 27%）。單憑這項快取與非同步管道優化，每個 Token 就省下了約 4 毫秒的等待延遲。

#### 優化二：輕量化推測解碼（Speculative Drafting）與 MoE 稅拆解

推測解碼（Speculative Drafting）透過小模型（Draft Head）預測接下來的幾個 Token，再由大模型進行一次性驗證。若預測成功，即可在一次大模型前向傳播（Forward Pass）中產出多個 Token。

然而，在 MoE 模型上實施推測解碼極具挑戰，會面臨嚴重的「MoE 稅（MoE Tax）」：
*   **密集模型 vs. MoE 模型**：傳統密集模型在驗證 3 個草稿 Token 時，模型權重可被重複讀取利用；但在 MoE 模型中，3 個草稿 Token 會各自獨立挑選 10 個專家，驗證一次可能需要觸及多達 $3 \times 10 = 30$ 個不同的專家，導致記憶體讀取量暴增。
*   **精確數學拆解**：
    *   Avalon 的 Draft Head 在固定測試集上記錄到 **80.7% 的接受率（Acceptance Rate）**（每輪預測 2 個 Token）。
    *   若假設預測完全獨立，理論最大加速比可達 **2.46 tokens/pass**。
    *   然而，實際量測到的效能加速僅為 **1.46 倍**。
    *   原因在於「MoE 稅」：由於專家讀取量增加，**每次驗證傳播付出的時間代價相當於生成 1.7 個普通 Token 的時間**。

Avalon 解決此問題的關鍵在於**將 Draft Head 輕量化與整合化**：

*   **縮減記憶體體積**：Avalon 的 Draft Head 僅佔用約 **1.5 GB** VRAM（相比之下，Strata 的獨立 Draft Head 高達 3.4 GB，過大的體積曾迫使 Strata 將主模型的專家擠回 CPU RAM，引發頻寬懲罰）。
*   **詞彙表裁剪與快取共享**：Avalon 將 Draft Head 的詞彙表裁剪至最常用的 **65,000** 個 Token，並讓 Draft Head 直接**共享主模型的 VRAM Expert Cache**。這讓 Draft Head 能在快取預算內運作，完全不犧牲主模型的快取空間。

透過動態快取與並行計算獲得的 **1.27 倍** 加速，乘以高效推測解碼帶來的 **1.15 倍** 加速（$1.27 \times 1.15 \approx 1.47$），最終達成了 **47% 的總效能提升**，將推論速度一舉推升至 **91 tokens/s**。

### 6. Benchmark 的魔鬼細節：引擎、模型檔與版本差異爭議

在客觀評估此基準測試時，身為專家必須審視數據背後的細節與變數：

#### 模型檔案差異與量化品質

測試中 Avalon 與 Strata 並非使用相同的模型檔案。Avalon 使用的是 **88 GB** 的自訂格式檔案，而 Strata 使用的是其專屬的 **78 GB ISTA 格式**。**Avalon 雖然每 Token 需要讀取多出 13% 的位元組（88GB vs 78GB），但推論速度依然更快**。這有力地證明了 Avalon 的速度提升來自於記憶體佈局與 Kernel 執行效率的改善，而非透過破壞質量的過度壓縮手法。

在模型困惑度（Perplexity，數值越低代表文本預測品質越好）測試中：
*   **Avalon 檔案（英文 PPL）**：1.443
*   **Strata ISTA 檔案（英文 PPL）**：1.469
*   **Unsloth IQ4 格式（英文 PPL）**：1.401
*   **Avalon 檔案（程式碼 PPL）**：1.331（Strata 為 1.338）

Avalon 保持了極高的文本預測品質（困惑度優於 Strata）。不過仍需提醒：困惑度不完全等於下游實際任務（Downstream Tasks）的邏輯表現，目前 Avalon 尚未公布 downstream 任務的評測數據。

#### 版本時間差與硬體優化重心

Avalon 在 10 月 22 日公布的對照組為 Strata 於 10 月 11 日發布的 **v0.1.43** 版本。在此後的 18 天內，Strata 快速疊代了 14 個版本（至 v0.2.8）。

查閱 Strata 的 Release Notes 可以發現，其近期的 AMD 優化重點已轉移至 **RDNA4 架構（如 Radeon AI Pro R9700）**。Strata 在 R9700 上成功跑出了 **94.6 tokens/s** 的佳績。Strata 官方維護者明確表示，雖然 RX7000 系列仍在支援清單中，但後續版本的封包並未在實體 RX7000 或 Strix Halo 卡上進行實機微調。

社群多位 RX 7900 XT / XTX 玩家實測 Strata 的反饋顯示，推論速度普遍落在 **59–62 tokens/s** 之間，證明 Avalon 測試表格中所採用的 61.9 tokens/s 基準線是真實且客觀的。此外，根據 Freya 最新報告， Avalon 在其平台上進行後續調校後已進一步突破至 **100 tokens/s**。

| 評比項目 | Avalon | Strata (測試時版本 v0.1.43) |
| :--- | :--- | :--- |
| **測試時間與版本** | 2026 年 10 月 22 日發布 Readme | 2026 年 10 月 11 日發布版本 |
| **模型檔案大小** | 約 **88 GB** | 約 **78 GB** (ISTA 格式) |
| **英文困惑度 (Perplexity)**| **1.443** (品質較佳) | 1.469 |
| **程式碼困惑度** | **1.331** | 1.338 |
| **硬體優化重心** | **RDNA3 (RX 7900 XT)** | **RDNA4 (R9700)** 及高階工作站平台 |
| **近期更新峰值表現** | 實測已達 **100 tokens/s** | R9700 實測達 **94.6 tokens/s** |

### 7. 邊界條件與邊際效應：Avalon 離開 RX 7900 XT 後的實測表現

Avalon 的優化是高度特化且依賴特定環境的，一旦脫離了「RX 7900 XT + 單卡 + 64GB RAM」的黃金組合，其邊際效益將會迅速遞減：

*   ⚠️ **NVIDIA GPU 平台 (RTX 4090)**
    由於 Avalon 的底層 Kernel 完全針對 RDNA3 編寫，CUDA 核心未經精細優化。作者在 RTX 4090 上實測成績為 **120.5 tokens/s**，與 Strata 在該卡上的表現基本持平，作者亦坦言在 NVIDIA 卡上「幾乎沒有優勢」。
*   ⚠️ **雙卡與大顯存環境 (Radeon Pro W7800)**
    當使用單張 48GB VRAM 的 W7800 時，Avalon 跑出 58 tokens/s（未開啟 Drafting）與 87 tokens/s（開啟 Drafting）。然而，當插入**兩張 W7800**、將全數 47 GB 專家權重完全塞入 VRAM 時，速度反而下降至 **46 / 70 tokens/s**（比單卡慢約 20%）。
    **架構解析**：當記憶體頻寬瓶頸消失後，瓶頸轉移到了 GPU 的算力極限（Compute Bound）。W7800 僅有 70 個 CU，少於 7900 XT 的 84 個 CU。這證明 Avalon 的優化極度依賴 7900 XT 特定的算力與頻寬比例。
*   ⚠️ **32GB 系統記憶體環境與未標明的 SSD 變數**
    Avalon 支援透過記憶體映射（mmap）在 32GB RAM（可用約 28GB）的機器上執行。在單純生成 Token 時，速度僅微幅下降 2%（91.2 $\rightarrow$ 89 tokens/s）。但在載入大文本提示詞（例如 19,000 tokens 的 Context）時，由於必須頻繁觸發 Page Fault 從 SSD 讀取資料，提示詞處理時間（Prompt Ingestion）從 15 秒暴增至 21 秒，**延遲增加了 40%**。
    **關鍵缺漏**：Freya 的 Readme 中未標明測試所使用的 SSD 介面規格。PCIe Gen4 NVMe（7,000 MB/s）與 SATA SSD（500 MB/s）在處理 mmap 分頁缺頁時的吞吐量相差達 14 倍，這是評估 32GB 環境時不可忽視的隱形變數。
*   ⚠️ **軟體成熟度與生態系限制**
    目前僅支援 Linux 系統（無 Vulkan 後端，不安裝於 Windows）；僅支援 Qwen 38B Flash Next 單一模型；早期版本甚至曾存在將專家檔案大小重複計算 3 倍（算成 150GB）導致雙卡系統掛起的 Bug，顯示其仍屬於極早期開發階段。

### 8. 結論與實用指南：超特化 Fork 與 Upstream 哲學及解讀 Benchmark 4 大金律

#### 超特化 Fork 與 Upstream 社群哲學的拉扯

Avalon 的出現引發了開源社群對「程式碼分叉（Fork）與主線回饋（Upstream）」的深層思索。Avalon 選擇了一條極端路線：**放棄通用性，無視社群共識，全盤針對單一硬體盒（RX 7900 XT）與單一模型（Qwen 38B）進行極致榨乾**。這種策略讓它在特定硬體上獲得了 47% 的狂暴增幅，但也使其失去了通用推論引擎的彈性。

與此同時，Llama.cpp 主線社群並未停下腳步。開發者 Pota Wilin 已在 Llama.cpp 主線提交了 Pull Request（PR），試圖在不破壞通用架構的前提下，原生整合 CPU/GPU 平行專家處理機制以擊敗 Strata。這代表了兩種不同的開源哲學：單一設備的激進特化 Fork，與維護長期通用相容性的 Upstream 主線。

#### 硬體對應引擎推薦清單

根據實測數據，針對不同的硬體與使用情境，建議選擇最適切的推論引擎：

*   **AMD RX 7900 XT / 7900 XTX 玩家（Linux 系統、RAM $\ge$ 32GB，主攻 Qwen 38B Flash Next）**
    👉 **首選 Avalon**。能立即享有接近 91–100 tokens/s 的極速推論體驗。
*   **AMD RDNA4 (R9700 或更新) 顯卡用戶**
    👉 **首選 Strata**。Strata 官方目前針對該架構進行頻繁優化，實測性能已超越 94.6 tokens/s。
*   **NVIDIA 顯卡用戶**
    👉 **首選 Strata 或原生調校版 Llama.cpp**。Avalon 在 CUDA 架構上無額外 Kernel 優化優勢。
*   **Windows 用戶 / 需要多模型支援 / 需要生態系工具鏈**
    👉 **首選 Strata 或 Llama.cpp 主線**。提供更完整的 Windows/Vulkan 支援與多模型相容性。

> 📋 **解讀 AI 效能 Benchmark 的 4 大金律**
>
> 在面對網路上各式各樣「性能提升 XX%」的宣傳標題時，請務必先確認以下四個核心問題：
>
> 1. **對比的引擎確切版本為何？**（是否拿最新版本的引擎與數個星期前的舊版本對比？）
> 2. **雙方使用的是否為完全相同的模型檔案？**（檔案大小、量化格式與模型精度是否一致？是否透過犧牲精度來換取速度？）
> 3. **硬體細節是否明確？**（是否清楚標示主機板 PCIe 世代、系統 RAM 實際吞吐頻寬以及 SSD 讀取速度？）
> 4. **該基準測試的作者擁有並針對哪台機器進行極致優化？**（效能數據通常反映的是「作者桌上那台機器」的極限調校，而非跨平台的通用真理。）
