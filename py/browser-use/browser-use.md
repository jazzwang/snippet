# browser-use

> 🌐 Make websites accessible for AI agents. Automate tasks online with ease.

- Git Repo
  - https://github.com/browser-use/browser-use
- Website
  - https://browser-use.com/
- Document
  - https://docs.browser-use.com/cloud/quickstart

## 2026-05-12

- 緣起：
  - LinkedIn
- Skill
  - https://skills.sh/browser-use/browser-use/browser-use
  ```bash
  ~$ npx skills add https://github.com/browser-use/browser-use --skill browser-use
  ```

## 2026-05-15

- Q1: 待比較 browser-use 跟 agent-browser 有什麼差異？
- A1:
- Google Search - AI Mode
> https://browser-use.com 跟 https://agent-browser.dev/ 有什麼不同？

browser-use 與 agent-browser 是兩款專為 AI 智慧體（Agent）設計的瀏覽器自動化工具。它們的核心定位、架構設計與整合方式有顯著不同： [1, 2]

-   browser-use 是一個全功能 Python 開源 AI Agent 框架，專注於讓 AI 自主規劃、理解視覺截圖並執行任務。
-   [agent-browser](https://agent-browser.dev/) 則是由 Vercel Labs 推出的輕量級、命令列（CLI）優先的底層工具，旨在減少 AI 的 Token 消耗。 [1, 2, 3, 4]

### 核心差異對比

下表彙整兩者在定位、開發語言、核心機制與整合場景的直接對比：
[agent-browser](https://agent-browser.dev/)

| 比較維度 [1, 4, 5, 6, 7, 8] | browser-use |
| --- |  --- |
| 主要定位 | 完整的 AI Agent 應用框架 |
| 主導開發語言 | Python |
| AI 畫面理解機制 | 視覺截圖（Vision） + 網頁 DOM 解析 |
| Token 消耗 | 較高（需傳送圖片與複雜 DOM 脈絡） |
| 主要使用對象 | Python AI 應用、自主執行任務的 Agent 開發 |
| 操作方式 | 透過 Python 程式碼編寫任務 |

### 詳細特點剖析

#### 1. 控制與理解網頁的方式不同

-   browser-use 的視覺引導： 它底層驅動 Playwright，並讓大型語言模型（LLM）觀看網頁截圖來決定下一步，類似人類視覺操作。適合需要高度依賴視覺排版理解的複雜多步驟任務（例如：買機票、訂餐廳）。
-   agent-browser 的標籤參考： 它不讓 AI 讀取幾千行的原始 HTML，而是將網頁簡化為「可互動的無障礙樹」，並為每個按鈕、輸入框標上序號（例如：`[ref=e1]`）。AI 只需要下達 `agent-browser click @e1` 的純文字指令即可完成操作，極度節省 Context 空間。 [1, 3, 7, 9]

#### 2. 架構與效能上的差異

-   browser-use： 純 Python 庫，整合了任務規劃器（Planner）、歷史紀錄管理、甚至是將操作過程錄製成 GIF 的功能，整體功能較重、較厚。
-   agent-browser： 採用精簡的 Rust CLI + Node.js Daemon 雙層架構。常駐服務（Daemon）啟動後會維持瀏覽器 Session，免除每次 AI 下指令時的冷啟動時間，且提供本地即時檢視畫面與指令流的儀表板（Dashboard）。 [3, 4, 10, 11]

#### 3. 整合生態與適用場景

-   如果您要開發獨立的 AI 應用： 選擇 browser-use。它能讓您用 Python 快速串接 LangChain 或其他 LLM，給它一個模糊的目標（如「幫我查今天最便宜的機票」），它就會自己規劃並點擊完成。
-   如果您想讓 IDE 編輯器或終端機助手具備網頁能力： 選擇 agent-browser。它完美整合了 MCP (Model Context Protocol) 協定與 Vercel 的 Skill 系統，是目前 Claude Code、Cursor 等 AI 寫程式工具用來<mark>測試網頁、爬取資料</mark>的最佳擴充元件。 [1, 3, 12, 13, 14]

您目前是在開發獨立的 AI 自動化 Agent，還是想在 AI 編碼工具（如 Claude Code/Cursor） 中引入瀏覽器操作呢？告訴我您的應用場景，我可以為您提供對應的安裝與程式碼範例。

[1] [https://www.cnblogs.com](https://www.cnblogs.com/itech/p/20045683)
[2] [https://help.apiyi.com](https://help.apiyi.com/en/agent-browser-ai-browser-automation-cli-guide-en.html)
[3] [https://www.youtube.com](https://www.youtube.com/watch?v=GPb4woYA_8s)
[4] [https://deepseek.csdn.net](https://deepseek.csdn.net/67fc87a9da5d787fd5cc831b.html)
[5] [https://www.instagram.com](https://www.instagram.com/p/DTmzBHaD5pf/)
[6] [https://agent-browser.dev](https://agent-browser.dev/)
[7] [https://www.deeplearning.ai](https://www.deeplearning.ai/short-courses/building-ai-browser-agents/)
[8] [https://www.pulumi.com](https://www.pulumi.com/blog/self-verifying-ai-agents-vercels-agent-browser-in-the-ralph-wiggum-loop/)
[9] [https://www.pulumi.com](https://www.pulumi.com/blog/self-verifying-ai-agents-vercels-agent-browser-in-the-ralph-wiggum-loop/)
[10] [https://www.npmjs.com](https://www.npmjs.com/package/agent-browser)
[11] [https://zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/1885651451088462924)
[12] [https://medium.com](https://medium.com/@bytefer/browser-automation-cli-designed-for-ai-agents-has-arrived-0b8181613669)
[13] [https://zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/1885651451088462924)
[14] [https://classic.yarnpkg.com](https://classic.yarnpkg.com/en/package/agent-browser-mcp)