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