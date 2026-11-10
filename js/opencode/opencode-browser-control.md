# OpenCode Browser Control 技術報告

> **版本**: 1.0  
> **來源**: https://opencode.ai/product/browse  
> **GitHub**: https://github.com/anomalyco/browse  
> **License**: MIT

---

## 概述

OpenCode Browser Control 是一套完整的瀏覽器自動化解決方案，由 **MCP Server** 和 **Chromium 擴充功能** 組成，讓 AI Agent 可以控制您的真實瀏覽器，包含您現有的標籤、登入資訊和擴充功能。

### 核心優勢

- **真實瀏覽器**: 支援 Chrome、Edge、Brave、Arc、Helium、Vivaldi、Opera 和所有 Chromium 瀏覽器
- **無縫整合**: 使用您現有的登入狀態，無需重新輸入密碼
- **背景執行**: Agent 標籤自動收斂至背景，不干擾您的工作
- **人工接管**: 遇到登入、2FA 或付款時，自動交回給您操作
- **完整記錄**: 可擷取螢幕截圖、錄影和網路流量 (HAR)

---

## 系統架構

```
┌─────────────────────────────────────────────────────────────────┐
│                    OpenCode Browser Control                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────┐     ┌─────────────────┐     ┌─────────────┐
│  │   MCP Server    │◄───►│   Relay Server  │◄───►│  Extension  │
│  │  (Stdio/TCP)    │     │  127.0.0.1:19988│     │ (WebSocket) │
│  └─────────────────┘     └─────────────────┘     └──────┬──────┘
│                  Playwright Control                     │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              User's Browser (Chrome/Edge/Brave etc.)    │   │
│  │  - Chrome Debugger API (chrome.debugger)                │   │
│  │  - Existing Tabs & Logins                               │   │
│  │  - Installed Extensions                                 │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 三層架構說明

1. **MCP Server**: 透過 stdio 或 TCP 與 AI Agent 通訊，提供 API 介面
2. **Relay Server**: 監聽在 `127.0.0.1:19988`，作為中介層
3. **Browser Extension**: 透過 WebSocket 連接 Relay，使用 `chrome.debugger` 控制瀏覽器標籤

> **關鍵設計**: Agent 不直接與 Chrome 通訊，而是透過本地伺服器，該伺服器模擬 Chrome DevTools 端點。這種設計讓擴充功能只需執行命令，無需處理決策邏輯。

---

## 安裝步驟

### 方法一：Chrome 擴充功能（推薦）

這是官方推薦的安裝方式，擴充功能會引導您完成後續步驟。

1. **安裝 Chrome 擴充功能**

   1. 前往 [Chrome Web Store](https://chromewebstore.google.com/detail/mfnicocicmmlkpjnaffgihfjhdgjkdjg)
   2. 點擊「加上 Chrome」安裝
   3. 按照螢幕指示完成設定

### 方法二：直接安裝 CLI

如果您需要直接安裝 Command Line Interface，可選擇以下方式：

#### macOS / Linux

```bash
curl -fsSL https://opencode.ai/browse/install | bash
```

#### Windows (PowerShell)

```powershell
irm https://opencode.ai/browse/install.ps1 | iex
```

#### Node.js (npm)

```bash
npx @opencode/browse install

# 或全局安裝
npm install -g @opencode/browse && browse install
```

#### Bun

```bash
bun add -g @opencode/browse && browse install
```

### 驗證安裝

執行以下命令檢查安裝狀態：

```bash
# 檢查是否在 PATH 中
which browse
# 或 Windows
where browse

# 執行安裝
browse install
```

安裝後，`browse` 命令會被加入到 `~/.local/bin`（當 `$XDG_BIN_HOME` 設定時）

---

## 功能說明

### 1. 瀏覽器支援

| 瀏覽器 | 支援 |
|--------|------|
| Chrome | ✅ |
| Edge | ✅ |
| Brave | ✅ |
| Arc | ✅ |
| Helium | ✅ |
| Vivaldi | ✅ |
| Opera | ✅ |
| 其他 Chromium 瀏覽器 | ✅ |

### 2. MCP Server API

Agent 獲得 `browse` MCP Server，可執行以下操作：

- **開啟/驅動標籤**: 使用 Playwright 控制
- **擷取截圖**: `screenshot()`
- **錄影**: `record()`
- **網路流量記錄**: 捕捉為 HAR 檔案
- **人工接管**: 遇到需要人工介入時，自動將標籤交回給使用者

### 3. 工作流程

```
1. Agent 發送瀏覽器任務
   ↓
2. Browse 開啟背景標籤或接收現有標籤
   ↓
3. Playwright 執行導航、點擊、輸入、擷圖等操作
   ↓
4. 遇到需要人工介入（登入、2FA、付款）
   ↓
5. 將標籤交回給使用者
   ↓
6. 使用者點擊「Continue」繼續流程
```

### 4. 標籤管理

- **Agent 標籤**: 自動收斂至背景，以「Agents」群組顯示在標籤列開頭
- **偏好設定**: 可選擇分窗、每會話一個群組或不分群組

---

## 測試步驟

### 環境準備

```bash
# 確認 Node.js 版本 (需要 22.19+)
node --version

# 確認 browse 命令可用
browse --version
```

### 基本測試

#### 1. 開啟新標籤

```bash
browse open "https://example.com"
```

#### 2. 驅動瀏覽器

```bash
browse navigate "https://opencode.ai"
browse click "#login-button"
browse type "input[name='username']" "test@example.com"
browse type "input[name='password']" "password123"
browse click "button[type='submit']"
```

#### 3. 擷取截圖

```bash
browse screenshot
# 或指定名稱和格式
browse screenshot --name "page1" --format png
```

#### 4. 錄影

```bash
browse record --duration 10
```

#### 5. 網路流量記錄

```bash
browse capture-har --output network.har
```

### 完整測試流程

#### 測試 1: 基本導航

```bash
# 建立測試腳本
cat > test-browse.sh << 'EOF'
#!/bin/bash
set -e

echo "=== 測試 OpenCode Browser Control ==="

# 開啟測試網站
echo "1. 開啟 OpenCode 主頁..."
browse navigate "https://opencode.ai"

sleep 2

# 擷取初始截圖
echo "2. 擷取初始截圖..."
browse screenshot --name "homepage"

# 等待頁面載入
sleep 3

# 驗證頁面標題
echo "3. 檢查頁面標題..."
browse title

# 測試導航
echo "4. 測試導航到產品頁面..."
browse navigate "https://opencode.ai/product/browse"
sleep 2

# 擷取截圖
browse screenshot --name "product-page"

echo "=== 測試完成 ==="
EOF

chmod +x test-browse.sh

# 執行測試
./test-browse.sh
```

#### 測試 2: 人工接管測試

```bash
# 建立測試腳本
cat > test-handoff.sh << 'EOF'
#!/bin/bash

echo "=== 測試人工接管功能 ==="

# 開啟需要登入的網站
browse navigate "https://github.com"

# 等待頁面載入
sleep 3

# 擷取截圖（應該顯示未登入狀態）
browse screenshot --name "github-unlogged-in"

# 此時應該顯示需要人工介入的提示
# 使用者需手動登入 GitHub
# 登入後，點擊 Continue 按鈕

# 驗證登入後狀態
browse screenshot --name "github-logged-in"

echo "=== 人工接管測試完成 ==="
EOF

chmod +x test-handoff.sh
./test-handoff.sh
```

---

## 驗證步驟

### 1. 功能驗證清單

- [ ] **基本導航**: 能成功開啟和導航到目標網站
- [ ] **互動操作**: 點擊、輸入等互動功能正常
- [ ] **截圖功能**: 能正確擷取頁面截圖
- [ ] **錄影功能**: 能正確錄製螢幕
- [ ] **網路流量記錄**: HAR 檔案格式正確
- [ ] **人工接管**: 遇到需要介入時正確提示使用者
- [ ] **標籤管理**: Agent 標籤正確收斂至背景

### 2. 瀏覽器相容性測試

```bash
# 測試不同瀏覽器
cat > test-browsers.sh << 'EOF'
#!/bin/bash

BROWSERS=(
    "chrome"
    "edge"
    "brave"
)

for browser in "${BROWSERS[@]}"; do
    echo "=== 測試 ${browser} ==="
    # 設定瀏覽器路徑（依實際情況調整）
    browse --browser "$browser" navigate "https://example.com"
    browse screenshot --name "${browser}-test"
done

echo "=== 所有瀏覽器測試完成 ==="
EOF

chmod +x test-browsers.sh
./test-browsers.sh
```

### 3. MCP 整合測試

如果您使用支援 MCP 的 AI Agent（如 OpenCode、Claude Code、Cursor 等），可進行以下測試：

```bash
# 設定 MCP Server
# 在您的 MCP 設定檔案中添加：
{
  "mcpServers": {
    "browse": {
      "command": "browse",
      "args": ["serve"],
      "cwd": "~/.local/share/opencode"
    }
  }
}

# 在 AI Agent 中測試
# 例如在 Cursor 或 Claude Code 中，發送：
"請幫我開啟 https://opencode.ai 並擷取截圖"
```

### 4. 效能測試

```bash
# 測試響應時間
cat > test-performance.sh << 'EOF'
#!/bin/bash

START=$(date +%s.%N)
browse navigate "https://opencode.ai"
sleep 2
browse screenshot --name "perf-test"
END=$(date +%s.%N)

ELAPSED=$(echo "$END - $START" | bc)
echo "測試執行時間: ${ELAPSED} 秒"
EOF

chmod +x test-performance.sh
./test-performance.sh
```

---

## 常見問題

### Q1: 擴充功能安裝後找不到 browse 命令

**解決方案**: 確保已執行 `browse install`

```bash
# 手動執行安裝
browse install

# 檢查 PATH
echo $PATH
# 應該包含 ~/.local/bin
```

### Q2: Agent 無法驅動瀏覽器

**檢查清單**:

1. Chrome 擴充功能是否已安裝且啟用
2. Relay Server 是否正在執行（預設監聽 127.0.0.1:19988）
3. MCP Server 是否正確設定
4. 瀏覽器版本是否過舊

### Q3: 人工接管提示不顯示

**解決方案**:

1. 確認擴充功能設定正確
2. 檢查瀏覽器設定是否允許彈出視窗
3. 確認当前標籤是 Agent 開啟的

### Q4: 無法使用現有的登入資訊

**可能原因**:

1. 擴充功能未正確安裝
2. 瀏覽器設定需要重新授權
3. Cookie 或 Cache 問題

**解決步驟**:

```bash
# 重新安裝擴充功能
# 1. 移除擴充功能
# 2. 重新從 Chrome Web Store 安裝
# 3. 重新登入需要的網站
```

---

## 進階設定

### 1. 自定义 MCP 設定

```bash
# 設定自訂 Port
browse serve --port 19989

# 設定 Relay 地址
browse serve --relay-host 127.0.0.1 --relay-port 19990
```

### 2. 允許清單 (Allowlist)

限制 Agent 只能訪問特定網站：

```json
// .opencode/allowlist.json
{
  "sites": [
    "opencode.ai",
    "example.com"
  ]
}
```

### 3. 背景群組設定

```bash
# 設定背景群組偏好
browse settings --group-tabs true
browse settings --separate-window false
```

---

## 參考資源

- **官方文件**: https://opencode.ai/product/browse
- **Chrome 擴充功能**: https://chromewebstore.google.com/detail/mfnicocicmmlkpjnaffgihfjhdgjkdjg
- **GitHub 專案**: https://github.com/anomalyco/browse
- **MCP Server 資訊**: https://glama.ai/mcp/servers/anomalyco/browse/tree
- **技術文章**: https://dev.to/dishant0406/opencode-browse-hands-your-agent-the-logged-in-browser-2nof

---

## 版本歷史

### v1.0 (2026-11-08)
- 初始技術報告
- 包含安裝、測試、驗證完整流程
- 涵蓋所有核心功能

---

*報告最後更新: 2026-11-08*
