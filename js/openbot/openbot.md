# CopilotKit OpenBot

- 緣起：
  - 先前觀察中的 AG-UI 通訊協定，都是 CopilotKit 這間公司在辦活動。
  - 最近看到 Ray Lin 分享 Open
  - CopilotKit 最近又辦了多場關於 OpenBot for Enterprise 的活動。
  - 經查 OpenBot 是基底實作，而 OpenFuse, OpenDuet, OpenDots 則是蓋在 OpenBot 上的「範本」

> [!NOTE]
> 根據 "https://github.com/CopilotKit/openbot https://open.bot/" 內容，用繁體中文（台灣技術用詞）撰寫一篇技術報告，含 step-by-step 安裝、測試、驗證步驟，存成 "js/openbot/openbot.md" .

## OpenBot 技術報告

### 概述

**OpenBot** 是由 CopilotKit 開發的模組化、可自我託管的 AI 協作者工作空間。它讓企業能夠自定義 AI 助手，同時保持對基礎設施、模型和工具的完全控制。

#### 核心特性

- **模組化架構**：支援自定義模型、代理和工具
- **自我託管**：可在 Kubernetes、雲端或本地部署
- **企業級治理**：內建 SSO、審計日誌、權限控制
- **AG-UI 支援**：支援所有 AG-UI 相容的代理框架
- **Open Source**：MIT 授權，完全開放原始碼

### 系統需求

#### 基本需求

| 項目 | 版本 | 說明 |
|------|------|------|
| Docker | 最新版本 | 用於 PostgreSQL、API 伺服器及內建 Bot |
| Bun | 1.4+ | 應用程式、設定輔助程式及測試 |
| Git | 最新版本 | 用於克隆原始碼 |
| CopilotKit 帳號 | 免費方案 | 用於 CopilotKit Intelligence |
| 模型 API 金鑰 | OpenAI/Anthropic/Google | 依配置選擇 |

#### 平台需求

- **macOS**：Docker Desktop (Apple Silicon 或 Intel)
- **Windows**：WSL 2 + Ubuntu (推薦)
- **Kubernetes**：amd64 節點，預設 StorageClass, `kubectl`, Helm

### Step-by-Step 安裝流程

#### 步驟 1：克隆原始碼

```bash
git clone https://github.com/CopilotKit/OpenBot.git
cd OpenBot
```

#### 步驟 2：初始化環境

```bash
cp .env.example .env
bun install
```

#### 步驟 3：設定 CopilotKit Intelligence

##### 選項 A：本地安裝（預設）

```bash
npx --yes copilotkit@latest login
npx --yes copilotkit@latest local setup
npx --yes copilotkit@latest local connect --approve-connection
```

> **說明**：此選項會在本機安裝 Intelligence，適用於 macOS 搭配 Docker Desktop。免費開發者方案支援 30 天授權。

##### 選項 B：使用託管專案

```bash
## 設定環境變數
INTELLIGENCE_API_URL=https://api.intelligence.copilotkit.ai
INTELLIGENCE_GATEWAY_WS_URL=wss://realtime.intelligence.copilotkit.ai

## 登入並選擇專案
npx --yes copilotkit@latest login
npx --yes copilotkit@latest project select

## 設定 Learning container
bun scripts/setup-learning.ts
```

#### 步驟 4：填充環境變數

編輯 `.env` 檔案，填充以下必填項目：

```bash
## 使用 OpenSSL 產生加密金鑰
openssl rand -base64 32

## 設定模型 API 金鑰（範例使用 OpenAI）
OPENAI_API_KEY="sk-xxxxx"
## 或用於 Anthropic
ANTHROPIC_API_KEY="sk-ant-xxxxx"
BOT_PROVIDER="anthropic"
```

> **注意**：`KEY_ENCRYPTION_KEY` 範例值為公開，建議產生自己的金鑰。

#### 步驟 5：啟動服務

```bash
bash scripts/start.sh
```

> **說明**：此腳本會：
> - 拉取 OpenBot 映像檔（依據 `backend-images.env` 中的標籤）
> - 啟動 Docker 服務（PostgreSQL、API 伺服器、Bot）
> - 啟動 API 伺服器（端口 3001）
> - 啟動應用程式（端口 3010）
> - 檢查服務健康狀態

#### 步驟 6：訪問應用程式

開啟瀏覽器至：<http://localhost:3010>

### 驗證步驟

#### 1. 基本功能測試

##### 測試 1：開啟瀏覽器並執行指令

1. 開啟 `/bot` 頁面
2. 輸入指令：`Open news.ycombinator.com and tell me the top story.`
3. **預期結果**：Bot 應該開啟瀏覽器並顯示網站內容

##### 測試 2：表單填寫與審計

1. 要求 Bot 填寫 <https://httpbin.org/forms/post>
2. 查看 `/admin/audit` 頁面
3. **預期結果**：應該看到完整的審計日誌記錄

##### 測試 3：權限邊界設定

1. 開啟 `/admin/boundaries`
2. 新增 deny rule 或 preset
3. 重新嘗試相同的瀏覽器動作
4. **預期結果**：動作應被拒絕，且拒絕原因應顯示對應規則

#### 2. Bot 創建與測試

##### 步驟 1：創建 Bot

1. 開啟 `/bots` 頁面
2. 創建一個具有常駐角色（standing role）的 Bot
3. 與該 Bot 開啟通訊頻道

##### 測試：Bot 日常任務

```
要求 Bot 執行以下任務：
- 檢查 Google Drive 中的飯店收據是否符合差旅政策
- 分別顯示房費和稅金，以便決定是否符合每晚限制
```

##### 步驟 2：Teach a Bot

1. 使用 **Teach a Bot** 功能記錄期望的步驟
2. 應用到下一個類似的請求
3. **預期結果**：Bot 應按照記錄的步驟執行

#### 3. 審計與監控

##### 檢查審計日誌

```bash
## 查看伺服器日誌
docker compose logs server

## 查看應用程式日誌
docker compose logs app
```

##### 審計頁面驗證

1. 開啟 `/admin/audit`
2. **預期結果**：應該能看到：
   - 所有允許的動作
   - 所有拒絕的動作
   - 失敗的動作
   - 每個拒絕都應顯示觸發的規則

### 部署選項

#### 選項 A：單機部署（推薦用於開發）

使用提供的腳本即可，適合個人使用和實驗。

#### 選項 B：Docker 單一映像

```bash
## 使用最新發布的映像
docker run -p 3001:3001 --env-file .env \
  -e EMBEDDED_POSTGRES=on -v openbot-data:/var/lib/postgresql \
  ghcr.io/copilotkit/openbot:latest

## 或使用特定版本標籤
docker run -p 3001:3001 --env-file .env \
  -e EMBEDDED_POSTGRES=on -v openbot-data:/var/lib/postgresql \
  ghcr.io/copilotkit/openbot:v1.0.1
```

> **注意**：此方式將應用程式、API、Bot 瀏覽器及可選 PostgreSQL 整合在單一映像中。

#### 選項 C：Kubernetes 部署（團隊版）

```bash
## 1. 建立配置檔案 openbot-values.yaml
cat > openbot-values.yaml << EOF
config:
  singleUser: true
postgresql:
  enabled: true
secrets:
  licenseToken: "<your CopilotKit trial or production license>"
  modelApiKey: "<your OpenAI API key>"
EOF

## 2. 安裝 Chart
helm install openbot https://github.com/CopilotKit/OpenBot/releases/download/v1.0.2/openbot-0.2.0.tgz \
  --namespace openbot --create-namespace \
  --values openbot-values.yaml \
  --timeout 15m

## 3. 開啟評價環境
kubectl -n openbot get pods,jobs
kubectl -n openbot port-forward svc/openbot-server 3001:3001

## 4. 開啟 <http://127.0.0.1:3010>
```

> **注意**：Kubernetes 部署需要：
> - amd64 節點
> - 預設 StorageClass
> - `kubectl` 和 Helm
> - 試用或生產授權
> - 模型金鑰

### 常見問題排障

#### 問題 1：服務無法啟動

**症狀**：`scripts/start.sh` 失敗

**解決方法**：
```bash
## 檢查 Docker 狀態
docker ps -a

## 查看伺服器日誌
docker compose logs server

## 手動拉取映像
docker pull ghcr.io/copilotkit/openbot:latest
```

#### 問題 2：Intelligence 連接失敗

**症狀**：登入頁面無法載入

**解決方法**：
```bash
## 確認 CopilotKit 帳號已登入
npx --yes copilotkit@latest login

## 重新連接
npx --yes copilotkit@latest local connect --approve-connection

## 確認 .env 中的設定正確
cat .env | grep INTELLIGENCE
```

#### 問題 3：Composio 設定失敗

**解決方法**：
```bash
## 手動設定 Composio
bun run setup:composio

## 或稍後重試
bun run setup:composio
```

#### 問題 4：Windows 環境問題

**解決方案**：
```bash
## 使用 WSL 2 在 Ubuntu 中克隆
## 所有步驟從 Ubuntu 終端機執行
## 在 Windows 瀏覽器開啟 <http://127.0.0.1:3010>
```

### 維護與管理

#### 停止服務

```bash
bash scripts/stop.sh
```

> **注意**：
> - `--keep-computers` 參數可保留 Bot 電腦運行
> - 不會刪除資料庫、Bot 檔案和瀏覽器配置（這些是 volumes）

#### 重新啟動

```bash
bash scripts/start.sh
```

#### 授權 Renewal

```bash
##  renew local license（每 30 天）
npx copilotkit@latest local renew
```

### 安全考量

#### 1. 權限管理

- **單一登入（SSO）**：支援 Google、Microsoft、Okta 或自定義 SAML/OpenID Connect
- **角色控制**：為每個 Bot、角色和使用者設定工具存取
- **審計追蹤**：所有存取和動作都記錄

#### 2. 秘密管理

- **加密儲存**：透過 `/admin/credentials` 寫入，永不透過 API 返回
- **審計事件紅字**：記錄秘密被請求的事實，但不記錄內容
- **永久的金鑰紅字**：從審計事件中移除

#### 3. 邊界控制

- **CEL 策略**：規則可檢查 `tool.name`、`intent`、`bot.id`、`actor.id` 等
- **Fail closed**：缺失的政策禁止所有動作，損壞的規則拒絕而非開啟
- **循環迴路預設**：電腦綁定到 `127.0.0.1`，需要每容器權杖

#### 4. 審計日誌

- **完整追蹤**：每個項目存取和每個動作都記錄
- **拒絕原因**：每個拒絕都攜帶觸發的規則
- **導出功能**：可將審計事件導出到安全團隊使用的 SIEM

### 最佳實踐

#### 1. 環境配置

```bash
## 不要將 .env 提交到版本控制
## 生產環境使用 Kubernetes Secrets 或外部金鑰管理系統
```

#### 2. 模型選擇

- **OpenAI**：最穩定，範例預設配置
- **Anthropic**：適合複雜推理任務
- **本地模型**：需要 OpenAI 相容端點

#### 3. Bot 設計

- **明確指令**：為每個 Bot 設定清晰的目標和權限
- **漸進授權**：先給讀取權限，再給寫入權限
- **審計監控**：定期查看審計日誌

#### 4. 團隊部署

- **SSO 設定**：優先使用公司現有身份驗證
- **多因素認證**：為高權限 Bot 啟用 MFA
- **預算控制**：設定每日、每週和每月 Token 限制

### 參考資源

- [官方文件](https://docs.open.bot)
- [架構詳細說明](docs/architecture.md)
- [自動學習](docs/automatic-learning.md)
- [Composio 設定](docs/plugins/composio.md)
- [Web 研究](docs/web-research.md)
- [開發指南](docs/development.md)
- [Kubernetes 部署](#deploy-on-kubernetes)

### 授權資訊

- **OpenBot 應用程式模板**：MIT 授權
- **CopilotKit Intelligence**：獨立授權，需要生產環境授權
- **完全本地選項**：可在自己機器上運行所有組件

> **注意**：完全本地運行需要免費的本地 Intelligence 授權（開發者方案）。雲端模型或線上應用程式仍會將請求發送給該服務。

### 版本資訊

- **當前版本**：v1.0.x
- **GitHub 星數**：12.4K+
- **狀態**：活躍開發中

*最後更新：2024 年*
