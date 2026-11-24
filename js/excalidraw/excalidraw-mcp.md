# Excalidraw MCP Server 技術報告

**撰寫日期**: 2026-11-24

## 1. 概述

Excalidraw MCP（Model Context Protocol）Server 是一個讓 AI 代理能夠透過 MCP 協定與 Excalidraw 手繪風格白板整合的開源專案。它允許 AI 代理在程式碼中自動建立、編輯和檢視架構圖、流程圖等視覺化圖表，並能將圖表儲存為 `.excalidraw` 檔案。

### 主要功能

- 透過 MCP 工具自動建立和編輯圖表元素
- 即時預覽 AI 所繪製的圖表（透過截圖或描述）
- 將 `.excalidraw` 檔案儲存到版本控制系統
- 支援多種傳輸方式（stdio 和 HTTP）
- 可獨立運行或與雲端 Canvas 整合

## 2. 前置需求

### 2.1 必要條件

1. **Node.js ≥ 20**：必須安裝 Node.js 20 或更高版本
2. **MCP 客戶端**：支援 Streamable HTTP 的 MCP 客戶端（如 Claude Code、Codex CLI、Cursor 等）
3. **（選用）Excalidraw Plus Workspace**：如使用官方雲端版本，需要 Excalidraw Plus 帳號

### 2.2 選擇版本

目前有三種主要的 Excalidraw MCP 實作：

| 觀點 | 官方 excalidraw-mcp | 社群版 mcp-excalidraw-server | Excalidraw+ MCP |
|------|---------------------|-----------------------------|-----------------|
| 最新版 | v0.3.2 | 2.1.2 | 公開測試版 |
| 形態 | 聊天內嵌小工具 | 本地常駐 Canvas | 雲端工作區 |
| 主要用途 | Claude、ChatGPT、VS Code | Claude Code、Codex、Cursor | Plus 合約用戶 |
| 可用工具 | 2 個 | 26 個 | 最多 37 個 |
| AI 可檢視圖表 | ❌ | ✅ | ✅ |

**推薦選擇**：
- 一般開發者使用：`mcp-excalidraw-server`（社群版）
- 需要完整功能整合：`excalidraw-mcp`（官方版）

## 3. 安裝步驟

### 3.1 方式一：使用 npm（推薦）

```bash
# 安裝 mcp-excalidraw-server
npx -y mcp-excalidraw-server install-skill --dir ~/.mcp
```

### 3.2 方式二：手動安裝

```bash
# 克隆官方倉庫
git clone https://github.com/yctimlin/mcp_excalidraw.git
cd mcp_excalidraw

# 或使用 Excalidraw 官方倉庫
git clone https://github.com/excalidraw/excalidraw-mcp.git
cd excalidraw-mcp

# 安裝依賴
npm install
```

### 3.3 方式三：使用 npx 直接啟動

```bash
# 啟動 Canvas（繪圖指令會自動啟動）
npx -y mcp-excalidraw-server start

# 開啟本地 Canvas
open http://127.0.0.1:3000

# 可選：使用 watch 模式（僅 mermaid 需要）
npx -y mcp-excalidraw-server watch
```

### 3.4 使用 HTTP 傳輸模式

```bash
# 啟動 HTTP 伺服器
npx excalidraw-mcp-server --transport http --server https://excalidraw.example.com --port 3001

# 或使用 stdio（預設模式，適合 AI 客戶端）
npx excalidraw-mcp-server --transport stdio --server
```

## 4. 設定步驟

### 4.1 設定 MCP 客戶端（以 Claude Code 為例）

編輯 `~/.claude.json` 檔案：

```json
{
  "mcpServers": {
    "excalidraw": {
      "type": "stdio",
      "command": "npx",
      "args": [
        "-y",
        "mcp-excalidraw-server",
        "--transport",
        "stdio",
        "--server"
      ],
      "env": {
        "NODE_ENV": "production"
      }
    }
  }
}
```

### 4.2 設定 HTTP 模式（以 Codex 為例）

```json
{
  "mcpServers": {
    "excalidraw": {
      "type": "http",
      "url": "https://api.excalidraw.com/api/v1/mcp",
      "headers": {
        "Authorization": "Bearer <API_KEY>"
      }
    }
  }
}
```

### 4.3 使用 Excalidraw+ 官方端點

```json
{
  "mcpServers": {
    "excalidraw-plus": {
      "type": "http",
      "url": "https://mcp.excalidraw.com",
      "authType": "oauth"
    }
  }
}
```

### 4.4 自訂環境變數

```bash
# 設定 Canvas 連接（選用）
export EXCALIDRAW_CANVAS_URL="http://localhost:3000"

# 設定 API Key（僅當使用需要認證的端點時）
export EXCALIDRAW_API_KEY="your-api-key"

# 設定 Canvas WebSocket 連接
export EXCALIDRAW_WS_URL="wss://canvas.excalidraw.com"
```

## 5. 測試步驟

### 5.1 基本功能測試

```bash
# 啟動伺服器
npx -y mcp-excalidraw-server start

# 在瀏覽器中開啟 Canvas
open http://127.0.0.1:3000
```

### 5.2 使用 MCP 客戶端測試

在 MCP 客戶端中執行以下指令：

```javascript
// 建立基本矩形
[
  {
    "id": "api",
    "type": "rectangle",
    "x": 100,
    "y": 100,
    "width": 160,
    "height": 80,
    "text": "API Server",
    "backgroundColor": "#a5d8ff"
  }
]
```

### 5.3 驗證圖表建立

```javascript
// 取得當前 Canvas 內容
await read_canvas()

// 取得 Canvas 截圖
await screenshot()

// 取得 Canvas 描述
await describe_canvas()
```

### 5.4 完整測試流程

```bash
# Step 1: 啟動 MCP Server
npx -y mcp-excalidraw-server start &

# Step 2: 開啟 Canvas 視窗
open http://127.0.0.1:3000

# Step 3: 使用 AI 客戶端執行繪圖指令
# 例如在 Claude Code 中：
# "Draw a simple architecture diagram with API and Database"

# Step 4: 驗證圖表是否正確顯示
# 應該能在 Canvas 中看到繪製的元素

# Step 5: 儲存圖表檔案
await save_to_repo()
```

## 6. 驗證步驟

### 6.1 功能驗證清單

- [ ] MCP Server 成功啟動且無錯誤
- [ ] MCP 客戶端能正常連接
- [ ] 能在 Canvas 中看到繪製的元素
- [ ] 截圖功能正常運作
- [ ] 能取得 Canvas 的描述
- [ ] 圖表檔案能正確儲存
- [ ] `.excalidraw` 檔案可被版本控制系統追蹤

### 6.2 自動測試腳本

```javascript
// test-excalidraw-mcp.js
const assert = require('assert');

async function testExcalidrawMCP() {
  console.log('開始 Excalidraw MCP 測試...');
  
  // Test 1: 建立元素
  console.log('Test 1: 建立基本元素');
  const element1 = await create_element({
    type: 'rectangle',
    x: 100,
    y: 100,
    width: 200,
    height: 100,
    text: '測試框'
  });
  assert(element1.id, '元素 ID 應該存在');
  console.log('✓ Test 1 通過');
  
  // Test 2: 截圖
  console.log('Test 2: 截圖功能');
  const screenshot = await screenshot();
  assert(screenshot.data, '截圖應該有數據');
  console.log('✓ Test 2 通過');
  
  // Test 3: 描述 Canvas
  console.log('Test 3: Canvas 描述');
  const description = await describe_canvas();
  assert(description.text, '描述應該有文本');
  console.log('✓ Test 3 通過');
  
  // Test 4: 儲存檔案
  console.log('Test 4: 儲存檔案');
  await save_to_repo('test-diagram.excalidraw');
  console.log('✓ Test 4 通過');
  
  console.log('所有測試通過！');
}

testExcalidrawMCP().catch(err => {
  console.error('測試失敗:', err);
  process.exit(1);
});
```

### 6.3 手動驗證清單

1. **啟動驗證**：
   ```bash
   npx -y mcp-excalidraw-server start
   # 應該看到：Server running on http://localhost:3000
   ```

2. **連接驗證**：
   ```bash
   # 在瀏覽器開啟
   http://localhost:3000
   # 應該看到空白 Canvas
   ```

3. **功能驗證**：
   ```javascript
   // 建立多個元素
   await create_element({
     type: 'rectangle',
     x: 50,
     y: 50,
     width: 100,
     height: 50,
     text: '元素 1'
   });
   
   await create_element({
     type: 'arrow',
     x: 150,
     y: 50,
     targetX: 200,
     targetY: 50
   });
   
   // 驗證截圖
   const image = await screenshot();
   // 應該能看到包含兩個元素的 Canvas
   ```

4. **檔案驗證**：
   ```bash
   # 列出專案中的 excalidraw 檔案
   git ls-files | grep excalidraw
   
   # 應該看到新儲存的 .excalidraw 檔案
   ```

## 7. 故障排除

### 7.1 常見問題

#### 問題 1: Server 啟動失敗

**症狀**：`npx -y mcp-excalidraw-server start` 無回應或報錯

**解決方案**：
```bash
# 檢查 Node.js 版本
node --version
# 應該 >= v20.0.0

# 檢查 npm 版本
npm --version

# 重新安裝套件
npx -y mcp-excalidraw-server@latest
```

#### 問題 2: Canvas 無法顯示

**症狀**：啟動後瀏覽器無反應

**解決方案**：
```bash
# 確認 Port 3000 是否被使用
lsof -i :3000

# 如果端口被佔用，改用其他端口
npx -y mcp-excalidraw-server start --port 3001

# 開啟新端口
open http://localhost:3001
```

#### 問題 3: MCP 連接失敗

**症狀**：客戶端報錯 "Failed to connect to MCP server"

**解決方案**：
```json
// 檢查 ~/.claude.json 設定
{
  "mcpServers": {
    "excalidraw": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "mcp-excalidraw-server", "--transport", "stdio", "--server"],
      "env": {
        "NODE_ENV": "production"
      }
    }
  }
}
```

#### 問題 4: 無法儲存檔案

**症狀**：`save_to_repo()` 失敗

**解決方案**：
```javascript
// 確保專案根目錄有 .git 初始化
git init

// 設定 Git 用戶資訊（如果尚未設定）
git config user.email "your@email.com"
git config user.name "Your Name"

// 儲存檔案
await save_to_repo('diagram.excalidraw')
git add diagram.excalidraw
git commit -m "Add diagram"
```

## 8. 進階設定

### 8.1 設定 Canvas 同步

```bash
# 啟動 Connected Mode（需要 Canvas Server）
npx -y mcp-excalidraw-server start --mode connected

# 或使用自訂 WebSocket URL
export EXCALIDRAW_WS_URL="wss://your-canvas-server.com"
npx -y mcp-excalidraw-server start --ws-url "$EXCALIDRAW_WS_URL"
```

### 8.2 設定自訂元素樣式

```javascript
// 定義自訂元素樣式
const customStyles = {
  servers: {
    backgroundColor: '#a5d8ff',
    borderRadius: 8,
    strokeWidth: 2
  },
  databases: {
    backgroundColor: '#99e694',
    borderRadius: 8
  }
};
```

### 8.3 設定自動儲存

```javascript
// 設定自動儲存到版本控制
const autoSave = {
  enabled: true,
  interval: 30000, // 每 30 秒
  path: './diagrams/'
};
```

## 9. 最佳實踐

### 9.1 專案結構建議

```
project/
├── diagrams/
│   ├── architecture.excalidraw
│   ├── flowcharts/
│   │   ├── user-flow.excalidraw
│   │   └── data-flow.excalidraw
│   └── system/
│       └── system-design.excalidraw
├── .gitignore
├── .gitattributes
└── README.md
```

### 9.2 .gitignore 設定

```gitignore
# 忽略臨時檔案
*.tmp
*.cache
diagrams/temp/

# 忽略 Canvas 狀態（如果不需要）
.excalidraw-state/
```

### 9.3 .gitattributes 設定

```gitattributes
*.excalidraw text eol=lf
```

### 9.4 團隊協作建議

- 使用 `Connected Mode` 允許多人協同編輯
- 建立標準化圖表樣式指南
- 定期儲存和 Commit 圖表檔案
- 使用描述性檔案名稱（如 `architecture-2026-11-24.excalidraw`）

## 10. 參考資源

### 10.1 官方文件

- [Excalidraw+ MCP 文檔](https://plus.excalidraw.com/docs/mcp)
- [MCP Servers 官方目錄](https://mcpservers.org/zh-TW/servers/excalidraw-app-demo-mcp)

### 10.2 社群專案

- [mcp-excalidraw-server](https://github.com/yctimlin/mcp_excalidraw)
- [excalidraw-mcp](https://github.com/excalidraw/excalidraw-mcp)
- [excalidraw-mcp-server](https://github.com/debu-sinha/excalidraw-mcp-server)

### 10.3 第三方文章

- [Excalidraw MCP 使用指南](https://creatos.io/guides/excalidraw-mcp)
- [Excalidraw MCP 三種實作比較](https://www.issoh.co.jp/tech/details/10968/)

## 11. 附錄：快速開始腳本

### 11.1 完整安裝腳本

```bash
#!/bin/bash
# install-excalidraw-mcp.sh

set -e

echo "=== Excalidraw MCP 安裝腳本 ==="

# 1. 檢查 Node.js
echo "檢查 Node.js..."
if ! command -v node &> /dev/null; then
  echo "❌ 需要安裝 Node.js >= 20"
  exit 1
fi
echo "✓ Node.js $(node --version)"

# 2. 安裝 MCP Server
echo "安裝 MCP Server..."
npx -y mcp-excalidraw-server install-skill --dir ~/.mcp
echo "✓ 安裝完成"

# 3. 啟動伺服器
echo "啟動 Server..."
npx -y mcp-excalidraw-server start &
SERVER_PID=$!

# 4. 開啟 Canvas
echo "開啟 Canvas..."
open http://127.0.0.1:3000

# 5. 等待並驗證
sleep 5
echo "伺服器 PID: $SERVER_PID"
echo "Canvas: http://127.0.0.1:3000"

echo "=== 安裝完成！==="

# 停用陷阱
trap "kill $SERVER_PID 2>/dev/null" EXIT
```

### 11.2 測試腳本

```bash
#!/bin/bash
# test-excalidraw-mcp.sh

set -e

echo "=== 開始測試 ==="

# 測試基本功能
npx -y mcp-excalidraw-server start
echo "Server 啟動中..."
sleep 5

# 測試 MCP 連接
echo "測試 MCP 連接..."
# （需要手動在客戶端測試）

echo "測試完成！"
```

**報告結束**

*最後更新：2026-11-24*
*版本：1.0*
