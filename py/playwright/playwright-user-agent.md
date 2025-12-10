# Changing User Agent in Playwright

- 2024-10-07
  - Changing User Agent in Playwright for Effective Web Scraping
  - https://scrapingant.com/blog/change-user-agent-playwright
  - 核心應該就是這兩行：
    ```python
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    context = await browser.new_context(user_agent=user_agent)
    ```

> [!NOTE]
>
> 這篇文章主要介紹為什麼在使用 Playwright 做網路爬蟲時需要修改 User-Agent，以及實作方法、最佳實務和風險考量。
>
> ## 主要內容概述
> - 說明 User-Agent 是瀏覽器與作業系統的識別字串，會影響網站回傳的內容版本（桌機/手機）、功能與封鎖判斷，也常被用來偵測機器人流量。
> - 文章示範如何在建立 Playwright browser context 時設定自訂 User-Agent，以及如何準備多個真實的 User-Agent 清單並進行輪替（例如每個 session 或每段時間更換一次）。
>
> ## 技術與最佳實務
> - 建議使用看起來真實、最新的 User-Agent，並確保 User-Agent 與其他標頭、瀏覽器能力（如 viewport、平台）一致，以降低被識別為機器人的機率。
> - 推薦搭配代理（proxy）輪換、控制請求頻率、模擬人類瀏覽行為等方式一起使用，而不是只依賴修改 User-Agent。
>
> ## 風險、效能與資料品質
> - 指出頻繁建立多個 context 或複雜輪換策略會增加資源消耗，需要在效能與隱匿性之間做權衡，並透過監控成功率和錯誤率來調整策略。
> - 不同 User-Agent 可能導致回傳內容差異（A/B 測試、地區版本、行動版頁面等），因此需要驗證與正規化資料，有時也要用多種 User-Agent 抓取同一頁來比對差異。
>
> ## 法律與倫理考量
> - 文章提醒修改 User-Agent 涉及偽裝行為，在法律和倫理上存在灰色地帶，建議尊重 robots.txt、網站使用條款與速率限制，並盡量以負責任的方式進行資料擷取。
>
> .

- 備忘：
  - 怎麼取得模擬不同裝置的 user_agent 字串？
  - https://developer.chrome.com/docs/devtools/device-mode/override-user-agent
  - e.g.
    - `Chrome - Mac`
    - `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36`