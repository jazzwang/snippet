# Excalidraw 技術報告

## 摘要

Excalidraw 是一款開源的虛擬白板工具，用於繪製手繪風格的圖表。本文提供詳細的安裝、測試和驗證步驟。

**報告日期：** 2026-11-24

## 1. 專案概述

Excalidraw 是一個免費且開源的虛擬白板，支援協同編輯和端到端加密。主要特性包括：

- 🎨 無限畫布基於的白板
- ✍️ 手繪風格
- 🌓 深色模式
- 📷 圖片支援
- 🔒 端到端加密
- 💾 本地優先支援（自動儲存至瀏覽器）
- 🔗 可分享連結

## 2. 安裝步驟

### 2.1 系統要求

| 項目 | 版本要求 |
|------|----------|
| Node.js | 建議 v16+ |
| Yarn | v1 或 v2.4.2+ |
| Git | 最新版本 |

### 2.2 克隆倉庫

```bash
git clone https://github.com/excalidraw/excalidraw.git
cd excalidraw
```

### 2.3 安裝相依套件

```bash
yarn
```

安裝後會建立以下目錄結構：

- `packages/` - 核心功能模組
- `excalidraw-app/` - 前端應用程式
- `packages/cli/` - CLI 工具
- `packages/core/` - 核心渲染引擎

### 2.4 啟動開發伺服器

```bash
yarn start
```

預設啟動在 `http://localhost:3000`

### 2.5 自我部署（Docker）

```bash
# 建立 Docker 映像檔
docker build -t excalidraw/excalidraw .

# 執行容器
docker run --rm -it -p 8080:8080 -v excalidraw-data:/data excalidraw/excalidraw
```

或使用 Docker Compose：

```bash
docker-compose up --build -d
```

## 3. 測試步驟

### 3.1 執行單元測試

Excalidraw 使用 **Vitest** 作為測試框架，並配置為模擬瀏覽器環境。

```bash
# 執行所有測試
yarn test

# 執行測試並顯示覆蓋率
yarn test --coverage

# 執行特定測試檔案
yarn test tests/elements.test.ts
```

### 3.2 測試配置

測試環境配置於 `vitest.config.mts`：

```typescript
import path from "path";
import { defineConfig } from "vitest/config";

export default defineConfig({
  resolve: {
    alias: [
      {
        find: /^@excalidraw\/common$/,
        replacement: path.resolve(__dirname, "./packages/common/src/index.ts"),
      },
      {
        find: /^@excalidraw\/common\/(.*?)/,
        replacement: path.resolve(__dirname, "./packages/common/src/$1.ts"),
      },
    ],
  },
  test: {
    globals: true,
    environment: "jsdom",
    setupFiles: ["./packages/core/src/test/setupTests.ts"],
  },
});
```

### 3.3 執行端對端測試（E2E）

```bash
# 執行 Cypress E2E 測試
yarn cy:test

# 執行特定測試套件
yarn cy:test --spec "cypress/e2e/**/collaboration.cy.ts"
```

### 3.4 依賴檢查

```bash
# 檢查相依套件版本
yarn why

# 檢查相依套件安全性
yarn audit
```

## 4. 驗證步驟

### 4.1 功能驗證清單

| 功能 | 驗證方法 |
|------|----------|
| 畫布互動 | 點擊、拖拽、縮放 |
| 圖形工具 | 矩形、圓形、箭頭、自由繪圖 |
| 物件操作 | 選取、移動、旋轉、刪除 |
| 文字輸入 | 新增、編輯、刪除文字 |
| 圖層管理 | 層級調整、隱藏/顯示 |
| 匯出功能 | PNG、SVG、剪貼簿 |
| 深色模式 | UI 切換 |
| 無障礙性 | 鍵盤快捷鍵、螢幕閱讀器 |

### 4.2 本地測試驗證

```bash
# 1. 啟動開發環境
yarn start

# 2. 開啟瀏覽器 http://localhost:3000

# 3. 執行以下測試用例：

# 3.1 基本繪圖功能
- 新增矩形、圓形、三角形
- 新增箭頭和連線
- 使用自由繪圖工具

# 3.2 物件操作
- 選取物件（點擊、框選）
- 移動、旋轉、縮放
- 刪除物件（Delete 鍵）

# 3.3 文字輸入
- 新增文字框
- 編輯文字內容
- 調整字體大小和顏色

# 3.4 匯出功能
- 匯出為 PNG
- 匯出為 SVG
- 複製到剪貼簿

# 3.5 儲存功能
- 自動儲存至瀏覽器
- 匯出為 .excalidraw JSON 檔案

# 4. 驗證測試結果
- 所有功能正常運作
- 無控制台錯誤
- 無瀏覽器警告
```

### 4.3 性能測試

```bash
# 執行性能測試
yarn test --run --reporter=verbose

# 監控記憶體使用
watch --node-options='--max-old-space-size=4096' -r ts-node/register ./scripts/performance-monitor.ts
```

### 4.4 安全性驗證

```bash
# 檢查已知安全問題
yarn audit

# 檢查相依套件漏洞
yarn audit --groups dependencies

# 驗證加密實現
# 1. 檢查端到端加密是否正確實現
# 2. 驗證資料傳輸使用 HTTPS
# 3. 確認沒有未授權的資料外洩
```

## 5. 相依套件分析

### 5.1 主要相依套件

| 相依套件 | 版本 | 用途 |
|----------|------|------|
| React | 17-19 | UI 框架 |
| React DOM | 17-19 | DOM 渲染 |
| @braintree/sanitize-url | 6.0.2+ | URL 清理 |
| @excalidraw/laser-pointer | 1.3.1+ | 雷射指針功能 |
| @excalidraw/mermaid-to-excalidraw | 2.2+ | Mermaid 圖表轉換 |

### 5.2 開發相依套件

| 相依套件 | 用途 |
|----------|------|
| TypeScript | 類型檢查 |
| Vite | 建構工具 |
| Vitest | 測試框架 |
| ESLint | 程式碼檢查 |
| Prettier | 程式碼格式化 |

### 5.3 Peer Dependencies

Excalidraw 支援以下 React 版本：
- React 17
- React 18
- React 19

## 6. 常見問題排解

### 6.1 相依套件安裝失敗

```bash
# 清除快取
rm -rf node_modules yarn.lock

# 重新安裝
yarn install --frozen-lockfile
```

### 6.2 Port 已被使用

```bash
# 修改 .env 檔案中的 PORT
PORT=3001

# 或停止佔用端口的程式
lsof -ti:3000 | xargs kill
```

### 6.3 構建失敗

```bash
# 清除快取並重新構建
rm -rf .turbo node_modules
yarn install
yarn build
```

### 6.4 Docker 啟動失敗

```bash
# 檢查 Docker 狀態
docker ps -a

# 檢查日誌
docker logs <container_id>

# 重新建立容器
docker-compose down
docker-compose up --build -d
```

## 7. 整合 Excalidraw NPM 套件

### 7.1 快速開始

```bash
# 安裝套件
npm install react react-dom @excalidraw/excalidraw
# 或
yarn add react react-dom @excalidraw/excalidraw
```

### 7.2 使用範例

```jsx
import { Excalidraw } from "@excalidraw/excalidraw";
import "@excalidraw/excalidraw/dist/browser/index.css";

function App() {
  const elements = [
    // 初始元素
  ];

  return (
    <div style={{ width: "100%", height: "100vh" }}>
      <Excalidraw
        initialElements={elements}
        // 自定義配置
      />
    </div>
  );
}
```

### 7.3 自訂主題

```jsx
<Excalidraw
  theme={{
    primaryColor: "#1a73e8",
    secondaryColor: "#1e8e3e",
  }}
  showGrid={true}
  showLibraryMenu={false}
  showIdlePopup={false}
>
</Excalidraw>
```

## 8. 貢獻指引

### 8.1 開發流程

```bash
# 1. Fork 倉庫
git clone https://github.com/your-username/excalidraw.git
cd excalidraw

# 2. 建立分支
git checkout -b feature/my-feature

# 3. 執行開發環境
yarn start

# 4. 執行測試
yarn test

# 5. 提交程式碼
git add .
git commit -m "feat: 新增功能"

# 6. 推送到遠端
git push origin feature/my-feature
```

### 8.2 程式碼風格

```bash
# 格式化程式碼
yarn lint
yarn format

# 檢查類型
yarn type-check
```

### 8.3 提交訊息規範

- `feat:` 新功能
- `fix:` 修復問題
- `docs:` 文件變更
- `style:` 程式碼格式變更
- `refactor:` 重構
- `test:` 新增測試
- `chore:` 其他變更

## 9. 參考資源

- [官方文件](https://docs.excalidraw.com)
- [Excalidraw.com](https://excalidraw.com)
- [GitHub 倉庫](https://github.com/excalidraw/excalidraw)
- [Excalidraw+](https://plus.excalidraw.com)
- [Discord 討論區](https://discord.gg/UexuTaE)

## 10. 版本資訊

| 版本 | 發布日期 | 主要變更 |
|------|----------|----------|
| 0.18.1 | 2026-09-28 | 安全修補、Mermaid XSS 修復 |
| 0.18.0 | 2026-09-XX | 協同功能增強 |
| 0.17.1 | 2026-XX-XX | 效能優化 |

## 附錄 A：快速命令清單

```bash
# 開發環境
yarn start

# 測試
yarn test

# 覆蓋率報告
yarn test --coverage

# 建構
yarn build

# 清理
yarn clean

# 相依套件更新
yarn upgrade-interactive

# Docker
docker-compose up
docker-compose down
```

*報告完成於 2026-11-24*
