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
(env) jazzw@JazzBook:~/git/snippet/py/playwright$ code MEMO.md
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