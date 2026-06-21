# Figma MCP

[TOC]

## 2026-06-15

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI Mode
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
are there tool to read Figma flow and convert the UI Mock design to data model and API?
</td></tr><tr><td>A:</td><td>

## Figma to Data Model and API

Yes, there are several specialized AI tools and workflow approaches designed exactly for this. While traditional tools focus strictly on converting Figma into frontend code (like React or HTML), modern AI-driven tools can read UI components, form inputs, and repetition logic to auto-generate data models, backend JSON schemas, and API contracts. [1, 2, 3, 4, 5]
These tools and workflows are categorized below by how they handle the conversion:

### 1. Direct Figma Plugins (Automated Data Extraction) [6, 7]

These tools run natively inside Figma to turn your visual designs into backend structures with one click. [1, 8, 9, 10]

-   [Genota AI](https://www.figma.com/community/plugin/1589196566404780018/genota-ai-sql-database-generator): Specifically built to analyze your visual frames, automatically detect tables, columns, and entity relationships, and instantly generate production-ready SQL database schemas (PostgreSQL, MySQL, SQLite) and interactive ERD diagrams. [11]
-   [Zeus Data](https://www.figma.com/community/plugin/1582437601081431642/zeus-data-design-to-data-with-1-click): Automatically extracts deep, structured JSON data schemas from UI mockups. It detects repeated design groups (like cards or lists) and groups them into arrays, allowing you to instantly create API contracts and database structures from visual elements. [1]
-   [Figma Raw](https://www.figma.com/community/plugin/1491678546144854232/figma-raw-export-design-data-for-ai-llm-agents): Strips out the styling junk and exports raw semantic layout data into clean, structured JSON. You feed this JSON into any AI model to dictate your backend API structure. [12, 13, 14]

### 2. Full-Stack Prototyping Tools (App-Builders) [15]

If you want to map your visual user flows directly to an API logic layer, look into full-stack AI platform plugins.

-   Builder.io Visual Copilot / Fusion: Takes multi-frame Figma user flows, builds functional navigation, and maps visual screens to real data lookups. You can prompt it using natural language to bind the generated forms and UI elements to live API endpoints or databases. [16, 17]

### 3. AI IDE Integration via MCP (Model Context Protocol) [18]

The most flexible workflow is to pull the Figma flow straight into your coding environment (like Cursor or Claude Desktop) using Figma's Model Context Protocol (MCP). [18, 19]

-   Figma Context MCP / Framelink MCP: These act as a universal bridge. By pasting a Figma frame or flow link into an AI-powered editor, the AI uses Figma's REST API to ingest the exact design metadata. [20, 21, 22]
-   The Workflow: You can prompt the AI agent inside your IDE: *"Analyze this Figma user profile flow link and write the Prisma data model, PostgreSQL schema, and Express.js REST API routes required to handle these forms."* [23]

### Recommendation on How to Proceed

If you want a quick database/API design, start with the Genota AI or Zeus Data plugins directly inside your canvas. If you are looking to build a fully connected full-stack application, connect your Figma project to Cursor or Claude via an MCP server. [1, 11, 18, 19]
To help tailor this, what backend stack or database (e.g., Node.js, Python, PostgreSQL, MongoDB) are you hoping to generate, and how complex is your user flow?

[1] [https://www.figma.com](https://www.figma.com/community/plugin/1582437601081431642/zeus-data-design-to-data-with-1-click)
[2] [https://www.aidesigner.ai](https://www.aidesigner.ai/blog/figma-to-code-tools)
[3] [https://javascript.plainenglish.io](https://javascript.plainenglish.io/ai-frontend-workflows-in-2025-fa16dc9c5244)
[4] [https://www.rocket.new](https://www.rocket.new/blog/best-figma-to-code-ai-tools)
[5] [https://www.reddit.com](https://www.reddit.com/r/FigmaDesign/comments/1oiyn3e/is_there_really_anything_that_can_turn_my_figma/)
[6] [https://www.lucaburgio.com](https://www.lucaburgio.com/insight/how-we-boosted-our-design-process.html)
[7] [https://www.onething.design](https://www.onething.design/post/best-ai-plugins-for-figma-designers)
[8] [https://sleek.design](https://sleek.design/alternatives/figma-ai-ux-pilot)
[9] [https://www.youtube.com](https://www.youtube.com/watch?v=a5LjVDRd47U)
[10] [https://www.builder.io](https://www.builder.io/blog/convert-figma-to-react-native)
[11] [https://www.figma.com](https://www.figma.com/community/plugin/1589196566404780018/genota-ai-sql-database-generator)
[12] [https://www.figma.com](https://www.figma.com/community/plugin/1491678546144854232/figma-raw-export-design-data-for-ai-llm-agents)
[13] [https://www.figma.com](https://www.figma.com/community/plugin/1491678546144854232/figma-raw-export-design-data-for-ai-llm-agents)
[14] [https://yannglt.com](https://yannglt.com/writing/introducing-framer-figma-sync)
[15] [https://codeconductor.ai](https://codeconductor.ai/blog/figma-make-alterantive/)
[16] [https://www.youtube.com](https://www.youtube.com/watch?v=uctbmzmmCj4)
[17] [https://www.figma.com](https://www.figma.com/community/plugin/747985167520967365/builder-io-figma-to-code-ai-apps-react-vue-tailwind-etc)
[18] [https://www.youtube.com](https://www.youtube.com/watch?v=X-aX1TuGP0s)
[19] [https://www.youtube.com](https://www.youtube.com/watch?v=T_YSzAKPC4U&t=190)
[20] [https://github.com](https://github.com/glips/figma-context-mcp)
[21] [https://dev.to](https://dev.to/crosspostr/comparison-of-the-best-figma-to-code-ai-tools-42fl)
[22] [https://www.emergentmind.com](https://www.emergentmind.com/topics/figma-api-data-extraction)
[23] [https://www.youtube.com](https://www.youtube.com/watch?v=X-aX1TuGP0s)

</td></tr>
</table>

## 2026-06-18

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI Mode
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
Figma 要使用 MCP Server 有 License 限制嗎?
</td></tr><tr><td>A:</td><td>

## Figma License limitation when using MCP Server

是的，Figma 的官方 MCP Server 在帳號授權（License）與方案上有非常嚴格的限制。 [1, 2]
如果你想讓 AI 透過 MCP 穩定讀取設計稿，主要會受到付費方案、席位（Seat）類型以及使用額度（AI Credits）的三重限制： [3, 4]

### 1. 方案限制：免費版幾乎無法實用

-   免費版（Starter Plan）：雖然官方的遠端（Remote）伺服器允許免費版帳號設定，但有極其嚴格的額度限制。免費版每月僅有 6 次 MCP 工具呼叫（Tool Calls）。對開發者來說，AI 讀兩三次設計稿額度就會完全用盡，因此免費版在實際開發中基本無法使用。 [4, 5, 6]
-   付費方案：必須是 Professional（專業版）、Organization（組織版） 或 Enterprise（企業版） 才能解鎖正常的 MCP Server 功能。 [2, 3]

### 2. 席位限制（Seat Tiers）

即便升級到付費方案，你的 Figma 帳號也必須具備對應的開發權限：

-   桌面版伺服器（Desktop Server）：如果想要使用本機 Desktop 運行的 MCP，你的帳號必須是付費方案中的 Full Seat（完整設計席位） 或 Dev Seat（開發者席位）。
-   如果你只是被拉進專案的免費觀看者（Viewer），將無法正常啟用官方的 Dev Mode MCP 服務。 [3, 6]

### 3. AI 額度限制（AI Credits）

Figma 將 MCP 的讀取呼叫綁定了其平台的 AI 點數： [4]

-   Professional 方案：每天約有 200 次的 MCP 工具呼叫額度（或依帳號包含的 3,000 AI credits/月進行扣抵）。
-   更高階方案：支援管理員統一採購 AI 訂閱或按量付費（Pay-as-you-go）來擴充點數。 [4, 5, 7]


### 4. 💡 沒預算？不想付錢的「繞道替代方案」

如果你只是個人開發者或不想為了 API 串接去訂閱 Figma 的付費 Dev Mode 方案，可以使用以下替代管道： [8]

1.  使用社群開源 MCP Server（例如 Figma Context MCP）：
    不走官方的 Dev Mode 管道，而是使用社群開發的開源 MCP 專案。你只需要在 Figma 的帳號設定裡免費建立一個 Personal Access Token (PAT)，並將其寫入 Cursor 或 Claude 的 `mcp.json` 設定檔中。這種方式走的是傳統 REST API，雖然偶爾會受到 API 頻率限制（Rate Limit），但完全不限次數且免費。 [1, 2, 6, 8, 9, 10, 11]
2.  複製 JSON 餵給 AI：
    利用免費的 Figma 插件（如前文提到的 *Figma Raw*），手動把設計稿的語義 JSON 數據複製出來，直接貼進 Cursor/Claude 聊天視窗中。雖然少了一步自動化的連線，但效果跟 MCP 讀取出來的結構相差無幾，也是完全免費的作法。 [12, 13]

你是打算在公司的企業團隊環境中使用，還是個人研究/獨立開發呢？如果是後者，建議直接下載開源的 `figma-context-mcp` 來設定即可！ [8]

[1] [https://developers.figma.com](https://developers.figma.com/docs/figma-mcp-server/rate-limits-access/)
[2] [https://skywork.ai](https://skywork.ai/skypage/zh-hant/mcp-figma-MCP-Server-%E6%B7%B1%E5%BA%A6%E8%A7%A3%E6%9E%90%EF%BC%9AAI%E5%B7%A5%E7%A8%8B%E5%B8%AB%E7%9A%84%E5%8D%94%E4%BD%9C%E5%88%A9%E5%99%A8/1972516569614446592)
[3] [https://help.figma.com](https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Figma-MCP-server)
[4] [https://rar.design](https://rar.design/posts/figma-ai-guide)
[5] [https://www.threads.com](https://www.threads.com/@jkrollingcc/post/DUwg0D9CCrs/%E5%81%9A%E5%89%8D%E7%AB%AF%E8%B6%85%E9%9B%A3%E7%9A%84%E5%88%B0%E5%BA%95%E6%98%AF%E8%AA%B0%E8%AA%AA-figma-%E6%9C%83%E8%A2%AB%E5%8F%96%E4%BB%A3%E7%9A%84%E5%85%8D%E8%B2%BB%E7%89%88%E6%9C%AC%E4%B8%80%E5%80%8B%E6%9C%88%E5%8F%AA%E6%9C%89-6-%E6%AC%A1-mcp-call-%E4%BD%86%E6%98%AFpro-%E4%B8%80%E5%A4%A9%E5%B0%B1%E6%9C%89-200-%E6%AC%A1-mcp-call%E5%AE%83%E5%9C%A8-ai-%E6%99%82%E4%BB%A3%E5%8F%AA)
[6] [https://ithelp.ithome.com.tw](https://ithelp.ithome.com.tw/m/articles/10392472)
[7] [https://www.figma.com](https://www.figma.com/pricing/)
[8] [https://uxwritinghub.com](https://uxwritinghub.com/the-complete-guide-to-figma-mcp-server-vibe-coding/)
[9] [https://developers.figma.com](https://developers.figma.com/docs/rest-api/rate-limits/)
[10] [https://developers.figma.com](https://developers.figma.com/docs/rest-api/authentication/)
[11] [https://github.com](https://github.com/glips/figma-context-mcp)
[12] [https://frankknow.com](https://frankknow.com/figma-ai/)
[13] [https://zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/1994153192506819522)

</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
乘上,Figma 的 Role 會影響 MCP Server 嗎? view, collaboration, dev 等
</td></tr><tr><td>A:</td><td>

## Figma Seat Type and MCP Quota

是的，Figma 的帳號角色（Role/Seat）會非常直接且嚴重地影響 MCP Server 的使用權限與呼叫額度。 [1]
Figma 官方針對 MCP Server 的限制，核心邏輯是將其綁定在 「Dev Mode（開發者模式）」 的功能權限內。不同角色的權限差異非常顯著： [2]

### 1. 各角色（Seat Type）的 MCP 權限與額度對照表

根據 [Figma 官方開發者文件](https://developers.figma.com/docs/figma-mcp-server/rate-limits-access/) 的規範，角色與額度的限制如下： [1]

| 角色類型 (Seat Type) [1, 3] | 適用對象與常見情境 | 官方 MCP 權限與額度限制 |
| --- |  --- |  --- |
| Dev Seat (開發者席位) | 團隊中專職看設計稿寫程式的工程師 | 完整支援。每天最高 200～600 次工具呼叫（依企業方案等級而定）。 |
| Full / Design Seat (完整設計席位) | 負責繪製 UI/UX 的設計師 | 完整支援。額度與 Dev Seat 相同，且只有此角色具備 MCP 「寫回畫布 (Write to Canvas)」的權限。 |
| View Seat (僅能觀看者) | 外部 PM、客戶、或團隊中未配置付費席位的成員 | 嚴重受限。不論公司買多高階的方案，每月僅能呼叫 6 次。AI 讀取 1~2 次設計稿就會斷線。 |
| Collaboration (協作者/舊版分類) | 參與討論但無設計/開發授權的成員 | 嚴重受限。同樣歸類於基本版限制，每月僅能呼叫 6 次。 |

### 2. 深入解析：不同角色在 MCP 中的行為差異

#### 2.1 💡 Dev Seat (開發者席位) ------ 最標準的開發配置

-   讀取設計（Read）：可以無限制（在每日額度內）讓 Cursor 或 Claude 讀取設計稿的圖層、Auto Layout 結構、變數（Variables）與元件中繼資料。 [1, 4]
-   Code Connect 整合：如果你們公司有設定 [Code Connect](https://help.figma.com/hc/en-us/articles/35280968300439-Figma-MCP-collection-What-is-the-Figma-MCP-server)（將程式碼元件對應到 Figma 元件），AI 透過 MCP 可以讀到真正前端元件的串接邏輯。 [5, 6]
-   寫回限制：Dev Seat 主要被定義為「讀取設計 context」，若嘗試叫 AI 幫你在 Figma 畫布上「通宵畫 UI」（Write to canvas），在草稿（Drafts）以外的正式專案檔案中會被拒絕。 [7]

#### 2.2 🎨 Full Seat (設計席位) ------ 雙向打通權限最高

-   擁有 Dev Seat 的所有讀取功能，外加完整的寫入權限。
-   你可以對 AI 下指令：*「幫我調整這個點選流程的 Frame 間距，並自動產生 3 個按鈕變體。」* AI 就能直接修改團隊正式專案裡的 UI 畫布。 [3, 7]

#### 2.3 🚫 View Seat (免費觀看者) ------ 實質上的「防禦壁壘」

-   這是最常踩坑的地方。許多公司為了省錢，只幫設計師買 Full Seat，工程師全部進去當免費的 Viewer。
-   當工程師把 Cursor 連上 Figma MCP 時，一開始會成功，但因為 View 權限每月只有 6 次扣點（Tool Calls），通常在嘗試產生第一個 API 結構或前端畫面時，額度就直接歸零歸零並噴出 `Rate Limit` 錯誤。 [1]

## 3. 🛠️ 結論與團隊配置建議

1.  若預算充足（走官方 MCP）：請團隊管理員至少將需要使用 AI 產 Code/產 API 的工程師升級為 Dev Seat。
2.  若想省錢（繞過 Role 限制）：不要在 Figma 介面裡點擊 "Enable Dev Mode MCP server"。請工程師直接去 Figma 帳號設定裡產出一組 Personal Access Token (PAT)，然後去 GitHub 下載開源社群維護的 Figma Context MCP [2]。這種走傳統 REST API 的開源 MCP Server，只要該帳號「看得到」那個設計檔（即使是免費 Viewer 角色），AI 就能順利讀取圖層資料，不再受到 6 次/月的硬性限制！ [2, 8, 9, 10]

[1] [https://developers.figma.com](https://developers.figma.com/docs/figma-mcp-server/rate-limits-access/)
[2] [https://help.figma.com](https://help.figma.com/hc/en-us/articles/35498519152663-Figma-MCP-collection-Dev-Mode-fundamentals-old-UI)
[3] [https://help.figma.com](https://help.figma.com/hc/en-us/articles/39252411778583-Figma-MCP-server-FAQs)
[4] [https://help.figma.com](https://help.figma.com/hc/en-us/articles/35280808976151-Figma-MCP-collection-MCP-collection-overview)
[5] [https://developers.figma.com](https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/)
[6] [https://help.figma.com](https://help.figma.com/hc/en-us/articles/35280968300439-Figma-MCP-collection-What-is-the-Figma-MCP-server)
[7] [https://developers.figma.com](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/)
[8] [https://www.youtube.com](https://www.youtube.com/watch?v=nPnkMPabCfI)
[9] [https://www.sina.cn](https://www.sina.cn/news/detail/5176299561157163.html)
[10] [https://www.youtube.com](https://www.youtube.com/watch?v=qdV1lRZjRc4)

</td></tr>
</table>
