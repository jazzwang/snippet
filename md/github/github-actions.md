# github-action-lab
Testing Github Actions and build DEB/RPM packages and win64 executables

## 2022-12-12

- ( 2022-12-12 22:14:56 )
- Testing ["Manual workflow"](https://github.com/jazzwang/github-action-lab/actions/new?category=automation)
![Manual Workflow](https://user-images.githubusercontent.com/76903/207067224-e496fb79-49a4-4908-aa29-6a13638050c3.png)
- ( 2022-12-12 22:19:39 )
- Testing ["Build projects with Make"](https://github.com/jazzwang/github-action-lab/actions/new?category=continuous-integration&query=make)
![image](https://user-images.githubusercontent.com/76903/207068575-d172bfab-8f35-40a6-bac3-34e6d5c928f6.png)
- ( 2022-12-12 22:25:56 )
- Q: Does Github Action support `git submodule`?
- A: https://github.com/marketplace/actions/checkout-submodules

>  **INSTALLATION**
>  Copy and paste the following snippet into your .yml file.
>
>  ```yaml
>  - name: Checkout submodules
>  uses: textbook/git-checkout-submodule-action@2.1.1
>  ```
>
>  [Learn more about this action in textbook/git-checkout-submodule-action](https://github.com/textbook/git-checkout-submodule-action)

## 2022-12-15

- ( 2022-12-15 11:08:10 )
- Q: How to store `secrets` in Github Actions?
- https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository
- https://github.com/Azure/actions-workflow-samples/blob/master/assets/create-secrets-for-GitHub-workflows.md
- AWS credentials?
- https://github.com/aws-actions/configure-aws-credentials
- GitHub Action workflows to deploy to Azure
- https://github.com/Azure/actions-workflow-samples

## 2022-12-29

- ( 2022-12-29 14:16:47 )
- Q: Does Github Action support cron job?
- https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule
- https://docs.getnacelle.com/deployment/scheduled-builds-github-actions.html
```yaml
# .github/workflows/scheduled-builds.yml
name: Trigger Site Rebuild on a CRON Schedule

on:
  schedule:
    # Runs "at minute 55 past every hour" (see https://crontab.guru)
    - cron: '55 * * * *'
```

## 2022-12-30

- ( 2022-12-30 09:13:01 )
- https://github.com/actions/setup-python#caching-packages-dependencies
```yaml
steps:
- uses: actions/checkout@v3
- uses: actions/setup-python@v4
  with:
    python-version: '3.9'
    cache: 'pip' # caching pip dependencies
- run: pip install -r requirements.txt
```

## 2024-07-09

- ( 2024-07-09 14:14:11 )
- 最近為了在內網的 Windows 環境裡裝 [plow](https://github.com/six-ddc/plow)，所以想要試試看怎麼產生 plow 的 win64 binary
- 首先需要能在 Github Actions 的 `windows-latest` 環境裡，安裝 golang
- Google 了一下，先找到 https://github.com/actions/setup-go
- 雖然 https://github.com/actions/setup-go/blob/main/.github/workflows/windows-validation.yml 有看到做了 Windows 環境的驗證，但沒有看到文件裡寫到 Windows 環境的範例。
- ( 2024-07-09 14:23:51 )
- 參考 https://www.omerlh.info/2022/02/25/how-to-build-go-c-code-for-windows-using-github-actions/
  - https://github.com/omerlh/wizo-scheduler/blob/main/.github/workflows/go.yml

### Github Marketplace

- ( 2024-07-09 14:24:45 )
- 後來發現 Github Marketplace 有一些 Actions 可以用
  - https://github.com/marketplace/actions/setup-go-environment
- https://github.com/marketplace?query=Chocolatey 
  - https://github.com/marketplace/actions/chocolatey-action - 在 [How To Build Go & C Code for Windows using Github Actions](https://www.omerlh.info/2022/02/25/how-to-build-go-c-code-for-windows-using-github-actions/) 有提到用 chocolatey 指令 `choco`，但是這篇作者的 github action 實作 [.github/workflows/go.yml](https://github.com/omerlh/wizo-scheduler/blob/main/.github/workflows/go.yml) 並沒有用到其他 marketplace 的 actions. 初步壞疑 `windows-latest` 已經包了 `choco` 。待確認。
  - https://github.com/marketplace/actions/install-chocolatey-pkg
- https://github.com/marketplace?query=scoop
  - https://github.com/marketplace/actions/setup-scoop
  - https://github.com/marketplace/actions/scoop-action
  - https://github.com/marketplace/actions/scoop-checkver-action

## 2024-07-11

- ( 2024-07-11 22:01:06 )
- 在 Github Actions Marketplace 看到一個有趣的實作 "Convert JSON to HTML Table"
  - https://github.com/marketplace/actions/convert-json-to-html-table
- 範例顯示有一個輸入 JSON 檔，會產生一個 HTML 的 `Table`
- ( 2024-07-11 22:02:44 )
- 反查了一下原始碼 https://github.com/Teebra/JSON-to-HTML-table/blob/main/entrypoint.py
- 原來是透過 `json2table` 這個套件
  - `json2table` 原始碼在 https://github.com/latture/json2table
  - 竟然是八年前的實作了。其次，沒什麼人給星星 :)
  - 以前常需要靠 PlantUML 把 JSON 檔轉成圖檔，以利找出一些規律（跟理解背後的 Data Model）
  - 未來也許可以用這個套件來解讀比較複雜的 JSON 檔。

## 2024-07-18

- ( 2024-07-18 23:28:12 )
- 緣起：想把查圖書館待取待還書目列表，透過 Github Actions 定期執行，並改用 HTML 方式呈現結果。
- 研究：
  - https://github.com/marketplace/actions/html-preview
  - https://github.com/marketplace/actions/html-reporter-github-pages
- ( 2024-07-18 23:30:03 )
- 看到另一個有趣的 Github Actions Marketplace 專案
  - https://github.com/marketplace/actions/aqua-security-trivy
  - 可以用 Github Actions 檢查 docker image 的 vulnerabilities
  - 原始碼：https://github.com/aquasecurity/trivy-action
  - Runs Trivy as GitHub action to scan your Docker container image for vulnerabilities

## 2024-10-29

- ( 2024-10-29 21:12:01 )
- 緣起：常要查小孩營養午餐吃什麼。如果可以定時去抓網頁，產生截圖，然後 LINE 傳訊息到群組，就太好了！
- 實作：
  - 產生截圖 - https://github.com/marketplace/actions/screenshots-ci-action
  - 通知 - LINE Notify 已經無法使用了 
    - https://github.com/louis70109/line-notify-action
    - https://engineering.linecorp.com/zh-hant/blog/github-actions-line-notify
  - LINE Message
    - https://github.com/marketplace/actions/line-push-message
    - https://github.com/ufoo68/line-push-message
- 先照 https://github.com/marketplace/actions/screenshots-ci-action 的範例，
  搭配 2022-12-29 查的排程寫法 [schedule trigger workflow](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule)
  - 因為不知道 cron 的時區是那一個，先假設是 UTC。所以台灣中午 12:30 等於 UTC 4:30 AM。
```yaml
# https://github.com/marketplace/actions/screenshots-ci-action
name: screenshots of lunch
on:
  schedule:
    # Runs "" (see https://crontab.guru)
    - cron: '30 4 * * 1-5'
```
  - 至於 workflow 的部份就先比照範例，只需要改掉 `url` 即可。
```yaml
jobs:
  screenshots:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: install puppeteer-headful
      uses: mujo-code/puppeteer-headful@master # Required for headful puppeteer
      env:
        CI: 'true'
    - name: screenshots-ci-action
      uses: flameddd/screenshots-ci-action@master
      with:
        url: https://fatraceschool.k12ea.gov.tw/frontend/search.html?school=64736003
        devices: iPad Pro landscape
    - uses: actions/upload-artifact@v2 # Uplaod screenshots to Actions Artifacts via actions/upload-artifact@v2
      with:
        path: screenshots
        name: Download-screenshots
```
   - 接著就等明天的結果囉 :P

## 2024-10-30

- 錯誤訊息：
```
Set up job

This request has been automatically failed because it uses a deprecated version of `actions/upload-artifact: v2`. 
Learn more: https://github.blog/changelog/2024-02-13-deprecation-notice-v1-and-v2-of-the-artifact-actions/
```
- 改版使用 `v4`
```diff
index 5240cca..7056a1f 100644
--- a/.github/workflows/lunch-screenshot.yml
+++ b/.github/workflows/lunch-screenshot.yml
@@ -18,7 +18,7 @@ jobs:
       with:
         url: https://fatraceschool.k12ea.gov.tw/frontend/search.html?school=64736003
         devices: iPad Pro landscape
-    - uses: actions/upload-artifact@v2
+    - uses: actions/upload-artifact@v4
```

## 2024-10-31

- ( 2024-10-31 00:46:20 )
- 修改 workflow ，先測看看手動觸發是否正常。
- 順便實驗一下，如果 `on` 的條件有兩個，會發生什麼事？
```diff
--- a/.github/workflows/lunch-screenshot.yml
+++ b/.github/workflows/lunch-screenshot.yml
@@ -4,13 +4,20 @@ on:
   schedule:
     # Runs "" (see https://crontab.guru)
     - cron: '30 4 * * 1-5'
+  workflow_dispatch:
+    inputs:
+      url:
+        description: 'The website URL (ex: https://www.google.com/)'
+        required: true
+        default: ''
```
- 結果：
  - (1) `schedule` 跟 `workflow_dispatch` 是可以同時存在的
  - (2) `screenshots-ci-action` 並無法成功運作 - 原因待查
```js
start process desktop
  Processing desktop screenshot
  Error: net::ERR_CONNECTION_CLOSED at https://fatraceschool.k12ea.gov.tw/frontend/search.html?school=64736003
  Error: net::ERR_CONNECTION_CLOSED at https://fatraceschool.k12ea.gov.tw/frontend/search.html?school=64736003
      at navigate (/home/runner/work/_actions/flameddd/screenshots-ci-action/master/dist/index.js:1:1482176)
      at process.processTicksAndRejections (node:internal/process/task_queues:95:5)
      at async FrameManager.navigateFrame (/home/runner/work/_actions/flameddd/screenshots-ci-action/master/dist/index.js:1:1481758)
      at async Frame.goto (/home/runner/work/_actions/flameddd/screenshots-ci-action/master/dist/index.js:1:1487252)
      at async Page.goto (/home/runner/work/_actions/flameddd/screenshots-ci-action/master/dist/index.js:1:704323)
      at async run (/home/runner/work/_actions/flameddd/screenshots-ci-action/master/dist/index.js:1:233557)
```
![2024-10-31_screenshot_github_action_error](https://i.imgur.com/GV29YhP.png)