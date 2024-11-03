# playwright

> Playwright enables reliable end-to-end testing for modern web apps.

- https://playwright.dev/
- Git Repo: https://github.com/microsoft/playwright

## 2024-11-03

- https://playwright.dev/python/docs/intro

### Installation

- 測試環境：Github Codespace
```bash
jazzw@JazzBook:~/git/snippet$ gh cs code
? Choose codespace: jazzwang/snippet (master*): snippet
```
- ( 2024-11-03 09:16:08 )
- 根據測試 JavaScript 版本的經驗，切到 `/tmp` 目錄做實驗：
```bash
@jazzwang ➜ /workspaces/snippet (master) $ cd /tmp/
@jazzwang ➜ /tmp $ pip install pytest-playwright
@jazzwang ➜ /tmp $ playwright install
@jazzwang ➜ /tmp $ playwright ^C
@jazzwang ➜ /tmp $ playwright install
@jazzwang ➜ /tmp $ 
@jazzwang ➜ /tmp $ cat > test_example.py << EOF
import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
EOF
@jazzwang ➜ /tmp $ pytest
======================================================================== test session starts =========================================================================
platform linux -- Python 3.10.13, pytest-8.3.3, pluggy-1.5.0
rootdir: /tmp
plugins: anyio-4.3.0, playwright-0.5.2, base-url-2.1.0
collected 2 items                                                                                                                                                    

test_example.py 
..                                                                                                                                             [100%]

========================================================================= 2 passed in 8.94s ==========================================================================
```
- ( 2024-11-03 09:30:46 )
- 本來想找類似 `npx playwright show-report` 的指令，不過看樣子應該得看 `pytest` 的設計怎麼產生報表。初步在目錄裡沒有找到報告。
```bash
@jazzwang ➜ /tmp $ ls -al
total 36
drwxr-xrwt+ 4 root      root       4096 Nov  3 09:25 .
drwxr-xr-x  1 root      root       4096 Apr 14  2024 ..
drwxr-xr-x+ 3 codespace codespace  4096 Nov  3 09:22 .pytest_cache
drwxr-xrw-+ 2 codespace codespace  4096 Nov  3 09:22 __pycache__
-rw-r--rw-  1 root      root      10811 Nov  3 09:16 dockerd.log
-rw-r--rw-  1 root      root         57 Nov  3 09:16 sshd.log
-rw-r--rw-  1 codespace codespace   553 Nov  3 09:21 test_example.py
srwxr-xr--  1 codespace codespace     0 Nov  3 09:15 vscode-git-f83137f03e.sock
srwxr-xr--  1 codespace codespace     0 Nov  3 09:15 vscode-ipc-078b1a70-dc0c-4927-9c59-6b374b3ad1f3.sock
srwxr-xr--  1 codespace codespace     0 Nov  3 09:15 vscode-ipc-2e9633f1-c426-4ff8-b512-0493ed38de41.sock
```
