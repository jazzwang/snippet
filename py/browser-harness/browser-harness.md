# browser-harness

> Browser Harness | Self-healing harness that enables LLMs to complete any task.

- Git Repo
  - https://github.com/browser-use/browser-harness
- Website
  - https://browser-harness.com/

## 2025-05-13

- Learn from https://www.linkedin.com/feed/update/urn:li:activity:7451625476818640896/

```
不只有 Harness Agent，連瀏覽器也需要 Browser Harness！

Browser Use 團隊最近開源出一個有趣的專案 Browser Harness，整個框架只有約 592 行程式碼，卻能讓 LLM 完整操控瀏覽器。

其中最特別的設計叫 self-healing，也就是 Agent 執行任務時若發現工具不夠用，能直接修改 harness 原始碼把函式補上，然後繼續完成任務。

這種自我修復能成立，關鍵在於 Browser Harness 刻意把抽象層減到最少，它直接建構在 Chrome DevTools Protocol 之上，中間沒有任何多餘的包裝。作者認為，厚重的框架反而會拖累 LLM 的推理能力，包裝越少，Agent 越能發揮全部實力。

這套「讓 Agent 自己補上缺口」的邏輯，還延伸到了 domain-skills 資料夾。Agent 處理某個網站時累積的Selector、流程與限制條件，會由 Agent 自己寫成 skill 檔案供日後共用。下次再處理同樣的網站，這個 skill 會被載入，Agent 就不用重新摸索一次。
```

## 2026-10-23

> [!NOTE]
> 根據 https://github.com/browser-use/browser-harness 內容撰寫一篇技術報告，採用繁體中文（台灣用詞）撰寫，包括 step-by-step 測試步驟，存成 browser-harness.md

## Browser Harness 技術報告

### 概述

Browser Harness 是一個開源的瀏覽器自動化框架，允許 AI 代理（如 Claude Code、Codex、Cursor）透過 DevTools 協議（CDP）直接控制使用者的 Chrome 瀏覽器。與傳統瀏覽器自動化工具不同，Browser Harness 可以直接操作使用者已經登入的 Chrome 瀏覽器，保留所有個人化設定、Cookie 和登入狀態。

**核心特點：**
- 使用 Chrome DevTools 協議（CDP）與瀏覽器通訊
- 支援使用者的 Chrome 瀏覽器，保留登入狀態
- 開源專案，採用 MIT 授權
- 代理自動生成輔助程式碼，隨著任務使用不斷優化

---

### 安裝與設定步驟

#### 步驟 1：快速安裝

使用 `uv` 工具安裝最新穩定版（建議使用 Python 3.12）：

```bash
uv tool install --python 3.12 --upgrade --force browser-harness
```

參數說明：
- `--python 3.12`：強制使用 Python 3.12，避免選擇支援舊版 Python 的舊版本
- `--upgrade --force`：替換任何先前安裝的 `browser-harness` 工具，但不會影響其他無關命令（如 `browser-use-Browser`）

#### 步驟 2：註冊技能（Skill）

將 Browser Harness 技能註冊到代理系統：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills/browser-harness"
browser-harness skill > "${CODEX_HOME:-$HOME/.codex}/skills/browser-harness/SKILL.md"
```

#### 步驟 3：測試連接

執行以下命令測試連接是否正常：

```bash
browser-harness <<'PY'
print(page_info())
PY
```

如果 `page_info()` 能正常輸出，則表示設定成功，可繼續進行下一步的錄音同意設定。

#### 步驟 4：設定錄音同意（可選）

執行以下命令檢查錄音設定狀態：

```bash
browser-harness recordings
```

如果顯示 `(default)`，則需要詢問使用者是否啟用本地瀏覽器錄音功能：

> Enable local browser recordings? This saves screenshots and action traces on this machine, which may include sensitive page content, so you can later ask "show me what you did" or request a video. Videos are never generated automatically. [y/N]

**預設值為 `no`。** 只有在使用者明確回答 `yes` 後，才執行 `browser-harness recordings enable`；否則執行 `browser-harness recordings disable`。升級時會保留現有的 `(config)` 或 `(BH_RECORD)` 偏好設定，不會再次詢問。

---

### 故障排除

#### Chrome 阻擋連線

如果連線失敗，需要手動在 Chrome 中啟用遠端除錯：

1. 開啟 `chrome://inspect/#remote-debugging`
2. 勾選 "Allow remote debugging for this browser instance"
3. 重新執行 `page_info()` 測試

如果在 macOS 上遇到 `permission-blocked` 錯誤，需要處理連線的允許視窗（不將 Chrome 帶到前景）：

```bash
browser-harness mac-approve
```

**注意：** 此工具需要 Accessibility 權限，需要在系統設定中授予啟動 CLI 的應用程式（如終端機、iTerm、Codex 或 IDE）存取權。

#### 其他診斷工具

如果安裝或連線仍然失敗，可以使用診斷工具：

```bash
browser-harness --doctor
```

常見失敗原因：
- `chrome running` FAIL：請使用者開啟 Chrome，或使用隔離/雲端瀏覽器
- `daemon alive` FAIL：Chrome 遠端除錯權限遺失、Chrome 已關閉，或 CDP 端點無法連接到
- `update available`：可執行 `browser-harness --update -y` 進行升級

#### 進階診斷

對於機器可讀的健康檢查，編排器可以設定 `BU_NAME` 為已配置的 daemon 並執行：

```bash
browser-harness doctor --json --require-existing-daemon
```

此命令會輸出版本化的 JSON 報告，並在該 daemon 沒有活躍的瀏覽器連線時以非零代碼退出。它從不啟動或發現其他瀏覽器。

---

### 雲端瀏覽器

雲端瀏覽器是選配功能，本地 Chrome 不需要 Browser Use API Key。

#### 登入認證

```bash
browser-harness auth login
```

或使用安全方式匯入金鑰：

```bash
printf '%s' "$BROWSER_USE_API_KEY" | browser-harness auth login --api-key-stdin
```

#### 啟動雲端瀏覽器

選擇一個短的自訂名稱（例如 `r7k2` 僅為範例）：

```bash
browser-harness <<'PY'
start_remote_daemon("r7k2")
PY
```

然後使用名稱呼叫：

```bash
BU_NAME=r7k2 browser-harness <<'PY'
print(page_info())
PY
```

#### 使用時機

建議在以下情況使用雲端瀏覽器：
- **使用者需要多個並行任務**：本地 Chrome 是單一共享瀏覽器，並行任務會爭奪標籤頁和焦點。每個任務使用一個雲端瀏覽器可完全隔離。
- **可能遇到 Captcha 或阻擋**：雲端瀏覽器使用乾淨的託管 IP 和隱形設定，較少被 Captcha 牆或速率限制，同時保護使用者的 IP 和本地瀏覽器。

#### 結束雲端瀏覽器

任務完成且雲端瀏覽器仍在運行時，應詢問使用者：「Should I close this browser now?」如果確認，執行：

```bash
stop_remote_daemon(name)
```

**注意：** 遠端 daemon 在停止或超時前會計費。

---

### 使用指引

#### 基本命令

```bash
browser-harness <<'PY'
## 列印當前頁面資訊
print(page_info())

## 開啟新分頁並導航
new_tab("https://example.com")

## 切換到指定標籤頁
switch_tab(id)

## 點擊元素
click_at_xy(x, y)

## 輸入文字
type(text)

## 擷取截圖
screenshot()

## 執行 JavaScript
js("document.body.innerHTML")
PY
```

#### 標籤頁管理

- **首次導航使用 `new_tab(url)`，而非 `goto_url(url)`**：daemon 保留所附連的標籤頁，避免在每個腳本中呼叫 `new_tab()`
- **保持單一工作標籤頁**：每個任務/網站保持一個工作標籤頁。開啟其他標籤前，先檢查 `current_tab()` 和 `list_tabs()`，並使用 `switch_tab()` 重複使用匹配的標籤頁
- **不遺留重複標籤頁**：不要在同一 URL 上遺留重複的標籤頁，也不要關閉未建立的標籤頁
- **任務完成時關閉標籤頁**：關閉任務中建立的、不再需要的標籤頁。如果使用者需要看到該標籤頁、需要已知後續使用、或關閉可能丟失未儲存的工作或其他重要狀態，則保持開啟

#### 重要注意事項

- **不要自動呼叫 `activate_tab(target)`**：這會將 Chrome 帶到前景。只有在使用者明确要求查看或切換到該標籤頁時才呼叫
- **不要將 `switch_tab()` 與 `activate_tab()` 搭配使用**
- **本地 daemon 是與整個 Chrome 實體的連線，而非單一網站、任務、卡片或代理**：省略 `BU_NAME` 並重複使用預設 daemon，以便在網站、標籤頁、截圖和 Codex 輪次之間進行正常的順序本地工作
- **不要為每個工作發明新的名稱**：如 `gmail1375` 或 `slack1371`。每個新的本地 daemon 會開啟另一個瀏覽器層級的 CDP 連線，Chrome 可能會顯示另一個 Allow 提示
- **設定 `BH_TAB_MARKER=0` 在啟動 daemon 前**：預設保持馬標記啟用

#### 時間超時與隱藏頁面

時間超時或頁面在隱藏時暫停，**不是**允許將 Chrome 帶到前景的許可。繼續使用背景 CDP 操作。對於焦點限制的頁面，臨時呼叫：

```python
cdp("Emulation.setFocusEmulationEnabled", enabled=True)
```

執行並驗證操作後，在 `finally` 區塊中停用它。如果背景控制仍無法工作，報告此限制，而非啟動標籤頁。不要發明 `Runtime.evaluate` 滾動替代方案或跨 frame JS 步行器。

---

### 遠端瀏覽器（雲端）

#### 使用時機

建議在以下情況使用雲端瀏覽器：
- **使用者需要多個並行任務**：本地 Chrome 是單一共享瀏覽器，並行任務會爭奪標籤頁和焦點。每個任務使用一個雲端瀏覽器可完全隔離
- **可能遇到 Captcha 或阻擋**：雲端瀏覽器使用乾淨的託管 IP 和隱形設定，較少被 Captcha 牆或速率限制，同時保護使用者的 IP 和本地瀏覽器

#### 建立遠端 daemon

```bash
browser-harness <<'PY'
start_remote_daemon("r7k2")
PY
```

然後使用名稱呼叫：

```bash
BU_NAME=r7k2 browser-harness <<'PY'
new_tab("https://example.com")
print(page_info())
PY
```

#### 重要提示

- 不要啟動遠端 daemon 然後繼續使用預設 daemon。使用相同的 `BU_NAME`
- 任務完成且雲端瀏覽器仍在運行時，詢問使用者是否關閉。如果確認，執行 `stop_remote_daemon(name)`
- 遠端 daemon 在停止或超時前會計費

---

### 頁面工作流程

1. **優先使用可訪問性樹（Accessibility Tree）尋找元素**，而非截圖：
   ```python
   cdp("Accessibility.getFullAXTree")["nodes"]
   ```
   具有每個元素的 role、name 和 `backendDOMNodeId` — 在 Python 中過濾後再列印（有數千個節點）

2. **點擊操作**：AX 節點 -> 方塊中心 -> `click_at_xy(x, y)` -> 使用目標化的 `js(...)`/`page_info()` 檢查驗證

3. **僅當 AX 樹缺乏元素時（canvas、特殊 widget），才回歸使用 HTML 的 `js(...)`**：當佈局或圖像相關時使用截圖

4. **導航後呼叫 `wait_for_load()`**

5. **如果當前標籤頁過期或為內部頁面，呼叫 `ensure_real_tab()`**

6. **使用 `js(...)` 進行 DOM 檢查或提取**：當座標是錯誤的工具時

7. **輸入異常長的文字時，避免慢速逐字輸入**：尋找更快的頁面合適輸入方法，然後驗證頁面保留了精確值

8. **登入牆**：停止並詢問。例外：當 Chrome 已經登入時自動使用可用的 SSO；但仍然在密碼、MFA、同意或模糊帳戶選擇時停止

9. **原始 CDP 可用於 `cdp("Domain.method", ...)`**：
   - 將 CDP 參數作為關鍵字傳遞：`cdp("Input.insertText", text="hello")`
   - 第二個位置參數是 session ID，而非參數字典
   - 當目標明確 session 時，使用 `session_id="..."` 與關鍵字搭配

---

### 錄音與影片

#### 基本錄音操作

```bash
browser-harness recordings enable
browser-harness recordings disable
browser-harness recordings
```

`BH_RECORD=1` 或 `BH_RECORD=0` 可覆蓋預設值。任何自然的「錄製」、「顯示」、「演示」或「製作影片」提示都會為該任務啟用；單獨的顯著工作則不會。

#### 錄音流程

1. 在瀏覽器工作前，呼叫 `start_recording(name, title=...)`
2. 保留其精確返回的目錄路徑
3. 驗證結果後，呼叫 `stop_recording()`

**不要**用 `recordings --latest` 替換該路徑。對於任務後請求的使用，使用：

```bash
browser-harness recordings --latest
```

**僅當**時間戳和頁面匹配時使用；否則表示工作未被捕捉。永遠不要重現已完成的工作。對於影片，請參閱 [make-video.md](https://github.com/browser-use/browser-harness/blob/main/interaction-skills/make-video.md)。

---

### 互動技能（Interaction Skills）

如果遇到瀏覽器機制問題，請檢查以下技能文件：

- connection.md - 連線
- cookies.md - Cookie 管理
- cross-origin-iframes.md - 跨來源 iframe
- dialogs.md - 對話框
- downloads.md - 下載
- drag-and-drop.md - 拖放
- dropdowns.md - 下拉選單
- iframes.md - iframe 處理
- make-video.md - 製作影片
- network-requests.md - 網路請求
- print-as-pdf.md - 列印為 PDF
- profile-sync.md - 用戶名檔同步
- screenshots.md - 截圖
- scrolling.md - 滾動
- shadow-dom.md - Shadow DOM
- tabs.md - 標籤頁管理
- uploads.md - 上傳
- viewport.md - 視窗大小

---

### 設計限制

- **座標點擊預設**：CDP mouse 事件在合成器層面透過 iframe/shadow/cross-origin
- **保持連線模型簡單**：使用預設 daemon、`BU_NAME`、`BU_CDP_URL`、`BU_CDP_WS`，或 `start_remote_daemon(...)`
- **信任的編排器可以設定 `BH_OPEN_LIVE_URL=0`**：在配置 Cloud daemon 時，避免列印或開啟其互動式即時視圖 URL。URL 仍會建立並由 `start_remote_daemon()` 返回；呼叫者必須避免記錄或序列化該返回欄位
- **已配置精確名稱 daemon 的信任編排器可以設定 `BH_REQUIRE_EXISTING_DAEMON=1`**：每個 CLI 呼叫則會健康檢查並重複使用該 daemon 或失敗；它從不自動啟動或發現其他 Chrome

---

### 錯誤避免清單（Gotchas）

- `chrome://inspect/#remote-debugging` 必須啟用才能控制本地 Chrome
- 在 macOS 上，如果本地 Chrome 顯示 "Allow remote debugging?" 視窗，呼叫 `mac-approve` 一次，並保持原始瀏覽器命令等待。不要輪詢或重新執行瀏覽器命令
- Omnibox 彈出視窗不是真實工作標籤頁
- CDP target 順序不是 Chrome 的可見標籤列順序
- `BU_CDP_URL` 是 HTTP DevTools 端點；daemon 將其解析為 WebSocket
- 在離開雲端瀏覽器前應詢問使用者
- 使用 `stop_remote_daemon(name)` 或 `PATCH /browsers/{id} {"action":"stop"}` 停止雲端瀏覽器

---

### MCP Server

`browser-harness-mcp` 命令將 `browser_harness.helpers` 作為 MCP 工具透過 stdio 暴露。它重複使用現有的 helper 層 — 沒有第二個 CDP 實作，也沒有在 `src/browser_harness/` 內部的變更。

#### 啟動

從任何目錄：

```bash
uvx --from 'browser-harness[mcp]' browser-harness-mcp
```

伺服器使用 MCP stdio 並連接到 `browser-harness` 使用的相同本地 Chrome CDP 端點（9222/9223）。daemon 在第一次工具呼叫時自動啟動。

#### 工具

瀏覽器控制 helper 從 `browser_harness.helpers` 作為 MCP 工具暴露，前綴為 `browser_`：

- `browser_new_tab`
- `browser_goto`
- `browser_page_info`
- `browser_click`
- `browser_type`
- `browser_fill`
- `browser_press`
- `browser_scroll`
- `browser_screenshot`
- `browser_list_tabs`
- `browser_current_tab`
- `browser_switch_tab`
- `browser_close_tab`
- `browser_ensure_real_tab`
- `browser_wait`
- `browser_wait_for_load`
- `browser_wait_for_element`
- `browser_js`
- `browser_cdp`
- `browser_upload_file`
- `browser_http_get`
- `browser_start_recording`
- `browser_stop_recording`

每個工具返回 JSON 文字。錯誤時回應為 `{"error": "..."}`，伺服器進程保持運行。

#### 範例流程

1. `browser_new_tab(url="https://example.com")`
2. `browser_wait_for_load()`
3. `browser_screenshot()` → 返回 `path`、`width`、`height`、`size_bytes`
4. `browser_page_info()` → 返回 `url`、`title`、viewport/scroll/page size

#### 客戶端配置

##### Claude Code

```bash
claude mcp add browser-harness \
  uvx --from 'browser-harness[mcp]' browser-harness-mcp
```

##### Devin

```bash
devin mcp add -s project browser-harness -- \
  uvx --from 'browser-harness[mcp]' browser-harness-mcp
```

##### Cursor / OpenClaw / 其他 MCP 客戶端

```json
{
  "mcpServers": {
    "browser-harness": {
      "command": "uvx",
      "args": [
        "--from",
        "browser-harness[mcp]",
        "browser-harness-mcp"
      ]
    }
  }
}
```

##### MCP Inspector

```bash
npx @modelcontextprotocol/inspector \
  uvx --from 'browser-harness[mcp]' browser-harness-mcp
```

從儲存庫檢查點，`uv run --extra mcp browser-harness-mcp` 對當前來源運行相同的包裝入口點。

---

### 設定提示（Setup Prompt）

將以下提示貼入 Claude Code 或 Codex（Cursor：使用 [MCP 配置](#cursor)）：

```text
Install or upgrade browser-harness to the latest stable version with uv using Python 3.12, register the skill from `browser-harness skill`, and connect it to my browser. Ask whether I want local browser recordings enabled; default to no and preserve my existing preference on upgrades. Follow https://github.com/browser-use/browser-harness/blob/main/install.md if setup or connection fails.
```

代理將開啟 `chrome://inspect/#remote-debugging`。首次設定時，勾選方框以便代理連接到瀏覽器：

![Remote debugging setup](https://github.com/browser-use/browser-use/blob/main/docs/setup-remote-debugging.png)

---

### 與其他瀏覽器工具比較

| 工具                        | 相容的代理                                                                                                | 驅動的瀏覽器                                                                                                | 使用者在 Chrome 中批准的範圍                                                  |
| ------------------------- | ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Browser Harness**       | Claude Code, Codex, Cursor, 任何 MCP 客戶端透過 `browser-harness-mcp`                                       | 使用者正在運行的 Chrome，以使用者身分登入                                                                              | 整個瀏覽器：在 Chrome 144+ 上，在 `chrome://inspect` 勾選遠端除錯，然後點擊 Allow        |
| **Playwright MCP**        | 任何 MCP 客戶端                                                                                           | 預設為其自己的瀏覽器用戶名檔。Chrome 使用 `--extension`（Playwright 擴充功能）或 `--cdp-endpoint`                             | 透過擴充功能的選取標籤（每個客戶端一個標籤組），可使用 token 跳過批准；或透過 `--cdp-endpoint` 使用整個瀏覽器 |
| **Playwright CLI**        | 任何運行 shell 命令的代理                                                                                     | 預設為其自己的瀏覽器。Chrome 使用 `attach --extension=chrome` 或 `attach --cdp=chrome`                              | 透過 Playwright 擴充功能的選取標籤，或透過 `--cdp` 使用整個瀏覽器                         |
| **Chrome DevTools MCP**   | 任何 MCP 客戶端及 CLI                                                                                      | 預設為具有專用用戶名檔的新 Chrome。Chrome 144+ 使用 `--autoConnect`                                                   | 整個瀏覽器：相同的 Chrome 144+ toggle 和 Allow dialog；伺服器看到該用戶名檔的每個開啟的視窗      |
| **agent-browser**         | 任何代理及 CLI                                                                                            | 預設為測試用途的自己的 Chrome。使用 `--profile` 複製使用者的 Chrome 用戶名檔。使用 `--auto-connect` 或 `--cdp` 連接使用者的正在運行的 Chrome | 整個瀏覽器：相同的 Chrome 144+ toggle 和 Allow dialog                         |
| **Claude in Chrome**      | 具有 Claude 擴充功能的 Claude Code（CLI 或 VS Code），使用直接 Anthropic 方案（Pro, Max, Team, Enterprise）登入，而非 API 金鑰 | 使用者正在運行的 Chrome、Edge 或其他 Chromium 瀏覽器，以使用者身分登入                                                        | 每網站：允許擴充功能中的網站，或每動作在 Claude Code（auto mode 可跳過每網站檢查）                |
| **ChatGPT Browser 和擴充功能** | ChatGPT 桌面 App 中的 Codex 和 ChatGPT 聊天                                                                 | 瀏覽器：專用用戶名檔。擴充功能：Chrome、Edge、Brave、Opera 或 Vivaldi 用戶名檔                                                | 每網站：每個新網站詢問一次（一次允許、對該網站或所有網站）                                       |

#### 效能比較（2026-10-14 測量）

在 200 個公開 BU Bench V2.1 任務中的 100 個任務上進行匹配評估（bu2-001 到 bu2-100；未運行 101-200）。

**測試條件：**
- 每個工具使用相同的代理：Codex CLI 0.144.6，GPT-6 Luna，medium reasoning，web search 關閉
- 使用相同的 frozen judge
- 所有工具驅動相同的 Browser Use cloud 瀏覽器（透過 CDP）
- 每個任務只運行一次，代理失敗從不重試
- Runner、browser 和 judge 失敗重試一次（Browser Harness 3 次任務，Playwright MCP 4 次，Chrome DevTools MCP 6 次，agent-browser 0 次）

| 工具                     | 平均評級分數 0-100 (95% CI) | 完全解決 | 每任務中位數輸入 token | 每任務中位數模型成本 (GPT-6 Luna 定價) | 每任務中位數代理時間 |
| ---------------------- | --------------------- | ---- | -------------- | -------------------------- | ---------- |
| Browser Harness (main) | 60.4 (55.2-65.4)      | 11%  | 2.1M           | $0.042                     | 9.0 min    |
| Playwright MCP         | 60.0 (55.1-65.0)      | 11%  | 4.4M           | $0.066                     | 8.3 min    |
| Chrome DevTools MCP    | 61.0 (55.8-65.9)      | 11%  | 6.7M           | $0.097                     | 8.7 min    |
| agent-browser          | 56.3 (51.1-61.5)      | 9%   | 3.3M           | $0.056                     | 11.2 min   |

**分析：**
- 沒有工具在分數上獲勝：所有與 Browser Harness 配對的差異的 95% CI 都包含零
- Browser Harness 擁有最低的輸入 token（2.1M 對比 3.3-6.7M）和最低的模型成本（$0.042 對比 $0.056-0.097）
- 模型成本不包含瀏覽器、代理和 judge
- 比 Playwright MCP 和 Chrome DevTools MCP 慢（中位數 9.0 對比 8.3 和 8.7 分鐘），但比 agent-browser 快（11.2 分鐘）
- 這些是中位數，沒有置信區間

**何時使用其他工具：**
- **Playwright**（測試、MCP 或 CLI）：在乾淨的瀏覽器中對自己的應用執行隔離、可重複的 CI 測試，沒有個人登入
- **Chrome DevTools MCP**：效能追蹤和 DevTools 除錯（網路、主控台、source-mapped stack traces）
- **Claude in Chrome**：只使用 Claude 且具有 Pro、Max、Team 或 Enterprise 方案
- **Cursor 內建 Browser**：代理不需要使用者登入的 Chrome。它在每個工作區專用用戶名檔中運行

---

### 狀態儲存位置

狀態預設儲存於 `${XDG_CONFIG_HOME:-~/.config}/browser-harness`：
- auth（認證）
- telemetry id（遥測 ID）
- agent workspace（代理工作區）
- runtime sockets（運行時 socket）
- logs（日誌）
- screenshots（截圖）
- temp files（暫存檔案）

可透過 `BH_HOME` 或 `BROWSER_HARNESS_HOME` 覆寫。

---

### 參考文件

- [install.md](https://github.com/browser-use/browser-harness/blob/main/install.md) - 安裝與連線
- [SKILL.md](https://github.com/browser-use/browser-harness/blob/main/SKILL.md) - 技能訓練資料
- [docs/MCP.md](https://github.com/browser-use/browser-harness/blob/main/docs/MCP.md) - MCP 伺服器設定
- [CONTRIBUTING.md](https://github.com/browser-use/browser-harness/blob/main/CONTRIBUTING.md) - 貢獻指南
- [interaction-skills](https://github.com/browser-use/browser-harness/tree/main/interaction-skills) - 互動技能文件

---

### 連結資源

- [Browser Use Cloud](https://cloud.browser-use.com/v4) - 雲端瀏覽器服務
- [Web Agents That Actually Learn](https://browser-use.com/posts/web-agents-that-actually-learn) - 真正學習的 Web 代理
- [The Bitter Lesson of Agent Harnesses](https://browser-use.com/posts/bitter-lesson-agent-harnesses) - 代理框架的艱難教訓
