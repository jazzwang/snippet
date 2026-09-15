# Graphify

- Git Repo
  - https://github.com/safishamsi/graphify
- Website
  - https://graphifylabs.ai/

> AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, and more). Turn any folder of code, SQL schemas, R scripts, shell scripts, docs, papers, images, or videos into a queryable knowledge graph. App code + database schema + infrastructure in one graph.

## 2026-06-22

- 緣起：
  - learn from Jeriel
- 查過平常訂閱的 Newsletter 只出現在 DevPost 一次
- 比較好奇用什麼 Tech Stack 來存 Knowledge Graph
  - SQLite?
  - Neo4j?

## 2026-06-23

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI Mode
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
could you describe the technical stack of graphify https://graphifylabs.ai/? how does graphify store Knowledge Graph? in SQLite? or Neo4j?
</td></tr><tr><td>A:</td><td>

By default, Graphify does not store its core knowledge graph in a standalone database like SQLite or Neo4j. Instead, it uses NetworkX to construct the graph entirely in-memory and outputs serialized data as portable JSON (`graph.json`) and HTML files (`graph.html`) directly into your project's local directory. [1, 2]
However, Graphify is a highly extensible tool that supports push/sync integrations to external graph platforms like Neo4j and FalkorDB for advanced querying and RAG workloads. [2, 3]

### The Core Technical Stack

Graphify operates as a three-pass local orchestration layer designed to map codebases and context files efficiently without heavy system prerequisites: [4]

-   Parsing Layer ([Tree-sitter](https://tree-sitter.github.io/tree-sitter/)): Parses source code across 20+ programming languages. It extracts Abstract Syntax Trees (AST) locally and deterministically. This pass uses no LLMs or API tokens. [4]
-   Graph Engine ([NetworkX](https://networkx.org/)): The underlying data structure framework. Graphify maps nodes (functions, classes, docs) and edges (dependencies, calls) in-memory inside a NetworkX graph instance. [1, 2, 5]
-   Clustering Engine (Leiden Algorithm): Groups interconnected code paths and concepts into logical structural communities. Unlike traditional RAG tools, it uses structural topology for similarity grouping instead of costly vector embeddings. [4]
-   Semantic Layer (Configured LLM): For non-code assets (PDFs, Markdown, images), it utilizes your AI assistant's existing model API (such as Anthropic Claude or OpenAI) to extract metadata. [4]
-   Transcription Layer (Faster-Whisper): Local audio and video processing for meeting transcripts. [6]

### How Graphify Handles Storage

#### 1. Standard Default Storage: Portable Files

Graphify's local design is optimized to match your Git workflow. When you execute `graphify .`, it writes outputs directly to a local folder (typically `graphify-out/`): [7, 8]

-   `graph.json`: The complete raw snapshot of the structural graph. It maps all relative directory paths so the graph can be committed to Git and immediately shared across team members. [1, 7]
-   `graph.html`: A standalone visualization UI featuring interactive network maps and community clusters. [1, 9]
-   `GRAPH_REPORT.md`: A plain-language text document describing the architecture and "god-nodes" (high impact blast-radii) for the AI assistant to read instantly. [9, 10]

#### 2. Neo4j Integration

Graphify provides built-in sink support to export its extracted snapshot to an instance of Neo4j (such as Neo4j Aura or local Docker instances). This lets you run complex graph traversals, structural path-finding algorithms, and Cypher queries on your codebase. [2, 3, 11]

#### 3. Where SQLite Fits In

Graphify itself does not use SQLite for graph state. However, SQLite often appears alongside Graphify in development environments because: [2]

-   Developers use Graphify alongside complementary plugins like code-review-graph (CRG), which *does* utilize a SQLite-backed AST engine to run local semantic search metrics. [12]
-   Graphify provides documentation blueprints for bundling a SQLite Model Context Protocol (MCP) server alongside its graph toolkit, creating a unified relational + graph workspace for tools like Claude Code. [13]

If you would like to explore setting this up for your project, let me know:

-   What AI assistant or IDE you are integrating it with?
-   Whether your primary codebase files are local or part of a shared team repository?
-   If you plan to scale into millions of edges, which would benefit from turning on the Neo4j or FalkorDB sinks? [2]

[1] [https://medium.com](https://medium.com/@aitoolinsight/graphify-solves-claudes-biggest-limitation-finally-turning-your-codebase-into-a-knowledge-graph-36433a9360f7)
[2] [https://github.com](https://github.com/safishamsi/graphify/issues/1175)
[3] [https://www.youtube.com](https://www.youtube.com/watch?v=HQEm4rBKdec)
[4] [https://medium.com](https://medium.com/how-to-profit-ai/graphify-one-command-turns-any-folder-into-a-knowledge-graph-7b0602b09bee)
[5] [https://graphify.net](https://graphify.net/)
[6] [https://www.youtube.com](https://www.youtube.com/watch?v=BkHps04qGgc)
[7] [https://github.com](https://github.com/safishamsi/graphify?ref=aiposthub.com)
[8] [https://tayipturk.medium.com](https://tayipturk.medium.com/claude-has-no-memory-so-we-built-one-cut-token-costs-70x-with-graphify-obsidian-8efffd8b8ecb)
[9] [https://pi.dev](https://pi.dev/packages/@gaodes/pi-graphify)
[10] [https://github.com](https://github.com/lucasrosati/claude-code-memory-setup)
[11] [https://github.com](https://github.com/cklam12345/wisdomGraph)
[12] [https://dev.to](https://dev.to/mir_mursalin_ankur/graphify-code-review-graph-build-a-self-updating-knowledge-graph-for-claude-code-and-other-ai-j1m)
[13] [https://github.com](https://github.com/safishamsi/graphify/blob/v8/docs/docker-mcp-sqlite.md)

</td></tr>
</table>

## 2026-06-24

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI Mode
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
alternatives of https://github.com/safishamsi/graphify
</td></tr><tr><td>A:</td><td>

Alternatives to safishamsi/graphify for AI-driven code context include <mark>code-review-graph</mark> for structural AST mapping and <mark>GitNexus</mark> for live agent indexing and MCP tools. <mark>TrueCourse</mark> provides architectural dependency analysis, while graphify-dotnet offers a tailored solution for the .NET ecosystem. For detailed comparisons of these tools, visit [Reddit](https://www.reddit.com/r/ClaudeCode/comments/1sme1zw/graphify_vs_codereviewgraph_which_is_better_for/). [1, 2, 3]

[1] [https://www.reddit.com](https://www.reddit.com/r/ClaudeCode/comments/1sme1zw/graphify_vs_codereviewgraph_which_is_better_for/)
[2] [https://ai-chain.tw](https://ai-chain.tw/en/blog/gitnexus-graphify-ai-coding-workflow-guide/)
[3] [https://github.com](https://github.com/elbruno/graphify-dotnet)

</td></tr>
</table>

### code-review-graph

- https://github.com/tirth8205/code-review-graph

### GitNexus

- https://github.com/abhigyanpatwari/GitNexus

### TrueCourse

- https://github.com/truecourse-ai/truecourse

## 2026-09-15

> [!NOTE]
> - title: "Graphify vs GitNexus vs CodeGraph — Which Code Knowledge Graph Should You Use?"
> - source: https://www.youtube.com/watch?v=-Fb1SBC_nmg
> - created: 2026-09-14
> - notebooklm: Agent

## 讓你的 AI 寫程式不再盲目：Graphify vs GitNexus vs CodeGraph 三大知識圖譜工具深度評測

### 1. AI 代理的「視力」革命：從檔案掃描到架構感知

身為軟體架構師，我們深知當前 AI 程式助手（AI Coding Agents）的瓶頸不在於推理邏輯，而在於「視力」。在缺乏架構感知的情況下，AI 處理一個 200 個檔案規模的專案時，往往處於盲目摸索狀態。根據實測基準，**引入程式碼知識圖譜後，AI 代理能減少 58% 的工具調用 (Tool Calls)**。

在傳統模式下，AI 處理單一查詢可能需要進行 15 次以上的工具調用，反覆讀取檔案、追蹤導入（Imports），這不僅大量**燃燒 Token**，且往往在耗費數千 Token 後仍遺漏關鍵的代碼連接。知識圖譜的出現，正是為了讓 AI 從單純的「文字閱讀者」進化為具備「架構意識」的開發專家。

### 2. 核心問題：為什麼傳統 Grep 不足以應付複雜程式碼？

傳統基於文本匹配的搜尋（如 Grep）存在明顯的「靜態分析天花板」（Static Analysis Ceiling）。當你詢問「OAuth 中間件如何連接到資料庫連接池」時，AI 會匹配到數十個檔案，卻難以理解回呼函式（Callbacks）、事件發射器（Event Emitters）或框架路由（Framework Routing）之間的隱形紐帶。

> **什麼是程式碼知識圖譜 (Code Knowledge Graph)？**
>
> 這是將源碼結構化為圖形數據的技術，其核心構成為：
> *   **節點 (Nodes)：** 代表函式 (Functions)、類別 (Classes)、模組 (Modules) 或檔案。
> *   **邊 (Edges)：** 代表它們之間的結構化關係，如呼叫 (Calls)、導入 (Imports)、繼承 (Extends) 或實作 (Implements)。
>
> 透過圖譜，AI 代理不再需要盲目讀取 20 個檔案來追蹤呼叫鏈，只需一次查詢即可獲取完整的「衝擊範圍」（Blast Radius）與路徑分析。

---

### 3. 三大選手登場：Graphify、GitNexus 與 CodeGraph

針對此領域，目前市面上有三個具備代表性的工具，其定位與技術棧各具特色：

*   **Graphify：多模態知識構建器** (Python, MIT 授權)
    *   支援高達 **36 種語言**，唯一能將程式碼與非程式碼文件（PDF、影片）整合的方案。
*   **GitNexus：預運算架構引擎** (NodeJS, 非商業用途免費/商業授權需付費)
    *   支援 **14 種語言**，專注於深度架構分析、跨儲存庫（Cross-repo）與微服務依賴追蹤。
*   **CodeGraph：零維護加速器** (Standalone Binary, MIT 授權)
    *   支援 **20+ 種語言**，強調極速同步與對動態程式碼流（Dynamic Flow）的深度理解。

---

### 4. 六大維度深度評測 (Head-to-Head Comparison)

| 評測維度 | Graphify | GitNexus | CodeGraph |
| :--- | :--- | :--- | :--- |
| **索引更新速度** | 手動更新或 Git Hooks | 手動分析，支援增量更新 | **2 秒自動同步** (基於 OS 級 FS Events/Inotify) |
| **支援內容廣度** | **涵蓋 36 語言**、PDF、**YouTube URLs、Google Workspace** | 14 語言，含 API 路由、資料庫模型與依賴注入 (DI) | 20+ 語言，專注代碼、框架路由與動態調度 |
| **動態理解能力** | 基本靜態分析 | **DI 解析**與抽象介面調度 (具備信心評分機制) | **最強** (支援 React SetState, 回呼與**函式指標調度**) |
| **查詢權限與體驗** | 7 個 MCP 工具 (支援自然語言圖表遍歷) | 17 個高度細化工具 (含影響分析、重新命名、路徑映射) | **單一工具** (降低 AI 選擇工具的認知負荷) |
| **跨專案與團隊** | 支援手動合併多專案圖譜 | **領先** (跨儲存庫影響分析與合約註冊表) | 單一專案專用，無團隊共享功能 |
| **視覺化與探索** | **7 種導出格式** (含 HTML, SVG, **Obsidian**) | Web UI (WebGL 驅動) 與 Wiki 生成 | 無 (純粹為 AI 代理設計，無人類視覺介面) |

#### 關鍵洞察：
*   **動態合成哲學：** CodeGraph 的優勢在於其「動態語意合成」層，僅在能閉合完整路徑時才建立邊緣，避免 AI 陷入無效的檔案讀取。
*   **AI 心理學：** 實測顯示，當 AI 代理看到 17 個專用工具時，往往會因為選項過多而選擇忽略。CodeGraph 採用的「單一工具、全量回答」策略，在 Agent 基準測試中表現出更高的調用成功率。

---

### 5. 底層共通點：AI 軟體架構的六大趨勢

這三款工具雖然在應用層有所不同，但底層設計皆遵循現代 AI 開發工具的核心模式：

1.  **Tree-sitter 作為解析基石：** 捨棄正則表達式，利用語法樹 (AST) 進行本地、高效且容錯的語法分析。
2.  **SHA-256 內容快取：** 透過檔案指紋識別，確保僅在內容變動時觸發增量索引，優化效能。
3.  **MCP (Model Context Protocol) 協議：** 三者均遵循此新興標準，確保與 Claude 或 IDE 插件無縫銜接。
4.  **置信度追蹤 (Confidence Tracking)：** 為每個圖譜邊緣標註來源（直接源碼、**啟發式推斷 Heuristic Inference** 或 LLM 預測）。
5.  **一次索引，多次查詢：** 將昂貴的解析開銷留在構建期。GitNexus 使用 **Ladybug DB**，CodeGraph 則採用 **SQLite 與 WAL (Write Ahead Logging)** 技術以確保讀寫效能。
6.  **尊重 `.gitignore`：** 自動排除專案噪音（如 `node_modules`），保持圖譜純淨度。

---

### 6. 不可忽視的局限性

> [!WARNING] **架構師的警告：**
> *   **無法捕捉執行時行為：** 工具分析的是靜態源碼，無法偵測動態競爭條件 (Race Conditions) 或效能瓶頸。
> *   **小型專案邊際效應低：** 對於少於 20 個檔案的專案，直接讀取檔案比建立圖譜更具成本效益。
> *   **特定語言缺口：** 目前對 Haskell, OCaml, F#, Clojure 等函數式語言支援尚不完善。
> *   **不保證邏輯正確性：** 掌握「衝擊範圍」不代表修改建議必然正確，仍需依賴測試單元。
> *   **初始建置開銷：** 大型專案首次索引需 1 至 5 分鐘。
> *   **靜態分析天花板：** 對於高度動態的反射 (Reflection)、Eval 或動態計算的檔案路徑，目前仍是技術盲點。

---

### 7. 決策指南：你該選擇哪一個？

*   [ ] **需要整合非代碼知識（如設計文件、研究論文、影片）：** 選擇 **Graphify**。它是唯一能將 Google Workspace、YouTube 內容與代碼串聯的 MIT 工具。
*   [ ] **處理微服務架構或跨儲存庫（Multi-repo）分析：** 選擇 **GitNexus**。其合約註冊表與跨服務路徑追蹤是企業級環境的首選。
*   [ ] **追求極速、零維護與深度動態追蹤：** 選擇 **CodeGraph**。適合單一大型專案開發，其自動同步機制能緊跟每一行代碼變動。

---

### 8. 結論與實踐建議

這三款工具並不互斥，架構師可以根據開發階段靈活切換。若要提升 AI 代理的效能，建議從以下指令開始：

**CodeGraph (零維護、安裝後無需手動指令):**
```bash
code-graph init
```

**GitNexus (跨儲存庫分析):**
```bash
npx gitnexus analyze
```

**Graphify (多模態與文件整合):**
```bash
uv tool install graphify
```

別再讓你的 AI 代理在黑暗中盲目摸索，透過知識圖譜為它裝上真正的「架構視角」。