# requestly

- https://github.com/requestly/requestly

> Requestly was built to save developers time by intercepting and modifying HTTP Requests. It has now developed into an open-source alternative to Charles Proxy and Telerik Fiddler that works directly in browsers without VPN and proxy Issues. It is used by more than 200,000+ front-end developers and 11,000+ companies worldwide.

## 2024-12-03

- 緣起：
  - 原本想試試看怎麼登入 APN 然後看能否擷取 https://explore.skillbuilder.aws/learn/lp/2193 
  - 看了一下 https://partnercentral.awspartner.com/partnercentral2/s/login 卻找不到 Login 是發送帳號密碼到哪裡
  - 問了一下 Perplexity，建議安裝  `Postman Interceptor` 或 `Requestly`
> 安裝像 `Postman Interceptor` 或 `Requestly` 的瀏覽器擴展，這些工具可以捕捉和記錄所有的 HTTP 請求，包括由 JavaScript 觸發的請求。
  - 所以裝了 [Requestly - Intercept, Modify & Mock HTTP Requests](https://chromewebstore.google.com/detail/requestly-intercept-modif/mdnleldcmiljblolnjhpnblkcekpdkpa)
- 試用心得：
  - 比較有趣的是可以 Record Session
    - 給定網址可以錄製該次的 network traffic
  - 安裝 Extension 以後會多一個 `Requestly` 的 Tab，相較於 `Chrome DevTools` 的 `Network` Tab 更容易理解