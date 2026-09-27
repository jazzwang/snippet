# Blume

- Git Repo
  - https://github.com/haydenbleasel/blume
- Website
  - https://useblume.dev/
  - Introduction - https://useblume.dev/docs
  - Quick Start - https://useblume.dev/docs/quickstart

## 2026-09-19

- Learn from InfoQ newsletter
  - 2026-09-05
  - Blume: Zero-Config Docs Framework That Turns a Markdown Folder into an AI-Ready Website
    - https://www.infoq.com/news/2026/09/blume-docs-ai/

## 2026-09-27

> [!QUESTION]
> /skill:understand given https://github.com/haydenbleasel/blume 可以告訴我 Blume 的技術創新為何？跟其他程式框架的差異為何？使用的限制與需求為何？

## Blume 技術分析報告

**Blume**（由 Hayden Bleasel 開發）是一個專為現代軟體專案設計的**開源、零配置（Zero-Config）文件網站生成框架**。它結合了 Astro 和 Vite 的高效能引擎，旨在解決現有文件工具在「易用性」與「自訂彈性」之間的極端衝突。

---

### 一、 Blume 的技術創新

1. **隱藏式 Astro 運行時（Hidden Astro Runtime）**
   Blume 引入了「**內容與程式碼完全分離**」的架構。當您在專案中建立 `docs/` 資料夾並放入 Markdown/MDX 後，Blume 的 CLI 會在幕後自動生成並驅動一個隱藏在 `.blume/` 目錄下的 Astro 專案。這意謂著使用者在寫文件時，**專案庫中完全不需要包含任何前端框架的樣板程式碼（Boilerplate）**，維持代碼庫極致乾淨。

2. **無縫退出機制（Eject Escape Hatch）**
   這是一個強大的架構創新。當文件專案規模擴大、需要高度客製化時，使用者可以執行 `blume eject`。此指令會**將隱藏的 `.blume/` 運行時「釋放（Promote）」出來，變成一個標準的、獨立的 Astro 專案**。這時使用者可以直接掌控所有的 Astro 設定檔、路由和樣式，而 `blume` 軟體包則轉為一般套件導入，保留原有的元件與 MDX 渲染能力。

3. **AI Ready / 智能代理技能（Agent Skills）**
   Blume 深度整合了現代 AI 輔助開發的趨勢。它內建並分發了針對 AI Agent（如 Cursor、Claude Code 等）的「Agent Skills」（放置在專案的 `skills/` 中，例如 `blume-migrate` 技能）。這能指導 AI 讀取現有其他框架（如 Mintlify、Docusaurus）的文件並自動重構、翻譯為 Blume 的格式。

4. **自動化 SEO、AEO（AI 搜尋引擎最佳化）與 Open Graph 生成**
   在背後，Blume 會根據文件結構和標題自動配置完美的 SEO 標籤，並為每一頁自動渲染專屬的 Open Graph 分享圖片，大幅減少行銷與分享文件的成本。

---

### 二、 與其他文件框架的差異

目前主流的文件工具大多落在以下兩個極端，而 Blume 走的是**第三條路**：

| 特性 | 託管型平台 (如 Mintlify) | 傳統開源框架/模板 (如 Docusaurus, Nextra, Fumadocs) | **Blume** |
| :--- | :--- | :--- | :--- |
| **程式碼體積** | 無需維護代碼，全在線上系統撰寫。 | 給你一整個 React/Next.js/Astro 專案，你必須在本地維護它。 | **本地零配置。所有代碼隱藏在 `.blume/`，專案內只有 Markdown。** |
| **部署彈性** | 強制綁定在其託管服務，有廠商鎖定（Vendor Lock-in）風險。 | 完全自由，可部署到任何靜態網站主機。 | **完全自由。預設打包為靜態網站，可部署至任何主機。** |
| **自訂極限** | 難以深度客製化（受限於平台提供的 API）。 | 自由度極高，但需要前端開發背景去修改樣板。 | **平時是零配置，一旦需要深度自訂可一鍵 `blume eject` 轉為 Astro 專案。** |
| **檔案結構** | 通常需要手動維護一個龐大的導覽手冊（Manifest JSON）。 | 通常需要手動設定 sidebars.js 或複雜的 config。 | **完全基於檔案系統（Filesystem-derived）自動生成導覽。** |

---

### 三、 使用的限制與需求

儘管 Blume 具有前瞻性，但在使用時也存在一些技術限制與特定需求：

1. **環境與相依需求**
   * **Node.js 版本需求**：必須使用 **Node.js 22.12 或更高版本**。
   * **資料夾結構限制**：預設專案根目錄必須包含一個 `docs/` 資料夾（或透過 `blume.config.ts` 設定 `content.root`），且其中必須至少包含一個 `.md` 或 `.mdx` 檔案才能順利啟動。

2. **`eject`（退出）是單向操作（One-Way Trip）**
   * 執行 `blume eject` 後，項目會被永久轉換為一個標準的 Astro 應用。你**無法簡單地將其「恢復」**回原本那種乾淨、完全隱藏運行時的 `blume dev` 模式（儘管舊有的 Markdown 和元件依然能正常工作）。

3. **API 測試沙盒（OpenAPI Playground）的 CORS 限制**
   * 如果你在文件中整合了 OpenAPI / AsyncAPI 並啟用 Playground 測試，瀏覽器會直接發送請求到目標 API，這要求目標 API **必須支援 CORS**（`Access-Control-Allow-Origin`）。
   * 如果目標 API 不支援 CORS，你必須開啟內建的反向代理（`playground.proxy: true`），這會強迫你的 Blume 專案必須以 **Server-Side Rendering（SSR）** 模式運行（即 `deployment.output: "server"`），從而**無法再使用一般的純靜態虛擬主機（Static Hosting）**進行部署，必須部署在 Vercel、Netlify 或 Node 伺服器等支援 Server 運行的地方。

4. **翻譯與多國語系限制**
   * Blume 提供了本地翻譯功能，但 Meta 標題的自動翻譯僅支援「目錄解析器（Dir-parser）」，「點號解析器（Dot-parser）」不支援此機制。
   * **無法翻譯外部內容**：如果你的文件來源是遠端（Remote）或是 CMS 系統，Blume 無法對其進行自動翻譯，因為本地沒有對應的實體文件可以寫入。

---

### 結論

Blume 的核心創新在於其**「漸進式披露（Progressive Disclosure）」**的設計哲學——平時讓非前端人員（如 Technical Writers、產品經理）能像用 Mintlify 一樣無痛撰寫 Markdown，但在需要客製化時，又能透過 `eject` 提供與 Docusaurus/Astro 同等的無限制開發體驗。
