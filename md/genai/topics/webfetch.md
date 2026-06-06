# WebFetch vs Web Search

## 2026-06-06

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search AI Mode
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
AI Agent 的 WebFetch 跟 Web Search 有何不同？WebFetch 有特定的程式實作或函式庫嗎？
</td></tr><tr><td>A:</td><td>

WebFetch 與 Web Search 的核心差異在於「直接獲取特定網頁的原始內容」與「透過搜尋引擎搜尋關鍵字並篩選網頁」。 WebFetch 專注於下載指定 URL 的 HTML、JSON 或文字資料，而 Web Search 則是利用搜尋引擎（如 Google、Bing）找出與關鍵字相關的一系列連結與摘要。
在 AI Agent（人工智慧代理）的架構中，這兩個工具通常是相輔相成的。
------------------------------
## WebFetch 與 Web Search 的核心差異

* 操作對象：WebFetch 的輸入通常是特定的 URL 網址；Web Search 的輸入則是關鍵字或自然語言問題。
* 運作邏輯：WebFetch 直接發送 HTTP 請求（如 GET）到目標伺服器並下載網頁內容；Web Search 則是調用搜尋引擎的 API，回傳包含多個網站標題、連結與摘要的列表。
* AI Agent 的使用情境：AI Agent 通常會先使用 Web Search 尋找答案可能存在的網站，取得 URL 後，再使用 WebFetch 進入該網站抓取詳細文字，最後進行讀取、總結或分析。

------------------------------
## WebFetch 的特定程式實作與函式庫
在開發 AI Agent 時，WebFetch 通常不會單獨被視為一個「全新發明的通訊協定」，而是基於現有的網路爬蟲（Web Scraping）與自訂義工具（Custom Tools）技術來實作。
根據 AI Agent 框架的不同，常見的實作方式與函式庫如下：
## 1. AI Agent 框架中的內建工具 (Built-in Tools)
主流的 AI Agent 框架通常直接內建了 WebFetch 功能：

* LangChain / LangGraph：內建了 LangChainCommunityURLLoader 或整合了 Jina Reader API、Firecrawl 等服務。這些服務能將任意網址的 HTML 直接轉換為適合大語言模型（LLM）閱讀的 Markdown 格式。
* CrewAI：提供了內建的 ScrapeWebsiteTool，AI Agent 只要傳入網址，該工具就會自動下載並解析網頁純文字。
* LlamaIndex：內建 SimpleWebPageReader，可以將一組 URLs 直接轉換為 AI 可以建立索引的 Document 物件。

## 2. 底層常用的 Python 函式庫
如果你想從零開始實作 AI Agent 的 WebFetch 工具，通常會封裝以下幾種熱門的 Python 函式庫：

* Requests：最基礎的 HTTP 庫，適合抓取靜態網頁（傳回原始 HTML）。
* Playwright / Selenium：當目標網頁是動態網頁（包含大量 JavaScript、需要等待元件渲染，例如單頁應用程式 SPA）時，AI Agent 會驅動這些無頭瀏覽器（Headless Browser）來執行 WebFetch。
* BeautifulSoup / Scrapy：用於 WebFetch 後的資料清理，剔除網頁中無用的廣告、導覽列（Navigation bar）和 JavaScript 程式碼，只保留核心文字供 LLM 閱讀，以節省 Token 成本。

------------------------------
## 兩者在 Agent 運作流程中的協同範例

   1. 使用者提問：「請幫我查詢微軟（Microsoft）最新一季的財報營收是多少？」
   2. Agent 決策：發現需要即時資訊，啟動 Web Search 工具（輸入關鍵字：Microsoft Q3 earnings report 2026）。
   3. Web Search 回傳：回傳前 5 個搜尋結果，其中一個連結是微軟官方的投資人關係頁面（URL: https://microsoft.com）。
   4. Agent 再次決策：為了獲取精確數字，啟動 WebFetch 工具（輸入 URL：https://microsoft.com）。
   5. WebFetch 回傳：抓取該網頁的完整文字或 Markdown 內容。
   6. Agent 總結：讀取 WebFetch 回傳的文字，擷取出營收數字，最終回答使用者。

------------------------------
如果想深入了解如何為你的 AI Agent 整合這兩項功能，您可以告訴我：

* 您目前使用的是哪套 AI Agent 框架（例如 LangChain、CrewAI、或是自己從零開發）？
* 您希望抓取的網頁是公開的靜態網頁，還是需要登入/驗證的動態網頁？
* 您是否需要處理防爬蟲機制（如 Cloudflare 阻擋）？

我可以為您提供更具體的程式碼實作範例。

</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
Q1: LangChian / LangGraph 內建的函數也是用 Requests, Playwright, Scrapy 實作的嗎？什麼是 Jina Reader API？
Q2: Firecrawl 與 CrewAI 有關係嗎？
Q3: 根據 OpenCode 的原始碼，可以知道 WebFetch 工具是如何實作的嗎？
</td></tr><tr><td>A:</td><td>
針對您提出的三個進階問題，以下為您進行深度的技術拆解：
------------------------------
## Q1: LangChain / LangGraph 內建函數也是用 Requests, Playwright, Scrapy 實作的嗎？什麼是 Jina Reader API？## 1. LangChain / LangGraph 的底層實作
是的，LangChain 的內建網頁讀取工具（Document Loaders），底層確實大量封裝了傳統的 Python 網路庫。
LangChain 本身並不發明新的網路傳輸協定，而是將現有技術包裝成 Agent 容易調用的介面（Tools）。例如：

* AsyncHtmlLoader：底層主要是基於 aiohttp（一種類似 Requests 但支援非同步的庫）或 Requests 來抓取靜態 HTML。
* PlaywrightURLLoader：直接在底層驅動 Playwright，用來啟動無頭瀏覽器（Headless Browser），等待 JavaScript 渲染完成後再撈取 DOM 節點。
* Scrapy 則較少作為 LangChain 內建核心：因為 Scrapy 是一個大型的非同步爬蟲框架，架構較重，更適合做大規模數據集爬取；AI Agent 通常需要的是單次、即時的網頁抓取，因此 LangChain 內建工具更傾向使用 BeautifulSoup 搭配 Requests 來解析靜態文字。

## 2. 什麼是 Jina Reader API？
Jina Reader API 是一個專門為大語言模型（LLM）量身打造的網頁轉換服務。 [1] 

* 運作原理：傳統爬蟲抓回來的 HTML 夾雜了大量的 <div> 標籤、廣告、JavaScript、CSS，直接丟給 LLM 會浪費大量的 Token 且干擾理解。Jina Reader 做的事情就是輸入任意網址，直接將其轉化為乾淨、排版整齊的 Markdown 文字。 [1] 
* 最大特色（超簡單調用）：它不需要你寫複雜的爬蟲程式碼。你只需要在你想爬的網址前面加上 https://r.jina.ai/ 即可。
* 例如：在瀏覽器或程式中請求 https://r.jina.ai/https://example.com。
   * 回傳的內容就是專屬給 LLM 閱讀的「閱讀模式」Markdown 文字。它已經被廣泛整合進各種 AI Agent 框架中作為高效率的 WebFetch 後端。 [1] 

------------------------------
## Q2: Firecrawl 與 CrewAI 有關係嗎？
兩者在官方組織上沒有直接的血緣關係（由不同團隊開發），但在生態系與應用上有極為緊密的整合關係。

* CrewAI 是一個 AI Agent 協同框架（負責管代理、分配任務、決定工作流）。
* Firecrawl 是一個專為 LLM 設計的開源網頁爬蟲與數據轉換工具，它能將整個網站或單一網頁轉成 Clean Markdown 或結構化 JSON。 [1, 2, 3] 

## 他們之間的關係：

   1. 官方工具整合：CrewAI 官方為了讓旗下的 Agent 擁有更強大的網頁抓取與自動翻頁（Crawl）能力，直接將 Firecrawl 封裝成了內建的工具元件（例如 FirecrawlScrapeWebsiteTool）。
   2. 解決傳統爬蟲痛點：CrewAI 內建的傳統 ScrapeWebsiteTool 若遇到動態網頁或複雜反爬蟲機制容易失效；這時開發者通常會改用 Firecrawl 作為 Agent 的底層 WebFetch 引擎，讓 CrewAI 的 Agent 能夠輕鬆穿透動態網頁並獲取乾淨的資料。

------------------------------
## Q3: 根據 OpenCode 的原始碼，可以知道 WebFetch 工具是如何實作的嗎？
是的，根據熱門開源 AI 編程助手 OpenCode 的官方 GitHub 儲存庫原始碼（具體位於 packages/opencode/src/tool/webfetch.ts），我們可以非常清楚地看到其 webfetch 工具的實作邏輯： [4, 5, 6] 
## 1. 技術棧：Bun + TypeScript
OpenCode 是基於 Bun（一個極快的 JavaScript/TypeScript 執行環境）所開發的。它的 webfetch 核心並不是使用 Python，而是使用 TypeScript 撰寫。 [4] 
## 2. 底層核心實作：Bun.fetch + 瀏覽器偽裝 (Spoofing)
在源碼中，webfetch 的實作本質上是一個高級的 HTTP 請求，具有以下特徵： [4] 

* 不使用完整瀏覽器：它為了追求極致的速度，並沒有在預設情況下啟動像 Playwright 這樣沈重的無頭瀏覽器，而是直接調用 Bun 內建的高效能 fetch() 函式。 [4] 
* User-Agent 偽裝：為了避免被許多網站的防火牆直接阻擋，OpenCode 在發送請求時，會在 Header 中配置常見的瀏覽器 User-Agent（例如偽裝成 Chrome 或 Safari 瀏覽器）。 [4] 
* HTML 轉 Markdown 處理：當 fetch 成功拿回網頁的原始 HTML 後，OpenCode 會在記憶體中利用解析庫（如 cheerio 或類似的 HTML Parser）將網頁中的導覽列、頁尾、腳本剔除，最後將核心內容格式化為 Markdown 文本 回傳給 LLM。 [7, 8] 

## 3. 原始碼中暴露的限制（反爬蟲碰撞）
從 OpenCode 的社群討論與原始碼更新中（如 Issue #2228），這種實作方式也揭示了 AI Agent 常遇到的瓶頸：

* 因為它使用 fetch（非真實瀏覽器）卻帶有瀏覽器的 User-Agent，當它遇到部署了 Anubis 或 Cloudflare 高級防護的網站時（例如 kernel.org），網站會要求進行「客戶端計算證明（Proof of Work / 驗證碼挑戰）」。 [4] 
* 由於 Bun.fetch 無法像真實瀏覽器一樣執行這些複雜的驗證腳本，這會導致 OpenCode 的 webfetch 工具在這些網站上被直接封鎖（Block）。這也是為什麼有些開發者在本地使用 OpenCode 時，會選擇額外掛載像 TinyFish MCP 這類的外部聯網插件來增強其 WebFetch 能力。 [4, 9] 

------------------------------
如果您正準備為自己的專案開發聯網功能，我們可以進一步討論：

* 您希望仿照 OpenCode 基於 Node.js/Bun 來實作工具，還是希望使用 Python 生態系？
* 您需要為 Agent 實作簡單的單頁讀取（Fetch），還是需要具備跟隨連結爬行（Crawl）的能力？


[1] [https://ithelp.ithome.com.tw](https://ithelp.ithome.com.tw/articles/10365557)
[2] [https://docs.crewai.com](https://docs.crewai.com/en/tools/ai-ml/langchaintool)
[3] [https://www.firecrawl.dev](https://www.firecrawl.dev/blog/best-open-source-web-crawler)
[4] [https://github.com](https://github.com/anomalyco/opencode/issues/2228)
[5] [https://hackmd.io](https://hackmd.io/@BASHCAT/B1zktAnNZx)
[6] [https://www.firecrawl.dev](https://www.firecrawl.dev/blog/claude-code-vs-opencode)
[7] [https://www.runoob.com](https://www.runoob.com/opencode/opencode-tools.html)
[8] [https://www.runoob.com](https://www.runoob.com/ai-agent/opencode-coding-agent.html)
[9] [https://www.youtube.com](https://www.youtube.com/watch?v=dZ71lfwqxj4)

</td></tr>
</table>