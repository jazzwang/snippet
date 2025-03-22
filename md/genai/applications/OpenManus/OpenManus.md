# OpenManus

- Git Repo:
  - https://github.com/mannaandpoem/OpenManus
- Document
  - https://openmanus.github.io/

## 2025-03-22

- 參考：[OpenManus 教學：快速打造專屬 AI Agent 實戰指南](https://medium.com/@cch.chichieh/openmanus-tutorial-8918612ba642)
- 看了一下 https://github.com/mannaandpoem/OpenManus 的影片，
  大致上概念是只要給一段簡單的 Prompt 描述，
  然後讓 LLM 去調用 Tool 完成工作（e.g. SEO 分析報告）。

### Install 安裝

- 官方大致上都是靠 `venv` 來達成目的，不管是靠 `pip` 或 `uv`。
  初步感覺還沒有寫成 command line 界面，所以就不必測試 `uv tool` 指令。
- 那就中規中矩照官方文件說明，用 `uv` 生成 `venv` 然後 checkout git repo 安裝
- ( 2025-03-22 10:57:01 )
```bash
jazzw@JazzBook:~/git/snippet/md/genai/applications/OpenManus$ uv venv --python 3.12
Using CPython 3.12.9
Creating virtual environment at: .venv
Activate with: .venv\Scripts\activate
jazzw@JazzBook:~/git/snippet/md/genai/applications/OpenManus$ source .venv/Scripts/activate
(OpenManus) jazzw@JazzBook:~/git/snippet/md/genai/applications/OpenManus$ git clone https://github.com/mannaandpoem/OpenManus.git
(OpenManus) jazzw@JazzBook:~/git/snippet/md/genai/applications/OpenManus/OpenManus$ uv pip install -r requirements.txt
```
- ( 2025-03-22 11:01:42 )
- 由於有查到 https://pypi.org/project/openmanus/ 所以也可以簡單用 `uv pip install openmanus` 完成安裝
```bash
(OpenManus) jazzw@JazzBook:~/git/snippet/md/genai/applications/OpenManus$ uv pip install openmanus
```
- ( 2025-03-22 11:04:02 )
- 實測 `uv tool` 確認沒辦法產生 execution
```bash
(OpenManus) jazzw@JazzBook:~/git/snippet/md/genai/applications/OpenManus$ deactivate 
jazzw@JazzBook:~/git/snippet/md/genai/applications/OpenManus$ uv tool install --force --python python3.12 openmanus
Resolved 1 package in 4ms
Installed 1 package in 16ms
 + openmanus==0.1.0
No executables are provided by `openmanus`
```

### Quick Start 快速開始

- ( 2025-03-22 11:05:49 )
- 乖乖地先照官方文件說明，設定 `config/config.toml`
```bash
jazzw@JazzBook:~/git/snippet/md/genai/applications/OpenManus$ source .venv/Scripts/activate
(OpenManus) jazzw@JazzBook:~/git/snippet/md/genai/applications/OpenManus$ cd OpenManus
(OpenManus) jazzw@JazzBook:~/git/snippet/md/genai/applications/OpenManus/OpenManus$ cp config/config.example.toml config/config.toml
```
- 想測試看看調用本地端模型，所以先測試一下 `qwen2.5-coder`
```
(OpenManus) jazzw@JazzBook:~/git/snippet/md/genai/applications/OpenManus/OpenManus$ ollama list
NAME                            ID              SIZE      MODIFIED     
qwen2.5-coder:latest            2b0496514337    4.7 GB    44 hours ago    
qwen25-7b-instruct-1m:q4_k_m    80b818033c9f    4.7 GB    13 days ago 
(OpenManus) jazzw@JazzBook:~/git/snippet/md/genai/applications/OpenManus/OpenManus$ cat config/config.toml 
[llm] #OLLAMA:
api_type = 'ollama'
model = "qwen2.5-coder"
base_url = "http://localhost:11434/v1"
api_key = "ollama"
max_tokens = 4096
temperature = 0.0
(OpenManus) jazzw@JazzBook:~/git/snippet/md/genai/applications/OpenManus/OpenManus$ 
```
- 因為牽涉到 Tool Function Calling，也許沒辦法辦到。
  - https://github.com/ollama/ollama/issues/6007 有討論到 Ollama 整合 Qwen 2.5 的可能性，已經在 2024 九月標為 `CLOSED`
    > jmorganca on Sep 11, 2024
    > Hi folks sorry for the delay. Qwen2 has been updated with the recommended system prompt, 
    > as well as the nous-style tool calling from the Qwen-Agent repo https://ollama.com/library/qwen2
  - 看起來跟 `system propmt` 有關，其次就是呼叫 `Qwen-Agent`。就姑且試試看吧～
- ( 2025-03-22 11:27:01 )
- 先測試簡易版
```bash
(OpenManus) jazzw@JazzBook:~/git/snippet/md/genai/applications/OpenManus/OpenManus$ python main.py
(OpenManus) jazzw@JazzBook:~/git/snippet/md/genai/applications/OpenManus/OpenManus$ python main.py
INFO     [browser_use] BrowserUse logging setup complete with level info
INFO     [root] Anonymized telemetry enabled. See https://docs.browser-use.com/development/telemetry for more information.
Enter your prompt: 幫我查詢明天台灣各縣市的溫度與濕度，並整理成 txt 儲存下來
2025-03-22 11:29:58.564 | WARNING  | __main__:main:15 - Processing your request...
2025-03-22 11:29:58.565 | INFO     | app.agent.base:run:140 - Executing step 1/20
2025-03-22 11:30:20.941 | INFO     | app.llm:update_token_count:250 - Token usage: Input=1820, Completion=612, Cumulative Input=1820, Cumulative Completion=612, Total=2432, Cumulative Total=2432
2025-03-22 11:30:20.941 | INFO     | app.agent.toolcall:think:80 - ✨ Manus's thoughts: 
2025-03-22 11:30:20.941 | INFO     | app.agent.toolcall:think:81 - 🛠️ Manus selected 5 tools to use
2025-03-22 11:30:20.941 | INFO     | app.agent.toolcall:think:85 - 🧰 Tools being prepared: ['browser_use', 'browser_use', 'str_replace', 'str_replace', 'str_replace']
2025-03-22 11:30:20.949 | INFO     | app.agent.toolcall:think:88 - 🔧 Tool arguments: {"action":"go_to_url","url":"https://www.cwb.gov.tw/V8/C/index.html"}
2025-03-22 11:30:20.951 | INFO     | app.agent.toolcall:execute_tool:179 - 🔧 Activating tool: 'browser_use'...
ERROR    [browser] Failed to initialize Playwright browser: BrowserType.launch: Executable doesn't exist at C:\Users\jazzw\AppData\Local\ms-playwright\chromium-1155\chrome-win\chrome.exe
╔════════════════════════════════════════════════════════════╗
║ Looks like Playwright was just installed or updated.       ║
║ Please run the following command to download new browsers: ║
║                                                            ║
║     playwright install                                     ║
║                                                            ║
║ <3 Playwright Team                                         ║
╚════════════════════════════════════════════════════════════╝
2025-03-22 11:30:22.572 | INFO     | app.agent.toolcall:act:149 - 🎯 Tool 'browser_use' completed its mission! Result: Observed output of cmd `browser_use` executed:
Error: Browser action 'go_to_url' failed: BrowserType.launch: Executable doesn't exist at C:\Users\jazzw\AppData\Local\ms-playwright\chromium-1155\chrome-win\chrome.exe
╔════════════════════════════════════════════════════════════╗
║ Looks like Playwright was just installed or updated.       ║
║ Please run the following command to download new browsers: ║
║                                                            ║
║     playwright install                                     ║
║                                                            ║
║ <3 Playwright Team                                         ║
╚════════════════════════════════════════════════════════════╝
2025-03-22 11:30:22.572 | INFO     | app.agent.toolcall:execute_tool:179 - 🔧 Activating tool: 'browser_use'...
ERROR    [browser] Failed to initialize Playwright browser: BrowserType.launch: Executable doesn't exist at C:\Users\jazzw\AppData\Local\ms-playwright\chromium-1155\chrome-win\chrome.exe
╔════════════════════════════════════════════════════════════╗
║ Looks like Playwright was just installed or updated.       ║
║ Please run the following command to download new browsers: ║
║                                                            ║
║     playwright install                                     ║
║                                                            ║
║ <3 Playwright Team                                         ║
╚════════════════════════════════════════════════════════════╝
2025-03-22 11:30:23.510 | INFO     | app.agent.toolcall:act:149 - 🎯 Tool 'browser_use' completed its mission! Result: Observed output of cmd `browser_use` executed:
Error: Browser action 'extract_content' failed: BrowserType.launch: Executable doesn't exist at C:\Users\jazzw\AppData\Local\ms-playwright\chromium-1155\chrome-win\chrome.exe
╔════════════════════════════════════════════════════════════╗
║ Looks like Playwright was just installed or updated.       ║
║ Please run the following command to download new browsers: ║
║                                                            ║
║     playwright install                                     ║
║                                                            ║
║ <3 Playwright Team                                         ║
╚════════════════════════════════════════════════════════════╝
2025-03-22 11:30:23.510 | INFO     | app.agent.toolcall:act:149 - 🎯 Tool 'str_replace' completed its mission! Result: Error: Unknown tool 'str_replace'
2025-03-22 11:30:23.510 | INFO     | app.agent.toolcall:act:149 - 🎯 Tool 'str_replace' completed its mission! Result: Error: Unknown tool 'str_replace'
2025-03-22 11:30:23.510 | INFO     | app.agent.toolcall:act:149 - 🎯 Tool 'str_replace' completed its mission! Result: Error: Unknown tool 'str_replace'
2025-03-22 11:30:23.510 | INFO     | app.agent.base:run:140 - Executing step 2/20
ERROR    [browser] Failed to initialize Playwright browser: BrowserType.launch: Executable doesn't exist at C:\Users\jazzw\AppData\Local\ms-playwright\chromium-1155\chrome-win\chrome.exe
╔════════════════════════════════════════════════════════════╗
║ Looks like Playwright was just installed or updated.       ║
║ Please run the following command to download new browsers: ║
║                                                            ║
║     playwright install                                     ║
║                                                            ║
║ <3 Playwright Team                                         ║
╚════════════════════════════════════════════════════════════╝
WARNING  [browser] Page load failed, continuing...
ERROR    [browser] Failed to initialize Playwright browser: BrowserType.launch: Executable doesn't exist at C:\Users\jazzw\AppData\Local\ms-playwright\chromium-1155\chrome-win\chrome.exe
╔════════════════════════════════════════════════════════════╗
║ Looks like Playwright was just installed or updated.       ║
║ Please run the following command to download new browsers: ║
║                                                            ║
║     playwright install                                     ║
║                                                            ║
║ <3 Playwright Team                                         ║
╚════════════════════════════════════════════════════════════╝
2025-03-22 11:30:30.432 | INFO     | app.llm:update_token_count:250 - Token usage: Input=2015, Completion=159, Cumulative Input=3835, Cumulative Completion=771, Total=2174, Cumulative Total=4606
2025-03-22 11:30:30.432 | INFO     | app.agent.toolcall:think:80 - ✨ Manus's thoughts: It seems that Playwright, which is a tool used for automating web browsers, is not properly installed on your system. The error message indicates that the executable file for Chromium does not exist at the specified path.

To resolve this issue, you need to install the necessary browsers using Playwright. You can do this by running the following command in your terminal or command prompt:

```sh
playwright install
```

This command will download and set up the required browsers (Chromium, Firefox, WebKit) for you.

Once you have installed the browsers, you should be able to use the `browser_use` tool with the `extract_content` action without encountering the error. If you encounter any further issues or need assistance with specific browser interactions, feel free to let me know!
2025-03-22 11:30:30.433 | INFO     | app.agent.toolcall:think:81 - 🛠️ Manus selected 0 tools to use
2025-03-22 11:30:30.433 | INFO     | app.agent.base:run:140 - Executing step 3/20
ERROR    [browser] Failed to initialize Playwright browser: BrowserType.launch: Executable doesn't exist at C:\Users\jazzw\AppData\Local\ms-playwright\chromium-1155\chrome-win\chrome.exe
╔════════════════════════════════════════════════════════════╗
║ Looks like Playwright was just installed or updated.       ║
║ Please run the following command to download new browsers: ║
║                                                            ║
║     playwright install                                     ║
║                                                            ║
║ <3 Playwright Team                                         ║
╚════════════════════════════════════════════════════════════╝
WARNING  [browser] Page load failed, continuing...
ERROR    [browser] Failed to initialize Playwright browser: BrowserType.launch: Executable doesn't exist at C:\Users\jazzw\AppData\Local\ms-playwright\chromium-1155\chrome-win\chrome.exe
╔════════════════════════════════════════════════════════════╗
║ Looks like Playwright was just installed or updated.       ║
║ Please run the following command to download new browsers: ║
║                                                            ║
║     playwright install                                     ║
║                                                            ║
║ <3 Playwright Team                                         ║
╚════════════════════════════════════════════════════════════╝
2025-03-22 11:30:36.101 | INFO     | app.llm:update_token_count:250 - Token usage: Input=1958, Completion=108, Cumulative Input=5793, Cumulative Completion=879, Total=2066, Cumulative Total=6672
2025-03-22 11:30:36.102 | INFO     | app.agent.toolcall:think:80 - ✨ Manus's thoughts: 
2025-03-22 11:30:36.102 | INFO     | app.agent.toolcall:think:81 - 🛠️ Manus selected 1 tools to use
2025-03-22 11:30:36.103 | INFO     | app.agent.toolcall:think:85 - 🧰 Tools being prepared: ['browser_use']
2025-03-22 11:30:36.103 | INFO     | app.agent.toolcall:think:88 - 🔧 Tool arguments: {"action":"go_to_url","url":"\u003cyour-url-here\u003e"}
2025-03-22 11:30:36.103 | INFO     | app.agent.toolcall:execute_tool:179 - 🔧 Activating tool: 'browser_use'...
ERROR    [browser] Failed to initialize Playwright browser: BrowserType.launch: Executable doesn't exist at C:\Users\jazzw\AppData\Local\ms-playwright\chromium-1155\chrome-win\chrome.exe
╔════════════════════════════════════════════════════════════╗
║ Looks like Playwright was just installed or updated.       ║
║ Please run the following command to download new browsers: ║
║                                                            ║
║     playwright install                                     ║
║                                                            ║
║ <3 Playwright Team                                         ║
╚════════════════════════════════════════════════════════════╝
2025-03-22 11:30:36.992 | INFO     | app.agent.toolcall:act:149 - 🎯 Tool 'browser_use' completed its mission! Result: Observed output of cmd `browser_use` executed:
Error: Browser action 'go_to_url' failed: BrowserType.launch: Executable doesn't exist at C:\Users\jazzw\AppData\Local\ms-playwright\chromium-1155\chrome-win\chrome.exe
╔════════════════════════════════════════════════════════════╗
║ Looks like Playwright was just installed or updated.       ║
║ Please run the following command to download new browsers: ║
║                                                            ║
║     playwright install                                     ║
║                                                            ║
║ <3 Playwright Team                                         ║
╚════════════════════════════════════════════════════════════╝
2025-03-22 11:30:36.992 | INFO     | app.agent.base:run:140 - Executing step 4/20
```
- 參考 [指南](https://medium.com/@cch.chichieh/openmanus-tutorial-8918612ba642)，這裡試跑以下的 Prompt (微調「天氣」成「溫度與濕度」)
```
幫我查詢明天台灣各縣市的溫度與濕度，並整理成 txt 儲存下來
```
- 錯誤是 playwright 沒安裝。確實，這個 `venv` 還沒有裝 playwright 的瀏覽器，手動補一下，不然等它 20 步跑完都報一樣的錯，沒啥意思。
```
(OpenManus) jazzw@JazzBook:~/git/snippet/md/genai/applications/OpenManus/OpenManus$ uv pip install playwright
Using Python 3.12.9 environment at: C:\Users\jazzw\git\snippet\md\genai\applications\OpenManus\.venv
Audited 1 package in 13ms
(OpenManus) jazzw@JazzBook:~/git/snippet/md/genai/applications/OpenManus/OpenManus$ which playwright
/c/Users/jazzw/git/snippet/md/genai/applications/OpenManus/.venv/Scripts/playwright
(OpenManus) jazzw@JazzBook:~/git/snippet/md/genai/applications/OpenManus/OpenManus$ playwright install -h
Usage: playwright install [options] [browser...]

ensure browsers necessary for this version of Playwright are installed

Options:
  --with-deps   install system dependencies for browsers
  --dry-run     do not execute installation, only print information
  --force       force reinstall of stable browser channels
  --only-shell  only install headless shell when installing chromium
  --no-shell    do not install chromium headless shell
  -h, --help    display help for command


Examples:
  - $ install
    Install default browsers.

  - $ install chrome firefox
    Install custom browsers, supports chromium, chromium-headless-shell, chromium-tip-of-tree-headless-shell, chrome, chrome-beta, msedge, msedge-beta, msedge-dev, bidi-chromium, firefox, webkit.
(OpenManus) jazzw@JazzBook:~/git/snippet/md/genai/applications/OpenManus/OpenManus$ playwright install chromium
Downloading Chromium 133.0.6943.16 (playwright build v1155) from https://cdn.playwright.dev/dbazure/download/playwright/builds/chromium/1155/chromium-win64.zip
140 MiB [=======             ] 35% 53.0s

(後略)
```
- ( 2025-03-22 11:37:50 )
- 再跑一次，確實第一頁有跑對中央氣象局，但很可惜該網址已經失效。所以它就跑去問 Google 怎麼達成目標，然後就卡在奇怪的地方了。
- 初步估計是因為 Qwen 2.5 Coder 的知識庫比較舊，所以沒找到正確的網址。
```bash
(OpenManus) jazzw@JazzBook:~/git/snippet/md/genai/applications/OpenManus/OpenManus$ python main.py
INFO     [browser_use] BrowserUse logging setup complete with level info
INFO     [root] Anonymized telemetry enabled. See https://docs.browser-use.com/development/telemetry for more information.
Enter your prompt: 幫我查詢明天台灣各縣市的溫度與濕度，並整理成 txt 儲存下來
2025-03-22 11:44:54.422 | WARNING  | __main__:main:15 - Processing your request...
2025-03-22 11:44:54.422 | INFO     | app.agent.base:run:140 - Executing step 1/20
2025-03-22 11:45:12.826 | INFO     | app.llm:update_token_count:250 - Token usage: Input=1820, Completion=612, Cumulative Input=1820, Cumulative Completion=612, Total=2432, Cumulative Total=2432
2025-03-22 11:45:12.826 | INFO     | app.agent.toolcall:think:80 - ✨ Manus's thoughts: 
2025-03-22 11:45:12.826 | INFO     | app.agent.toolcall:think:81 - 🛠️ Manus selected 5 tools to use
2025-03-22 11:45:12.832 | INFO     | app.agent.toolcall:think:85 - 🧰 Tools being prepared: ['browser_use', 'browser_use', 'str_replace', 'str_replace', 'str_replace']
2025-03-22 11:45:12.832 | INFO     | app.agent.toolcall:think:88 - 🔧 Tool arguments: {"action":"go_to_url","url":"https://www.cwb.gov.tw/V8/C/index.html"}
2025-03-22 11:45:12.833 | INFO     | app.agent.toolcall:execute_tool:179 - 🔧 Activating tool: 'browser_use'...
2025-03-22 11:45:14.998 | INFO     | app.agent.toolcall:act:149 - 🎯 Tool 'browser_use' completed its mission! Result: Observed output of cmd `browser_use` executed:
Error: Browser action 'go_to_url' failed: Page.goto: net::ERR_NAME_NOT_RESOLVED at https://www.cwb.gov.tw/V8/C/index.html
Call log:
  - navigating to "https://www.cwb.gov.tw/V8/C/index.html", waiting until "load"

2025-03-22 11:45:14.999 | INFO     | app.agent.toolcall:execute_tool:179 - 🔧 Activating tool: 'browser_use'...
2025-03-22 11:45:15.096 | INFO     | app.agent.toolcall:act:149 - 🎯 Tool 'browser_use' completed its mission! Result: Observed output of cmd `browser_use` executed:
Error: Failed to extract content: Page.content: Unable to retrieve content because the page is navigating and changing the content.
2025-03-22 11:45:15.096 | INFO     | app.agent.toolcall:act:149 - 🎯 Tool 'str_replace' completed its mission! Result: Error: Unknown tool 'str_replace'
2025-03-22 11:45:15.100 | INFO     | app.agent.toolcall:act:149 - 🎯 Tool 'str_replace' completed its mission! Result: Error: Unknown tool 'str_replace'
2025-03-22 11:45:15.100 | INFO     | app.agent.toolcall:act:149 - 🎯 Tool 'str_replace' completed its mission! Result: Error: Unknown tool 'str_replace'
2025-03-22 11:45:15.101 | INFO     | app.agent.base:run:140 - Executing step 2/20
2025-03-22 11:45:22.858 | INFO     | app.llm:update_token_count:250 - Token usage: Input=1977, Completion=225, Cumulative Input=3797, Cumulative Completion=837, Total=2202, Cumulative Total=4634
2025-03-22 11:45:22.858 | INFO     | app.agent.toolcall:think:80 - ✨ Manus's thoughts: 
2025-03-22 11:45:22.858 | INFO     | app.agent.toolcall:think:81 - 🛠️ Manus selected 2 tools to use
2025-03-22 11:45:22.860 | INFO     | app.agent.toolcall:think:85 - 🧰 Tools being prepared: ['browser_use', 'browser_use']
2025-03-22 11:45:22.860 | INFO     | app.agent.toolcall:think:88 - 🔧 Tool arguments: {"action":"go_to_url","url":"https://www.google.com"}
2025-03-22 11:45:22.860 | INFO     | app.agent.toolcall:execute_tool:179 - 🔧 Activating tool: 'browser_use'...
2025-03-22 11:45:24.396 | INFO     | app.agent.toolcall:act:149 - 🎯 Tool 'browser_use' completed its mission! Result: Observed output of cmd `browser_use` executed:
Navigated to https://www.google.com
2025-03-22 11:45:24.396 | INFO     | app.agent.toolcall:execute_tool:179 - 🔧 Activating tool: 'browser_use'...
2025-03-22 11:45:25.825 | INFO     | app.llm:update_token_count:250 - Token usage: Input=872, Completion=38, Cumulative Input=4669, Cumulative Completion=875, Total=910, Cumulative Total=5544
2025-03-22 11:45:25.825 | INFO     | app.agent.toolcall:act:149 - 🎯 Tool 'browser_use' completed its mission! Result: Observed output of cmd `browser_use` executed:
Extracted from page:
{
  "title": "Google"
}

2025-03-22 11:45:25.825 | INFO     | app.agent.base:run:140 - Executing step 3/20
2025-03-22 11:45:30.569 | INFO     | app.llm:update_token_count:250 - Token usage: Input=1884, Completion=106, Cumulative Input=6553, Cumulative Completion=981, Total=1990, Cumulative Total=7534
2025-03-22 11:45:30.569 | INFO     | app.agent.toolcall:think:80 - ✨ Manus's thoughts: 
2025-03-22 11:45:30.569 | INFO     | app.agent.toolcall:think:81 - 🛠️ Manus selected 1 tools to use
2025-03-22 11:45:30.571 | INFO     | app.agent.toolcall:think:85 - 🧰 Tools being prepared: ['browser_use']
2025-03-22 11:45:30.571 | INFO     | app.agent.toolcall:think:88 - 🔧 Tool arguments: {"action":"web_search","query":"important items related to my goal"}
2025-03-22 11:45:30.571 | INFO     | app.agent.toolcall:execute_tool:179 - 🔧 Activating tool: 'browser_use'...
2025-03-22 11:45:30.571 | INFO     | app.tool.web_search:_try_all_engines:104 - 🔎 Attempting search with Google...
2025-03-22 11:45:34.154 | INFO     | app.agent.toolcall:act:149 - 🎯 Tool 'browser_use' completed its mission! Result: Observed output of cmd `browser_use` executed:
Searched for 'important items related to my goal' and navigated to first result: https://www.indeed.com/career-advice/career-development/list-of-goals-set-for-yourself
All results:https://www.indeed.com/career-advice/career-development/list-of-goals-set-for-yourself
https://www.linkedin.com/pulse/7-most-important-elements-achieving-goals-alba-vsese
https://www.quora.com/What-is-the-most-important-thing-to-have-to-succeed-at-your-goals
https://positivepsychology.com/benefits-goal-setting/
https://jamesclear.com/goals-systems
https://medium.com/@ForcingFunction/choosing-goals-how-to-figure-out-what-you-really-want-101ae562a560
https://humaninprogress.com/15-ways-to-achieve-your-goals/
https://www.mindtools.com/a4wo118/smart-goals
https://markmanson.net/goal-setting
https://www.betterup.com/blog/how-to-set-goals-and-achieve-them
2025-03-22 11:45:34.155 | INFO     | app.agent.base:run:140 - Executing step 4/20
2025-03-22 11:45:39.330 | INFO     | app.llm:update_token_count:250 - Token usage: Input=1854, Completion=87, Cumulative Input=8407, Cumulative Completion=1068, Total=1941, Cumulative Total=9475
2025-03-22 11:45:39.332 | INFO     | app.agent.toolcall:think:80 - ✨ Manus's thoughts: 
2025-03-22 11:45:39.332 | INFO     | app.agent.toolcall:think:81 - 🛠️ Manus selected 1 tools to use
2025-03-22 11:45:39.332 | INFO     | app.agent.toolcall:think:85 - 🧰 Tools being prepared: ['browser_use']
2025-03-22 11:45:39.332 | INFO     | app.agent.toolcall:think:88 - 🔧 Tool arguments: {"action":"extract_content","goal":"all company names, a specific description, all information about links with companies in structured format or simply links"}
2025-03-22 11:45:39.332 | INFO     | app.agent.toolcall:execute_tool:179 - 🔧 Activating tool: 'browser_use'...
2025-03-22 11:45:42.618 | INFO     | app.llm:update_token_count:250 - Token usage: Input=2048, Completion=82, Cumulative Input=10455, Cumulative Completion=1150, Total=2130, Cumulative Total=11605
2025-03-22 11:45:42.618 | INFO     | app.agent.toolcall:act:149 - 🎯 Tool 'browser_use' completed its mission! Result: Observed output of cmd `browser_use` executed:
No content was extracted from the page.
2025-03-22 11:45:42.618 | INFO     | app.agent.base:run:140 - Executing step 5/20
2025-03-22 11:45:47.302 | INFO     | app.llm:update_token_count:250 - Token usage: Input=1891, Completion=84, Cumulative Input=12346, Cumulative Completion=1234, Total=1975, Cumulative Total=13580
2025-03-22 11:45:47.302 | INFO     | app.agent.toolcall:think:80 - ✨ Manus's thoughts: 
2025-03-22 11:45:47.302 | INFO     | app.agent.toolcall:think:81 - 🛠️ Manus selected 1 tools to use
2025-03-22 11:45:47.302 | INFO     | app.agent.toolcall:think:85 - 🧰 Tools being prepared: ['browser_use']
2025-03-22 11:45:47.302 | INFO     | app.agent.toolcall:think:88 - 🔧 Tool arguments: {"action":"extract_content","goal":"list of goals"}
2025-03-22 11:45:47.302 | INFO     | app.agent.toolcall:execute_tool:179 - 🔧 Activating tool: 'browser_use'...
2025-03-22 11:45:50.497 | INFO     | app.llm:update_token_count:250 - Token usage: Input=2048, Completion=82, Cumulative Input=14394, Cumulative Completion=1316, Total=2130, Cumulative Total=15710
2025-03-22 11:45:50.497 | INFO     | app.agent.toolcall:act:149 - 🎯 Tool 'browser_use' completed its mission! Result: Observed output of cmd `browser_use` executed:
```
- 觀察：
  - 從 OpenManus 開啟的 Chromiun 頁面上看到許多影像辨識的標記，蠻特別的。代表背後的想法是去辨識瀏覽器的內容，嘗試看要點擊哪裡。這也難怪需要設置 vision 模型。
  - 感覺如果是用推理模型，或許能力會再更精準一點。然後搭配多模態的模型，支援 vision 的辨識。確實有機會解決一些工作上的流程自動化。
- 想法：
  - 這對於爬取公開資料來解決問題，或許有用。但是如果是需要調用內部資料，光是身份認證這一段，相信還是有其侷限性。

### 實驗一：寫程式

- ( 2025-03-22 11:57:04 )
- 實驗 Prompt:
```
可以幫我寫一個 python 程式，調用 playwright，爬取 https://cwiki.apache.org/confluence/display/hadoop 的頁面，並轉成 Markdown 檔案存起來？
```bash
(OpenManus) jazzw@JazzBook:~/git/snippet/md/genai/applications/OpenManus/OpenManus$ python main.py
INFO     [browser_use] BrowserUse logging setup complete with level info
INFO     [root] Anonymized telemetry enabled. See https://docs.browser-use.com/development/telemetry for more information.
Enter your prompt: 可以幫我寫一個 python 程式，調用 playwright，爬取 https://cwiki.apache.org/confluence/display/hadoop 的頁面，並轉成 Markdown 檔案存起來？
2025-03-22 11:56:53.902 | WARNING  | __main__:main:15 - Processing your request...
2025-03-22 11:56:53.903 | INFO     | app.agent.base:run:140 - Executing step 1/20
2025-03-22 11:57:06.853 | INFO     | app.llm:update_token_count:250 - Token usage: Input=1839, Completion=382, Cumulative Input=1839, Cumulative Completion=382, Total=2221, Cumulative Total=2221
2025-03-22 11:57:06.854 | INFO     | app.agent.toolcall:think:80 - ✨ Manus's thoughts: 
2025-03-22 11:57:06.855 | INFO     | app.agent.toolcall:think:81 - 🛠️ Manus selected 5 tools to use
2025-03-22 11:57:06.856 | INFO     | app.agent.toolcall:think:85 - 🧰 Tools being prepared: ['browser_use', 'browser_use', 'str_replace_editor', 'str_replace_editor', 'terminate']      
2025-03-22 11:57:06.858 | INFO     | app.agent.toolcall:think:88 - 🔧 Tool arguments: {"action":"go_to_url","url":"https://cwiki.apache.org/confluence/display/hadoop"}
2025-03-22 11:57:06.859 | INFO     | app.agent.toolcall:execute_tool:179 - 🔧 Activating tool: 'browser_use'...
2025-03-22 11:57:35.857 | INFO     | app.agent.toolcall:act:149 - 🎯 Tool 'browser_use' completed its mission! Result: Observed output of cmd `browser_use` executed:
Navigated to https://cwiki.apache.org/confluence/display/hadoop
2025-03-22 11:57:35.857 | INFO     | app.agent.toolcall:execute_tool:179 - 🔧 Activating tool: 'browser_use'...
2025-03-22 11:57:43.984 | INFO     | app.llm:update_token_count:250 - Token usage: Input=2048, Completion=279, Cumulative Input=3887, Cumulative Completion=661, Total=2327, Cumulative Total=4548
2025-03-22 11:57:43.984 | INFO     | app.agent.toolcall:act:149 - 🎯 Tool 'browser_use' completed its mission! Result: Observed output of cmd `browser_use` executed:
No content was extracted from the page.
2025-03-22 11:57:43.984 | INFO     | app.agent.toolcall:execute_tool:179 - 🔧 Activating tool: 'str_replace_editor'...
2025-03-22 11:57:43.984 | INFO     | app.agent.toolcall:act:149 - 🎯 Tool 'str_replace_editor' completed its mission! Result: Observed output of cmd `str_replace_editor` executed:      
File created successfully at: C:\Users\jazzw\git\snippet\md\hadoop_page.md
2025-03-22 11:57:43.984 | INFO     | app.agent.toolcall:execute_tool:179 - 🔧 Activating tool: 'str_replace_editor'...
2025-03-22 11:57:43.989 | INFO     | app.agent.toolcall:act:149 - 🎯 Tool 'str_replace_editor' completed its mission! Result: Observed output of cmd `str_replace_editor` executed:      
The file C:\Users\jazzw\git\snippet\md\hadoop_page.md has been edited. Here's the result of running `cat -n` on a snippet of the edited file:
     1
     2  <page_content>
Review the changes and make sure they are as expected (correct indentation, no duplicate lines, etc). Edit the file again if necessary.
2025-03-22 11:57:43.989 | INFO     | app.agent.toolcall:execute_tool:179 - 🔧 Activating tool: 'terminate'...
2025-03-22 11:57:44.282 | INFO     | app.agent.toolcall:_handle_special_tool:224 - 🏁 Special tool 'terminate' has completed the task!
2025-03-22 11:57:44.282 | INFO     | app.agent.toolcall:act:149 - 🎯 Tool 'terminate' completed its mission! Result: Observed output of cmd `terminate` executed:
The interaction has been completed with status: success
2025-03-22 11:57:44.282 | INFO     | __main__:main:17 - Request processing completed.
```
- 確實有看到產出
```bash
2025-03-22 11:57:43.984 | INFO     | app.agent.toolcall:act:149 - 🎯 Tool 'str_replace_editor' completed its mission! Result: Observed output of cmd `str_replace_editor` executed:      
File created successfully at: C:\Users\jazzw\git\snippet\md\hadoop_page.md
```
- 不過內容挺慘的
```bash
(OpenManus) jazzw@JazzBook:~/git/snippet/md/genai/applications/OpenManus/OpenManus/logs$ cat ~/git/snippet/md/hadoop_page.md

<page_content>
```
- 小結：
  - 根據初步測試 Local Ollama Model 的結果，產出效果不佳。看起來可能還是要仰賴比較強大的 LLM，像是 OpenAI, Claude 或 Gemini 等。
  - 觀察到執行的 log 可以在 `OpenManus/logs` 底下找到。
    ```bash
    (OpenManus) jazzw@JazzBook:~/git/snippet/md/genai/applications/OpenManus/OpenManus/logs$ ls -al
    total 49
    drwxr-xr-x 1 jazzw 197609     0 三月   22 11:55 .
    drwxr-xr-x 1 jazzw 197609     0 三月   22 11:28 ..
    -rw-r--r-- 1 jazzw 197609    80 三月   22 11:28 20250322112842.log
    -rw-r--r-- 1 jazzw 197609 12474 三月   22 11:30 20250322112907.log
    -rw-r--r-- 1 jazzw 197609 13709 三月   22 11:46 20250322114437.log
    -rw-r--r-- 1 jazzw 197609  3474 三月   22 11:57 20250322115507.log
    ```
  - OpenManus 有點類似 OpenHands，也會有 `workspace`，不過看起來執行時並沒有用到，反而是以 git repo 的根目錄為主。
    這也是為何把生成的 markdown 檔案放在 `~/git/snippet/md/hadoop_page.md` ，
    而非 `~/git/snippet/md/applications/OpenManus/OpenManus/workspace/hadoop_page.md`
- ( 2025-03-22 13:28:50 )
- 初步先測試到這邊。相信一些簡單的工作，或許 OpenManus 可以辦得到。
  不過以程式生成而言，我還是比較喜歡 `aider` 跟 `openhands`。至少會拿到一個可重複執行的成果，而不是單一產出。

### Cleanup 清理實驗環境

```bash
jazzw@JazzBook:~/git/snippet/md/genai/applications/OpenManus$ rm -rf .venv/
jazzw@JazzBook:~/git/snippet/md/genai/applications/OpenManus$ rm -rf OpenManus
jazzw@JazzBook:~/git/snippet/md/genai/applications/OpenManus$ git add OpenManus.md
jazzw@JazzBook:~/git/snippet/md/genai/applications/OpenManus$ git commit -a -m "docs: [md][genai][applications][OpenManus] test OpenManus from scratch."
```

### 補充: WebUI

- https://github.com/YunQiAI/OpenManusWeb 
- https://github.com/Shybert-AI/OpenManus-WebUI
