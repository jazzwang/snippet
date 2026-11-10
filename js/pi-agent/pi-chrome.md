# pi-chrome 安裝與設定指南

## 快速開始（60 秒）

```bash
# 1. 系統終端機安裝
pi install npm:pi-chrome
```

```text
# 2. Pi 內部啟動設定
/chrome onboard
```

```text
# 3. 授權當前 Pi _session
/chrome authorize
```

**完成！現在 Pi 可以控制你的 Chrome 了。**

---

## 完整步驟說明

### 步驟 1：系統終端機安裝

```bash
# 在系統終端機（Terminal）輸入
pi install npm:pi-chrome
```

這會：
- 下載 `pi-chrome` 套件（版本 0.15.57）
- 套用 Pi manifest
- 準備 Chrome 擴充套件資源

**注意：** `pi install` 命令必須在**系統終端機**輸入，不是在 Pi 內部。

---

### 步驟 2：啟動 Chrome Bridge

```text
# 在 Pi 輸入（不是終端機！）
/chrome onboard
```

這會：
1. 自動開啟 `chrome://extensions` 網頁
2. 在 Finder/檔案總管顯示 `browser-extension/` 資料夾
3. 將資料夾路徑複製到剪貼簿

#### 安裝擴充套件

在打開的 `chrome://extensions` 頁面中：

1. 右上角開啟 **「開發者模式」** (Developer mode)
2. 拖曳 `browser-extension/` 資料夾到頁面
3. 等待安裝完成（擴充套件名稱：「Pi Chrome Connector」）

**重要：** 若使用 macOS，步驟 2 會自動用 Finder 顯示資料夾並複製路徑到剪貼簿。

---

### 步驟 3：授權 Pi 存取 Chrome

```text
# 在 Pi 輸入
/chrome authorize
```

這會：
- 建立 Pi 與 Chrome 的橋接連接
- 允許 Pi 控制你的 Chrome profile（cookies、登入狀態、extensions）
- 橋接監聽 `127.0.0.1:17318`（僅本地迴圈）

**安全提示：**
- 橋接僅綁定到 `127.0.0.1`，不外洩到網路
- 需要 `/chrome authorize` 才允許存取
- 可以 `/chrome revoke` 隨時撤銷授權

---

### 步驟 4：驗證安裝

#### 檢查橋接狀態

```text
/chrome doctor
```

預期輸出範例：

```
Performing Chrome bridge health check
pi-chrome v0.15.57
• Local bridge 127.0.0.1:17318: connected
• Chrome extension: installed
• Profile: /Users/yourname/Library/Application\ Support/Google/Chrome/Default
• Tabs detected: 3
• Authorization: active
```

#### 測試基本功能

在 Pi 中嘗試以下指令：

```text
# 列出所有 Chrome tabs
/chrome tab list

# 查看特定 tab 內容
/chrome tab snapshot <tab-id>

# 取得 tab 標題
/chrome tab title <tab-id>

# 擷取 tab 截圖
/chrome tab screenshot <tab-id>

# 開啟新 tab
/chrome tab open "https://example.com"

# 關閉 tab
/chrome tab close <tab-id>
```

---

## 常見使用情境

### 情境 1：Debug 已登入的網站

```text
# 尋找已登入的 GitHub 通知 tab
Use chrome_tab list to find my GitHub notifications tab.

# 擷取內容
chrome_snapshot it.

# 檢查是否有未處理的 PR
chrome_get_text @notifications-list
```

### 情境 2：檢查 Linear Standup

```text
chrome_snapshot my Linear standup tab
chrome_get_text @task-list
chrome_get_text @blocked-tasks
chrome_get_text @completed-tasks
chrome_get_text @pending-tasks
```

### 情境 3：表單填寫

```text
# 開啟 Google 搜尋
chrome_tab open "https://www.google.com"

# 等待頁面載入
sleep 1

# 填寫搜尋欄
chrome_fill @search-box "Pi agent browser control comparison"

# 按下 Enter
chrome_press Enter
```

---

## 進階設定

### 支援的瀏覽器

✅ **支援：**
- Chrome（任何版本）
- Edge（Chromium 版）
- Brave
- Arc
- Vivaldi
- 任何其他 Chromium 瀏覽器

❌ **不支援：**
- Firefox（不同 extension 模型）
- WebKit 瀏覽器

### Incognito 模式

預設情況下，`pi-chrome` **不支援** Incognito 模式，因為擴充套件需要明確的「Allow in incognito」權限。

若要使用 Incognito：

1. 在 `chrome://extensions` 中，找到「Pi Chrome Connector」
2. 開啟 **「允許在私密視窗中執行」**
3. 注意：不建議用於敏感工作

### 更新套件

套件更新時：

- 若新增 Chrome 權限，需要重新 `/chrome authorize`
- 擴充套件會自動更新（除非手動重新載入）

### 撤銷授權

```text
# 隨時撤銷授權
/chrome revoke

# 重新授權
/chrome authorize
```

---

## 故障排除

### 問題 1：`/chrome doctor` 顯示未連接

**解決方案：**

```text
# 檢查擴充套件是否安裝
chrome://extensions

# 確認開發者模式開啟
# 確認「Pi Chrome Connector」已啟用
```

### 問題 2：`/chrome authorize` 失敗

**可能原因：**
- 未先執行 `/chrome onboard`
- 擴充套件未安裝
- 未開啟開發者模式

**解決方案：**

```text
# 重新啟動 onboard
/chrome onboard

# 重新授權
/chrome authorize
```

### 問題 3：無法控制特定 tab

**檢查：**
- 該 tab 是否已被其他 process 鎖定
- 該 tab 是否為 Incognito
- 該 tab 是否被 chrome://extensions 阻擋

### 問題 4：瀏覽器相容性問題

**檢查：**
- 確認使用的是 Chromium 瀏覽器
- 確認版本不過舊（建議 Chrome 90+）

---

## 安全考量

### 威脅模型

`pi-chrome` 是開發者工具，需知情安裝。它**不設計**防護：

- ❌ 惡意頁面試圖偵測或逃逸自動化（標準瀏覽器安全邊界適用）
- ❌ 同機其他 process 的存取（橋接僅綁定 `127.0.0.1:17318`）

**風險控制：**
- 橋接僅本地迴圈，不洩漏到網路
- 需要 `/chrome authorize` 才允許存取
- 可 `/chrome revoke` 隨時撤銷

### 進階安全建議

如需更嚴格的安全控制，建議：
- 在獨立 OS 用戶帳號運行 `pi-chrome`
- 使用虛擬環境隔離敏感工作

---

## 實戰範例

### PR Triage 工作流程

```text
# 尋找 GitHub 通知 tab
Use chrome_tab list to find my GitHub notifications tab.

# 擷取內容
chrome_snapshot it.

# 分組 PRs
Group PRs by:
- awaiting my review
- blocked on me (changes requested back)
- mergeable (approved + green CI)

# 輸出 5 bullet ranked triage
Output a 5-bullet ranked triage. Do not click anything.
```

### Daily Standup 檢查

```text
chrome_snapshot my Linear standup tab
chrome_get_text @task-list
chrome_get_text @blocked-tasks
chrome_get_text @completed-tasks
chrome_get_text @pending-tasks
chrome_get_text @time-spent
```

### 資料擷取

```text
# 開啟目標網站
chrome_tab open "https://example.com/data"

# 等待載入
sleep 2

# 擷取表格
chrome_get_text @table-1
chrome_get_text @table-2

# 截圖存檔
chrome_screenshot /tmp/data-screenshot.png
```

---

## 相關資源

- **官方網站：** [pi.dev/packages/pi-chrome](https://pi.dev/packages/pi-chrome)
- **GitHub：** [github.com/tianrendong/pi-chrome](https://github.com/tianrendong/pi-chrome)
- **FAQ：** [docs/FAQ.md](https://github.com/tianrendong/pi-chrome/blob/main/docs/FAQ.md)
- **範例：** [docs/EXAMPLES.md](https://github.com/tianrendong/pi-chrome/blob/main/docs/EXAMPLES.md)
- **架構：** [docs/ARCHITECTURE.md](https://cdn.jsdelivr.net/npm/pi-chrome@0.15.57/docs/ARCHITECTURE.md)
- **安全性：** [SECURITY.md](https://github.com/tianrendong/pi-chrome/blob/main/SECURITY.md)

---

## 快速命令總覽

| 命令 | 說明 | 執行位置 |
|------|------|---------|
| `pi install npm:pi-chrome` | 安裝套件 | 系統終端機 |
| `/chrome onboard` | 啟動橋接並開啟設定頁面 | Pi 內部 |
| `/chrome authorize` | 授權 Pi 存取 Chrome | Pi 內部 |
| `/chrome revoke` | 撤銷授權 | Pi 內部 |
| `/chrome doctor` | 檢查橋接狀態 | Pi 內部 |
| `chrome_tab list` | 列出所有 tabs | Pi 內部 |
| `chrome_tab snapshot <id>` | 擷取 tab 內容 | Pi 內部 |
| `chrome_tab title <id>` | 取得 tab 標題 | Pi 內部 |
| `chrome_tab open "url"` | 開啟新 tab | Pi 內部 |
| `chrome_tab close <id>` | 關閉 tab | Pi 內部 |
| `chrome_fill @selector "text"` | 填寫表單 | Pi 內部 |
| `chrome_press <key>` | 按下鍵 | Pi 內部 |
| `chrome_screenshot <path>` | 截圖存檔 | Pi 內部 |

---

*最後更新：2025*
