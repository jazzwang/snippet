# Live Bench

- Git Repo
  - https://github.com/livebench/livebench
- Website
  - https://livebench.ai/#/

> [!INFO]
> LiveBench: A Challenging, Contamination-Free LLM Benchmark

## 2026-08-31

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI Mode
</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
我可以自己用 https://github.com/livebench/livebench 跑新模型的 benchmark 並回饋給 livebench?
</td></tr><tr><td>A:</td><td>

是的，你可以自己下載並運行 LiveBench 來測試新模型。 [1, 2] 

[LiveBench 的 GitHub 儲存庫](https://github.com/livebench/livebench)是一個開源項目，設計的目的之一就是讓研究人員與開發者可以自行驗證分數，或接入自定義的模型 API 進行跑分。 [1, 2] 

關於運行測試與回饋數據的具體運作方式如下：

### 🛠️ 如何自己跑新模型 Benchmark

1. 建立環境：建議使用虛擬環境（如 conda 或 venv），並複製安裝專案依賴。
2. 設定 API / 模型路徑：你可以透過專案支援的框架（如 vLLM）載入本地開源模型，或填入你新模型的 API 密鑰與 Endpoint。
3. 執行腳本：運行 python run_livebench.py 來對模型進行自動化評測。
4. 檢視結果：評測完成後，使用 show_livebench_result.py 來計算並呈現該模型在數學、寫程式、推理等各大維度的客觀得分。 [1, 3] 

### 📊 如何將結果回饋給 LiveBench 官方？

LiveBench 官方排行榜（livebench.ai）的更新與維護主要由發起團隊（Abacus AI）主導。如果你測試了新模型並希望官方納入排行榜，通常有以下幾種回饋管道： [4] 

* 提交 Issue 或 Pull Request (PR)：在 GitHub 上提交 PR，附上你測試新模型所產生的完整結果 JSON 檔案（包含每個子任務的得分詳情），並說明該模型的來源與測試環境。
* 聯絡維護團隊：透過 GitHub 頁面上說明的聯繫方式，或直接向 Abacus AI 的 LiveBench 負責人團隊提交模型評測申請。如果是主流的開源新模型，通常很快就會被採納。
* 貢獻新問題（回饋社群）：除了回饋模型分數，你也可以向 LiveBench 貢獻尚未被污染的新測試題目，幫助這個 Benchmark 保持最新狀態。 [1, 2] 

若你想開始動手測試，建議先閱讀 LiveBench GitHub Readme 內的 Installation 與 Running Evaluation 詳細指引。 [1] 

如果你在操作過程中遇到問題，可以告訴我：

* 你打算測試的是本地開源模型（如 Llama、Mistral 變體）還是雲端 API 模型？
* 你在安裝或執行 run_livebench.py 時是否有出現特定的錯誤訊息？

我可以為你提供更具體的指令調整建議！

[1] [https://github.com](https://github.com/livebench/livebench)
[2] [https://blog.minz.li](https://blog.minz.li/posts/ai/benchmark/)
[3] [https://www.datalearner.com](https://www.datalearner.com/benchmarks/livebench)
[4] [https://www.facebook.com](https://www.facebook.com/ihower/posts/%E6%9C%80%E8%BF%91%E7%9A%84%E5%A4%A7%E6%A8%A1%E5%9E%8B%E6%8E%92%E8%A1%8C%E6%A6%9C%E9%99%A4%E4%BA%86%E5%8F%83%E8%80%83-lmsys-chatbot-arena-%E5%A4%96%E6%88%91%E7%9A%84%E6%96%B0%E6%AD%A1%E6%98%AF-livebench-%E8%B7%9F-seal-leaderboards-%E9%80%99%E5%85%A9%E5%80%8B-bench/10161255391418971/)

</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
what's the difference between "Coding" and "Agentic Coding" defined in https://github.com/livebench/livebench?
</td></tr><tr><td>A:</td><td>

Based on the definition and structure used by the [LiveBench benchmark](https://livebench.ai/), the core difference between "Coding" and "Agentic Coding" comes down to how the model interacts with its environment to solve a problem: [1, 2] 

* Coding (Traditional / Static): Measures single-turn, single-pass generation. The model is given a prompt (like a code completion or text-to-code task), and it must emit one finished, complete code block in one shot. The output is then evaluated against hidden, held-out test cases to see if it works. [2, 3, 4] 
* Agentic Coding: Measures multi-turn, iterative problem-solving. Instead of guessing the correct code instantly, the model operates inside a sandbox or dockerized terminal task environment. It must actively use tools (like terminals, files, or languages like Python, JavaScript, and TypeScript) to run code, analyze errors, and rewrite things iteratively until it passes the target goal. [2, 4, 5, 6] 

### Direct Comparison

| Feature | Coding (LiveBench) | Agentic Coding (LiveBench) |
|---|---|---|
| Interaction Style | Single-pass / One-shot | Multi-turn loop / Scaffolding |
| Environment | None (Static text output) | Sandbox / Dockerized terminal tasks |
| Execution Tooling | Handled externally by the evaluator | Controlled natively by the AI model |
| Error Correction | Impossible (Must be right the first time) | Active debugging through trial and error |

### Why This Matters for Performance

As highlighted in user discussions of LiveBench data on platforms like the [AI Agents community on Reddit](https://www.reddit.com/r/AI_Agents/comments/1urc1rf/the_may_2025_sonnet_still_beats_sonnet_5_on/), a model can rank exceptionally high in standard Coding but crash severely in Agentic Coding. [4] 

For instance, an advanced reasoning model might score heavily on standard coding syntax but fail agentic benchmarks if it gets caught in loop formatting errors or lacks the specific autonomy required to coordinate tool usage across complex workflows. [4, 7] 

If you are interested in exploring how specific AI models compare on these tasks, I can fetch the latest model leaderboard data or break down how LiveBench builds its Python and JavaScript environments. What would you like to explore next?

[1] https://livebench.ai
[2] [https://themodelgap.com](https://themodelgap.com/benchmarks/livebench)
[3] [https://blog.sshh.io](https://blog.sshh.io/p/understanding-ai-benchmarks)
[4] [https://www.reddit.com](https://www.reddit.com/r/AI_Agents/comments/1urc1rf/the_may_2025_sonnet_still_beats_sonnet_5_on/)
[5] [https://arxiv.org](https://arxiv.org/html/2511.20709v2)
[6] [https://codersera.com](https://codersera.com/blog/deepseek-v4-pro-0813-guide-2026/)
[7] [https://www.webfuse.com](https://www.webfuse.com/blog/agentic-coding-in-2026)

</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
改以中文回答
</td></tr><tr><td>A:</td><td>

根據 [LiveBench 基準測試](https://livebench.ai/) 的定義與評分架構，「Coding（傳統編碼）」與「Agentic Coding（智能體/代理編碼）」的核心差異，在於模型如何與環境互動來解決問題：

* Coding（傳統/靜態編碼）： 測試單輪、一次性（Single-pass）的生成能力。系統給予模型一個提示詞（如：代碼補全或文字轉代碼），模型必須在沒有任何執行反饋的情況下，直接產出一段完整的代碼。最後由外部系統運行測試案例來評判對錯。
* Agentic Coding（智能體編碼）： 測試多輪、反覆迭代的解決問題能力。模型會被放置在一個沙盒（Sandbox）或 Docker 化的終端機環境中。它必須主動使用工具（例如：操作終端機、讀寫檔案、執行 Python 或 JavaScript/TypeScript 腳本），根據運行報錯進行自主除錯（Debugging），直到成功達成目標。

### 核心對比表

| 特性 | Coding (傳統編碼) | Agentic Coding (智能體編碼) |
|---|---|---|
| 互動模式 | 單輪輸出 / 一次搞定 | 多輪循環 / 提示詞框架架構 |
| 程式環境 | 無（僅輸出靜態文字） | 沙盒 / Docker 終端機任務環境 |
| 工具執行 | 由外部評測系統執行代碼 | 由 AI 模型親自控制與操作工具 |
| 錯誤修正 | 無法修正（必須一次就寫對） | 透過反覆測試與錯誤訊息自主除錯 |

### 為什麼這個區分很重要？

在 LiveBench 的實際數據中，這兩項指標展現出截然不同的結果。有些推理模型在標準的 Coding（語法、演算法邏輯）分數極高，但在 Agentic Coding 上卻表現不佳。

這是因為「寫出一段正確的代碼」與「在真實電腦環境中，像工程師一樣切換檔案、看報錯日誌、逐步修復 Bug」是完全不同的能力。後者極度考驗 AI 是否具備長文本的邏輯規劃，以及在工具調用（Tool Calling）時不發生格式錯誤的自主能力。

如果你有興趣，我可以為你查詢 LiveBench 當前最新的模型排行榜數據，或是進一步解說它如何構建 Python 和 JavaScript 的測試環境。接下來你想了解哪一部分呢？

</td></tr>
</table>