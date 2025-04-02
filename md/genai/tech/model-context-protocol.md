# Model Context Protocol (MCP)

- https://modelcontextprotocol.io/introduction

## 2025-03-15

### MCP 跟 aider 整合 -- `mcpm-aider`

- ( 2025-03-15 21:05:49 )
- 想法： `aider` 目前並沒有支援可以呼叫外部工具的作法，像是可否請 `aider` 的 `/ask` 模式做 web search 並彙整到 Markdown
- 搜尋：找到一個 YouTube 影片 [Use MCP Servers and Tools in Aider](https://www.youtube.com/watch?v=OM1h4YDPjRU) 提到他寫了一個工具，可以讓 `aider` 知道有 MCP Tool
  - 相關 Aider Github issues
    - https://github.com/Aider-AI/aider/issues/2525
    - https://github.com/Aider-AI/aider/issues/3314

### 初步理解 MCP 是什麼

- ( 2025-03-15 22:44:05 )
- 2025-03-15: [Model Context Protocol (MCP), clearly explained (why it matters)](https://www.youtube.com/watch?v=7j_NE6Pjv-E)

Key Points: 要點：

- MCP (Model ContextProtocol) is a standard that creates a unified layer between LLMs and external services/tools - LLMs by themselves are limited to text prediction and cannot perform meaningful tasks without tools - MCP solves the problem of connecting multiple tools to LLMs by creating a standardized communication protocol - The MCP ecosystem consists of clients (like Tempo, Windsurf, Cursor), the protocol, servers, and services

> - MCP（模型上下文協定）是一種在模型和外部服務/工具之間創建統一層的標準 - LLMs 本身僅限於文字預測，如果沒有工具則無法執行有意義的任務 - MCP 透過建立標準化通訊協定解決了將多個工具連接到 LLMs 的問題 - MCP 生態系統由客戶端（如 Tempo、Windsurf、Cursor）、協定、伺服器和服務組成

1) What are MCPs and why should you care?

> 1）什麼是 MCP？

MCPs are NOT some complex physics theory - they're simply STANDARDS that help LLMs connect to external tools and services.

> MCP 不是某種複雜的物理理論 - 它們只是幫助連接外部工具和服務的標準。

Think of them as universal translators between AI models and the tools they need to be truly useful.

> 可以將它們視為人工智慧模型與真正有用所需工具之間的通用轉換器。

This is HUGE for making AI assistants actually capable!

> 這對於讓人工智慧助理真正發揮其能力具有重大意義！

2) The Evolution of LLMs: From Text Prediction to Tool Use

> 2）LLMs的演變：從文字預測到工具使用

Stage 1: Basic LLMs can only predict text - Ask ChatGPT to send an email? "Sorry, I can't do that" - They're glorified text predictors (if I say "My big fat Greek..." it knows "wedding" comes next) - Limited to answering questions, not DOING things

> 第 1 階段：基本LLMs只能預測文本 - 要求 ChatGPT 發送電子郵件？ "抱歉，我做不到" - 它們是經過美化的文字預測器（如果我說「我的大胖子希臘...」它知道接下來是「婚禮」） - 僅限於回答問題，而非做事

3) The Current State: LLMs + Tools

> 3) 目前狀態：LLMs + 工具

Stage 2: LLMs connected to tools - Companies like Perplexity connect LLMs to search engines - This makes them more useful but creates problems - Each tool = different "language" the LLM must learn - Connecting multiple tools = engineering NIGHTMARE

> 第 2 階段：LLMs連接到工具 - Perplexity 等公司與搜尋引擎建立聯繫 - 這使得它們更有用，但也帶來了問題 - 每種工具 = 必須學習的不同"語言" - 連結多種工具 = 工程噩夢

This is why we don't have Jarvis-level assistants yet!

> 這就是我們還沒有賈維斯級助手的原因！

![](assets/2025-03-15_LLM_Tools.png)

4) Enter MCPs: The Game-Changer

> 4）進入 MCP：遊戲規則改變者

MCPs create a UNIFIED LAYER between LLMs and external services.

> MCP 在與外部服務之間建立一個統一層。

Instead of your AI speaking 10 different "languages" to use 10 different tools, MCPs translate everything into ONE language.

> 您的 AI 不會說 10 種不同的「語言」來使用 10 種不同的工具，而是 MCP 將所有內容翻譯成一種語言。

Result? LLMs can easily access databases, APIs, and services without massive engineering headaches.

> 結果？可以輕鬆存取資料庫、API 和服務，而無需大量的工程麻煩。

![](assets/2025-03-15_LLM_MCP_Services.png)

5) The MCP Ecosystem Explained

> 5）MCP 生態系解析

The MCP system has 4 key components:

> MCP 系統有 4 個關鍵組件：

- MCP Client: User-facing apps like @tempoai, Windsurf, Cursor - Protocol: The standardized communication method - MCP Server: Translates between client and services - Service: The actual tool (database, search engine, etc.)

> - MCP 用戶端：面向使用者的應用程序，例如@tempoai、Windsurf、Cursor - 協定：標準化的通訊方法 - MCP 伺服器：在客戶端和服務之間進行轉換 - 服務：實際工具（資料庫、搜尋引擎等）

Brilliant move by Anthropic: SERVICES must build MCP servers!

> Anthropic 的妙招：SERVICES 必須建置 MCP 伺服器！

![](assets/2025-03-15_MCP_Ecosystem.png)

6) Why This Matters For Builders

> 6）為什麼這對開發者很重要

For technical folks: - Opportunity to build tools like MCP app stores - Easier integration between services - Less engineering headaches

> 對於技術人員： - 有機會建立 MCP 應用商店等工具 - 服務之間更容易集成 - 減少工程難題

For non-technical folks: - Watch closely as standards evolve - When standards finalize, new business opportunities will emerge - Think of MCPs as Lego pieces you'll stack to build powerful AI apps

> 對於非技術人員： - 密切關注標準的發展 - 標準最終確定後，將會出現新的商機 - 將 MCP 視為樂高積木，你可以將其堆疊起來以構建強大的 AI 應用程式

## 2025-04-02

- What is MCP? (Model Context Protocol) - A Primer
  - https://www.whatismcp.com/