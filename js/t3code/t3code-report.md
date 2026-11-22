# T3 Code 技術報告

## 1. 產品概述

T3 Code 是一個開源的程式碼 Agent 控制平面（Control Plane），為 50 萬+ 開發者所採用。它讓使用者能夠在單一介面中管理多個 AI 開發 Agent，並提供跨平台的使用體驗。

### 核心價值主張

- **自帶訂閱（Bring Your Own Sub）**：不重新銷售 Token，直接使用用戶已有的 Agent 帳戶（Claude Code、Codex、Cursor、Antigravity 等）
- **跨平台統一介面**：桌面端、Web、iOS、Android 共用同一個伺服器，所有客戶端顯示相同對話串
- **遠端就緒（Remote Ready）**：支援透過本機網路、Tailscale 或 T3 Connect 連接遠端機器
- **內建 Git 整合**：每個對話串獨立工作樹，一鍵完成 Commit、Push 和建立 Pull Request
- **效能優先**：將幀率掉落視為 Bug，追求極致流暢體驗
- **完全開源（MIT）**：可自由 Fork、修改和重新分發

### 相容的 Agent

- Claude Code
- Codex CLI
- Cursor
- OpenCode
- Grok Build
- Antigravity
- Kiro
- Pi
- Muse Code
- fx
- 任何符合 ACP 規範的 Agent

## 2. 安裝步驟

### 2.1 系統要求

- macOS、Windows 或 Linux
- 至少一個 AI Agent CLI 工具已安裝並登入

### 2.2 桌面應用安裝

#### 方法一：官方安裝器

1. 訪問 [https://t3.codes/download](https://t3.codes/download) 下載對應平台的安裝程式
2. 執行安裝程式，依指示完成安裝

#### 方法二：套件管理器

| 平台 | 指令 |
|------|------|
| macOS | `brew install --cask t3-code` |
| Windows | `winget install T3Tools.T3Code` 或 `scoop install extras/t3code` |
| Arch Linux | `yay -S t3code-bin` |
| Nix | `nix profile add github:NixOS/nixpkgs/nixos-unstable#t3code` |
| Debian/Ubuntu | 從 [Releases](https://github.com/pingdotgg/t3code/releases) 下載 `.deb` 檔案 |

#### 方法三：命令列安裝

```bash
# Linux/Mac
curl -fsSL https://t3.codes/install.sh | sh

# Windows PowerShell
irm https://t3.codes/install.ps1 | iex
```

#### 方法四：一鍵試用

```bash
npx t3@latest
```

此方法無需安裝，適合快速測試。

### 2.3 手機 App 安裝

1. **iOS**：[App Store](https://apps.apple.com/us/app/t3-code-remote-claude-more/id6787819824)
2. **Android**：[Google Play](https://play.google.com/store/apps/details?id=com.t3tools.t3code)

安裝後，參照 [遠端存取](#3-驗證步驟) 章節設定連線。

## 3. 初始設定

### 3.1 登入 AI Agent

T3 Code 需要至少一個已安裝並登入的 AI Agent CLI 工具。

#### 範例一：Claude Code

```bash
# 安裝 Claude Code（如尚未安裝）
# 依官方文件安裝

# 登入
claude auth login
```

#### 範例二：Codex CLI

```bash
# 安裝 Codex CLI
# 依官方文件安裝

# 登入
codex login
```

#### 其他 Agent 登入方式

- **Cursor**: `cursor login`
- **OpenCode**: `opencode auth`
- **Antigravity**: Google 登入

詳細設定請參照 [Provider 設定文件](https://t3.codes/docs/user/install.md#providers)。

### 3.2 啟動伺服器

```bash
# 使用命令行啟動
t3

# 或使用 npx（無需安裝）
npx t3@latest
```

啟動後會顯示服務地址，例如：
```
▲ T3 Code dev server → http://localhost:4001
```

### 3.3 開啟 Web 介面

1. 複製啟動訊息顯示的網址
2. 在瀏覽器中開啟
3. 首次使用會引導您完成初始設定

## 4. 測試步驟

### 4.1 基本功能測試

#### 測試項目一：對話串啟動

1. 開啟 Web 介面
2. 點擊「New Thread」或「+」按鈕
3. 輸入測試提示詞，例如：
   ```
   請幫我檢查這個檔案的程式碼品質
   ```
4. 觀察 Agent 是否能正常回應

**預期結果**：Agent 回應時間合理，回應內容符合預期

#### 測試項目二：模型切換

1. 在對話串中開啟模型設定
2. 切換至不同模型（如從 Claude 切換至 Codex）
3. 繼續對話

**預期結果**：模型切換成功，新模型正確回應

#### 測試項目三：Git 整合測試

1. 開啟一個對話串
2. 讓 Agent 進行檔案修改
3. 查看底部 Git 面板
4. 點擊「Commit & push」按鈕

**預期結果**：
- 自動生成 Commit Message
- 自動建立新 Branch（如 `thread-{timestamp}`）
- 成功 Push 至遠端仓库
- 自動開啟 Pull Request

#### 測試項目四：遠端存取測試（如適用）

1. 在桌面 App 啟動 T3 Code
2. 在手機 App 中開啟「Remote Access」
3. 選擇您的電腦作為目標
4. 輸入電腦 IP 或掃描 QR Code
5. 批准連線請求

**預期結果**：手機 App 成功連接到電腦上的 T3 Code 伺服器

### 4.2 效能測試

#### 測試項目一：幀率監控

1. 開啟對話串
2. 觀察 Agent 執行過程中的幀率
3. 記錄幀率是否穩定在 60 FPS

**預期結果**：幀率維持在 60 FPS，無明顯卡頓

#### 測試項目二：回應速度測試

1. 開啟多個對話串
2. 同時發送多個請求
3. 記錄各請求的回應時間

**預期結果**：回應時間在合理範圍內，無明顯延遲

## 5. 驗證步驟

### 5.1 系統配置驗證

#### 檢查清單

- [ ] T3 Code 服務正在運行（檢查端口 4001 是否監聽）
- [ ] 至少一個 AI Agent 已登入並可用
- [ ] 瀏覽器可正常存取 Web 介面
- [ ] 桌面 App、Web、手機 App 可互相看到相同對話串

#### 驗證命令

```bash
# 檢查 T3 Code 是否運行
ps aux | grep t3

# 檢查端口監聽
lsof -i :4001
# 或
netstat -an | grep 4001

# 檢查程式碼是否運行
curl http://localhost:4001
```

### 5.2 Agent 整合驗證

#### 驗證項目一：Token 管理

- [ ] 確認 T3 Code 未重新銷售 Token
- [ ] 確認 Token 僅用於當前登入的 Agent
- [ ] 檢查設定檔中 Token 隔離情況

#### 驗證項目二：多 Agent 協作

1. 建立對話串，使用 Agent A
2. 在對話串中要求轉交任務給 Agent B
3. 觀察任務是否成功轉移

**預期結果**：任務成功轉移，Agent B 執行任務

### 5.3 遠端連線驗證

#### 驗證項目一：本機網路連線

1. 確保電腦與手機在同一 Wi-Fi 網路
2. 在手機瀏覽器輸入電腦 IP + 端口
3. 批准連線請求

**預期結果**：成功連線並看到對話串

#### 驗證項目二：Tailscale 連線

1. 在電腦和手機都安裝 Tailscale
2. 建立 Tailscale 連線
3. 使用 Tailscale IP 進行連線

**預期結果**：即使不在同一網路也能成功連線

#### 驗證項目三：T3 Connect

1. 在手機 App 中使用 T3 Connect 功能
2. 掃描電腦上的 QR Code
3. 建立連線

**預期結果**：無需設定 IP，透過 QR Code 快速連線

### 5.4 Git 功能驗證

#### 驗證項目一：工作樹隔離

1. 開啟對話串
2. 讓 Agent 進行程式碼修改
3. 檢查修改是否在工作樹中

**預期結果**：修改在工作樹中，不影響主分支

#### 驗證項目二：一鍵 Commit/PR

1. 完成程式碼修改
2. 點擊「Commit & push」按鈕
3. 檢查 GitHub

**預期結果**：
- 自動建立 Commit
- 自動建立 Branch
- 自動 Push 至遠端
- 自動建立 Pull Request
- Commit Message 和 PR Description 自動生成

### 5.5 安全性驗證

#### 檢查項目

- [ ] 確認所有通訊使用 HTTPS/TLS 加密
- [ ] 檢查 Token 不暴露在網路流量中
- [ ] 確認遠端連線需要批准機制
- [ ] 檢查敏感資料（如 Token）的保護機制

#### 命令列檢查

```bash
# 檢查 T3 Code 版本
t3 --version

# 檢查已登入的 Agent
# 依各 Agent 指令檢查登入狀態
claude auth status
codex status
```

## 6. 故障排除

### 6.1 常見問題

#### 問題一：無法啟動伺服器

**症狀**：執行 `t3` 後無反應或報錯

**解決方案**：
```bash
# 檢查 Node.js 版本
node --version

# 檢查 port 4001 是否被佔用
lsof -i :4001

# 如需釋放端口
kill -9 <PID>

# 重新啟動
t3
```

#### 問題二：Agent 無法回應

**症狀**：發送訊息後 Agent 不回應

**解決方案**：
```bash
# 檢查 Agent CLI 是否登入
claude auth login
# 或
codex login

# 檢查 Agent 是否運行
claude --version
# 或
codex --version
```

#### 問題三：遠端連線失敗

**症狀**：手機 App 無法連接到電腦

**解決方案**：
1. 確認電腦和手機在同一網路
2. 確認電腦防火墙允許 4001 端口
3. 嘗試使用 Tailscale 或 T3 Connect
4. 檢查連線請求是否被批准

### 6.2 日誌查看

```bash
# 查看日誌
t3 logs

# 查看特定 Agent 的日誌
# 依各 Agent 指令查看
```

## 7. 最佳實踐

### 7.1 系統配置

- 使用獨立的 CPU 核心運行 T3 Code
- 確保足夠的記憶體（建議 8GB+）
- 使用 SSD 以減少 I/O 延遲

### 7.2 效能優化

- 限制同時運行的對話串數量
- 為重要任務分配更多資源
- 定期清理過時的 Branch 和對話串

### 7.3 安全性建議

- 定期更新 T3 Code 至最新版本
- 使用強密碼保護遠端連線
- 定期審視登入的 Agent 和 Token
- 在生產環境使用 HTTPS

## 8. 參考資源

- [官方文件](https://t3.codes/docs)
- [GitHub Repository](https://github.com/pingdotgg/t3code)
- [Discord 社群](https://discord.gg/jn4EGJjrvv)
- [Releases](https://github.com/pingdotgg/t3code/releases)
- [Contributing Guide](https://github.com/pingdotgg/t3code/blob/main/CONTRIBUTING.md)

## 9. 版本資訊

- **報告日期**：2026 年 11 月
- **T3 Code 版本**：依安裝時顯示
- **相容 Agent**：Claude Code, Codex, Cursor, OpenCode, Grok Build, Antigravity, Kiro, Pi, Muse Code, fx

*本報告基於 [https://github.com/pingdotgg/t3code](https://github.com/pingdotgg/t3code) 和 [https://t3.codes/](https://t3.codes/) 的官方文件編寫。*
