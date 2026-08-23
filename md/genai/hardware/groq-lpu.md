# Groq LPU

## 2026-08-17

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI Mode
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
groq lpu
</td></tr><tr><td>A:</td><td>

The Groq LPU (Language Processing Unit) is a specialized AI hardware architecture explicitly engineered for ultra-low latency AI inference. Unlike standard GPUs that excel at handling dense, parallel math workloads for model training, the LPU is purpose-built to solve the sequential "token-by-token" bottleneck that slows down generative Large Language Models (LLMs). [1, 2, 3, 4] 
In a massive industry shakeup in December 2025, NVIDIA acquired Groq's core technology and engineering team for $20 billion. This architecture has now been integrated directly into NVIDIA's roadmap, culminating in the official launch of the Groq 3 LPU at GTC 2026. [5, 6] 

## Core Architectural Differences: GPU vs. LPU

| Feature | GPU (Graphics Processing Unit) | Groq LPU (Language Processing Unit) |
|---|---|---|
| Primary Design Focus | Massive throughput for parallel math (AI Training). | Extreme low-latency token generation (AI Inference). |
| Memory Technology | External HBM (High Bandwidth Memory). | On-chip SRAM (Static Random-Access Memory). |
| Execution Model | Dynamic & Non-deterministic (Relies on variable hardware caching). | Static & 100% Deterministic (Operations mapped down to the exact clock cycle). |
| Memory Bandwidth | Up to ~22 TB/s (e.g., NVIDIA Rubin GPU). | Up to 150 TB/s per chip (Groq 3 LPU). |

## Key Architectural Pillars

* SRAM Over HBM: Traditional GPUs use heavy, external High Bandwidth Memory (HBM). While HBM offers massive storage capacity, fetching data from external pools creates a memory-bandwidth bottleneck. Groq utilizes an all-SRAM memory design woven directly onto the silicon fabric next to the compute logic. This eliminates off-chip traffic and allows data to process at blistering speeds. [2, 3, 5, 7, 8] 
* Software-Defined Determinism: Groq strips out complex, unpredictable hardware schedulers and dynamic caches. Instead, a static compiler maps out every single data movement and computation down to the clock cycle before the model even executes. This creates a predictable "programmable assembly line" with virtually zero latency variance. [2, 3] 
* Disaggregated Inference Execution: Because SRAM takes up massive amounts of physical chip space, storing giant models on a single LPU is difficult. The ecosystem handles this by separating operations: calculation-heavy tasks (prefill) run on traditional GPUs, while bandwidth-heavy token generation (decode) runs on networked LPU clusters. [3, 5] 

## The NVIDIA Integration: Groq 3 LPU (2026)

Following its historic transaction to bypass antitrust issues through a team "acquihire" and IP licensing model, NVIDIA moved the architecture from an independent startup to an industry-standard component: [6, 8] 

* The Groq 3 LPU Chip: Manufactured via Samsung’s advanced logic process, each chip features 500MB of embedded SRAM (eSRAM) delivering a phenomenal 150 TB/s of bandwidth. [5] 
* The LPX Rack System: NVIDIA packs 256 of these LPUs into a liquid-cooled LPX Rack System. Operating alongside traditional Vera Rubin NVL72 GPU racks under a unified orchestration engine, it results in up to a 35x performance-per-watt increase for token generation. [5] 
* Long-Term Roadmap: NVIDIA CEO Jensen Huang confirmed that LPU blocks are now a permanent fixture in future designs, with plans already underway to integrate a next-generation LPU (LP40) alongside Rosa CPUs in the 2028 "Feynman" hardware architecture. [5] 

If you'd like to dig deeper, tell me if you want to explore:

* How Groq's compiler maps framework code like PyTorch to deterministic hardware.
* The financial or stock impact on global SRAM supply chain manufacturers.
* A deeper look into how it stacks up against other ASIC inference rivals like Cerebras or SambaNova. [5, 6, 7, 9] 

[1] [https://groq.com](https://groq.com/blog/the-groq-lpu-explained)
[2] [https://www.youtube.com](https://www.youtube.com/watch?v=TKw8kICxJus&t=44)
[3] [https://www.youtube.com](https://www.youtube.com/watch?v=a7wMKgvo8XY&t=519)
[4] [https://www.youtube.com](https://www.youtube.com/watch?v=rHphpyf0i0I&t=305)
[5] [https://www.sinotrade.com.tw](https://www.sinotrade.com.tw/richclub/hotstock/Groq-3-LPU-%E6%98%AF%E4%BB%80%E9%BA%BC-GTC-2026%E6%8F%90%E5%88%B0%E7%9A%84-SRAM-%E7%82%BA%E4%BD%95%E6%88%90-AI-%E6%8E%A8%E8%AB%96%E9%97%9C%E9%8D%B5-%E5%8F%B0%E5%BB%A0%E5%8F%97%E6%83%A0%E8%82%A1%E4%B8%80%E6%AC%A1%E7%9C%8B--%E8%82%A1%E5%B8%82%E8%A9%B1%E9%A1%8C-69b90b3f0aa34962f499e431)
[6] [https://www.fomosoc.com](https://www.fomosoc.com/p/48groqlpunvidia-groq-27nvidiagroq)
[7] [https://www.youtube.com](https://www.youtube.com/watch?v=WQDMKTEgQnY)
[8] [https://www.pocket.tw](https://www.pocket.tw/school/report/SB/6881/)
[9] [https://www.cerebras.ai](https://www.cerebras.ai/blog/cerebras-cs-3-vs-groq-lpu)

</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
改以中文回答
</td></tr><tr><td>A:</td><td>

Groq LPU（Language Processing Unit，語言處理單元） 是一種專為 超低延遲 AI 推理（Inference） 設計的專用硬體架構。
與擅長處理大批次、高平行數學運算（AI 訓練）的傳統 GPU 不同，LPU 是為了突破生成式大型語言模型（LLM）逐字生成（Token-by-Token）的效能瓶頸而誕生。
在 2025 年 12 月的重大產業異動中，NVIDIA（輝達）以 200 億美元收購了 Groq 的核心技術與工程團隊。這項架構現已全面融入 NVIDIA 的產品路線圖，並在 GTC 2026 大會上正式發表了 Groq 3 LPU。

## 核心架構對比：GPU vs. LPU

| 特性 | GPU (圖形處理單元) | Groq LPU (語言處理單元) |
|---|---|---|
| 主要設計核心 | 大吞吐量的平行運算（AI 訓練） | 極低延遲的文字生成（AI 推理） |
| 記憶體技術 | 外部 HBM（高頻寬記憶體） | 晶片內建 SRAM（靜態隨機存取記憶體） |
| 執行模式 | 動態且非確定性（依賴變動的硬體快取） | 靜態且 100% 確定性（運算精準映射至每個時脈週期） |
| 記憶體頻寬 | 最高約 22 TB/s（如 NVIDIA Rubin GPU） | 單晶片最高可達 150 TB/s（Groq 3 LPU） |

## 三大核心架構支柱

* SRAM 取代 HBM： 傳統 GPU 依賴外部的 HBM 晶片，雖然容量大，但從外部頻繁讀取資料會造成記憶體頻寬瓶頸（Memory-Wall）。Groq 則直接在運算邏輯旁織入全 SRAM 記憶體，徹底消除晶片外部的資料傳輸延遲，實現極致的讀寫速度。
* 軟體定義的「確定性」（Determinism）： Groq 拔除了複雜且不可預測的硬體排程器與動態快取。改由靜態編譯器（Compiler）在模型執行前，就將每一步資料移動與運算精準排定到特定的時脈週期（Clock Cycle）。這讓整體運算就像一條完全可控的自動化流水線，幾乎沒有延遲變異。
* 解耦式推理執行（Disaggregated Inference）： 由於 SRAM 極佔晶片物理空間，單顆 LPU 很難塞下龐大的完整模型。現在的硬體生態系採用「術業有專攻」的配置：將重度計算的預填階段（Prefill）交給傳統 GPU，而需要極高頻寬的文字解碼生成階段（Decode）則交給 LPU 叢集高速處理。


## NVIDIA 整合現況：Groq 3 LPU (2026)

NVIDIA 透過「人才收購（Acqui-hire）」與智慧財產權授權模式避開了反壟斷審查，順利將此技術納入正規產品線：

* Groq 3 LPU 晶片： 採用三星先進邏輯製程，每顆晶片內建 500MB 嵌入式 SRAM (eSRAM)，提供驚人的 150 TB/s 頻寬。
* LPX 機櫃系統： NVIDIA 將 256 顆 LPU 封裝進水冷架構的 LPX 機櫃中。它可以與 Vera Rubin NVL72 GPU 機櫃並排運行，透過統一的編排引擎，將模型解碼生成的「每瓦效能比」提升了高達 35 倍。
* 長期路線圖： NVIDIA 執行長黃仁勳已證實 LPU 架構將成為未來的常駐設計。目前已著手計畫在 2028 年推出的「費曼（Feynman）」硬體架構中，將下一代 LPU (LP40) 與 Rosa CPU 進行原生整合。

如果你想進一步了解，可以告訴我你想探討哪一個面向：

* Groq 的編譯器如何將 PyTorch 等框架代碼轉換為硬體的靜態指令。
* 此架構對全球 SRAM 供應鍊廠商帶來的財務與股價影響。
* 它與 Cerebras 或 SambaNova 等其他 AI 推理晶片（ASIC）對手的競爭分析。

</td></tr>
</table>