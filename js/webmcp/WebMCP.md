# WebMCP

- Git Repo
  - https://github.com/webmachinelearning/webmcp
- Website
  - https://webmachinelearning.github.io/webmcp/

## 2026-06-05

- 緣起：
  - 在看 Chrome DevTool for Agent 時看到 WebMCP 這個關鍵字的連結
  - https://developer.chrome.com/docs/ai/webmcp

## 2026-06-14

- Build your website for the agentic era
  > Build websites for an era where AI agents, like Gemini in Chrome, assist users by understanding page context and triggering actions. Learn how to prepare your pages to help agents perform tasks efficiently, and explore APIs like WebMCP that make agent interactions faster and more reliable.
- https://io.google/2026/explore/technical-session-32

## 2026-09-09

> [!QUESTION]
> WebMCP 如何讓 AI Agent 知道網站是如何運作?

WebMCP（Web Model Context Protocol）讓網站從被動地「讓 AI 猜測畫面」，轉變為主動「宣告自己的功能與規則」。 [1, 2]
傳統上，AI Agent（如瀏覽器操作助手）要理解網站，必須像人類一樣抓取網頁原始碼（DOM）、截圖、並盲目猜測按鈕的功能，這既慢又容易因為網頁改版而壞掉。而 WebMCP 則是讓網站直接提供一組結構化的「工具清單」給 AI Agent，其核心運作機制主要透過以下幾種方式： [3, 4]

### 1. 透過標準 API 主動宣告能力 (Imperative API)

網站開發者可以使用 WebMCP 提供的 API（例如 document.modelContext），在 JavaScript 中直接註冊網站具備的功能。 [5]

*
* 宣告結構： 每個註冊的工具都包含名稱（Name）、自然語言描述（Description） 以及輸入規格（JSON Schema）。
* 舉例說明： 網站可以告訴 AI 這裡有一個叫 search_products 的功能，描述是「搜尋站內鍵盤」，且限制最大價格。AI Agent 讀到這段規格後，不需要去點擊搜尋框、輸入文字、再按送出，而是直接呼叫這個 JavaScript 函式並傳入參數。 [4, 5]
*

### 2. 透過 HTML 表單直接轉化 (Declarative API)

除了用 JavaScript 寫死，網頁也可以利用現有的 HTML 標籤（如 <form> 表單）進行宣告。WebMCP 允許將表單直接轉化為 AI 看得懂的 Schema，AI 讀取後就能理解「這個表單是拿來訂便當或訂機票的」以及「需要填入哪些必填欄位」，並直接在背景送出資料。 [2, 6, 7, 8]

### 傳統 Browser Agent 運作 vs. WebMCP 運作對比

| 比較項目 | 傳統 Browser Agent 運作 (如看截圖、猜 DOM) | WebMCP 運作模式 |
|---|---|---|
| 理解方式 | 閱讀整份 DOM 程式碼、掃描截圖、盲猜按鈕功能 | 直接讀取網站宣告的工具清單與自然語言描述 |
| 操作步驟 | 重演人類步驟（點擊輸入框 → 打字 → 按送出） | 直接呼叫 JavaScript 函式或結構化表單 |
| 穩定度 | 差。網頁一旦改版、換個 Class 名稱就會失效 | 高。只要底層的 API 規則沒變，UI 怎麼改都不影響 AI |
| 速度與成本 | 慢且貴（每一步都要塞大量截圖與程式碼給 AI） | 極快。直接傳遞結構化 JSON 資料，通常只需幾秒 |

簡單來說，WebMCP 就像是網站幫 AI Agent 準備了一份「網頁專用說明書與快捷鍵」，讓 AI 不需要走人類的視覺老路，直接進行高效率的機器對機器（M2M）通訊。 [2, 3]
如果你想深入了解或實作，可以參考詳細的 [WebMCP 基本概念解析](https://fullstackladder.dev/blog/2026/07/15/webmcp-basic-concepts/) 或查看 [Kuro Hsu 的 WebMCP 實測筆記](https://kurohsu.dev/learn/learning-webmcp.html)。 [1, 4]

您目前是想評估自家網站是否適合導入 WebMCP，還是想了解如何在前端寫出對應的 JavaScript 程式碼呢？請告訴我您的情境，我可以提供更具體的程式碼範例或安全性的設計原則！

[1] [https://fullstackladder.dev](https://fullstackladder.dev/blog/2026/07/15/webmcp-basic-concepts/)
[2] [https://jikensitu.com](https://jikensitu.com/digital-marketing/webmcp/)
[3] [https://www.facebook.com](https://www.facebook.com/jerry.chang.505523/posts/%E5%BE%9E-seo-%E5%88%B0-aeo-%E5%88%B0-agent-%E5%9F%B7%E8%A1%8Cwebmcp-%E6%80%8E%E9%BA%BC%E8%AE%93%E7%B6%B2%E7%AB%99%E7%82%BA-ai-agent-%E6%BA%96%E5%82%99%E5%A5%BDwebmcp-%E6%98%AF-google-%E5%92%8C-microsoft-%E7%9A%84%E8%81%AF%E5%90%88%E5%AF%A6/10241917151880650/)
[4] [https://kurohsu.dev](https://kurohsu.dev/learn/learning-webmcp.html)
[5] [https://ithelp.ithome.com.tw](https://ithelp.ithome.com.tw/articles/10409012)
[6] [https://yishiashia.github.io](https://yishiashia.github.io/posts/webmcp-introduction/)
[7] [https://www.np.com.tw](https://www.np.com.tw/modules/news/article.php?storyid=20)
[8] [https://masonailab.com](https://masonailab.com/tech/webmcp-browser-ai-agent-standard-2026/)

## 2026-09-10

- 2026-04-24
  - 讓網站直接跟 AI Agent 對話：初試 WebMCP
  - https://kurohsu.dev/learn/learning-webmcp.html
- 2026-07-15
  - [WebMCP] 基本概念：讓網站把功能直接變成 AI Agent 的工具
  - https://fullstackladder.dev/blog/2026/07/15/webmcp-basic-concepts/