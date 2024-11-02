# avantation

> Build OpenAPI3.0 specification from HAR.

- https://avantation.in/
- Git Repo: https://github.com/anbuksv/avantation

## 2024-10-31

- 緣起：
  - 工作上常遇到不同的 web service，有時候想要批次查詢（例如：針對每個團隊成員，查看 IdentityIQ 上是否有需要的權限，查詢到職日等），靠瀏覽器逐一查詢，複製貼上很曠日費時。
  - 雖然曾經用 Selenium 自動化操縱瀏覽器來做查詢，甚至做資料萃取，但控制瀏覽器會比單純使用 API 吃硬體資源。
- 已知限制：
  - 當然牽涉到該 web service 到底是 server side render, client side render 是否有 backend API 還是根本連 MVC 架構都沒有。如果該服務本身並沒有 RESTful API，或者用 GraphQL 等，也是跑不出結果的。
- 蒐集：
  - 在 https://openapi.tools/ 有看到三個可以把瀏覽器匯出的網路紀錄 HAR 檔案轉成 OpenAPI Swagger 文件的工具：
    - https://github.com/jonluca/har-to-openapi
    - https://github.com/dcarr178/har2openapi
    - https://github.com/anbuksv/avantation
- 實測：
  - 經實測，目前 avantation 的產出結果比另兩套符合需求。