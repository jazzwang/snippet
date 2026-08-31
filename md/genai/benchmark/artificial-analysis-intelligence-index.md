# Artificial Analysis Intelligence Index

- https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index
  - 還蠻常看到的模型評測指標，特別是最近在比較不同模型能力與 Token 成本的時候
- 方法論：
  - Artificial Analysis Intelligence Benchmarking Methodology
  - https://artificialanalysis.ai/methodology/intelligence-benchmarking

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Gemini Live Chat
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
幫我生成中文摘要 https://artificialanalysis.ai/methodology/intelligence-benchmarking#artificial-analysis-intelligence-index
</td></tr><tr><td>A:</td><td>

[Artificial Analysis Intelligence Index v4.1.1](https://artificialanalysis.ai/methodology/intelligence-benchmarking#artificial-analysis-intelligence-index) 是由 Artificial Analysis 建立的語言模型智力評測框架，結合 9 項基準測試來評估 AI 在推理、知識、數學與程式設計等面向的綜合能力，重點偏重於 Agent（代理人）任務。

**四大評測類別與權重**

* **Agents 代理任務 (34%)**：包含 GDPval-AA v2 (20%) 與 $\tau^3$-Banking (14%)，測試 AI 在複雜環境下的文件產出、資料檢索與雙向代理模擬能力。
* **Coding 程式編程 (24%)**：包含 Terminal-Bench v2.1 (16%) 與 SciCode (8%)，評估終端機指令執行與科學計算程式碼寫作。
* **Scientific Reasoning 科學推理 (24%)**：包含 Humanity's Last Exam (12%)、GPQA Diamond (6%) 與 CritPt (6%)，測試高難度的跨學科科學推理與符號運算。
* **General 通用能力 (18%)**：包含 AA-Omniscience (12%) 與 AA-LCR (6%)，衡量模型回答的準確度、幻覺抑制率與長文本理解力。

**核心評測原則**

* **標準化與零樣本 (Zero-Shot)**：所有模型皆在一致的條件下測試，不給予範例（Few-shot），直接檢驗模型理解並執行指令的能力。
* **客觀與透明**：結合測試集比對與專家模型（LLM Judge）評分，並完全公開提示詞範本與測試條件。

**測試參數與環境**

* **溫度（Temperature）設定**：一般模型設定為 0；推理型模型設定為 0.6。
* **執行環境與計分**：程式評測統一於 Ubuntu 22.04 LTS / Python 3.12 環境運行，計分主要採用 pass@1（首次嘗試正確率）。

</td></tr>
</table>

## 2026-08-31

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI Mode
</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
我可以自己跑 benchmark 並貢獻回 https://artificialanalysis.ai/agents/coding-agents 嗎?
</td></tr><tr><td>A:</td><td>

你無法直接將自己跑的跑分數據（Log 或分數）直接上傳、Commit 或自動貢獻回 [Artificial Analysis Coding Agent 排行榜](https://artificialanalysis.ai/agents/coding-agents)。 [1, 2] 

因為 Artificial Analysis（AA）是一個獨立的第三方評測機構。為了保證排行榜的公信力、防止廠商或社群造假（Data Contamination），他們所有的核心排行榜數據都是由 AA 官方在標準化的受控環境中自行運行、獨立審計並發布的。 [3, 4, 5, 6] 

不過，如果你是開源 Agent 的開發者、有自己獨特的優化設定，或者希望推薦新的 AI 智能體上榜，你依然可以透過以下幾種「間接方式」參與和貢獻：

### 1. 聯繫官方申請將你的 Agent 納入評測

如果你自己開發了一個 Coding Agent（或是某個開源專案的大幅優化版本），你可以透過 Artificial Analysis 網站底部的 Contact 頁面或其官方 X（Twitter）帳號聯繫他們。

* 你需要提供：Agent 的開源儲存庫（Repository）、具體的架構說明、API 調用設定，以及可在標準化環境（如 Docker）中重現的部署指南。
* 官方審查：若他們評估該 Agent 具有社群關注度或技術創新性，AA 團隊會親自使用他們的測試座（Harness）來為你的 Agent 跑分並上榜。

### 2. 本地自行運行組成該 Index 的三大開源基準測試

雖然不能直接上榜，但 [Coding Agent Index](https://artificialanalysis.ai/zh/methodology/coding-agents-benchmarking) 的組成成分是由三個公開的 Benchmark 構成的： [1] 

* DeepSWE：專注於真實軟體工程任務（包含 113 個任務）。
* Terminal-Bench v2：評估 Agent 在終端機/命令列的操作能力（包含 89 個任務）。
* SWE-Atlas-QnA：測試技術問答與程式碼理解（包含 124 個任務）。 [1] 

你可以到這些基準測試的 GitHub 官方開源專案中，依據他們的規範在本地跑分。如果你在執行過程中發現了 Benchmark 題目本身的 Bug（例如測試案例寫錯、環境壞掉），你可以向這些 Benchmark 的原作者提交 Pull Request (PR)。當基準測試更新後，Artificial Analysis 未來重新跑分時也會採用。

### 3. 利用官方推出的開源基礎設施（如 Pipette）

如果你對硬體或端到端（On-device）的 AI 表現有興趣，Artificial Analysis 與 Liquid AI 合作開源了名為 [Pipette](https://www.liquid.ai/blog/pipette-on-device-ai-benchmarking-by-liquid-ai) 的評測基礎設施。 [7] 

* 他們推出了採用 Apache 2.0 授權的開源評測客戶端與架構。
* 針對這一類特定專案，官方有開放 Community-submitted results（社群提交結果） 的 Beta 測試。你可以留意未來這套機制是否會全面擴展到 Coding Agent 的區塊。 [7] 

請問你目前是想測試自己開發的 Coding Agent，還是只是想幫某個現有的開源 Agent（例如 Aider、Cline） 跑出最新模型的數據呢？我可以為你提供對應的本地跑分工具或指南。

[1] [https://artificialanalysis.ai](https://artificialanalysis.ai/agents/coding-agents)
[2] [https://benchlm.ai](https://benchlm.ai/blog/posts/ai-coding-agents)
[3] [https://github.com](https://github.com/SAILResearch/awesome-ai-leaderboard)
[4] [https://www.facebook.com](https://www.facebook.com/will.fans/posts/ai-%E5%88%B0%E5%BA%95%E8%83%BD%E4%B8%8D%E8%83%BD%E5%8B%9D%E4%BB%BB%E5%B0%88%E6%A5%AD%E7%9A%84%E6%95%B8%E6%93%9A%E5%88%86%E6%9E%90%E5%B7%A5%E4%BD%9C%E9%97%9C%E9%8D%B5%E5%BE%80%E5%BE%80%E4%B8%8D%E5%9C%A8%E6%96%BC%E5%AE%83%E5%81%B6%E7%88%BE%E8%83%BD%E7%AE%97%E5%B0%8D%E4%B8%80%E6%AC%A1%E8%80%8C%E6%98%AF%E5%9C%A8%E6%96%BC%E5%AE%83%E8%83%BD%E5%90%A6%E6%AF%8F%E4%B8%80%E6%AC%A1%E9%83%BD%E7%B6%AD%E6%8C%81%E9%9B%B6%E5%A4%B1%E8%AA%A4%E8%A9%95%E6%B8%AC%E6%A9%9F%E6%A7%8B-artificial-analysis-%E6%9C%80%E8%BF%91%E6%8E%A8%E5%87%BA%E4%BA%86/1514093580744726/)
[5] [https://artificialanalysis.ai](https://artificialanalysis.ai/zh/methodology/coding-agents-benchmarking)
[6] [https://captain-balung-blog.ghost.io](https://captain-balung-blog.ghost.io/how-to-fairly-benchmark-an-ai-coding-agent/)
[7] [https://www.liquid.ai](https://www.liquid.ai/blog/pipette-on-device-ai-benchmarking-by-liquid-ai)

</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
幫某個現有的開源 Agent 如 Aider 或 Pi Coding Agent 跑出最新模型的數據
</td></tr><tr><td>A:</td><td>

想要幫 Aider 或 Pi Coding Agent (pi-coding-agent) 這類現有的開源工具跑出最新模型的數據（例如搭配最新的 GPT-5、Claude 4.6 或 DeepSeek 最新模型），你需要將「Agent 工具本身」與「評測座（Benchmark Harness）」分開來看。 [1] 
因為 Agent 本身只是互動工具，要測出具有統計意義的勝率，必須透過自動化測試座（如官方提供的測試腳本或 SWE-bench / Terminal-Bench 框架）來進行。以下為你整理這兩個熱門 Agent 的本地跑分與評測指南： [1, 2] 

### 一、 幫 Aider 跑最新模型數據

Aider 是目前開源界公認的指標性 AI 補丁與編輯工具。Aider 官方非常注重 Benchmark，並且有完整開源他們自己用的測試座。

#### 1. 執行 Aider 專屬的 Polyglot 基準測試（推薦：快速、成本低）
Aider 官方維護了一個跨語言的程式練習題基準測試。它專門用來測試模型是否能準確輸出 Aider 獨特的「Diff 編輯格式」。

步驟：

1. 複製官方評測儲存庫：git clone https://github.com
   2. 切換到 benchmark 目錄，設定好你的最新模型 API Key（例如 ANTHROPIC_API_KEY 或 OPENAI_API_KEY）。
   3. 執行指令：python -m aider.benchmark.run --model <最新模型名稱>
* 優點：速度快，幾小時內即可跑完，可以立刻知道最新模型在 Aider 格式下的程式碼修改準確率。

#### 2. 執行工業級 SWE-bench 測試（難度高、耗時長）

如果你想測出 Artificial Analysis 或各大 Leaderboard 最看重的 SWE-bench 分數： [2] 

* 工具：你需要使用 [Aider SWE Bench Harness](https://github.com/Aider-AI/aider-swe-bench) 官方開源儲存庫。
* 原理：此測試座會建立一個 Docker 安全沙箱，下載真實的 GitHub Issues 專案，自動調用 Aider 配合你指定的最新模型去解 Bug，並自動執行測試檢查是否修復成功。 [2] 
* 注意：跑一次完整的 SWE-bench Lite 需要測試數百個任務，會消耗數百到數千美元的 API Token 費用，且需要高性能主機跑 Docker，通常不建議個人全量運行，建議挑選其中 10~20 個 Sample 任務進行小規模測試。 [3] 

## 二、 幫 Pi Coding Agent 跑最新模型數據

由 Mario Zechner 開發的 [Pi Coding Agent (pi-coding-agent)](https://pi.dev/) 是目前社群上極其火熱的「極簡主義」終端 Agent（主打核心 Loop 和強大的客製化工具能力）。 [4, 5, 6] 

#### 1. 透過 pi-ai 模組接入最新模型

Pi 的架構中，所有模型的橋接都是透過底層開源的 @earendil-works/pi-ai 模組來規範化。它天生支援超過 15 個 Provider（如 OpenRouter、DeepSeek、Together AI 等）。 [4, 7] 

* 若要測試未原生內建的「最新模型」，你只需要透過 OpenRouter 或 自訂 OpenAI-compatible 網址，並在 SYSTEM.md 或環境變數中指定模型 ID 即可直接讓 Pi 開始運作。

#### 2. 自行測試 Terminal-Bench 任務

在 Artificial Analysis 的評測中，Pi 這一類基於 Terminal/Bash 運作的 Agent 最適合拿來跑 Terminal-Bench（評估在 Linux 終端機下規劃與執行 Shell 的能力）。 [1, 2] 

* 你可以前往 [Terminal-Bench GitHub 專案](https://github.com/) 下載其標準化任務（例如編譯程式碼、設定伺服器、排查問題等）。
* 將 Pi Agent 執行檔放入 Terminal-Bench 的測試沙箱中，使用指令將任務敘述餵給 Pi：

pi "請幫我設定此環境中的 nginx 以進行 TLS 終端，並確認服務重啟正常"

* 執行完成後，跑 Terminal-Bench 的評分腳本，檢查 Pi 產出的系統狀態（Exit Code 或檔案 Diff）是否符合預期。 [1, 8] 

## 三、 本地跑分的重要注意事項 ⚠️

1. 環境隔離與安全（最重要）：
Coding Agent 具備「執行終端機指令（Bash/Tool Call）」的能力。不論是 Aider 的測試座還是 Pi Agent，請絕對不要直接在你的工作電腦（Host 主機）上盲目跑 Benchmark。AI 模型在解題時可能會誤刪檔案或執行危險指令。必須全程在 Docker 容器或獨立的虛擬機（VM）內運行。
2. API 費用控管：
最新模型（尤其是推理解模型）的 Input/Output Token 費用通常很高。Agent 在 Benchmark 中會不斷進行「思考 → 執行 → 看報錯 → 再思考」的循環（Loop）。建議在指令中加入限制單次最大 Token 或最大迭代次數，避免 AI 陷入無窮迴圈導致信用卡被刷爆。 [3, 9, 10] 
3. 紀錄（Logging）與可觀測性：
跑分時記得開啟 Aider 的 --analytics 或使用像 Opik 這類的開源 LLM 觀測平台來記錄每一筆 Tool Call 和 Token 消耗。即使這些數據不能直接同步到排行榜，你也可以將「最新模型在現有 Agent 上的表現與不完美 Diff」整理成 GitHub Issue 或部落格，這對開源社群來說是非常有價值的貢獻。 [9] 

你想先從 Aider 的 Polyglot 快速測試開始動手，還是想了解如何設定環境變數讓 Pi Agent 接入自訂的最新模型 API 呢？我可以提供具體的終端機指令範例。

[1] [https://www.kdnuggets.com](https://www.kdnuggets.com/top-10-open-source-benchmarks-for-ai-coding-agents-in-2026)
[2] [https://nerdstool.com](https://nerdstool.com/blog/top-10-open-source-benchmarks-for-ai-coding-agents-in-2026)
[3] [https://blaxel.ai](https://blaxel.ai/blog/llm-coding-benchmarks)
[4] https://pi.dev
[5] https://pi.dev
[6] [https://daily.dev](https://daily.dev/posts/building-pi-in-a-world-of-slop-mario-zechner-jevewaayg)
[7] [https://github.com](https://github.com/earendil-works/pi)
[8] [https://www.npmjs.com](https://www.npmjs.com/package/@mariozechner/pi-coding-agent)
[9] [https://www.decodingai.com](https://www.decodingai.com/p/building-a-coding-agent-from-scratch-system-design)
[10] [https://aimultiple.com](https://aimultiple.com/ai-coding-benchmark)

</td></tr>
</table>