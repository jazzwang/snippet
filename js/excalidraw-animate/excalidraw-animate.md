# excalidraw-animate 技術報告

## 專案概述

excalidraw-animate 是一個用於將 Excalidraw 繪圖轉換為動畫的外掛工具。使用者可以在 Excalidraw 中繪製圖示、箭頭、文字等元素，並透過設定動畫順序和持續時間，將靜態繪圖轉為動態 SVG 動畫。

**版本資訊**
- 專案版本: 0.7.2
- 最後更新: 2026-11-23
- 技術棧: React 19, Vite 7, TypeScript 5

## 環境需求

### 開發環境需求

- **Node.js**: v18+
- **包管理工具**: pnpm (建議 v11.3.0)
- **作業系統**: Windows/macOS/Linux

### 專案依賴

```json
{
  "dependencies": {
    "@excalidraw/excalidraw": "0.18.1",
    "pako": "2.1.0"
  },
  "devDependencies": {
    "@playwright/test": "^1.60.0",
    "@testing-library/react": "^16.3.2",
    "browser-fs-access": "^0.38.0",
    "eslint": "^9.39.2",
    "prettier": "^3.8.1",
    "vitest": "^4.0.18",
    "vite": "^7.3.1",
    "vitest-canvas-mock": "^1.1.3"
  }
}
```

## 安裝步驟

### 步驟 1: 複製專案

```bash
# 從 GitHub 克隆
git clone https://github.com/dai-shi/excalidraw-animate.git
cd excalidraw-animate

# 或者使用 pnpm 安裝 NPM 套件
pnpm add excalidraw-animate
```

### 步驟 2: 安裝依賴

```bash
# 使用 pnpm 安裝
pnpm install
```

### 步驟 3: 驗證安裝

```bash
# 檢查 TypeScript 編譯
pnpm run test:type

# 檢查程式碼格式
pnpm run test:format

# 執行 ESLint 檢查
pnpm run test:lint
```

## 測試步驟

### 步驟 1: 執行單元測試

```bash
# 執行 Vitest 單元測試
pnpm run test:spec

# 執行所有測試
pnpm run test
```

### 步驟 2: 執行端對端測試 (E2E)

```bash
# 使用 Playwright 執行 E2E 測試
pnpm run e2e

# 僅使用 Chromium
pnpm run e2e:ci

# 以 UI 模式執行 (需要 Playwright 圖形介面)
pnpm run e2e:ui
```

### 步驟 3: 執行測試覆蓋率

```bash
# 測試會自動生成覆蓋率報告
# 報告位置通常在 coverage/ 目錄
```

## 驗證步驟

### 方式一: 開發環境驗證

```bash
# 啟動開發伺服器
pnpm run dev

# 訪問 http://localhost:5173
```

**驗證項目:**

1. **基本 UI 元素**
   - Edit/Animate 切換按鈕
   - 主題切換按鈕 (🌙/☀️)
   - Load File 按鈕
   - Load Library 按鈕
   - Animate! 按鈕

2. **模式切換功能**
   ```
   預設模式：Animate
   點擊 Edit 按鈕 → 切換到 Edit 模式
   點擊 Animate 按鈕 → 切換回 Animate 模式
   ```

3. **主題切換功能**
   ```
   預設主題：Light mode (顯示 🌙 圖示)
   點擊主題按鈕 → 切換為 Dark mode (顯示 ☀️ 圖示)
   再次點擊 → 恢復 Light mode
   ```

### 方式二: 使用 NPM 套件

```bash
# 安裝套件
pnpm add excalidraw-animate

# 在您的專案中使用
import excalidrawAnimate from 'excalidraw-animate';

// 或導出 library
import { library } from 'excalidraw-animate';
```

### 方式三: 使用線上演示

訪問 https://dai-shi.github.io/excalidraw-animate

## 功能驗證

### 1. 載入檔案

```bash
# 測試檔案載入流程
1. 在 Excalidraw 中創建繪圖
2. 選擇 File → Export as JSON
3. 回到 excalidraw-animate
4. 點擊 Load File
5. 選擇 .excalidraw 或 .json 檔案
```

**預期結果**:
- 繪圖正確顯示
- 所有元素可編輯
- 儲存狀態至 localStorage

### 2. 載入 Library

```bash
# 測試 Library 載入
1. 在 Excalidraw 中創建多組繪圖
2. 選擇 File → Export as Library
3. 產生 .excalidrawlib 檔案
4. 回到 excalidraw-animate
5. 點擊 Load Library
6. 選擇 .excalidrawlib 檔案
```

**預期結果**:
- 每個 Library item 獨立動畫
- 可分別設定每個 item 的 Order 和 Duration

### 3. 連結動畫

```bash
# 測試連結動畫
1. 使用 Excalidraw shareable link: https://excalidraw.com/#json=xxxxx,yyyyy
2. 或直接連結到 Library 檔案: https://example.com/file.excalidrawlib
3. 複製連結並貼到 excalidraw-animate
4. 點擊 Animate!
```

**預期結果**:
- 連結正確解碼
- 繪圖正確顯示
- 動畫正常播放

## 動畫功能驗證

### 元素類型支援

| 元素類型 | 動畫支援 | 備註 |
|---------|---------|------|
| Line (線條) | ✅ | 支援圓角線條 |
| Arrow (箭頭) | ✅ | 支援箭頭頭部 |
| Rectangle (矩形) | ✅ | 支援圓角矩形 |
| Diamond (菱形) | ✅ | 使用 rectangle 動畫邏輯 |
| Ellipse (橢圓) | ✅ | 支援圓角橢圓 |
| Text (文字) | ✅ | 文字沿路徑出現 |
| FreeDraw (自由繪畫) | ✅ | 點點出現動畫 |
| Image (圖片) | ✅ | 透明度漸變 |

### 動畫設定項目

#### Order (動畫順序)
- **功能**: 設定元素動畫播放順序
- **預設值**: 0 (按創建順序播放)
- **設定方式**: 選擇元素後在 Animate 模式設定
- **群組元素**: 顯示 "Mixed" 提示，可統一設定或保留原值

#### Duration (動畫持續時間)
- **功能**: 設定單個元素動畫持續時間
- **單位**: 毫秒 (ms)
- **預設值**:
  - 個別元素: 500ms
  - 群組元素: 5000ms 總時間 (平均分配)
- **群組動畫**: 5 秒總時長，均分給群組成員

### 指針功能驗證

```bash
# 指針功能測試
1. 點擊 Pointer 區域的 File... 按鈕
2. 選擇或輸入指針圖片 URL
3. 設定指針寬度 (px)
```

**預期結果**:
- 指針圖片正確顯示
- 指針寬度可自訂
- 指針沿著元素路徑顯示

## 導出功能驗證

### SVG 導出

```bash
# 測試 SVG 導出
1. 完成動畫設定
2. 導出 SVG 檔案
3. 使用任何 SVG 查看器打開
```

**驗證項目**:
- SVG 檔案結構正確
- 動畫標籤 (animate, animateMotion) 正確生成
- 所有元素動畫順序正確

### WebM 導出

```bash
# 測試 WebM 導出
1. 完成動畫設定
2. 導出 WebM 檔案
3. 使用瀏覽器或媒體播放器播放
```

**注意**: WebM 導出功能可能不完美，建議使用螢幕錄製作為備選方案

## 已知問題

1. **WebM 導出**: 導出功能可能不完美，建議使用螢幕錄製
2. **群組元素**: 群組元素顯示 "Mixed" 提示，需特別注意
3. **Edit/Animate 模式**: 
   - 兩種模式使用不同資料
   - 從 Edit 模式導出後，在 Animate 模式載入
   - 導出的 SVG 無法在 Edit 模式編輯

## 最佳實踐

### 1. 檔案管理

```bash
# 編輯模式載入後，重新儲存
# 選擇 File → Export as JSON → 勾選 "Embed scene"
# 此確保資料不會遺失
```

### 2. 群組動畫設定

```bash
# 當群組元素有不同 Order 時
# 1. 選擇所有群組元素
# 2. 觀察 Order 欄位顯示 "Mixed"
# 3. 可選擇：
#    - 保留原值 (不改變)
#    - 統一設定新值 (適用於所有選中元素)
```

### 3. 指針圖片最佳化

```bash
# 推薦格式: PNG, SVG
# 建議尺寸: 20-40px
# 透明度支援: 推薦使用
```

## 開發檔案結構

```
excalidraw-animate/
├── src/
│   ├── AnimateApp.tsx    # 動畫模式主應用程式
│   ├── AnimateConfig.tsx # 動畫設定組件
│   ├── App.tsx           # 主應用程式 (Edit/Animate 切換)
│   ├── ExcalidrawApp.tsx # 編輯模式應用程式
│   ├── Viewer.tsx        # SVG 查看器 (網格佈局)
│   ├── animate.ts        # 核心動畫邏輯
│   ├── export.ts         # 導出功能 (SVG/WebM)
│   ├── library.ts        # Library 載入
│   ├── Toolbar.tsx       # 工具列
│   └── useLoadSvg.ts     # SVG 載入 Hook
├── e2e/                  # 端對端測試
├── test/                 # 單元測試
├── vite.config.ts        # Vite 配置
└── package.json          # 專案依賴
```

## 測試覆蓋

### 基本測試項目

```bash
# UI 元素測試
- Edit/Animate 切換
- 主題切換
- Load File/Library
- Animate! 按鈕

# 功能測試
- 模式切換
- 載入檔案
- 動畫播放
- SVG/WebM 導出
```

### E2E 測試流程

```bash
pnpm run e2e
# 測試項目:
# - Basic UI 元素可見性
# - 模式切換功能
# - 主題切換功能
```

## 常見問題解決方案

### 問題 1: 無法載入檔案

**症狀**: 點擊 Load File 後無反應

**解決方案**:
```bash
# 1. 確認檔案格式正確 (.excalidraw 或 .json)
# 2. 檢查瀏覽器控制台是否有錯誤
# 3. 重新載入檔案
```

### 問題 2: 動畫不播放

**症狀**: 點擊播放按鈕無動畫

**解決方案**:
```bash
# 1. 確認已選擇動畫元素
# 2. 檢查 Order/Duration 設定
# 3. 重新設定動畫參數
```

### 問題 3: WebM 導出失敗

**症狀**: 導出 WebM 檔案為空白或錯誤

**解決方案**:
```bash
# 使用螢幕錄製替代
# 或使用其他瀏覽器導出
```

## 參考資源

- **官方文件**: https://github.com/dai-shi/excalidraw-animate
- **線上演示**: https://dai-shi.github.io/excalidraw-animate
- **NPM 套件**: https://www.npmjs.com/package/excalidraw-animate
- **Excalidraw**: https://excalidraw.com

*技術報告生成時間: 2026-11-23*
