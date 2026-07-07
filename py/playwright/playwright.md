# Playwright (Python)

## 2025-03-05

### Installation

- test on Windows 11 laptop
```bash
jazzw@JazzBook:~$ source ~/git/confluence-insight/env/Scripts/activate
(env) jazzw@JazzBook:~$ cd git/snippet/py/
(env) jazzw@JazzBook:~/git/snippet/py$ mkdir playwright
(env) jazzw@JazzBook:~/git/snippet/py$ cd playwright/
(env) jazzw@JazzBook:~/git/snippet/py/playwright$ ls
(env) jazzw@JazzBook:~/git/snippet/py/playwright$ code playwright.md
(env) jazzw@JazzBook:~/git/snippet/py/playwright$ pip3 install playwright
(env) jazzw@JazzBook:~/git/snippet/py/playwright$ playwright install
(env) jazzw@JazzBook:~/git/snippet/py/playwright$ playwright install-deps
```

### CodeGen

- testing login Amazon Kindle
```bash
(env) jazzw@JazzBook:~/git/snippet/py/playwright$ playwright codegen -b chrome https://read.amazon.com/?asin=B0DM6BHQYR
```
- example output
```python
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=1209600&openid.return_to=https%3A%2F%2Fread.amazon.com%2F%3Fasin%3DB0DM6BHQYR&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_kindle_mykindle_us&openid.mode=checkid_setup&language=en_US&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
    page.get_by_role("textbox", name="Email or mobile phone number").click()
    page.get_by_role("textbox", name="Email or mobile phone number").fill("jazz.wang@example.com") ## masked email
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("textbox", name="Password").fill("THIS_IS_MY_PASSWORD") ## masked password
    page.get_by_role("button", name="Sign in").click()
    page.get_by_role("button", name="Next page").click()
    page.get_by_role("button", name="Next page").click()
    page.get_by_role("button", name="Next page").click()
    page.get_by_role("button", name="Next page").click()
    page.get_by_role("button", name="Next page").click()
    page.get_by_role("button", name="Next page").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
```

## 2025-03-11

- Authentication
  - https://playwright.dev/python/docs/auth
- Test generator
  - https://playwright.dev/python/docs/codegen#generating-locators

## 2025-03-22

- 改用 `uv tool` 裝
```bash
jazzw@JazzBook:~/git/snippet$ uv tool install --force --python python3.12 playwright
Resolved 4 packages in 441ms
Prepared 1 package in 20.99s
Installed 4 packages in 153ms
 + greenlet==3.1.1
 + playwright==1.51.0
 + pyee==12.1.1
 + typing-extensions==4.12.2
Installed 1 executable: playwright.exe
jazzw@JazzBook:~/git/snippet$ playwright install --with-deps --no-shell chromium
Downloading Chromium 134.0.6998.35 (playwright build v1161) from https://playwright.download.prss.microsoft.com/dbazure/download/playwright/builds/chromium/1161/chromium-win64.zip
141.8 MiB [====================] 100% 0.0s
Chromium 134.0.6998.35 (playwright build v1161) downloaded to C:\Users\jazzw\AppData\Local\ms-playwright\chromium-1161
jazzw@JazzBook:~/git/snippet$ which playwright
/c/Users/jazzw/.local/bin/playwright
```

## 2025-05-23

- 目標：
  - 讀取 Jira User Profile 所有可以查到的 Activity
  - 持續捲動到最下方，並且點選 'more'
  - 關閉前，將 DOM 存成檔案
- 實作：
  - 首先，使用 `codegen` 的方式進行錄製：
  ```bash
  ~/git/snippet/py/playwright$ playwright codegen -o jira-profile.py --target=python --save-storage local-storage.json https://issues.apache.org/jira/secure/ViewProfile.jspa?name=jazzwang
  ```

## 2025-06-26

- 承襲上次用 `--save-storage` 來儲存 local storage 到 JSON 檔。也可以用 `--load-storage` 來載入已經儲存的 JSON 檔。
  ```bash
  ~/git/snippet/py/playwright$ playwright codegen -o jira-activity.py --target=python --load-storage local-storage.json https://issues.apache.org/jira/secure/ViewProfile.jspa?name=jazzwang
  ```

## 2025-07-15

- ( 2025-07-15 21:43:08 )
- 紀錄一些關於 Playwright 與 VNC 整合的相關連結：
  - [Feature] Add back support for docker and VNC #20954
    - https://github.com/microsoft/playwright/issues/20954
  - [Feature]: Docker container to run playwright in VNC for use headed mode #2648
    - https://github.com/microsoft/playwright-python/issues/2648
    - https://github.com/Grommash9/playwright_vnc

## 2025-12-10

- 實驗更換 User Agent
```bash
~/git/snippet/py/playwright$ playwright codegen -o playwright-user-agent.py --target=python --save-storage local-storage.json https://myapps.microsoft.com/
```
- 照著參考文章，補上這一段：
```diff
 def run(playwright: Playwright) -> None:
     browser = playwright.chromium.launch(headless=False)
+    ## force to use 'Chrome - Mac' user_agent string
+    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
+
+    if os.path.exists('sso-storage.json'):
+      print("[INFO] sso-storage.json found. loading into browser context.")
+      context = browser.new_context(storage_state='sso-storage.json', user_agent=user_agent)
+    else:
+      context = browser.new_context(user_agent=user_agent)
-    context = browser.new_context()
     page = context.new_page()
```
- 實際上我也可以不用手動把程式碼加上去，只要執行 `playwright codegen` 時加上 `--user-agent <ua string>` 即可。

```bash
~/git/snippet/py/playwright$ playwright.exe codegen -h
Usage: playwright codegen [options] [url]

open page and generate code for user actions

Options:
  -o, --output <file name>             saves the generated script to a file
  --target <language>                  language to generate, one of javascript, playwright-test, python, python-async, python-pytest, csharp,
                                       csharp-mstest, csharp-nunit, java, java-junit (default: "python")
  --test-id-attribute <attributeName>  use the specified attribute to generate data test ID selectors
  -b, --browser <browserType>          browser to use, one of cr, chromium, ff, firefox, wk, webkit (default: "chromium")
  --block-service-workers              block service workers
  --channel <channel>                  Chromium distribution channel, "chrome", "chrome-beta", "msedge-dev", etc
  --color-scheme <scheme>              emulate preferred color scheme, "light" or "dark"
  --device <deviceName>                emulate device, for example  "iPhone 11"
  --geolocation <coordinates>          specify geolocation coordinates, for example "37.819722,-122.478611"
  --ignore-https-errors                ignore https errors
  --load-storage <filename>            load context storage state from the file, previously saved with --save-storage
  --lang <language>                    specify language / locale, for example "en-GB"
  --proxy-server <proxy>               specify proxy server, for example "http://myproxy:3128" or "socks5://myproxy:8080"
  --proxy-bypass <bypass>              comma-separated domains to bypass proxy, for example ".com,chromium.org,.domain.com"
  --save-har <filename>                save HAR file with all network activity at the end
  --save-har-glob <glob pattern>       filter entries in the HAR by matching url against this glob pattern
  --save-storage <filename>            save context storage state at the end, for later use with --load-storage
  --timezone <time zone>               time zone to emulate, for example "Europe/Rome"
  --timeout <timeout>                  timeout for Playwright actions in milliseconds, no timeout by default
  --user-agent <ua string>             specify user agent string
  --viewport-size <size>               specify browser viewport size in pixels, for example "1280, 720"
  -h, --help                           display help for command

Examples:

  $ codegen
  $ codegen --target=python
  $ codegen -b webkit https://example.com
```

## 2026-07-07

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI Mode
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
如果我需要 AI Code Agent (如 OpenCode)參考我的瀏覽器操作,看我如何執行 Jira JQL 查詢,並將結果下載成 Excel 檔案,並且開啟 Excel,將特定區域建立新的 Excel Table,再用該 Table 產生三個固定的 Pivot Table 樞紐分析。將這個程序生成 Python 自動化程式(例如結合 Playwright 跟 Python Excel library)。可以幫我規劃 step-by-step instruction 嗎?
</td></tr><tr><td>A:</td><td>

略 -- 詳 [browser-use.md](../browser-use/browser-use.md)
</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
如何讓 OpenCode Agent 錄製 existing browser session 的操作?
</td></tr><tr><td>A:</td><td>

要讓 OpenCode Agent（或類似的 AI Code Agent、Playwright 腳本）直接接管或「錄製」你當前已經打開、登入好 Jira 的瀏覽器視窗（Existing Browser Session），最有效且能繞過 2FA 驗證的方法，就是利用 Chromium 的 遠端除錯連接埠（Remote Debugging Port）。
這樣 AI 就不需要從頭模擬登入，而是直接在你已經開好的瀏覽器中「看著你操作」並自動生成 Playwright 程式碼。
以下是具體的實作步驟：

### 第一步：完全關閉現有的 Chrome / Edge 瀏覽器

為了重啟帶有除錯功能的瀏覽器，必須先將後台所有該瀏覽器的程序（Processes）完全關閉。

### 第二步：從終端機啟動「除錯模式」的瀏覽器

打開你的終端機（Terminal 或 Command Prompt），依據你的作業系統執行以下指令，這會打開一個全新、乾淨但允許外部控制的瀏覽器視窗：

-   Windows (Chrome):
    ```bash
    "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\ChromeDebug"
    ```

-   Mac (Chrome):
    ```bash
    /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="/tmp/chrome_dev"
    ```

> 💡 重要：請在這個剛剛跳出來的新瀏覽器視窗中，手動登入你的 Jira，並切換到你要開始查詢的畫面。

### 第三步：讓 OpenCode / Playwright 接管並開始錄製

此時，該瀏覽器已經在 `9222` 連接埠（Port）等待指令 \[1\]。你可以給 OpenCode Agent 以下的指令，讓它啟動 Playwright 的錄製器（Codegen）直接連入該視窗：

### 🤖 提供給 OpenCode 的 Prompt 指令：

> "Please start the Playwright recorder to connect to my existing Chrome browser session on port 9222, and record my actions as I run a JQL query and download the Excel file. Generate a Python script from it."

### ⚙️ Agent 會在後台執行的指令：

OpenCode 收到後，會在終端機執行這行 Playwright 內建的接管錄製指令：
```
playwright codegen localhost:9222
```

執行後，你會看到 Playwright 的程式碼生成視窗（Inspector）跳出來。此時，你只要在剛剛打開的 Jira 網頁上進行以下操作：

1.  點擊 JQL 輸入框並輸入查詢。
2.  點擊 Export 按鈕。
3.  下載 Excel 檔案。

Playwright Inspector 視窗就會即時（Real-time）將你的滑鼠點擊與鍵盤輸入轉化為 Python (Playwright) 程式碼。

### 第四步：將錄製的程式碼與 Excel 自動化整合

錄製完成後，OpenCode 拿到的 Playwright 接管程式碼結構會類似這樣：
```python
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        # 連接到你已經開啟的 9222 視窗，不用重新登入
        browser = p.chromium.connect_over_cdp("http://localhost:9222")
        default_context = browser.contexts[0]
        page = default_context.pages[0]
        
        # 以下為 Playwright 自動錄製生成的點擊與下載代碼
        # page.locator("...").click()
        # with page.expect_download() as download_info:
        #     page.locator("text=Export").click()
            
        print("錄製成功，已取得網頁操作邏輯！")

run()
```

此時，你就可以叫 OpenCode 接續進行：*「請將這段錄製好的 Playwright 程式碼，與先前規劃的 pandas/openpyxl Excel 樞紐分析腳本結合成一個完整的自動化流程。」*

你想先讓 OpenCode 嘗試連線到 `9222` 連接埠並測試能否成功控制網頁，還是直接開始撰寫後續整合 Excel 處理的程式碼呢？
</td></tr>
</table>
