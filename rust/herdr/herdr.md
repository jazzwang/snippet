# Herdr 技術報告

> Herdr: 專為 AI 程式碼智能體設計的終端機多工器
> 
> 版本：0.9.5 (stable) | 更新時間：2026 年

---

## 一、概述

**Herdr** 是一款專為 AI 程式碼智能體（AI Coding Agents）設計的終端機多工器（Terminal Multiplexer）。與傳統的 tmux 或 zellij 不同，Herdr 特別針對 AI 智能體的運行情境進行優化，提供：

- **背景持續運行**：即使關閉終端機或斷線，智能體繼續工作
- **狀態感知**：自動偵測並顯示每個智能體的狀態（進行中/阻塞/閒置）
- **跨機器協作**：透過 SSH 連接多台機器，在同一視窗管理所有智能體
- **AI 原生設計**：CLI 與 Socket API 介面一致，支援智能體之間的互動與協調

### 核心特性

| 特性 | 說明 |
|------|------|
| **Always Running** | 不保持開啟的應用程式，而是背景運行的伺服器，終端機在其中運行 |
| **State Awareness** | 讀取每個終端機，標記智能體為 working、blocked 或 idle |
| **Agent-Native** | CLI 與 Socket API 為同一介面，智能體可直接調用 |
| **Runs What You Run** | 支援現有 AI 智能體的 CLI，不封裝或替換 |
| **All Machines** | 本機、遠端伺服器、租用的機器，一視同仁管理 |

---

## 二、安裝指南

Herdr 提供 Linux、macOS 和 Windows 的稳定版二進制檔案。

### 2.1 官方安裝指令

**Linux 或 macOS:**
```bash
curl -fsSL https://herdr.dev/install.sh | sh
```

**Windows:**
```powershell
powershell -ExecutionPolicy Bypass -c "irm https://herdr.dev/install.ps1 | iex"
```

如果端點安全軟體阻止無文件 PowerShell 指令，請使用：
```cmd
curl.exe -fsSLo install.cmd https://herdr.dev/install.cmd && install.cmd && del install.cmd
```

### 2.2 使用包管理工具安裝

**Homebrew:**
```bash
brew install herdr
```

**Mise:**
```bash
mise use -g herdr
```
如果顯示 `herdr not found in mise tool registry`，請更新 mise 後重試，或使用：
```bash
mise use -g github:herdrdev/herdr
```

**Nix:**
```bash
nix run github:herdrdev/herdr/v0.x
nix profile install github:herdrdev/herdr/v0.x
```

### 2.3 手動下載

從 [GitHub Releases](https://github.com/herdrdev/herdr/releases) 下載：

| 系統 | 檔案名稱 |
|------|----------|
| Linux x86_64 | `herdr-linux-x86_64` |
| Linux aarch64 | `herdr-linux-aarch64` |
| macOS Intel | `herdr-macos-x86_64` |
| macOS Apple Silicon | `herdr-macos-aarch64` |
| Windows x86_64 | `herdr-windows-x86_64.zip` |

**安裝步驟（Linux/macOS）:**
```bash
chmod +x herdr-linux-x86_64
mv herdr-linux-x86_64 ~/.local/bin/herdr
```

**Windows 注意事項:**
壓縮檔包含 `herdr.exe` 和其 app-local ConPTY  runtime，需保留整個解壓縮目錄，不可只複製 `herdr.exe`。

### 2.4 更新管理

Herdr 會自動檢查新版本並通知：

```bash
# 手動更新
herdr update

# 切換更新頻道
herdr channel set preview  # 預覽版
herdr channel set stable   # 穩定版
```

**重要：** 僅使用 Herdr 安裝器管理的直接安裝執行 `herdr update`。Homebrew、mise 和 Nix 安裝應透過各自的包管理器更新。

---

## 三、快速開始

### 3.1 啟動 Herdr

在任何專案目錄中啟動：

```bash
herdr
```

Herdr 會啟動或連接到預設的背景會話。您不需管理 socket。即使中斷連線，智能體仍會繼續運行。

### 3.2 创建工作区

當會話沒有工作區時，Herdr 會自動打開一個。工作區是專案級別的容器，容納標籤頁（tabs）、窗格（panes）和智能體。

**建議：** 給每個活躍專案一個獨立的工作區，讓側邊欄中的智能體狀態清晰可讀。

### 3.3 使用滑鼠操作

Herdr 是滑鼠原生的，操作從點擊開始：

- **點擊** 窗格、標籤頁、工作區和智能體以聚焦
- **拖曳分割邊框** 調整大小
- **右鍵點擊** 打開上下文選單（包含分割窗格、建立標籤頁）
- **拖曳選取文字** 複製到剪貼簿
- **雙擊單字** 直接複製，或按住第二次點擊並拖曳以整詞擴展選取

**Ctrl+點擊** 打開窗格內的連結（OSC 8 超連結和 http/https URL）

---

## 四、支援的 AI 程式碼智能體

Herdr 自動偵測和監控超過 20 個 AI 程式碼智能體和 CLI 工具。

### 4.1 完整整合支援

透過 `herdr integration install <name>` 安裝，支援狀態追蹤、會話儲存和恢復：

| 智能體 | CLI 指令 |
|--------|----------|
| Claude Code | `claude` |
| Codex | `codex` |
| GitHub Copilot CLI | `copilot` |
| Cursor Agent CLI | `cursor` |
| Devin CLI | `devin` |
| OpenCode | `opencode` |
| Hermes Agent | `hermes` |
| Pi | `pi` |
| OMP | `omp` |
| Droid | `droid` |
| Kimi Code CLI | `kimi` |
| Kilo Code CLI | `kilo` |
| Qoder CLI | `qodercli` |
| Qwen Code | `qwen` |
| Letta Code | `letta` |
| MastraCode | `mastracode` |
| Grok CLI | `grok` |
| Antigravity CLI | `antigravity-cli` |

### 4.2 狀態偵測支援

Herdr 直接從畫面/程式輸出追蹤即時狀態，無需額外設定：

- Amp
- Kiro CLI
- Maki
- Gemini CLI
- Cline

### 4.3 智能體狀態

Herdr 讀取每個終端機，標記每個智能體為：

- **working**：智能體正在執行程式碼、測試或指令
- **blocked**：智能體已暫停，等待用戶輸入、提示批准或反饋
- **idle**：智能體已完成任務，等待新指示

側邊欄會顯示每個工作區中智能體的狀態，讓您清楚知道哪個專案需要您。

### 4.4 安裝 Herdr 支援到智能體

透過以下指令安裝 Herdr 技能：

```bash
npx skills add herdrdev/herdr --skill herdr -g
```

或在終端機窗格中設定環境變數 `HERDR_ENV=1`，智能體即可使用 Herdr CLI/Socket API：

- 檢查相鄰窗格
- 啟動工作智能體
- 發送提示
- 等待其他智能體完成任務

---

## 五、工作流程

### 5.1 本機工作

在專案目錄中啟動 Herdr：

```bash
herdr
```

Herdr 會自動啟動或連接到本機背景會話。不需管理 socket。在窗格中照常運行 shell、伺服器、測試和智能體。

**中斷連線：** 用 `ctrl+b q` 中斷連線。窗格會繼續運行。

**重新連線：**
```bash
herdr
```

**結束會話：**
```bash
herdr server stop
```

### 5.2 透過 SSH 遠端工作

SSH 到擁有程式碼和憑證的機器，然後在該處運行 Herdr：

```bash
ssh you@server
herdr
```

這與終端機多工器的用法相同。您的 shell 在遠端，Herdr 伺服器在遠端，智能體和窗格都在遠端機器上運行。

**中斷連線：** 用 `ctrl+b q` 中斷並斷開連線，之後再 SSH 回來並運行 `herdr`。

### 5.3 從本機終端機遠端工作

透過 SSH 附加而不先打開 shell：

```bash
herdr --remote workbox
herdr --remote ssh://you@server:2222
```

遠端伺服器保持窗格運行，並透過 SSH 發送終端機內容和會話狀態。您的本機 Herdr 使用本機主題和顯示設定繪製 UI。

**使用此方法的時機：** 希望遠端會話感覺像本機時。客戶端在您的機器上運行，因此本機桌面功能（如圖片剪貼簿貼上）可橋接到遠端伺服器。

如果先 SSH 然後在伺服器上運行 `herdr`，Herdr 完全在該伺服器上運行，無法讀取本機桌面剪貼簿。

### 5.4 重複目標設定

為重複使用的遠端目標，將其放入 SSH 配置：

```bash
Host workbox
  HostName server.example.com
  User you
  Port 2222
```

然後附加：
```bash
herdr --remote workbox
```

### 5.5 多台機器單一視窗

在同一視窗中保持 Local 和多個 SSH 機器，使用：

```bash
herdr machine add <host> --label <label>
```

詳細資訊請參閱 [Connecting Machines](https://herdr.dev/docs/connecting-machines/)。

---

## 六、配置設定

Herdr 透過 `config.toml` 檔案讀取所有規範鍵。

### 6.1 設定檔位置

- **macOS / Linux**：`~/.config/herdr/config.toml`
- **Windows**：`%APPDATA%\herdr\config.toml`

### 6.2 快速匯出預設設定

```bash
# 印出完整預設配置
herdr --default-config

# 直接導出並儲存為設定檔
herdr --default-config > ~/.config/herdr/config.toml
```

### 6.3 常用管理指令

| 指令 | 說明 |
|------|------|
| `herdr server reload-config` | 重新載入運行中的設定檔（無需重啟窗格） |
| `herdr config reset-keys` | 備份當前 config.toml 並將按鍵綁定重置為預設值 |
| `herdr channel show` | 查看當前的更新頻道（stable / preview） |
| `herdr channel set stable` | 切換更新頻道為穩定版 |

### 6.4 主要配置區塊

#### 引導與全局選項

```toml
# 是否顯示第一次啟動的引導教學
onboarding = false
```

#### 主題與外觀

```toml
[theme]
# 內建主題：catppuccin, terminal, tokyo-night, dracula, nord,
#           gruvbox, one-dark, solarized, kanagawa, rose-pine, vesper
name = "catppuccin"

# 自動跟隨系統切換深淺色主題
auto_switch = false
dark_name = "catppuccin"
light_name = "rose-pine"

# 自訂個別顏色 Token（覆蓋主題配色）
[theme.custom]
accent = "#f5c2e7"
panel_bg = "#1e1e2e"
```

#### 終端機設定

```toml
[terminal]
# 新建 Pane 時使用的預設 Shell（留空則自動讀取 $SHELL）
default_shell = ""

# 啟動模式："auto", "login", 或 "non_login"
shell_mode = "auto"

# 新建 Pane / Tab / Workspace 時的工作目錄繼承策略：
# "follow", "home", "current", 或指定固定路徑
new_cwd = "follow"
```

#### 使用者介面與通知

```toml
[ui]
# 側邊欄展開時的列寬（字元數）
sidebar_width = 30

# 側邊欄預設是否收合
sidebar_collapsed = false

# 啟用滑鼠捕獲（點擊切換、拖曳調整分割邊框、選取複製）
mouse_capture = true

# Agent 完成或等待輸入時的 Toast 彈出通知設定
[ui.toast]
delivery = "herdr"       # "herdr" 或 "system"
delay_seconds = 1        # 停留幾秒後才發送通知

# 個別 Agent 聲音提示切換
[ui.sound.agents]
claude = "on"
droid = "off"
```

#### 按鍵綁定

```toml
[keys]
# 設定前綴按鍵（預設為 ctrl+b）
prefix = "ctrl+b"

# 視窗與分頁操作
new_tab = "prefix+c"
next_tab = "prefix+n"
previous_tab = "prefix+p"

# 分割與窗格導航
split_horizontal = "prefix+minus"  # 水平分割
split_vertical = "prefix+v"        # 垂直分割
focus_pane_left = "prefix+h"
focus_pane_right = "prefix+l"
focus_pane_up = "prefix+k"
focus_pane_down = "prefix+j"

# 工作區與系統操作
reload_config = "prefix+shift+r"
detach = "prefix+q"
toggle_sidebar = "prefix+b"
```

**自訂命令快捷鍵範例：**
```toml
[[keys.command]]
key = "prefix+g"
command = "git status"
```

#### 伺服器與更新

```toml
[server]
# 當沒有用戶端連接時，背景虛擬終端機採用的預設解析度
headless_cols = 120
headless_rows = 40

[update]
channel = "stable"       # "stable" 或 "preview"
version_check = true     # 自動檢查版本更新
```

### 6.5 完整範例配置

```toml
# ~/.config/herdr/config.toml
onboarding = false

[theme]
name = "catppuccin"

[terminal]
new_cwd = "follow"

[ui.toast]
delivery = "herdr"
delay_seconds = 1

[keys]
prefix = "ctrl+a"  # 使用 Ctrl+A 作為前綴鍵
new_tab = "prefix+c"
split_vertical = "prefix+v"
split_horizontal = "prefix+minus"
reload_config = "prefix+shift+r"

[update]
channel = "stable"
```

---

## 七、按鍵快捷鍵參考

Herdr 採用 tmux 風格的**前綴鍵（Prefix）**機制。預設前綴鍵為 `ctrl+b`，按下並釋放前綴鍵後，再按下對應的操作鍵。

### 7.1 通用與內建幫助

| 快捷鍵 | 動作 |
|--------|------|
| `prefix + ?` | 查看 Herdr 內即時有效的按鍵綁定 |
| `prefix + s` | 打開設定選單 |
| `prefix + shift + r` | 重新載入 `config.toml`（即時生效） |
| `prefix + o` | 聚焦目前可見的通知目標 |

### 7.2 窗格操作

| 快捷鍵 | 動作 |
|--------|------|
| `prefix + v` | 垂直分割窗格（向右分割） |
| `prefix + -` | 水平分割窗格（向下分割） |
| `prefix + h` | 聚焦左側窗格 |
| `prefix + j` | 聚焦下方窗格 |
| `prefix + k` | 聚焦上方窗格 |
| `prefix + l` | 聚焦右側窗格 |
| `prefix + [` | 進入複製模式 |

### 7.3 標籤頁操作

| 快捷鍵 | 動作 |
|--------|------|
| `prefix + c` | 建立新標籤頁 |
| `prefix + n` | 下一個標籤頁 |
| `prefix + p` | 上一個標籤頁 |
| `prefix + ,` | 重新命名目前標籤頁 |

### 7.4 工作區與會話

| 快捷鍵 | 動作 |
|--------|------|
| `prefix + w` | 打開工作區選取器/導航器 |
| `prefix + shift + n` | 建立新工作區 |
| `prefix + shift + w` | 重新命名選取的工作區 |
| `prefix + shift + d` | 關閉選取的工作區 |
| `prefix + g` | 打開會話導航器（goto） |
| `prefix + q` | 中斷用戶端（背景會話仍運行） |

### 7.5 常見操作

| 快捷鍵 | 動作 |
|--------|------|
| `prefix + +` | 建立新智能體 |
| `prefix + /` | 搜尋智能體 |
| `prefix + .` | 中斷目前智能體 |

---

## 八、測試範例

### 8.1 基本工作流程測試

#### 測試 1：啟動 Herdr 並建立窗格

```bash
# 步驟 1：啟動 Herdr
herdr

# 步驟 2：建立新的 shell 窗格（右鍵選單或 prefix+v）
# 步驟 3：在窗格中執行指令
```

**預期結果：**
- Herdr 視窗打開，顯示預設 shell
- 右鍵選單可用
- 可執行任何 shell 指令

#### 測試 2：啟動 AI 智能體

```bash
# 在 Herdr 窗格中執行：
claude

# 或在側邊欄點擊 AI 智能體圖示
```

**預期結果：**
- 智能體在窗格中啟動
- 側邊欄顯示智能體狀態為 `working`
- 智能體開始執行其預設任務

#### 測試 3：智能體狀態偵測

```bash
# 啟動多個智能體在不同窗格：
claude        # 執行任務 A
codex         # 執行任務 B
pi            # 執行任務 C

# 觀察側邊欄狀態
```

**預期結果：**
- 每個智能體顯示正確狀態：
  - `working`：正在執行
  - `blocked`：等待輸入/批准
  - `idle`：已完成任務
- 狀態會隨智能體行為即時更新

### 8.2 中斷連線測試

#### 測試 4：中斷連線並重新連線

```bash
# 步驟 1：啟動 Herdr 並啟動智能體
herdr
claude  # 執行長時間任務

# 步驟 2：中斷連線（ctrl+b q 或關閉視窗）
# 步驟 3：等待幾分鐘
# 步驟 4：重新連線
herdr
```

**預期結果：**
- 智能體仍在運行，不會中斷
- 視窗佈局已恢復
- 智能體從中斷處繼續執行

#### 測試 5：結束會話

```bash
# 步驟 1：確認所有智能體完成或可中斷
herdr

# 步驟 2：中斷所有智能體
herdr pane input --all --ctrl+d

# 步驟 3：結束會話
herdr server stop
```

**預期結果：**
- 所有窗格中的程式停止
- 伺服器不再運行

### 8.3 遠端工作測試

#### 測試 6：SSH 遠端工作

```bash
# 步驟 1：SSH 到遠端伺服器
ssh you@server

# 步驟 2：在遠端運行 Herdr
herdr

# 步驟 3：啟動智能體
claude

# 步驟 4：中斷 SSH 連線（ctrl+d）
# 步驟 5：重新 SSH
ssh you@server
herdr
```

**預期結果：**
- 智能體在遠端持續運行
- 重新連線後視窗狀態恢復

#### 測試 7：herdr --remote 模式

```bash
# 步驟 1：設定 SSH config
Host workbox
  HostName server.example.com
  User you
  Port 2222

# 步驟 2：使用 --remote 模式
herdr --remote workbox

# 步驟 3：啟動智能體
claude

# 步驟 4：中斷連線
herdr pane input --all --ctrl+d
# 或直接關閉視窗
```

**預期結果：**
- 本機 Herdr 客戶端顯示遠端會話
- 遠端智能體持續運行
- 剪貼簿功能可用（圖片貼上等）

### 8.4 配置測試

#### 測試 8：主題切換

```bash
# 步驟 1：查看當前主題
herdr config show theme

# 步驟 2：修改 ~/.config/herdr/config.toml
[theme]
name = "dracula"

# 步驟 3：重新載入配置
herdr server reload-config
# 或在 Herdr 內按 prefix+shift+r
```

**預期結果：**
- 介面主題立即改變為 dracula
- 顏色方案正確應用

#### 測試 9：前綴鍵自訂

```bash
# 步驟 1：修改 config.toml
[keys]
prefix = "ctrl+a"

# 步驟 2：重新載入
herdr server reload-config
```

**預期結果：**
- 所有快捷鍵現在使用 `ctrl+a` 作為前綴
- 原有 `ctrl+b` 快捷鍵不再有效

### 8.5 多台機器測試

#### 測試 10：添加多台機器

```bash
# 步驟 1：添加本機機器
herdr machine add local

# 步驟 2：添加遠端機器
herdr machine add workbox --label "Workbox"
herdr machine add server1 --label "Server 1"
herdr machine add server2 --label "Server 2"

# 步驟 3：啟動 Herdr
herdr

# 步驟 4：觀察側邊欄
# 應顯示所有連通的機器
```

**預期結果：**
- 側邊欄顯示所有機器狀態
- 可切換到不同機器
- 每台機器的智能體獨立運行

---

## 九、故障排除

### 9.1 常見問題

#### 問題 1：Herdr 無法啟動

```bash
# 檢查 Herdr 是否在 PATH 上
which herdr

# 檢查版本
herdr --version

# 查看日誌
herdr --verbose
```

#### 問題 2：智能體狀態顯示不正確

```bash
# 重新載入配置
herdr server reload-config

# 檢查智能體整合
herdr integration list

# 重新安裝智能體
herdr integration install claude
```

#### 問題 3：遠端連線失敗

```bash
# 檢查 SSH 配置
herdr machine list

# 測試連線
herdr --remote --test servername

# 檢查 SSH config
cat ~/.ssh/config
```

#### 問題 4：剪貼簿功能不工作

```bash
# 檢查 mouse_capture 設定
herdr config show ui.mouse_capture

# 應為 true
```

### 9.2 重置設定

```bash
# 重置按鍵綁定到預設值
herdr config reset-keys

# 重置所有設定到預設
herdr config reset
```

---

## 十、參考資源

### 官方文件
- [Herdr 主頁](https://herdr.dev/)
- [快速開始](https://herdr.dev/docs/quick-start/)
- [安裝指南](https://herdr.dev/docs/install/)
- [使用方式](https://herdr.dev/docs/how-to-work/)
- [配置參考](https://herdr.dev/docs/config-reference/)
- [按鍵快捷鍵](https://herdr.dev/docs/keyboard/)
- [智能體支援](https://herdr.dev/docs/agents/)
- [整合](https://herdr.dev/docs/integrations/)
- [多台機器](https://herdr.dev/docs/connecting-machines/)
- [會話狀態](https://herdr.dev/docs/session-state/)

### GitHub
- [herdrdev/herdr 官方儲存庫](https://github.com/herdrdev/herdr)
- [herdrdev/herdr  Releases](https://github.com/herdrdev/herdr/releases)

### 中文資源
- [最懂 AI 的 Herdr 使用教學](https://most.tw/posts/ainews/herdr-agent-multiplexer/)
- [Herdr 完整設定與使用教程](https://github.com/joeseesun/herdr-guide/blob/main/Herdr_%E8%BD%AF%E4%BB%B6%E5%85%A8%E9%9D%A2%E8%B0%83%E7%A0%94%E4%B8%8E%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B.md)
- [Herdr 捷徑 Cheat Sheet](https://getmoshi.app/articles/herdr-cheatsheet)
- [ithome Herdr 介紹](https://ithelp.ithome.com.tw/articles/10407114)

---

## 十一、總結

Herdr 是一款為 AI 程式碼智能體量身打造的終端機多工器，具有以下優勢：

1. **無需中斷即可離線**：即使關閉終端機或斷線，智能體繼續工作
2. **智能體狀態感知**：自動偵測並顯示每個智能體的狀態
3. **跨機器協作**：在同一視窗管理多台機器的智能體
4. **AI 原生設計**：支援超過 20 個主流 AI 智能體
5. **滑鼠優先操作**：降低學習曲線，提高使用效率
6. **高度可配置**：支援自訂主題、快捷鍵和行為

無論是在本機開發、遠端伺服器工作，還是透過手機 SSH 連線，Herdr 都能提供一致的使用體驗。

---

**參考文獻：**
1. [herdr.dev/docs/quick-start/](https://herdr.dev/docs/quick-start/)
2. [herdr.dev/docs/install/](https://herdr.dev/docs/install/)
3. [herdr.dev/docs/how-to-work/](https://herdr.dev/docs/how-to-work/)
4. [herdr.dev/docs/config-reference/](https://herdr.dev/docs/config-reference/)
5. [herdr.dev/docs/agents/](https://herdr.dev/docs/agents/)
6. [herdr.dev/docs/keyboard/](https://herdr.dev/docs/keyboard/)
7. [herdr.dev/docs/connecting-machines/](https://herdr.dev/docs/connecting-machines/)
8. [herdr.dev/docs/session-state/](https://herdr.dev/docs/session-state/)
9. [GitHub herdrdev/herdr](https://github.com/herdrdev/herdr)
10. [herdr.dev/llms.txt](https://herdr.dev/llms.txt)

---

*報告撰寫日期：2026 年*
*Herdr 版本：0.9.5 (stable)*
