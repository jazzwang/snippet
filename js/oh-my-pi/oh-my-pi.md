# oh-my-pi 技術摘要

- Git Repo
  - https://github.com/can1357/oh-my-pi
- Website
  - https://omp.sh/

> A coding agent with the IDE wired in.

## 2026-09-02

- 同仁推薦我使用 omp (oh-my-pi) 會比自己慢慢設定 pi coding agent 容易上手
- 讀了 [Oh My Pi（omp）是什麼？終端機 AI Coding Agent 入門介紹](https://kamadiam.com/oh-my-pi-introduction/)，比較了解 omp 跟 pi 兩者的差異。
- 以下是 GPT 5.6 Luna 生成的技術摘要：

> 參考專案：<https://github.com/can1357/oh-my-pi>  
> 摘要基準：專案 `README.md`、根目錄 `package.json` 與公開檔案樹；內容以目前主分支公開資訊為準。

## 1. 專案定位

**oh-my-pi（OMP）** 是以 Pi coding agent 為基礎延伸的開放原始碼程式開發代理（coding agent）。它不是單純的聊天介面，而是把檔案系統、Shell、語言伺服器、除錯器、瀏覽器、桌面自動化、網路搜尋與多代理協作整合到同一套工具介面中。

其核心設計目標是「讓代理具備 IDE 級的上下文與操作能力」，並降低傳統代理常見的問題：

- 只能依賴外部 `grep`、`find` 或 `bash`，造成跨平台與 fork/exec 成本。
- 以文字取代結構化程式碼操作，容易產生錯誤或過時 patch。
- 代理只能讀取檔案，無法使用 IDE 已知的符號、診斷與重命名資訊。
- 長任務缺乏子代理、審查、記憶與可恢復的工作流程。
- 每個供應商或服務都需要一組不同的工具與參數，增加模型學習負擔。

README 所列的規模指標包括 60 多個模型供應商、31 個內建工具、14 種 LSP 操作、28 種 DAP 操作，以及約 80,000 行 Rust 核心程式碼。這些數字是專案目前的自述指標，實際數量會隨版本演進變動。

## 2. 高階架構

OMP 採用 **TypeScript/Bun 應用層 + Rust 原生核心 + N-API 連接層** 的混合架構：

```text
使用者 / TUI / ACP / Web 協作介面
                │
      TypeScript coding-agent 應用層
  ┌─────────────┼──────────────────┐
  │             │                  │
模型與路由     工具編排           工作階段/記憶/協作
  │             │                  │
  └─────────────┴──────────────────┘
                │ N-API
         Rust 原生能力層
  Shell · walker · AST · PTY · LSP/DAP 支援 · 桌面/影像/語音
                │
     macOS / Linux / Windows 原生平台
```

### 2.1 TypeScript 與 Bun

根目錄以 Bun 作為套件管理與執行環境，使用 workspace 管理 `packages/*` 與 Python 相關工作區。`packages/coding-agent` 是主要 CLI 與代理執行入口，周邊套件則負責模型、TUI、原生模組、Wire 通訊、統計與記憶等功能。

根目錄 `package.json` 顯示專案同時提供：

- TypeScript 編譯、格式化與 lint 檢查。
- Rust 測試、lint、格式化與 Bazel 任務。
- 原生二進位建置與多平台 release。
- Web 協作介面與 relay。
- Python/robomp 執行環境與整合測試。
- Docker、Nix、Home Manager 等部署方式。

### 2.2 Rust 原生核心

Rust 用於高頻率、跨平台或需要系統整合的部分，再透過 N-API 提供給 Bun/Node 應用層。README 列出的主要 crate 如下：

| Crate | 主要責任 |
|---|---|
| `pi-natives` | 對外提供各種 Rust 原生模組的 N-API 介面 |
| `pi-shell` | 持久化 Shell、嵌入式 bash、內建命令與輸出最小化 |
| `pi-walker` | 平行、忽略規則感知的檔案遍歷與掃描快取 |
| `pi-iso` | 工作區隔離、reflink、overlayfs、APFS/Btrfs/ZFS 等平台能力 |
| `pi-ast` | tree-sitter/ast-grep 解析、結構化搜尋與 AST 編輯 |
| `pi-voice` | 音訊擷取、播放、Opus 與 WebRTC 能力 |

專案也維護 `crates/pi-builtins`，將常見命令列工具整合到 Shell 執行環境中，例如 `ls`、`sed`、`sort`、`xargs`、`jq`、`find`、`diff` 與 ripgrep 相關能力。這種設計可在 Windows 等沒有 Unix 工具鏈的環境提供一致行為，也減少反覆建立子程序的成本。

## 3. 代理工具表面

OMP 的重要抽象是：**工具盡量以一致的路徑或檔案介面呈現**。例如 GitHub PR、衝突、子代理結果與技能資源，均可透過 `pr://`、`conflict://`、`agent://`、`skill://` 等內部 URI 存取；模型不必為每種後端學習完全不同的 API 形狀。

### 3.1 檔案與搜尋

- `read`：讀取檔案、目錄、壓縮檔、SQLite、PDF、Notebook、URL、SSH 路徑及內部 URI。
- `write`：建立或覆寫檔案，也可操作部分特殊資源。
- `edit`：以 hashline anchor 進行內容雜湊定位的 patch，避免因空白或內容過時造成錯誤替換。
- `ast_edit`：以 AST/ast-grep 執行結構化修改，先產生提案再套用。
- `ast_grep`：針對 50 多種 tree-sitter grammar 執行結構化查詢。
- `grep` / `glob`：提供正規表示式內容搜尋與 glob 路徑查找。

### 3.2 執行環境

`bash` 使用持久化工作階段，並可搭配 PTY 與內建命令；`eval` 則提供持久化 Python 與 JavaScript/Bun cell。兩種執行核心都能透過 loopback bridge 回呼代理工具，因此程式碼執行環境不只是沙盒，而是能繼續呼叫 `read`、`search`、`task` 等能力的工作環境。

### 3.3 程式碼智慧

- `lsp`：診斷、跳轉、符號、重命名、code action 及 raw request。
- `debug`：透過 DAP 控制 lldb、dlv、debugpy 等除錯器，支援 breakpoint、step、thread、stack、scope 與 variable。
- `security_scan`：規劃並執行原生安全檢查。

LSP 與寫入流程緊密整合。以檔案重命名為例，代理不只是移動檔案，也可先經過 `workspace/willRenameFiles`，讓 re-export、barrel file 與 alias import 一併更新。

### 3.4 協作與工作流程

- `task`：平行啟動子代理，可使用隔離工作樹，並以 schema 驗證的結構化結果回傳。
- `hub`：監控、傳訊息、等待、恢復或取消長時間執行的代理。
- `todo`：管理有順序及階段狀態的工作清單。
- `advisor`：使用另一個模型觀看主代理每一回合，插入提醒、疑慮或阻擋事項。
- `/review`：平行啟動專門審查代理，以 P0–P3 優先級與信心分數整理問題。
- `/collab`：透過 relay 分享即時 session，可使用瀏覽器或 `omp join` 加入，並提供唯讀或可寫模式。

## 4. 可靠編輯與代理控制

### 4.1 Hashline 編輯

OMP 的 `edit` 不要求模型重新輸出大量原始程式碼，而是使用帶有內容雜湊的 anchor 指定修改位置。套用時會重新驗證 anchor：

1. 模型提出帶 anchor 的修改。
2. 工具以目前檔案內容驗證 anchor。
3. 若檔案已被其他變更修改，anchor 不一致時拒絕套用。
4. 只有驗證通過才寫入檔案。

這種 optimistic concurrency 控制能避免 patch 套到錯誤位置，也能減少「字串找不到」與重試造成的 token 消耗。

### 4.2 AST 編輯的兩階段提交

`ast_edit` 先回傳包含替換數量的 proposed card，修改保持在暫存狀態；代理再將理由寫入 `xd://resolve`，由 TUI 轉成 Accept 操作，最後以原子方式套用。這將「產生修改」與「確認修改」分離，適合大範圍 codemod 或高風險重寫。

### 4.3 Time-traveling stream rules

串流規則可在模型輸出違反規範時即時介入。當輸出符合指定 regex 時，OMP 會：

1. 中止目前串流。
2. 注入規則作為系統提醒。
3. 從相同位置重試輸出。
4. 將注入內容保留到後續壓縮後的上下文。

這種方式避免每回合都把所有規則塞入 prompt，同時能在模型偏離時及時修正。

## 5. 模型、搜尋與記憶

### 5.1 多模型角色路由

OMP 將模型分配為角色，而不是只設定一個全域模型。README 提到的角色包括 `default`、`smol`、`slow`、`plan`、`commit`、`vision`、`task`、`advisor` 與 `tiny`。因此可用便宜模型執行子代理 fan-out，以高推理模型處理規劃，再用專用模型執行審查或提交訊息。

路由層支援：

- 多家 frontier API、coding plan、OAuth 與本地 OpenAI-compatible server。
- 自訂 provider 與多種 API protocol。
- 每個角色或模型的 fallback chain。
- 依路徑設定啟用/停用模型與 provider。
- 同一 provider 的多組 credential 輪替與 backoff。

### 5.2 內建網路搜尋

`web_search` 可依設定走多個搜尋後端，並將搜尋結果交給 site-aware extractor。README 列出的特殊處理涵蓋 GitHub/GitLab、npm/PyPI/crates.io 等套件註冊站、arXiv、Semantic Scholar、Stack Overflow、Reddit，以及 MDN、Read the Docs、docs.rs 等文件來源；PDF 與網頁會轉成保留連結與 anchor 的結構化 Markdown。

這種設計讓代理以同一種工具使用本地檔案、遠端文件與研究資料，並降低直接處理 HTML 或 PDF 的複雜度。

### 5.3 跨 session 記憶

記憶功能由代理主動維護：

- `retain`：在執行期間保存事實。
- `learn`：記錄可重用的經驗與教訓。
- `recall`：查詢既有記憶。
- session 壓縮：將工作脈絡整理成下一次啟動可載入的 mental model。

記憶後端可設定為 local、Hindsight 或 Mnemopi，預設以專案範圍隔離，避免不同 repository 的知識互相污染。

## 6. 桌面、瀏覽器與編輯器整合

OMP 不只控制瀏覽器 DOM，也提供更廣泛的自動化邊界：

- `browser`：以 Puppeteer/Chromium、CDP 附加應用程式，或透過 relay 接管使用者既有 Chrome 分頁。
- `computer`：持久化 JavaScript，支援視窗與螢幕列舉、截圖、原生輸入、OS accessibility tree 與剪貼簿。
- ACP：讓 OMP 在 Zed 等編輯器內執行，讀取目前 buffer、透過編輯器儲存路徑寫入，並使用編輯器終端機。
- `/collab`：將 agent session 以加密框架分享給隊友；README 說明 relay 不直接看見使用者金鑰。

這些整合使代理能從「修改 repository」延伸到「觀察與操作實際開發環境」，但也代表權限、憑證、瀏覽器 session 與桌面輸入必須採取更嚴格的使用者授權策略。

## 7. 建置、平台與發布

### 7.1 支援平台

README 列出的原生平台包括：

- `linux-x64`
- `linux-arm64`
- `darwin-x64`
- `darwin-arm64`
- `win32-x64`

在 macOS/Linux 可透過安裝腳本、Homebrew、Bun、Nix 或 mise 安裝；Windows 提供 PowerShell 安裝方式。專案也提供 Docker 與 Nix flake/Home Manager 整合。

### 7.2 Build system

JavaScript 以 Bun workspace 管理；Rust 則同時使用 Cargo 與 Bazel 設定，並在 CI 中執行 TypeScript、Rust、Python、原生模組、安裝方法與 release 檢查。`package.json` 可見的品質門檻包括 oxlint、oxfmt、Rust lint/fmt、單元測試、整合測試與跨平台二進位建置。

### 7.3 Shell completion

`omp completions` 根據 CLI 即時 command/flag metadata 產生 bash、zsh 與 fish completion。模型名稱、enum 值與磁碟上的 session 也能提供補全，避免手工維護補全腳本與實際 CLI 行為不一致。

## 8. 技術優勢

1. **IDE 級上下文**：LSP、DAP 與 AST 工具讓代理可依符號與語法結構工作，而非只依賴文字搜尋。
2. **跨平台一致性**：將 Shell、搜尋與常用命令整合到原生核心，降低對 Unix 外部程式的依賴。
3. **較安全的修改流程**：hashline 驗證、AST preview、衝突 URI 與原子接受機制降低誤寫風險。
4. **可擴展的代理編排**：子代理、advisor、Agent Hub、審查與隔離工作樹適合大型任務。
5. **供應商解耦**：角色化路由、fallback、credential rotation 與自訂 provider 讓模型層可替換。
6. **統一資源介面**：FS-shaped URI 將 PR、issue、agent 結果與衝突等資源納入既有 `read`/`write`/`grep` 模型。
7. **效能導向**：Rust 原生模組、平行 walker、快取、內嵌命令與持久化執行環境減少重複啟動成本。

## 9. 可能的工程取捨

- **系統複雜度高**：同時維護 TypeScript、Rust、Python、Bazel、Cargo、Bun 與多平台 native artifact，會增加建置與除錯成本。
- **安全邊界更寬**：Shell、瀏覽器、桌面輸入、SSH、DAP 與協作 relay 都可能接觸敏感資料，部署時應限制權限並審核模型可使用的工具集合。
- **模型路由需要治理**：多 provider、OAuth、coding plan 與 fallback 雖提高彈性，但也要管理費用、資料留存、速率限制與供應商政策。
- **原生依賴的跨平台負擔**：桌面、音訊、PTY、瀏覽器與檔案系統隔離功能在不同 OS 上的行為可能不完全一致。
- **版本變動快速**：README 的功能數字、模型清單與 provider 支援會持續更新，正式導入時應以特定 release/tag、CHANGELOG 與 CI 結果作為依據，而非只依賴主分支文件。

## 10. 適用情境

OMP 特別適合：

- 需要代理直接處理大型 repository 的團隊。
- 重視跨平台 CLI、Windows 原生支援與低 fork/exec 成本的開發環境。
- 需要 LSP 重構、真實除錯器、AST codemod 或安全掃描的工程任務。
- 要把一項工作拆成多個隔離子任務並集中審查結果的團隊。
- 需要在本地模型、雲端 API、coding plan 與多家 provider 間切換的使用者。

若需求只是簡單的問答、單檔案修改，OMP 的完整功能可能超出必要範圍；其主要價值在於長流程、跨工具與需要驗證的軟體工程工作。

## 11. 結論

oh-my-pi 的核心特色不是單一模型或單一工具，而是將代理執行環境做成一個完整的、可組合的工程平台：TypeScript/Bun 負責代理體驗與流程編排，Rust 負責高效能及跨平台原生能力，LSP/DAP/AST 提供 IDE 級程式碼理解，URI 型工具介面統一本地與遠端資源，子代理、advisor、記憶及協作功能則延伸了單一 agent session 的能力。

從架構角度看，OMP 試圖解決的是 **agent harness problem**：模型本身只是推理核心，真正決定軟體工程可靠度的，還包括工具契約、編輯驗證、上下文壓縮、執行環境、錯誤恢復、權限控制與結果審查。這也是它以原生核心、結構化工具與多層工作流程作為主要技術投資的原因。
