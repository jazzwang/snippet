# ARTEX 技術報告

> **警告：本文檔僅供教育、研究與合法安全測試用途。使用本工具必須獲得明確授權，且僅針對自有系統、實驗室環境或授權漏洞賞格計劃的目標。**

---

## 系統概述

**ARTEX**（Autonomous Penetration Testing System）是一個基於大語言模型的多智能體自動滲透測試系統。該系統使用 Go 語言開發後端，內嵌 Next.js 前端，並搭配 PostgreSQL 數據庫，可自動化執行各種滲透測試工作流程。

### 核心架構

ARTEX 採用雙圖架構（Dual-Graph Architecture），包含：

- **資產圖（Asset Graph）**：全局共享的資產真相來源，包含根網域名稱、子網域、IP、服務、應用程式、端點等節點
- **探索圖（Exploration Graph）**：每項任務獨有的思考與推進過程，記錄目標、意圖、事實、漏洞發現及其線性關係

系統核心包括：
- **規劃器（Planner）**：單一意圖生成器，負責讀取探索圖狀況並分派意圖
- **工作節點（Worker）**：執行者，每個工作節點負責執行單一意圖
- **主智能體（Main Agent）**：支持人環（Human-in-the-loop）交互

---

## 系統需求

### 必要條件

- **Go 1.21+**（如使用本地構建方式）
- **PostgreSQL 14+** 數據庫
- **LLM API 金鑰**（Anthropic 或 OpenAI，也可在 UI 中配置）
- **Node.js 18+**（如使用 Docker 以外的方式）

### 可選條件

- Docker（使用 Docker 部署時需要）
- Docker Compose
- curl、wget 等網路工具

---

## 安裝步驟

### 方法一：一鍵安裝腳本（推薦）

```bash
git clone https://github.com/BaaRai/ARTEX.git
cd ARTEX
./install.sh
```

**安裝流程：**

1. 腳本自動檢測/安裝 Docker
2. 選擇部署模式：
   - **① 全 Docker 模式**：輸入 PostgreSQL 密碼（按 Enter 使用隨機密碼）→ 自動寫入 `.env` → `docker compose up -d --build`
   - **② 本地構建模式**：選擇數據庫（連接到現有數據庫或使用 Docker 啟動）→ 生成 `config.json` → 構建嵌入式單一二進制檔案

3. 安裝完成後，訪問 **http://localhost:8787**
   - 首次進入時，`/setup` 會要求設置管理員密碼
   - 後端啟動時會輸出一次性設置令牌（可通過 `docker compose logs artex | grep "Setup token"` 查看）

### 方法二：Docker Compose 手動部署

```bash
git clone https://github.com/BaaRai/ARTEX.git
cd ARTEX
cp .env.example .env

# 編輯 .env 文件，設置必要環境變數
# 必須設置：POSTGRES_PASSWORD
# 可選設置：ANTHROPIC_API_KEY 或 OPENAI_API_KEY

docker compose up -d --build
```

**注意：**
- 影像會在地本構建，無預發布影像可拉取
- 影像已包含常見工具（ripgrep、curl、vim、npm、nmap 等）
- `./skills` 和 `./data` 目錄透過綁定掛載持久化

### 方法三：下載預構建二進制檔案

```bash
# 從 Releases 頁面下載對應平台的 zip 檔案
# https://github.com/BaaRai/ARTEX/releases

# 解壓縮後：
unzip artex-*.zip

# 配置數據庫連接
cp config.example.json config.json
# 編輯 config.json，填入 PostgreSQL 連接資訊

# 啟動
./start.sh
# → http://localhost:8787
```

**注意：**
- 使用 `start.sh` / `start.bat` 而非直接運行 `./artex`
- 啟動腳本為守護進程腳本，進程崩潰時會自動重啟
- 背景運行：`nohup ./start.sh >artex.log 2>&1 &`

### 方法四：從原始碼構建單一二進制

```bash
# 1) 構建前端靜態檔案
cd web && npm ci && npm run build:static && cd ..

# 2) 複製到嵌入目錄
cp -r web/out server/webui/dist

# 3) 構建（僅需添加 -tags embedui 參數將前端嵌入）
CGO_ENABLED=0 go build -tags embedui -o artex ./cmd/artex

# 4) 啟動
./start.sh
```

### 方法五：構建跨平台發行版

```bash
# 構建所有目標平台並打包
./build.sh --release
# 輸出：dist/artex-0.3.3-*.zip

# 指定目標平台
ARTEX_TARGETS=linux/amd64,windows/amd64 ./build.sh --release

# 使用 UPX 壓縮（需確認目標環境相容）
./build.sh --target linux/amd64 --upx
```

---

## 測試步驟

### 1. 本地開發環境測試

```bash
./dev.sh
```

此腳本啟動：
- 後端 API（端口 8787）
- 流量記錄代理（端口 8788）
- 前端開發伺服器（端口 5173）

訪問 http://localhost:5173 進行測試。

### 2. 基本功能測試

訪問 UI 後，依序測試以下功能：

#### 2.1 系統設置
- 驗證管理員登入
- 檢查 LLM 配置頁面（可添加 Ollama 本地模型）
- 驗證系統設置（工作智能體數量預設為 3）

#### 2.2 資產同步（ScopeSentry）
- 輸入 ScopeSentry 地址和 API Key
- 選擇目標和資產類型進行同步
- 驗證資產同步到探索圖

#### 2.3 流量捕獲瀏覽器外掛
- 從 `extension/` 目錄載入 unpacked 外掛（Chrome/Edge 開發模式 → Load unpacked）
- 在彈出視窗設置 ARTEX URL 和 token
- 按 **Start capture** 開始捕獲
- 使用網站，請求/回應會批次上傳到 `POST /api/traffic/ingest`
- 按 **Stop** 停止捕獲

### 3. LLM 提供者測試

#### 3.1 配置 LLM 提供者

在 "LLM Configuration" 頁面或通過環境變數配置：

```bash
# Anthropic
export ANTHROPIC_API_KEY=sk-...

# OpenAI
export OPENAI_API_KEY=sk-...

# Ollama（本地模型）
export ARTEX_LLM_PROVIDER=ollama
export ARTEX_LLM_BASE_URL=http://127.0.0.1:11434/v1
```

#### 3.2 測試 LLM 連接

1. 訪問 LLM Configuration 頁面
2. 添加 Ollama 提供者（若使用本地模型）
3. 測試模型加載狀態

---

## 驗證步驟

### 1. 數據庫連接驗證

```sql
-- 連接 PostgreSQL 數據庫
psql -U artex -d artex

-- 檢查資產圖表
SELECT * FROM "assets" LIMIT 10;

-- 檢查探索圖表
SELECT * FROM "exploration_nodes" LIMIT 10;

-- 檢查公司範圍
SELECT * FROM "companies" LIMIT 10;
```

### 2. 後端 API 驗證

```bash
# 測試 API 端點
curl http://localhost:8787/api/health

# 測試 JWT 登入
curl -X POST http://localhost:8787/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"yourpassword"}'

# 測試活動流（SSE）
curl http://localhost:8787/api/activity \
  -H "Authorization: Bearer <your-token>" \
  --max-time 5
```

### 3. 前端靜態資源驗證

```bash
# 檢查前端靜態檔案是否存在
ls -la server/webui/dist/

# 訪問前端頁面
curl http://localhost:8787/
```

### 4. 功能完整性驗證清單

| 功能模組 | 驗證項目 | 預期結果 |
|---------|---------|---------|
| 登入/認證 | 登入成功、JWT 生成 | 返回有效的 JWT token |
| 儀表板 | 總覽、Token 使用、活動流 | 顯示系統資訊 |
| 任務列表 | 任務列表、狀態顯示 | 可查看所有任務 |
| 任務執行 | Sessions、Tool calls | 顯示執行細節 |
| 探索圖 | Graph 視圖 | 顯示探索節點與邊 |
| 資產圖 | 資產覆蓋圖 | 顯示資產與測試高亮 |
| 漏洞發現 | Findings 列表 | 顯示發現的漏洞 |
| 資產同步 | ScopeSentry 同步 | 成功導入資產 |
| 流量捕獲 | 外掛捕獲 | 成功記錄請求/回應 |
| 人環對話 | Chat 介面 | 可與智能體互動 |
| 攔截批準 | 工具批準閘門 | 需授權才能執行敏感操作 |
| 備份 | 數據庫備份 | 成功創建備份檔案 |

### 5. 安全驗證

```bash
# 檢查端口綁定（預設僅 127.0.0.1）
netstat -tlnp | grep 8787

# 驗證 SSL/TLS（如使用反向代理）
openssl s_client -connect your.domain.com:443 -servername your.domain.com

# 檢查 CORS 配置
curl -I http://localhost:8787/
```

### 6. 流量記錄代理驗證

```bash
# 檢查代理端口
curl http://localhost:8788/

# 驗證 CA 證書
ls -la ./data/ca.crt
```

---

## 配置參數

### 數據庫配置（config.json）

```json
{
  "database": {
    "host": "127.0.0.1",
    "port": 5432,
    "user": "artex",
    "password": "yourpass",
    "dbname": "artex",
    "sslmode": "disable"
  }
}
```

### 環境變數

| 變數名稱 | 說明 | 預設值 |
|---------|------|-------|
| `ARTEX_PG_DSN` | PostgreSQL 連接字串 | - |
| `ANTHROPIC_API_KEY` | Anthropic API 金鑰 | - |
| `OPENAI_API_KEY` | OpenAI API 金鑰 | - |
| `ARTEX_LLM_PROVIDER` | LLM 提供者 | - |
| `ARTEX_LLM_MODEL` | LLM 模型 | - |
| `ARTEX_LLM_BASE_URL` | LLM 基礎 URL | - |
| `ARTEX_TRUSTED_PROXIES` | 信任的代理 CIDR 列表 | - |
| `ARTEX_BIND_ADDR` | 綁定地址 | 127.0.0.1 |

### 反向代理部署（HTTPS）

```nginx
server {
    listen 443 ssl;
    server_name your.domain.com;
    # ssl_certificate / ssl_certificate_key ...

    location / {
        proxy_pass http://127.0.0.1:8787;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

        # SSE 必要設定：關閉緩衝、長超時
        proxy_buffering off;
        proxy_cache off;
        proxy_read_timeout 3600s;
        proxy_http_version 1.1;
        proxy_set_header Connection "";
    }
}
```

**注意：** 後端預設監聽 `127.0.0.1:8787`，Docker 容器在 `:8787` 發布到 `127.0.0.1`。

---

## 日誌與監控

### 日誌位置

- Docker 模式：`docker logs artex`
- 本地模式：查看 `./data/logs/` 或 `artex.log`

### 關鍵日誌訊息

```bash
# 查看設置令牌
docker compose logs artex | grep "Setup token"

# 查看後端日誌
docker compose logs --tail 100 artex

# 查看錯誤日誌
docker compose logs --tail 50 --filter "ERROR" artex
```

### 備份與還原

```bash
# 備份數據庫和數據目錄
scripts/backup.sh --with-data

# 僅備份數據庫（保留 7 個）
scripts/backup.sh --keep 7

# 還原備份
gunzip -c backups/artex-db-<timestamp>.sql.gz | docker compose exec -T postgres \
  psql -U "$POSTGRES_USER" -d "$POSTGRES_DB"
```

### 定期備份（Cron 範例）

```bash
# 添加到 /etc/crontab 或使用者 crontab
20 3 * * * cd /path/to/ARTEX && scripts/backup.sh --with-data >> backups/backup.log 2>&1
```

---

## 升級步驟

> **重要提示：** 升級僅替換程式，不觸碰數據：Postgres 卷 `pgdata`、`./data`（SQLite、任務檔案等）、`./keys`（jwt.key）均會保留。**無需手動數據庫遷移**。

### 升級前準備

```bash
# 備份重要數據
tar -czf backup-data-$(date +%Y%m%d).tar.gz ./data
docker compose exec -T postgres pg_dumpartex -U "$POSTGRES_USER" > backup-db-$(date +%Y%m%d).sql
```

### 方法一：一鍵更新腳本

```bash
cd ARTEX
./update.sh
```

### 方法二：Docker Compose 手動升級

```bash
cd ARTEX
git pull                    # 更新程式碼
docker compose build artex  # 重新構建影像
docker compose up -d artex  # 重啟容器（自動遷移架構）
docker image prune -f       # 清理舊影像（可選）
```

### 方法三：預構建二進制升級

```bash
# 停止舊進程
pkill -f "./start.sh"

# 下載新版本
cd /tmp && wget https://github.com/BaaRai/ARTEX/releases/download/vX.Y.Z/artex-*.zip
unzip artex-*.zip

# 替換檔案（保持 config.json 和 data/）
cp -r /tmp/ARTEX-*/skills ./
cp /tmp/ARTEX-*/artex ./

# 重啟
./start.sh
```

### 特殊情況處理：2026-10-23 前克隆的倉庫

```bash
git stash                 # 若有本地變更
git fetch origin
git reset --hard origin/main
git stash pop             # 恢復暫存
```

---

## 故障排除

### 常見問題

#### 問題 1：前端無法載入

```bash
# 重新構建前端
cd web && npm ci && npm run build:static && cd ..
cp -r web/out server/webui/dist
```

#### 問題 2：數據庫連接失敗

```bash
# 檢查數據庫狀態
docker compose ps

# 檢查 .env 配置
cat .env | grep POSTGRES

# 手動啟動數據庫測試
docker compose up postgres
```

#### 問題 3：LLM 無法連接

```bash
# 檢查 API 金鑰
echo $ANTHROPIC_API_KEY

# 測試 LLM 連接
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{"messages":[{"role":"user","content":"Hello"}],"model":"claude-3-5-sonnet-20240620"}'
```

#### 問題 4：反向代理緩存問題

```nginx
# 確認已關閉緩衝
proxy_buffering off;
proxy_cache off;

# 重新載入配置
nginx -s reload
```

---

## 安全注意事項

### ⚠️ 重要警告

1. **僅在授權環境使用**：僅針對自有系統、實驗室環境或授權漏洞賞格計劃的目標
2. **遵守法律法規**：使用本工具必須符合當地法律法規
3. **責任自負**：使用者須承擔所有法律責任和後果

### 禁止事項

- ❌ 未經授權掃描、探測、利用或攻擊任何網站或網路服務
- ❌ 超出計劃範圍測試或違反行為準則
- ❌ 用於非法入侵、數據竊取、勒索或破壞性活動
- ❌ 違反國家/地區法律法規

---

## 參考資料

- [ARTEX 官方倉庫](https://github.com/BaaRai/ARTEX)
- [ARTEX 原始倉庫](https://github.com/Autumn-27/ARTEX)
- [Microsoft 安全博客 - Storm-0940 使用 ARTEX 的供應鏈攻擊](https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/)
- [norma SDK](https://github.com/Autumn-27/norma)
- [Cairn 專案](https://github.com/oritera/Cairn)

---

## 開源許可

本專案採用 **GNU Affero General Public License v3.0 (AGPL-3.0)** 授權。

- 允許自由使用、修改和分發
- 衍生作品必須同樣開源並採用 AGPL-3.0
- 若通過網路向使用者提供修改後的版本，必須提供對應的完整原始碼

---

## 版本歷史

| 版本 | 日期 | 說明 |
|-----|------|------|
| 0.3.3 | 2026-10-23 | 歷史重新編寫，移除個人郵件 |
| 0.3.x | - | 雙圖架構、多智能體系統 |

---

*本文檔最後更新：$(date -Isecond)*
