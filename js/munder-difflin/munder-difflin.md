# Munder Difflin 技術摘要

- Git repo
  - https://github.com/chaitanyagiri/munder-difflin
- Website
  - https://munderdiffl.in/

> [!NOTE]
> Agent harness to run an office of your clones

## 2026-08-27

- 已經忘了是否在 LinkedIn 上看到這個專案，挺有趣的～設計成有點像遊戲一樣的界面。

## 2026-09-01

> 本摘要依據 [chaitanyagiri/munder-difflin](https://github.com/chaitanyagiri/munder-difflin) repository 的 README、`HIVE.md`、`SPEC.md`、`DESIGN.md` 與 `TELEMETRY.md` 整理；版本背景以 repository README 所標示的 v0.4.6 為準。

## 1. 專案定位

Munder Difflin 是一個以 Electron 製作的本機優先（local-first）多代理人 harness。它不重新實作各家 AI 模型或取代既有的 coding CLI，而是將使用者已安裝的終端機代理程式包裝成可管理、可觀察、可協作的 agent fleet。

支援的 engine 包含 Claude Code、Antigravity、OpenAI Codex、xAI Grok、Kimi Code、Gemini CLI、Qwen、OpenCode、Crush、pi.dev、GitHub Copilot CLI、Cursor，以及自訂命令。每個 agent 都保有原本 CLI 的執行能力，並額外取得：

- 獨立的工作目錄、身分與角色設定
- 以 pseudo-terminal 執行的真實終端機工作階段
- 長期記憶與語意搜尋
- inbox/outbox 郵件信箱
- 共用 blackboard、任務帳本與事件紀錄
- 在 2D 辦公室樓層上的可視化 avatar

系統的主要互動入口是 GOD agent（化身 Michael），使用者將工作交給它，再由它進行分派、路由、協調與必要的人機協作升級。

## 2. 整體架構

系統採 Electron 的 main process、preload bridge 與 React renderer 分層，並將資料流拆成兩個互補的 plane：

```text
React renderer
   │ typed IPC / contextBridge
   ├── Event plane：hooks、hive、router、GOD、memory
   └── Terminal plane：node-pty、檔案系統、Git
           │
      真實的 agent CLI processes
```

### 2.1 Terminal plane

Electron main process 中的 `PtyManager` 透過 `node-pty` 啟動各個 CLI agent，並以 agent id 為單位將終端輸出送到 renderer（例如 `pty:data:<id>`）。renderer 透過 preload 的 typed `window.cth` API 與主程序溝通，而不是直接接觸 Node.js 或作業系統資源。

Terminal plane 同時提供：

- PTY 的 spawn、write、resize、kill 與 output stream
- xterm.js 終端機渲染，保留 ANSI 與原始輸出體驗
- 經主程序仲介的 sandboxed filesystem 操作
- Git 操作、歷史、diff、branch compare 與受保護的 checkout
- 選配的 per-agent Git worktree，降低並行修改互相衝突的機率

### 2.2 Event plane

Event plane 處理結構化的 agent lifecycle 與協作訊息。`hooks.ts` 啟動 hook server，provider-specific shim（如 `cth-hook`、`agy-hook`）將 CLI lifecycle payload 傳回應用程式。這些事件可驅動：

- agent 狀態更新與 avatar 動畫
- 工具使用站點（檔案、Terminal、Web 等）的視覺映射
- mailbox 唤醒與 Stop-loop
- router 的訊息投遞
- 活動紀錄、任務狀態與 observability 資料

這種分離使終端輸出的「位元組真實性」與 agent 狀態的「結構化語意」各自由適合的管線處理，避免只靠終端文字解析來猜測 agent 正在做什麼。

## 3. Hive 多代理協作層

Hive 是一個位於 `<harnessHome>/hive/` 的本機 Git repository，採 markdown/JSON 檔案作為協作與稽核介面。其核心設計是「single committer」與「single writer per file」：agent 不直接執行 Git，只有 Electron main process 負責 commit，以避免多個並行 agent 同時操作 `.git/index` 造成 `index.lock` 衝突。

### 3.1 檔案結構

```text
hive/
  PROTOCOL.md          # agent 協作契約
  registry.json        # agent roster、角色、能力與狀態
  board.md             # 共用 blackboard / 協作計畫
  tasks.json           # 任務帳本
  log.jsonl            # append-only 事件流
  agents/<agentId>/
    identity.md        # 身分、角色與能力
    memory.md          # agent 長期記憶
    inbox/             # 收到的訊息
    inbox/.done/       # 已處理訊息，保留稽核記錄
    outbox/            # 待 router 投遞的訊息
    cursor.json        # 已處理訊息游標
```

訊息使用「一檔一訊息」模型，先寫入暫存檔，再以 atomic rename 發佈，避免共同修改單一 mailbox 檔案。事件 log 採 append-only JSONL，各 consumer 使用自己的 cursor 追蹤進度。

### 3.2 訊息協定

訊息格式是簡化的 FIPA/KQML-like speech-act schema，包含 id、conversation、回覆關係、寄件者、收件者、act、subject、body、hop count 與 human escalation 標記。常見 act 有 `request`、`inform`、`propose`、`query`、`agree`、`refuse` 與 `done`。

為避免協作陷入 livelock：

- 只有 `request`、`query`、`propose` 必須回覆
- 每次回覆增加 `hops`，超過上限後交由 GOD agent 處理
- 已處理過的 message id 以 cursor 做 idempotent 去重
- 處理完的訊息移至 `inbox/.done/`，不直接刪除

### 3.3 Router 與 GOD agent

Agent 將訊息寫入自己的 outbox，main process 的 router 監看並投遞到目標 agent 的 inbox，同時追加 log 並提交 Git。收件 agent 在目前 turn 結束時觸發 Stop hook；若仍有未讀訊息，hook 以 block decision 讓 agent 繼續工作，形成受控的 autonomous loop。

GOD agent 是一個普通的 CLI agent，但擁有較高層的協調責任：

- 維護 roster 與能力路由
- 將任務拆解並交給合適的 specialist
- 直接處理澄清、資料查詢與一般計畫調整
- 作為 `board.md` 的單一 scribe
- 維護 task ledger、重試與 checkpoint
- 對破壞性操作、支出、範圍變更或無法解決的衝突進行人機協作升級

「機制」由 Electron main process 負責；「判斷與智能」則由 GOD agent 負責，這是專案在可控性與可擴充性上的重要切分。

## 4. 記憶系統

Munder Difflin 採 markdown-first memory：每個 agent 以 `memory.md` 保存長期知識，啟動時讀取，工作過程中追加學到的內容。共用的 blackboard 用於跨 agent 的計畫與工作狀態。

在此基礎上，`memory.ts` 可整合 MemPalace CLI：

- 每個 agent 的 markdown 記憶被挖掘至共用 palace 的不同 wing
- 以檔案修改時間作增量處理，避免不必要的重建
- agent 與 UI 可使用 semantic search / wake-up 做跨 session recall
- 未安裝 MemPalace 時降級為 no-op，基本 markdown memory 仍可用
- 預設使用較輕量的 `minilm`，並提供 multilingual embedding 選項

這是一種務實的降級設計：語意索引是加速層，而不是系統運作的必要依賴。專案另規劃 memory reflection/condensation，以防止長期執行造成 `memory.md` 無限制成長。

## 5. Agent 狀態與視覺化

Renderer 使用 React 管理控制介面，Pixi.js 建立 2D office floor。每個 agent 對應一個 avatar，依實際 lifecycle event 在 desk、file shelf、terminal station、web portal、task board 或 mailbox 等位置移動。

典型狀態流如下：

```text
idle → alert → thinking → working → success → idle
                         └────→ blocked / waiting
```

狀態並非純裝飾：

- 在 file shelf 表示讀寫檔案
- 在 terminal station 表示執行 shell command
- 在 mailbox 揮手表示需要使用者輸入
- 坐在 desk 表示工作完成或等待新任務
- ghost 表示底層 process 已消失，經過保留時間後封存

終端畫面使用 xterm.js，提供真實的 terminal stream；辦公室 floor 使用 Pixi.js，適合持續動畫、tile map、camera 與 sprite。這兩者共享 agent state，但不混用渲染責任。

此外，Command Center 提供較偏資料與控制的介面，包括：

- tasks dependency-aware Kanban
- fleet monitoring、activity log 與 CI watcher
- memory search 與 hive message threads
- agent approvals、steer/stop 控制
- Monaco IDE、檔案樹與 Git rails
- skills catalog、scheduled missions 與 heartbeat
- 多視窗 floor、session resume 與 provider 設定

## 6. 安全性、可靠性與成本控制

專案將可靠性視為多代理系統的核心問題，而非僅是 UI 功能：

1. **單一提交者**：避免 Git index lock 與並行 commit 破壞協作狀態。
2. **原子檔案投遞**：temp-file + rename 確保 mailbox 不會讀到半成品。
3. **游標與 hop cap**：分別處理重複訊息與 agent 間無限對話。
4. **Stop hook guard**：使用 `stop_hook_active` 避免 Stop-loop 自我遞迴。
5. **Circuit breaker**：對 loop、錯誤風暴或預算超支提供 steer → constrain → stop 的控制階梯。
6. **Human-in-the-loop**：涉及支出、破壞性操作與範圍變更時，回到 agent 原生的 permission prompt 或 GOD agent 的升級流程。
7. **Secret broker**：provider API key 以 write-only 方式管理，不直接暴露於一般 UI 資料流。
8. **Sandboxed bridge**：檔案與 Git 存取由 main process broker，renderer 僅使用 typed preload API。
9. **成本與用量帳本**：根據 transcript、model pricing 與 durable ledger 進行成本歸因，並搭配 OTel spans 與 tool waterfall 觀測。

## 7. 技術堆疊與專案結構

主要技術如下：

| 層次 | 技術 | 職責 |
|---|---|---|
| Desktop runtime | Electron | main、preload、renderer 與跨平台封裝 |
| UI | React + TypeScript | 控制面板、設定、任務與資料視圖 |
| 2D world | Pixi.js | office floor、sprite、動畫與路徑 |
| Terminal | `@xterm/xterm` | ANSI terminal rendering |
| Process | `node-pty` | 啟動與控制真實 CLI process |
| Editor | Monaco / CodeMirror | 內建檔案編輯與語言支援 |
| Persistence | SQLite / `better-sqlite3` | 視窗狀態、歷史、成本與 durable data |
| State | Zustand | renderer store 與事件狀態 |
| Build | electron-vite、electron-builder | 開發、打包與發佈 |
| Memory | MemPalace CLI（optional） | 語意索引與跨 session recall |

`src/main/` 負責 window、IPC、PTY、hive、hooks、memory、config、transcript、telemetry、breaker、Git 與檔案系統；`src/preload/` 暴露安全的 `window.cth` API；`src/renderer/src/` 則包含 React app、Command Center、Pixi office scene、store、hooks 與各種控制元件。

## 8. 建置與執行

必要條件包括 macOS、Windows 或 Linux、Node.js 18+、npm、`node-pty` 所需的 C/C++ toolchain，以及至少一個支援的 agent CLI。基本流程：

```bash
git clone https://github.com/chaitanyagiri/munder-difflin.git
cd munder-difflin
npm install
npm run dev
```

常用命令：

```bash
npm run build       # electron-vite production build
npm run preview     # 預覽 production build
npm run typecheck   # node/main/preload 與 web/renderer 型別檢查
npm run dist        # build + electron-builder
```

`npm install` 的 postinstall 會執行 Electron ABI 對應的 `electron-rebuild`，並處理 `node-pty` 的平台權限與相容性；若 Electron 升級後 PTY 無法載入，通常需要重新安裝依賴。

## 9. Telemetry 與隱私

官方 build 只傳送受 allowlist 限制的匿名使用事件，例如 app 啟動、agent spawn、onboarding 完成、功能使用與粗略 session duration。共用欄位僅包含 app version、OS 與 CPU architecture。

特別值得注意的是：`message_sent` 只記錄使用者從哪個 surface 傳送訊息（terminal、composer、steer 或 hive），不傳送訊息內容、長度、字數、雜湊、prompt、transcript、檔案路徑或 agent output。系統使用隨機 UUID 作為安裝識別，不從機器硬體或網路資訊推導身份，也停用 GeoIP/IP 衍生位置。

使用者可透過 Settings、`DO_NOT_TRACK` 或自行從 source build 完全停用 telemetry；fork/local build 因沒有官方 PostHog key，預設不會送出事件。

## 10. 設計評估

Munder Difflin 的核心價值在於把「多個可獨立運作的 CLI agent」提升成具備協調、記憶、稽核與可觀察性的本機 agent operating environment。其設計取捨可概括為：

- 以既有 CLI 為 runtime，降低重新實作模型工具鏈的成本
- 以檔案與 Git 作為透明、可稽核且容易除錯的協作媒介
- 以 main process 集中掌握 process、檔案、Git 與路由等副作用
- 以 hook 取得結構化事件，避免脆弱的 terminal text scraping
- 以 markdown-first memory 保持可讀性，再以語意索引提升檢索效率
- 以 GOD agent 做高階編排，以人機協作處理真正需要授權的決策
- 以視覺化 floor 將抽象的 agent 狀態轉為可快速理解的空間訊號

目前仍屬 pre-release 性質；後續方向包含更多 chat integrations、更多 engine/template、完整的 avatar hook coverage，以及更持久化的 layout 與 command history。整體而言，它是一個將 Electron desktop UX、terminal process orchestration、file-based multi-agent protocol 與 human oversight 結合起來的實驗性但架構完整的多代理人工作平台。

## 參考資料

- Repository：<https://github.com/chaitanyagiri/munder-difflin>
- README：專案定位、功能、建置方式與架構總覽
- `HIVE.md`：Hive 協作層、訊息協定、router、GOD agent 與可靠性設計
- `SPEC.md`：terminal/event plane 與 agent lifecycle 的產品規格
- `DESIGN.md`：Pixi.js office floor 與 pixel UI 設計系統
- `TELEMETRY.md`：匿名事件、隱私保證與 opt-out 規則
