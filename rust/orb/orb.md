# Orb 技術報告

**作者**: Thomas Marchand (Th0rgal)  
**專案**: https://github.com/Th0rgal/orb  
**官方網站**: https://orb.thomas.md/  
**版本**: 最新版 (2025 年 12 月)

---

## 一、專案概述

Orb 是一個整合式 AI Agent 管理平台，用於集中管理所有 AI 提供者、執行機器和 Agent 工具集。它讓使用者可以將訂閱帳號、API 金鑰和本地硬體连接到執行環境，並從 macOS 和 iOS 設備上統一切換和管理所有 Agent。

### 核心概念

Orb 採用「前端 - 後端」分離架構：
- **Orb (客戶端)**: Tauri (macOS) 和 SwiftUI (iOS) 建構的桌面與行動端應用程式
- **Core (後端)**: 前身為 sandboxed.sh，是 Rust 後端服務，負責專案管理、任務歷史和遠端執行服務

---

## 二、系統架構

### 2.1 執行模式

Orb 提供三種執行模式，使用者可以選擇 Agent 在哪裡執行：

| 模式 | 執行位置 | 使用方式 |
|------|----------|----------|
| **您的電腦 (Your Computer)** | 本地桌面環境 | 選擇「新 Agent → 本機電腦」，然後選擇工具集和模型。使用您的本機檔案和工具 |
| **您的私有雲 (Your Private Cloud)** | 自有伺服器和遠端機器 | 將機器添加到 Core，然後在 Orb 中選擇。在配置的宿主或隔離容器工作空間中執行 Agent |
| **雲端 Agent (Cloud Agents)** | 協調器或提供者管理的服務 | 選擇「雲端 Agent」，然後選擇 Hermes、Grok Bot 或 Cursor Cloud |

### 2.2 技術棧

- **客戶端**: 
  - macOS: Tauri + SolidJS
  - iOS: SwiftUI
  - Web 管理控制台: Next.js
- **後端**: 
  - Rust (sandboxed-sh)
  - Lean 4 決策核心 (用於編排、代理和任務生命週期)
  - MCP 夥伴 (sandboxed-mcp, workspace-mcp, desktop-mcp)
- **資料庫**: SQLite (missions.db, projects.db, ask.db)

---

## 三、安裝與設定

### 3.1 Docker 安裝 (推薦)

Docker 是安裝 Orb 最快的方式，可在 Linux、macOS 或 Windows 上運行。

#### 步驟 1: 克隆專案

```bash
git clone https://github.com/Th0rgal/orb.git
cd orb
```

#### 步驟 2: 設定環境變數

```bash
cp .env.example .env
```

編輯 `.env` 檔案，設定以下必要變數：

```bash
# 必須設定
DASHBOARD_PASSWORD=您的密碼
JWT_SECRET=長隨機秘密字串

# 可選
DEV_MODE=false  # 生產環境設為 false 以強制密碼/JWT 驗證
LIBRARY_REMOTE=您的 Git 儲存庫 URL
MAX_PARALLEL_MISSIONS=10  # 最大並行任務數
```

#### 步驟 3: 啟動服務

```bash
docker compose up -d
```

啟動後，服務會運行在：
- **Web 控制台 & API**: `http://localhost:3000`
- **Orb 桌面/iOS**: 連接到 `http://localhost:3000` 並使用 `DASHBOARD_PASSWORD` 登入

### 3.2 原生 Linux 安裝 (生產環境)

#### 步驟 1: 安裝系統依賴

```bash
apt update && apt install -y \
  ca-certificates curl git jq unzip tar python3 python3-yaml \
  build-essential pkg-config libssl-dev \
  systemd-container debootstrap
```

#### 步驟 2: 安裝 Bun 和 Node.js

```bash
curl -fsSL https://bun.sh/install | bash
install -m 0755 /root/.bun/bin/bun /usr/local/bin/bun

curl -fsSL https://sh.rustup.rs | sh -s -- -y
source /root/.cargo/env
```

#### 步驟 3: 安裝 Agent 工具集

```bash
# Claude Code
npm install -g @anthropic-ai/claude-code

# Codex
npm install -g @openai/codex

# Antigravity
# 從 https://antigravity.google/docs/cli/install/ 安裝

# OpenCode
curl -fsSL https://opencode.ai/install | bash -s -- --no-modify-path && \
install -m 0755 /root/.opencode/bin/opencode /usr/local/bin/opencode

# Grok
# 安裝 Grok CLI 並執行 "grok login --device-auth"
```

#### 步驟 4: 編譯後端

```bash
mkdir -p /opt/sandboxed_sh
cd /opt/sandboxed_sh
git clone https://github.com/Th0rgal/orb.git repo
cd repo

# 使用 debug 模式編譯 (不適合 --release，因為是 I/O 密集型控制平面)
cargo build --bin sandboxed-sh --bin sandboxed-mcp --bin sandboxed-node --bin palomactl

# 安裝執行檔
install -m 0755 target/debug/sandboxed-sh /usr/local/bin/sandboxed-sh
install -m 0755 target/debug/sandboxed-mcp /usr/local/bin/sandboxed-mcp
install -m 0755 target/debug/sandboxed-node /usr/local/bin/sandboxed-node
install -m 0755 target/debug/palomactl /usr/local/bin/palomactl
```

#### 步驟 5: 設定環境

```bash
mkdir -p /etc/sandboxed-sh
cat > /etc/sandboxed-sh/sandboxed-sh.env << 'EOF'
HOST=127.0.0.1
PORT=3000
WORKING_DIR=/root
DEV_MODE=false
DASHBOARD_PASSWORD=change-me-to-something-strong
JWT_SECRET=change-me-to-a-long-random-string
SANDBOXED_OAUTH_OWNER=cli-proxy
EOF
chmod 0600 /etc/sandboxed-sh/sandboxed-sh.env
```

#### 步驟 6: 建立 systemd 服務

```bash
cat > /etc/systemd/system/sandboxed-sh.service << 'EOF'
[Unit]
Description=sandboxed.sh (Orb) Control Plane
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
EnvironmentFile=/etc/sandboxed-sh/sandboxed-sh.env
ExecStart=/usr/local/bin/sandboxed-sh
WorkingDirectory=/root
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable --now sandboxed-sh.service
```

#### 步驟 7: 設定反向代理

使用 Nginx 或 Caddy 在 `127.0.0.1:3000` 前加上 TLS 配置，例如：
- `https://orb.thomas.md`
- `https://agent-backend.example.com`

### 3.3 連接客戶端

| 客戶端 | 連接方式 |
|--------|----------|
| **Orb 桌面 (macOS)** | 在 `orb/` 目錄中執行 `pnpm install && pnpm tauri dev`，然後在「設定 → 客戶端 → 後端」輸入伺服器 URL |
| **Orb iOS** | 透過 XcodeGen 編譯 `ios_dashboard/` (使用 `SandboxedDashboard` 範例，產品名稱 `Orb`)，並連接到您的伺服器 URL |
| **Web 管理控制台** | 部署 `dashboard/` 到 Vercel (設定 `NEXT_PUBLIC_API_URL`) 或執行 `bun dev` |
| **Hermes 協調器** | 將 Hermes 的 MCP 伺服器配置指向 `/usr/local/bin/sandboxed-mcp` |

---

## 四、核心功能

### 4.1 專案與任務管理

Orb 使用專案來組織任務、任務歷史、技能和本地同步的 **Context** 資料夾 (`@context`)。

#### 專案特性

- 每個專案有獨特顏色標識
- 可配置技能 (`skills/<name>/SKILL.md`)
- 支援本地 Context 資料夾雙向同步
- 任務歷史完整記錄

### 4.2 任務執行與跟隨

在對話過程中：

1. **即時跟隨與導向**:
   - 可收合的 `Worked — ...` 工具/思考摺疊
   - 巢狀子代理
   - `/plan` 模式：原生問題和核准卡片
   - `/goal` 模式：自主多輪執行
   - 持久化的跟隨佇列，在回合完成時自動發送

2. **側邊助理 (`/btw`)**:
   - 按下 `⌘⇧J` 開啟懸掛的側邊助理面板
   - 使用共享工作空間上下文和 `@conversation` 快照詢問問題
   - 不中斷主要 Agent 回合

3. **保持長任務進行**:
   - 排程持久任務喚醒 (`schedule_wakeup`)
   - 自動恢復中斷的執行
   - **跨機器轉移工作空間** (`Change machine…`)，保留符號連結並跳過編譯副產品

4. **豐富輸出**:
   - Markdown、程式碼、表格、LaTeX、互動式問卷
   - 內嵌圖片和可點擊工作空間檔案連結 (`⌘J` / `⌘P`)

### 4.3 管理訂閱帳號

Orb 支援直接從「提供者」頁面登入訂閱帳號（macOS、web 和 iOS），或透過 **CLIProxyAPI Plus** 連接：

```bash
SANDBOXED_OAUTH_OWNER=cli-proxy
```

#### 支援的提供者

- Anthropic (Claude)
- OpenAI
- xAI (Grok)
- Kimi
- Google (Antigravity)

#### CLIProxyAPI 功能

- OAuth 驗證
- 更新 token
- 啟用/停用個別帳號
- 檢查即時方案/配額狀態
- 處理路由和輪轉

---

## 五、工作空間隔離

### 5.1 容器工作空間 (systemd-nspawn)

預設情況下，Docker 中的工作空間在容器內以宿主/回退模式執行。要啟用完整的每工作空間 `systemd-nspawn` 容器隔離，需要修改 `docker-compose.yml`：

```yaml
services:
  sandboxed-sh:
    privileged: true
    cgroup: host
```

然後重新啟動：

```bash
docker compose down && docker compose up -d
```

### 5.2 持久化資料

| 資料卷 | 路徑 | 內容 |
|--------|------|------|
| `sandboxed-data` | `/root/.sandboxed-sh` | SQLite 資料庫、Library 借閱、同步 `@context` 檔案、容器 rootfs 樹 |
| `claude-auth` | `/root/.claude` | 傳統 Claude 憑證（不使用 CLIProxyAPI 時） |
| `~/.ssh` | `/root/.ssh:ro` | 宿主 SSH 金鑰的只讀掛載（在啟動時複製到可寫鍵目錄用於私有 Git 儲存庫） |

---

## 六、API 與 MCP 整合

### 6.1 認證

所有 HTTP 端點需要 `Authorization: Bearer ` 授權標頭。透過 `POST /api/auth/login` 獲取 JWT：

```bash
curl -X POST "https://orb.thomas.md/api/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"password": "your-password"}'
```

### 6.2 REST API

Orb 提供完整的 REST API，支援：
- 專案管理
- 任務控制
- 機器註冊
- 提供者配置

### 6.3 MCP 伺服器

Orb 提供統一的 `sandboxed-mcp` 伺服器，可供協調器（如 Hermes）使用：

```bash
# 在後端目錄中
/usr/local/bin/sandboxed-mcp
```

---

## 七、測試步驟

### 7.1 Docker 安裝測試

#### 步驟 1: 驗證容器狀態

```bash
docker ps
```

預期輸出應該包含 `sandboxed-sh` 容器。

#### 步驟 2: 檢查服務端口

```bash
curl http://localhost:3000
```

應該返回 API 響應或 HTML 頁面。

#### 步驟 3: 驗證 API 端點

```bash
# 測試登入端點
curl -X POST "http://localhost:3000/api/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"password": "your-password"}'
```

應該返回 JWT token。

### 7.2 原生 Linux 安裝測試

#### 步驟 1: 驗證 systemd 服務

```bash
systemctl status sandboxed-sh.service
```

應該顯示 `active (running)`。

#### 步驟 2: 檢查端口監聽

```bash
ss -tlnp | grep 3000
```

應該顯示 `127.0.0.1:3000` 正在監聽。

#### 步驟 3: 驗證後端回應

```bash
curl http://127.0.0.1:3000
```

#### 步驟 4: 測試任務執行

```bash
# 使用 sandboxed-sh 執行測試任務
sandboxed-sh --help
```

應該顯示可用命令和選項。

### 7.3 客戶端測試

#### macOS 桌面客戶端

```bash
cd orb
pnpm install
pnpm tauri dev
```

在應用程式中：
1. 進入「設定 → 客戶端 → 後端」
2. 輸入 `http://localhost:3000`
3. 輸入 `DASHBOARD_PASSWORD`
4. 點擊登入

#### iOS 客戶端

1. 打開 Xcode
2. 打開 `ios_dashboard/` 目錄
3. 選擇 `SandboxedDashboard` 範例
4. 在模擬器或裝置上運行
5. 輸入伺服器 URL 並登入

### 7.4 工作空間測試

#### 步驟 1: 建立測試專案

在 Orb 中：
1. 點擊「新建專案」
2. 選擇專案名稱
3. 設定執行模式（本機、遠端或雲端）

#### 步驟 2: 執行測試任務

在專案中：
1. 建立新任務
2. 輸入測試指令（例如：「列出當前目錄檔案」）
3. 觀察任務執行過程

#### 步驟 3: 驗證工作空間隔離

如果是使用 `systemd-nspawn` 容器：

```bash
# 檢查容器狀態
systemctl list-units --type=transient | grep sandbox

# 查看容器日誌
journalctl -u sandboxed-sh.service
```

#### 步驟 4: 測試跨機器轉移

如果有多台機器配置：
1. 在任務中選擇「Change machine…」
2. 選擇目標機器
3. 驗證任務狀態和檔案連結

### 7.5 提供者測試

#### 步驟 1: 配置提供者

在 Orb 中：
1. 進入「設定 → 提供者」
2. 新增提供者帳號
3. 選擇提供者類型（Claude、OpenAI、Grok 等）
4. 輸入必要資訊
5. 點擊驗證

#### 步驟 2: 測試模型調用

在任務中：
1. 使用剛配置的提供者
2. 發送測試訊息
3. 驗證回應格式和內容

#### 步驟 3: 檢查配額狀態

在 Orb 中：
1. 進入「設定 → 提供者」
2. 點擊提供者名稱
3. 查看配額使用情況

### 7.6 完整流程測試

#### 測試流程：從專案建立到任務完成

1. **建立專案**
   - 新建專案「測試專案」
   - 選擇執行模式（本機）
   - 選擇工具集（Claude Code）
   - 選擇模型

2. **建立任務**
   - 撰寫任務描述：「建立一個簡單的計算器程式」
   - 設定目標和約束
   - 啟動任務

3. **跟隨任務**
   - 使用 `/btw` 側邊助理詢問問題
   - 查看 `Worked — ...` 摺疊內容
   - 使用 `@conversation` 引用對話內容

4. **中斷與恢復**
   - 故意中斷任務
   - 重新啟動 Orb
   - 驗證任務自動恢復

5. **跨機器轉移**（如配置了多台機器）
   - 選擇「Change machine…」
   - 選擇目標機器
   - 驗證任務狀態和檔案連結

6. **任務完成與成果**
   - 查看最終結果
   - 驗證檔案輸出
   - 測試程式功能

---

## 八、故障排除

### 8.1 常見問題

#### 問題 1: 容器啟動失敗

**症狀**: `docker compose up -d` 執行後，容器立即停止

**可能的原因**:
- Docker 版本過舊
- 系統資源不足
- 網路配置問題

**解決方案**:
```bash
# 檢查 Docker 版本
docker --version

# 更新 Docker
docker-compose down
docker system prune -a
docker compose up -d
```

#### 問題 2: 無法連接到後端

**症狀**: Orb 客戶端顯示「連接錯誤」

**可能的原因**:
- 後端服務未運行
- 防火牆阻擋 3000 端口
- 環境變數設定錯誤

**解決方案**:
```bash
# 檢查後端服務狀態
docker logs sandboxed-sh

# 檢查端口監聽
netstat -tlnp | grep 3000

# 檢查環境變數
docker exec sandboxed-sh cat /root/.env
```

#### 問題 3: 任務執行失敗

**症狀**: 任務無法執行或返回錯誤

**可能的原因**:
- 工具集未安裝
- 工作空間隔離配置錯誤
- 模型 API 限額

**解決方案**:
```bash
# 檢查工具集
which claude-code
which opencode

# 查看任務日誌
journalctl -u sandboxed-sh.service

# 檢查 API 限額
curl http://localhost:3000/api/providers
```

### 8.2 日誌查看

#### Docker 容器日誌

```bash
# 查看所有日誌
docker logs sandboxed-sh

# 查看即時日誌
docker logs -f sandboxed-sh

# 查看指定時間範圍日誌
docker logs sandboxed-sh --since "1h"
```

#### systemd 服務日誌

```bash
# 查看系統日誌
systemctl status sandboxed-sh.service

# 查看即時日誌
journalctl -f -u sandboxed-sh.service

# 查看指定時間範圍日誌
journalctl -u sandboxed-sh.service -n 100
```

#### 後端應用日誌

```bash
# 進入容器查看日誌
docker exec sandboxed-sh cat /root/.sandboxed-sh/logs/*.log

# 查看 SQLite 資料庫
docker exec sandboxed-sh sqlite3 /root/.sandboxed-sh/missions.db "SELECT * FROM missions;"
```

### 8.3 數據庫管理

#### 備份數據庫

```bash
docker exec sandboxed-sh \
  cp /root/.sandboxed-sh/missions.db /root/backup/missions_backup_$(date +%Y%m%d).db

docker exec sandboxed-sh \
  cp /root/.sandboxed-sh/projects.db /root/backup/projects_backup_$(date +%Y%m%d).db
```

#### 還原數據庫

```bash
docker exec sandboxed-sh \
  cp /root/backup/missions_20240101.db /root/.sandboxed-sh/missions.db

docker exec sandboxed-sh \
  cp /root/backup/projects_20240101.db /root/.sandboxed-sh/projects.db

docker exec sandboxed-sh \
  chmod 600 /root/.sandboxed-sh/missions.db /root/.sandboxed-sh/projects.db
```

#### 清除數據（測試用）

```bash
docker exec sandboxed-sh rm -rf /root/.sandboxed-sh/*
docker exec sandboxed-sh chmod 600 /root/.sandboxed-sh/.env
docker compose restart sandboxed-sh
```

---

## 九、最佳實踐

### 9.1 安全建議

1. **密碼安全**: 使用強密碼和隨機生成的 JWT_SECRET
2. **防火牆配置**: 只允許必要的端口（3000）
3. **定期更新**: 保持 Docker 和後端程式庫更新
4. **備份策略**: 定期備份 SQLite 數據庫
5. **SSH 金鑰**: 使用只讀掛載防止意外修改

### 9.2 性能優化

1. **限制並行任務**: 設定合理的 `MAX_PARALLEL_MISSIONS`
2. **使用 SSD**: 數據庫和工作空間放在 SSD 上
3. **資源限制**: 設定合理的 cgroup 資源限制
4. **容器隔離**: 使用 `systemd-nspawn` 提升安全性

### 9.3 開發建議

1. **使用 debug 模式**: 控制平面使用 debug 編譯（非 release）
2. **模塊化技能**: 使用 `skills/<name>/SKILL.md` 格式
3. **Context 管理**: 合理管理本地 Context 資料夾大小
4. **日誌記錄**: 充分記錄任務執行過程

---

## 十、參考資源

### 10.1 官方文件

- [Orb 官網](https://orb.thomas.md/)
- [Docker 安裝指南](https://orb.thomas.md/install-docker)
- [原生 Linux 安裝](https://orb.thomas.md/setup)
- [工作空間隔離](https://orb.thomas.md/workspaces)
- [API & MCP 參考](https://orb.thomas.md/api)

### 10.2 GitHub 資源

- [Orb 專案](https://github.com/Th0rgal/orb)
- [Hermes Agent](https://github.com/Th0rgal/hermes-agent)
- [CLIProxyAPI Plus](https://github.com/kaitranntt/CLIProxyAPIPlus)
- [CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI)

### 10.3 社群資源

- [Discord 社群](https://relens.ai/community)
- [GitHub Issues](https://github.com/Th0rgal/orb/issues)
- [Release Notes](https://github.com/Th0rgal/orb/releases)

---

## 十一、附錄

### 11.1 環境變數參考

| 變數名稱 | 類型 | 描述 | 預設值 |
|----------|------|------|--------|
| `DEV_MODE` | Boolean | 開發模式 | false |
| `DASHBOARD_PASSWORD` | String | 後端登入密碼 | - |
| `JWT_SECRET` | String | JWT 簽名秘密 | - |
| `SANDBOXED_SH_USERS` | JSON | 多用戶認證 | [] |
| `LIBRARY_REMOTE` | String | Library Git URL | - |
| `MAX_PARALLEL_MISSIONS` | Integer | 最大並行任務數 | 10 |
| `SANDBOXED_OAUTH_OWNER` | String | OAuth 擁有者 | cli-proxy |

### 11.2 命令參考

```bash
# 啟動服務
docker compose up -d

# 停止服務
docker compose down

# 查看日誌
docker logs -f sandboxed-sh

# 重新啟動
docker compose restart sandboxed-sh

# 進入容器
docker exec -it sandboxed-sh bash

# 重建後端
cargo build --bin sandboxed-sh --bin sandboxed-mcp --bin sandboxed-node --bin palomactl

# 安裝工具集
npm install -g @anthropic-ai/claude-code
curl -fsSL https://opencode.ai/install | bash -s -- --no-modify-path
```

### 11.3 服務端口

| 服務 | 端口 | 描述 |
|------|------|------|
| API / Web | 3000 | 後端 API 和 Web 控制台 |
| MCP | 3001 | MCP 夥伴服務 |

---

**版本**: 1.0  
**最後更新**: 2025 年 12 月  
**作者**: AI Assistant (基於官方文件整理)
