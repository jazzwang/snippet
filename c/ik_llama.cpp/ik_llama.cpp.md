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
