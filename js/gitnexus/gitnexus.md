# GitNexus

- Git Repo
  - https://github.com/abhigyanpatwari/GitNexus
- 2026-04-07
  - 知識圖譜改變程式碼探索：GitNexus 在瀏覽器內把程式碼庫變成一張關係網
  - https://ithelp.ithome.com.tw/articles/10399650

## 2026-09-15

> [!Question]
>

## GitNexus 技術簡介與功能驗證指南

> 參考專案：[abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus)
>
> 本文件以 GitNexus GitHub 儲存庫的 README 與 CLI 說明為基礎，整理成一套可以實際執行的驗證流程。GitNexus 的版本與工具數量可能持續變動；如果命令列輸出與本文不同，請以該版本的 `--help`、MCP 的 `tools/list` 和官方 README 為準。

### 1. GitNexus 是什麼？

GitNexus 是一個程式碼知識圖譜工具。它會分析 Git 儲存庫，把檔案、符號、函式呼叫、匯入關係、執行流程與功能群組整理成可查詢的圖，接著透過 CLI、MCP 和網頁介面提供查詢結果。

它處理的問題很實際：大型專案裡，改一個函式往往不只影響同一個檔案。只做關鍵字搜尋，容易漏掉間接呼叫者、相關測試或另一個模組中的相依關係。GitNexus 的重點，是在建立索引時先整理這些關係，讓後續的搜尋、影響分析和程式碼探索不必從零開始拼圖。

GitNexus 的主要元件如下：

- **分析器與索引器**：讀取程式碼，建立知識圖譜與全文搜尋索引。
- **CLI**：執行分析、查看狀態、查詢圖譜、啟動服務與清理索引。
- **MCP Server**：讓 Claude Code、Cursor、Codex、Windsurf 等支援 MCP 的工具呼叫 GitNexus。
- **Web UI**：在瀏覽器中檢視圖譜、探索程式碼並進行對話。
- **Agent skills 與 hooks**：協助 AI agent 在探索、除錯、影響分析和重構前，先取得架構脈絡。

### 2. CLI、MCP 與 Web UI 怎麼分工？

| 使用方式 | 適合情境 | 主要驗證重點 |
| --- | --- | --- |
| CLI | 開發者直接操作，或在 CI／腳本中使用 | 能否成功分析、更新、查詢與清理索引 |
| CLI + MCP | 日常搭配 AI agent 開發 | agent 是否能取得正確的程式碼脈絡與影響範圍 |
| Web UI | 快速展示、探索陌生專案或不想先設定編輯器 | 能否載入儲存庫、瀏覽圖譜和提出查詢 |
| `gitnexus serve` | 讓本機索引提供給 Web UI | CLI 建立的索引能否被瀏覽器服務使用 |

一般開發流程是：先用 `analyze` 建立索引，再用 `setup` 設定 MCP。索引完成後，AI agent 才有足夠的圖譜資料可以查詢。

### 3. 測試前準備

#### 3.1 建議環境

準備以下工具：

- Git
- Node.js 與 npm
- 一個可以讀取 MCP 工具的客戶端，例如 Claude Code、Cursor 或 Codex
- 一個可分析的 Git 儲存庫

建議先用小型測試專案驗證安裝和流程，再對大型產品專案建立索引。這樣比較容易判斷問題是安裝環境造成的，還是專案本身的語言與規模造成的。

#### 3.2 建立隔離測試專案

以下指令會建立一個簡單的 JavaScript 專案。它刻意保留幾層函式呼叫，方便測試 `context`、`impact` 和 `trace`。

```bash
mkdir gitnexus-demo
cd gitnexus-demo
git init
mkdir src test
```

建立 `src/user.js`：

```js
export function validateUser(user) {
  return Boolean(user && user.name);
}
```

建立 `src/login.js`：

```js
import { validateUser } from './user.js';

export function login(user) {
  if (!validateUser(user)) {
    throw new Error('invalid user');
  }
  return { ok: true };
}
```

建立 `test/login.test.js`：

```js
import { login } from '../src/login.js';

export function testLogin() {
  return login({ name: 'Ada' });
}
```

最後提交一次，讓後面的變更偵測測試有基準點：

```bash
git add .
git commit -m "create GitNexus demo project"
```

### 4. Step-by-step 功能測試

#### Step 1：確認 CLI 可以執行

不用先全域安裝，也可以用 `npx` 直接執行：

```bash
npx gitnexus@latest --help
```

**預期結果**：看到 GitNexus 的命令列說明，以及 `analyze`、`setup`、`mcp`、`serve`、`status`、`list`、`clean` 等命令。若使用公司網路或 npm 11 遇到安裝問題，可改用全域安裝或依官方 README 的 pnpm 替代指令。

若希望固定使用全域版本：

```bash
npm install -g gitnexus
gitnexus --help
```

#### Step 2：分析測試儲存庫

在測試專案根目錄執行：

```bash
npx gitnexus analyze
```

或使用全域安裝版本：

```bash
gitnexus analyze
```

**預期結果**：

- GitNexus 掃描 `src` 與 `test` 中的程式碼。
- 建立本機索引與儲存庫登錄資訊。
- 顯示解析檔案、建立符號或圖譜資料的進度。
- 依版本設定，可能同時產生 agent 使用的 skills、hooks 或上下文檔案。

如果只想先驗證圖譜，不在第一次測試就等待向量嵌入，可以查看該版本是否支援並使用：

```bash
gitnexus analyze --skip-embeddings
```

如果要測試語意搜尋，再使用官方支援的 embeddings 選項重新分析。嵌入模型會增加第一次執行的時間與下載需求，應該獨立測試，不要把它和基本安裝問題混在一起。

#### Step 3：查看索引狀態

```bash
gitnexus status
gitnexus list
```

**預期結果**：

- `status` 顯示目前專案是否已有索引，以及索引是否可能過期。
- `list` 顯示 GitNexus 登錄的儲存庫。
- 測試專案應該可以在清單中找到。

這一步可以確認後續查詢到底是在正確的儲存庫上執行。多個儲存庫同時被索引時，查詢通常要明確指定 `repo`。

#### Step 4：測試命令列查詢

README 說明 CLI 提供與 MCP 對應的查詢入口。先從最容易觀察結果的查詢開始：

```bash
gitnexus query "user validation"
gitnexus context validateUser
gitnexus impact validateUser upstream
gitnexus trace validateUser login
```

不同版本的參數細節可能略有不同，若某個子命令回報用法錯誤，先執行：

```bash
gitnexus query --help
gitnexus context --help
gitnexus impact --help
gitnexus trace --help
```

**各項測試要看什麼**：

- `query`：是否找到 `validateUser`、`login` 和相關測試；若啟用語意搜尋，也觀察自然語言查詢是否能找到概念相關的程式碼。
- `context`：是否列出符號所在檔案、參照、參與的執行流程或功能群組。
- `impact ... upstream`：是否列出呼叫 `validateUser` 的上游程式碼；這是評估修改可能造成哪些影響的核心功能。
- `trace`：是否能指出兩個符號之間的最短關係路徑。

不要只看「有沒有回傳結果」。請把結果和測試專案的實際程式碼對照，確認關係方向沒有搞反，也確認測試檔案是否依該命令的預設值被排除或包含。

#### Step 5：確認 MCP Server 可以啟動

先直接啟動 MCP Server：

```bash
gitnexus mcp
```

這個程序通常會透過 stdio 等待 MCP 客戶端連線，因此啟動後沒有一般人類可讀的畫面並不代表失敗。用 `Ctrl+C` 停止即可。

更實際的做法是讓 GitNexus 自動設定支援的編輯器：

```bash
gitnexus setup
```

如果只想設定特定整合，例如 Cursor 或 Codex，可依該版本支援的選項執行：

```bash
gitnexus setup --coding-agent cursor
```

**預期結果**：

- GitNexus 找到可用的編輯器或客戶端。
- MCP 設定被寫入對應的設定檔。
- 客戶端重新載入後，可以看到 GitNexus Server。

若不使用自動設定，也可以手動加入 MCP 設定。以 Cursor 為例：

```json
{
  "mcpServers": {
    "gitnexus": {
      "command": "npx",
      "args": ["-y", "gitnexus@latest", "mcp"]
    }
  }
}
```

Windows 若遇到 `npx` 或 shell 啟動問題，請優先使用 `gitnexus setup`，或依官方 README 的 Windows 指令設定。設定完成後，完全重啟編輯器，避免它仍在使用舊的 MCP 設定。

#### Step 6：透過 MCP 做最小驗證

在 MCP 客戶端中依序做以下操作：

1. 列出可用的儲存庫或讀取 `gitnexus://repos`。
2. 讀取測試專案的 context 資源。
3. 搜尋 `user validation`。
4. 查詢 `validateUser` 的 symbol context。
5. 對 `validateUser` 執行 `impact`，方向選 `upstream`。
6. 查詢 `login` 與 `validateUser` 之間的 `trace`。

GitNexus README 列出的 MCP 工具包含以下類型；實際工具數量會隨版本增加或調整：

- `list_repos`：列出已索引的儲存庫。
- `query`：以關鍵字與語意方式搜尋程式碼。
- `context`：查看符號的完整上下文。
- `impact`：分析變更的影響範圍。
- `trace`：找出兩個符號之間的關係路徑。
- `detect_changes`：將 Git 差異對應到受影響的流程。
- `check`：執行圖譜上的結構檢查。
- `rename`：根據圖譜和文字搜尋進行跨檔案重新命名。
- `cypher`：直接執行圖譜查詢。
- `route_map`、`tool_map`、`shape_check`、`api_impact`：針對 API、MCP/RPC 和資料形狀做分析。
- `explain`、`pdg_query`：在使用 PDG 索引時查看資料流或控制／資料相依關係。

**驗收標準**：MCP 客戶端能看到工具，工具呼叫不會因為儲存庫未指定而失敗，回傳結果中的檔名、符號和呼叫方向與測試程式碼一致。

#### Step 7：測試變更偵測與增量更新

先修改 `src/user.js`，例如加入一個註解或改變驗證規則：

```js
export function validateUser(user) {
  return Boolean(user && user.name && user.name.length > 0);
}
```

接著執行：

```bash
git diff
gitnexus detect-changes
```

如果該版本只有 MCP 工具，則在 MCP 客戶端中呼叫 `detect_changes`。

再重新分析：

```bash
gitnexus analyze
```

最後重做：

```bash
gitnexus impact validateUser upstream
gitnexus context validateUser
```

**預期結果**：GitNexus 能辨識工作樹差異，重新分析後仍能找到 `login` 對 `validateUser` 的依賴。這一步同時驗證兩件事：索引更新不是只在第一次有效，以及變更後的圖譜沒有遺留舊資料。

若專案需要即時更新，也可測試：

```bash
gitnexus analyze --watch
```

在另一個終端機修改程式碼，等待索引更新，再重新查詢。停止 watcher 使用 `Ctrl+C`。

#### Step 8：測試 Web UI 與本機服務

啟動本機服務：

```bash
gitnexus serve
```

再用瀏覽器開啟 CLI 顯示的網址。GitNexus Web UI 可以用來檢視圖譜、搜尋程式碼和進行對話；本機服務模式的好處是直接使用已建立的 CLI 索引，不必再次上傳或分析同一份專案。

**預期結果**：

- 瀏覽器能連線到服務。
- 可以看到測試儲存庫。
- 能搜尋 `validateUser`，並在圖譜中看到它與 `login` 的關係。
- Web UI 顯示的資料與 CLI、MCP 查詢結果相符。

如果只是想快速體驗，也可以使用官方提供的 Web UI。但請留意：瀏覽器模式的記憶體與檔案數量限制，和本機 CLI／Server 模式不是同一個測試條件。

#### Step 9：測試 PDG 與資料流功能（選用）

若要測試 statement-level 的控制／資料相依或 taint analysis，需用 PDG 選項建立索引。先查看目前版本的參數：

```bash
gitnexus analyze --help
```

確認支援後，再執行：

```bash
gitnexus analyze --pdg
```

之後透過 MCP 呼叫 `explain` 或 `pdg_query`。這類測試比一般圖譜分析耗費更多時間，建議使用刻意包含輸入、驗證與輸出的測試專案，才看得出資料流結果。不要把「沒有找到 taint flow」直接當成工具故障；先確認測試程式碼、語言支援與索引確實包含 PDG。

#### Step 10：測試清理與重新建立

完成驗證後，測試清理功能：

```bash
gitnexus clean
gitnexus status
```

若該版本支援清理全部索引，並且目前是在隔離環境，也可以使用：

```bash
gitnexus clean --all
```

再重新執行：

```bash
gitnexus analyze
gitnexus status
```

**預期結果**：清理後查詢不應假裝仍有可用索引；重新分析後，`status` 恢復為可查詢狀態。這是確認索引生命週期和測試環境可重置的重要一步。

### 5. 一份可重複執行的驗收清單

- [ ] `npx gitnexus@latest --help` 或 `gitnexus --help` 成功。
- [ ] `analyze` 能完成小型 Git 儲存庫的索引。
- [ ] `status` 能顯示索引狀態。
- [ ] `list` 能列出已索引的儲存庫。
- [ ] `query` 能找出已知符號或概念。
- [ ] `context` 能回傳符號、檔案與參照資訊。
- [ ] `impact upstream` 能找出已知呼叫者。
- [ ] `trace` 能找出已知的關係路徑。
- [ ] MCP Server 能啟動，客戶端能看到 GitNexus 工具。
- [ ] MCP 查詢結果與 CLI 結果一致。
- [ ] 修改程式碼後，`detect_changes` 能指出相關差異或流程。
- [ ] 重新 `analyze` 後，查詢結果反映最新程式碼。
- [ ] `serve` 能讓 Web UI 讀取本機索引。
- [ ] 清理後可以重新建立索引，沒有殘留的舊資料。
- [ ] 若測試 PDG，`explain` 或 `pdg_query` 能在 PDG 索引上執行。

### 6. 常見問題與排查順序

#### `npx` 安裝失敗

先確認 Node.js 和 npm 版本，再試著全域安裝：

```bash
npm install -g gitnexus@latest
gitnexus analyze
```

如果是 npm 11 的 Arborist 錯誤，官方 README 提到可以改用 pnpm 或全域安裝。不要反覆刪除專案檔案，先把問題分辨為 npm、原生套件或 GitNexus 本身。

#### MCP Server 啟動後看不到工具

依序確認：

1. `gitnexus analyze` 是否真的在目標專案完成。
2. `gitnexus list` 是否列出該專案。
3. MCP 設定中的命令是否和實際安裝方式一致。
4. 編輯器是否已完全重啟。
5. 多個儲存庫時是否傳入正確的 `repo`。
6. Server 的 stderr 是否顯示原生模組或 Node.js 版本錯誤。

#### 查詢結果為空

先不要立刻重建所有東西。先執行 `status`，確認目前查詢的是哪個儲存庫和分支，再用已知的函式名稱查詢。若函式所在語言或副檔名不在該版本支援範圍，也可能只建立了部分索引。

#### `serve` 可以啟動，但 Web UI 沒有資料

確認 Web UI 連到的是本機 `serve` 位址，而不是沒有索引資料的另一個服務。接著用 `list` 和 `status` 確認索引存在，再重新整理瀏覽器。若使用多儲存庫模式，確認 Web UI 選到正確的儲存庫。

#### 原生相依套件或語言 grammar 安裝失敗

GitNexus 使用 Tree-sitter 和原生資料庫元件；某些語言 grammar 可能需要額外的預建二進位檔或編譯環境。先用官方 README 的相容性和安裝替代方案處理，不要把跳過某些 grammar 後的「分析不完整」誤判成完整成功。

### 7. 實務上怎麼使用比較穩

1. **先分析，再讓 agent 改程式碼。** 沒有索引時，MCP 只能啟動，不能提供完整圖譜脈絡。
2. **改動前先跑 `impact`。** 先知道上游呼叫者、相關流程和測試，再決定修改範圍。
3. **改動後跑 `detect_changes`。** 它適合用來檢查目前 diff 是否碰到預期之外的流程。
4. **大型專案分開驗證 embeddings、PDG 和基本圖譜。** 這些功能的資源需求不同，故障訊號也不同。
5. **把 CLI、MCP 和 Web UI 當成三個介面測試。** 其中一個介面正常，不代表另外兩個的設定也正確。
6. **記錄 GitNexus 版本和 Node.js 版本。** 索引格式、MCP 工具名稱和 CLI 參數可能會改變，測試結果必須能回溯環境。

GitNexus 最值得驗證的地方，不是它能不能列出一個搜尋結果，而是它能否把「某個符號在哪裡」一路回答到「誰呼叫它、會影響哪些流程、改完之後哪些地方需要重新檢查」。只要用上面的測試專案先走完一輪，再換成實際產品儲存庫，通常比較容易看出它在日常開發中的價值。

### 8. 參考資料

- GitNexus GitHub：<https://github.com/abhigyanpatwari/GitNexus>
- GitNexus README：<https://github.com/abhigyanpatwari/GitNexus/blob/main/README.md>
- GitNexus Web UI：<https://gitnexus.vercel.app>
- npm 套件：<https://www.npmjs.com/package/gitnexus>

## 實測

- 首先，用一個範例 Repo 的 ZIP 檔解開來測測看。
  - 因為遇到警告不是 git repo，所以多加上 `--skip-git` 參數。
  - 執行之後，會多兩個檔案 `AGENTS.md` 跟 `CLAUDE.md`
```bash
~/sample-code$ npx gitnexus analyze --skip-git
$ ls
AGENTS.md    CLAUDE.md
core-api     web            web-api-resources
web-auth2-guid-filter       web-authentication-filter
```
- 觀察索引狀態 `npx gitnexus status`
```
~/cdk/uip/ia.ui$ npx gitnexus status

  GitNexus Status (1.6.12)

Repository: (略)
Branch: (detached HEAD)
Indexed: 9/15/2026, 5:16:10 PM
Indexed commit:
Current commit:
Indexed analyzer runner identity: (略)
Status: ✅ up-to-date
```
- `npx gitnexus list` 列出已索引的 Git Repo
```bash
$ npx gitnexus list

  GitNexus List (1.6.12)

  Indexed Repositories (1)

  ia.ui
    Path:    (略)
    Indexed: 9/15/2026, 5:16:10 PM
    Commit:  unknown
    Stats:   1430 files, 17781 symbols, 44488 edges
    Clusters:   745
    Processes:  1279
```

> [!QUESTION]
> gitnexus 的 PDG 是什麼

在 [GitNexus](https://github.com/abhigyanpatwari/GitNexus) 中，PDG 指的是 程式相依圖（Program Dependence Graph）。 [1]

這是一種用來表示程式碼內部控制流（Control Dependence）與資料流（Data Dependence）關係的圖形結構。在 GitNexus 的使用情境中，PDG 的核心作用與功能如下：

## 1. 提供深度的代碼關係分析

GitNexus 本身是一個將程式碼庫轉換為知識圖譜的工具。當你在建立索引時加上 --pdg 參數，GitNexus 就會深入分析函數與變數之間的調用、傳遞關係： [1, 2, 3]

* 資料流（Data Flow）：追蹤某個變數或資料從哪裡輸入、經過哪些計算、最後從哪裡輸出。
* 控制流（Control Flow）：分析程式碼執行的先後順序與條件判定。 [1]

## 2. 核心應用場景
開啟 PDG 功能後，主要會用在以下兩個 GitNexus 的內建命令： [1]

* `explain`：用來向開發者或 AI 解釋某段複雜程式碼的具體執行邏輯。
* `pdg_query`：讓開發者可以精準查詢特定的業務鏈路或跨檔案的調用關係。

## 3. 與常規代碼圖譜的差別

GitNexus 預設的知識圖譜主要處理的是巨觀的結構關係（如：哪個類別繼承了誰、A 函數調用了 B 函數）。而 PDG 則是微觀的代碼分析，它會去看函數內部的邏輯。 [1, 4]

## 💡 開發實務建議

雖然 PDG 分析非常精準，但它會顯著增加索引（Index）的時間與記憶體消耗。一般日常開發、重構或單純透過 [MCP 協定](https://modelcontextprotocol.io/) 提供上下文給 AI Agent（如 Claude Code、Cursor）時，通常不需要開啟 --pdg。除非你需要進行非常嚴格的業務鏈路追蹤或安全審計，才建議加上此參數。 [1, 5]

您目前是在配置 GitNexus 的環境，還是正在嘗試解決特定程式碼的影響範圍分析（Blast Radius）呢？如果需要，我可以為您提供 GitNexus CLI 常見命令的配置範例。

[1] [https://mcp.csdn.net](https://mcp.csdn.net/6a7541bc99d9213aaa7e3121.html)
[2] [https://termdock.com](https://termdock.com/zh/blog/gitnexus-code-intelligence-knowledge-graph)
[3] [https://www.bydfi.com](https://www.bydfi.com/zh/crypto-news/gitnexus-102020)
[4] [https://ithelp.ithome.com.tw](https://ithelp.ithome.com.tw/articles/10399650)
[5] [https://zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/2034594927980581273)
