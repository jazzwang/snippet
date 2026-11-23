# Excalimate 技術報告

**報告日期：** 2026-11-23

## 1. 專案概述

[Excalimate](https://excalimate.com/) 是一個開源的動畫工具，專為將手繪的 Excalidraw 圖表轉換為關鍵幀動畫而設計。它支援完整的 Excalidraw 編輯器，提供關鍵幀動畫、相機動畫、AI 整合等功能，並將結果導出為多種格式（MP4、WebM、GIF、SVG 等）。

### 核心功能

- **完整的 Excalidraw 編輯器** — 繪製、編輯、調整大小、連接箭頭、添加文字
- **關鍵幀動畫** — 透明度淡入淡出、位置滑動、縮放效果、旋轉、箭頭繪製動畫
- **時間軸動畫** — 可收縮的每元素音軌，包含插值線、剪輯標記、刮擦功能
- **相機動畫** — 縮放/縮放關鍵幀，含長寬比控制
- **統一導出** — MP4、WebM、GIF、動畫 SVG、Lottie 和 dotLottie
- **MCP Server** — 讓 AI 代理可以即時創建和動畫化圖表
- **端對端加密分享** — 使用 AES-256-GCM，密鑰保留在 URL hash 中

## 2. 系統需求

### 開發環境

| 項目 | 版本要求 |
|------|----------|
| Node.js | 24.x（CI 使用的版本） |
| npm | 最新穩定版 |
| 瀏覽器 | 現代瀏覽器支援 WebCodecs API |

### 推薦環境

- **VS Code** 或類似 IDE
- **Git** 版本控制系統
- 至少 2GB 可用記憶體

## 3. 安裝步驟

### Step 1: 克隆儲存庫

```bash
git clone https://github.com/excalimate/excalimate.git
cd excalimate
```

### Step 2: 安裝依賴

#### 主專案安裝

```bash
npm install
```

#### MCP Server 獨立安裝

```bash
cd mcp-server
npm install
```

### Step 3: 構建共享工作區

MCP Server 需要構建以下工作區：

```bash
npm run build --workspace @excalimate/project-schema
npm run build --workspace @excalimate/animation-core
npm run build --workspace @excalimate/mcp-server
```

### Step 4: 啟動開發伺服器

#### 主應用程式

```bash
npm run dev
```

預設訪問地址：`http://localhost:5173`

#### MCP Server（HTTP 模式）

```bash
cd mcp-server
node dist/index.js
```

預設端口：`3001`，訪問地址：`http://localhost:3001/mcp`

#### MCP Server（自訂端口）

```bash
node dist/index.js --port 4000
```

## 4. AI 整合（MCP Server）

### 4.1 基本設定

啟動 MCP Server 後，將 AI 工具指向 `http://127.0.0.1:3001/mcp`。連接後，將列印的預覽配對 URL 複製到 [app.excalimate.com](https://app.excalimate.com) 的 **File → Preferences**，然後點擊 **Live**。

### 4.2 VS Code（GitHub Copilot）設定

在 `.vscode/mcp.json` 中添加：

```jsonc
{
  "mcpServers": {
    "excalimate": {
      "type": "http",
      "url": "http://localhost:3001/mcp"
    }
  }
}
```

### 4.3 Claude Desktop 設定

在 `claude_desktop_config.json` 中添加：

```json
{
  "mcpServers": {
    "excalimate": {
      "command": "npx",
      "args": ["@excalimate/mcp-server", "--stdio"]
    }
  }
}
```

> **注意：** Claude Desktop 使用 stdio 傳輸 — 無即時預覽。使用 `save_checkpoint`，在 [app.excalimate.com](https://app.excalimate.com) 匯入 V2 專案，然後從認證的瀏覽器 UI 分享。

### 4.4 Claude Code（CLI）設定

```bash
npx @excalimate/mcp-server &
claude mcp add excalimate http://localhost:3001/mcp
```

### 4.5 Cursor / Windsurf / 其他 HTTP 客戶端

指向 MCP 客戶端 `http://localhost:3001/mcp` 並啟動伺服器 `npx @excalimate/mcp-server`。

> **提示：** HTTP 模式（預設）啟用 **即時預覽** — 您可在即時中看到 AI 的變更。stdio 模式僅需要那些不支援 HTTP 傳輸的工具。

## 5. AI 技能（可選）

Excalimate 內建 **16 種專業技能**，教導 AI 代理如何創建特定類型的圖表（架構圖、流程圖、序列圖等）並使用適當的動畫模式。技能可大幅提高輸出品質。

### GitHub Copilot 推薦設定

```bash
npx skills add https://github.com/excalimate/excalimate
```

### 手動安裝（任何代理）

複製 `skills/` 目錄到您的專案，或指向代理的技能/上下文配置到技能檔案。每種技能都是獨立的 `SKILL.md` 檔案，可載入為上下文。

### 可用技能列表

- `excalimate-core` — 核心技能
- `animated-presentations` — 動畫演示
- `animation-patterns` — 動畫模式
- `architecture-diagrams` — 架構圖
- `comparison-diagrams` — 比較圖
- `data-pipelines` — 資料流程
- `diagram-theming` — 圖表主題
- `er-diagrams` — ER 圖
- `explainer-animations` — 解釋型動畫
- `export-optimization` — 導出最佳化
- `flowcharts` — 流程圖
- `mind-maps` — 心智圖
- `network-topologies` — 網路拓撲
- `org-charts` — 組織圖
- `sequence-diagrams` — 序列圖
- `timeline-roadmaps` — 時間軸路線圖

## 6. 測試步驟

### Step 1: 執行測試套件

```bash
npm run test
```

### Step 2: 執行 Lint 檢查

```bash
npm run lint
```

### Step 3: 執行 ESLint

```bash
npm run lint
```

### Step 4: 構建專案

```bash
npm run build
```

## 7. 驗證步驟

### 7.1 功能驗證清單

| 功能 | 驗證方法 |
|------|----------|
| 完整 Excalidraw 編輯器 | 嘗試繪製圖形、連接箭頭、添加文字 |
| 關鍵幀動畫 | 調整透明度、位置、縮放、旋轉 |
| 時間軸 | 檢查可收縮音軌和插值曲線 |
| 相機動畫 | 測試縮放/縮放關鍵幀 |
| 導出功能 | 導出為 MP4、WebM、GIF、SVG |
| MCP Server | 連接 AI 代理並創建動畫 |
| 加密分享 | 測試分享連結的加密功能 |

### 7.2 安裝驗證命令

```bash
# 檢查 Node.js 版本
node --version  # 應為 24.x

# 檢查 npm 版本
npm --version

# 驗證 MCP Server 端口
npx @excalimate/mcp-server --help

# 測試 MCP Server 是否啟動
# 應能訪問 http://localhost:3001/mcp
```

### 7.3 功能測試腳本

#### 測試 1：基本動畫流程

```bash
# 啟動主應用程式
npm run dev &

# 啟動 MCP Server
npx @excalimate/mcp-server &

# 等待伺服器啟動
sleep 5

# 訪問 http://localhost:5173 進行手動測試
```

#### 測試 2：MCP Server 工具測試

```bash
# 測試 create_element 工具
curl -X POST http://localhost:3001/mcp -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{}}'

# 測試 add_keyframe 工具
curl -X POST http://localhost:3001/mcp -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":2,"method":"create_element","params":{"type":"rectangle","label":"Test"}}'
```

#### 測試 3：技能載入驗證

```bash
# 驗證技能目錄存在
ls skills/

# 檢查技能檔案
ls skills/*.md
```

## 8. 架構說明

```
excalimate/
├── src/                        # React Web 應用程式（Vite + TypeScript）
│   ├── components/             # UI（Mantine + Tailwind CSS）
│   ├── core/                   # 動畫引擎、插值、播放
│   ├── stores/                 # Zustand 狀態管理
│   ├── services/               # 導出流程、加密、檔案 I/O
│   └── hooks/                  # MCP 即時、快捷鍵、自動儲存
├── mcp-server/                 # MCP Server（Node.js + Express）
│   └── src/server/             # 模組化工具註冊
├── packages/
│   ├── project-schema/         # 共享 V2 專案編碼和驗證
│   ├── animation-core/         # 共享確定性動作編譯器/執行時
│   ├── player-runtime/         # 托管播放器套件、淨化器、播放
│   └── export-runtime/         # 統一導出採樣和工作員
├── skills/                     # AI 技能定義（16 種技能）
└── docs/                       # 設計準則、計劃
```

### 技術棧

| 層次 | 技術 |
|------|------|
| UI | React 19、Mantine 8、Tailwind CSS 4、Tabler Icons |
| Canvas | Excalidraw 0.18 |
| 狀態 | Zustand |
| 動畫 | 自定義關鍵幀引擎含插值和緩動 |
| 導出 | WebCodecs（MP4/WebM）、gif.js、SVG |
| 加密 | Web Crypto API（AES-256-GCM） |
| MCP Server | Node.js、Express、MCP SDK |
| 建置 | Vite 7、TypeScript 5.9 |
| 部署 | Cloudflare Pages、Cloudflare Workers、Cloudflare R2 |

## 9. 使用流程

### V2 創建器工作流程

1. **繪製** — 使用完整 Excalidraw 編輯器或從動畫模板開始
2. **魔法（Magic）** — 預覽本地 Auto Animate、套用預設值或創建場景狀態之間的 Smart Transition
3. **序列（Sequence）** — 重新排序動作並調整平實語言定時（例如「在上一個動作後」或「與上一個動作同時」）
4. **工作室（Studio）** — 開啟先進時間軸、自定義關鍵幀、剪輯範圍、相機和音軌控制
5. **導出** — 導出影片、圖片、動畫 SVG、Lottie 或 dotLottie，或創建加密過期分享連結以進行托管播放

## 10. 隱私敏感部署設定

### Cloudflare Workers 建置

- 配置 landing-page Cloudflare Workers 建置，根目錄為 `landing-page`
- 建置命令：`npm run build`
- 部署命令：`npx wrangler versions upload --config dist/server/wrangler.json`

### Cloudflare 分析設定

- 僅使用 Cloudflare 邊緣/區域聚合流量分析
- **不要**啟用 Cloudflare Web Analytics 瀏覽器標記或導出請求記錄用於分析
- **不要**描述或使用 Cloudflare 的 IP 衍生唯一訪客計數作為匿名
- 在 30 天內刪除原始/導出的 Cloudflare 報告；聚合趨勢報告可保留無固定限制

### PostHog 設定

- 保留在 Cloud EU
- 禁用：IP 捕捉、自動捕捉、會話重放、調查、產品導覽、網頁實驗和功能旗幟
- 設定事件保留時間不超過 12 個月
- 發布前審查 DPA 和子處理商

## 11. 常見問題

### 1. 如何開始動畫我的圖表？

1. 使用完整 Excalidraw 編輯器繪製圖表
2. 使用 **Magic** 預覽 Auto Animate 或套用預設值
3. 使用 **Sequence** 調整動作順序和定時
4. 使用 **Studio** 進行自定義關鍵幀調整
5. 導出為所需的格式

### 2. MCP Server 無法連接？

- 確認 MCP Server 已啟動：`npx @excalimate/mcp-server`
- 檢查防火牆設定
- 驗證 URL 是否正確：`http://localhost:3001/mcp`
- 確認 AI 工具設定正確

### 3. 導出失敗怎麼辦？

- 檢查瀏覽器是否支援 WebCodecs API
- 嘗試其他導出格式
- 清除快取並重新導出
- 查看導出控制台日誌

## 12. 參考資源

- [官方網站](https://excalimate.com/)
- [GitHub 儲存庫](https://github.com/excalimate/excalimate)
- [MCP Server 文件](mcp-server/README.md)
- [V2 用戶指南](docs/v2-user-guide.md)
- [安全與分享](docs/security-and-sharing.md)
- [可訪問性驗證矩陣](docs/accessibility.md)

## 13. 授權

MIT 授權 — 見 [LICENSE](LICENSE)

**報告結束**
