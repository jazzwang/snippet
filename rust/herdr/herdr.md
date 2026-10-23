# Herdr

- Git Repo: https://github.com/herdrdev/herdr
- 官網：https://herdr.dev/

---

## 什麼是 Herdr？

Herdr 是專為 AI 程式碼代理（AI Coding Agents）設計的終端機多工器，版本 0.9.5（穩定版），2026 年更新。

跟傳統的 tmux 或 zellij 不太一樣，Herdr 是特別針對 AI 代理的運作環境優化的。簡單來說，它解決的是這些問題：

- 代理跑著跑著，你關掉終端機或斷線，代理就停了？Herdr 讓代理在背景繼續跑
- 不知道哪個代理卡住了、哪個在等你的輸入？Herdr 會自動偵測狀態並顯示出來
- 有好幾台機器要管理？Herdr 能透過 SSH 把多台機器整合到一個視窗裡管理
- AI 代理之間需要互相配合？Herdr 的 CLI 和 Socket API 是一樣的，代理可以直接跟其他代理溝通

### 核心設計理念

| 概念 | 實際做法 |
|------|----------|
| **Always Running** | 不把你關掉的程式當「伺服器」，而是讓它在背景繼續跑，你關掉終端機它還照跑 |
| **State Awareness** | 讀取每個終端機畫面，標記代理是「正在執行」、「卡住等輸入」或「閒著」 |
| **Agent-Native** | CLI 和 Socket API 是一樣的介面，代理可以直接呼叫 |
| **Runs What You Run** | 支援你已經在用的 AI 代理 CLI，不會封裝或替換掉 |
| **All Machines** | 本機、遠端伺服器、租用的機器，一視同仁管理 |

---

## 安裝

Herdr 有 Linux、macOS 和 Windows 的穩定版二位元檔案。

### 官方安裝指令

**Linux 或 macOS:**
```bash
curl -fsSL https://herdr.dev/install.sh | sh
```

**Windows:**
```powershell
powershell -ExecutionPolicy Bypass -c "irm https://herdr.dev/install.ps1 | iex"
```

如果遇到資安設定跑不動，試試：
```cmd
curl.exe -fsSLo install.cmd https://herdr.dev/install.cmd && install.cmd && del install.cmd
```

### 用套件管理工具裝

**Homebrew:**
```bash
brew install herdr
```

**Mise:**
```bash
mise use -g herdr
```
如果看到 `herdr not found in mise tool registry`，先更新 mise 再試，或直接：
```bash
mise use -g github:herdrdev/herdr
```

**Nix:**
```bash
nix run github:herdrdev/herdr/v0.x
nix profile install github:herdrdev/herdr/v0.x
```

### 手動下載

去 [GitHub Releases](https://github.com/herdrdev/herdr/releases) 下載：

| 系統 | 檔案名稱 |
|------|----------|
| Linux x86_64 | `herdr-linux-x86_64` |
| Linux aarch64 | `herdr-linux-aarch64` |
| macOS Intel | `herdr-macos-x86_64` |
| macOS Apple Silicon | `herdr-macos-aarch64` |
| Windows x86_64 | `herdr-windows-x86_64.zip` |

**裝到系統（Linux/macOS）:**
```bash
chmod +x herdr-linux-x86_64
mv herdr-linux-x86_64 ~/.local/bin/herdr
```

**Windows 注意事項:**
壓縮檔內有 `herdr.exe` 加上 app-local ConPTY runtime，要把整個解壓縮目錄保留，不能只複製 `herdr.exe`。

### 更新

Herdr 會自動檢查新版本並提醒你：

```bash
# 手動更新
herdr update

# 切換更新頻道
herdr channel set preview  # 預覽版
herdr channel set stable   # 穩定版
```

**重點：** 只有用 Herdr 安裝器裝的直接安裝，才用 `herdr update`。用 Homebrew、mise 和 Nix 裝的，要用各自套件管理工具來更新。

---

## 快速開始

### 啟動 Herdr

在任何專案目錄中執行：
```bash
herdr
```

Herdr 會啟動或連到預設的背景會話。你不用管 socket，就算斷線代理還是繼續跑。

### 工作區（Workspace）

如果會話沒工作區，Herdr 會自動開一個。工作區是專案級的容器，裡面有標籤頁、窗格和代理。

**建議：** 每個活躍專案給一個獨立工作區，這樣側邊欄的代理狀態才看得清楚。

### 滑鼠操作

Herdr 原生就支援滑鼠，操作從點擊開始：

- **點擊** 窗格、標籤頁、工作區、代理來聚焦
- **拖曳分割邊框** 調整大小
- **右鍵點擊** 開上下文選單（裡面有分割窗格、建立標籤頁）
- **拖曳選取文字** 複製到剪貼簿
- **雙擊單字** 直接複製，或按住第二次點擊並拖曳來整詞選取

**Ctrl+點擊** 打開窗格內的連結（OSC 8 超連結和 http/https URL）

---

## 支援的 AI 程式碼代理

Herdr 自動偵測和監控超過 20 個 AI 程式碼代理和 CLI 工具。

### 完整整合

用 `herdr integration install <name>` 安裝，支援狀態追蹤、會話儲存和恢復：

| 代理 | CLI 指令 |
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

### 狀態偵測（不用裝）

Herdr 直接從畫面或程式輸出追蹤即時狀態，不用額外設定：

- Amp
- Kiro CLI
- Maki
- Gemini CLI
- Cline

### 代理狀態

Herdr 讀取每個終端機，標記代理狀態：

- **working**：代理正在跑程式碼、測試或指令
- **blocked**：代理暫停，等你的輸入、批准或反饋
- **idle**：代理完成任務，等新的指示

側邊欄會顯示每個工作區中代理的狀態，讓你清楚知道哪個專案需要你的 attention。

### 讓代理支援 Herdr

用這行安裝 Herdr 技能：
```bash
npx skills add herdrdev/herdr --skill herdr -g
```

或在終端機窗格中設定環境變數 `HERDR_ENV=1`，代理就可以用 Herdr CLI/Socket API：

- 檢查相鄰窗格
- 啟動工作代理
- 發送提示
- 等其他代理完成任務

---

## 工作模式

### 本機工作

在專案目錄中啟動：
```bash
herdr
```

Herdr 自動啟動或連到本機背景會話，不用管 socket。在窗格中照常跑 shell、伺服器、測試和代理。

**斷線：** 用 `ctrl+b q` 斷線，窗格繼續跑。

**重連：**
```bash
herdr
```

**結束會話：**
```bash
herdr server stop
```

### SSH 遠端工作

SSH 到有程式碼和憑證的機器，在那邊跑 Herdr：
```bash
ssh you@server
herdr
```

跟終端機多工器用法一樣。你的 shell 在遠端，Herdr 伺服器在遠端，代理和窗格都在遠端機器跑。

**斷線：** 用 `ctrl+b q` 斷開連線，之後再 SSH 回來跑 `herdr`。

### 從本機終端機遠端工作

透過 SSH 附加而不先開 shell：
```bash
herdr --remote workbox
herdr --remote ssh://you@server:2222
```

遠端伺服器保持窗格跑，透過 SSH 發終端機內容和會話狀態。你的本機 Herdr 用本機主題和顯示設定畫 UI。

**什麼時候用這個：** 希望遠端會話感覺像本機時。客戶端在你的機器跑，所以本機桌面功能（如圖片剪貼簿貼上）可以橋接到遠端伺服器。

如果你先 SSH 然後在伺服器上跑 `herdr`，Herdr 完全在那邊跑，讀不到本機桌面剪貼簿。

### 重複目標設定

對重複使用的遠端目標，放進 SSH config：
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

### 多台機器單一視窗

在同一視窗保持 Local 和多個 SSH 機器：
```bash
herdr machine add <host> --label <label>
```

詳細看 [Connecting Machines](https://herdr.dev/docs/connecting-machines/)。

---

## 配置

Herdr 用 `config.toml` 讀設定。

### 設定檔在哪

- **macOS / Linux**：`~/.config/herdr/config.toml`
- **Windows**：`%APPDATA%\herdr\config.toml`

### 匯出預設設定

```bash
# 印完整預設配置
herdr --default-config

# 直接導出並存成設定檔
herdr --default-config > ~/.config/herdr/config.toml
```

### 常用管理指令

| 指令 | 說明 |
|------|------|
| `herdr server reload-config` | 重新載入運行中的設定檔（不用重啟窗格） |
| `herdr config reset-keys` | 備份當前 config.toml 並將按鍵綁定重置為預設 |
| `herdr channel show` | 看目前更新頻道（stable / preview） |
| `herdr channel set stable` | 切更新頻道為穩定版 |

### 主要設定區塊

#### 引導與全局

```toml
# 第一次啟動要不要顯示教學
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
# 新建 Pane 時用的預設 Shell（空則自動讀 $SHELL）
default_shell = ""

# 啟動模式："auto", "login", 或 "non_login"
shell_mode = "auto"

# 新建 Pane / Tab / Workspace 時的工作目錄繼承策略：
# "follow", "home", "current", 或指定固定路徑
new_cwd = "follow"
```

#### 介面與通知

```toml
[ui]
# 側邊欄展開時的列寬（字元數）
sidebar_width = 30

# 側邊欄預設要不要收合
sidebar_collapsed = false

# 啟用滑鼠捕獲（點擊切換、拖曳調整分割邊框、選取複製）
mouse_capture = true

# Agent 完成或等輸入時的 Toast 通知
[ui.toast]
delivery = "herdr"       # "herdr" 或 "system"
delay_seconds = 1        # 停留幾秒後才發通知

# 個別 Agent 聲音提示
[ui.sound.agents]
claude = "on"
droid = "off"
```

#### 按鍵綁定

```toml
[keys]
# 前綴鍵（預設 ctrl+b）
prefix = "ctrl+b"

# 視窗與分頁
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

# 工作區與系統
reload_config = "prefix+shift+r"
detach = "prefix+q"
toggle_sidebar = "prefix+b"
```

**自訂命令範例：**
```toml
[[keys.command]]
key = "prefix+g"
command = "git status"
```

#### 伺服器與更新

```toml
[server]
# 沒用戶端時背景虛擬終端機預設解析度
headless_cols = 120
headless_rows = 40

[update]
channel = "stable"       # "stable" 或 "preview"
version_check = true     # 自動檢查更新
```

### 完整範例

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
prefix = "ctrl+a"  # 用 Ctrl+A 當前綴
new_tab = "prefix+c"
split_vertical = "prefix+v"
split_horizontal = "prefix+minus"
reload_config = "prefix+shift+r"

[update]
channel = "stable"
```

---

## 按鍵捷徑

Herdr 用 **前綴鍵（Prefix）** 機制。預設前綴是 `ctrl+b`，按下並釋放後，再按對應操作。

### 通用與幫助

| 捷徑 | 動作 |
|--------|------|
| `prefix + ?` | 看 Herdr 當前有效的按鍵綁定 |
| `prefix + s` | 開設定選單 |
| `prefix + shift + r` | 重新載入 `config.toml`（即時生效） |
| `prefix + o` | 聚焦目前可見的通知目標 |

### 窗格操作

| 捷徑 | 動作 |
|--------|------|
| `prefix + v` | 垂直分割窗格（向右） |
| `prefix + -` | 水平分割窗格（向下） |
| `prefix + h` | 聚焦左側窗格 |
| `prefix + j` | 聚焦下方窗格 |
| `prefix + k` | 聚焦上方窗格 |
| `prefix + l` | 聚焦右側窗格 |
| `prefix + [` | 進入複製模式 |

### 標籤頁

| 捷徑 | 動作 |
|--------|------|
| `prefix + c` | 建新標籤頁 |
| `prefix + n` | 下一個標籤頁 |
| `prefix + p` | 上一個標籤頁 |
| `prefix + ,` | 重新命名目前標籤頁 |

### 工作區與會話

| 捷徑 | 動作 |
|--------|------|
| `prefix + w` | 開工作區選取器/導航器 |
| `prefix + shift + n` | 建新工作區 |
| `prefix + shift + w` | 重新命名選取的工作區 |
| `prefix + shift + d` | 關閉選取的工作區 |
| `prefix + g` | 開會話導航器（goto） |
| `prefix + q` | 斷用戶端（背景會照跑） |

### 常見操作

| 捷徑 | 動作 |
|--------|------|
| `prefix + +` | 建新代理 |
| `prefix + /` | 搜尋代理 |
| `prefix + .` | 斷目前代理 |

---

## 測試範例

### 基本流程測試

#### 測試 1：啟動並建窗格

```bash
# 步驟 1：啟動 Herdr
herdr

# 步驟 2：建新 shell 窗格（右鍵選單或 prefix+v）
# 步驟 3：在窗格中執行指令
```

**預期結果：**
- Herdr 視窗打開，顯示預設 shell
- 右鍵選單可用
- 能跑任何 shell 指令

#### 測試 2：啟動 AI 代理

```bash
# 在 Herdr 窗格中執行：
claude

# 或在側邊欄點 AI 代理圖示
```

**預期結果：**
- 代理在窗格中啟動
- 側邊欄顯示代理狀態為 `working`
- 代理開始跑預設任務

#### 測試 3：代理狀態偵測

```bash
# 啟動多個代理在不同窗格：
claude        # 跑任務 A
codex         # 跑任務 B
pi            # 跑任務 C

# 看側邊欄狀態
```

**預期結果：**
- 每個代理顯示正確狀態：
  - `working`：正在跑
  - `blocked`：等輸入/批准
  - `idle`：任務完成
- 狀態會隨代理行為即時更新

### 斷線測試

#### 測試 4：斷線並重連

```bash
# 步驟 1：啟動 Herdr 並啟動代理
herdr
claude  # 跑長時間任務

# 步驟 2：斷線（ctrl+b q 或關視窗）
# 步驟 3：等幾分鐘
# 步驟 4：重連
herdr
```

**預期結果：**
- 代理還在跑，不會停
- 視窗佈局恢復
- 代理從中斷處繼續

#### 測試 5：結束會話

```bash
# 步驟 1：確認代理完成或可斷
herdr

# 步驟 2：斷所有代理
herdr pane input --all --ctrl+d

# 步驟 3：結束會話
herdr server stop
```

**預期結果：**
- 所有窗格中的程式停
- 伺服器不再跑

### 遠端測試

#### 測試 6：SSH 遠端工作

```bash
# 步驟 1：SSH 到遠端伺服器
ssh you@server

# 步驟 2：在遠端跑 Herdr
herdr

# 步驟 3：啟動代理
claude

# 步驟 4：斷 SSH（ctrl+d）
# 步驟 5：重 SSH
ssh you@server
herdr
```

**預期結果：**
- 代理在遠端持續跑
- 重連後視窗狀態恢復

#### 測試 7：herdr --remote 模式

```bash
# 步驟 1：設定 SSH config
Host workbox
  HostName server.example.com
  User you
  Port 2222

# 步驟 2：用 --remote 模式
herdr --remote workbox

# 步驟 3：啟動代理
claude

# 步驟 4：斷連線
herdr pane input --all --ctrl+d
# 或直接關視窗
```

**預期結果：**
- 本機 Herdr 客戶端顯示遠端會話
- 遠端代理持續跑
- 剪貼簿功能可用（圖片貼上等）

### 配置測試

#### 測試 8：主題切換

```bash
# 步驟 1：看目前主題
herdr config show theme

# 步驟 2：改 ~/.config/herdr/config.toml
[theme]
name = "dracula"

# 步驟 3：重新載入配置
herdr server reload-config
# 或在 Herdr 內按 prefix+shift+r
```

**預期結果：**
- 介面主題立即變 dracula
- 顏色方案正確應用

#### 測試 9：前綴鍵自訂

```bash
# 步驟 1：改 config.toml
[keys]
prefix = "ctrl+a"

# 步驟 2：重新載入
herdr server reload-config
```

**預期結果：**
- 所有捷鍵現在用 `ctrl+a` 當前綴
- 原有 `ctrl+b` 捷鍵不再有效

### 多台機器測試

#### 測試 10：添加多台機器

```bash
# 步驟 1：添本機機器
herdr machine add local

# 步驟 2：添遠端機器
herdr machine add workbox --label "Workbox"
herdr machine add server1 --label "Server 1"
herdr machine add server2 --label "Server 2"

# 步驟 3：啟動 Herdr
herdr

# 步驟 4：看側邊欄
# 應該顯示所有連通的機器
```

**預期結果：**
- 側邊欄顯示所有機器狀態
- 可切換到不同機器
- 每台機器的代理獨立跑

---

## 故障排除

### 常見問題

#### 問題 1：Herdr 啟動不了

```bash
# 檢查 Herdr 是否在 PATH
which herdr

# 檢查版本
herdr --version

# 看日誌
herdr --verbose
```

#### 問題 2：代理狀態顯示不對

```bash
# 重新載入配置
herdr server reload-config

# 檢查代理整合
herdr integration list

# 重裝代理
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

#### 問題 4：剪貼簿不工作

```bash
# 檢查 mouse_capture 設定
herdr config show ui.mouse_capture

# 應該是 true
```

### 重置設定

```bash
# 重置按鍵綁定到預設
herdr config reset-keys

# 重置所有設定到預設
herdr config reset
```

---

## 參考資源

### 官方文件
- [Herdr 主頁](https://herdr.dev/)
- [快速開始](https://herdr.dev/docs/quick-start/)
- [安裝指南](https://herdr.dev/docs/install/)
- [使用方式](https://herdr.dev/docs/how-to-work/)
- [配置參考](https://herdr.dev/docs/config-reference/)
- [按鍵捷徑](https://herdr.dev/docs/keyboard/)
- [代理支援](https://herdr.dev/docs/agents/)
- [整合](https://herdr.dev/docs/integrations/)
- [多台機器](https://herdr.dev/docs/connecting-machines/)
- [會話狀態](https://herdr.dev/docs/session-state/)

### GitHub
- [herdrdev/herdr 官方儲存庫](https://github.com/herdrdev/herdr)
- [Releases](https://github.com/herdrdev/herdr/releases)

### 中文資源
- [最懂 AI 的 Herdr 使用教學](https://most.tw/posts/ainews/herdr-agent-multiplexer/)
- [Herdr 完整設定與使用教程](https://github.com/joeseesun/herdr-guide/blob/main/Herdr_%E8%BD%AF%E4%BB%B6%E5%85%A8%E9%9D%A2%E8%B0%83%E7%A0%94%E4%B8%8E%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B.md)
- [Herdr 捷徑 Cheat Sheet](https://getmoshi.app/articles/herdr-cheatsheet)
- [ithome Herdr 介紹](https://ithelp.ithome.com.tw/articles/10407114)

---

## 總結

Herdr 是為 AI 程式碼代理量身打造的終端機多工器，優勢在於：

1. **不用中斷就能離線**：關掉終端機或斷線，代理照跑
2. **代理狀態感知**：自動偵測並顯示每個代理狀態
3. **跨機器協作**：同一視窗管理多台機器的代理
4. **AI 原生設計**：支援超過 20 個主流 AI 代理
5. **滑鼠優先操作**：降低學習曲線，提高效率
6. **高度可配置**：自訂主題、捷鍵和行為

不管是在本機開發、遠端伺服器工作，還是用手機 SSH 連線，Herdr 都能提供一致的使用體驗。

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

*報告撰寫日期：2026-10-23*
*Herdr 版本：0.9.5 (stable)*