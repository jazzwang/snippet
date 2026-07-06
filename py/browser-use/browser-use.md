# browser-use

> 🌐 Make websites accessible for AI agents. Automate tasks online with ease.

- Git Repo
  - https://github.com/browser-use/browser-use
- Website
  - https://browser-use.com/
- Document
  - https://docs.browser-use.com/cloud/quickstart

## 2026-05-12

- 緣起：
  - LinkedIn
- Skill
  - https://skills.sh/browser-use/browser-use/browser-use
  ```bash
  ~$ npx skills add https://github.com/browser-use/browser-use --skill browser-use
  ```

## 2026-05-15

- Q1: 待比較 browser-use 跟 agent-browser 有什麼差異？
- A1:
<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI Mode
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
https://browser-use.com 跟 https://agent-browser.dev/ 有什麼不同？

</td></tr><tr><td>A:</td><td>

`browser-use` 與 `agent-browser` 是兩款專為 AI 智慧體（Agent）設計的瀏覽器自動化工具。它們的核心定位、架構設計與整合方式有顯著不同： [1, 2]

-   browser-use 是一個全功能 Python 開源 AI Agent 框架，專注於讓 AI 自主規劃、理解視覺截圖並執行任務。
-   [agent-browser](https://agent-browser.dev/) 則是由 Vercel Labs 推出的輕量級、命令列（CLI）優先的底層工具，旨在減少 AI 的 Token 消耗。 [1, 2, 3, 4]

### 核心差異對比

下表彙整兩者在定位、開發語言、核心機制與整合場景的直接對比：
[agent-browser](https://agent-browser.dev/)

| 比較維度 [1, 4, 5, 6, 7, 8] | browser-use |
| --- |  --- |
| 主要定位 | 完整的 AI Agent 應用框架 |
| 主導開發語言 | Python |
| AI 畫面理解機制 | 視覺截圖（Vision） + 網頁 DOM 解析 |
| Token 消耗 | 較高（需傳送圖片與複雜 DOM 脈絡） |
| 主要使用對象 | Python AI 應用、自主執行任務的 Agent 開發 |
| 操作方式 | 透過 Python 程式碼編寫任務 |

### 詳細特點剖析

#### 1. 控制與理解網頁的方式不同

-   browser-use 的視覺引導： 它底層驅動 Playwright，並讓大型語言模型（LLM）觀看網頁截圖來決定下一步，類似人類視覺操作。適合需要高度依賴視覺排版理解的複雜多步驟任務（例如：買機票、訂餐廳）。
-   agent-browser 的標籤參考： 它不讓 AI 讀取幾千行的原始 HTML，而是將網頁簡化為「可互動的無障礙樹」，並為每個按鈕、輸入框標上序號（例如：`[ref=e1]`）。AI 只需要下達 `agent-browser click @e1` 的純文字指令即可完成操作，極度節省 Context 空間。 [1, 3, 7, 9]

#### 2. 架構與效能上的差異

-   browser-use： 純 Python 庫，整合了任務規劃器（Planner）、歷史紀錄管理、甚至是將操作過程錄製成 GIF 的功能，整體功能較重、較厚。
-   agent-browser： 採用精簡的 Rust CLI + Node.js Daemon 雙層架構。常駐服務（Daemon）啟動後會維持瀏覽器 Session，免除每次 AI 下指令時的冷啟動時間，且提供本地即時檢視畫面與指令流的儀表板（Dashboard）。 [3, 4, 10, 11]

#### 3. 整合生態與適用場景

-   如果您要開發獨立的 AI 應用： 選擇 browser-use。它能讓您用 Python 快速串接 LangChain 或其他 LLM，給它一個模糊的目標（如「幫我查今天最便宜的機票」），它就會自己規劃並點擊完成。
-   如果您想讓 IDE 編輯器或終端機助手具備網頁能力： 選擇 agent-browser。它完美整合了 MCP (Model Context Protocol) 協定與 Vercel 的 Skill 系統，是目前 Claude Code、Cursor 等 AI 寫程式工具用來<mark>測試網頁、爬取資料</mark>的最佳擴充元件。 [1, 3, 12, 13, 14]

您目前是在開發獨立的 AI 自動化 Agent，還是想在 AI 編碼工具（如 Claude Code/Cursor） 中引入瀏覽器操作呢？告訴我您的應用場景，我可以為您提供對應的安裝與程式碼範例。

[1] [https://www.cnblogs.com](https://www.cnblogs.com/itech/p/20045683)
[2] [https://help.apiyi.com](https://help.apiyi.com/en/agent-browser-ai-browser-automation-cli-guide-en.html)
[3] [https://www.youtube.com](https://www.youtube.com/watch?v=GPb4woYA_8s)
[4] [https://deepseek.csdn.net](https://deepseek.csdn.net/67fc87a9da5d787fd5cc831b.html)
[5] [https://www.instagram.com](https://www.instagram.com/p/DTmzBHaD5pf/)
[6] [https://agent-browser.dev](https://agent-browser.dev/)
[7] [https://www.deeplearning.ai](https://www.deeplearning.ai/short-courses/building-ai-browser-agents/)
[8] [https://www.pulumi.com](https://www.pulumi.com/blog/self-verifying-ai-agents-vercels-agent-browser-in-the-ralph-wiggum-loop/)
[9] [https://www.pulumi.com](https://www.pulumi.com/blog/self-verifying-ai-agents-vercels-agent-browser-in-the-ralph-wiggum-loop/)
[10] [https://www.npmjs.com](https://www.npmjs.com/package/agent-browser)
[11] [https://zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/1885651451088462924)
[12] [https://medium.com](https://medium.com/@bytefer/browser-automation-cli-designed-for-ai-agents-has-arrived-0b8181613669)
[13] [https://zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/1885651451088462924)
[14] [https://classic.yarnpkg.com](https://classic.yarnpkg.com/en/package/agent-browser-mcp)

</td></tr>
</table>

## 2026-07-06

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI Mode
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
如果我需要 AI Code Agent （如 OpenCode）參考我的瀏覽器操作，看我如何執行 Jira JQL 查詢，並將結果下載成 Excel 檔案，並且開啟 Excel，將特定區域建立新的 Excel Table，再用該 Table 產生三個固定的 Pivot Table 樞紐分析。將這個程序生成 Python 自動化程式（例如結合 Playwright 跟 Python Excel library）。可以幫我規劃 step-by-step instruction 嗎？
</td></tr><tr><td>A:</td><td>

要讓 AI Code Agent（例如 OpenCode、Devin 或 AutoGPT）完美複製你的瀏覽器與 Excel 操作，你需要提供結構極高、無歧義且包含精確定位點（Selectors）的步驟指南。AI 主要是透過 DOM 結構（如 `id`, `data-testid`）與程式庫 API 來思考，而非視覺畫面。
以下為你規劃的 Step-by-Step Instruction 範本，你可以直接將其餵給 AI Agent。這份規劃結合了 Playwright（負責網頁自動化）與 openpyxl / pandas（負責 Excel 自動化）。

### AI Agent 任務指令：Jira 數據導出與 Excel 樞紐分析自動化

#### 🤖 任務目標

請編寫一支 Python 腳本，結合 `playwright` 與 `openpyxl`（或 `pandas`），自動登入 Jira 執行 JQL 查詢，將結果下載為 Excel 檔案後，自動開啟該檔案、將特定範圍轉換為 Excel 表格（Table），並建立三個指定的樞紐分析表（Pivot Table）。


#### 🛠️ 第一階段：環境配置與套件

請使用以下 Python 套件進行開發：

-   `playwright` (非同步或同步模式皆可，建議使用 `sync_api`)
-   `pandas` (用於處理數據與結構)
-   `openpyxl` (用於精確控制 Excel 格式、建立 Table 與 Pivot Table)


#### 🌐 第二階段：網頁自動化步驟 (Playwright)

##### 1\. 登入 Jira

-   導向網址：前往你的 Jira 登入頁面。
-   輸入憑證：定位使用者名稱與密碼輸入框，輸入環境變數中的憑證（勿寫死在程式碼中）。
-   點擊登入：點擊提交按鈕，並等待頁面完全載入（`wait_for_load_state("networkidle")`）。

##### 2\. 執行 JQL 查詢

-   導向篩選器頁面：直接前往 `https://<your-domain>.atlassian.net/issues/?jql=<你的JQL語句>`，或者點擊導覽列的「Filters」並切換至進階搜尋。
-   確認輸入：確保 JQL 輸入框內顯示正確的查詢字串（例如：`project = "PROJ" AND status = "Done"`）。

##### 3\. 下載 Excel 檔案

-   觸發導出：在頁面右上角尋找「Export」按鈕（通常帶有 `data-testid="search-results-export-menu.trigger"` 或類似屬性）。
-   選擇格式：點擊「Export Excel (All fields)」或「Export CSV」。
-   處理下載事件：使用 Playwright 的 `with page.expect_download() as download_info:` 語法監聽下載事件。
-   儲存檔案：將下載的檔案儲存至本地工作目錄，重新命名為 `jira_raw_data.xlsx`。


#### 📊 第三階段：Excel 自動化步驟 (Python Excel Library)

##### 4\. 建立 Excel 表格 (Excel Table)

-   讀取檔案：使用 `openpyxl` 載入 `jira_raw_data.xlsx`。
-   動態偵測範圍：自動偵測資料的最後一行（`max_row`）與最後一列（`max_column`），定義資料區間（例如 `A1:Z100`）。
-   建立 Table：使用 `openpyxl.worksheet.table.Table` 將該區間轉換為名為 `JiraDataTable` 的 Excel 表格。
-   套用樣式：設定表格樣式為 `TableStyleMedium9`，並確認勾選「標題列（`showFirstColumn=False`, `showLastColumn=False`）」。

##### 5\. 建立三個固定的樞紐分析表 (Pivot Table)

*請注意：`openpyxl` 支援建立樞紐分析的定義，但最穩定的方式是利用 `pandas` 計算出結構後，用 `openpyxl` 寫入新工作表（Sheet），並將其美化為報表樣式。請依序建立以下三個 Sheet：*

##### 📊 樞紐分析表一：任務狀態分佈 (Sheet 名稱: `Pivot_Status`)

-   列 (Rows)：`Status` (狀態)
-   值 (Values)：`Issue key` (計算個數 Count)
-   排序：依個數由大到小排序。

##### 📊 樞紐分析表二：團隊成員工作量 (Sheet 名稱: `Pivot_Assignee`)

-   列 (Rows)：`Assignee` (經辦人)
-   欄 (Columns)：`Priority` (優先級)
-   值 (Values)：`Issue key` (計算個數 Count)

##### 📊 樞紐分析表三：每月完成趨勢 (Sheet 名稱: `Pivot_Monthly_Trend`)

-   列 (Rows)：`Resolved` (解決日期，請自動解析並依「年份-月份」分組)
-   值 (Values)：`Issue key` (計算個數 Count)

#### ⚙️ 第四階段：異常處理與輸出規範

-   無頭模式：預設使用 `headless=True` 執行，但保留開關以便偵錯。
-   驗證機制：在處理 Excel 前，必須檢查下載的檔案大小是否大於 0 KB。
-   最終儲存：將處理完畢、包含原始資料 Table 與三個 Pivot Sheets 的活頁簿儲存為 `Jira_Automation_Report.xlsx`。

#### 💡 給 AI Agent 的 Hint / 提示

> 如果在 `openpyxl` 中建立原生 Excel 樞紐分析快取（Pivot Cache）過於複雜，允許使用 `pandas.pivot_table` 產生聚合數據，再將結果寫入 Excel，並透過 `openpyxl` 套用樣式（如 Table Style 或欄寬自適應），以達到完全相同的視覺與數據效果。

* * * *

若要讓我幫你精確寫出這個 Python 程式碼，你可以提供：

-   你目前使用的 Jira 是雲端版（Cloud）還是地端版（Server）？（這會影響下載按鈕的網頁標籤）
-   你的 JQL 查詢語句大概長怎樣？
-   你的 Jira 欄位名稱（例如：經辦人是叫 `Assignee` 還是中文的 `經辦人`）？
</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
如何讓 OpenCode Agent 錄製 existing browser session 的操作？
</td></tr><tr><td>A:</td><td>

### OpenCode + Chrome Remote Debugging

要讓 OpenCode Agent（或類似的 AI Code Agent、Playwright 腳本）直接接管或「錄製」你當前已經打開、登入好 Jira 的瀏覽器視窗（Existing Browser Session），最有效且能繞過 2FA 驗證的方法，就是利用 Chromium 的 遠端除錯連接埠（Remote Debugging Port）。
這樣 AI 就不需要從頭模擬登入，而是直接在你已經開好的瀏覽器中「看著你操作」並自動生成 Playwright 程式碼。
以下是具體的實作步驟：

#### 第一步：完全關閉現有的 Chrome / Edge 瀏覽器

為了重啟帶有除錯功能的瀏覽器，必須先將後台所有該瀏覽器的程序（Processes）完全關閉。

#### 第二步：從終端機啟動「除錯模式」的瀏覽器

打開你的終端機（Terminal 或 Command Prompt），依據你的作業系統執行以下指令，這會打開一個全新、乾淨但允許外部控制的瀏覽器視窗：

-   Windows (Chrome):

```cmd
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\ChromeDebug"
```

-   Mac (Chrome):

```bash
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="/tmp/chrome_dev"
```

> 💡 重要：請在這個剛剛跳出來的新瀏覽器視窗中，手動登入你的 Jira，並切換到你要開始查詢的畫面。

#### 第三步：讓 OpenCode / Playwright 接管並開始錄製

此時，該瀏覽器已經在 `9222` 連接埠（Port）等待指令 \[1\]。你可以給 OpenCode Agent 以下的指令，讓它啟動 Playwright 的錄製器（Codegen）直接連入該視窗：

#### 🤖 提供給 OpenCode 的 Prompt 指令：

> "Please start the Playwright recorder to connect to my existing Chrome browser session on port 9222, and record my actions as I run a JQL query and download the Excel file. Generate a Python script from it."

#### ⚙️ Agent 會在後台執行的指令：

OpenCode 收到後，會在終端機執行這行 Playwright 內建的接管錄製指令：
```
playwright codegen localhost:9222
```

執行後，你會看到 Playwright 的程式碼生成視窗（Inspector）跳出來。此時，你只要在剛剛打開的 Jira 網頁上進行以下操作：

1.  點擊 JQL 輸入框並輸入查詢。
2.  點擊 Export 按鈕。
3.  下載 Excel 檔案。

Playwright Inspector 視窗就會即時（Real-time）將你的滑鼠點擊與鍵盤輸入轉化為 Python (Playwright) 程式碼。

#### 第四步：將錄製的程式碼與 Excel 自動化整合

錄製完成後，OpenCode 拿到的 Playwright 接管程式碼結構會類似這樣：
```py
fromplaywright.sync_apiimportsync_playwrightdefrun():
    with sync_playwright() asp:
        # 連接到你已經開啟的 9222 視窗，不用重新登入browser = p.chromium.connect_over_cdp("http://localhost:9222")
        default_context = browser.contexts[0]
        page = default_context.pages[0]

        # 以下為 Playwright 自動錄製生成的點擊與下載代碼# page.locator("...").click()# with page.expect_download() as download_info:#     page.locator("text=Export").click()

        print("錄製成功，已取得網頁操作邏輯！")

run()
```

此時，你就可以叫 OpenCode 接續進行：*「請將這段錄製好的 Playwright 程式碼，與先前規劃的 pandas/openpyxl Excel 樞紐分析腳本結合成一個完整的自動化流程。」*

* * * *

你想先讓 OpenCode 嘗試連線到 `9222` 連接埠並測試能否成功控制網頁，還是直接開始撰寫後續整合 Excel 處理的程式碼呢？
</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
OpenCode 搭配 browser-use 可以達成類似的目標嗎？
</td></tr><tr><td>A:</td><td>

### OpenCode + Browser-Use

可以，而且使用 OpenCode 搭配 `browser-use` 達成的效果會比單純用 Playwright 錄製更強大、更聰明。 \[1\]
`browser-use` 是專門為大型語言模型（LLM）設計的瀏覽器控制框架 \[1\]。它不採用「錄製死板腳本」的邏輯，而是讓 AI Agent 像人類一樣看著網頁、理解內容，並動態做出決策。
以下為你拆解 OpenCode 搭配 `browser-use` 實作此任務的核心機制與步驟：

* * * *

#### 💡 為什麼搭配 `browser-use` 更適合？

-   不需要維護 Selector：Jira 經常改版或使用動態生成的 CSS 類名。Playwright 錄製的 `page.locator(".css-xyz")` 很容易失效，而 `browser-use` 讓 AI 理解「這是一個 Export 按鈕」，改版也能自動適應。
-   支援接管現有瀏覽器：它同樣支援連接到你已經登入、開啟 `9222` 連接埠的 Chrome 視窗，直接跳過驗證碼與 2FA 登入步驟。
-   自動處理不確定性：如果 JQL 查詢載入太慢，AI 會自動等待，不需要你在程式碼裡寫死 `time.sleep()` 或複雜的等待條件。

#### 🛠️ 實作三步驟：OpenCode + browser-use 設定

你可以讓 OpenCode 依照以下步驟，幫你寫出基於 `browser-use` 的自動化 Agent。

##### 第一步：啟動除錯模式的 Chrome (與前述相同)

在終端機啟動一個允許外部控制、且你已經手動登入 Jira 的 Chrome：
```
# Windows
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\ChromeDebug"
# Mac
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="/tmp/chrome_dev"
```

##### 第二步：讓 OpenCode 安裝依賴套件

在 OpenCode 的環境中執行：
```
pip install browser-use langchain-openai pandas openpyxl
```

##### 第三步：撰寫 `browser-use` 執行腳本

你可以要求 OpenCode 生成如下的 Python 程式碼。這段程式碼會連進你的 Chrome，自動執行 JQL 並下載檔案，最後交給 Excel 處理函式：
```python
import asyncio
from browser_use import Agent, Browser, BrowserConfig
from langchain_openai import ChatOpenAI
import pandas as pd
from openpyxl import load_workbook

# 1. 設定瀏覽器：連接到你已經開啟的 9222 連接埠
config = BrowserConfig(
    chrome_instance_path=None, # 不啟動新瀏覽器
    wss_url="ws://localhost:9222/devtools/browser/..." # 或者直接指定 cdp_url
)
# 註：browser-use 支援透過 connect_over_cdp 接入現有 Chrome

async def main():
    browser = Browser(config=config)
    
    # 2. 定義給 AI Agent 的自然語言任務指令
    task_description = """
    1. 前往我已經打開的 Jira 分頁（或輸入網址 https://atlassian.net）。
    2. 在 JQL 輸入框中輸入 'project = "PROJ" AND status = "Done"' 並按下 Enter 查詢。
    3. 點擊右上角的 'Export' 按鈕，並選擇 'Export Excel' 或 'Export CSV' 下載檔案。
    4. 將下載下來的檔案重新命名並儲存為 'jira_raw_data.xlsx'。
    """
    
    # 3. 啟動 browser-use Agent
    agent = Agent(
        task=task_description,
        llm=ChatOpenAI(model="gpt-4o"), # 或 Claude 3.5 Sonnet
        browser=browser
    )
    
    # 執行網頁操作
    history = await agent.run()
    await browser.close()
    
    # 4. 接續執行你的 Excel 處理邏輯
    process_excel_report()

def process_excel_report():
    print("網頁下載完成，開始處理 Excel Table 與三個 Pivot Tables...")
    # 這裡放入先前規劃的 pandas/openpyxl 程式碼
    # ...

if __name__ == "__main__":
    asyncio.run(main())
```

* * * *

##### ⚖️ Playwright 錄製 vs Browser-use 方案對比

| 特性 | Playwright 錄製 (Codegen) | OpenCode + browser-use |
| --- |  --- |  --- |
| 撰寫難度 | 需手動錄製、點擊，再調整程式碼 | 極低，直接寫中文/英文原理想法 \[1\] |
| 維護成本 | 高，網頁稍微改版（如 ID 改變）就需重新錄製 | 極低，AI 會自己看畫面重新尋找按鈕 \[2\] |
| 執行速度 | 快（直接執行底層網頁指令） | 稍慢（AI 每一步需要思考與解讀畫面） \[2\] |
| 除錯難度 | 需工程師看懂 Playwright 語法 | AI 會自己看 Log 嘗試自我修復 \[2\] |

總結來說：如果你希望一勞永逸，不想因為 Jira 未來按鈕改位置、換顏色而常常進去修程式碼，強烈建議讓 OpenCode 採用 `browser-use` 方案。
如果準備好了，我們可以先請 OpenCode 寫出連接 `9222` 連接埠並嘗試在 Jira 搜尋的 `browser-use` 測試腳本，你覺得如何？
</td></tr>
</table>

