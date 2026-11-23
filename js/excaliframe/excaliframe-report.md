# Excaliframe 技術報告

**版本**: 1.0  
**生成日期**: 2026-11-23  
**作者**: martin-lysk  
**原始來源**: [Excalidraw VS Code Fork](https://github.com/martin-lysk/excalidraw-vscode)

## 📋 摘要

Excaliframe 是一個基於 Excalidraw 的 VS Code 擴充功能，提供動畫圖示和自動導出功能。此擴充功能讓使用者可以建立精美的動畫可視化，並自動導出為 SVG 格式，非常適合用於文件、部落格文章和簡報。

### 主要特色

- 🎬 **動畫圖示**: 支援手繪風格（Draw）、淡入（Fade）和靜態（None）三種動畫類型
- 📦 **自動導出**: 檔案在編輯時自動更新，無需手動導出
- 🎨 **雙主題支援**: 自動導出淺色和深色版本
- 💎 **圖示管理**: 隨機命名、導出切換、圖示引用
- 🌐 **完整整合**: 支援所有 Excalidraw 功能

## 📦 安裝步驟

### 方法一：從 VS Code 市場安裝（推薦）

1. **開啟 VS Code**

2. **開啟擴充功能面板**
   - 按 `Cmd+Shift+X`（Mac）或 `Ctrl+Shift+X`（Windows/Linux）

3. **搜尋 Excaliframe**
   - 在搜尋框輸入 "Excaliframe"

4. **安裝擴充功能**
   - 點擊安裝按鈕
   - 等待安裝完成

### 方法二：從 Releases 下載（手動安裝）

1. **前往 Releases 頁面**
   - 訪問 [Releases 頁面](https://github.com/martin-lysk/excalidraw-vscode/releases)

2. **下載 VSIX 檔案**
   - 下載最新的 `.vsix` 檔案

3. **在 VS Code 中安裝**
   - 開啟擴充功能面板（`Cmd+Shift+X` / `Ctrl+Shift+X`）
   - 點擊擴充功能面板的 "..." 選單
   - 選擇 "Install from VSIX..."
   - 選擇剛下載的 `.vsix` 檔案
   - 等待安裝完成

## ✅ 測試步驟

### 步驟 1：建立第一個動畫圖示

1. **建立新檔案**
   - 使用命令選單（`Cmd+Shift+P`）執行 "Excalidraw: New File"
   - 或建立一個空的 `.excalidraw` 檔案

2. **繪製圖示**
   - 使用 Excalidraw 的工具建立形狀、箭頭、文字等元素
   - 可從瀏覽器繪製並嵌入：`Ctrl+Shift+V`（Mac）/ `Ctrl+Shift+V`（Windows）

3. **建立 Frame**
   - 選取要動畫化的元素
   - 點擊工具列中的 Frame 圖示，或按 `Ctrl/Cmd + Shift + F`
   - Frame 會獲得隨機名稱（如 `jumping__horse`）

4. **啟用導出**
   - 選取 Frame
   - 在 Animation 面板中，切換 "Export" 開關
   - SVG 檔案會自動在相同目錄中建立

### 步驟 2：添加動畫效果

1. **選取 Frame 內的元素**
   - 點擊 Frame 內的特定元素

2. **設定動畫屬性**
   - 在 Animation 面板的 Properties 標籤頁中：
     - **Animation Type**: 選擇 Draw、Fade 或 None
     - **Start**: 動畫開始時間（毫秒）
     - **Duration**: 動畫持續時間（毫秒）

3. **使用時間軸調整**
   - 選取元素：點擊時間軸上的元素以在圖示中選取
   - 移動：拖曳元素左右以改變開始時間
   - 調整大小：拖曳邊緣以調整持續時間
   - 縮放：使用 +/- 按鈕縮放以精確控制
   - 多列：元素可分配到不同列以組織

### 步驟 3：預覽動畫

1. **播放動畫**
   - 點擊 Animation 面板頂部的播放圖示

2. **檢視導出**
   - 將游標懸停在導出檔案上
   - 可看到動畫預覽

3. **調整時間軸**
   - 在時間軸上拖曳以調整時間

## 🔍 驗證步驟

### 驗證 1：確認自動導出功能

1. **修改 Frame 內容**
   - 在 Frame 中添加或修改元素

2. **檢查導出檔案**
   - 確認相同目錄中是否自動產生新的 `.exp.svg` 檔案
   - 驗證檔案命名格式：`{framename}.{type}.{theme}.exp.svg`
   - 驗證檔案是否包含淺色和深色版本

### 驗證 2：確認動畫效果

1. **檢查動畫檔案**
   - 打開導出的 `.anim` 檔案
   - 確認包含 SMIL 動畫資料

2. **測試動畫播放**
   - 在 Frame Reference 檢視器中開啟 `.exp.svg` 檔案
   - 確認動畫正確播放

3. **測試不同主題**
   - 切換 VS Code 主題（淺色/深色）
   - 確認導出檔案對應主題

### 驗證 3：測試 Markdown 整合

1. **在 Markdown 中使用圖示**
   ```markdown
   ![My diagram - dark](./animation.anim.dark.exp.svg#gh-dark-mode-only)
   ![My diagram - light](./animation.anim.light.exp.svg#gh-light-mode-only)
   ```

2. **驗證 GitHub/GitLab**
   - 提交到 GitHub 或 GitLab
   - 確認圖示在不同主題下正確顯示

3. **測試 HTML**
   ```html
   <picture>
     <source srcset="./animation.anim.dark.exp.svg" media="(prefers-color-scheme: dark)">
     <img src="./animation.anim.light.exp.svg" alt="Diagram">
   </picture>
   ```

## ⚙️ 設定選項

### 基本設定

```json
{
  // 主題（預設："light"）
  "excaliframe.theme": "auto",  // "auto", "light", or "dark"

  // 語言（預設：VS Code 顯示語言）
  "excaliframe.language": "en",

  // 工作區路徑庫
  "excaliframe.workspaceLibraryPath": "library.excalidrawlib",

  // 圖片導出設定
  "excaliframe.image": {
    "exportScale": 1,              // 1, 2, or 3
    "exportWithBackground": true,
    "exportWithDarkMode": false
  },

  // Frame 導出 debounce 延遲（毫秒）
  "excalidraw.frameExportDebounce": 500,

  // 贊助者授權金鑰（移除水印）
  "excaliframe.licenseKey": "your-license-key-here"
}
```

### 設定說明

| 設定項目 | 說明 |
|---------|------|
| `theme` | 控制 Excaliframe 的顏色主題 |
| `language` | UI 語言（支援 30+ 種語言） |
| `workspaceLibraryPath` | 路徑庫檔案路徑（相對於工作區根目錄） |
| `image.exportScale` | 嵌入圖片的解析度倍率（1/2/3） |
| `frameExportDebounce` | 修改後重新導出的延遲（毫秒） |
| `licenseKey` | 贊助者授權金鑰（移除水印） |

## 🎬 動畫類型說明

### 1. Draw（✏️）手繪風格

- 元素逐筆劃動畫化，如同手繪
- 最適合：線條、箭頭、方塊、橢圓
- 營造手繪感覺

### 2. Fade（〰️）淡入效果

- 元素從透明到不透明平滑淡入
- 適用於所有元素類型
- 最適合：文字、組合元素、複雜形狀

### 3. None（⃠）靜態

- 無動畫 - 元素立即顯示
- 最適合：靜態背景、標籤、參考元素
- 可與動畫元素混合在同一 Frame 中

## 📦 導出檔案命名規則

檔案命名格式：`{framename}.{type}.{theme}.exp.svg`

| 變數 | 說明 | 範例 |
|------|------|------|
| `framename` | 隨機生成的動詞__動物，或自訂 | `jumping__horse` |
| `type` | `stat`（靜態）或 `anim`（動畫） | `stat`, `anim` |
| `theme` | `light` 或 `dark` | `light`, `dark` |

### 範例導出

```
jumping__horse.stat.light.exp.svg      # 靜態淺色版本
jumping__horse.stat.dark.exp.svg      # 靜態深色版本
jumping__horse.anim.light.exp.svg     # 動畫淺色版本（僅在 Frame 有動畫元素時）
jumping__horse.anim.dark.exp.svg      # 動畫深色版本（僅在 Frame 有動畫元素時）
```

## 💡 進階技巧

### 圖示組織

1. **使用描述性名稱**
   ```
   tutorials/installation/process.diagram
   ../assets/logo.animation
   ```

2. **組合相關元素**
   - 將相關動畫放在同一 Frame

3. **疊加 Frame**
   - 使用多個 Frame 建立複雜圖示

### 動畫最佳實踐

1. **從簡單開始**
   - 一開始只動畫化 1-2 個元素

2. **使用時間軸**
   - 視覺回饋有助於理解時間設定

3. **混合動畫類型**
   - 使用 **Draw** 用於輪廓和箭頭
   - 使用 **Fade** 用於文字和填充形狀
   - 使用 **None** 用於背景

4. **持續時間指南**
   - 快速強調：200-400ms
   - 標準動畫：500-800ms
   - 複雜揭露：1000-1500ms

5. **錯開元素**
   ```
   Element 1: 0ms
   Element 2: 200ms
   Element 3: 400ms
   ```

### 效能提示

1. **限制 Frame 大小**
   - 非常大的 Frame（>50 個元素）可能會變慢

2. **使用 debounce**
   - 如果編輯感覺遲緩，增加 `frameExportDebounce`

3. **選擇性導出**
   - 只切換需要 Frame 的 "Export"

## 🔄 與 Excalidraw VS Code 的差異

Excaliframe 在基礎 [excalidraw-vscode](https://github.com/excalidraw/excalidraw-vscode) 擴充功能上增加了以下功能：

| 功能 | Excalidraw VS Code | Excaliframe |
|------|-------------------|-------------|
| 動畫系統 | ❌ | ✅ 基於時間軸的動畫 |
| 自動導出 | ❌ | ✅ 檔案變更時自動 SVG 導出 |
| Frame 管理 | 基礎 | ✅ 增強 Frame 命名、導出切換、引用 |
| 雙主題導出 | ❌ | ✅ 自動生成淺色和深色版本 |
| 水印系統 | ❌ | ✅ 可選水印，贊助者授權移除 |
| 預覽系統 | ❌ | ✅ 即時預覽，互動式水印移除 |
| SMIL 動畫 | ❌ | ✅ 導出 SVG 包含 SMIL 動畫資料 |

## 📚 工作流程範例

### 建立教學圖示

```
1. 建立 Frame: `tutorial/step1.setup`
2. 添加靜態背景元素（動畫：none）
3. 添加第一個動作（動畫：draw, start: 0ms）
4. 添加說明（動畫：fade, start: 500ms）
5. 導出並使用於文件
```

### Logo 動畫

```
1. 匯入或繪製 Logo
2. 包裹 Frame: `assets/logo.anim`
3. 動畫筆劃（draw）然後填充（fade）
4. 導出用於網頁使用
```

### 架構圖

```
1. 建立基礎圖示 Frame（靜態）
2. 建立覆蓋 Frame 用於流程（動畫）
3. 在 Markdown 中使用不同主題
```

## 🌐 在 Markdown 中使用

### GitHub/GitLab Markdown

```markdown
![Diagram - dark](https://github.com/martin-lysk/excalidraw-vscode/raw/HEAD/animation.anim.dark.exp.svg#gh-dark-mode-only)
![Diagram - light](https://github.com/martin-lysk/excalidraw-vscode/raw/HEAD/animation.anim.light.exp.svg#gh-light-mode-only)
```

### HTML

```html
<picture>
  <source srcset="./animation.anim.dark.exp.svg" media="(prefers-color-scheme: dark)">
  <img src="./animation.anim.light.exp.svg" alt="Diagram">
</picture>
```

### VS Code Markdown

```markdown
![Diagram](https://github.com/martin-lysk/excalidraw-vscode/raw/HEAD/animation.anim.exp.svg)
```

（使用預設主題版本）

## 🙏 致谢

此擴充功能基於 pomdtr 的優秀 [excalidraw-vscode](https://github.com/excalidraw/excalidraw-vscode) 擴充功能分叉。所有原始整合的信用歸屬於 pomdtr 和整個 [Excalidraw](https://excalidraw.com/) 團隊。

## 📄 授權

請參閱 [LICENSE](https://github.com/martin-lysk/excalidraw-vscode/blob/main/LICENSE) 檔案。

*此報告基於 Excaliframe 官方文檔和 GitHub 倉庫內容生成。*
