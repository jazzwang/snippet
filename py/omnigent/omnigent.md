# Omnigent

- Git Repo
  - https://github.com/omnigent-ai/omnigent
- Website
  - https://omnigent.ai/

## 2026-09-01

- 今天再次在 [AI Coding 預算暴衝怎麼辦？Databricks 揭 4 招省錢心法，先找效率前沿模型就對了](https://fc.bnext.com.tw/articles/view/4884) 看到 Meta-Harness 跟 Omnigent 的描述。從 [Databricks 的文章 "Managing AI Coding Costs at Scale" (August 7, 2026)](https://www.databricks.com/blog/managing-ai-coding-costs-scale) 也連結了 Smart Routing 的重要性。

![](https://www.databricks.com/sites/default/files/inline-images/2026-08-Blog-Managing-AI-coding-costs-at-scale-Inline-01-960x385-2x-1.png)

<center>Smart Routing 可以省約 30%</center>

![](https://www.databricks.com/sites/default/files/inline-images/2026-08-Blog-Managing-AI-coding-costs-at-scale-Inline-02-960x548-2x-1.png)

<center>meta-harness</center>

> 本摘要依據 [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) 儲存庫的 README、`pyproject.toml`、`docs/AGENT_YAML_SPEC.md`、`docs/POLICIES.md`、`omnigent/server/API.md` 與 `deploy/README.md` 整理。儲存庫目前標示為 Alpha；版本資訊以本次檢視到的 `0.12.0.dev0` 為準，實際使用時應以目標 commit 或 release 為準。

## 1. 專案定位

Omnigent 是一個開源的 **meta-harness**：在不同 AI coding agent／LLM harness 之上提供統一的規格、執行、協作、治理與部署層。它不是單一模型或單一 agent，而是把 Claude Code、Codex、Cursor、OpenCode、Hermes、Pi，以及透過 YAML 或 ACP 定義的自訂 agent，納入同一個控制平面。

核心價值包括：

- **Harness 解耦**：同一類 agent 工作流可替換或混用不同 harness。
- **多代理協作**：支援 sub-agent、handoff、平行工作與 reviewer 工作流。
- **跨裝置操作**：終端機、瀏覽器、手機與 macOS 桌面 UI 共用 session 狀態。
- **可治理執行**：以政策控制工具呼叫、檔案／Shell 存取、模型費用與人工核准。
- **本地或雲端執行**：runner 可在使用者機器上執行，也可透過 managed sandbox 連接多種雲端環境。

專案採 Apache License 2.0，定位仍是 Alpha，因此 API、harness 整合與部署選項可能持續演進。

## 2. 整體架構

Omnigent 的執行模型將控制平面與執行平面分離：

```text
┌──────────────────────────────────────────────┐
│ Client layer                                  │
│ Web UI / Browser / Phone / Desktop / CLI      │
└──────────────────────┬───────────────────────┘
                       │ HTTP + SSE + WebSocket
┌──────────────────────▼───────────────────────┐
│ Server：FastAPI + Uvicorn                    │
│ sessions、auth、sharing、projects、policies  │
│ persistence、files、managed hosts、API       │
└──────────────────────┬───────────────────────┘
                       │ WS /v1/runner/tunnel
┌──────────────────────▼───────────────────────┐
│ Runner：使用者主機／dev container             │
│ spec loader → runtime → harness adapter      │
│ tools、MCP、sub-agents、terminal、sandbox    │
└──────────────────────┬───────────────────────┘
                       │ vendor SDK / CLI / ACP
       Claude / Codex / Cursor / Pi / ACP / ...
```

### Server

`omnigent/server/app.py` 是 FastAPI 應用程式入口，負責 HTTP API、SSE session stream、WebSocket tunnel、靜態 Web UI、認證與多種 route。Server 儲存 session、conversation、agent、policy、project、file、permission、comment 與 scheduled task 等資料，但一般 agent loop 與工具執行是在 runner 端進行。

### Runner

Runner 是連回 server 的 Python 執行程序。它載入並驗證 agent spec，建立 runtime，啟動對應 harness，執行 LLM turn、工具呼叫、審批與事件串流，再把結果送回 server。這個設計讓模型金鑰、程式碼工作目錄與本機工具不必放進 server image，也能讓 server 以較小的部署映像提供多使用者協作。

### Runtime

`omnigent/runtime` 是可作為 library 使用的執行引擎，而非只能透過服務啟動的 monolith。其主要職責是：

1. 組合 agent instructions、每次 request instructions 與 framework metadata。
2. 驅動 LLM reasoning loop。
3. 將工具 schema 暴露給模型並處理 tool result。
4. 管理 skills、sub-agent、handoff、cancellation 與 pending input。
5. 執行 policy enforcement、審批與 session stream。

## 3. Agent 規格與擴充模型

Agent 以 YAML 描述，通常包含 `name`、`prompt` 或 `instructions`、`executor`、`tools`、`policies`、`os_env`、`terminals`、`params` 等欄位。它可以是單一 YAML 檔，也可以是含 `config.yaml` 與資產的 bundle；載入器同時支援目錄、tarball 與 raw bytes，並提供安全解壓與 schema validation。

最小範例：

```yaml
name: analyst
prompt: |
  你是一位簡潔、可驗證的資料分析助理。

executor:
  harness: claude-sdk
  model: databricks-claude-sonnet-4-6
  auth:
    type: databricks
    profile: oss

tools:
  docs:
    type: mcp
    url: https://example.com/mcp
```

### Executor／Harness

`executor.harness` 決定底層執行器；README 與 spec 文件列出的路徑包含 SDK、native CLI、ACP 與其他 vendor adapter，例如：

- Claude SDK／native、OpenAI Agents／Codex native
- Cursor SDK／native、OpenCode、Hermes、Pi
- Antigravity、GitHub Copilot、Kimi、Qwen
- `acp:<slug>`：執行設定檔中註冊的任意 Agent Client Protocol server

`model`、`reasoning_effort` 與 `auth` 可在 spec 中指定，也能由 CLI 或 Omnigent 設定覆寫。Databricks gateway 是其中一種模型路由方式；另支援第一方 API key、Claude／ChatGPT subscription、OpenAI／Anthropic 相容 gateway，以及部分 provider-specific authentication。

### Tools

工具透過宣告式設定注入，主要類型包括：

- **Python function tool**：以 dotted import path 指向 callable，從函式簽名建立 schema。
- **MCP server**：可使用本地 command 或遠端 URL，並可限制允許的 tool 名稱。
- **Sub-agent**：在同一 agent spec 內定義委派目標，可繼承必要工具。
- **Built-in tools**：檔案／Shell、terminal、skills、session policy、spawn、model listing、檔案上傳、排程與協作等。

### Skills 與 instructions

Agent 可以透過 `prompt`／`instructions` 置入作者定義的行為規則，也可宣告 skills，由 runtime 在有 `load_skill` 工具時提示模型按需載入。框架自己的 lifecycle／metadata instructions 會在作者與 request instructions 之後附加，避免將 runtime policy 混入可攜式 agent spec。

## 4. LLM 與資料流

一次典型請求大致經過以下流程：

1. Client 將訊息送到 conversation/session API。
2. Server 將 session 工作轉送給已註冊的 runner。
3. Runner 解析 agent spec，解析 auth、model、tools 與 sandbox。
4. Runtime 組合 system instructions、對話歷史與 tool schemas。
5. Harness adapter 將統一的 runtime 呼叫轉換成 vendor SDK、CLI 或 ACP 訊息。
6. LLM 回傳文字、tool call 或要求使用者核准的事件。
7. Runner 執行工具；policy engine 在 request、tool call、tool result 等 enforcement point 檢查。
8. 事件透過 WebSocket tunnel 回 server，再以 SSE／WebSocket 推送至各個 client。
9. 對話、工具結果、成本與檔案等資訊持久化，供重連、fork、分享與後續 turn 使用。

LLM adapter 位於 `omnigent/llms`，可見 Anthropic、OpenAI、Bedrock、Gemini、Vertex、Databricks 等 provider adapter 與 routing、usage observer、context-window、retry 等元件。對話 API 採 session／conversation 模型；從非最新 response 繼續時會建立 fork，使每條 conversation 維持線性 thread。

## 5. 安全性與治理

### Policy engine

Policy 的結果有三種：

- `ALLOW`：繼續執行。
- `DENY`：阻擋動作並回傳錯誤。
- `ASK`：暫停，要求使用者核准；核准後等同 `ALLOW`，拒絕後等同 `DENY`。

Policy 可在三個層級設定，執行順序是 session → agent spec → server-wide；同一層依宣告順序執行，任一 `DENY` 可短路。內建能力包含：

- Shell／檔案工具核准與 tool-call 數量上限。
- 累計費用或使用者每日費用上限，超出後要求切換便宜模型或阻擋。
- 限制 skill、GitHub repo／branch、Google 資源與工作目錄。
- PII 偵測、風險評分與路由相關規則。
- 以 CEL（Common Expression Language）撰寫非圖靈完備、無副作用且可終止的條件。

### Sandbox

`omnigent/sandbox` 提供統一 sandbox primitive，實作位於 `omnigent/inner`。依平台可使用：

- Linux `bubblewrap`（`linux_bwrap`）
- macOS `seatbelt`（`darwin_seatbelt`）
- Windows Job Object（`windows_jobobject`，主要提供 process-tree containment 與資源限制）
- 明確設定的 `none`

`os_env` 可以限制 working directory、read/write paths、network 與傳給 agent 的環境變數。環境變數採 deny-by-default，只傳入共用基礎變數與 harness 所需的 family；需要其他 secret 時必須明確列在 `env_passthrough`。

Credential proxy 進一步讓 sandbox 內的工具使用外部服務而不持有真實 token：L7 egress proxy 在對外請求時附加 credential，sandbox 內只看到 placeholder。這對 Databricks CLI 等情境特別有用，但必須搭配網路隔離 backend 與明確的 `egress_rules`。

### Bundle 與輸入安全

Agent bundle 上傳會經過暫存解壓、路徑穿越防護、spec validation，以及在不受信任上傳路徑啟用的 handler allowlist。載入 tenant-supplied bundle 時不應從 server process 環境展開 `${VAR}`，以避免 spec 控制的連線設定讀出 server secret。

## 6. Server API 與持久化

API 主要分成：

- `/api/agents`：agent bundle 的建立、列出、查詢與刪除。
- `/v1/conversations`：對話查詢、歷史與 fork。
- `/v1/sessions`：長時間執行的 session-first API、session stream 與協作。
- `/v1/sessions/{session_id}/resources/files`：session scope 的不可變檔案資源。
- runner tunnel、terminal attach、sharing、projects、policies、usage、scheduled tasks 等專用 route。

資料層使用 SQLAlchemy 與 Alembic migration，支援 PostgreSQL 與 SQLite 共用 schema；SQLite 適合 demo／單一 instance，PostgreSQL 是多 instance 與 production 的建議選擇。文字與 JSON 型對話內容可由 client-side compression（Zstandard）統一壓縮。Artifact／file store 可使用 local、S3-compatible backend 或 Databricks Unity Catalog Volumes 等配置。

多使用者部署可啟用內建 accounts auth；另支援 OIDC（例如 Google、GitHub、Okta、Microsoft）與特定 proxy/header auth 模式。Session 可以分享、共同駕駛（co-drive），也可以從 fork point 複製成獨立 conversation。

## 7. Web、桌面與互動層

`web/` 是以 React、TypeScript、Vite 建置的前端，使用 Zustand／TanStack Query 管理狀態與資料請求，並整合：

- Markdown、GFM、數學式、Mermaid 與 syntax highlighting。
- Monaco Editor、xterm.js terminal。
- 拖放、檔案、圖表、session／project sidebar。
- OpenTelemetry web instrumentation。
- Vitest、Testing Library 與 Storybook。

Server 可直接提供編譯後 SPA；macOS desktop app 以 Electron 包裝同一個 Web UI，並額外提供 OS notification 與 dock badge。CLI 與瀏覽器使用同一個 session，因此可從 terminal 啟動後在手機或瀏覽器接續。

## 8. 部署模式

官方部署文件將 server 與 runner 分開：

- **Docker Compose**：共用 Docker image，可搭配 PostgreSQL。
- **Render／Railway**：一鍵部署並可自動配置 managed PostgreSQL。
- **Fly.io／Hugging Face Spaces／Modal**：依平台特性提供部署樣板。
- **Cloudflare Containers + D1 + R2**：serverless、scale-to-zero 路徑。
- **Databricks Apps**：以 Lakebase PostgreSQL 與 Unity Catalog Volumes 取代一般 Postgres／artifact backend。
- **Tailscale／Cloudflare quick tunnel**：將本機 server 安全或快速暴露給其他裝置，不必另建完整雲端 server。

部署時的關鍵考量：

1. Server 需要穩定 URL，runner 以 `WS /v1/runner/tunnel` 回連。
2. 多 server instance 應使用 PostgreSQL；SQLite 受限於單 instance 與持久磁碟。
3. UI 的 session stream 是長時間 SSE 連線，正式多使用者部署宜在 Uvicorn 前放置支援 HTTP/2 的 TLS reverse proxy。
4. Managed sandbox provider（如 Modal、Daytona、Blaxel、E2B、Kubernetes、OpenShell、Boxlite 等）是 runner／host 執行選項，不等同於 server 部署目標。

## 9. 安裝與開發

基本需求是 Python 3.12+；可使用 `uv tool install omnigent` 或 repository installer。不同 provider、sandbox、SDK harness、tracing、storage 與 memory 整合透過 optional extras 拆分，避免預設安裝載入所有重量級依賴。

常見操作：

```bash
# 啟動互動式本地工作階段
omnigent

# 啟動指定 harness
omnigent claude
omnigent codex
omnigent pi

# 執行 YAML agent
omnigent run path/to/agent.yaml

# 啟動 server／註冊本機 host
omnigent start
omnigent host https://your-server
```

Repository 同時包含 Python backend／runtime、React web、Electron 與 mobile 目錄、部署樣板、examples 與大量測試。開發流程提供 `just dev`、`just lint`、`just lint-all`、`just run-ios`、`just run-android` 等 shortcut；前端則可使用 `pnpm dev`、`pnpm build`、`pnpm type-check`、`pnpm test` 與 Storybook。

## 10. 技術評估與適用情境

### 優勢

- 以 spec、runtime、harness adapter 三層抽象，降低切換 agent vendor 的成本。
- Server／runner 分離，同時兼顧遠端協作與本機程式碼、工具、credential 的可用性。
- Policy、sandbox、credential proxy 與審批模型形成較完整的 agent governance 基礎。
- YAML agent bundle 適合版本控制、複製、分享與由 agent 自動產生。
- API、SSE、WebSocket、CLI、Web UI 與多種部署 target 提供完整產品化路徑。

### 需要注意

- 專案仍處 Alpha，harness 能力與相容性應透過實際 capability bench 驗證，不宜只依名稱推定功能一致。
- 不同平台的隔離能力不同；Windows Job Object 不提供 Linux／macOS 等級的 filesystem、network sandbox。
- 每個 provider／SDK 的認證、model id、streaming、tool approval 與 reasoning effort 語意可能不同。
- SQLite 適合單機或 demo；正式多使用者與水平擴展應規劃 PostgreSQL、artifact persistence、TLS reverse proxy 與備份。
- 代理可執行 Shell、檔案操作與外部 MCP；部署前應以最小權限設定 `os_env`、policy、egress 與 environment passthrough。

## 結論

Omnigent 的技術核心不是重新實作一個 LLM agent，而是建立一個可插拔的 agent operating layer：以 YAML 描述 agent，以 runtime 統一推理與工具生命週期，以 harness adapter 對接各家 agent，以 server／runner tunnel 支援遠端控制，再用 policy、sandbox、auth、持久化與 Web UI 將它包裝成可協作、可治理、可部署的系統。對需要同時管理多種 coding agent、模型 provider、工具與執行環境的團隊而言，它提供了一個集中控制與逐步擴充的架構；但在導入 production 前，仍應針對目標 harness、部署平台、隔離邊界與資料持久性進行端到端驗證。
