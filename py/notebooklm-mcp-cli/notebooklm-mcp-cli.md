# notebooklm-mcp-cli

- Git Repo
  - https://github.com/jacob-bd/notebooklm-mcp-cli

## 2026-06-13

- Learn from https://github.com/mathruffian-dot/claude-code-lazy-packs

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI Mode
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
在安裝特定 PyPI 套件前,可以在哪裡找到 Security 的建議?
</td></tr><tr><td>A:</td><td>

### PyPI Security Advisory

安裝特定 PyPI 套件前，建議在 [PyPI 官方網站](https://pypi.org/) 檢查專案頁面與發布資訊，並搭配漏洞資料庫查詢，確認是否有已知的安全風險。 [1, 2, 3, 4]
您可以透過以下幾個核心平台，查詢 PyPI 套件的 Security 建議與漏洞報告：

* PyPI 官方網站： 在套件頁面的 Security 標籤或側邊欄，可以直接查看官方與套件維護者發布的 Security Advisories（安全性建議）與漏洞通報。 [2, 3]
* GitHub Advisory Database： 如果套件是開源的，可至 [GitHub Advisory](https://github.com/advisories) 搜尋該套件名稱，查看由社群與資安人員驗證過的 CVE（Common Vulnerabilities and Exposures）漏洞報告。 [4]
* OSV (Open Source Vulnerability)： 這是整合多個開源生態系的漏洞資料庫。可至 [OSV.dev](https://osv.dev/) 搜尋特定套件，取得跨平台、結構化的安全性數據。 [4]

#### ⚠️ 安裝前評估與預防建議

* 檢查套件元數據 (Metadata)： 下載前請確認套件名稱有無拼寫錯誤（防止 Typing squatting 惡意套件），並觀察其發布日期、維護活躍度與官方原始碼連結。 [5, 6, 7]
* 靜態檢測工具 (安裝後)： 專案中使用到的套件，務必透過 [pip-audit](https://pypi.org/project/pip-audit/) 或 [Safety](https://pypi.org/project/safety/) 等 Python 資安掃描工具進行檢查，防堵潛在的安全危機。 [4, 8, 9]

如果您想針對目前專案中特定的套件或軟體供應鏈安全管理進一步了解：

   1. 您目前想評估的是哪一個 特定的 PyPI 套件？
   2. 是否需要了解如何將 自動化資安掃描 (CI/CD) 整合到您的開發流程中？


[1] [https://www.reddit.com](https://www.reddit.com/r/Python/comments/11iymqr/how_do_you_manage_malicious_package_security/?tl=zh-hant)
[2] [https://realnewbie.com](https://realnewbie.com/posts/python-pypi)
[3] [https://cloudtop10.com](https://cloudtop10.com/post/pypi-supply-chain-attack-ai-malicious-packages/)
[4] [https://yorkisinhere.medium.com](https://yorkisinhere.medium.com/python-%E5%A5%97%E4%BB%B6%E6%BC%8F%E6%B4%9E%E6%AA%A2%E6%9F%A5-375dfa508609)
[5] [https://www.informationsecurity.com.tw](https://www.informationsecurity.com.tw/article/article_detail.aspx?aid=10031)
[6] [https://www.twcert.org.tw](https://www.twcert.org.tw/tw/cp-104-4823-1b554-1.html)
[7] [https://blog.csdn.net](https://blog.csdn.net/ProceNest/article/details/152455904)
[8] [https://ithelp.ithome.com.tw](https://ithelp.ithome.com.tw/m/articles/10378349)
[9] [https://fourdollars.blogspot.com](https://fourdollars.blogspot.com/2017/11/python-safety.html)

</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
notebooklm-mcp-cli
</td></tr><tr><td>A:</td><td>

要評估 [notebooklm-mcp-cli](https://pypi.org/project/notebooklm-mcp-cli/) 套件的安全建議，我們可以從其專案特性、驗證管道與運行機制來全面檢視。 [1]
這是整合 Google NotebookLM 與 Model Context Protocol (MCP) 的社群熱門開源套件，能讓 Claude Desktop、Claude Code 等 AI 代理直接調用 NotebookLM 的功能。 [2, 3, 4]

#### 🔍 1. 安全漏洞與套件評估管道

* 官方專案與資料庫狀態： 前往開源原始碼庫 [jacob-bd/notebooklm-mcp-cli](https://github.com/jacob-bd/notebooklm-mcp-cli) 檢查最新版本的 Issue 與維護現況。由於此套件整合了舊版的 `notebooklm-mcp` 與 `notebooklm-cli`，建議透過 GitHub Advisory Database 或第三方資安平台（如 [Socket.dev 的安全性分析](https://socket.dev/pypi/package/notebooklm-mcp)）確認有無歷史漏洞残留。
* 相依套件掃描： 該套件在自動化操作、瀏覽器模擬與 MCP 通訊上依賴了其他 Python 庫。安裝前可在終端機執行測試掃描（如使用 uvx pip-audit）來掃描潛在的供應鏈風險。 [3, 5, 6, 7, 8]

#### ⚠️ 2. 架構層面的核心安全考量

在安裝與設定 notebooklm-mcp-cli 時，應特別注意以下特有的隱私與安全機制：

* 憑證與 Session 授權安全（主要風險點）：
* 該套件需要透過 nlm login 啟動 Chrome 來提取 Google 帳戶的 Session Cookies 進行內部 API 認證。
   * 安全建議： 確保您的本地環境安全，防止惡意軟體讀取該套件儲存在本地的憑證檔案。不建議在多人共用的不安全伺服器上執行此認證。 [9, 10]
* 第三方 API 與非官方性質：
* 此專案非 Google 官方發布，而是透過逆向/內部 API 驅動。
   * 安全建議： 隨時注意 Google 服務條款的更新。如果將其用於企業敏感資料或內部知識庫，需評估資料經由非官方通道傳輸的合規性風險。 [10, 11]
* 執行權限（建議的安裝方式）：
* 官方強烈推薦使用 uv tool install notebooklm-mcp-cli 進行安裝。
   * 安全建議： 使用 uv 或 pipx 進行隔離安裝，能避免該套件的相依版本污染到您全域或其他核心專案的 Python 環境。 [1, 4, 9, 12]

------------------------------
如果您正準備將此工具整合至日常工作流，接下來可以：

* 了解如何安全地將它設定到 Claude Desktop 或 Claude Code 的設定檔中？
* 評估在多帳戶切換時，如何避免 Cookie 覆蓋的隱私問題？ [2, 3, 6, 13]


[1] [https://pypi.org](https://pypi.org/project/notebooklm-mcp-cli/)
[2] [https://www.youtube.com](https://www.youtube.com/watch?v=W7Uhzy3IR2Y&t=4)
[3] [https://github.com](https://github.com/jacob-bd/notebooklm-mcp-cli)
[4] [https://www.xda-developers.com](https://www.xda-developers.com/notebooklm-connects-to-claude-through-mcp/)
[5] [https://github.com](https://github.com/PleasePrompto/notebooklm-mcp)
[6] [https://www.reddit.com](https://www.reddit.com/r/notebooklm/comments/1qs7v2s/notebooklm_mcp_cli_v027_unified_package_file/)
[7] [https://socket.dev](https://socket.dev/pypi/package/notebooklm-mcp)
[8] [https://github.com](https://github.com/alfredang/notebooklm-mcp)
[9] [https://github.com](https://github.com/jacob-bd/notebooklm-cli)
[10] [https://ainsights.blog](https://ainsights.blog/notebooklm-mcp-server/)
[11] [https://github.com](https://github.com/jacob-bd/notebooklm-mcp-cli?ref=legaled.ai)
[12] [https://github.com](https://github.com/jacob-bd/notebooklm-mcp-cli/blob/main/CONTRIBUTING.md)
[13] [https://www.xda-developers.com](https://www.xda-developers.com/notebooklm-connects-to-claude-through-mcp/)

</td></tr>
</table>

## 2026-06-14

- 安裝
```bash
~/git/snippet$ uv tool install notebooklm-mcp-cli
```
- 登入
```bash
~/git/snippet$ nlm login
```
- 列表
```bash
~/git/snippet$ nlm list --help

 Usage: nlm list [OPTIONS] COMMAND [ARGS]...

 List resources (notebooks, sources, artifacts)

╭─ Options ────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                          │
╰──────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────────────╮
│ notebooks      List all notebooks.                                                   │
│ sources        List sources in a notebook.                                           │
│ artifacts      List all studio artifacts.                                            │
│ aliases        List all aliases.                                                     │
│ stale-sources  List Drive sources that need syncing.                                 │
│ skills         List available skills and installation status.                        │
╰──────────────────────────────────────────────────────────────────────────────────────╯
```
- 列出 Notebook （有點像「書櫃」的概念）
```bash
~/git/snippet$ nlm list notebooks
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━┳━━━━━━━━━━━━┓
┃ ID                                   ┃ Title                                              ┃  Src ┃ Updated    ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━╇━━━━━━━━━━━━┩
│ b2a0d4bc-000e-4e72-b9c6-659a488c1cbe │ GCP                                                │    2 │ 2026-06-11 │
```
- 列出 Skills （比較像是不同 AI Agent 的整合）
```bash
~/git/snippet$ nlm list skills
                         NotebookLM Skill Installation Status
┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━┳━━━━━━━━━┓
┃ Tool        ┃ Description                                         ┃ User ┃ Project ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━╇━━━━━━━━━┩
│ claude-code │ Claude Code CLI and Desktop                         │  -   │    -    │
│ cursor      │ Cursor AI editor                                    │  -   │    -    │
│ agents      │ Generic agent skill (Gemini CLI, Codex, and others) │  -   │    -    │
│ gemini-cli  │ Google Gemini CLI                                   │  -   │    -    │
│ codex       │ OpenAI Codex CLI                                    │  -   │    -    │
│ opencode    │ OpenCode AI assistant                               │  -   │    -    │
│ antigravity │ Antigravity agent framework                         │  -   │    -    │
│ cline       │ Cline CLI terminal agent                            │  -   │    -    │
│ openclaw    │ OpenClaw AI agent framework                         │  -   │    -    │
│ alef-agent  │ Alef Agent AI agent framework                       │  -   │    -    │
│ hermes      │ Hermes Agent (NousResearch)                         │  -   │    -    │
└─────────────┴─────────────────────────────────────────────────────┴──────┴─────────┘

Legend: ✓ = installed, - = not installed, N/A = not applicable
```
- 列出指定 Notebook 右側 Studio 的所有 Artifact
```bash
~/git/snippet$ nlm list artifacts --help

 Usage: nlm list artifacts [OPTIONS] NOTEBOOK

 List all studio artifacts.

╭─ Arguments ─────────────────────────────────────────────────────────────────────────╮
│ *    notebook      TEXT  Notebook ID or alias [required]                            │
╰─────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ───────────────────────────────────────────────────────────────────────────╮
│ --full     -a            Show all details                                           │
│ --json     -j            Output as JSON                                             │
│ --profile  -p      TEXT  Profile to use                                             │
│ --help                   Show this message and exit.                                │
╰─────────────────────────────────────────────────────────────────────────────────────╯
```
- 下載指定 Notebook 右側 Studio 的特定種類 Artifact
```bash
~/git/snippet$ nlm download --help

 Usage: nlm download [OPTIONS] COMMAND [ARGS]...

 Download artifacts (audio, video, etc)

╭─ Options ───────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                         │
╰─────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────────────╮
│ audio        Download Audio Overview.                                               │
│ video        Download Video Overview.                                               │
│ slide-deck   Download Slide Deck (PDF or PPTX).                                     │
│ infographic  Download Infographic (PNG).                                            │
│ report       Download Report (Markdown).                                            │
│ mind-map     Download Mind Map (JSON).                                              │
│ data-table   Download Data Table (CSV).                                             │
│ quiz         Download Quiz.                                                         │
│ flashcards   Download Flashcards.                                                   │
╰─────────────────────────────────────────────────────────────────────────────────────╯
```
- 下載指定 Notebook 右側 Studio 指定 Report 種類的 Artifact
```bash
~/git/snippet$ nlm download report --help

 Usage: nlm download report [OPTIONS] NOTEBOOK_ID

 Download Report (Markdown).

╭─ Arguments ─────────────────────────────────────────────────────────────────────────╮
│ *    notebook_id      TEXT  Notebook ID [required]                                  │
╰─────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ───────────────────────────────────────────────────────────────────────────╮
│ --output  -o      TEXT  Output path (default: ./{notebook_id}_report.md)            │
│ --id              TEXT  Specific artifact ID                                        │
│ --help                  Show this message and exit.                                 │
╰─────────────────────────────────────────────────────────────────────────────────────╯
```
- 實測如果只給 NOTEBOOK_ID，沒有加上 `--id` 的話，只會存最新一筆的 Report
- 列出指定 Notebook 左側的 Source
```bash
~/git/snippet$ nlm list sources --help

 Usage: nlm list sources [OPTIONS] NOTEBOOK

 List sources in a notebook.

╭─ Arguments ─────────────────────────────────────────────────────────────────────────╮
│ *    notebook      TEXT  Notebook ID or alias [required]                            │
╰─────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ───────────────────────────────────────────────────────────────────────────╮
│ --full            -a            Show all columns                                    │
│ --drive           -d            Show Drive sources with freshness status            │
│ --skip-freshness  -S            Skip freshness checks (faster, use with --drive)    │
│ --json                          Output as JSON                                      │
│ --quiet           -q            Output IDs only                                     │
│ --url             -u            Output as ID: URL                                   │
│ --profile         -p      TEXT  Profile to use                                      │
│ --help                          Show this message and exit.                         │
╰─────────────────────────────────────────────────────────────────────────────────────╯
```
- 所有指令
```
~/git/snippet$ nlm

 Usage: nlm [OPTIONS] COMMAND [ARGS]...

 NotebookLM Tools - Unified CLI for Google NotebookLM

╭─ Options ───────────────────────────────────────────────────────────────────────────╮
│ --version             -v        Show version and exit                               │
│ --ai                            Output AI-friendly documentation for this CLI       │
│ --debug                         Enable debug logging (shows raw API responses)      │
│ --install-completion            Install completion for the current shell.           │
│ --show-completion               Show completion for the current shell, to copy it   │
│                                 or customize the installation.                      │
│ --help                          Show this message and exit.                         │
╰─────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────────────╮
│ login        Authentication and profile management                                  │
│ notebook     Manage notebooks                                                       │
│ label        Manage source labels                                                   │
│ note         Manage notes                                                           │
│ source       Manage sources                                                         │
│ chat         Configure chat settings                                                │
│ studio       Manage studio artifacts                                                │
│ research     Research and discover sources                                          │
│ alias        Manage ID aliases                                                      │
│ config       Manage configuration                                                   │
│ download     Download artifacts (audio, video, etc)                                 │
│ share        Manage notebook sharing                                                │
│ export       Export artifacts to Google Docs/Sheets                                 │
│ skill        Install skills for AI tools                                            │
│ setup        Configure MCP server for AI tools                                      │
│ doctor       Diagnose installation and configuration                                │
│ batch        Batch operations across notebooks                                      │
│ cross        Cross-notebook queries                                                 │
│ pipeline     Run multi-step pipelines                                               │
│ tag          Manage notebook tags                                                   │
│ audio        Create audio overviews                                                 │
│ report       Create reports                                                         │
│ quiz         Create quizzes                                                         │
│ flashcards   Create flashcards                                                      │
│ mindmap      Create and manage mind maps                                            │
│ slides       Create slide decks                                                     │
│ infographic  Create infographics                                                    │
│ video        Create video overviews                                                 │
│ data-table   Create data tables                                                     │
│ create       Create resources (notebooks, audio, video, etc)                        │
│ list         List resources (notebooks, sources, artifacts)                         │
│ get          Get details about resources                                            │
│ delete       Delete resources (notebooks, sources, artifacts)                       │
│ add          Add resources (sources to notebooks)                                   │
│ rename       Rename resources                                                       │
│ status       Check status of resources                                              │
│ describe     Get AI-generated descriptions and summaries                            │
│ query        Chat with notebook sources                                             │
│ sync         Sync resources (Drive sources)                                         │
│ content      Get raw content from sources                                           │
│ stale        List stale resources that need syncing                                 │
│ configure    Configure settings                                                     │
│ set          Set values (aliases, config)                                           │
│ show         Show information                                                       │
│ install      Install resources (skills)                                             │
│ uninstall    Uninstall resources (skills)                                           │
│ update       Update resources (skills)                                              │
╰─────────────────────────────────────────────────────────────────────────────────────╯
```
- 安裝 Auto-completion
```bash
~/git/snippet$ nlm --install-completion
```
- 整合 OpenCode
```bash
~/git/snippet$ nlm setup add opencode

OpenCode — Adding NotebookLM MCP

✓ Added to OpenCode
  C:\Users\jazzw\.config\opencode\opencode.json

Restart OpenCode to activate the MCP server.
```
- 覺得比較特別的指令 (1) -- `batch` 批次作業
```bash
~/git/snippet$ nlm batch --help

 Usage: nlm batch [OPTIONS] COMMAND [ARGS]...

 Batch operations across notebooks

╭─ Options ──────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                            │
╰────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ─────────────────────────────────────────────────────────────────────────────╮
│ query       Query multiple notebooks with the same question.                           │
│ add-source  Add the same source URL to multiple notebooks.                             │
│ create      Create multiple notebooks at once.                                         │
│ delete      Delete multiple notebooks. IRREVERSIBLE.                                   │
│ studio      Generate studio artifacts across multiple notebooks.                       │
╰────────────────────────────────────────────────────────────────────────────────────────╯
```
- 覺得比較特別的指令 (2) -- `pipeline` 自訂工作流
```bash
~/git/snippet$ nlm pipeline --help

 Usage: nlm pipeline [OPTIONS] COMMAND [ARGS]...

 Run multi-step pipelines

╭─ Options ──────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                            │
╰────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ─────────────────────────────────────────────────────────────────────────────╮
│ run     Execute a pipeline on a notebook.                                              │
│ list    List all available pipelines.                                                  │
│ create  Create a user-defined pipeline from a YAML file.                               │
╰────────────────────────────────────────────────────────────────────────────────────────╯

~/git/snippet$ nlm pipeline list
                                      Pipelines (3)
┏━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Name                ┃ Steps ┃ Source  ┃ Description                                    ┃
┡━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ ingest-and-podcast  │   3   │ builtin │ Add a URL source, query for summary, then      │
│                     │       │         │ generate audio podcast                         │
│ research-and-report │   2   │ builtin │ Add a URL source and generate a briefing doc   │
│                     │       │         │ report                                         │
│ multi-format        │   3   │ builtin │ Generate audio, report, and flashcards from a  │
│                     │       │         │ notebook                                       │
└─────────────────────┴───────┴─────────┴────────────────────────────────────────────────┘
```
- 覺得比較特別的指令 (2) -- `cross` 跨 Notebook 查詢
```bash
~/git/snippet$ nlm cross --help

 Usage: nlm cross [OPTIONS] COMMAND [ARGS]...

 Cross-notebook queries

╭─ Options ──────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                            │
╰────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ─────────────────────────────────────────────────────────────────────────────╮
│ query  Query multiple notebooks and get aggregated answers.                            │
╰────────────────────────────────────────────────────────────────────────────────────────╯

~/git/snippet$ nlm cross query --help

 Usage: nlm cross query [OPTIONS] QUERY

 Query multiple notebooks and get aggregated answers.

╭─ Arguments ────────────────────────────────────────────────────────────────────────────╮
│ *    query      TEXT  Question to ask across notebooks [required]                      │
╰────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ──────────────────────────────────────────────────────────────────────────────╮
│ --notebooks  -n      TEXT  Comma-separated notebook names or IDs                       │
│ --tags       -t      TEXT  Comma-separated tags to select notebooks                    │
│ --all        -a            Query ALL notebooks (rate limits apply)                     │
│ --help                     Show this message and exit.                                 │
╰────────────────────────────────────────────────────────────────────────────────────────╯
````

### 新 NotebookLM 聊天中的代理功能

- https://x.com/NotebookLM/status/2064016460964585549
> Introducing a more powerful NotebookLM 🚀
>
> Massive upgrades deliver agentic capabilities in chat, more advanced reasoning, and a suite of new output formats. Tackling complex, multi-step research problems has never been easier.
>
> Rolling out now to Google AI Ultra subscribers.
>
> 推出更強大的 NotebookLM 🚀
>
> 大規模升級帶來聊天中的代理功能、更先進的推理以及一套新的輸出格式。解決複雜的多步驟研究問題從未如此輕鬆。
>
> 現正向 Google AI Ultra 會員推出。