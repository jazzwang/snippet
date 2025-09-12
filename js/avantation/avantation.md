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

## 2024-11-22

- ( 2024-11-22 10:20:59 )
- 測試 Github Codespace Usage 的 HAR 生成 API
- 環境：Github Codespace
```bash
jazzw@JazzBook:~/git/snippet$ gh cs code
? Choose codespace: jazzwang/snippet (master*): snippet
```
- 安裝
```bash
@jazzwang ➜ /workspaces/snippet (master) $ npm install -g avantation
@jazzwang ➜ /workspaces/snippet (master) $ which avantation 
/home/codespace/nvm/current/bin/avantation
```
- 上傳 HAR 檔
```bash
jazzw@JazzBook:~/Downloads$ gh cs cp github_codespaces_usage.har 'remote:/tmp' -R jazzwang/snippet
github_codespaces_usage.har
```
- ( 2024-11-22 11:19:58 )
- 發現似乎 MIME 必須是 `application/json` 才會被納入考慮。
```bash
@jazzwang ➜ /workspaces/snippet/js/avantation (master) $ avantation /tmp/github_codespaces_usage.har 
 ›   Warning: Skipping invalid mimeType:text/html @https://github.com/settings/contexts?context_type=user&id=jazzwang in response.
 ›   Warning: Skipping invalid mimeType:text/html @https://github.com/settings/billing/usage_notification in response.
 ›   Warning: Skipping invalid mimeType:text/html @https://github.com/settings/billing/actions_usage in response.
 ›   Warning: Skipping invalid mimeType:text/html @https://github.com/settings/billing/packages_usage in response.
 ›   Warning: Skipping invalid mimeType:text/html @https://github.com/settings/billing/shared_storage_usage in response.
 ›   Warning: Skipping invalid mimeType:text/html @https://github.com/settings/billing/codespaces_usage.jazzwang in response.
✔ GET   /notifications/indicator
✔ all taskes completed
```
- 把 HAR 裡的 `"text/html"` 取代為 `""`，就可以跑得出來了。
```bash
@jazzwang ➜ /workspaces/snippet/js/avantation (master) $ avantation github_codespaces_usage.har 
✔ GET   /settings/contexts
✔ GET   /settings/billing/usage_notification
✔ GET   /settings/billing/actions_usage
✔ GET   /settings/billing/packages_usage
✔ GET   /settings/billing/shared_storage_usage
✔ GET   /settings/billing/codespaces_usage.jazzwang
✔ GET   /notifications/indicator
✔ all taskes completed
```
- 只不過生成的 OpenAPI Swagger 文件，都是以 `application/json` 為 MIME，所以還要在研究看看其他解法。

## 2025-09-11

- 初步做了一些實驗，除了遇到 `application/json` 為 MIME 才能解析並生成 `openapi.yaml` 檔以外，
  也遇到額外的錯誤：
  ```
  Failed to resolve $ref
  ```
- 測試環境：Windows 11
- 安裝：
  ```bash
  [09/11 11:45:37] npm install -g avantation
  [09/11 11:46:26] which avantation
  ```
- Jira 匯出 Excel 的功能，從 HAR 看起來，還蠻直覺的。但 `avantation` 沒辦法識別
  ```bash
  [09/11 11:46:52] avantation 2025-09-10_JQL_Export_as_Excel.har
  ```