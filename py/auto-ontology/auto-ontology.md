# Auto Ontology 技術報告

**報告日期**: 2026-11-24  
**版本**: v1.0  
**專案**: [NVIDIA Auto Ontology](https://github.com/NVIDIA/auto-ontology)

## 1. 專案簡介

Auto Ontology 是 NVIDIA 開發的開放式語義圖庫（Ontology Library），自動從企業元數據中建立、協調並暴露語義圖，支援任何 Agent 架構透過 MCP、CLI 和 API 獲取語義上下文。

### 核心功能

- **發現 (Discover)**: 從元數據自動生成企業級語義圖，連接現有語義模型和語義圖，建立 AI 準備就緒的知識圖譜
- **接地 (Ground)**: 為 Agent 提供受信任的業務概念定義，協調跨系統的不一致定義
- **驗證 (Validate)**: 在專家正式認證前，使用真實問題測試草稿，檢查生成的查詢
- **暴露 (Expose)**: 透過 MCP、CLI 和 API 向任何 Agent 架構提供語義上下文
- **學習 (Learn)**: 將認證的修正和實際使用回饋到語義圖中，使共享上下文隨使用而改進

### 優勢

Auto Ontology 在 [BIRD-Interact](https://bird-interact.github.io/) 和 [BEAVER](https://beaverbench.github.io/#leaderboard) 基準測試中排名第一，測試文字轉 SQL 分析問題回答在互動流程中的準確性。

## 2. 系統需求

### 基本需求

- **Docker** (包含 Compose v2)
- **uv** (Python 包管理器)
- **NVIDIA API Key** (`nvapi-...`)，從 [build.nvidia.com](https://build.nvidia.com) 取得
- **PostgreSQL** 17 + **pgvector**

### 選用需求

- **HashiCorp Vault** (用於儲存連接憑證)
- **KumoRFM API** (用於預測分析)

## 3. 安裝步驟

### Step 1: 克隆儲存庫並初始化環境

```bash
# 克隆儲存庫
git clone https://github.com/NVIDIA/auto-ontology.git
cd auto-ontology

# 建立 .env 檔案並設定環境變數
cp .env.example .env
```

### Step 2: 設定環境變數

在 `.env` 檔案中設定以下必要變數：

```bash
# 必要變數
DEFAULT_MODELS_API_KEY=nvapi-...                    # NVIDIA API 金鑰
AUTH_SECRET=<長隨機字串，例如: openssl rand -base64 32>
APP_URL=http://localhost:3000
POSTGRES_PASSWORD=<新密碼>
CONNECTION_STRINGS=postgresql://postgres:<相同密碼>@postgres:5432/wideworldimporters
AUTO_ONTOLOGY_ADMIN_PASSWORD=<新密碼>
PGADMIN_PASSWORD=<新密碼>
AUTO_ONTOLOGY_ADMIN_EMAIL=admin@example.com

# 選用變數（若不使用可刪除）
# DEFAULT_MODELS_REASONING=nvidia/nemotron-3.5-lightning-30b-a3b
# DEFAULT_MODELS_NON_REASONING=nvidia/nemotron-3.5-lightning-30b-a3b
# DEFAULT_MODELS_EMBED=nvidia/nemotron-3.5-embed-1b
# DEFAULT_MODELS_RERANK=nvidia/nemotron-3.5-rerank-8b
```

### Step 3: 啟動 Postgres 並載入樣本資料庫

```bash
# 啟動 Postgres
docker compose up -d --wait postgres

# 克隆樣本評估資料庫
git clone https://github.com/NVIDIA/auto-ontology-eval.git ../auto-ontology-eval

# 載入 Wide World Importers 資料庫
cd ../auto-ontology-eval
uv sync
cp .env.example .env
POSTGRES_PASSWORD='<上述相同密碼>' uv run python scripts/seed/seed_wwi.py --database-name wideworldimporters --drop
```

### Step 4: 建立並啟動完整堆疊

```bash
# 回到主目錄
cd ..

# 構建並啟動所有服務
docker compose up -d --build
```

### Step 5: 驗證安裝

```bash
# 檢查服務狀態
docker compose ps

# 應該看到以下服務運行：
# - postgres              # Postgres 資料庫
# - app                   # 後端 API 服務 (port 3001)
# - ingestion             # 語義圖收錄服務 (port 3002)
# - web                   # Web 應用程式 (port 3000)
# - pgadmin               # 資料庫管理介面
```

## 4. 測試步驟

### Step 1: 登入 Web 介面

開啟瀏覽器訪問 `http://localhost:3000`，使用以下憑證登入：

- **Email**: `AUTO_ONTOLOGY_ADMIN_EMAIL` (從 `.env` 取得)
- **密碼**: `AUTO_ONTOLOGY_ADMIN_PASSWORD` (從 `.env` 取得)

### Step 2: 啟用語義編譯

1. 進入 **Settings → Semantic Compilation**
2. 開關啟用 **Semantic Compilation**
3. 系統將自動開始語義圖編譯，完成後顯示 "Semantic compilation is ready"

### Step 3: 查看語義圖

1. 進入 **Catalog** 頁面
2. 探索已生成的語義圖
3. 驗證以下元素：
   - Terms (術語)
   - Mapped Columns (映射欄位)
   - SQL Attributes (SQL 屬性)
   - Relationships (關係)

### Step 4: 透過 Chat 進行測試

在 **Chat** 頁面測試問題回答功能：

```
問題：What was revenue for the USB food flash drive - sushi roll in Pennsylvania in June 2015?
```

**預期輸出**:

```
Answer:  Revenue for USB food flash drive - sushi roll in Pennsylvania in
          June 2015 was $588.80, from 3 invoice lines.

SQL:     SELECT SUM(il.extendedprice) AS revenue, COUNT(*) AS invoice_lines
          FROM sales.invoicelines il
          JOIN sales.invoices i             ON il.invoiceid = i.invoiceid
          JOIN warehouse.stockitems si      ON il.stockitemid = si.stockitemid
          JOIN sales.customers c            ON i.customerid = c.customerid
          JOIN application.cities ct        ON c.deliverycityid = ct.cityid
          JOIN application.stateprovinces sp ON ct.stateprovinceid = sp.stateprovinceid
          WHERE si.stockitemname = 'USB food flash drive - sushi roll'
            AND sp.stateprovincename = 'Pennsylvania'
            AND i.invoicedate >= '2015-06-01' AND i.invoicedate < '2015-07-01'

Steps:   Resolved terms: Invoice Line (revenue), Stock Item, State Province, Invoice
          Joined: invoice line -> invoice -> customer -> city -> state province
          Validated the filter values against the data, then executed
```

## 5. 驗證步驟

### Step 1: 驗證 MCP 連接

測試 MCP Server 功能：

```bash
# 啟動 MCP Server
AUTO_ONTOLOGY_API_URL=http://localhost:3000 \
  uvx --from "git+https://github.com/NVIDIA/auto-ontology.git#subdirectory=mcp" auto-ontology-mcp
```

### Step 2: 測試 MCP 工具

在 Cursor 或 Claude Desktop 中配置 MCP：

**Cursor** (`~/.cursor/mcp.json`):
```json
{
  "mcpServers": {
    "auto-ontology": {
      "url": "http://localhost:3003/mcp"
    }
  }
}
```

**Claude Desktop** (`claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "auto-ontology": {
      "command": "npx",
      "args": ["mcp-remote", "http://localhost:3003/mcp"]
    }
  }
}
```

### Step 3: 測試 REST API

```bash
# 取得 API Token
# 登入後點擊用戶選單 → API Tokens → Create Token

# 測試查詢
curl -N http://localhost:3000/api/chat/completions \
  -H "x-api-key: $AUTO_ONTOLOGY_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"question": "How many orders shipped last week?"}'
```

### Step 4: 驗證回答正確性

測試無法回答的問題，確認系統能正確識別數據缺口：

```
問題：What was return on ad spend for the sushi roll flash drive in June 2015?
```

**預期行為**: 系統應提示 "no term covers 'ad spend'" 並詢問用戶是否要使用其他數據。

### Step 5: 驗證 Ossie 兼容性

測試語義圖的進出功能：

```bash
# 導出為 Ossie YAML
curl -X POST http://localhost:3000/api/model/export \
  -H "x-api-key: $AUTO_ONTOLOGY_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'

# 導入 Ossie YAML
curl -X POST http://localhost:3000/api/model/import \
  -H "x-api-key: $AUTO_ONTOLOGY_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"file": "path/to/ossie.yaml"}'
```

## 6. 架構概覽

### 系統組成

```mermaid
flowchart LR
  subgraph clients["客戶端"]
    ui["瀏覽器: Web UI (port 3000)"]
    rest["腳本: REST API"]
    mcpc["MCP 客戶端: Cursor, Claude Desktop"]
  end
  
  subgraph services["服務"]
    mcp["MCP Server (port 3003)"]
    fe["Web App, 驗證, API Gateway (port 3000)"]
    be["後端: Text-to-SQL Agent, Catalog, Ontology APIs (port 3001)"]
    ing["收錄和語義編譯服務 (port 3002)"]
  end
  
  subgraph data["數據層"]
    pg[("Postgres + pgvector: 應用程式數據，目錄，語義圖，向量儲存")]
    src[("來源資料庫: 10 個連接器")]
    vault["Vault (選用): 連接憑證儲存"]
  end
  
  subgraph models["模型端點"]
    models["NVIDIA NIM 或 OpenAI 相容端點"]
    kumo["KumoRFM (選用): 預測分析"]
  end

  ui --> fe
  rest --> fe
  mcpc --> mcp
  mcp --> fe
  fe --> be
  fe --> pg
  be --> ing
  ing --> pg
  be --> src
  ing --> src
  be --> models
  ing --> models
  be -.-> vault
  ing -.-> vault
  be -.-> kumo
```

### 模型角色

| 角色 | 預設模型 | 用途 |
|------|---------|------|
| `REASONING` | `nvidia/nemotron-3.5-lightning-30b-a3b` | 運行回答 Agent 和 `check_answerable`，構建語義圖，檢測 PII |
| `NON_REASONING` | `nvidia/nemotron-3.5-lightning-30b-a3b` | 重寫後續問題，規劃圖表，撰寫 PQL 用於預測 |
| `EMBED` | `nvidia/nemotron-3.5-embed-1b` | 在 pgvector 中建立索引，匹配問題 |
| `RERANK` | `nvidia/nemotron-3.5-rerank-8b` | 在編譯期間選擇橋接表 SQL 屬性 |

### 連接器支援

Auto Ontology 支援以下 10 個資料庫引擎：

- PostgreSQL
- MySQL
- Databricks
- Snowflake
- ClickHouse
- Trino
- Apache Kyuubi
- HeavyDB
- DuckDB
- SQLite

## 7. 常見問題排錯

### 問題 1: 瀏覽器左側導航未顯示

**症狀**: 重新啟動後，瀏覽器左側導航未顯示

**解決方案**: 清除 `localhost:3000` 的網站數據，重新登入

```bash
# Windows (PowerShell)
ie-sitesdata -clear localhost:3000

# macOS
open /Applications/Safari.app/Contents/Profiles/Default/Storage/Web\ Content
```

### 問題 2: 服務啟動失敗

**症狀**: `docker compose up` 失敗

**診斷**:
```bash
docker compose logs -f
```

**常見原因**:
- Port 衝突
- 記憶體不足
- NVIDIA API Key 無效

**解決方案**:
```bash
# 檢查端口佔用
netstat -ano | findstr :3000

# 停止所有容器並重新啟動
docker compose down
docker compose up -d --build
```

### 問題 3: 語義編譯失敗

**症狀**: "Semantic compilation" 無法完成

**診斷**:
```bash
# 檢查收錄服務日誌
docker compose logs ingestion
```

**常見原因**:
- 模型 API 限額
- 數據量過大
- 網絡問題

**解決方案**:
- 檢查 NVIDIA API 使用情況
- 增加 `uv` 的記憶體限制
- 檢查網絡連接

## 8. 參考文檔

| 主題 | 文檔 |
|------|------|
| Kubernetes 部署 (Helm) | [DEPLOYMENT.md](https://github.com/NVIDIA/auto-ontology/blob/main/DEPLOYMENT.md) |
| 架構和流程步驟 | [docs/architecture.md](https://github.com/NVIDIA/auto-ontology/blob/main/docs/architecture.md) |
| 連接器、範圍和 Vault | [docs/connections.md](https://github.com/NVIDIA/auto-ontology/blob/main/docs/connections.md) |
| 驗證、SSO 和 API Token | [docs/authentication.md](https://github.com/NVIDIA/auto-ontology/blob/main/docs/authentication.md) |
| 對話 API | [docs/conversation-api.md](https://github.com/NVIDIA/auto-ontology/blob/main/docs/conversation-api.md) |
| MCP Server | [docs/mcp.md](https://github.com/NVIDIA/auto-ontology/blob/main/docs/mcp.md) |
| REST API 規範 | [docs/openapi/auto-ontology-api.json](https://github.com/NVIDIA/auto-ontology/blob/main/docs/openapi/auto-ontology-api.json) |

## 9. 授權

Auto Ontology 採用 [Apache License, Version 2.0](https://github.com/NVIDIA/auto-ontology/blob/main/LICENSE) 授權。

- SPDX 標識符: `Apache-2.0`
- 第三方組件: 參閱 [THIRD_PARTY_NOTICES.md](https://github.com/NVIDIA/auto-ontology/blob/main/THIRD_PARTY_NOTICES.md)

**報告結束**
