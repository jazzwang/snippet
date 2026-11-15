# LoopForge 技術報告

## 一、系統概述

### 1.1 什麼是 LoopForge

**LoopForge** 是騰訊開源的一個可自主部署的團隊工作平台，讓開發團隊與編碼 AI Agent 協同交付軟體。平台提供兩種核心工作模式：

1. **對話工作模式**：透過 Main Bot 對話描述需求，系統自動建立 Docker 沙箱工作區，分派任務給專案角色，最終提交 PR
2. **SOP 工作模式**：將驗證過的工作方式固化為標準作業程序（SOP），包含 Agent、腳本和人工核對的標準化流程

### 1.2 核心優勢

- **可重複性**：同一 SOP 確保每個需求都有相同的執行階段和檢查
- **角色分離**：需求澄清、設計、實現、獨立審查、測試各有獨立的角色提示詞、執行器、模型、規則和工具
- **人在迴路**：關鍵節點設置人工審批，可打回指定環節返工
- **可觀測**：節點狀態、工具軌跡、日誌和產物集中呈現
- **完全自主**：技術棧和伺服器都是自己的，執行器支援 10 種編碼 Agent CLI

### 1.3 支援的執行器

| 執行器 | 憑證 | 安裝方式 |
|--------|------|----------|
| CodeBuddy | 個人 Key 或平台共享 Key | Docker 鏡像內建 |
| Codex | 個人 Key | Docker 鏡像內建 |
| Claude Code | 個人 Key | npm 安裝並快取 |
| OpenCode / Kimi Code / Pi | 僅個人 Key | npm 安裝並快取 |
| DeepSeek Harness | 僅個人 Key | Docker 鏡像內建 |
| Cursor CLI / Antigravity | 僅個人 Key | 廠商安裝腳本 |
| ZCode | 僅個人 Key | 需安裝到服務或執行機器的 PATH |

---

## 二、系統需求

### 2.1 平台版（Container Installation）

| 項目 | 需求 |
|------|------|
| 作業系統 | Linux、macOS、Windows（WSL2） |
| Docker | 安裝並可執行 |
| Docker Compose | v2.x |
| Python 3 | 用於安裝腳本驗證 |
| 網路 | 可存取 Docker 鏡像站（ghcr.io） |
| 權限 | 需要 sudo 權限或加入 Docker 群組 |

### 2.2 LoopForge Local 版

| 項目 | 需求 |
|------|------|
| 作業系統 | macOS、Linux |
| Node.js | v20+ |
| Python 3 | v3.8+ |
| 編碼助手 | Claude Code、CodeBuddy、Codex、Cursor 等 |

---

## 三、安裝步驟

### 3.1 平台版快速安裝（推薦）

#### 步驟 1：準備環境

```bash
# 確認 Docker 和 Docker Compose 已安裝
docker --version
docker compose version

# 確認網路可連接 ghcr.io
curl -I https://ghcr.io
```

#### 步驟 2：克隆官方倉庫

```bash
git clone https://github.com/Tencent/LoopForge.git
cd LoopForge
```

#### 步驟 3：執行安裝腳本

```bash
# 互動式安裝（預設）
./start.sh
```

安裝腳本會自動：
- 檢查 Docker、Compose、Python 3 和 curl
- 補裝缺少的組件（Linux 使用 apt/dnf/yum，macOS 使用 Homebrew）
- 拉取官方 Docker 鏡像 `ghcr.io/tencent/loopforge:0.3.9-rc.1`
- 建立 MySQL 和平台服務
- 生成配置與會話密鑰
- 導入內建沙箱、通用 SOP 和體驗專案

**接受安裝提示**：`LOOPFORGE_YES=1 ./start.sh`

#### 步驟 4：處理網路緩慢問題（中國大陸）

國內拉取 `ghcr.io` 經常中斷，建議使用鏡像站：

```bash
# 使用南京大學 GHCR 鏡像站
MIRROR=ghcr.nju.edu.cn ./start.sh

# 或者使用其他可用鏡像站
MIRROR=ghcr.aliyuncs.com ./start.sh
```

**驗證鏡像摘要**：
```bash
docker image inspect --format '{{index .RepoDigests 0}}' ghcr.io/tencent/loopforge:0.3.9-rc.1
```

#### 步驟 5：管理服務

```bash
# 檢視日誌
./start.sh logs

# 停止服務
./start.sh stop

# 完全移除容器但保留資料
./start.sh down

# 重啟服務
./start.sh restart

# 拉取最新鏡像
./start.sh pull

# 從源碼構建（開發用途）
./start.sh dev
```

---

### 3.2 LoopForge Local 版安裝

LoopForge Local 將工作流直接帶入您正在使用的編碼助手，無需部署服務端。

#### 步驟 1：安裝 CLI

```bash
# 安裝 LoopForge CLI
npm install -g loopforge-cli
```

#### 步驟 2：安裝特定執行器

| 執行器 | 安裝命令 |
|--------|----------|
| CodeBuddy | `npx -y loopforge-cli@latest install codebuddy` |
| Codex | `npx -y loopforge-cli@latest install codex` |
| Cursor | `npx -y loopforge-cli@latest install cursor` |
| Claude Code | `npx -y loopforge-cli@latest install claude` |
| DeepSeek Harness | `npx -y loopforge-cli@latest skills install dsh` |

#### 步驟 3：驗證安裝

```bash
# 檢查安裝狀態
npx -y loopforge-cli@latest status codebuddy

# 環境診斷
npx -y loopforge-cli@latest doctor
```

#### 步驟 4：啟動工作流

```bash
# 在專案目錄中執行
/start-devflow "添加訂單列表的狀態篩選功能並覆蓋 API 測試"

# 或簡寫形式
/devflow "添加訂單列表的狀態篩選功能並覆蓋 API 測試"
```

---

## 四、測試與驗證步驟

### 4.1 平台版快速驗證

#### 步驟 1：訪問平台

```bash
# 服務預設監聽 8090 端口
# 打開瀏覽器訪問：
# - 本地：http://localhost:8090
# - 網路：http://<您的 IP>:8090
```

#### 步驟 2：建立第一個帳號

1. 在瀏覽器中打開平台網址
2. 點擊「建立帳號」
3. 輸入帳號名稱和密碼
4. 第一個帳號自動成為平台管理員

**安全提醒**：建立帳號前，請限制防火牆或安全組僅允許您的 IP 訪問

#### 步驟 3：無 API Key 體驗（推薦新手）

LoopForge 內建「平台驗收·腳本與審批」SOP，無需 API Key 即可體驗：

1. 切換到體驗專案
2. 打開 **流程範本**
3. 進入 **平台驗收·腳本與審批**
4. 點擊 **執行流程**
5. 觀察腳本生成報告
6. 在 **待我確認** 或執行詳情頁審批通過

#### 步驟 4：完整功能測試

**準備 API Key**：
- 進入個人設定
- 選擇執行器（如 CodeBuddy）
- 輸入 API Key 或選擇平台共享 Key

**測試對話工作流**：
1. 在首頁輸入框描述需求
2. 使用 `@` 引用角色、技能、需求、SOP
3. 觀察 Main Bot 建立工作區並執行任務
4. 檢視產出成果

**測試 SOP 工作流**：
1. 進入流程設計器
2. 選擇內建 SOP（如「通用後端交付」）
3. 配置專案設定
4. 執行流程
5. 審批人工關卡
6. 查看最終產出

### 4.2 測試用例清單

#### 基本功能測試

| 測試項目 | 預期結果 | 驗證方式 |
|----------|----------|----------|
| 帳號建立 | 成功建立第一個管理員帳號 | 登入驗證 |
| 服務啟動 | 平台監聽 8090 端口 | netstat -tlnp \| grep 8090 |
| 日誌輸出 | 安裝腳本輸出平台地址 | 檢查終端輸出 |
| 帳號登入 | 成功登入平台 | 瀏覽器頁面 |
| 體驗 SOP 執行 | 腳本生成報告並等待審批 | 查看產出 |

#### 核心功能測試

| 測試項目 | 測試步驟 | 預期結果 |
|----------|----------|----------|
| 對話工作流 | 描述需求 → Main Bot 回應 → 建立工作區 | 工作區自動建立，任務執行 |
| 專案綁定 | 連接 GitHub → 選擇專案 → 提交 PR | PR 成功創建 |
| SOP 執行 | 選擇 SOP → 配置 → 執行 | 各節點順序執行，可審批 |
| 人工關卡 | 執行到人工關卡 → 審批通過 | 流程繼續執行 |
| 打回重做 | 審批不通過 → 打回上游 | 流程退回指定節點 |

#### 執行器測試

| 執行器 | 測試項目 | 驗證方式 |
|--------|----------|----------|
| CodeBuddy | 執行需求澄清 | 觀察對話回應 |
| Codex | 執行程式碼生成 | 檢視生成內容 |
| Claude Code | 執行任務 | 檢查輸出檔案 |
| DeepSeek Harness | 執行任務 | 驗證結果 |

### 4.3 驗證腳本測試

在專案目錄中測試腳本功能：

```bash
# 執行簡單的腳本任務
./start.sh logs
# 觀察日誌輸出，確認平台運行正常
```

---

## 五、配置與部署

### 5.1 環境變數配置

在 `.env` 文件中配置重要參數：

```bash
# HTTP 端口
AGENTFLOW_HTTP_PORT=8090

# MySQL 端口
AGENTFLOW_MYSQL_PORT=3306

# 綁定地址
LOOPFORGE_BIND=0.0.0.0

# 公開 URL（可選）
LOOPFORGE_PUBLIC_URL=http://localhost:8090

# 允許註冊
AGENTFLOW_ALLOW_SIGNUP=true

# 會話密鑰（預設隨機生成）
AGENTFLOW_SESSION_SECRET

# GitHub OAuth（自定義應用）
AGENTFLOW_GITHUB_CLIENT_ID
```

### 5.2 Git SSH 配置

#### 步驟 1：建立已知主機檔案

```bash
# 建立已知主機檔案
mkdir -p ~/.ssh/loopforge
touch ~/.ssh/loopforge/known_hosts

# 添加 Git 主機公鑰（以 GitHub 為例）
curl -s https://github.com/known_hosts >> ~/.ssh/loopforge/known_hosts
```

#### 步驟 2：配置環境變數

```bash
# 設定 SSH 已知主機檔案路徑
export AGENTFLOW_GIT_SSH_KNOWN_HOSTS=~/.ssh/loopforge/known_hosts
```

#### 步驟 3：建立 SSH 密鑰

```bash
# 建立無密碼 SSH 密鑰
ssh-keygen -t ed25519 -C "loopforge@your-email" -f ~/.ssh/loopforge/id_loopforge -N ""

# 將公鑰添加到您的 Git 平台（如 GitHub、GitLab）
cat ~/.ssh/loopforge/id_loopforge.pub
```

### 5.3 GitHub 整合

#### 方式 1：使用內建 LoopForge OAuth App

1. 點擊「連接 GitHub」
2. 複製顯示的 PIN
3. 在 GitHub 上批准 LoopForge 應用
4. 完成授權

#### 方式 2：自定義 OAuth App（管理員）

```bash
# 在 .env 中配置
AGENTFLOW_GITHUB_CLIENT_ID=your-client-id
```

### 5.4 安全組配置

#### 建議配置

| 端口 | 用途 | 建議 |
|------|------|------|
| 8090 | 平台 HTTP | 限制管理員 IP |
| 3306 | MySQL | 僅 Docker 網橋 |
| 22 | SSH（可選） | 僅管理員 IP |

#### 雲平台安全組

**Tencent Cloud（騰訊雲）**：
```bash
# 安裝腳本會自動讀取元數據並提示
# 手動配置：
# 入方向規則：TCP 8090，源：管理員 IP
```

**AWS EC2**：
```bash
# 安裝腳本會自動讀取公網 IP
# 安全組：端口 8090，來源：0.0.0.0/0（測試階段）
# 生產環境：限制管理員 IP
```

---

## 六、常見問題排解

### 6.1 安裝失敗

**問題**：`./start.sh` 失敗，提示缺少依賴

**解決方案**：
```bash
# 手動安裝 Python 和 curl（Ubuntu/Debian）
sudo apt update
sudo apt install python3 python3-pip curl

# macOS
brew install python curl

# 重試安裝
./start.sh
```

### 6.2 Docker 鏡像拉取失敗

**問題**：ghcr.io 連接中斷

**解決方案**：
```bash
# 使用鏡像站
MIRROR=ghcr.nju.edu.cn ./start.sh

# 或使用阿里云鏡像站
MIRROR=ghcr.aliyuncs.com ./start.sh
```

### 6.3 端口已被佔用

**問題**：端口 8090 已被使用

**解決方案**：
```bash
# 修改端口
export AGENTFLOW_HTTP_PORT=8091
./start.sh
```

### 6.4 SSH Git 連接失敗

**問題**：Git SSH 連接失敗

**解決方案**：
```bash
# 確認 SSH 密鑰已添加
cd ~/.ssh/loopforge
ls -la

# 確認已知主機檔案正確
cat known_hosts | grep github.com

# 測試 SSH 連接
ssh -i ~/.ssh/loopforge/id_loopforge git@github.com
```

### 6.5 API Key 配置錯誤

**問題**：執行器返回認證錯誤

**解決方案**：
1. 進入個人設定
2. 重新輸入 API Key
3. 確認 Key 有對應的模型權限
4. 測試模型連接

---

## 七、升級指南

### 7.1 平台版升級

```bash
# 1. 拉取最新代碼
git fetch --tags && git checkout vX.Y.Z

# 2. 拉取新鏡像
./start.sh pull

# 資料不會丟失，容器的 Compose volume 會保留
```

### 7.2 源碼開發模式升級

```bash
# 切換到源碼構建模式
./start.sh dev

# 重新構建
./start.sh dev

# 切回官方鏡像
./start.sh release
```

---

## 八、最佳實踐

### 8.1 生產環境部署

1. **使用 HTTPS 反向代理**
   ```bash
   # Nginx 配置示例
   server {
       listen 443 ssl http2;
       server_name loopforge.example.com;

       ssl_certificate /etc/ssl/certs/loopforge.crt;
       ssl_certificate_key /etc/ssl/private/loopforge.key;

       location / {
           proxy_pass http://localhost:8090;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
       }
   }
   ```

2. **配置身份驗證表頭**
   ```bash
   # 企業單點登入
   AGENTFLOW_TRUST_IDENTITY_HEADERS=true
   AGENTFLOW_IDENTITY_HEADER_SECRET=random-secret-key
   ```

3. **限制帳號註冊**
   ```bash
   # 生產環境關閉自動註冊
   AGENTFLOW_ALLOW_SIGNUP=false
   ```

### 8.2 開發環境最佳實踐

1. **使用 `.local/` 目錄**：將 `.env`、`.local/` 和資料庫 volume 放在版本控制之外
2. **定期備份**：定期備份 `mysql` 容器的資料卷
3. **監控日誌**：設定日誌監控和告警
4. **資源限制**：為容器設定合理的 CPU 和記憶體限制

---

## 九、參考文檔

| 主題 | 文檔位置 |
|------|----------|
| 部署指南 | [docs/deployment.md](https://github.com/Tencent/LoopForge/blob/main/docs/deployment.md) |
| 對話工作區 | [docs/conversation-workspaces.md](https://github.com/Tencent/LoopForge/blob/main/docs/conversation-workspaces.md) |
| AI 定時任務 | [docs/ai-scheduled-task-capabilities.md](https://github.com/Tencent/LoopForge/blob/main/docs/ai-scheduled-task-capabilities.md) |
| Token 成本統計 | [docs/token-pricing.md](https://github.com/Tencent/LoopForge/blob/main/docs/token-pricing.md) |
| 本地工作流 | [docs/local/usage.md](https://github.com/Tencent/LoopForge/blob/main/docs/local/usage.md) |
| API 參考 | [docs/api/README.md](https://github.com/Tencent/LoopForge/blob/main/docs/api/README.md) |
| 架構說明 | [docs/architecture.md](https://github.com/Tencent/LoopForge/blob/main/docs/architecture.md) |

---

## 十、社群與貢獻

- **GitHub 倉庫**：https://github.com/Tencent/LoopForge
- **官方網站**：https://loopforge.cn
- **貢獻指南**：[CONTRIBUTING.zh-CN.md](https://github.com/Tencent/LoopForge/blob/main/CONTRIBUTING.zh-CN.md)
- **安全政策**：[SECURITY.zh-CN.md](https://github.com/Tencent/LoopForge/blob/main/SECURITY.zh-CN.md)

---

*技術報告版本：1.0*
*最後更新：2026 年*
