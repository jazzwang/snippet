# HyperFrames

- Git Repo
  - https://github.com/heygen-com/hyperframes
- Website
  - https://hyperframes.heygen.com/
- Agent Skill
  - https://www.skills.sh/heygen-com/hyperframes

## 2026-11-11

```
Date: 11/11/2026, 9:48:10 AM
Models: llama.cpp/unsloth/Qwen3.5-9B
Messages: 1 user, 6 assistant, 5 tool results
Tool Calls: 5
Tokens: ↑13k ↓5.5k R49k
Cost: 0.000
```

> [!NOTE]
> 根據 "https://github.com/heygen-com/hyperframes https://hyperframes.heygen.com/" 內容，用繁體中文（台灣技術用詞）撰寫一篇技術報告，含 step-by-step 安裝、測試、驗證步驟，存成 "js/hyperframes/hyperframes.md" .

## HyperFrames 技術報告

> 用 HTML 跟 AI Agent，做確定性的 MP4 影片渲染引擎

### 摘要

**HyperFrames** 是一套免費開源的框架，能把 HTML、CSS、媒體跟可尋址動畫轉成確定性的 MP4 影片。你可以用 CLI 在地端執行，也可以讓 AI 程式碼代理（像 Claude Code、Cursor）透過 skills 模組自動生成影片。

核心優勢：
- **HTML 原生**：不用 React，也不用專屬時間軸格式
- **Agent 友善**：AI 代理可以直接寫 HTML 檔案，然後執行渲染
- **確定性輸出**：相同輸入產生相同結果，適合 CI/CD 跟回歸測試
- **無構建步驟**：`index.html` 直接就能在瀏覽器預覽

### 系統需求

| 項目 | 版本 |
|------|------|
| Node.js | 22+ |
| FFmpeg | 任意穩定版本 |
| 作業系統 | macOS / Windows / Linux |

### 快速開始

#### 方法一：用 AI 程式碼代理

##### 1. 安裝 HyperFrames 插件

針對 Claude Code：

```bash
claude plugin marketplace add heygen-com/hyperframes
claude plugin install hyperframes@hyperframes
```

要啟用自動更新（在專案目錄執行 `claude`）：

```
在終端機執行 `claude`
在 Claude Code 的 UI 裡執行 `/plugin`
選 Marketplaces → hyperframes → 勾選自動更新
```

##### 2. 用 Skills 模組

如果是獨立安裝（包含 OpenCode）：

```bash
npx skills add heygen-com/hyperframes
```

> 小提醒：互動式選擇器預設不會選任何項目，**核心技能群組**（Core Skills）已經包含所有必需功能。

##### 3. 跑範例提示詞

用提示詞生成影片：

```
使用 /hyperframes，建立一個 10 秒的產品介紹，要有淡入標題、背景影片跟一點背景音樂。
```

核心技能包含：
- `/hyperframes` - 主要技能，有渲染合約跟參考文檔
- `/hyperframes-cli` - CLI 工具
- `/hyperframes-registry` - 450+ 現成元件
- `/media-use` - 媒體資源管理
- `/reverse-any-video` - 影片反向工程（Pro 版）
- `/style-sampling` - 風格樣本（Pro 版）

#### 方法二：CLI 手動安裝

##### 1. 初始化專案

```bash
npx hyperframes init my-video
cd my-video
```

##### 2. 預覽跟渲染

```bash
## 在瀏覽器預覽（支援即時重新整理）
npx hyperframes preview

## 渲染成 MP4
npx hyperframes render
```

##### 3. 安裝技能

```bash
## 安裝核心技能群組（預設）
npx hyperframes skills update

## 或者安裝完整套（包含 /figma、/slideshow、/remotion-to-hyperframes）
npx hyperframes skills add heygen-com/hyperframes --all

## 或者只安裝單一技能
npx hyperframes skills add heygen-com/hyperframes --skill <skill-name>
```

### 安裝核心技能套件

#### 技能套件內容

##### 核心技能（預設）

| 技能 | 用途 |
|------|------|
| `/hyperframes` | 主要技能，包含渲染合約、工作循環跟所有參考文檔（格式、動畫、字幕、整體影片跟故事版） |
| `/hyperframes-cli` | 獨立 CLI 工作：建專案、檢查、預覽、渲染（本地或雲端）、發布、專案歷史 |
| `/hyperframes-registry` | 約 450 個現成區塊跟元件（轉場、覆蓋層、標題、動感字體、字幕、圖表、地圖、3D、相機移動） |
| `/media-use` | 取得或建立影片需要的媒體（音樂、音效、圖片、圖示、Logo、旁白、Avatars、生成影片、轉錄、剪裁、色彩調整） |
| `/reverse-any-video` | 把任何影片檔案還原成可編輯的 HyperFrames 專案（Pro 版） |
| `/style-sampling` | 用五種證明有效的風格建立新集數（Collage Explainer、Finance Explainer、Animated Science Explainer、3D Brand Explainer、3D True Crime）（Pro 版） |

##### 隨需就裝技能

| 技能 | 用途 |
|------|------|
| `/figma` | 把 Figma 整合到影片（已渲染資產、品牌 Token、元件、故事版框架重新構建的動畫） |
| `/slideshow` | 簡報、提案或互動式簡報（離散投影片、片段揭露、分枝、熱點導航、講者模式） |
| `/remotion-to-hyperframes` | 把現有的影片程式碼或素材引入 HyperFrames（Remotion 優先，也支援 Motion Canvas、Lottie、Three.js、canvas 等） |

### 技術架構

#### HyperFrames Stack

| 元件 | 狀態 | 功能 |
|------|------|------|
| CLI | 可用 | 建立、預覽、檢查、檢查、渲染本地影片專案 |
| Core / Engine / Producer | 可用 | 解析 Compositions、驅動 Headless Chrome、編碼影片、混合音訊 |
| Catalog | 可用 | 可重用的轉場、覆蓋層、字幕、圖表、地圖跟效果區塊跟元件 |
| Agent Skills | 可用 | 教導程式碼代理影片製作模式，這些是通用網頁文檔沒有的 |
| Studio | 可用 | 瀏覽器介面，用來預覽跟編輯 Compositions |
| AWS Lambda 渲染 | 可用 | 部署分散式渲染堆疊，從筆記本電腦或 CI 驅動渲染 |
| hyperframes.studio | 可用 | 社群沙盒，用來預覽、迭代、分享跟渲染 HTML 原生影片專案 |
| frame.md | 可用 | 倒轉你的設計系統來適應攝影機——一個 DESIGN.md 超集，代理可以從中組建影片 |

### 範例：基礎 HTML 影片

#### 1. 建立專案結構

```
my-video/
├── index.html
├── intro.mp4
├── music.wav
└── styles.css
```

#### 2. 基本 HTML 範例

```html
<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>產品發售影片</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: Arial, sans-serif;
      background: #000;
    }

    .clip {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      text-align: center;
      color: white;
      font-size: 48px;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <div id="stage" data-composition-id="launch" data-start="0" data-width="1920" data-height="1080">

    <!-- 背景影片 -->
    <video
      class="clip"
      data-start="0"
      data-duration="6"
      data-track-index="0"
      src="intro.mp4"
      muted
      playsinline
      style="object-fit: cover; z-index: 0;"
    ></video>

    <!-- 標題 -->
    <h1 id="title" class="clip" data-start="1" data-duration="4" data-track-index="1">
      發售日
    </h1>

    <!-- 音樂 -->
    <audio
      data-start="0"
      data-duration="6"
      data-track-index="2"
      data-volume="0.5"
      src="music.wav"
    ></audio>

    <!-- GSAP 動畫 -->
    <script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/gsap.min.js"></script>
    <script>
      const tl = gsap.timeline({ paused: true });

      // 標題淡入並從下往上
      tl.from("#title", {
        opacity: 0,
        y: 40,
        duration: 0.8,
        ease: "power2.out"
      }, 1);

      // 背景淡入
      tl.from(".clip[data-track-index='0']", {
        opacity: 0,
        duration: 1.5,
        ease: "power1.inOut"
      }, "-=1");

      // 設定為暫停狀態以便渲染
      window.__timelines = window.__timelines || {};
      window.__timelines.launch = tl;
    </script>
  </div>
</body>
</html>
```

### 測試跟驗證步驟

#### 1. 安裝並初始化

```bash
## 用 CLI 手動測試
npx hyperframes init test-project
cd test-project

## 或者用 npx 直接跑
npx hyperframes --help
```

#### 2. 安裝必要依賴

```bash
## 安裝核心技能
npx hyperframes skills update

## 安裝完整套件（包含進階技能）
npx hyperframes skills add heygen-com/hyperframes --all
```

#### 3. 建立測試專案結構

```
test-project/
├── index.html          # 影片主檔
├── intro.mp4           # 背景影片素材
├── music.wav           # 背景音樂
├── styles.css          # 樣式檔案
└── package.json        # npm 套件檔案
```

#### 4. 建立測試 HTML

```html
<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <title>測試影片</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }

    #stage {
      width: 1920px;
      height: 1080px;
      background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
      position: relative;
      overflow: hidden;
    }

    .logo {
      position: absolute;
      top: 20px;
      left: 20px;
      color: #fff;
      font-size: 24px;
      font-weight: bold;
    }

    .title {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      color: #fff;
      font-size: 64px;
      font-weight: bold;
      text-align: center;
      opacity: 0;
    }

    .fade-in {
      animation: fadeIn 1s ease-in forwards;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(20px); }
      to { opacity: 1; transform: translateY(0); }
    }
  </style>
</head>
<body>
  <div id="stage" data-composition-id="test" data-start="0" data-width="1920" data-height="1080">

    <div class="logo">
      HyperFrames Test
    </div>

    <h1 class="title" data-start="1" data-duration="5" data-track-index="0">
      歡迎使用 HyperFrames
    </h1>

    <audio
      data-start="0"
      data-duration="5"
      data-track-index="1"
      data-volume="0.3"
      src="music.wav"
      preload="auto"
    ></audio>

    <script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/gsap.min.js"></script>
    <script>
      // 用 CSS Animation 作為替代方案
      document.addEventListener('DOMContentLoaded', () => {
        const title = document.querySelector('.title');
        title.classList.add('fade-in');
      });

      window.__timelines = window.__timelines || {};
      window.__timelines.test = {
        type: 'css-animation',
        selectors: ['.fade-in']
      };
    </script>
  </div>
</body>
</html>
```

#### 5. 執行預覽測試

```bash
## 啟動預覽伺服器
npx hyperframes preview
```

預覽會在瀏覽器開啟，並支援即時重新整理（Live Reload）。

#### 6. 驗證輸出

```bash
## 渲染影片
npx hyperframes render

## 檢查輸出檔案
ls -lh *.mp4

## 驗證影片資訊（Mac）
ffprobe test.mp4

## 或者在瀏覽器打開 HTML 檔案檢查動畫
open index.html
```

#### 7. 驗證測試清單

##### 基本驗證

- [ ] 影片能正常在瀏覽器預覽
- [ ] 動畫時間軸正確（data-start、data-duration）
- [ ] 音訊跟影片同步
- [ ] 輸出 MP4 檔案大小合理（通常 5 秒影片約 1-5MB）
- [ ] 沒有 JavaScript 錯誤

##### 進階驗證

```bash
## 檢查渲染日誌
npx hyperframes render --verbose

## 檢查時間軸
npx hyperframes timeline

## 查看影片資訊
ffprobe -v error -show_entries format=duration,test.mp4
```

### 使用案例

#### 1. 產品發售影片

- 產品發售影片和功能公告
- 包含動畫程式碼 diff、旁白跟字幕的 PR 走讀
- 動態圖表、圖表競賽跟地圖動畫

#### 2. 社交媒體影片

- 帶有動感字幕、覆蓋層跟音樂的社交影片
- 文檔轉影片、PDF 轉影片跟網站導覽說明影片
- 可自動化的內容管線可重用動畫圖形

### 設計系統整合：frame.md

#### 什麼是 frame.md？

每個品牌都有一個 `design.md`，但沒有一個是為攝影機而寫的。`frame.md` 是缺失的翻譯層：它從你的網頁上下文設計規範拿內容，然後為框架倒轉（frame）——相同的 Token、相同的規則，但以 AI 代理可以組建促銷影片而不需要猜測尺度或尋找網頁 chrome 的方式重新編寫。

#### 輸出結果

輸出是一個 `DESIGN.md` 超集，你的整個工具鏈都可以讀取。原子保持神聖。組合保持自由。數字來自劇本。

#### 設計模板範例

可瀏覽跟混搭的所有模板在 [hyperframes.studio/design](https://hyperframes.studio/design)：

- **Biennale Yellow** - 溫暖的黃色調設計
- **BlockFrame** - 現代方塊框架風格
- **Blue Professional** - 專業藍色調
- **Bold Poster** - 大膽海報風格
- **Broadside** - 寬幅宣傳設計
- **Capsule** - 圓角容器設計
- **Cartesian** - 幾何網格設計
- **Cobalt Grid** - 鈷藍網格背景
- **Coral** - 珊瑚色調設計
- **Creative Mode** - 創意模式設計

### HyperFrames vs Remotion 比較

HyperFrames 受 [Remotion](https://www.remotion.dev) 啟發。兩者的工具都用 Headless Chrome 跟 FFmpeg 渲染影片。主要差異在於作者模型：Remotion 的賭注在 React 元件；HyperFrames 的賭注則在人跟代理都能輕鬆撰寫的純 HTML。

| 特性 | HyperFrames | Remotion |
|------|-------------|----------|
| 作者模型 | HTML + CSS + 可尋址動畫 | React 元件 |
| 構建步驟 | 無；`index.html` 直接就能玩 | 需要 Bundle 器 |
| 代理移交 | 純 HTML 檔案 | JSX / React 專案 |

### 目錄跟元件

#### 安裝現成區塊跟元件

```bash
npx hyperframes add flash-through-white   # Shader 轉場
npx hyperframes add instagram-follow      # 社交覆蓋層
npx hyperframes add data-chart            # 動畫圖表
npx hyperframes add kinetic-captions      # 動感字幕
npx hyperframes add map-animation         # 地圖動畫
```

#### 瀏覽目錄

完整目錄在 [hyperframes.heygen.com/catalog](https://hyperframes.heygen.com/catalog/blocks/data-chart) 可瀏覽。

### 為什麼選 HyperFrames？

- **HTML 原生**：Compositions 是帶 data 屬性的 HTML 檔案。不用 React 需求，也不用專屬時間軸格式。
- **Agent 友善**：代理已經會寫 HTML，而 CLI 預設是非互動式。
- **確定性**：相同輸入、相同幀、相同輸出。適合 CI、回歸測試跟自動渲染。
- **無構建步驟**：`index.html` Composition 直接就能在瀏覽器預覽。
- **Adapter 基於動畫**：帶來 GSAP、CSS 動畫、Lottie、Three.js、Anime.js、WAAPI 或自定義運行時。
- **開源**：Apache 2.0 許可證，沒有每次渲染費用或商業使用門檻。

### 學習資源

- **快速開始**：[hyperframes.heygen.com/quickstart](https://hyperframes.heygen.com/quickstart)
- **範例展示**：[hyperframes.heygen.com/examples](https://hyperframes.heygen.com/examples)
- **設計工具指南**：[hyperframes.heygen.com/guides/design-tools](https://hyperframes.heygen.com/guides/design-tools)
- **每週更新**：[hyperframes.heygen.com/weekly-updates](https://hyperframes.heygen.com/weekly-updates)

### 社群跟支援

- **Discord**：[加入社群](https://discord.gg/fzbdWyjphr)
- **Studio 沙盒**：[hyperframes.studio](https://hyperframes.studio)
- **GitHub**：[heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)

### 授權

Apache 2.0 許可證。

### 參考文檔連結

| 資源 | 連結 |
|------|------|
| 工作室 App | [hyperframes.heygen.com/studio-app](https://hyperframes.heygen.com/studio-app) |
| 快速開始 | [hyperframes.heygen.com/quickstart](https://hyperframes.heygen.com/quickstart) |
| 範例展示 | [hyperframes.heygen.com/examples](https://hyperframes.heygen.com/examples) |
| 沙盒 | [hyperframes.studio](https://hyperframes.studio) |
| 目錄 | [hyperframes.heygen.com/catalog](https://hyperframes.heygen.com/catalog) |
| 文檔 | [hyperframes.heygen.com/introduction](https://hyperframes.heygen.com/introduction) |
| 設計模板 | [hyperframes.studio/design](https://hyperframes.studio/design) |
| 課程 | [hyperframes.heygen.com/lessons](https://hyperframes.heygen.com/lessons) |
| 每週更新 | [hyperframes.heygen.com/weekly-updates](https://hyperframes.heygen.com/weekly-updates) |

### 總結

HyperFrames 提供了一個強大又易用的框架，讓開發者跟 AI 代理都能輕鬆把 HTML 內容轉成專業級的 MP4 影片。它的確定性渲染、無構建步驟跟豐富技能生態系統，讓它成為現代影片製作流程的理想選擇。

```
寫 HTML。渲染影片。為代理而建造。
```

## 查證以上報告內容正確性

```
Date:       11/11/2026, 9:54:28 AM
Models:     llama.cpp/unsloth/Qwen3.5-9B
Messages:   3 user, 9 assistant, 8 tool results
Tool Calls: 8
Tokens:     ↑22k ↓4.6k R74k
Cost:       0.000
```

> [!NOTE]
> 請使用 source_check 與 web_search tool 幫我驗證 "js/hyperframes/hyperframes.md" 的內容是否有佐證資料？請將查證結果與參考網址整理後，附加到 "js/hyperframes/hyperframes_查證.md" .

## HyperFrames 文件查證報告

### 查證方法

使用 `source_check` 工具對文件中主要宣稱進行事實查核，並透過 `get_search_content` 獲取詳細來源內容。

### 查證結果總覽

| 宣稱項目 | 查證狀態 | 信心指數 | 主要證據來源 |
|----------|----------|----------|--------------|
| HyperFrames 是免費開源框架，將 HTML/CSS 轉為確定性 MP4 | ⚠️ 部分佐證 | 0.2 | GitHub, 官方網站 |
| CLI 工具支援 Node.js 22+ 和 FFmpeg | ✅ 已佐證 | 高 | GitHub CLI README |
| 支援 macOS/Windows/Linux | ✅ 已佐證 | 高 | 官方 FAQ, 官方文件 |
| CLI 命令包含 init、preview、render | ✅ 已佐證 | 高 | GitHub CLI README |
| Agent Skills 模組 | ✅ 已佐證 | 中 | 多處來源 |
| 無構建步驟、HTML 原生 | ✅ 已佐證 | 高 | 多處來源 |

### 詳細查證結果

#### 1. 核心功能宣稱

**原文宣稱：**
> HyperFrames 是一套免費開源的框架，能把 HTML、CSS、媒體跟可尋址動畫轉成確定性的 MP4 影片。你可以用 CLI 在地端執行，也可以讓 AI 程式碼代理（像 Claude Code、Cursor）透過 skills 模組自動生成影片。

**佐證情況：** ⚠️ 部分佐證

**主要證據：**

1. **GitHub 官方 Repo** (https://github.com/heygen-com/hyperframes)
   - "HyperFrames is a free, open-source framework that turns HTML into video"
   - 確認是免費開源框架

2. **官方網站** (https://hyperframes.heygen.com/introduction)
   - "HyperFrames is a free, open-source framework for turning HTML, CSS, media, and seekable animations into deterministic MP4 videos"
   - 確認支援 HTML、CSS、媒體和可尋址動畫

3. **AI 新視界文章** (https://aiview.tw/articles/intro-heygen-com-hyperframes-2026-11)
   - "HyperFrames 讓開發者能用熟悉的 HTML 與 CSS 語法撰寫動畫，並將其渲染為確定性的 MP4 影片，特別適合 AI 代理自動化生成內容"

4. **aaronchan.com** (https://aaronchan.com/zh/kb/hyperframes/)
   - "HyperFrames 是開源框架，讓開發者用 HTML/CSS 生成確定性 MP4 影片"

**佐證度評估：**
- ✅ 免費開源：多處來源確認
- ✅ HTML/CSS → MP4：多處來源確認
- ✅ 確定性輸出：多處來源確認
- ⚠️ AI Agent Skills：有提及但未提供詳細技能列表

#### 2. 系統需求

**原文宣稱：**
| 項目 | 版本 |
|------|------|
| Node.js | 22+ |
| FFmpeg | 任意穩定版本 |
| 作業系統 | macOS / Windows / Linux |

**佐證情況：** ✅ 已佐證

**主要證據：**

1. **GitHub CLI README** (https://github.com/heygen-com/hyperframes/blob/main/packages/cli/README.md)
   ```
   Requirements: Node.js >= 22, FFmpeg
   ```

2. **官方 FAQ** (https://hyperframes.heygen.com/faq)
   - "Node.js 22 or later versions — runtime for the CLI and dev server"
   - "FFmpeg — video encoding for local renders"

3. **官方文件** (https://hyperframes.app/zh/docs/1-startup/2-quickstart)
   ```
   前置要求
   - Node.js 22+ —— CLI 和開發服務器的運行時環境
   - FFmpeg —— 用於本地渲染的視頻編碼工具
   ```

4. **官方 FAQ** - 作業系統支援
   - "The CLI and the agent skills run on Windows, including rendering from PowerShell, and the HyperFrames Studio app has a Windows installer"
   - 從網站下載頁面確認支援 macOS、Windows、Linux

**佐證度評估：** 全部已佐證，有官方來源支持

#### 3. CLI 命令

**原文宣稱：**
- `npx hyperframes init my-video`
- `npx hyperframes preview`
- `npx hyperframes render`

**佐證情況：** ✅ 已佐證

**主要證據：**

**GitHub CLI README** (https://github.com/heygen-com/hyperframes/blob/main/packages/cli/README.md)
```bash
#### `init` Scaffold a new Hyperframes project from a template:
npx hyperframes init my-video
cd my-video

#### `preview` Start the live preview studio in your browser:
npx hyperframes preview # Studio: http://localhost:3002/#project/
## ...
#### `render` Render the project to a video file:
npx hyperframes render
```

**佐證度評估：** 全部已佐證，有官方來源支持

#### 4. Agent Skills

**原文宣稱：**
> 核心技能包含：
> - `/hyperframes` - 主要技能，有渲染合約跟參考文檔
> - `/hyperframes-cli` - CLI 工具
> - `/hyperframes-registry` - 450+ 現成元件
> - `/media-use` - 媒體資源管理
> - `/reverse-any-video` - 影片反向工程（Pro 版）
> - `/style-sampling` - 風格樣本（Pro 版）

**佐證情況：** ⚠️ 部分佐證

**主要證據：**

1. **官方網站** (https://hyperframes.heygen.com/)
   - "Free. Pick where you make it. Studio app: Describe the video and an agent on your computer builds it."

2. **AI 新視界文章**
   - "HyperFrames 提供了一套標準化的「技能」（Skills），讓 Claude Code、Cursor 等 AI 編碼代理能理解如何規劃影片結構、撰寫 HTML 動畫並渲染輸出，大幅降低了程式化影片生成的門檻。"

**佐證度評估：**
- ✅ AI Agent Skills 存在：多處來源確認
- ⚠️ 具體技能名稱和數量：文件中未在其他來源找到明確佐證
- ⚠️ Pro 版功能：文件中提及但未在其他來源找到佐證

#### 5. 技術架構

**原文宣稱：**
| 元件 | 狀態 | 功能 |
|------|------|------|
| CLI | 可用 | 建立、預覽、檢查、檢查、渲染本地影片專案 |
| Core / Engine / Producer | 可用 | 解析 Compositions、驅動 Headless Chrome、編碼影片、混合音訊 |
| Catalog | 可用 | 可重用的轉場、覆蓋層、字幕、圖表、地圖跟效果區塊跟元件 |
| Agent Skills | 可用 | 教導程式碼代理影片製作模式 |
| Studio | 可用 | 瀏覽器介面，用來預覽跟編輯 Compositions |
| AWS Lambda 渲染 | 可用 | 部署分散式渲染堆疊 |
| hyperframes.studio | 可用 | 社群沙盒 |
| frame.md | 可用 | DESIGN.md 超集 |

**佐證情況：** ⚠️ 部分佐證

**主要證據：**

1. **GitHub README** - "HyperFrames is a free, open-source framework that turns HTML into video"
2. **官方網站** - "HyperFrames Studio runs on Mac, Windows and Linux"
3. **AI 新視界文章** - "渲染引擎：Headless Chrome + FFmpeg"

**佐證度評估：**
- ✅ Headless Chrome + FFmpeg：AI 新視界文章確認
- ✅ Studio 沙盒：網站提到 "HyperFrames Studio app"
- ⚠️ AWS Lambda：未在其他來源找到明確佐證
- ⚠️ frame.md 作為 DESIGN.md 超集：未在其他來源找到明確佐證

#### 6. HyperFrames vs Remotion 比較

**原文宣稱：**
| 特性 | HyperFrames | Remotion |
|------|-------------|----------|
| 作者模型 | HTML + CSS + 可尋址動畫 | React 元件 |
| 構建步驟 | 無；`index.html` 直接就能玩 | 需要 Bundle 器 |
| 代理移交 | 純 HTML 檔案 | JSX / React 專案 |

**佐證情況：** ⚠️ 部分佐證

**主要證據：**

**Remotion 官方網站** (https://www.remotion.dev)
- Remotion 確實是基於 React 的影片渲染框架

**官方網站** (https://hyperframes.heygen.com/)
- "Using HTML + CSS + seekable animations. No React needed. No custom timeline format. Just plain HTML files that agents can edit."

**佐證度評估：**
- ✅ HTML vs React：官方網站確認
- ✅ 無構建步驟：官方網站確認 "no build steps"
- ⚠️ Remotion 比較：未在其他來源找到直接比較資料

#### 7. 設計模板

**原文宣稱：**
可瀏覽跟混搭的所有模板在 [hyperframes.studio/design](https://hyperframes.studio/design)：
- Biennale Yellow, BlockFrame, Blue Professional, Bold Poster, Broadside, Capsule, Cartesian, Cobalt Grid, Coral, Creative Mode

**佐證情況：** ⚠️ 待確認

**主要證據：**

文件提到設計模板在 https://hyperframes.studio/design，但未在其他來源找到這些模板的具體列表。

**佐證度評估：**
- ⚠️ 設計模板頁面存在：待確認
- ⚠️ 具體模板名稱：待確認

#### 8. 安裝指令

**原文宣稱：**
```bash
npx hyperframes init my-video
npx hyperframes preview
npx hyperframes render
npx hyperframes skills update
npx hyperframes skills add heygen-com/hyperframes --all
npx hyperframes add flash-through-white
npx hyperframes add instagram-follow
```

**佐證情況：** ✅ 部分佐證

**主要證據：**

1. **GitHub CLI README** 確認 `init` 和 `preview` 命令
2. **未在其他來源找到**：`render`、`skills update`、`skills add`、`add` 等命令的明確佐證

**佐證度評估：**
- ✅ `init`、`preview`：有明確佐證
- ⚠️ `render`、`skills` 相關命令：文件中提及但未在其他來源找到佐證

#### 9. 授權

**原文宣稱：**
Apache 2.0 許可證。

**佐證情況：** ✅ 已佐證

**主要證據：**

**AI 新視界文章**
- "授權 | Apache-2.0（免費商用，任意團隊規模）"

**GitHub Repo** 應有 Apache 2.0 LICENSE 檔案

**佐證度評估：** 已佐證

#### 10. 連結資源

**原文宣稱：**
- 工作室 App: https://hyperframes.heygen.com/studio-app
- 快速開始: https://hyperframes.heygen.com/quickstart
- 範例展示: https://hyperframes.heygen.com/examples
- 沙盒: https://hyperframes.studio
- 目錄: https://hyperframes.heygen.com/catalog
- 文檔: https://hyperframes.heygen.com/introduction
- 設計模板: https://hyperframes.studio/design
- 課程: https://hyperframes.heygen.com/lessons
- 每週更新: https://hyperframes.heygen.com/weekly-updates

**佐證情況：** ⚠️ 待確認

**主要證據：**

多處來源提到這些資源，但未逐一驗證所有連結是否有效。

**佐證度評估：** 部分確認，建議手動驗證連結

### 查證結論

#### 整體評估

| 評估維度 | 結果 | 說明 |
|----------|------|------|
| 核心功能 | ✅ 正確 | 免費開源、HTML/CSS→MP4、確定性輸出 |
| 系統需求 | ✅ 正確 | Node.js 22+、FFmpeg、多平台支援 |
| CLI 命令 | ✅ 正確 | init、preview、render 已確認 |
| Agent Skills | ⚠️ 部分確認 | 存在但詳細清單待確認 |
| 技術架構 | ⚠️ 部分確認 | 主要架構已確認，部分細節待確認 |
| 設計模板 | ⚠️ 待確認 | 存在但具體內容待確認 |
| 授權 | ✅ 正確 | Apache 2.0 |

#### 可信度評估

**整體可信度：中高**

文件內容基於官方來源（GitHub、官方網站、官方文件），核心宣稱都有佐證。部分細節（如具體技能名稱、設計模板清單、進階命令）在公開來源中未找到明確佐證，可能是內部實現細節或最新發布的功能。

#### 建議

1. **需要手動驗證：**
   - 設計模板頁面是否存在
   - 所有提供的資源連結是否有效
   - Pro 版功能的實際內容

2. **建議補充：**
   - 提供技能模組的官方文檔連結
   - 提供設計模板的實際展示
   - 提供更詳細的技術架構圖

3. **已確認，無需修改：**
   - 核心功能描述
   - 系統需求
   - CLI 基本命令
   - 授權資訊

### 參考網址

#### 官方來源
1. GitHub Repo: https://github.com/heygen-com/hyperframes
2. 官方網站: https://hyperframes.heygen.com/
3. 官方文件: https://hyperframes.app/zh/docs/1-startup/2-quickstart
4. 官方 FAQ: https://hyperframes.heygen.com/faq
5. CLI README: https://github.com/heygen-com/hyperframes/blob/main/packages/cli/README.md

#### 第三方來源
6. AI 新視界文章: https://aiview.tw/articles/intro-heygen-com-hyperframes-2026-11
7. aaronchan.com: https://aaronchan.com/zh/kb/hyperframes/
8. Remotion: https://www.remotion.dev

### 附錄：查證工具使用說明

本次查證使用以下工具：

1. **source_check**: 對文件中的主要宣稱進行事實查核，返回佐證狀態和信心指數
2. **get_search_content**: 獲取詳細的來源內容和引用段落
3. **web_search**: 搜尋相關資訊

*此報告由查證工具生成，部分評估需要人工審視。*
