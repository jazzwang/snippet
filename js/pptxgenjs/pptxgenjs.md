# pptxgenjs

- Git Repo
  - https://github.com/gitbrent/PptxGenJS
- Website
  - https://gitbrent.github.io/PptxGenJS/
- npm
  - https://www.npmjs.com/package/pptxgenjs

## 2026-08-18

- 緣起：因為 Anthropic 的 pptx skill 會使用 pptxgenjs 來生成投影片，所以想進一步理解一些細節。
- https://share.google/aimode/q5ecXFBptc4otfp6k

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI Mode
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
pptxgenjs 可以自訂公司的 theme 跟 icon 嗎?
</td></tr><tr><td>A:</td><td>

可以，PptxGenJS 完全支援自訂公司的 Theme（主題顏色、字型、母片版型）與 Icon 圖示。
雖然 PptxGenJS 是透過 JavaScript 程式碼動態生成簡報，不像 PowerPoint 軟體有可視化的自訂介面，但你可以透過定義全域變數、設定 Slide Master（母片）以及讀取圖片編碼來達到完全品牌化的效果。

### 一、 如何自訂公司的 Theme (主題)

在 PptxGenJS 中，自訂主題主要透過定義顏色、字型以及建立Slide Master（母片版型）來實現。

#### 1. 定義品牌顏色與字型

建議在專案開頭建立一個常數物件，方便統一管理品牌視覺：

```js
const COMPANY_THEME = {
  fontFace: "Microsoft JhengHei", // 支援系統字型，如微軟正黑體
  colors: {
    primary: "003366",   // 填入 6 碼 HEX 顏色（不含 #）
    secondary: "FF6600",
    accent: "F5F5F5",
    text: "333333"
  }
};
```

#### 2. 建立 Slide Master (簡報母片)

利用 pptx.defineSlideMaster() 功能，你可以像在 PowerPoint 裡一樣，設定每一頁投影片的預設背景、頁首、頁尾和公司 Logo：

```js
import pptxgen from "pptxgenjs";let pptx = new pptxgen();
// 定義公司專屬的母片版型
pptx.defineSlideMaster({
  title: "COMPANY_INTERNAL_TEMPLATE",
  background: { color: COMPANY_THEME.colors.accent },
  objects: [
    // 預設公司 Logo (可使用網路圖片 URL 或 Base64 格式)
    { image: { x: 0.5, y: 0.3, w: 1.5, h: 0.4, path: "https://yourcompany.com" } },
    // 預設頁尾版權宣告
    { 
      text: { 
        text: "© 2026 Your Company All Rights Reserved.", 
        options: { x: 0.5, y: 7.1, w: 5.0, h: 0.3, fontSize: 10, color: "999999", fontFace: COMPANY_THEME.fontFace } 
      } 
    },
    // 裝飾用條紋（品牌主色）
    { rect: { x: 0, y: 0, w: "100%", h: 0.1, fill: { color: COMPANY_THEME.colors.primary } } }
  ],
  slideNumber: { x: 9.5, y: 7.1, fontFace: COMPANY_THEME.fontFace, fontSize: 10, color: "999999" }
});
// 套用此母片建立新投影片
let slide = pptx.addSlide({ masterName: "COMPANY_INTERNAL_TEMPLATE" });
```

### 二、 如何自訂公司的 Icon (圖示)

PptxGenJS 沒有內建的 Icon 庫，但你可以透過以下三種方式自由加入公司專屬的 Icon：

#### 1. 使用 SVG 格式（最推薦：向量不失真）

你可以直接將 SVG 圖示的 Path 帶入，這樣產生的 Icon 不管放大縮小都不會模糊，還能動態修改 Icon 顏色：

```js
slide.addShape(pptx.ShapeType.custGeom, {
  x: 1.0, y: 1.0, w: 0.5, h: 0.5,
  fill: { color: COMPANY_THEME.colors.secondary }, // 動態變更 Icon 顏色
  points: [
    // 這裡放入 SVG 的 Path Data
    { m: [0, 0], l: [100, 0], l: [100, 100], l: [0, 100], z: true } 
  ]
});
```

(註：複雜的 SVG 轉換較繁瑣，一般會推薦使用下方的圖片路徑法)

#### 2. 使用圖片路徑 (PNG / JPG / SVG 檔案)

最直覺的方式，直接讀取公司內部伺服器或專案資料夾中的 Icon 圖檔：

```js
slide.addImage({ 
  path: "images/icons/user-icon.png", 
  x: 2.0, 
  y: 2.0, 
  w: 0.4, 
  h: 0.4 
});
```

#### 3. 使用 Base64 編碼（適合無網路環境/獨立封裝）

如果你希望產生的程式碼不依賴外部圖片檔案，可以事先把 Icon 轉成 Base64 字串包在程式碼中：

```js
const ICON_USER = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA...";

slide.addImage({ 
  data: ICON_USER, 
  x: 3.0, 
  y: 2.0, 
  w: 0.4, 
  h: 0.4 
});
```

### 三、 實務開發建議

1. 打包成公司專屬模組：建議將上述的 defineSlideMaster 與 COMPANY_THEME 獨立寫成一個 theme.js。其他專案要產生 PPT 時，直接 import 該設定檔，就能確保全公司產出的簡報視覺完全一致。
2. 文字樣式重用：在 slide.addText() 時，多加利用展開運算子 (...) 來套用定義好的文字主題，例如：

```js
const TITLE_STYLE = { fontFace: COMPANY_THEME.fontFace, fontSize: 24, color: COMPANY_THEME.colors.primary, bold: true };
slide.addText("專案報告", { x: 0.5, y: 1.0, ...TITLE_STYLE });
```
      
若您想進一步了解特定的實作細節，可以告訴我：

* 您打算在前端瀏覽器還是 Node.js 後端環境執行？
* 是否需要幫您寫一份完整的自動化產生腳本範例？

</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
預計用 Node.js 後段生成。可以給我一份自訂 Slide Master 的專案範例嗎?
</td></tr><tr><td>A:</td><td>
這裡為您準備一份在 Node.js 後端環境執行的完整專案範例。
這個範例會示範如何建立獨立的 theme.js 模組，並在主程式中建立一個具備公司標準母片（含 Logo、主色調線條、頁尾宣告、頁碼）的簡報，最後將檔案儲存至本地端。

#### 1. 初始化專案與安裝套件

首先，在您的專案資料夾中執行以下指令來安裝 pptxgenjs：

```bash
npm init -y
npm install pptxgenjs
```

注意： 在 Node.js 環境中，如果母片或投影片有使用到 path 讀取本地圖片，請確保路徑正確。本範例將直接使用 Base64 編碼來處理公司 Logo，這在後端執行時最為穩定，不需擔心相對路徑或網路斷線問題。

#### 2. 建立主題設定檔：theme.js

將品牌顏色、字型與母片邏輯獨立出來，方便未來維護。

```js
// theme.js
const pptxgen = require("pptxgenjs");
// 1. 定義公司品牌視覺規範 (全域變數)const COMPANY_THEME = {
  fontFace: "Arial", // 後端環境建議選用系統通用字型
  colors: {
    primary: "003366",   // 科技深藍
    secondary: "FF6600", // 活力橘
    bgLight: "F8F9FA",   // 淺灰背景
    textDark: "212529",  // 深灰內文
    textMuted: "6C757D" // 頁尾淡灰
  },
  // 模擬一個簡單的公司 Logo Base64 ( 1x1 像素的透明圖，實務上請替換成您公司的 Logo Base64 )
  logoBase64: "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="
};
// 2. 封裝母片註冊函式
function registerCompanyMaster(pptx) {
  pptx.defineSlideMaster({
    title: "COMPANY_STANDARD_LAYOUT",
    background: { color: COMPANY_THEME.colors.bgLight },
    objects: [
      // 頂部品牌主色裝飾條
      { rect: { x: 0, y: 0, w: "100%", h: 0.15, fill: { color: COMPANY_THEME.colors.primary } } },
      
      // 左上角公司 Logo
      { image: { x: 0.6, y: 0.4, w: 1.2, h: 0.4, data: COMPANY_THEME.logoBase64 } },
      
      // 右上角裝飾小字 (如：部門名稱或機密層級)
      { 
        text: { 
          text: "CONFIDENTIAL / INTERNAL USE ONLY", 
          options: { x: 7.0, y: 0.4, w: 5.7, h: 0.3, align: "right", fontSize: 9, color: COMPANY_THEME.colors.textMuted, fontFace: COMPANY_THEME.fontFace } 
        } 
      },
      
      // 底部中央：頁尾版權宣告
      { 
        text: { 
          text: "© 2026 Your Company Name. All rights reserved.", 
          options: { x: 1.0, y: 7.0, w: 11.3, h: 0.3, align: "center", fontSize: 9, color: COMPANY_THEME.colors.textMuted, fontFace: COMPANY_THEME.fontFace } 
        } 
      }
    ],
    // 右下角：自動頁碼設定
    slideNumber: { x: 12.3, y: 7.0, fontFace: COMPANY_THEME.fontFace, fontSize: 9, color: COMPANY_THEME.colors.textMuted }
  });
}
// 3. 常用文字樣式組合（文字 Theme）const TEXT_STYLES = {
  title: { fontFace: COMPANY_THEME.fontFace, fontSize: 28, color: COMPANY_THEME.colors.primary, bold: true },
  subtitle: { fontFace: COMPANY_THEME.fontFace, fontSize: 18, color: COMPANY_THEME.colors.secondary },
  body: { fontFace: COMPANY_THEME.fontFace, fontSize: 14, color: COMPANY_THEME.colors.textDark, align: "left" }
};

module.exports = {
  COMPANY_THEME,
  registerCompanyMaster,
  TEXT_STYLES
};
```

#### 3. 建立主程式：index.js

引入主題設定，動態生成投影片並輸出成實體檔案。

```js
// index.js
const pptxgen = require("pptxgenjs");
const { registerCompanyMaster, TEXT_STYLES, COMPANY_THEME } = require("./theme");
// 初始化
PptxGenJSlet pptx = new pptxgen();
// 設定簡報尺寸為 16:9 寬螢幕
pptx.layout = "LAYOUT_169";
// 步驟一：註冊我們自訂的公司母片
registerCompanyMaster(pptx);
// 步驟二：新增第一頁投影片 (套用自訂母片)
let slide1 = pptx.addSlide({ masterName: "COMPANY_STANDARD_LAYOUT" });
// 寫入標題與副標題 (使用解構賦值套用文字 Theme)
slide1.addText("2026 年度第一季營運報告", { x: 0.6, y: 2.0, w: 12.0, h: 0.6, ...TEXT_STYLES.title });
slide1.addText("報告人：研發部門主管", { x: 0.6, y: 2.7, w: 12.0, h: 0.4, ...TEXT_STYLES.subtitle });

// 步驟三：新增第二頁投影片 (同樣套用母片，展示內文與區塊)let slide2 = pptx.addSlide({ masterName: "COMPANY_STANDARD_LAYOUT" });

slide2.addText("核心季度目標", { x: 0.6, y: 1.5, w: 5.0, h: 0.5, ...TEXT_STYLES.title });
// 建立一個帶有公司主色的數據卡片區塊 (Shape + Text)
slide2.addShape(pptx.ShapeType.roundRect, { 
  x: 0.6, y: 2.5, w: 3.5, h: 2.0, 
  fill: { color: "FFFFFF" }, 
  line: { color: COMPANY_THEME.colors.primary, width: 2 } 
});

slide2.addText("營收成長率", { x: 0.8, y: 2.8, w: 3.1, h: 0.4, ...TEXT_STYLES.body, bold: true });
slide2.addText("+ 150%", { x: 0.8, y: 3.3, w: 3.1, h: 0.8, fontFace: COMPANY_THEME.fontFace, fontSize: 36, color: COMPANY_THEME.colors.secondary, bold: true });

// 步驟四：存檔輸出 (Node.js 專屬的 writeFile 功能)const outputFileName = "Company_Report_2026.pptx";

pptx.writeFile({ fileName: outputFileName })
  .then(fileName => {
    console.log(`🎉 簡報生成成功！檔案已儲存至: ${fileName}`);
  })
  .catch(err => {
    console.error("❌ 簡報生成失敗:", err);
  });
```

#### 4. 執行與驗證

在終端機執行主程式：

```bash
node index.js
```

預期結果：

* 您的專案目錄下會多出一個 Company_Report_2026.pptx 檔案。
* 打開後，兩頁投影片都會自動帶有深藍頂條、Logo、頁尾宣告與自動遞增的頁碼（第 1 頁與第 2 頁）。

不曉得這套架構是否符合您的系統需求？如果接下來需要加入動態圖表 (Charts) 或 資料庫表格 (Tables)，我也可以提供對應的主題配色程式碼。

</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
有辦法將 Figma Slide 的範本匯出成 pptxgenjs 的 theme.js 嗎?是否需要先轉換成 HTML?
</td></tr><tr><td>A:</td><td>

沒辦法直接一鍵匯出，而且「先轉換成 HTML」對產生 theme.js 沒有幫助。

Figma 官方提供直接匯出成實體 .pptx 檔的功能，而許多社群外掛則專門用來轉換成「可編輯」的 PowerPoint 檔案。然而，PptxGenJS 本質上是一套「程式碼驅動」的渲染引擎，它需要的是明確的座標數字、HEX 顏色字串和文字大小配置，而不是圖形介面的設計檔或 HTML 標籤。 [1, 2, 3, 4] 

如果希望自動化將 Figma 設計轉化為 PptxGenJS 代碼，以下是實務上的最佳解決方案：

### 一、 為什麼不需要先轉成 HTML？

許多開發者會誤以為 PptxGenJS 支援類似 html2canvas 的做法。實際上，雖然 PptxGenJS 有一個 htmlToSlides() 的功能，但它的限制極其嚴格：

* 它只能粗糙地解析標準的 HTML `<table>` 表格。
* 它完全無法解析複雜的 CSS 佈局（如 Flexbox, Grid, 圓角, 陰影等）。
* 如果先將 Figma 轉成 HTML，再丟給 PptxGenJS，最終生成的簡報高機率會嚴重跑版、字型錯亂。 [1, 2, 5, 6, 7, 8] 

### 二、 正確的工程實作法：利用 Figma API 自動化生成

如果公司的 Figma 設計稿經常變動，需要經常同步到後端的 theme.js，最標準的自動化流程是：直接讀取 Figma REST API，並透過一個簡單的 Node.js 腳本將其轉換為 PptxGenJS 代碼。

#### 1. 轉換邏輯

Figma 所有的設計元素都可以透過 API 取得 JSON 格式的樹狀結構（Figma Node）。您可以寫一個 Node.js 工具來解析這些屬性：

* 顏色： 將 Figma 的 fills[0].color (RGB 0~1) 乘以 255，轉換為 PptxGenJS 所需的 6 碼 HEX 字串。
* 位置： 讀取 Figma 框線（Frame）的 absoluteBoundingBox（取得 x, y, width, height）。
* 單位轉換（關鍵）： Figma 使用的是像素（Pixels, px），而 PptxGenJS 使用的是英吋（Inches）。您需要在腳本中加入轉換公式：

    ```mermaid
    graph LR
    A["$$\text{Inches} = \frac{\text{Pixels}}{\text{96}}$$"]
    ```

(註：通常 16:9 簡報在 Figma 中會設定為 1280x720 px，除以 96 後剛好對應 PptxGenJS 預設的 13.33 x 7.5 英吋)

#### 2. 自動化轉換腳本範例 (Node.js)

您可以撰寫一個如下的本地端轉換工具（例如 parse-figma.js）：

```js
// parse-figma.jsconst fs = require('fs');
// 模擬從 Figma API 獲取的 JSON 數據const figmaTextNode = {
  name: "Slide Title",
  type: "TEXT",
  absoluteBoundingBox: { x: 57.6, y: 144, width: 480, height: 48 }, // 單位：px
  style: {
    fontFamily: "Arial",
    fontSize: 24,
    fills: [{ color: { r: 0, g: 0.2, b: 0.4 } }] // 科技深藍
  }
};
// 像素轉英吋工具函式const pxToInch = (px) => Number((px / 96).toFixed(2));
// RGB 轉 HEX 工具函式const rgbToHex = (r, g, b) => {
  const toHex = (c) => Math.round(c * 255).toString(16).padStart(2, '0');
  return `${toHex(r)}${toHex(g)}${toHex(b)}`.toUpperCase();
};
// 生成 PptxGenJS 配置const pptxConfig = {
  text: figmaTextNode.name,
  options: {
    x: pxToInch(figmaTextNode.absoluteBoundingBox.x),
    y: pxToInch(figmaTextNode.absoluteBoundingBox.y),
    w: pxToInch(figmaTextNode.absoluteBoundingBox.width),
    h: pxToInch(figmaTextNode.absoluteBoundingBox.height),
    fontFace: figmaTextNode.style.fontFamily,
    fontSize: figmaTextNode.style.fontSize,
    color: rgbToHex(figmaTextNode.style.fills[0].color.r, figmaTextNode.style.fills[0].color.g, figmaTextNode.style.fills[0].color.b)
  }
};
// 輸出成可以被 theme.js 讀取的 JSON 或直接寫入 theme.js
console.log("成功轉換為 PptxGenJS 參數：", pptxConfig);/* 
輸出結果：
{
  text: 'Slide Title',
  options: { x: 0.6, y: 1.5, w: 5, h: 0.5, fontFace: 'Arial', fontSize: 24, color: '003366' }
}
*/
```

### 三、 懶人折衷法：圖層切圖匯出

如果公司的母片（Master Slide）偏向視覺裝飾型（例如有很多複雜的網格、漸層背景、特殊向量幾何圖形），透過程式碼一行行繪製 Shape 會非常痛苦。 [5, 6] 

這時建議採取半自動折衷作法：

1\. 在 Figma 中，將沒有文字的純背景裝飾、特殊圖案直接 Export 成一張高解析度的 PNG 或 SVG。
2\. 將該圖片封裝成 Base64 字串。
3\. 在 PptxGenJS 的 defineSlideMaster 物件中，直接用一整張 image 鋪滿當作底圖。
4\. 程式碼中只需要手動抓取 Figma 裡「動態文字區塊」的 x, y, w, h 位置即可。 [5, 9] 

您目前 Figma 上的設計稿，主要是文字、表格與簡單色塊居多，還是包含許多複雜的漸層、陰影或插圖呢？我可以根據您的設計複雜度給予具體的 API 欄位解析建議。

[1] [https://help.figma.com](https://help.figma.com/hc/en-us/articles/24848334599447-Export-from-Figma-Slides)
[2] [https://forum.figma.com](https://forum.figma.com/share-your-feedback-26/export-figma-to-powerpoint-google-slides-40439)
[3] [https://www.figma.com](https://www.figma.com/community/plugin/1429112411482976285/figma-to-ppt)
[4] [https://www.figma.com](https://www.figma.com/community/plugin/1578641531033845057/convert-figma-to-powerpoints-pptx-googleslides-pdfs-editable-slides-or-web-link)
[5] [https://www.figma.com](https://www.figma.com/community/plugin/1615362275036928949/figma-to-pptx)
[6] [https://www.figma.com](https://www.figma.com/community/plugin/1666939164797860020/one-click-pptx-export)
[7] [https://www.reddit.com](https://www.reddit.com/r/FigmaDesign/comments/1cjmglm/best_way_to_convert_a_figma_design_to_an_editable/)
[8] [https://www.tpisoftware.com](https://www.tpisoftware.com/tpu/articleDetails/3347)
[9] [https://deckary.com](https://deckary.com/blog/figma-to-powerpoint)

</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
如果有 PowerPoint 範本母片檔案,有什麼方式可以轉換成 pptxgenjs 的 theme.js 呢?
</td></tr><tr><td>A:</td><td>

如果是現有的 PowerPoint (.pptx) 範本檔案，同樣沒有官方一鍵轉換的工具，但相較於 Figma，從 PowerPoint 轉換成 PptxGenJS 代碼有更精準、更低成本的方法。
因為 .pptx 檔案本質上是一個 ZIP 壓縮檔，裡面封裝了標準的 XML 結構（Office Open XML）。只要解析這些 XML，就能百分之百還原裡面所有物件的精確英吋座標、字型與顏色。

以下是實務上最推薦的三種轉換方式，從「全自動程式化」到「半自動省時法」供您選擇：

### 方法一：使用 Node.js 開源套件自動解析（推薦，適合自動化流程）

在 Node.js 後端，你可以利用開源的 XML 解析套件或專門讀取 PPTX 的工具，直接抓取母片（Slide Master）中的幾何圖形與文字框參數。
常用的 Node.js 輔助套件：

* jszip + fast-xml-parser：最底層的做法。將 .pptx 解壓縮後，直接讀取 /ppt/slideMasters/ 資料夾底下的 slideMaster1.xml。裡面會以 EMUs (English Metric Units) 為單位記錄所有元件的位置（1 inch = 914,400 EMUs），換算極其精準。
* pizzip + docxtemplater：通常用於文字替換，但也可以用來遍歷投影片結構。

#### 核心轉換邏輯範例：

你可以寫一個簡單的 Node.js 轉換腳本（背後邏輯如下）：

```js
// 偽代碼：展示如何將 PPTX 的 XML 數據轉為 PptxGenJS
function convertEmuToInch(emu) {
  return Number((emu / 914400).toFixed(2));
}

// 假設從 XML 中解析出來的標題文字框數據
const pptxXmlNode = {
  x: 548640,   // EMUs
  y: 1371600,  // EMUs
  cx: 4572000, // 寬度 EMUs
  cy: 457200,  // 高度 EMUs
  color: "003366",
  font: "Microsoft JhengHei"
};

// 輸出成 PptxGenJS 的 Theme 格式
const themeConfig = {
  x: convertEmuToInch(pptxXmlNode.x),   // 0.6 英吋
  y: convertEmuToInch(pptxXmlNode.y),   // 1.5 英吋
  w: convertEmuToInch(pptxXmlNode.cx),  // 5.0 英吋
  h: convertEmuToInch(pptxXmlNode.cy),  // 0.5 英吋
  fontFace: pptxXmlNode.font,
  color: pptxXmlNode.color
};

```

### 方法二：半自動「大絕招」— 匯出成全幅底圖（開發速度最快）

如果你的 PPT 範本母片是由視覺設計師製作，裡面包含很多複雜的漸層、特殊線條、陰影、多邊形組合。千萬不要嘗試用程式碼去刻這些圖形，那會耗費極大心力且極易失真。
最聰明且業界最常用的折衷作法是：

   1. 分離動態與靜態元素：在 PowerPoint 中，把母片裡的「文字框」刪除，只留下純視覺背景（Logo、裝飾條、背景色）。
   2. 匯出高解析度圖片：將這一頁空白母片「另存新檔」為高解析度的 background.png。
   3. 線上轉 Base64：將圖片轉成 Base64 字串。
   4. 一體化寫入 Theme：在 PptxGenJS 的 theme.js 中，直接用這張圖片鋪滿整頁母片，接著只要手動手動補上文字框的相對座標即可。
```js
// theme.js 中的折衷作法
pptx.defineSlideMaster({
  title: "COMPLEX_VISUAL_LAYOUT",
  objects: [
    // 用一整張從 PPT 匯出的高解析度背景圖填滿
    { image: { x: 0, y: 0, w: "100%", h: "100%", data: "data:image/png;base64,..." } }
  ]
});

```

* 優點：100% 不跑版，開發時間從 3 天縮短到 5 分鐘。
* 缺點：生成的檔案體積會稍微變大（因為內嵌了圖片）。

### 方法三：手動對照法（使用 PPT 內建的「英吋」單位）

如果你只需要設定 1~2 個標準母片，且不打算寫複雜的 XML 解析腳本，最直接的做法是手動點擊 PowerPoint 介面，直接抄寫數值。
為了避免像素（px）轉換誤差，請先將 PowerPoint 的度量單位切換為英吋 (Inches)。

* Windows 系統：必須到 Windows 的「地區設定」->「其他設定」中，將計量系統改為「美制」。
* Mac 系統：直接在 PowerPoint 的「偏好設定」->「一般」->「度量單位」改為「英吋」。

改完後，在 PowerPoint 進入「投影片母片」檢視：

   1. 點擊標題文字框，查看「格式」面板中的高度、寬度、水平位置、垂直位置。
   2. 這四個英吋數值，完全可以直接 1:1 填入 PptxGenJS 的 x, y, w, h 中，完全不需要任何公式轉換。

### 總結：我該選哪一種？

* 如果你的 PPT 母片完全由簡單的矩形、標準文字框組成，且未來有幾十個不同的範本要處理 → 建議走方法一，寫一個腳本去讀 XML 檔案。
* 如果你的 PPT 母片有設計感、有漸層、有複雜插圖 → 強烈建議走方法二，背景直接切圖變 Base64，程式碼只負責寫動態文字與圖表。
* 如果這只是單一專案，且母片以後很少會變更 → 走方法三，花 10 分鐘人工對照英吋數值填入 theme.js 是最省省時的。

您目前手邊的 PowerPoint 範本，視覺上是屬於偏向純色塊與表格的科技簡約風，還是有許多豐富轉折、漸層與複雜圖案的設計風呢？我可以進一步提供相關的轉換建議。

</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
視覺上是屬於偏向純色塊與表格的科技簡約風
</td></tr><tr><td>A:</td><td>

### 一、 支援不同情境的母片嗎？

完全支援。 PptxGenJS 的 defineSlideMaster 可以讓你定義無限多個不同版型的母片。你只需要在 theme.js 中為每種情境命名（例如：TITLE_PAGE、AGENDA_PAGE），並在建立投影片時，指定要套用哪一個母片名稱即可。
以下是針對你提到的四種情境（標題頁、大綱頁、雙欄、標準頁），在 theme.js 中最推薦的結構化寫法：

```js
// theme.jsconst pptxgen = require("pptxgenjs");
const TECH_THEME = {
  font: "Segoe UI",
  colors: { darkBg: "0B192C", lightBg: "F9F9F9", primary: "1E3E62", textDark: "1E293B", textLight: "FFFFFF", muted: "94A3B8" }
};
function registerAllMasters(pptx) {
  
  // 情境 1：標題頁 (深色大器背景，大標置中)
  pptx.defineSlideMaster({
    title: "MASTER_TITLE_PAGE",
    background: { color: TECH_THEME.colors.darkBg },
    objects: [
      { rect: { x: 0, y: 0, w: 0.2, h: "100%", fill: { color: "00D2C4" } } } // 側邊科技亮線
    ]
  });

  // 情境 2：大綱頁 (左側固定為大綱視覺，右側留空給動態文字)
  pptx.defineSlideMaster({
    title: "MASTER_AGENDA_PAGE",
    background: { color: TECH_THEME.colors.lightBg },
    objects: [
      // 左側深色條區塊，營造目錄感
      { rect: { x: 0, y: 0, w: 3.5, h: "100%", fill: { color: TECH_THEME.colors.primary } } },
      { text: { text: "CONTENTS", options: { x: 0.5, y: 0.8, w: 2.5, h: 0.5, fontFace: TECH_THEME.font, fontSize: 24, color: TECH_THEME.colors.textLight, bold: true } } }
    ]
  });

  // 情境 3：標準頁面 (上方固定有標題列，下方為單一區塊)
  pptx.defineSlideMaster({
    title: "MASTER_STANDARD_PAGE",
    background: { color: TECH_THEME.colors.lightBg },
    objects: [
      // 頁尾宣告與自動頁碼
      { text: { text: "Standard Report Layout", options: { x: 0.6, y: 7.1, w: 5.0, h: 0.3, fontSize: 9, color: TECH_THEME.colors.muted, fontFace: TECH_THEME.font } } }
    ],
    slideNumber: { x: 12.3, y: 7.1, fontFace: TECH_THEME.font, fontSize: 9, color: TECH_THEME.colors.muted }
  });

  // 情境 4：左右雙文字欄頁面 (可在母片繪製中間的分隔虛線，或直接留白給主程式呼叫)
  pptx.defineSlideMaster({
    title: "MASTER_TWO_COLUMN_PAGE",
    background: { color: TECH_THEME.colors.lightBg },
    objects: [
      // 垂直分線 (x 在中間 6.66 英吋處)
      { line: { x: 6.66, y: 1.8, w: 0, h: 4.8, line: { color: TECH_THEME.colors.muted, width: 1, dashType: "dash" } } }
    ],
    slideNumber: { x: 12.3, y: 7.1, fontFace: TECH_THEME.font, fontSize: 9, color: TECH_THEME.colors.muted }
  });
}
// 預設各版型的物件座標字典，方便主程式呼叫（確保排版整齊）const LAYOUT_SLOTS = {
  STANDARD: { titleX: 0.6, titleY: 0.5, contentX: 0.6, contentY: 1.5, contentW: 12.1, contentH: 5.0 },
  TWO_COLUMN: { 
    titleX: 0.6, titleY: 0.5,
    col1X: 0.6, col1Y: 1.5, col1W: 5.5, col1H: 5.0,
    col2X: 7.2, col2Y: 1.5, col2W: 5.5, col2H: 5.0
  }
};

module.exports = { registerAllMasters, LAYOUT_SLOTS, TECH_THEME };
```

#### 在主程式中自由切換使用：

```js
const { registerAllMasters, LAYOUT_SLOTS } = require("./theme");
// ... 初始化 pptx 並註冊母片 ...

// 1. 建立首頁
let slideTitle = pptx.addSlide({ masterName: "MASTER_TITLE_PAGE" });
slideTitle.addText("雲端架構遷移報告", { x: 1.0, y: 3.0, fontSize: 32, color: "FFFFFF" });

// 2. 建立標準頁 (放單一圖表/文字)
let slideStd = pptx.addSlide({ masterName: "MASTER_STANDARD_PAGE" });
slideStd.addText("系統架構概述", { x: LAYOUT_SLOTS.STANDARD.titleX, y: LAYOUT_SLOTS.STANDARD.titleY, fontSize: 24, bold: true });
slideStd.addText("這裡是單一文字欄的內容區塊...", { x: LAYOUT_SLOTS.STANDARD.contentX, y: LAYOUT_SLOTS.STANDARD.contentY, w: LAYOUT_SLOTS.STANDARD.contentW, h: LAYOUT_SLOTS.STANDARD.contentH });

// 3. 建立雙欄頁面
let slide2Col = pptx.addSlide({ masterName: "MASTER_TWO_COLUMN_PAGE" });
slide2Col.addText("現況 vs 目標架構對比", { x: LAYOUT_SLOTS.TWO_COLUMN.titleX, y: LAYOUT_SLOTS.TWO_COLUMN.titleY, fontSize: 24, bold: true });
slide2Col.addText("左側：現有地端機房缺點...", { x: LAYOUT_SLOTS.TWO_COLUMN.col1X, y: LAYOUT_SLOTS.TWO_COLUMN.col1Y, w: LAYOUT_SLOTS.TWO_COLUMN.col1W, h: LAYOUT_SLOTS.TWO_COLUMN.col1H });
slide2Col.addText("右側：目標雲端架構優勢...", { x: LAYOUT_SLOTS.TWO_COLUMN.col2X, y: LAYOUT_SLOTS.TWO_COLUMN.col2Y, w: LAYOUT_SLOTS.TWO_COLUMN.col2W, h: LAYOUT_SLOTS.TWO_COLUMN.col2H });
```

### 二、 自訂具備語意化（文字意義）的 Icon 圖庫

這是一個非常棒且專業的後端工程實作思路！

在 PptxGenJS 中，你可以直接建立一個 icons.js 或在 theme.js 裡建立一個語意化物件字典。透過將圖片路徑或 Base64 編碼綁定到有意義的 Key（如 LOGO, AWS, RDS）上，主程式在調用時就不需要死記檔名或重複填寫寬高，還能順便封裝自訂的替代文字（Alternative Text / Description）以利 accessibility。

#### 1. 設計語意化圖庫字典 (icons.js)

```js
// icons.js
const path = require("path");

// 定義語意化 Icon 庫
const ICON_LIBRARY = {
  COMPANY_LOGO: {
    path: path.join(__dirname, "assets/logo.png"),
    defaultW: 1.5,
    defaultH: 0.4,
    description: "公司商標識別圖" // 封裝語意化說明
  },
  AWS_CORE: {
    path: path.join(__dirname, "assets/aws.png"),
    defaultW: 0.6,
    defaultH: 0.6,
    description: "Amazon Web Service 商標"
  },
  AWS_RDS: {
    path: path.join(__dirname, "assets/rds.png"),
    defaultW: 0.5,
    defaultH: 0.5,
    description: "AWS RDS 資料庫服務代表 Icon"
  }
};

// 封裝一個方便主程式調用的 Helper 函式
function addIcon(slide, iconKey, customOptions = {}) {
  const icon = ICON_LIBRARY[iconKey];
  if (!icon) {
    console.warn(`⚠️ 找不到關鍵字為 ${iconKey} 的 Icon`);
    return;
  }

  // 合併預設大小與使用者自訂的位置
  const finalOptions = {
    path: icon.path,
    x: customOptions.x || 1.0,
    y: customOptions.y || 1.0,
    w: customOptions.w || icon.defaultW,
    h: customOptions.h || icon.defaultH,
    // PptxGenJS 支援設定替代文字，強化物件的語意化
    desc: icon.description 
  };

  slide.addImage(finalOptions);
}

module.exports = { addIcon, ICON_LIBRARY };

```

#### 2. 主程式調用示範

有了這套語意化圖庫，主程式的程式碼會變得極度乾淨且好讀，完全不需要看見任何 .png 副檔名：

```js
const pptxgen = require("pptxgenjs");const { registerAllMasters } = require("./theme");const { addIcon } = require("./icons");
let pptx = new pptxgen();
registerAllMasters(pptx);
let slide = pptx.addSlide({ masterName: "MASTER_STANDARD_PAGE" });
slide.addText("雲端資料庫搬遷計劃", { x: 0.6, y: 0.5, fontSize: 24, bold: true });
// 呼叫語意化 Icon，只需傳入 Slide 物件、Key、以及座標位置
addIcon(slide, "AWS_CORE", { x: 2.0, y: 3.0 });
addIcon(slide, "AWS_RDS", { x: 4.5, y: 3.0 });
// 也可以視情況覆寫預設大小
addIcon(slide, "COMPANY_LOGO", { x: 11.0, y: 0.4, w: 1.8, h: 0.5 });

pptx.writeFile({ fileName: "Cloud_Report.pptx" });
```

### 總結

   1. 多情境母片：透過註冊不同的 title 字串，能完美實現標題頁、大綱頁、雙欄頁的切換。
   2. 語意化 Icon：透過封裝 addIcon 函式與 desc 屬性，你可以建立一個既好維護、又具備文字意義描述的架構圖專用圖庫。

請問在您的簡報生成系統中，這些 Icon（例如 AWS、RDS）之間是否需要繪製架構連接線（例如箭頭指引）？如果需要，我也可以補充如何在 PptxGenJS 中動態畫出帶箭頭的連接線。

</td></tr>
</table>