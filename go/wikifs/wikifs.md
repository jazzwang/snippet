# KiwiFS 技術報告

**生成日期：** 2026-11-24

KiwiFS 是一套專為 AI 代理（agents）和團隊設計的 Markdown 知識文件系統。它將 Markdown 文件轉化為可搜索、可版本控制、結構化的知識庫，提供單一二進制文件、零配置的部署體驗。

## 1. 專案簡介

KiwiFS 的核心理念是：**文件是單一的真實來源（single source of truth）**。所有文檔都是純 Markdown 文件，搜索索引、向量索引、元數據表都可以從文件重新構建。

### 主要特性

| 特性 | 說明 |
|------|------|
| **62+ MCP 工具** | 與 Claude、Cursor 等 AI 代理原生命整合 |
| **內嵌 Web UI** | 區塊編輯器、維基連結、知識圖譜，內嵌於二進制中 |
| **全文 + 向量搜尋** | BM25 透過 SQLite FTS5，向量可插拔（OpenAI、Ollama、ONNX、Qdrant 等） |
| **Git 版本控制** | 每個寫入都是原子的 Git 提交，支援 blame、diff、時點還原 |
| **DQL 查詢** | SQL-like 查詢 frontmatter 元數據 |
| **6 種訪問協議** | REST、MCP、NFS、S3、WebDAV、FUSE |
| **19 種資料匯入器** | Postgres、MySQL、MongoDB、Notion、CSV、Obsidian 等 |
| **內容健康檢查** | 過期頁面、斷裂連結、孤兒頁面、矛盾偵測 |
| **多空間（Multi-space）** | 單一伺服器支援多個隔離的工作區 |
| **Webhook** | 支援 Slack、CI 或自定義 URL，HMAC 簽名，重試退避 |

## 2. 系統架構

```
┌──────────────────────────────────────────────────────────┐
│  KiwiFS                                    單一 Go 二進制 │
│                                                          │
│  ┌────────────────────────────────────────────────────┐  │
│  │  Web UI (內嵌 via go:embed)                        │  │
│  │  shadcn/ui · BlockNote · CodeMirror · Sigma.js     │  │
│  └────────────────────┬───────────────────────────────┘  │
│                       │                                  │
│  ┌────────────────────▼───────────────────────────────┐  │
│  │  訪問協議：REST :3333 · MCP · NFS :2049 · S3 :3334 │  │
│  │  · WebDAV :3335 · FUSE                             │  │
│  └────────────────────┬───────────────────────────────┘  │
│                       │                                  │
│  ┌────────────────────▼───────────────────────────────┐  │
│  │  核心功能                                          │  │
│  │  儲存 · Git 版本控制 · FTS5 + 向量搜尋              │  │
│  │  監看器 (fsnotify) · SSE 事件 · Schema/驗證         │  │
│  └────────────────────┬───────────────────────────────┘  │
│                       │                                  │
│  ┌────────────────────▼───────────────────────────────┐  │
│  │  檔案系統：local · NFS · EFS · JuiceFS · FUSE-S3   │  │
│  └────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
```

## 3. 安裝步驟

### 3.1 系統需求

- **Go 版本：** 1.27 或更高
- **作業系統：** Linux、macOS、Windows
- **記憶體：** 建議至少 512MB RAM（向量搜尋需要更多）

### 3.2 方法一：使用 Homebrew（macOS / Linux）

```bash
brew install kiwifs/tap/kiwifs
```

### 3.3 方法二：使用安裝腳本

```bash
curl -fsSL https://raw.githubusercontent.com/kiwifs/kiwifs/main/install.sh | sh
```

### 3.4 方法三：使用 Go install

```bash
go install github.com/kiwifs/kiwifs@latest
```

### 3.5 方法四：使用 Docker

```bash
docker pull ameliaanhlam/kiwifs
```

### 3.6 方法五：從原始碼編譯

```bash
git clone https://github.com/kiwifs/kiwifs.git
cd kiwifs
go build -o kiwifs .
```

### 3.7 編譯 ONNX 離線版本

如需完全離線的向量搜尋功能，可編譯內建 ONNX 模型：

```bash
kiwifs model download all-minilm-l6-v2
go build -tags onnx -o kiwifs .
```

## 4. 初始化工作區

### 4.1 基本初始化

```bash
kiwifs init --template knowledge --root ./knowledge
```

### 4.2 選擇模板

```bash
# 管理型知識庫
kiwifs init --template kb --root ./docs-kb

# 團隊維基
kiwifs init --template wiki --root ./team-wiki

# 代理episodic記憶
kiwifs init --template memory --root ./agent-memory

# 任務追蹤 + Kanban
kiwifs init --template tasks --root ./project

# 資料收集 + DQL 儀表板
kiwifs init --template data --root ./analytics

# 內容管理系統
kiwifs init --template cms --root ./blog

# 運維 Runbooks
kiwifs init --template runbook --root ./ops

# 架構決策記錄 (ADR)
kiwifs init --template adr --root ./decisions

# Prompt 庫 + 評估
kiwifs init --template prompt --root ./prompts

# 研究 + 引用
kiwifs init --template research --root ./research

# 追加式事件記錄
kiwifs init --template log --root ./audit
```

### 4.3 工作區結構

```
knowledge/
├── SCHEMA.md                 # 結構與 frontmatter 慣例
├── index.md                  # 自動維護的目錄
├── log.md                    # 追加式時間軸記錄
├── pages/                    # 持久化知識頁
├── episodes/                 # 每會話的 episodic 筆記
├── .git/                     # Git 倉庫（審計日誌、版本控制）
│   ├── objects/              # 不可變內容可尋址儲存
│   ├── refs/                 # 分支指標
│   └── logs/                 # Reflog
└── .kiwi/                    # KiwiFS 系統目錄
    ├── config.toml           # 伺服器與搜尋設定
    ├── playbook.md           # 代理可讀的操作指南
    ├── server.lock           # 單一實例 flock
    ├── state/
    │   └── search.db         # SQLite: FTS5 + 元數據 + 向量索引
    ├── comments/             # 內聯註解（JSON）
    └── templates/            # 頁面模板
```

## 5. 啟動伺服器

### 5.1 基本啟動

```bash
kiwifs serve --root ./knowledge
```

預設端口：3333

### 5.2 自定義配置

```bash
kiwifs serve --root ./knowledge --port 4000 --search sqlite --versioning git
```

### 5.3 配置檔案（.kiwi/config.toml）

```toml
[server]
port = 3333
host = "0.0.0.0"
public_url = "https://wiki.mycompany.com"  # 啟用永久連結

[storage]
root = "/data/knowledge"

[search]
engine = "sqlite"  # grep | sqlite

[search.vector]
enabled = true
worker_count = 1

[search.vector.embedder]
provider = "ollama"      # openai | ollama | cohere | bedrock | vertex | http
model = "nomic-embed-text"
timeout = "120s"

[search.vector.store]
provider = "sqlite-vec"  # sqlite-vec | qdrant | pgvector | pinecone | weaviate | milvus

# 完全離線 ONNX 替代方案（需要編譯 -tags onnx）：
# [search.vector.embedder]
# type = "onnx"
# model_path = "~/.kiwi/models/multilingual-e5-small/onnx/model.onnx"
# dimensions = 384

[versioning]
strategy = "git"  # git | cow | none

[auth]
type = "none"     # none | apikey | perspace | oidc

[trash]
enabled        = true
retention_days = 30
```

## 6. 測試步驟

### 6.1 健康檢查測試

```bash
curl -X GET http://localhost:3333/health
# 預期回應：{"status":"ok"}
```

### 6.2 檔案操作測試

```bash
# 取得目錄樹
curl -X GET http://localhost:3333/api/kiwi/tree

# 取得單一檔案
curl -X GET http://localhost:3333/api/kiwi/file?path=index.md

# 寫入新檔案（使用 X-Actor 標頭指定 Git 作者）
curl -X PUT 'http://localhost:3333/api/kiwi/file?path=pages/test.md' \
  -H "X-Actor: test-agent" \
  -d "# Test Page\n\nThis is a test."

# 批量寫入（單一提交）
curl -X POST 'http://localhost:3333/api/kiwi/bulk' \
  -H "Content-Type: application/json" \
  -d '{
    "files": [
      {"path": "pages/auth.md", "content": "# Authentication\n\nOAuth2 + JWT..."},
      {"path": "pages/payments.md", "content": "# Payments\n\n..."},
      {"path": "log.md", "content": "- 2026-05-21: Updated auth and payments"}
    ],
    "actor": "agent:exec_abc",
    "message": "run #249: updated auth and payments"
  }'
```

### 6.3 搜尋功能測試

```bash
# 全文搜尋（BM25）
curl -X GET "http://localhost:3333/api/kiwi/search?q=authentication"

# 向量搜尋
curl -X POST http://localhost:3333/api/kiwi/search/semantic \
  -H "Content-Type: application/json" \
  -d '{"query": "how to authenticate"}'

# 信任權重搜尋
curl -X GET http://localhost:3333/api/kiwi/search/verified

# Recall（融合檢索：keyword + vector + graph）
curl -X POST http://localhost:3333/api/kiwi/recall \
  -H "Content-Type: application/json" \
  -d '{
    "query": "how did we handle the auth migration?",
    "limit": 10,
    "rrf_k": 60
  }'
```

### 6.4 維基連結測試

```bash
# 取得回鍊（哪些頁面連結到當前頁面）
curl -X GET http://localhost:3333/api/kiwi/backlinks?path=pages/auth.md

# 解析維基連結 [[wiki-links]] 為永久連結
curl -X POST http://localhost:3333/api/kiwi/resolve-links \
  -H "Content-Type: application/json" \
  -d '{"path": "pages/test.md"}'
```

### 6.5 版本控制測試

```bash
# 取得檔案的版本歷史
curl -X GET "http://localhost:3333/api/kiwi/versions?path=pages/test.md"

# 取得特定版本的內容
curl -X GET "http://localhost:3333/api/kiwi/version?path=pages/test.md&version=abc123"

# 取得差異
curl -X GET "http://localhost:3333/api/kiwi/diff?path=pages/test.md&from=abc123&to=def456"

# 取得行級歸因（blame）
curl -X GET "http://localhost:3333/api/kiwi/blame?path=pages/test.md"
```

### 6.6 元數據查詢測試（DQL）

```bash
# 基本查詢
curl -X GET "http://localhost:3333/api/kiwi/query?q=TABLE title, status FROM \"pages\" WHERE priority = \"high\""

# 分組統計
curl -X GET "http://localhost:3333/api/kiwi/query/aggregate?group_by=status&calc=count,avg:priority"

# 結構化查詢
curl -X GET "http://localhost:3333/api/kiwi/meta?where=\$.status=published&where=\$.priority=high&sort=\$.updated&order=desc"
```

### 6.7 垃圾回收（Trash）測試

```bash
# 取得垃圾桶清單
curl -X GET http://localhost:3333/api/kiwi/trash

# 還原檔案
curl -X POST http://localhost:3333/api/kiwi/trash/restore \
  -H "Content-Type: application/json" \
  -d '{"restore_id": "20261113T101530Z_notes-a.md"}'

# 永久刪除
curl -X DELETE http://localhost:3333/api/kiwi/trash/:id
```

### 6.8 分享連結測試

```bash
# 建立分享連結
curl -X POST http://localhost:3333/api/kiwi/share \
  -H "Content-Type: application/json" \
  -d '{"path": "reports/q2-review.md"}'

# 取得分享連結清單
curl -X GET http://localhost:3333/api/kiwi/share

# 撤銷分享連結
curl -X DELETE http://localhost:3333/api/kiwi/share/:id
```

### 6.9 內容健康檢查

```bash
# 取得內容健康儀表板
curl -X GET http://localhost:3333/api/kiwi/analytics

# 取得最熱門頁面
curl -X GET "http://localhost:3333/api/kiwi/analytics/views?top=10"

# 取得搜尋失敗記錄
curl -X GET "http://localhost:3333/api/kiwi/analytics/failed-searches?top=10"

# 取得過期頁面
curl -X GET http://localhost:3333/api/kiwi/stale

# 取得矛盾內容
curl -X GET http://localhost:3333/api/kiwi/contradictions

# 執行內容健康掃描
curl -X GET http://localhost:3333/api/kiwi/janitor
```

### 6.10 外部連結檢查

```bash
# 啟用外部連結檢查
# 在 .kiwi/config.toml 中設定：
# [janitor]
# external_link_check = true
# external_link_timeout = "5s"
# external_link_ignore = ["localhost", "example.com"]

# 取得外部連結檢查報告
curl -X GET "http://localhost:3333/api/kiwi/janitor?fresh=true"
```

## 7. 驗證步驟

### 7.1 驗證 Git 版本控制

```bash
# 檢查 Git 倉庫是否存在
ls -la ./knowledge/.git/

# 檢查最近提交
cd ./knowledge
git log --oneline -5

# 驗證作者歸因
git log --format="%H %an %ae" -1
```

### 7.2 驗證搜索索引

```bash
# 重新建立搜索索引
kiwifs reindex

# 檢查索引檔案
ls -la ./knowledge/.kiwi/state/search.db

# 驗證索引完整性
kiwifs check
```

### 7.3 驗證向量搜尋

```bash
# 如果使用的是 ONNX 模型，驗證模型路徑
# 在 .kiwi/config.toml 中確認 model_path 正確指向

# 執行向量搜尋測試
curl -X POST http://localhost:3333/api/kiwi/search/semantic \
  -H "Content-Type: application/json" \
  -d '{"query": "test query"}'
```

### 7.4 驗證 MCP 整合

```bash
# 配置本地 MCP 客戶端（如 Cursor、Claude Desktop）
{
  "mcpServers": {
    "kiwifs": {
      "command": "kiwifs",
      "args": ["mcp", "--root", "/path/to/knowledge"]
    }
  }
}

# 驗證 MCP 工具可呼叫
# 在 MCP 客戶端中測試 kiwi_search、kiwi_write 等工具
```

### 7.5 驗證 Web UI

```bash
# 開啟瀏覽器訪問
open http://localhost:3333   # macOS
# 或
xdg-open http://localhost:3333  # Linux
# 或
start http://localhost:3333     # Windows

# 驗證以下功能：
# - 區塊編輯器（Block editor）
# - 維基連結（[[wiki-links]]）
# - 回鍊（Backlinks）
# - 知識圖譜（Knowledge graph）
# - 黑暗模式（Dark mode）
```

### 7.6 驗證多空間（Multi-space）

```bash
# 建立多個工作區
kiwifs init --template knowledge --root ./workspace1
kiwifs init --template knowledge --root ./workspace2

# 啟動多空間伺服器（透過 REST API 路徑前綴區分）
kiwifs serve --root ./workspace1 --root ./workspace2

# 訪問不同空間
curl -X GET http://localhost:3333/workspace1/api/kiwi/tree
curl -X GET http://localhost:3333/workspace2/api/kiwi/tree
```

### 7.7 驗證資料匯入

```bash
# 從 Markdown 匯入
kiwifs import --from markdown --path ./docs --root ./knowledge

# 從 Postgres 匯入
kiwifs import --from postgres --dsn "postgres://user:pass@localhost/db" --table users --root ./knowledge

# 從 CSV 匯入
kiwifs import --from csv --path data.csv --root ./knowledge

# 乾跑測試（不實際匯入）
kiwifs import --from csv --path data.csv --root ./knowledge --dry-run
```

### 7.8 驗證資料匯出

```bash
# 匯出為 JSONL
kiwifs export --format jsonl --output knowledge.jsonl

# 匯出為 CSV（包含向量嵌入）
kiwifs export --format csv --include-embeddings --output dataset.csv

# 匯出為 Parquet（包含內容）
kiwifs export --format parquet --include-content --output knowledge.parquet

# 匯出為 PDF
kiwifs export --format pdf --path docs/report.md --output report.pdf

# 匯出為 HTML
kiwifs export --format html --path concepts/ --self-contained --output site.html

# 匯出為 Slides（Marp）
kiwifs export --format slides --path talks/intro.md --output slides.html

# 匯出為 MkDocs
kiwifs export --format mkdocs --path docs/ --site-name "My Wiki" --output docs-project/
```

### 7.9 驗證工作流（Workflow）

```bash
# 建立工作流
cat > .kiwi/workflows/review.json << 'EOF'
{
  "name": "review",
  "states": ["draft", "review", "approved", "published"],
  "transitions": {
    "draft": ["review"],
    "review": ["approved", "draft"],
    "approved": ["published"]
  }
}
EOF

# 推進頁面狀態
curl -X POST 'http://localhost:3333/api/kiwi/workflow/advance' \
  -H 'Content-Type: application/json' \
  -d '{"path":"pages/report.md","target_state":"review","actor":"agent:reviewer"}'
```

### 7.10 驗證 Schema 驗證

```bash
# 在 .kiwi/config.toml 中設定 schema
# 寫入不符合 schema 的檔案應該被拒絕
curl -X PUT 'http://localhost:3333/api/kiwi/file?path=pages/test.md' \
  -H "X-Actor: test-agent" \
  -d "# Invalid\n\nMissing required fields."
# 預期：返回 422 錯誤
```

### 7.11 驗證 Webhook

```bash
# 配置 Webhook
# 在 .kiwi/config.toml 中：
# [webhooks]
# enabled = true
# urls = ["https://example.com/webhook"]
# headers = {"Authorization": "Bearer secret"}

# 寫入檔案並觀察 Webhook 是否被觸發
curl -X PUT 'http://localhost:3333/api/kiwi/file?path=pages/test.md' \
  -H "X-Actor: test-agent" \
  -d "# Test"
```

### 7.12 驗證 SSE 事件

```bash
# 開啟新終端機，監聽 SSE 事件
curl -X GET "http://localhost:3333/api/kiwi/events"

# 在另一個終端機寫入檔案
curl -X PUT 'http://localhost:3333/api/kiwi/file?path=pages/test.md' \
  -H "X-Actor: test-agent" \
  -d "# Test"

# 預期：事件流中應該出現 write 事件
```

## 8. 常見問題與排錯

### 8.1 端口已被佔用

```bash
# 查看占用端口的進程
lsof -i :3333
# 或
netstat -tlnp | grep 3333

# 殺進程
kill <PID>

# 或使用自定義端口
kiwifs serve --port 4000
```

### 8.2 向量搜尋失敗

```bash
# 檢查向量索引是否存在
ls -la ./knowledge/.kiwi/state/

# 重新建立索引
kiwifs reindex

# 如果是 ONNX 模型，檢查模型路徑
# 在 .kiwi/config.toml 中確認 model_path 正確
```

### 8.3 搜索無結果

```bash
# 檢查是否使用正確的搜索引擎
# 在 .kiwi/config.toml 中：
# [search]
# engine = "sqlite"  # 或 "grep"

# 重新建立索引
kiwifs reindex
```

### 8.4 Git 提交失敗

```bash
# 檢查 Git 是否安裝
which git

# 檢查 Git 配置
git config --list

# 在倉庫中檢查
cd ./knowledge
git status
git log -1
```

### 8.5 記憶體不足

```bash
# 檢查系統記憶體
free -h

# 增加 worker_count（減少記憶體使用）
# 在 .kiwi/config.toml 中：
# [search.vector]
# worker_count = 1
```

## 9. 最佳實踐

### 9.1 檔案命名慣例

- 使用 snake_case 命名頁面
- 使用日期前綴：`2026-06-21-authentication.md`
- 使用 slug 函數：`{{slug()}}`

### 9.2 Frontmatter 結構

```yaml
---
title: Authentication
status: published
priority: high
tags: [security, backend, oauth2]
scope: backend
confidence: 0.95
created: 2026-06-21
updated: 2026-11-24
---
```

### 9.3 維基連結使用

```markdown
- 使用 `[[page]]` 格式連結其他頁面
- 使用 `[[page#heading]]` 連結到特定標題
- 使用 `[[page]|label]` 自定義顯示文字
```

### 9.4 定期維護

```bash
# 定期執行 janitor（建議每天）
kiwifs janitor

# 定期重新建立索引
kiwifs reindex

# 定期清理垃圾桶
kiwifs check --trash
```

## 10. 參考資源

- [官方文件](https://docs.kiwifs.com)
- [API 參考](https://docs.kiwifs.com/api-reference)
- [範例](docs/EXAMPLES.md)
- [架構](docs/ARCHITECTURE.md)
- [FAQ](docs/FAQ.md)
- [Roadmap](docs/ROADMAP.md)

## 11. 授權

[Business Source License 1.1](LICENSE) - 可免費使用、自我託管、修改。唯一限制：不能提供 KiwiFS 作為商業託管服務。每個版本在 4 年後轉換為 Apache 2.0。

*本文檔生成於 2026-11-24*
