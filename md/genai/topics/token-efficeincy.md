# LLM Token Usage Efficiency of different AI Code Agents

## 2026-07-09

- 緣起：同仁分享 Benchmarking Coding Agents on Databricks’ Multi-Million Line Codebase
  - https://www.databricks.com/blog/benchmarking-coding-agents-databricks-multi-million-line-codebase
  - 提到 Pi harness 比較省 token
  <img src='https://www.databricks.com/sites/default/files/inline-images/pareto.png?v=1783530297'>
  <img src='https://www.databricks.com/sites/default/files/inline-images/dumbell.png?v=1783530297'>
- 查證：
  - 是否有其他研究結果也存在類似的結論呢？

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI Mode
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
are there study on token effeciency of different AI Code Agent CLI, such as Claude Code, Github Copilot, OpenClaw, Hermus Agent, Pi Agent, OpenCode?
</td></tr><tr><td>A:</td><td>

Yes, multiple comparative studies, academic benchmarks, and community tests track the token efficiency of these AI command-line interfaces (CLIs). [1, 2]

A foundational study from the [Stanford Digital Economy Lab](https://digitaleconomy.stanford.edu/publication/how-do-ai-agents-spend-your-money-analyzing-and-predicting-token-consumption-in-agentic-coding-tasks/) highlighted that autonomous code agents consume up to 1,000x more tokens than simple code autocomplete tools. This massive burn rate is driven by input context (swapping files, checking errors, and re-reading codebases) rather than output code generation. [3, 4, 5]
Because token efficiency translates directly to project costs and execution speeds, the architecture of an agent CLI heavily determines its token footprint. [6, 7]

### Comparative Breakdown: Token Management Across Agent CLIs

| Agent CLI | Baseline Token Usage Trend | Core Context Management Mechanism | Best Suited For |
|---|---|---|---|
| Pi Agent | 🟢 Lowest (Highly Optimized) | Strict AgentMessage conversion & aggressive history pruning. | Local LLMs and resource-constrained environments. |
| Hermes Agent | 🟡 Medium-Low (Decreases over time) | Automated self-learning loops; condenses actions into lightweight reusable skills. | Long-term automation & routine developer operations. |
| OpenCode | 🟡 Medium (Configurable) | Stripped-down architecture; users must explicitly add tools to avoid system prompt bloat. | Privacy-centric developers using self-hosted open-source models. |
| Claude Code | 🔴 High (Dense reasoning overhead) | 1-million-token window; manages context using structural graph summaries and Grep. | Deep architectural changes & multi-file repository refactoring. |
| OpenClaw | 🔴 High (Unfiltered search loops) | Post-execution truncation; trims oversized tool responses after the token expense is incurred. | Complex cross-model orchestrations with deep customization. |
| GitHub Copilot CLI | Variable (Billing-dependent) | Batching multiple tool requests into single execution threads (copilot-codeact-plugin). | Day-to-day inline assistance and native GitHub workflows. |

### Key Findings on Specific Agents

#### 1. Pi Agent & OpenCode: The Local LLM Champions

In tests evaluating local developer footprints, such as data compiled on the [r/LocalLLM community](https://www.reddit.com/r/LocalLLM/comments/1tebx71/those_who_use_it_why_open_code_over_pi_and_hermes/), Pi Agent consistently emerges as the least token-hungry framework. It uses a specific code architecture (pi-agent-core) that processes internal configurations using custom message structures, converting them to standard LLM tokens only at the absolute boundary of an API call. Similarly, developer benchmarks show that stripping OpenCode down into a custom "minimal agent" layout can slash baseline token consumption by up to 96% by eliminating unnecessary system prompts. [8, 9, 10]

#### 2. Hermes Agent vs. OpenClaw: Structural vs. Reactive Savings

Independent evaluations emphasize a sharp philosophical divide in how these two open-source frameworks manage tokens: [11, 12]

* Hermes Agent features a specialized "Curator" loop. The first time it tackles a problem, token usage is standard. However, it immediately writes its solution into a condensed "Procedural Memory Skill". On subsequent repetitions, it calls that lightweight skill directly, reducing recurring token costs significantly. [12, 13, 14]
* OpenClaw relies on a reactive method. When using code search tools, it frequently dumps unranked, massive chunks of files into the context window. While it utilizes hooks (transformContext) to compress old chat history, it does so after the initial expensive token query has already been executed and billed. [15, 16]

#### 3. Claude Code: Maximizing Context via Knowledge Graphs [17]

While Claude Code boasts a massive 1-million-token context window capable of loading entire repositories, it can easily burn through heavily metered plans during long sessions. To combat this, developers frequently use open-source indexers like Graphify or Code-Graph. These tools map out repository structures into pre-indexed knowledge graphs. Instead of Claude Code scanning whole files to understand codebase relationships, it reads the dense graph guide—cutting ambient token consumption by up to 60%–95%. [18, 19, 20, 21, 22]

#### 4. GitHub Copilot CLI: Message-Based Optimization

Copilot CLI is unique because of its hybrid billing strategy. Historically insulated by flat-rate subscriptions, recent optimization frameworks for Copilot rely heavily on tool collapsing. Using techniques like the `copilot-codeact-plugin`, the CLI strings sequential shell instructions together before querying the backend, avoiding the repetitive token overhead of back-and-forth prompt cycles. [3, 18, 23, 24, 25]

### Hidden Metric: The Clean Code Premium

A notable study by SonarSource quantified a critical human factor in agent efficiency. In a controlled trial of 660 agent execution paths, researchers discovered that clean basecode structures make AI agents roughly 34% more efficient. Well-maintained, modular repositories minimized file-revisitations by the agents, reducing context-window refresh cycles and trimming baseline token overhead by 7% to 8% without any changes to the agent software itself. [26]

Would you like details on how to set up context compression tools for a specific CLI, or are you looking to optimize a local model setup?

[1] [https://medium.com](https://medium.com/@unicodeveloper/10-must-have-clis-for-your-ai-agents-in-2026-51ba0d0881df)
[2] [https://link.springer.com](https://link.springer.com/chapter/10.1007/978-3-032-01402-3_26)
[3] [https://dev.to](https://dev.to/webmaxru/a-practitioners-guide-to-getting-more-value-out-of-ai-coding-agent-quality-token-optimization-3n7j)
[4] [https://digitaleconomy.stanford.edu](https://digitaleconomy.stanford.edu/publication/how-do-ai-agents-spend-your-money-analyzing-and-predicting-token-consumption-in-agentic-coding-tasks/)
[5] [https://davefriedman.substack.com](https://davefriedman.substack.com/p/nobody-reads-the-tokens)
[6] [https://medium.com](https://medium.com/@nprasads/token-efficiency-in-ai-coding-agents-12d4e3b00f00)
[7] [https://medium.com](https://medium.com/@jakenesler/context-compression-to-reduce-llm-costs-and-frequency-of-hitting-limits-e11d43a26589)
[8] [https://www.reddit.com](https://www.reddit.com/r/LocalLLM/comments/1tebx71/those_who_use_it_why_open_code_over_pi_and_hermes/)
[9] [https://zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/2043727154320499415)
[10] [https://www.youtube.com](https://www.youtube.com/watch?v=FX7jcd3GYtI&t=439)
[11] [https://latenode.com](https://latenode.com/blog/openclaw)
[12] [https://www.linkedin.com](https://www.linkedin.com/posts/brandonkellyrx_ai-development-agents-activity-7457082945074429952-Zhzh)
[13] [https://www.youtube.com](https://www.youtube.com/watch?v=86Dfgazdu-0)
[14] [https://www.youtube.com](https://www.youtube.com/watch?v=jOK10k70XWE&t=164)
[15] [https://milvus.io](https://milvus.io/blog/why-ai-agents-like-openclaw-burn-through-tokens-and-how-to-cut-costs.md)
[16] [https://medium.com](https://medium.com/@techlatest.net/openclaw-agent-masterclass-66d6a4f88cd5)
[17] [https://www.instagram.com](https://www.instagram.com/reel/DZUjy7ISS0i/)
[18] [https://www.reddit.com](https://www.reddit.com/r/GithubCopilot/comments/1rttkzw/claude_code_vs_github_copilot_limits/)
[19] [https://kilo.ai](https://kilo.ai/articles/top-ai-coding-agents)
[20] [https://www.instagram.com](https://www.instagram.com/reel/DY0cOXvNI9O/)
[21] [https://www.linkedin.com](https://www.linkedin.com/posts/hafshari_github-juliusbrusseecaveman-why-use-activity-7470677242168098816--XfP)
[22] [https://tech-insider.org](https://tech-insider.org/claude-code-vs-github-copilot-2026/)
[23] [https://www.youtube.com](https://www.youtube.com/watch?v=UMRUu7pjdug)
[24] [https://windowsforum.com](https://windowsforum.com/threads/github-copilot-ai-credits-usage-based-billing-starts-june-1-2026.415470/)
[25] [https://calvinfo.substack.com](https://calvinfo.substack.com/p/the-coding-agent-metagame)
[26] [https://www.developersdigest.tech](https://www.developersdigest.tech/blog/code-cleanliness-affects-ai-coding-agents)

</td></tr>
</table>

## 2026-07-13

- 2026-07-12
  - Claude Code Is Way More Token-Hungry Than OpenCode. We Measured Exactly How Much
  - https://systima.ai/blog/claude-code-vs-opencode-token-overhead
  - 測驗工具：https://github.com/systima-ai/agentic-coding-tools-comparison

## 2026-09-14

> [!NOTE]
> - title: "I Cut My OpenCode Token Usage by 96%  - Here's How"
> - source: https://www.youtube.com/watch?v=FX7jcd3GYtI
> - created: 2026-09-14
> - notebooklm: Harness
> - report-id: e2a398cb-d5c4-41a0-bb50-28e020197888

## 為什麼說聲「你好」要花 8,000 個 Token？OpenCode 隱藏成本大揭密與 96% 節省策略

### 一個價值 8,000 Token 的招呼語：當 UI 糖衣變成帳單負擔

想像一下，你在當紅的 AI 寫程式工具 OpenCode 中輸入一個簡單的「hello」。你既沒有要求它重構複雜的遺留程式碼，也沒有請它從零構建一個 React 組件。然而，透過底層監測發現，這一個簡單的招呼，在背後竟然消耗了高達 8,000 個 Token。

這並非發生在複雜的開發場景，而僅僅是初始化階段。這 8,000 個 Token 相當於 8 到 10 頁的 A4 紙張內容。作為一名 AI 效能優化專家，我必須直言：**Token 就是金錢，更是珍貴的上下文空間。** 本文將透過可觀測性（Observability）技術，揭開 OpenCode 運作背後的「Prompt Overhead」，並分享如何透過精簡的代理工程，將 Token 用量大幅削減 96%。

### 偵探工具箱：如何看穿 LLM 背後的傳輸細節

要優化效能，第一步必須實現完全的透明化。

1.  **失效的方案 A：內建 OpenTelemetry**
    OpenCode 雖然提供了實驗性的 OpenTelemetry 支援，但對於效能優化者來說極其雞肋。它能記錄 HTTP 狀態碼與延遲，卻完全無法提供 Token 消耗細項，更看不見具體的 Prompt 內容與工具定義（Tool Definitions）。

2.  **成功的方案 B：MITM Proxy 與自定義攔截腳本**
    我最終採用了 **MITM Proxy（中間人代理）**。這個工具攔截了 OpenCode 與 LLM 伺服器之間的所有通訊。我撰寫了一段約 40 行的 Python 腳本，專門捕捉所有 `system role` 的請求與回應，將其轉存為 JSON。這讓我們能以「上帝視角」檢視模型（本案例使用 **MIMO 2.5**）到底接收了什麼。

### Token 消失的真相：兩階段的隱形成本

數據顯示，當你輸入 "hello" 時，OpenCode 實際上發送了兩次獨立的請求。

#### 第一階段：代價昂貴的「UI 糖衣」

在你收到回應前，OpenCode 會先自動發送一次請求，僅為了替這段對話產生一個標題。

> **這是一個極其諷刺的發現：** OpenCode 消耗了約 500 個 Prompt Token 與 1,500 個 Completion Token，僅為了在視窗頂端顯示一個詞：**"Greeting"**。在真正的對話開始前，2,000 個 Token 已付諸流水。

#### 第二階段：巨大的「支架（Scaffolding）」與系統提示詞

當真正的 "hello" 被送出時，模型接收到的是一個臃腫不堪的封包。我們來算一下這筆帳：

*   **系統提示詞（System Message）：** 約 9,500 個字元。包含行為準則、格式規範、甚至詳細到規定 AI 該使用哪些表情符號。
*   **工具定義（Tool Definitions）：** OpenCode 預設附帶 11 個工具的完整 JSON Schema。
    *   **Bash 工具（4,700 字元）：** 詳細描述了作業系統環境、Shell 指令規則、目錄驗證步驟及引號處理慣例。
    *   **Task 工具（3,000 字元）：** 定義了如何委派子代理（Sub-agents）任務的複雜邏輯。
    *   **Edit 與 Read 工具：** 各佔約 1,000 字元以上的參數說明。

**核心數學計算：**

9,500 字元的系統提示 + 超過 10,000 字元的工具定義 $\approx$ 20,000+ 字元。按照「4 字元 $\approx$ 1 Token」的通則計算，這正是那 5,000 至 8,000 個 Token 的來源。

> **關鍵統計數據：** 使用者輸入的 "hello"（5 個字元）僅佔總傳輸數據量的 **0.025%**。其餘 99.975% 全是為了讓 AI 維持運作的支架資訊。

### 破解迷思：為什麼快取（Caching）救不了你？

開發者常有一種誤解：「既然有快取，這些重複的 System Prompt 應該不花錢吧？」
事實上，快取是 **供應商的優化**，而非使用者的。

1.  **傳輸延遲與頻寬：** 無論是否快取，這 8,000 個 Token 每次都必須從你的筆電傳送到雲端，這造成了不必要的延遲。
2.  **Context Window Bloat（上下文視窗膨脹）：** 這些 Token 依然佔用了模型有限的上下文空間。如果你在處理大型專案，這 8,000 個 Token 可能就是導致模型「忘記」前面程式碼的最後一根稻草。
3.  **環境成本：** 處理如此龐大的冗餘數據，背後的電力損耗與碳足跡亦不容忽視。

### 實戰優化：建立自定義輕量代理 (Custom Agents)

OpenCode 的 `build` 代理之所以臃腫，是因為它想做「全能助手」。但 90% 的時間，你不需要 MCP Servers 或複雜的 Bash 工具。

**優化步驟：**

1.  **建立目錄：** 在專案根目錄下建立 `open code/agents/` 資料夾（請注意目錄名稱包含空格）。
2.  **建立檔案：** 建立一個名為 `agentx.md` 的 Markdown 檔案。
3.  **置入極簡指令：** 拷貝以下結構以取代預設的百行提示詞：

```markdown
---
name: Agent X
model: mimo-2.5
temperature: 0
primary: true
---

You are a minimalist coding assistant.
You have access to NO tools.
Respond concisely to user questions.
```

透過將 `primary` 設為 `true`，你可以利用 Tab 鍵在 OpenCode 中快速切換到這個極簡環境。

### 成果對比：極簡主義的威力

| 項目 | 預設 Build 代理 | 自定義 Agent X | 改善幅度 |
| :--- | :--- | :--- | :--- |
| **Token 消耗** | 約 8,000 | 300 - 500 | **~96% 節省** |
| **Context Window 佔用** | 高 (10+ 頁 A4) | 極低 (幾行字) | 大幅釋放空間 |
| **API 成本** | 全額支付 (含快取折扣) | 忽略不計 | **極大幅降低** |
| **工具功能** | 11 種工具 (全功能) | 無工具 / 按需添加 | 視需求動態調整 |

### 結論與核心行動建議

這不是魔術，而是「代理工程（Agent Engineering）」與「可觀測性」的具體實踐。我們不需要為了修剪一個指甲而啟動一整台重型機械。

**給開發者的行動清單：**
1.  **透明化：** 永遠了解你的 IDE 究竟偷偷發送了什麼。
2.  **按需添加（Start Minimal）：** 預設使用 Agent X 處理日常對談，僅在需要執行 Bash 或讀取檔案時，才切換到功能完整的代理。
3.  **剝離冗餘：** 90% 的任務不需要 MCP Servers 或複雜的子代理邏輯，果斷移除它們。

掌握了這些技巧，你將擁有更快的反應速度與更精確的對話脈絡。在下一篇文章中，我將探討「Orchestrator 模式」——如何透過一個中控代理來動態調度這些輕量代理，進一步優化複雜專案的開發成本。