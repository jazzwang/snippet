# ik_llama.cpp

- Git Repo
  - https://github.com/ikawrakow/ik_llama.cpp

> [!Note]
> llama.cpp fork with additional SOTA quants and improved performance

## 2026-09-05

> [!QUESTION]
> ik_llama.cpp 與 llama.cpp 的關係與差異

ik_llama.cpp 與 llama.cpp 的關係是「激進實驗分支（Fork）」與「主線（Mainline）」的關係。

簡單來說，[llama.cpp](https://atomic.chat/blog/guides/ollama-vs-llamacpp) 是由 Georgi Gerganov 主導、整個開源 AI 社群共同維護的主線專案；而 [ik_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp) 則是由核心開發者 ikawrakow 獨立拉出的高效能優化分支。 [1, 2, 3]
很多時候，ikawrakow 會在自己的 ik_llama.cpp 中嘗試非常激進、前沿的量化演算法與記憶體優化，一旦技術成熟且穩定，這些成果就會被併回（Merge）主線的 llama.cpp 中。 [3, 4]

以下是兩者在核心設計與技術上的差異：

### 📊 核心差異對比

| 比較維度 | llama.cpp (主線) 🦙 | ik_llama.cpp (優化分支) 🚀 |
|---|---|---|
| 專案定位 | 追求最高的硬體相容性與架喚穩定性，是整個地端開源 AI 的標準基石。 | 追求極致的推論速度與前沿量化技術的實驗場。 |
| 硬體強項 | 通用性極佳。從舊電腦、手機、Mac 到企業級顯示卡皆可穩定執行。 | 特別針對 現代 CPU 運算與 CPU+GPU 混合推論（Hybrid Offloading） 進行魔改優化。 |
| 量化技術 (Quant) | 支援最經典的標準 K-quants（如 Q4_K_M）以及已被社群驗證穩定的 IQ 量化。 | 前沿量化技術的發源地。率先研發並支援 IQ_K、IQ_KS、IQ4_NL、IQ4_KSS 等超低位元（Low-bit）高保真量化。 |
| 大型模型優化 | 逐步跟進 MoE 模型優化，注重通用框架的擴充。 | 針對 235B、671B（如 DeepSeek-R1）等超大型混合專家模型（MoE）深度優化，引入 FlashMLA 和模組融合技術。 |
| 更新與周邊生態 | 更新穩健。擁有完美的 WebUI、API 以及週邊生態（如 Ollama 的完美支援）。 | 更新極度頻繁（有時甚至一天數次），功能更前沿，但相對較缺乏週邊上層應用整合。 |

### 🔍 關鍵技術突破## 1. 前沿量化技術（IQ 系列）的推手

地端開源模型能用極低的顯示卡記憶體（VRAM）運行且不變笨，這要歸功於「量化（Quantization）」。ik_llama.cpp 在低位元（2-bit 到 4-bit）量化上做出了突破性的貢獻（如 IQ4_KSS、Trellis 量化）。它利用非線性查找表與 SIMD 優化，做到「相同體積下質量更高，相同質量下速度更快」。 [3, 5]

* 註：許多在 ik_llama.cpp 大獲成功的 IQ 系列量化，已經在 2026 年初陸續被官方併回主線的 llama.cpp 儲存庫中。 [3, 4]

### 2. CPU 與混合推論（Hybrid）的效能榨乾

在標準的 llama.cpp 中，如果 VRAM 不夠、將模型的一部分分流到記憶體（CPU）執行時，速度通常會面臨嚴重的斷崖式下跌。
ik_llama.cpp 修改了底層的矩陣乘法核心（如 AVX2、ARM_NEON 優化）與記憶體交叉排布（Row-interleaved packing），大幅提升了 CPU 的推論效率（有時可達數倍），讓預算有限、需要用「顯示卡 + 電腦記憶體」硬跑超大模型的玩家能獲得顯著的效能回報。 [3, 6, 7, 8]

### 3. 多顯卡（Multi-GPU）並行架構

ik_llama.cpp 引入了創新的圖表分割模式（Split mode graph），解決了以往多張低階顯示卡（例如多張 RTX 3090/4090）並行時效率不彰、僅能疊加 VRAM 的缺點，達成了多顯示卡協同運算時的跨越式效能提升。 [9]

### 💡 總結：你該用哪一個？

* 使用官方主線 llama.cpp（或 Ollama / LM Studio）如果：
* 你想要開箱即用、絕對穩定的體驗，不希望環境常常報錯。
   * 你的模型都可以完全塞進 VRAM（顯示卡記憶體）裡，不需要用到 CPU 記憶體分流。
   * 想要搭配多元的第三方精美 UI 介面使用。 [2, 5, 6]
* 切換到 ik_llama.cpp 如果：
* 你是進階玩家，想要在地端越級挑戰極高參數的大型 MoE 模型（如 DeepSeek-R1 671B、Qwen3-235B），且必須倚賴 CPU+GPU 混合推論。
   * 你擁有多張顯示卡組成的 Homelab，希望榨乾多 GPU 協同運算的每一滴頻寬。
   * 想要第一時間測試 Hugging Face 上最新推出的實驗性高強度的 IQ 量化模型（通常檔名帶有 -ik 或由 ubergarm 等大神壓製的格式）。 [6, 7, 9, 10]

你目前是否正打算在本地部署特定的超大型模型（例如 DeepSeek R1），或者是遇到了 VRAM 不足、需要分流到 CPU 的速度瓶頸呢？我可以進一步提供相關的組態配置建議！

[1] [https://github.com](https://github.com/ikawrakow/ik_llama.cpp)
[2] [https://atomic.chat](https://atomic.chat/blog/guides/ollama-vs-llamacpp)
[3] [https://note.com](https://note.com/nullby/n/n2ebf968774fd?hl=en)
[4] [https://jangwook.net](https://jangwook.net/en/blog/en/llama-cpp-iq-quantization-merge/)
[5] [https://www.reddit.com](https://www.reddit.com/r/LocalLLaMA/comments/1qfcg4h/need_to_know_more_about_less_known_engines_ik/?tl=zh-hant)
[6] [https://www.reddit.com](https://www.reddit.com/r/LocalLLaMA/comments/1qfcg4h/need_to_know_more_about_less_known_engines_ik/)
[7] [https://github.com](https://github.com/ubergarm/r1-ktransformers-guide/issues/11)
[8] [https://daily.dev](https://daily.dev/posts/ikawrakow-ik-llama-cpp-llama-cpp-fork-with-additional-sota-quants-and-improved-performance-esem3uuzj)
[9] [https://medium.com](https://medium.com/@jagusztinl/llama-cpp-performance-breakthrough-for-multi-gpu-setups-04c83a66feb2)
[10] [https://www.reddit.com](https://www.reddit.com/r/LocalLLaMA/comments/1m0wji2/i_feel_that_the_duality_of_llamacpp_and_ikllama/)

## 2026-09-07

- Tool: Pi Agent + llama.cpp + Qwen 3.5 9B Q4_K_M
> [!QUESTION]
> 參考 https://github.com/ikawrakow/ik_llama.cpp 撰寫一篇技術摘要，並附加到 @ik_llama.cpp.md

# 技術摘要：ik_llama.cpp

## 概述

ik_llama.cpp 是 llama.cpp 專案的一個分支，始於 2024 年 6 月，旨在提供改進的 CPU 性能、更先進的量化技術和最先於 mainstream llama.cpp 出現的 LLM 推論功能。

## 核心特性

### 1. 量化技術創新

#### 1.1 新增量化類型

**Trellis 量化** (`IQ1_KT`, `IQ2_KT`, `IQ3_KT`, `IQ4_KT`)
- 基於新型整數基數網格結構
- 實現於 CUDA、Metal、NEON 和 CPU
- 在 CPU 上達到合理的性能表現

**IQK 量化** 系列：
- `IQ2_K`, `IQ3_K`, `IQ4_K`, `IQ5_K`, `IQ6_K`
- `IQ1_S_R4`, `IQ1_M_R4`, `IQ2_KS`, `IQ2_KS_R4`
- `IQ3_KS`, `IQ4_KS`, `IQ4_KSS`, `IQ5_KS`, `IQ5_KS_R4`
- `IQ4_K_R4`, `IQ5_K_R4`, `IQ2_K_R4`, `IQ3_K_R4`
- 支援 Zen4、AVX2、ARM_NEON 架構

**其他量化改進**：
- `IQ1_M`, `IQ2_XS`, `IQ2_KL`
- `Q2_K`, `Q4_K`, `Q5_K`, `Q4_1`, `Q5_1`, `Q4_0`, `Q5_0`, `Q6_0`, `Q3_K`, `Q6_K`
- `Q8_KV` - 8 位 KV 快取量化
- `IQ4_XS`, `IQ4_NL`

#### 1.2 量化性能優化

- 所有非交叉量化類型在 CPU 上的提示處理速度大幅提升
- 所有量化類型均支援 CUDA 量化矩陣乘法核
- Trellis 量化和 MoE 模型的 CPU 提示處理加速
- MXFP4 量化支援（用於 gpt-oss 模型）

### 2. 架構特性

#### 2.1 推理加速技術

- **MLA (Multi-Head Latent Attention)** - 多頭潛在注意力機制
- **FlashMLA** - 結合 Flash Attention 的 MLA 實現
- **Flash Attention** - 用於 GQA 模型的 GPU 加速
- **Fused Delta-Net (Fused Gated Delta Net)** - 用於 Qwen3-Next 和 Qwen3.5-MoE
- **Quant Repacking** - 量化重打包技術
- **Hadamard 變換** - 用於 K 快取和 V 快取

#### 2.2 多 GPU 和 MoE 支援

- **Tensor Parallel (TP)** - 張量平行處理
- **MTP (Multi-Token Parallel)** - 多 token 並行
- **DFlash** - 初始支援
- **DSpark** - 初始支援
- **Smart Expert Reduction** - 更快速的 DeepSeek 推論
- **Auto-fit offloaded tensors** - 自動適應可用 VRAM 的離載張量

### 3. 模型支援

支援的模型包括：

- LLaMA-3-Nemotron
- Qwen3 (包括 Qwen3-VL)
- GLM-4, GLM-4.5, GLM-4.6, GLM-4.7, GLM-5
- Command-A
- DeepSeek-V3, DeepSeek-V4
- Kimi-2
- dots.llm1
- Hunyuan
- Gemma3, Gemma4
- Mistral 4
- Ernie 4.5 MOE
- grok-2
- Ling/Ring (Bailing-MoE2)
- 以及更多...

### 4. 功能增強

- **函數呼叫支援** - 完整的 API 端點
- **Jinja 模板支援** - 用於提示工程
- **多模態視覺支援** - 在 `llama-mtmd-cli` 和 `llama-server` 中
- **OpenAI /v1/responses API** - 完整 API 相容性
- **適應性-P 採樣器** - 由原作者設計的採樣器
- **自 speculative 解碼** - ngram 和 suffix 支援
- **圖形平行模式 (graph)** - 用於多 GPU 設置

### 5. 後端支援

- **CPU** - AVX2 或更高級別，ARM_NEON 或更高級別
- **CUDA** - Turing 或更新版本
- **Metal** (有限支援)
- **注意**：ROCm、Vulkan、舊版 NVIDIA GPU 的支援有限

## 重要注意事項

### ⚠️ 混合 CPU/GPU MoE 推理警告

對於 MoE 模型，當部分專家留在 CPU 上時，**不要使用 `-rtr` 選項**，除非您完全了解其影響：

- `-rtr` 選項會將所有留在 RAM 中的張量重新打包為行間隔格式
- 並非所有量化類型都有 CUDA 行間隔實現
- 這會導致這些張量的矩陣乘法**永遠在 CPU 上執行**，即使 GPU 處理會更快
- 特別影響 k-量化類型（K2_K, Q3_K, Q4_K, Q5_K, Q6_K）

### ⚠️ Unsloth 模型兼容性

避免使用 Unsloth 名稱中包含 `_XL` 的量化模型，這些模型可能無法正常工作（特別是包含 f16 張量的模型）。

### ⚠️ 圖形平行問題

在使用圖形平行模式（split mode `graph`）和部分 GPU 卸載時，某些用戶報告了無意義回答的問題。建議添加 `-cuda graphs=0` 來解決。

## 快速開始

### 安裝

```bash
git clone https://github.com/ikawrakow/ik_llama.cpp
cd ik_llama.cpp
apt-get update && apt-get install build-essential git libcurl4-openssl-dev curl libgomp1 cmake
```

### 編譯

**CPU 編譯**：
```bash
cmake -B build -DGGML_NATIVE=ON
cmake --build build --config Release -j$(nproc)
```

**GPU 編譯**：
```bash
cmake -B build -DGGML_NATIVE=ON -DGGML_CUDA=ON
cmake --build build --config Release -j$(nproc)
```

### 運行

```bash
./build/bin/llama-server --model <model.gguf> --ctx-size 4096
```

或 GPU 加速：
```bash
./build/bin/llama-server --model <model.gguf> --ctx-size 4096 -ngl 999
```

### Docker 支援

```bash
docker pull ghcr.io/ikawrakow/ik-llama-cpp:cpu-server
docker pull ghcr.io/ikawrakow/ik-llama-cpp:cu12-server
```

## 技術亮點總結

1. **最先端的量化技術** - Trellis 和 IQK 量化系列領先 mainstream llama.cpp
2. **優化的 CPU 性能** - AVX-512 專為 CPU 設計，支援 IQK 量化 GEMM 核
3. **先進的架構技術** - MLA、FlashMLA、Flash Attention 實現
4. **廣泛的模型支援** - 支援最新和最大的開源模型
5. **完整的 API 相容性** - OpenAI API 端點、函數呼叫、多模態支援
6. **多平台支援** - Linux、Windows、Docker、Android

## 資源

- 維基頁面：https://github.com/ikawrakow/ik_llama.cpp/wiki
- 性能比較：https://github.com/ikawrakow/ik_llama.cpp/wiki
- 開發文檔：https://github.com/ikawrakow/ik_llama.cpp/docs
- Docker 指南：https://github.com/ikawrakow/ik_llama.cpp/docs/docker.md