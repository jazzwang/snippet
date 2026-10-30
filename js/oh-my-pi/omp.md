# Oh My Pi 技術報告

> 版本：18.1.10
> 來源：[can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) / [omp.sh](https://omp.sh)
> 撰寫日期：2026-10-30

## 摘要

Oh My Pi (omp) 是一個以終端為先的編碼 AI Agent 工具，專為那些遠不止「貼上一段程式碼片段」的工作而生。它整合了 IDE、終端、模型、工具、會話和擴充套件系統，讓開發者可以在單一會話中完成調查、編輯、執行命令、驗證等完整開發循環。

本文技術報告涵蓋以下主題：

- 系統需求與安裝方式
- 核心功能特性
- 工具列表與使用方式
- 最佳實踐與測試步驟
- 擴充套件與自定義能力

## 一、系統需求與安裝

### 1.1 環境需求

omp 支援以下平台與環境：

| 項目 | 需求 |
|------|------|
| 作業系統 | macOS、Linux、Windows（原生支援，無需 WSL） |
| Bun | >= 1.3.14（推薦）或 curl/mise |
| API 金鑰 | 至少一個 AI Provider 憑證（Anthropic、Ollama、vLLM 等） |
| 終端模擬器 | 相容的終端模擬器 |
| git | 用於 subagent worktree 功能 |

### 1.2 安裝方式

#### 方式一：官方安裝腳本（推薦）

macOS 或 Linux：

```bash
curl -fsSL https://omp.sh/install | sh
```

Windows（PowerShell）：

```powershell
irm https://omp.sh/install.ps1 | iex
```

確認安裝成功：

```bash
omp --version
omp --help
```

#### 方式二：Homebrew

```bash
brew install can1357/tap/omp
brew upgrade omp
```

#### 方式三：Bun 全域安裝

```bash
bun install -g @oh-my-pi/pi-coding-agent
bun update -g
```

#### 方式四：mise 版本鎖定

```bash
mise use -g github:can1357/oh-my-pi
```

### 1.3 版本鎖定

若要鎖定特定版本：

```bash
curl -fsSL https://omp.sh/install | sh -s -- --binary --ref v18.1.10
```

PowerShell：

```powershell
irm https://omp.sh/install.ps1 -Binary -Ref v18.1.10
```

## 二、核心功能特性

### 2.1 完整開發循環

omp 整合以下核心能力：

1. **探索程式碼與檔案資訊**
   - 讀取檔案與資源（`read`）
   - 搜尋內容（`grep`）
   - 查找路徑（`glob`）

2. **程式碼編輯**
   - Hashline patches with content-hash anchors
   - Stale-anchor recovery
   - 結構化程式碼查詢（AST）

3. **執行命令**
   - Shell 執行能力
   - 測試運行
   - 進程檢查

4. **LSP 與 DAP**
   - 14 種 LSP 操作
   - 28 種 DAP 操作（Debug Adapter Protocol）

5. **瀏覽器能力**
   - 開啟需要登入的頁面
   - 處理內部 URL

6. **Web 搜尋**
   - 即時搜尋能力

7. **記憶與自適應**
   - 會話記憶
   - 自適應工具選擇

### 2.2 性能優勢

- **即時的搜尋**：返回結果迅速
- **一擊編輯**：reads summarize files instead of dumping content
- **Hashline patches**：可追蹤的編輯，支持 stale-anchor recovery
- **60+ AI Providers**：支援眾多模型選擇
- **31 內建工具**：开箱即用

## 三、工具列表

### 3.1 可用工具檢視

在會話中使用 `/tools` 查看當前模型與項目實際可用的能力：

```bash
omp
/tools
```

### 3.2 主要工具類別

#### 文件操作工具

| 工具 | 功能 |
|------|------|
| `read` | 讀取檔案、資源、圖片、SQLite、內部 URL 等 |
| `glob` | 依名稱或 glob 模式定位檔案與目錄 |
| `grep` | 使用正規表達式搜尋本地或遠端內容 |
| `ast_grep` | 結構化程式碼查詢（50+ tree-sitter） |

#### 執行工具

| 工具 | 功能 |
|------|------|
| `bash` / `shell` | 執行 shell 命令 |
| `python` | Python 程式碼執行 |
| `task` | 任務分發 |

#### 搜尋工具

| 工具 | 功能 |
|------|------|
| `grep` | 正規表達式搜尋 |
| `web_search` | Web 搜尋 |
| `source_check` | 來源查核 |
| `fetch_content` | 抓取網頁內容 |

#### 編輯工具

| 工具 | 功能 |
|------|------|
| `edit` | Hashline 編輯 |
| `write` | 寫入檔案 |
| `ast_grep` | 結構化查詢 |

### 3.3 工具控制

#### 設定可用工具

打開 `/settings` 使用「可用工具」進行持久開關切換。

#### 啟動受限會話

```bash
omp --tools read,glob,grep
omp --no-tools
```

#### 工具審批模式

```bash
omp --approval-mode always-ask
omp --approval-mode write
omp --approval-mode yolo
```

持久配置：`tools.approvalMode`

## 四、最佳實踐與測試步驟

### 4.1 基本工作流程

#### 步驟一：啟動會話

```bash
cd my-project
omp
```

#### 步驟二：發送有邊界的請求

```bash
# 範例：尋找並修正 race condition
Find the refresh-token race, fix only the implementation and its focused tests, show me the diff, and run those tests. Do not commit.
```

按 Enter 鍵即可開始。

### 4.2 完整任務：逐輪進行

omp 的可靠互動式任務遵循以下循環：

#### 1. 說明預期結果與邊界

- 指出 bug 或功能
- 重要的路徑
- 任何不得改變的內容
- 應當通過的檢查

#### 2. 讓 omp 調查

- 它會敘述進度
- 每次讀取、命令或更改以卡片形式顯示在對話記錄中

#### 3. 在需要時介入

- 發送引導消息
- 回答問題
- 拒絕不安全的操作

#### 4. 審查證據

- 展開工具卡片與 diff
- 檢查被更改的路徑
- 檢查命令的退出狀態
- 檢查測試結果

#### 5. 在同一會話中完善

```bash
# 範例：保持公共簽名、補上缺失的邊界情況
Keep the public signature, add missing edge cases, and revert changes to cache.ts
```

### 4.3 工具卡片使用

工具卡片是提示詞與答案之間的審計軌跡：

1. **讀標題**：标明動作、命令、路徑或遠端資源
2. **檢查狀態**：查看工具輸出狀態
3. **檢查結果**：查看命令結果、diff、測試結果

#### 展開與收合

- 按 `Ctrl+O` 展開或收合工具輸出
- 查看被截斷的命令記錄或完整的可見 diff

### 4.4 測試範例

#### 範例一：單一指令測試

```bash
omp -p "用一句話說明當前目錄是什麼項目"
```

#### 範例二：完整任務測試

```bash
# 創建測試專案
mkdir test-project
cd test-project
echo "test" > README.md

# 啟動 omp
omp

# 發送任務
Read README.md, create hello.py that outputs Hello, Oh My Pi!, and run it using the locally available Python interpreter.
```

#### 範例三：修正 bug 測試

```bash
# 描述問題
Fix the race condition in the token refresh logic. Only modify the implementation file and its unit tests. Show me the diff before committing.
```

### 4.5 一鍵測試

```bash
# 解釋專案
omp --print "explain this repo in one sentence"

# 測試模型
omp --model ollama:qwen2.5:7b "你好"

# 受限工具測試
omp --tools read,glob "列出這個專案的所有目錄"
```

## 五、自定義與擴充套件

### 5.1 自定義工具

自定義工具是一個小型的 TypeScript 或 JavaScript 模組，讓 omp 能夠調用由你掌控的程式碼。

#### 作用域選擇

| 作用域 | 推薦路徑 | 使用時機 |
|--------|----------|----------|
| 專案 | `.omp/tools/index.ts` | 工具屬於某個倉庫，應隨倉庫被審查 |
| 使用者 | `~/.omp/tools/index.ts` | 工具出現在當前 omp profile 下的每個專案 |

#### 範例：創建項目工具

```typescript
// .omp/tools/hello/index.ts
import { ExtensionAPI } from "@oh-my-pi/pi-coding-agent";

export default async function greeting(pi: ExtensionAPI) {
  return "Hello from custom tool!";
}
```

#### 重新啟動

從專案目錄重新啟動 omp 後，請它使用該工具。

### 5.2 Hook

Hook 讓你可以為 omp 每次工作時應用一條本地策略。

#### 範例：阻止 git push --force

```typescript
// .omp/hooks/pre/force-push.ts
import { isToolCallEventType, type ExtensionAPI } from "@oh-my-pi/pi-coding-agent";

const FORCE_PUSH = /\bgit\s+push\b[^\n]*(?:--force(?:\s|$)|(?:^|\s)-f(?:\s|$))/;

export default function forcePushGuard(pi: ExtensionAPI) {
  pi.on("session_start", (_event, ctx) => {
    if (ctx.hasUI) {
      ctx.ui.addNotification({
        text: "⚠️ Force push is blocked by Hook",
        timeout: 5,
        type: "error",
      });
    }
  });
}
```

### 5.3 擴充套件系統

omp 擴充套件是一個 TypeScript 或 JavaScript 模組，添加工具、slash 命令、事件行為等能力。

#### 創建擴充套件

```bash
mkdir my-extension
cd my-extension
npm init -y
npm install @oh-my-pi/pi-coding-agent
```

#### 範例：添加自定義工具

```typescript
// src/tools/calculator.ts
import { Tool, ToolDefinition } from "@oh-my-pi/pi-coding-agent";
import { type } from "type";

const calculatorSchema = type({
  a: "number",
  b: "number",
  operation: "'add'|'subtract'|'multiply'|'divide'",
});

export const calculatorTool: Tool = {
  name: "math_operation",
  description: "Perform basic arithmetic operations",
  parameters: calculatorSchema,
  execute: async (model, { a, b, operation }) => {
    const results = {
      add: a + b,
      subtract: a - b,
      multiply: a * b,
      divide: a / b,
    };
    return `Result: ${operation} = ${results[operation]}`;
  },
};

export default {
  tools: [calculatorTool],
} as ToolDefinition;
```

#### 載入擴充套件

```bash
omp
/plugins add ./path/to/extension
```

## 六、配置與設定

### 6.1 配置目錄

```bash
# 默認配置和運行數據位於
~/.omp
```

### 6.2 環境變數

```bash
# API 金鑰
export ANTHROPIC_API_KEY=sk-ant-...

# 模型設定
export MODEL_PROVIDER=anthropic
export MODEL_NAME=claude-3-5-sonnet-20240620
```

### 6.3 設定項目

#### 可用工具

```bash
# 查看當前可用工具
omp /tools
```

#### 設定工具審批

```bash
omp /settings
# 修改 tools.approvalMode
```

#### 設定記憶

```bash
# 查看記憶配置
omp /settings
# 修改 memory.enabled
```

## 七、常見問題

### 7.1 安裝問題

#### Q: 安裝後找不到 `omp` 命令

```bash
# 檢查 PATH
echo $PATH

# 重新載入 shell
source ~/.bashrc
# 或
source ~/.zshrc
```

#### Q: Alpine / musl 系統需要額外套件

```bash
apk add libstdc++ libgcc
```

### 7.2 執行問題

#### Q: 工具無法執行

```bash
# 檢查工具狀態
omp /tools

# 查看錯誤日誌
omp /logs
```

#### Q: API 金鑰無效

```bash
# 檢查環境變數
env | grep API_KEY

# 重新設置金鑰
export ANTHROPIC_API_KEY=new-key
```

### 7.3 性能問題

#### Q: 搜尋太慢

```bash
# 檢查 grep 配置
omp /settings
# 修改 grep.enabled
```

#### Q: 編輯會失敗

```bash
# 檢查 read 配置
omp /settings
# 修改 read.enabled
```

## 八、資源與參考

### 8.1 官方資源

- [oh-my-pi GitHub](https://github.com/can1357/oh-my-pi)
- [omp.sh 官方文件](https://omp.sh)
- [omp.sh/docs](https://omp.sh/docs)

### 8.2 中文資源

- [Oh My Pi 中文文檔](https://aieguu.github.io/omp-docs-cn/)
- [部署與安裝設計文檔](https://yeluo45.github.io/oh-my-pi-design/docs/17-deployment)

### 8.3 社群資源

- [Trove 詳細指南](https://trove.xin/detailed/oh-my-pi)
- [菜鸟教程](https://www.runoob.com/vibe-coding/omp-usage.html)

## 九、測試清單

### 9.1 安裝測試

- [ ] 執行安裝命令成功
- [ ] `omp --version` 返回正確版本
- [ ] `omp --help` 顯示幫助訊息
- [ ] 可進入專案目錄啟動會話

### 9.2 基本功能測試

- [ ] `/tools` 顯示可用工具列表
- [ ] `/settings` 可進入設定頁面
- [ ] 發送基本提示詞可執行
- [ ] 讀取檔案功能正常

### 9.3 工具測試

- [ ] `read` 可讀取檔案
- [ ] `bash` 可執行命令
- [ ] `grep` 可搜尋內容
- [ ] `edit` 可編輯檔案
- [ ] `write` 可寫入檔案

### 9.4 測試任務

- [ ] 創建測試專案並啟動 omp
- [ ] 發送完整任務提示詞
- [ ] 審查工具卡片輸出
- [ ] 檢查最終結果正確

### 9.5 自定義功能測試

- [ ] 創建自定義工具並載入
- [ ] 創建 Hook 並驗證
- [ ] 創建擴充套件並載入

## 十、結論

Oh My Pi 是一個功能完整、性能優異的編碼 AI Agent 工具。它整合了 IDE、終端、模型、工具、會話和擴充套件系統，讓開發者可以在單一會話中完成完整的開發循環。

透過本技術報告，讀者應能：

1. 理解 omp 的系統需求與安裝方式
2. 熟悉 omp 的核心功能特性
3. 掌握 omp 的工具列表與使用方式
4. 學習 omp 的最佳實踐與測試步驟
5. 了解 omp 的自定義與擴充套件能力

建議初學者從官方安裝腳本開始，並參考中文文檔逐步學習。對於進階使用者，可透過自定義工具、Hook 和擴充套件來擴展 omp 的能力。

**版本歷史**

| 版本 | 日期 | 說明 |
|------|------|------|
| 1.0 | 2026 | 初始版本 |

**作者**：技術團隊

**審閱**：待審閱
