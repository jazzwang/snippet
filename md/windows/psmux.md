# psmux：Windows 原生的 tmux 技術摘要

- Git Repo
  - https://github.com/psmux/psmux
- Website
  - https://psmux.pages.dev

## 2026-09-04

- 緣起：
  - 持續思考怎麼建立日常工作流中
  - 在評估能否把開啟 vs code 編輯器改成 neovim 
    - 目前想到可能的障礙反而是 Markdown Preview Enhanced 的一些整合功能，像是 mermaid.js 的 render 結果
    - 另一個就是把工作流改成在 VS Code + Terminal 一起用
  - 在 Pi Coding Agent 作者的文章中，提到開多個 tmux 視窗，所以想測看看能否在 Windows 平台上跑 tmux。
  - 其次是遠端登入 `code tunnel` 的 Windows 機器時，也想要有 `screen` 指令可以單一 Terminal 也可以有多個視窗。
  - 再來就是斷線後仍能接回原本正在跑的 Shell Script 等
    - 在高鐵開發上特別感覺困擾，以前是靠 `mosh` 接回 SSH session ... 但現在多數 Cloud IDE 環境都是跑在 k8s 的容器中，不確定 mosh client 能怎麼接進去容器的 mosh server。

- 解法：
  - Scoop 搜尋結果是 psmux
```
~$ scoop info psmux

Name        : psmux
Description : Terminal multiplexer for Windows - tmux alternative for PowerShell and Windows Terminal
Version     : 3.3.8
Source      : main
Website     : https://psmux.pages.dev
License     : MIT
Updated at  : 2026-08-19 9:56:01 AM
Updated by  : github-actions[bot]
Binaries    : psmux.exe | pmux.exe | tmux.exe
```
- 以下是 GPT 5.6 Luna 寫的技術摘要，經 speak-human-tw skill 修改：

> [!QUESTION]
> 參考 https://github.com/psmux/psmux 與 https://psmux.pages.dev/ 撰寫一則技術摘要並更新於 psmux.md

-----

> psmux 是用 Rust 撰寫的 Windows 終端機多工器，直接使用 ConPTY 與 Win32 API。它沿用 tmux 的命令和設定格式，讓 PowerShell、cmd、Git Bash、WSL 與 nushell 都能使用 session、window、pane，以及 detach／reattach。
>
> 參考：[`psmux/psmux`](https://github.com/psmux/psmux) · [官方網站](https://psmux.pages.dev/)

## 核心定位

psmux 直接在 Windows 上實作 tmux 的多工功能，不需要透過 WSL、Cygwin 或 MSYS2。

- 不需要 WSL、Cygwin 或 MSYS2；每個 pane 都是 Windows 原生 ConPTY。
- 直接啟動 `pwsh.exe`、`cmd.exe` 或其他 Windows 程式，因此可保留 Windows 路徑、剪貼簿與 Windows 工具的行為。
- 安裝後會提供 `psmux.exe`、`pmux.exe` 與 `tmux.exe` 三個入口，既有 tmux 腳本通常只需要調整 Windows 路徑和 shell 引號。
- 可以直接讀取既有的 `~/.tmux.conf`，並支援 90 多個 tmux 相容命令、140 多個格式變數、hooks、control mode，以及外掛和主題。

## 架構與資料流

```text
Windows Terminal
      │  client：輸入、渲染、滑鼠事件
      ▼
psmux client ── loopback TCP ──► psmux detached server
                                      │
                       ┌──────────────┼──────────────┐
                       ▼              ▼              ▼
                    ConPTY          ConPTY          ConPTY
                    pwsh.exe        cmd.exe          wsl.exe
```

1. `new-session` 會啟動一個與終端機視窗脫離的 server。關閉 Windows Terminal 只會關閉 client，session 與其中的 shell 仍可存活。
2. server 在 `127.0.0.1` 的動態 TCP port 監聽，並在預設的 `%USERPROFILE%\.psmux\` 寫入 `.key`、`.sid`、`.pid`、`.port` 等 registry 檔案。client 先以 key 驗證，再透過 TCP 傳送命令與畫面資料。

每個 pane 都有自己的 ConPTY。ConPTY 輸出的 VT bytes 由 reader thread 讀取，再交給 VT parser 維護畫面格、scrollback、色彩、OSC 7 工作目錄與 OSC 8 hyperlink。client 以 ratatui／crossterm 渲染畫面，將鍵盤與滑鼠事件回送 server，server 再寫入對應 pane 的 ConPTY。輸出採 event-driven frame push，而非固定週期重新繪製。

Windows 11 22H2（build 22621）以上可使用 ConPTY passthrough mode；若系統不支援，psmux 會回退至一般模式，也可用 `PSMUX_NO_PASSTHROUGH=1` 停用。

因此，psmux 不需要 POSIX 的 `fork()`、Unix socket 或 pty device，仍能使用 Windows 的 process tree、剪貼簿、IME 與 console 行為。psmux server 是以目前使用者身分執行的背景程序，不是 Windows Service。

## 主要能力

- **多工與持久化**：支援 session、window、水平／垂直切 pane、5 種 layout，以及 detach／reattach。也能建立 floating pane，或用 `join-pane`／`move-pane` 在 session 間移動 pane。
- **互動操作**：支援滑鼠點選 pane、拖曳調整大小、用狀態列切換 window、捲動輸出，以及拖曳選取文字並使用 Windows clipboard。
- **tmux 相容性**：支援 `bind-key`、`set-option`、`if-shell`、`run-shell`、`display-popup`、`display-menu`、`choose-tree`、`send-keys`、`capture-pane`、`pipe-pane`、`wait-for` 等命令，也支援 vi copy mode、命名 buffer、hooks 與 command chaining。
- **設定與主題**：可使用 `.tmux.conf`，支援 16 色、256 色、24-bit true color、狀態列、pane border，以及 Catppuccin／Dracula／Nord 等主題和外掛。
- **多 shell 與輸入法**：預設使用 PowerShell 7（`pwsh`），也可指定 PowerShell 5、cmd、Git Bash、WSL、nushell 或任意 Windows executable；支援中／日／韓 CJK 與 IME 輸入。
- **自動化與整合**：提供 tmux control mode（`-C`／`-CC`）、穩定的 session／window／pane ID、format engine，以及 Python、Node.js、Go、Rust 與 libtmux 整合方式。
- **終端機 AI 工具**：在 psmux session 中執行 Claude Code 時，agent team 的 teammate 可自動分配到獨立 pane，適合並行執行 agent、編譯器、log tail 與 TUI 工具。

## 安裝與快速使用

psmux 支援 Windows 10 和 Windows 11，建議搭配 PowerShell 7 使用。

```powershell
# 以 WinGet 安裝
winget install psmux

# 或使用 Cargo
cargo install psmux

# 建立、列出、連回 session
psmux new-session -s work
psmux ls
psmux attach -t work
```

常用快捷鍵沿用 tmux 預設設定：`Ctrl-b %` 水平切 pane、`Ctrl-b "` 垂直切 pane、`Ctrl-b d` detach、`Ctrl-b [` 進入 copy mode。非互動腳本則可使用：

```powershell
psmux new-session -d -s dev
psmux split-window -h -t dev
psmux send-keys -t dev:0.0 'git status' Enter
psmux capture-pane -p -t dev:0.0
psmux attach -t dev
```

## 設定範例

psmux 依序尋找第一個存在的設定檔：`~/.psmux.conf`、`~/.psmuxrc`、`~/.tmux.conf`、`~/.config/psmux/psmux.conf`。例如：

```tmux
set -g prefix C-a
set -g mouse on
set -g default-shell pwsh
set -g history-limit 5000
set -g status-right "%H:%M  #{pane_title}"
set -g mode-keys vi
```

若要指定不同設定檔，可使用 `psmux -f <path>`；`psmux -f NUL` 可啟動不載入設定的環境。Windows 特有的狀態與診斷資料可透過 `PSMUX_DATA_DIR` 移動，並可用 `PSMUX_NO_WARM=1` 關閉 warm pool。

## 效能設計與取捨

psmux 使用 Rust 的 release build，降低互動延遲主要靠以下幾項設計：

- **warm server／warm pane**：預先啟動待命 server 與 shell，降低第一次建立 session、window 或 pane 的成本。
- **reader／parser／write queue 分離**：輸出讀取、VT 解析與輸入寫入不互相阻塞；每個 pane 具備獨立的工作執行緒。
- **frame push 與 lazy resize**：只有狀態變更時才推送畫面，背景 window 延後到切換時才 resize。
- **程序優先權**：psmux 自身預設使用 `above-normal`，pane 裡的 shell 仍維持 normal，避免把使用者正在執行的工作一併提升。

專案在參考機器上的測試結果是：CLI round trip 約 15–25 ms；啟用 warm pool 時，`new-session -d` 約 50 ms，冷啟動約 215 ms。實際看到 PowerShell prompt 的時間，主要受 PowerShell profile 和 shell 啟動速度影響。這些數字是專案文件中的基準，不應視為所有 Windows 主機的保證值。

## 適用情境與限制

**適合：** 需要在 Windows 上長時間保留建置或測試程序、透過 SSH／RDP 重新連回工作環境、用腳本建立固定 pane 佈局，或同時觀察多個 terminal agent 與 TUI 的情境。

**需要留意：**

- tmux 依賴 Unix signal、daemon 或 POSIX process semantics 的部分無法一比一移植；應查閱專案的 compatibility matrix。
- 每個 pane 都會啟動一個實際 shell，記憶體主要消耗在 `pwsh` 等子程序，而非 psmux server；大量 pane 應控制 shell profile 與 `history-limit`。
- loopback TCP 連線依賴每個 session 的 key 檔案保護。若變更 `PSMUX_DATA_DIR`，應確保資料夾 ACL 不會讓其他使用者讀取 `.key`。
- 跨 Windows 版本的滑鼠與 ConPTY 行為可能不同；尤其是 SSH 遠端滑鼠支援需符合專案文件列出的 Windows build 要求。

對以 PowerShell 和 Windows 工具為主、又需要 tmux 式持久化與多工的使用者，psmux 比在 WSL 裡再跑一層 tmux 更直接。若工作流主要使用純 Linux shell，或依賴 Unix signal 等 POSIX 行為，則應先查閱相容性文件。
