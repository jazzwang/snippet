# Pi Agent 的 OpenCode Browser Control 最佳替代方案

## 快速推薦

**🏆 最佳選擇：`pi-chrome`**

Pi 官方官方推薦，使用你現有的 Chrome 資料檔（已登入、cookies、extensions），無需額外設定。

---

## 主要替代方案比較

### 1. **pi-chrome** ⭐⭐⭐⭐⭐（推薦）

Pi 官方提供的 Chrome 控制套件。

**特點：**
- 使用你現有的 Chrome 配置檔（已登入狀態、cookies、extensions）
- 無需手動設定，直接套用現有的 Chrome profile
- 適合 debug 已登入的應用、檢查 dashboard、截圖

**安裝：**
```bash
npm i -g pi-chrome
```

**適用情境：**
- Debug 已登入的網站
- 檢查有登入狀態的 dashboard
- 捕捉已登入頁面的 console 和 network 錯誤
- 需要你的真實 Chrome 環境（非 headless）

**參考：** [pi.dev/packages/pi-chrome](https://pi.dev/packages/pi-chrome)

---

### 2. **pi-browser-harness** ⭐⭐⭐⭐⭐

Pi 官方包，功能最完整的瀏覽器控制工具。

**特點：**
- 40+ 種工具，透過 CDP（Chrome DevTools Protocol）控制
- 使用你已登入的 Chrome，保留所有設定
- 讀取頁面時以 accessibility tree 呈現，元素 handle 穩定
- 能填寫 React 不會復原的表單
- 捕捉 network traffic 和 console errors
- 工具用盡時可降級到 raw CDP

**安裝：**
```bash
npm i -g pi-browser-harness
```

**適用情境：**
- 需要完整的瀏覽器控制能力
- 需要穩定的元素 handle
- 需要捕捉 network 和 console 資訊
- 需要與 React 等框架深度整合

**參考：** [pi.dev/packages/pi-browser-harness](https://pi.dev/packages/pi-browser-harness)

---

### 3. **pi-chrome-dev-tools** ⭐⭐⭐⭐

輕量級系統 Chrome 控制工具。

**特點：**
- 使用你系統上的 Chrome（非 remote debugging）
- 使用 persistent profile，登入狀態、cookies、extensions 跨 session 保留
- 自動 stealth-patched，避免被 bot 偵測
- 零設定，瀏覽器首次工具呼叫時自動啟動

**比較：**

| 功能 | chrome-dev-tools | pi-browser-harness | Playwright MCP |
|------|------------------|-------------------|----------------|
| 零設定 | ✅ | ❌ 需手動 Chrome 設定 | ❌ |
| 即時啟動 | ✅ | ❌ 需先設定 | ❌ |
| 使用系統 Chrome | ✅ | ✅ | ❌ 需新瀏覽器 |

**安裝：**
```bash
npm i -g pi-chrome-dev-tools
```

**參考：** [GitHub - lallenlowe/pi-chrome-dev-tools](https://github.com/lallenlowe/pi-chrome-dev-tools)

---

### 4. **pi-control-chrome** ⭐⭐⭐⭐

Codex 對齊的 Chrome 和 Edge 瀏覽器控制。

**特點：**
- 透過本地 WebSocket Bridge 和 Manifest V3 extension 重用用戶現有的 Chromium profile
- 支援 Chrome 和 Edge
- Stage 1/2 核心實作已完成

**功能：**
- 重用現有的 Chrome/Edge profile、登入狀態、cookies、extensions、tabs
- 可檢查並 claim 明確選擇的現有 tabs

**安裝：**
```bash
npm i -g pi-control-chrome
```

**參考：** [pi.dev/packages/pi-control-chrome](https://pi.dev/packages/pi-control-chrome)

---

### 5. **pi-skill-agent-browser** ⭐⭐⭐⭐

輕量級的瀏覽器控制技能。

**特點：**
- 輕量級 CDP 腳本，直接 remote-control Google Chrome 或 Chromium
- 不依賴 Puppeteer 或 Playwright
- 透過 WebSocket 進行 raw CDP

**能力：**
| Command | Description |
|---------|-------------|
| `agent-browser start` | 啟動 Chrome，在 `:9222` 開啟 remote debugging |
| `agent-browser nav` | 導向當前 tab 或開啟新 tab |
| `agent-browser screenshot` | 截取當前頁面 |
| `agent-browser click` | 點擊元素 |
| `agent-browser fill` | 填寫表單 |
| `agent-browser text` | 讀取文字 |

**安裝：**
```bash
npm i -g pi-skill-agent-browser
```

**參考：** [pi.dev/packages/pi-skill-agent-browser](https://pi.dev/packages/pi-skill-agent-browser)

---

### 6. **pi-agent-browser** ⭐⭐⭐⭐

提供 browser 工具給 Pi。

**功能：**
- `open url` - 開啟網頁
- `snapshot -i` - 取得互動元素（回傳 `@ref` handle）
- `click @e1` - 點擊元素
- `fill @e2 "search query"` - 填寫表單
- `press Enter` - 按下 Enter
- `scroll down` - 向下捲動
- `get text` - 取得文字
- `get title` - 取得標題
- `get url` - 取得 URL
- `screenshot` - 截圖（內嵌圖片回傳）

**適用情境：**
- 網頁自動化測試
- 資料擷取
- 網頁互動

**參考：** [pi.dev/packages/pi-agent-browser](https://pi.dev/packages/pi-agent-browser)

---

### 7. **pi-browser-use** ⭐⭐⭐⭐

Agent Plugins 1.0 相容的瀏覽器擴展。

**特點：**
- 原生 Pi 擴展和 Agent Plugins 1.0 相容
- 共用相同的瀏覽器 runtime
- 基於 `chrome-devtools-mcp`（非 Playwright）
- 預設是自啟動的 headless Chrome，配置檔在 `~/.pi/browser-profile`

**優勢：**
- 一次登入即可持久化使用
- MCP 透過 ephemeral loopback 連接
- 不搶佔視窗、不偷取 focus

**安裝：**
```bash
npm i -g pi-browser-use
```

**參考：** [pi.dev/packages/pi-browser-use](https://pi.dev/packages/pi-browser-use)

---

### 8. **open-web-bridge** ⭐⭐⭐⭐

跨平台的瀏覽器控制橋接工具。

**特點：**
- 支援 OpenCode、Pi 或任何 Harness
- 驅動你的真實瀏覽器，保留登入 session、fingerprint、當前 tab
- CLI 版本，也可作為 extension 使用

**安裝：**
```bash
npm i -g open-web-bridge
```

**參考：** [GitHub - woniu9524/open-web-bridge](https://github.com/woniu9524/open-web-bridge)

---

### 9. **Better AI Browser Utilities (BABU)** ⭐⭐⭐⭐

MCP 控制的瀏覽器工具。

**特點：**
- 控制你正在使用的 Chrome session（tab、cookies、logins）
- 透過 Chrome extension 連接，非獨立 automation profile
- 四個緊湊的 MCP schema 取代 20+ 重複的瀏覽器工具
- Progressive disclosure：`browser_read` 回傳有限文字和緊湊控制，`browser_help` 才揭露命令細節

**安裝：**
```bash
npm i -g better-ai-browser-utilities
```

**參考：** [GitHub - ItMeDiaTech/better-ai-browser-utilities](https://github.com/ItMeDiaTech/better-ai-browser-utilities)

---

## 選擇指南

### 情境 1：需要快速開始，使用現有的 Chrome 環境
✅ **pi-chrome** - 最簡單，直接套用現有 profile

### 情境 2：需要最完整的工具集
✅ **pi-browser-harness** - 40+ 工具，功能最齊全

### 情境 3：不想設定，系統 Chrome 即可
✅ **pi-chrome-dev-tools** - 零設定，自動 stealth

### 情境 4：需要跨平台支援（Chrome + Edge）
✅ **pi-control-chrome** - 支援多種瀏覽器

### 情境 5：輕量級需求
✅ **pi-skill-agent-browser** - 簡單輕量

### 情境 6：需要 Agent Plugins 1.0 相容性
✅ **pi-browser-use** - 原生相容

### 情境 7：跨平台支援（OpenCode + Pi）
✅ **open-web-bridge** - 多平台支援

### 情境 8：MCP 控制需求
✅ **BABU** - 緊湊的 MCP schema

---

## 總結建議

| 需求 | 推薦方案 |
|------|---------|
| 快速開始、現有 Chrome | `pi-chrome` ⭐⭐⭐⭐⭐ |
| 完整功能、深度整合 | `pi-browser-harness` ⭐⭐⭐⭐⭐ |
| 零設定、系統 Chrome | `pi-chrome-dev-tools` ⭐⭐⭐⭐ |
| 跨瀏覽器支援 | `pi-control-chrome` ⭐⭐⭐⭐ |
| 輕量級 | `pi-skill-agent-browser` ⭐⭐⭐⭐ |
| Agent Plugins 1.0 | `pi-browser-use` ⭐⭐⭐⭐ |
| OpenCode + Pi 跨平台 | `open-web-bridge` ⭐⭐⭐⭐ |
| MCP 控制 | `BABU` ⭐⭐⭐⭐ |

**個人推薦順序：**
1. `pi-chrome` - 官方推薦，最簡單
2. `pi-browser-harness` - 功能最齊全
3. `pi-chrome-dev-tools` - 零設定優勢

---

*最後更新：2025*
