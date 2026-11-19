## 2026-11-19

```
Date:       11/19/2026, 1:46:56 PM
Models:     llama.cpp/unsloth/Qwen3.5-9B
Messages:   1 user, 11 assistant, 10 tool results, 1 compactions
Tool Calls: 10
Tokens:     ↑53k ↓5.1k R141k
Cost:       0.000
```

> [!NOTE]
> 根據 "https://github.com/garrytan/gbrain" 內容，用繁體中文（台灣技術用詞）撰寫一篇技術報告，含 step-by-step 安裝、測試、驗證步驟，存成 "js/gbrain/gbrain.new.md" .

## GBrain 技術報告

> **GBrain** 是一個為 AI 代理（Agent）設計的統一知識庫，讓您的團隊所有 Agent 能共享同一個「大腦」。將您的筆記、公司文檔、決策記錄和會議轉錄集中管理，Claude Code、Codex 和其他 AI 代理在回答前都會先查閱這些知識，避免從零開始，而是基於您和團隊實際撰寫的內容進行工作。

### 一、專案概述

GBrain 採用 MIT 授權，支援自行架設，初始時無需 API Key（使用關鍵字搜尋），可選添加入工智搜尋能力。

#### 核心功能

| 功能 | 說明 |
|------|------|
| 知識庫 | 集中管理個人筆記、公司文檔、決策記錄、會議轉錄 |
| 記憶持久化 | Agent 的記憶和事實跨會話持久化，所有連接到知識庫的 Agent 都能存取 |
| 語意搜尋 | 支援語意檢索、查詢擴充、自動事實擷取 |
| 知識圖譜 | 可選的有向無環圖（DAG），支援關聯查詢 |
| 多代理支援 | 支援 Claude Code、Codex、OpenClaw、Hermes、Cursor、ChatGPT 等多種 Agent |

#### 搜尋模式（Search Mode）

GBrain 提供三種搜尋模式，影響檢索的語料量：

| 模式 | 語料量（Token） | 分塊數 | 適用場景 |
|------|---------------|--------|----------|
| conservative | 4K | 10 | Haiku 類 Agent、成本敏感環境、高頻率循環 |
| balanced | 12K | 25 | 一般使用，帶有重排序 |
| tokenmax | 無限 | 50 | 推薦搭配聊天 Key 使用，最寬的檢索 |

**成本估算（每月 10K 查詢，輸入成本）：**

```
                  Haiku 5.5     Sonnet 5.5    Opus 5.5
                  ($0.10/M in)  ($2/M in)     ($4/M in)
  conservative    $4/mo         $80/mo        $160/mo
  balanced        $10/mo        $200/mo       $400/mo
  tokenmax        $20/mo        $400/mo       $800/mo
```

### 二、安裝步驟

#### 2.1 前置條件

```bash
## 檢查是否已安裝 Bun
bun --version
```

GBrain 需要 **Bun 1.4.4 或更高版本**。如果版本過舊，先執行：

```bash
bun upgrade
```

**注意：Bun 安裝器需要 `unzip`**

檢查是否安裝：

```bash
command -v unzip
```

如果沒有輸出，需要先安裝：

```bash
## Debian/Ubuntu
sudo apt-get update && sudo apt-get install -y unzip

## Fedora/RHEL
sudo dnf install -y unzip

## Alpine
sudo apk add unzip
```

#### 2.2 安裝 GBrain CLI

**重要警告：GBrain 不在 npm 上分發！**

npm 上的 `gbrain` 套件是無關的，可能遮蔽真正的二進制檔案。**永遠不要**執行：

```bash
npm install -g gbrain      # ❌ 錯誤！
bun add -g gbrain          # ❌ 錯誤！
```

**正確的安裝方式：**

```bash
## 安裝 Bun（如果尚未安裝）
curl -fsSL https://bun.sh/install | bash
export PATH="$HOME/.bun/bin:$PATH"

## 安裝 GBrain CLI（穩定通道）
bun install -g github:garrytan/gbrain#stable
```

**驗證安裝：**

```bash
gbrain --version
```

如果找不到 `gbrain`，需要重新載入 shell 或在 shell profile 中加入 PATH：

```bash
echo 'export PATH="$HOME/.bun/bin:$PATH"' >> ~/.profile
export PATH="$HOME/.bun/bin:$PATH"
bash -lc 'gbrain --version'
```

### 三、建立知識庫（Brain）

#### 3.1 為現有 Agent 添加記憶

對於 **Claude Code** 或 **Codex**，使用以下命令：

```bash
## 預先檢查（不寫入任何檔案）
gbrain setup claude-code --dry-run --json

## 正式建立並連線
gbrain setup claude-code --json
```

這會執行以下操作：

1. 如果不存在知識庫，自動執行 `gbrain init --pglite --no-embedding`
2. 建立 MCP 註冊
3. 建立讀取上下文 hook
4. 進行煙霧測試
5. 在 `~/.claude/CLAUDE.md` 或 Codex 的 `AGENTS.md` 中寫入 brain-first block

**對於其他 Agent（如 Hermes、Grok Build、opencode）：**

```bash
## Hermes
printf 'Y\n' | hermes mcp add gbrain --env GBRAIN_HOME=$HOME --connect-timeout 60 --command $(which gbrain) --args serve --surface starter --advertise verbs

## Grok Build
grok mcp add gbrain -e "GBRAIN_HOME=$HOME" -- "$(command -v gbrain)" serve --surface starter --advertise verbs

## opencode
opencode mcp add gbrain --env GBRAIN_HOME=$HOME -- "$(command -v gbrain)" serve --surface starter --advertise verbs
```

#### 3.2 獨立 CLI 模式（無需 Agent）

```bash
## 初始化知識庫（PGLite 引擎，無嵌入）
gbrain init --pglite --no-embedding

## 驗證健康狀態
gbrain doctor --json
```

#### 3.3 資料庫選項

GBrain 支援多種資料庫引擎，依優先順序自動選擇：

| 順序 | 引擎 | 條件 |
|------|------|------|
| 1 | 現有 Postgres | 設定 `GBRAIN_DATABASE_URL` |
| 2 | Supabase | 發現現有的 Supabase 專案 |
| 3 | 本地 Postgres | 設定環境變數或 `--local-postgres` |
| 4 | Docker Postgres | 使用 `gbrain-postgres` 容器 |
| 5 | PGLite | 預設嵌入式方案（終端回退） |

**使用 Postgres 優先：**

```bash
gbrain init --prefer-postgres [--allow-docker] [--allow-create-db] [--local-postgres] [--json]
```

### 四、配置 API Key（可選）

GBrain 的關鍵字搜尋無需 API Key。但如果要啟用語意檢索、自動事實擷取等進階功能，需要配置 API Key。

#### 4.1 預設嵌入服務器（Voyage）

```bash
export VOYAGE_API_KEY=pa-...
```

預設使用 `voyage-4`（嵌入，1024 維）和 `rerank-3-lite`（重排序），一個 Key 即可。

#### 4.2 替代方案（OpenAI）

```bash
export OPENAI_API_KEY=sk-...
```

用於向量搜尋、自動事實擷取和聊天模型。

#### 4.3 Anthropic

```bash
export ANTHROPIC_API_KEY=sk-ant-...
```

用於自動事實擷取、聊天模型和查詢擴充。

#### 4.4 儲存位置

API Key 可以儲存在：

1. **環境變數**（推薦）：`export VOYAGE_API_KEY=pa-...`
2. **配置檔案**：`~/.gbrain/config.json`
3. **Daemon 環境**：`~/.gbrain/env`（Autopilot daemon 使用）

**設定 API Key：**

```bash
export VOYAGE_API_KEY=pa-...
gbrain config set voyage_api_key $VOYAGE_API_KEY
```

### 五、匯入和索引

#### 5.1 匯入 Markdown 檔案

```bash
gbrain import ~/my-knowledge --no-embed
```

#### 5.2 建立知識圖譜（可選）

如果已經有知識庫倉儲，可以建立有向無環圖（DAG）連結：

```bash
## 預覽
gbrain extract links --source db --dry-run | head -20

## 正式執行
gbrain extract links --source db
gbrain extract timeline --source db

## 驗證
gbrain stats
```

#### 5.3 匯入公司知識庫

```bash
## 個人筆記
gbrain sources add notes --path ~/notes --federated --force

## 公司文檔
gbrain sources add company --path ~/company --federated --force

## 同步
gbrain sync --all
```

### 六、測試和驗證

#### 6.1 基本驗證

```bash
## 完整的安裝合約檢查
gbrain bootstrap verify

## 詳細的健康檢查
gbrain doctor --json

## 檢查配置的模型
gbrain models

## 模型探針測試
gbrain models doctor
```

#### 6.2 記憶測試

**測試 remember/recall 往返：**

```bash
## 記住一個事實
gbrain remember "GBrain 是一個知識庫系統" --entity "gbrain" --content-origin user_said --provenance "測試"

## 查詢該事實
gbrain recall "GBrain 是一個知識庫系統" --json

## 遺忘該事實
gbrain forget_fact "GBrain 是一個知識庫系統"
```

**關鍵字搜尋測試：**

```bash
## 關鍵字搜尋
gbrain search "GBrain 知識庫" --json

## 語意查詢（需要 API Key）
gbrain query "GBrain 的主要功能是什麼？" --json
```

#### 6.3 完整性檢查

```bash
## 檢查嵌入狀態
gbrain embed --status

## 檢查資料來源
gbrain sources list --json

## 檢查知識圖譜
gbrain graph-query "gbrain" --depth 2

## 查看統計資訊
gbrain stats --json
```

#### 6.4 上線檢查（Onboard）

```bash
## 檢查知識庫健康狀況
gbrain onboard --check --json

## 自動修復（需要設定 $MAX_USD 限制）
gbrain onboard --auto --max-usd 5
```

### 七、常見使用範例

#### 7.1 記憶查詢

```bash
## 記住新事實
gbrain remember "我們決定採用 Vue 3 作為前端框架" --entity "tech-decisions"

## 查詢決策
gbrain query "前端框架選型" --json

## 查詢特定實體
gbrain entity "tech-decisions"
```

#### 7.2 語意搜尋

```bash
## 關鍵字搜尋
gbrain search "Vue 3 框架"

## 語意查詢
gbrain query "什麼是我們選用的前端技術？"

## 詳細查詢
gbrain query "技術選型" --explain-target "tech-decisions"
```

#### 7.3 時間軸查詢

```bash
## 查看特定實體的時間軸
gbrain timeline "tech-decisions"

## 列出特定類型的頁面
gbrain list --type "meeting"

## 查看反向連結
gbrain backlinks "tech-decisions"
```

#### 7.4 實體查詢

```bash
## 查詢特定人員
gbrain entity "alice"

## 查詢特定公司
gbrain entity "acme-corp"
```

### 八、維護和升級

#### 8.1 自動維護（Autopilot）

**安裝 Autopilot daemon：**

```bash
gbrain autopilot --install --repo ~/brain
```

**檢查狀態：**

```bash
gbrain autopilot --status
```

**手動維護命令：**

```bash
## 即時同步
gbrain sync --watch

## 更新嵌入（僅針對過期的）
gbrain embed --stale

## 完整性檢查
gbrain doctor --json

## 更新嵌入
gbrain embed --stale
```

#### 8.2 升級

**記憶體-only 升級：**

```bash
GBRAIN_NO_AUTOPILOT_INSTALL=1 GBRAIN_NO_REEMBED=1 gbrain upgrade --no-autopilot-install
```

**完整升級（包含服務和提供者）：**

```bash
gbrain upgrade
```

**升級驗證：**

```bash
## 檢查版本
gbrain --version

## 健康檢查
gbrain doctor --json

## 驗證關鍵字查詢
gbrain search "測試關鍵字"
```

#### 8.3 問題修復

**PGLite 啟動失敗：**

```bash
## 自動修復
gbrain pglite-repair --dry-run
gbrain pglite-repair --yes

## 重建
gbrain reinit-pglite

## 切換到 Postgres
gbrain migrate --to postgres
```

**資料庫存取問題：**

```bash
## 檢查狀態
gbrain engine status --json --probe

## 修復
gbrain db-repair --yes --apply-rewrites
```

### 九、最佳實踐

#### 9.1 資料組織

```
brain/
├── people/          # 人員資料
├── companies/       # 公司資料
├── concepts/        # 概念知識
├── decisions/       # 決策記錄
├── meetings/        # 會議轉錄
└── notes/           # 個人筆記
```

#### 9.2 定期維護

| 任務 | 頻率 | 命令 |
|------|------|------|
| 健康檢查 | 每週 | `gbrain doctor --json` |
| 更新嵌入 | 每週 | `gbrain embed --stale` |
| 完整性掃描 | 每週 | `gbrain onboard --check --json` |
| 自動修復 | 每日 | `gbrain autopilot --status` |

#### 9.3 備份建議

```bash
## 匯出資料（非完整資料庫備份）
gbrain export --path ~/gbrain-backup/

## 完整備份建議使用 git 倉儲
```

### 十、故障排除

#### 10.1 常見錯誤

**錯誤：`schema_version: 0`**

```bash
## 套用移轉
gbrain apply-migrations --yes --no-autopilot-install

## 如果仍然失敗
gbrain doctor --json
```

**錯誤：`unzip is required to install bun`**

```bash
## 安裝 unzip
sudo apt-get install -y unzip  # 或對應的套件管理器

## 重新安裝 Bun
curl -fsSL https://bun.sh/install | bash
```

**錯誤：`RuntimeError: Aborted()` (PGLite 啟動失敗)**

```bash
## 自動修復
gbrain pglite-repair --yes

## 如果仍然失敗，重建
gbrain reinit-pglite
```

#### 10.2 查詢無結果

```bash
## 檢查索引狀態
gbrain doctor --only search_index

## 檢查搜尋模式
gbrain search modes

## 重新建立索引
gbrain embed --stale --force
```

### 十一、參考資源

- [GBrain 官方文件](https://github.com/garrytan/gbrain)
- [安裝指南](https://github.com/garrytan/gbrain/blob/master/docs/INSTALL.md)
- [Agent 安裝指南](https://github.com/garrytan/gbrain/blob/master/INSTALL_FOR_AGENTS.md)
- [驗證指南](https://github.com/garrytan/gbrain/blob/master/docs/GBRAIN_VERIFY.md)
- [搜尋模式指南](https://github.com/garrytan/gbrain/blob/master/docs/guides/search-modes.md)

### 十二、總結

GBrain 是一個強大的知識庫系統，為 AI 代理提供：

1. **統一知識來源**：所有 Agent 共享同一個知識庫
2. **持久化記憶**：跨會話保持記憶
3. **語意理解**：支援語意檢索和查詢擴充
4. **知識圖譜**：可選的有向無環圖連結
5. **多代理支援**：支援主流 AI 代理平台

**快速開始：**

```bash
## 安裝
bun install -g github:garrytan/gbrain#stable

## 建立知識庫
gbrain init --pglite --no-embedding

## 連線 Agent
gbrain setup claude-code

## 匯入知識
gbrain import ~/notes

## 驗證
gbrain doctor --json
```

GBrain 的強項在於讓 AI 代理不僅僅是「聊天」，而是基於您團隊實際撰寫的知識進行工作，實現真正的知識共享和記憶持久化。
