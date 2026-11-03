# Rakazo 技術報告

## 1. 專案概述

### 1.1 專案簡介

Rakazo 是一個開源 AI Agent 平台，用於建立持久化團隊成員（persistent teammates）和可自行託管的 AI 助手。該專案支援 Web、Electron 桌面應用程式以及 iOS 和 Android 行動裝置。使用者可自帶模型和電腦提供者，或完全在本地運行整個技術棧。

Rakazo 是 Grok Bot、Meta Muse、OpenAI Dots、Instinct、OpenClaw、Hermes Agent 和 Claude Duet 等商業產品的開源自行託管替代方案。

### 1.2 核心功能

- **持久化 AI 機器人（Persistent Bots）**：擁有獨立對話、記憶、常態任務和歷史記錄
- **語音模式（Voice Mode）**：支援語音回覆、口述指令和呼叫機器人，可自帶 ElevenLabs、OpenAI、Cartesia 或 Fish Audio API 金鑰，或使用 Mac 伺服器已安裝的聲音
- **共享團隊電腦（Shared Team Computers）與隔離私人電腦（isolated Private computers）**
- **瀏覽器、終端機、檔案和圖形桌面存取**
- **機器人可委派給同儕機器人或短壽命子代理人（subagents）**
- **透過 Pi 自帶模型憑證**
- **應用程式整合**：透過 Composio 或 Pipedream Connect，加上使用者自行安裝的 Treg、遠端 MCP（Model Context Protocol）和 OpenAPI 工具來源
- **電腦提供者支援**：Docker、E2B、Daytona、CreateOS、Boat 以及受信任的本地電腦支援

## 2. 技術棧

Rakazo 採用現代化的全棧技術架構：

| 層面 | 技術 |
|------|------|
| 前端 | TypeScript、React 19、Vite、Tailwind CSS |
| 桌面應用程式 | Electron 和 Expo |
| 後端 API | Hono 和 oRPC |
| 數據庫 | PostgreSQL 和 Prisma ORM |
| 身份驗證 | Better Auth |
| 背景任務 | Graphile Worker |
| AI 模型 | Pi（支援自帶模型） |
| 電腦執行環境 | Docker、E2B、Daytona、CreateOS、Boat |
| 整合平台 | Composio、Pipedream Connect、MCP、OpenAPI |

## 3. 安裝與部署

### 3.1 快速啟動（使用已發布的 Docker 影像）

此方法無需複製程式碼或安裝 Node.js，只需 Docker Engine。

#### 3.1.1 環境要求

- Docker Engine 26 或更新版本（支援 Compose 外掛程式）
- `curl` 和 `OpenSSL` 工具
- 網路連線（用於拉取 Docker 影像和下載安裝腳本）

#### 3.1.2 安裝步驟

1. **建立工作目錄並下載安裝腳本**：

```bash
mkdir -p rakazo && cd rakazo && \
curl -fsSLO https://raw.githubusercontent.com/elie222/rakazo/main/infra/compose/install-images.sh && \
bash install-images.sh
```

2. **安裝腳本執行流程**：
   - 下載 `docker-compose.images.yml` 和 `.env.images.example`
   - 自動建立 `.env` 檔案並生成隨機安全密鑰
   - 拉取所需 Docker 影像（Postgres 和 `ghcr.io/elie222/rakazo/app`）
   - 啟動所有服務

3. **開啟 Web 介面**：

```bash
# 預設端口 5173
http://127.0.0.1:5173
```

4. **完成初始設定**：
   - 註冊新帳戶
   - 連接 AI 模型提供者（OpenRouter、OpenAI 等）

#### 3.1.3 自訂化部署

如需自訂公開 URL、影像標籤或選用提供者，使用 `--prepare-only` 參數：

```bash
bash install-images.sh --prepare-only
# 編輯 .env 檔案設定環境變數
bash install-images.sh
```

常用環境變數：

| 變數 | 說明 |
|------|------|
| `SANDBOX_PROVIDER` | 電腦沙盒提供者（預設 `docker`），可選 `e2b`、`novita`、`daytona`、`createos`、`boat` |
| `RAKAZO_HOST` | 公開域名（如 `app.example.com`） |
| `OPENROUTER_API_KEY` | OpenRouter API 金鑰 |
| `COMPOSIO_API_KEY` | Composio API 金鑰（選用） |

### 3.2 本地開發（原始碼檢查出）

適合開發者進行程式碼修改和測試。

#### 3.2.1 環境要求

| 工具 | 版本要求 |
|------|----------|
| Node.js | 22.22.2 或更新（22.x 系列）、24.x 或 26+ |
| pnpm | 9.x |
| Docker | 任意版本 |

**注意**：Node.js 23.x 和 25.x 不支援。

#### 3.2.2 安裝步驟

```bash
# 1. 複製原始碼
git clone https://github.com/elie222/rakazo.git
cd rakazo

# 2. 複製環境範例檔案
cp .env.example .env

# 3. 生成並設定安全密鑰
# 執行以下命令生成 16 位元的隨機密鑰：
POSTGRES_PASSWORD=$(openssl rand -hex 16)
POSTGRES_APP_PASSWORD=$(openssl rand -hex 16)
BETTER_AUTH_SECRET=$(openssl rand -hex 32)
ENCRYPTION_KEY=$(openssl rand -hex 64)
SCREEN_PROXY_SECRET=$(openssl rand -hex 32)
SANDBOX_SUPERVISOR_TOKEN=$(openssl rand -hex 32)

# 將上述變數設定到 .env 檔案中
# 將 POSTGRES_PASSWORD 和 POSTGRES_APP_PASSWORD 分別放入 DATABASE_MIGRATION_URL 和 DATABASE_URL

# 4. 安裝依賴
pnpm install

# 5. 建立電腦沙盒影像
pnpm sandbox:build

# 6. 啟動開發環境
pnpm dev
```

#### 3.2.3 Docker 沙盒設定

對於使用 Docker Desktop 的開發者，設定 `SANDBOX_CONTROL_VIA_LOOPBACK=true`：

```env
SANDBOX_CONTROL_VIA_LOOPBACK=true
```

此設定會讓監理服務透過 Docker Desktop 的使用者 socket 自動發現，或透過 `DOCKER_HOST` / `DOCKER_SOCKET` 變數指定其他 Docker 執行環境。

#### 3.2.4 使用 Compose 運行 PostgreSQL

要使用 Compose 檔案中的 PostgreSQL，啟動 `postgres-host` 覆蓋檔：

```bash
docker compose --env-file .env \
  -f infra/compose/docker-compose.yml \
  -f infra/compose/docker-compose.postgres-host.yml \
  up postgres -d
```

使用 URI 安全的 `POSTGRES_PASSWORD`（`openssl rand -hex 16`）。現有的 `pgdata` 卷會保留使用者、密碼和資料庫，因此首次初始化後請保持這些值在 `.env` 中，或使用 `ALTER ROLE` 直接在原處修改。

### 3.3 在伺服器上運行

適合部署在 VPS（虛擬私人伺服器）上，讓使用者透過桌面、行動或瀏覽器連接。

#### 3.3.1 安裝步驟

```bash
# 1. 準備影像（不立即啟動）
bash install-images.sh --prepare-only

# 2. 編輯 .env 檔案
# 設定電腦沙盒提供者：SANDBOX_PROVIDER=boat（或 e2b / daytona / createos）
# 並加入對應的 API 金鑰
# 設定公開域名：RAKAZO_HOST=your.domain

# 3. 啟動服務
bash install-images.sh
```

#### 3.3.2 生產環境設定

1. **在 HTTPS 前端加裝端口 5173**：使用 Caddy 或 Nginx 反向代理

```caddyfile
app.example.com {
    reverse_proxy 127.0.0.1:5173
}
```

2. **設定環境變數**：
   - `BETTER_AUTH_URL`：完整的 HTTPS 來源 URL
   - `WEB_ORIGIN`：完整的 HTTPS 來源 URL
   - `API_URL`：完整的 HTTPS 來源 URL
   - `RAKAZO_HOST`：主機域名（如 `app.example.com`）

3. **桌面應用程式連接**：
   - 在桌面 App 中選擇 **Existing instance**
   - 輸入 `https://` 開頭的網址

#### 3.3.3 Railway 部署

也可透過 [Railway](https://railway.com/new/template/rakazo-template) 快速部署，詳細說明請參閱 [Railway 設定指南](https://github.com/elie222/rakazo/tree/main/infra/railway)。

## 4. 配置與環境變數

### 4.1 必要環境變數

#### 4.1.1 資料庫設定

```env
# PostgreSQL 主密碼（用於資料庫初始化和遷移）
POSTGRES_PASSWORD=<32 位元以上的隨機字串>

# PostgreSQL 應用程式密碼（rakazo_app 使用者）
POSTGRES_APP_PASSWORD=<32 位元以上的隨機字串>

# 資料庫連接 URL
DATABASE_URL=postgresql://rakazo_app:YOUR_PASSWORD@127.0.0.1:5432/rakazo
DATABASE_MIGRATION_URL=postgresql://rakazo_owner:YOUR_PASSWORD@127.0.0.1:5432/rakazo
```

#### 4.1.2 身份驗證與加密

```env
# Better Auth 簽名金鑰（獨立隨機長字串）
BETTER_AUTH_SECRET=<64 位元以上的隨機字串>

# 內容加密金鑰（64 位元十六進位字串）
ENCRYPTION_KEY=<64 位元以上的隨機字串>

# 螢幕代理程式金鑰（獨立隨機長字串）
SCREEN_PROXY_SECRET=<32 位元以上的隨機字串>
```

#### 4.1.3 沙盒控制

```env
# Docker 沙盒監理令牌（Docker 沙盒也需要獨立隨機字串）
SANDBOX_SUPERVISOR_TOKEN=<32 位元以上的隨機字串>

# Docker Desktop 開發模式
SANDBOX_CONTROL_VIA_LOOPBACK=true
DOCKER_HOST=<可選>
DOCKER_SOCKET=<可選>
```

### 4.2 可選環境變數

#### 4.2.1 AI 模型提供者

```env
# OpenRouter API 金鑰
OPENROUTER_API_KEY=<您的 OpenRouter API 金鑰>

# 其他提供者金鑰（直接傳遞給 API 和 Worker）
OPENAI_API_KEY=<OpenAI API 金鑰>
GEMINI_API_KEY=<Google Gemini API 金鑰>
MISTRAL_API_KEY=<Mistral API 金鑰>
GROQ_API_KEY=<Groq API 金鑰>
XAI_API_KEY=<xAI API 金鑰>
ANTHROPIC_API_KEY=<Anthropic API 金鑰>
```

#### 4.2.2 整合服務

```env
# Composio API 金鑰（用於應用程式整合）
COMPOSIO_API_KEY=<您的 Composio API 金鑰>

# Pipedream Connect（需三個變數）
PIPEDREAM_CLIENT_ID=<Client ID>
PIPEDREAM_CLIENT_SECRET=<Client Secret>
PIPEDREAM_PROJECT_ID=<Project ID>
```

#### 4.2.3 本地模型

```env
# 本地模型列表（如 Ollama、LM Studio、llama.cpp）
RAKAZO_LOCAL_MODELS=qwen3:4b,llama3.1:8b,qwen3-vl
RAKAZO_LOCAL_MODELS_URL=http://127.0.0.1:11434/v1
RAKAZO_LOCAL_CONTEXT_WINDOW=32768
RAKAZO_LOCAL_MAX_TOKENS=4096
RAKAZO_LOCAL_VISION_MODELS=qwen3-vl
```

#### 4.2.4 電腦沙盒提供者

```env
# 沙盒提供者（預設 docker）
SANDBOX_PROVIDER=docker  # 或 e2b / novita / daytona / createos / boat

# E2B 提供者
SANDBOX_PROVIDER=e2b
E2B_API_KEY=<您的 E2B API 金鑰>

# Daytona 提供者
SANDBOX_PROVIDER=daytona
DAYTONA_API_KEY=<您的 Daytona API 金鑰>

# CreateOS 提供者
SANDBOX_PROVIDER=createos
CREATEOS_API_KEY=<您的 CreateOS API 金鑰>

# Boat 提供者
SANDBOX_PROVIDER=boat
BOAT_API_KEY=<您的 Boat API 金鑰>
```

### 4.3 公開伺服器設定

```env
# 公開主機域名
RAKAZO_HOST=app.example.com

# Better Auth 公開 URL
BETTER_AUTH_URL=https://app.example.com

# Web 公開來源
WEB_ORIGIN=https://app.example.com

# API 公開 URL
API_URL=https://app.example.com

# 公開端口
WEB_PORT=5173
API_PORT=3100
```

## 5. API 端點與功能

### 5.1 oRPC API 合約

Rakazo 使用 oRPC（OpenRPC）作為 API 協議。主要端點包括：

```typescript
export const appContract = {
  // 健康檢查
  health: oc.output(z.object({ 
    ok: z.literal(true), 
    version: z.string() 
  })),
  
  // 使用者資訊
  me: oc.output(MeSchema),
  
  // 部署設定
  deployment: {
    get: oc.output(DeploymentSettingsSchema),
    update: oc.input(z.object({
      signupsEnabled: z.boolean().optional(),
      signupAllowlist: z.array(z.string()).optional(),
      computerHost: z.enum(["docker", "this-mac"]).nullable().optional(),
    }))
    .output(DeploymentSettingsSchema),
  },
  
  // 模型管理
  models: {
    list: oc.output(z.array(z.object({
      provider: z.string(),
      providerName: z.string()
    }))),
  },
  // ... 更多端點
}
```

### 5.2 主要功能端點

| 端點 | 說明 |
|------|------|
| `/api/health` | 健康檢查 |
| `/api/me` | 取得當前使用者資訊 |
| `/api/deployment` | 部署設定管理 |
| `/api/models` | 模型提供者列表 |
| `/api/bots` | 機器人管理 |
| `/api/computers` | 電腦資源管理 |
| `/api/integrations` | 應用程式整合 |
| `/api/mcp` | Model Context Protocol 端點 |
| `/api/media` | 媒體生成（圖片、影片） |
| `/api/voice` | 語音合成 |
| `/api/search` | 網路搜尋工具 |

### 5.3 Webhook 端點

| 端點 | 說明 |
|------|------|
| `/api/billing-webhook` | 計費 webhook |
| `/api/messaging-webhook` | 訊息接收 webhook |
| `/api/github-webhook` | GitHub webhook |

## 6. 測試步驟

### 6.1 快速啟動測試

#### 步驟 1：驗證環境

```bash
# 檢查 Docker 版本（需要 26+）
docker --version

# 檢查 Compose 外掛程式
docker compose version

# 檢查 OpenSSL
openssl version
```

#### 步驟 2：下載並執行安裝腳本

```bash
mkdir -p rakazo-test && cd rakazo-test
curl -fsSLO https://raw.githubusercontent.com/elie222/rakazo/main/infra/compose/install-images.sh
bash install-images.sh
```

#### 步驟 3：驗證服務啟動

```bash
# 查看所有容器狀態
docker compose ps

# 預期輸出應包含：
# - api
# - worker
# - web
# - postgres
# - sandbox-supervisor
```

#### 步驟 4：測試 Web 介面

```bash
# 開啟瀏覽器訪問
http://127.0.0.1:5173

# 執行以下測試：
# 1. 頁面應正常載入
# 2. 點擊 "Sign up" 建立新帳戶
# 3. 完成身份驗證後，應能看到 "Models" 設定
# 4. 點擊 "Add provider" 並輸入 OpenRouter API 金鑰測試模型連接
```

#### 步驟 5：測試 API 健康檢查

```bash
# 使用 curl 測試 API 端點
curl http://127.0.0.1:5173/api/health

# 預期回應
# {
#   "ok": true,
#   "version": "<版本号>"
# }
```

### 6.2 本地開發測試

#### 步驟 1：複製原始碼並設定環境

```bash
git clone https://github.com/elie222/rakazo.git
cd rakazo
cp .env.example .env

# 生成必要的安全密鑰
POSTGRES_PASSWORD=$(openssl rand -hex 16)
POSTGRES_APP_PASSWORD=$(openssl rand -hex 16)
BETTER_AUTH_SECRET=$(openssl rand -hex 32)
ENCRYPTION_KEY=$(openssl rand -hex 64)
SCREEN_PROXY_SECRET=$(openssl rand -hex 32)
SANDBOX_SUPERVISOR_TOKEN=$(openssl rand -hex 32)
```

#### 步驟 2：修改 .env 檔案

```bash
# 將上述變數加入 .env 檔案
# 設定 OPENROUTER_API_KEY 或保持空白以使用預設
echo "OPENROUTER_API_KEY=your-key" >> .env
```

#### 步驟 3：安裝依賴並建立影像

```bash
pnpm install
pnpm sandbox:build
```

#### 步驟 4：啟動開發環境

```bash
pnpm dev
```

#### 步驟 5：驗證服務

```bash
# 查看啟動的 URL（預設 http://127.0.0.1:5173 或 http://localhost:5173）
# 兩種 loopback 主機都被信任

# 開啟瀏覽器並執行測試：
# 1. 註冊新帳戶
# 2. 連接模型提供者
# 3. 建立測試機器人
# 4. 與機器人對話
```

#### 步驟 6：測試 Electron 桌面應用程式

```bash
# 在開發環境仍運行的情況下啟動桌面 App
pnpm --filter @rakazo/desktop dev

# 在 App 中選擇 "Existing instance" 並輸入開發環境 URL
```

### 6.3 功能測試

#### 測試 1：機器人基本功能

```bash
# 1. 建立測試機器人
# 2. 傳送測試訊息
# 3. 驗證機器人回覆（包含對話歷史、記憶）
# 4. 驗證語音模式（如有設定語音提供者）
```

#### 測試 2：電腦工具功能

```bash
# 1. 開啟機器人 "Agent computer"
# 2. 測試瀏覽器存取
# 3. 測試終端機存取
# 4. 測試檔案存取
# 5. 測試圖形桌面存取（Mac 環境）
```

#### 測試 3：模型提供者

```bash
# 1. 在 "Settings → Models" 中切換不同提供者
# 2. 測試 OpenRouter 預設模型（openai/gpt-6-luna）
# 3. 測試自帶模型（如 OpenAI、Anthropic 等）
# 4. 測試本地模型（如 Ollama）
# 5. 測試 OpenAI 相容端點
```

#### 測試 4：整合功能

```bash
# 1. 設定 Composio API 金鑰測試應用程式整合
# 2. 設定 Pipedream Connect 測試自定義整合
# 3. 測試 MCP 伺服器連接
# 4. 測試 Treg 使用量計費
```

#### 測試 5：媒體生成

```bash
# 1. 設定 MEDIA_GENERATION_PROVIDER=fal
# 2. 使用 generate_image 工具生成圖片
# 3. 使用 generate_video 工具生成影片
# 4. 驗證輸出符合格式要求（PNG 圖片、MP4 影片）
```

#### 測試 6：語音功能

```bash
# 1. Mac 環境：使用 macOS 內建聲音
# 2. 自帶提供者：設定 ElevenLabs、OpenAI、Cartesia 或 Fish Audio
# 3. 測試語音合成和語音識別
# 4. 測試呼叫機器人功能
```

### 6.4 沙盒提供者測試

#### Docker 沙盒（預設）

```bash
# 驗證 Docker 沙盒監理服務
docker compose ps | grep sandbox

# 建立測試電腦並驗證
# 1. 在機器人中選擇 "Agent computer"
# 2. 執行測試指令
# 3. 驗證電腦容器是否正確建立和執行
```

#### E2B 沙盒

```bash
# 設定 E2B API 金鑰
SANDBOX_PROVIDER=e2b
E2B_API_KEY=<您的 E2B API 金鑰>

# 驗證 E2B 電腦執行
docker compose down
docker compose up -d
```

#### Daytona 沙盒

```bash
# 設定 Daytona API 金鑰
SANDBOX_PROVIDER=daytona
DAYTONA_API_KEY=<您的 Daytona API 金鑰>

# 驗證 Daytona 電腦執行
docker compose up -d
```

### 6.5 資料庫測試

#### 執行資料庫遷移

```bash
# 從 Compose 執行
docker compose exec postgres psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "SELECT 1;"

# 從原始碼檢查出執行
pnpm db:migrate
```

#### 驗證資料庫結構

```bash
# 連接資料庫
docker compose -f infra/compose/docker-compose.yml exec postgres psql -U "$POSTGRES_USER" -d "$POSTGRES_DB"

# 執行查詢
\dt                    # 列出所有資料表
\d bots                # 查看 bots 資料表結構
\d conversations       # 查看 conversations 資料表結構
```

### 6.6 安全性測試

#### 測試 1：憑證加密

```bash
# 1. 在機器人中輸入測試內容
# 2. 驗證資料庫中內容是否加密儲存
# 3. 檢查 .env 檔案是否包含密鑰（不應有實際憑證）
```

#### 測試 2：權限控制

```bash
# 1. 建立多個使用者帳戶
# 2. 驗證每個使用者只能存取自己的資料
# 3. 測試權限升級和降級功能
```

#### 測試 3：網路隔離

```bash
# 1. 驗證 PostgreSQL 未公開到外部網路
# 2. 驗證沙盒監理服務僅在內部網路
# 3. 測試 Docker 容器間網路隔離
```

### 6.7 效能測試

#### 測試 1：記憶體使用

```bash
# 監控 API 服務記憶體
docker stats

# 預期：API 服務應在合理範圍內（< 512MB）
```

#### 測試 2：回應時間

```bash
# 測試 API 回應時間
curl -w "@curl-format" -o /dev/null -s "http://127.0.0.1:5173/api/health"

# 預期：健康檢查回應時間 < 1 秒
```

#### 測試 3：並行請求

```bash
# 測試並行請求處理
for i in {1..10}; do
  curl "http://127.0.0.1:5173/api/health" &
done
wait
```

### 6.8 錯誤診斷

```bash
# 生成診斷報告
docker compose -f infra/compose/docker-compose.yml exec api node dist/cli/diagnostics.js

# 診斷報告包含：
# - 版本資訊
# - 功能開關狀態
# - 遷移狀態
# - 各機器人 MCP 伺服器健康狀態
# - 最新執行記錄
```

### 6.9 日誌與監控

```bash
# 查看 API 日誌
docker compose logs -f api

# 查看 Worker 日誌
docker compose logs -f worker

# 查看 Web 日誌
docker compose logs -f web

# 查看資料庫日誌
docker compose logs -f postgres

# 查看所有容器日誌
docker compose logs -f
```

## 7. 最佳實踐與注意事項

### 7.1 安全性最佳實踐

1. **永遠不要將 `.env` 檔案提交到 Git**
2. **定期更新 API 金鑰**
3. **使用強密碼（至少 32 位元隨機字串）**
4. **為公開伺服器啟用 HTTPS**
5. **限制沙盒容器的資源使用**
6. **定期備份資料庫**

### 7.2 效能最佳化

1. **使用本地模型減少 API 成本**
2. **配置合理的上下文窗口大小**
3. **啟用快取功能（prompt cache）**
4. **使用適當的沙盒提供者**
5. **監控資源使用並調整配置**

### 7.3 維護建議

1. **定期檢查依賴項更新（`.github/workflows/weekly-dependencies.yml`）**
2. **監控錯誤報告和日誌**
3. **定期執行資料庫備份**
4. **更新 Docker 影像標籤（從 `edge` 切換到穩定版本）**

## 8. 常見問題解決方案

### 8.1 Node.js 版本不支援

**問題**：`pnpm` 提示 Node.js 版本不支援

**解決方案**：
```bash
# 檢查當前版本
node --version

# 安裝支援的版本（22.22.2+ 或 24.x 或 26+）
# Ubuntu/Debian:
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt-get install -y nodejs

# macOS:
brew install node@22
```

### 8.2 Docker 沙盒啟動失敗

**問題**：沙盒容器啟動失敗

**解決方案**：
```bash
# 檢查 Docker 版本
docker --version  # 需要 26+

# 重新建立電腦影像
pnpm sandbox:build

# 如果問題持續，重新啟動容器
docker compose restart
```

### 8.3 資料庫連接失敗

**問題**：`ECONNREFUSED` 錯誤

**解決方案**：
```bash
# 檢查 PostgreSQL 狀態
docker compose ps | grep postgres

# 如果未運行，啟動它
docker compose up -d postgres

# 檢查端口是否被佔用
lsof -i :5432
```

### 8.4 模型連接失敗

**問題**：模型提供者連接失敗

**解決方案**：
```bash
# 1. 驗證 API 金鑰是否有效
# 2. 檢查網路連線
curl https://api.openrouter.com/v1/models

# 3. 或重新設定模型
# 在 Web 介面中重新連接模型提供者
```

### 8.5 受限網路環境

**問題**：無法從 GitHub 下載檔案

**解決方案**：
參閱 [受限網路/鏡像下載指南](https://github.com/elie222/rakazo/blob/main/docs/self-host-restricted-network.md)

```bash
# 設定鏡像下載
RAKAZO_DOWNLOAD_BASE=https://your-mirror.example.com
RAKAZO_DOWNLOAD_SKIP_EXISTING=1

bash install-images.sh
```

## 9. 故障排除與支援

### 9.1 問題回報

遇到問題時，請附上診斷報告：

```bash
docker compose -f docker-compose.images.yml exec api node dist/cli/diagnostics.js
```

並提交到 [自託管問題頁面](https://github.com/elie222/rakazo/issues/new?template=self-host.yml)

### 9.2 社群資源

- **Discord**: [加入社群](https://discord.gg/RWwKa2Sn7h)
- **GitHub Issues**: [問題追蹤](https://github.com/elie222/rakazo/issues)
- **官方文件**: [Rakazo 文件](https://rakazo.com/docs/)
- **官方博客**: [Rakazo Blog](https://rakazo.com/blog/)

## 10. 參考文獻

- [Rakazo GitHub 原始碼](https://github.com/elie222/rakazo)
- [自託管指南](https://github.com/elie222/rakazo/blob/main/docs/self-host.md)
- [配置指南](https://github.com/elie222/rakazo/blob/main/docs/self-host-configuration.md)
- [模型設定](https://github.com/elie222/rakazo/blob/main/docs/self-host-models.md)
- [整合指南](https://github.com/elie222/rakazo/blob/main/docs/self-host-integrations.md)
- [電腦提供者](https://github.com/elie222/rakazo/blob/main/docs/self-host-sandbox-providers.md)
- [生產部署](https://github.com/elie222/rakazo/blob/main/docs/self-host-production.md)
- [備份與還原](https://github.com/elie222/rakazo/blob/main/docs/self-host-backups.md)
- [升級指南](https://github.com/elie222/rakazo/blob/main/docs/self-host-upgrading.md)
- [日誌與監控](https://github.com/elie222/rakazo/blob/main/docs/self-host-observability.md)
- [審計日誌](https://github.com/elie222/rakazo/blob/main/docs/self-host-audit-log.md)
- [應用程式與客戶](https://github.com/elie222/rakazo/blob/main/docs/self-host-clients.md)
- [計費設定](https://github.com/elie222/rakazo/blob/main/docs/self-host-billing.md)

---

**報告編寫日期**：2026 年 11 月 03 日  
**Rakazo 版本**：Beta（最新版）  
**作者**：AI 技術報告生成系統
