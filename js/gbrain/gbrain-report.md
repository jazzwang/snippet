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

> **GBrain** 是一個為 AI 代理（Agent）設計的統一知識庫，讓您的團隊所有 Agent 能共享同一個「大腦」。將您的筆記、公司文檔、決策記錄和會議逐字稿集中管理，Claude Code、Codex 和其他 AI 代理在回答前都會先查閱這些知識，避免從零開始，而是基於您和團隊實際撰寫的內容進行工作。

### 一、專案概述

GBrain 採用 MIT 授權，支援自行架設，初始時無需 API Key（使用關鍵字搜尋），可選添加入工智搜尋能力。

#### 核心功能

| 功能 | 說明 |
|------|------|
| 知識庫 | 集中管理個人筆記、公司文檔、決策記錄、會議逐字稿 |
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
├── meetings/        # 會議逐字稿
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

## 2026-11-22

- 使用 Github Codespace 實測
- 參考 https://github.com/oven-sh/bun 的 README.md
```
# with install script (recommended)
curl -fsSL https://bun.com/install | bash

# on windows
powershell -c "irm bun.sh/install.ps1 | iex"

# with npm
npm install -g bun

# with Homebrew
brew tap oven-sh/bun
brew install bun

# with Docker
docker pull oven/bun
docker run --rm --init --ulimit memlock=-1:-1 oven/bun
```
- 這裡採用 install script 安裝 `bun`
```bash
Welcome to Ubuntu 24.04.5 LTS (GNU/Linux 6.8.0-1070-azure x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro
Last login: Tue Nov 17 00:00:31 2026 from ::1
@jazzwang ➜ /workspaces/codespaces-blank (main) $
@jazzwang ➜ /workspaces/codespaces-blank (main) $ curl -fsSL https://bun.com/install | bash
######################################################################## 100.0%
bun was installed successfully to ~/.bun/bin/bun

Added "~/.bun/bin" to $PATH in "~/.bashrc"

To get started, run:

  source /home/codespace/.bashrc
  bun --help
```

- 檢查是否已安裝 Bun

```bash
@jazzwang ➜ /workspaces/codespaces-blank (main) $ ## 檢查是否已安裝 Bun
@jazzwang ➜ /workspaces/codespaces-blank (main) $ bun --version
1.4.5
```

- 檢查是否安裝 `unzip`

```bash
@jazzwang ➜ /workspaces/codespaces-blank (main) $ command -v unzip
/usr/bin/unzip
```

- 安裝 GBrain CLI

```bash
@jazzwang ➜ /workspaces/codespaces-blank (main) $ bun install -g github:garrytan/gbrain#stable
```

- 驗證安裝

```bash
@jazzwang ➜ /workspaces/codespaces-blank (main) $ gbrain --version
gbrain 0.60.753.0
```

- 因為 gbrain 沒有支援 Pi Agent, 所以先不測試 `gbrain setup` 的整合
- Pi Agent 1.0 以後支援 MCP 了，理論上可以設定 MCP，這邊先列為 TODO
- 先從 「3.2 獨立 CLI 模式（無需 Agent）」開始
```bash
## 初始化知識庫（PGLite 引擎，無嵌入）
gbrain init --pglite --no-embedding

## 驗證健康狀態
gbrain doctor --json
```
```
@jazzwang ➜ /workspaces/codespaces-blank (main) $ gbrain init --pglite --no-embedding
[gbrain notice release_channel] This install now follows the stable channel: weekly releases promoted after testing. To get every release instead, run: gbrain config set self_upgrade.channel alpha
Setting up local brain with PGLite (no server needed)...
  --no-embedding: deferred setup — enable later with `gbrain init --force --embedding-model voyage:voyage-4 --embedding-dimensions 1024 --path /home/codespace/.gbrain/brain.pglite` (setting embedding_model through `gbrain config set` is refused by design)
  Setting up brain schema (v330)...
  v142: takes.embedding resized to vector(1024); existing take vectors cleared
  325 migration(s) applied
[init] Migrations: 14 recorded as not needed on a new brain; 5 setup migration(s) pending (0.11.0, 0.14.0, 0.22.4, 0.28.0, 0.53.0). Finish setup: gbrain apply-migrations --yes --no-autopilot-install
Fresh brain setup approves following the packaged memory skills: prose only, existing memory/discovery tools, no scripts, paid services, capture or editor grants.
[init] Content: /home/codespace/.gbrain/content/9e0ca848-da10-4798-86e8-0acbfd070f53/default (content_directory; ready). Optional: initialize Git explicitly; configure an off-host backup separately.
[init] Using schema pack: gbrain-base-v2 (override with --schema-pack <name>)

Search mode preference
──────────────────────
Three named modes. Cost depends on BOTH the mode AND your downstream model.
Pick the pairing intentionally.

Estimated downstream input cost of the retrieved payload @ 10K queries/mo:

                  Haiku 5.5     Sonnet 5.5    Opus 5.5
                  ($0.10/M in)  ($2/M in)     ($4/M in)
  conservative    $4/mo         $80/mo        $160/mo
  balanced        $10/mo        $200/mo       $400/mo
  tokenmax        $20/mo        $400/mo       $800/mo

  Assumed payload per query: conservative 4K, balanced 10K, tokenmax 20K tokens.
  Scales linearly: x10 for 100K queries/mo, /10 for 1K. 200x corner-to-corner spread.
  Embedding, reranking and query expansion are separate provider charges.

GBrain's semantic result caching is temporarily disabled; budget for fresh retrieval.
Downstream provider prompt caching may discount input charges; it does not skip
retrieval or downstream generation.

  1) conservative   4K-token cap, 10 results by default, no reranker.
                    Best for: Haiku subagents, cost-sensitive agents,
                    high-volume search loops, MCP servers w/ many users.

  2) balanced       12K-token cap, 25 results by default, reranked.
                    Best for: mixed workloads, a reranker without a chat key.

  3) tokenmax       no token cap, 50 results by default, reranked.
                    Best for: the widest retrieval, low-volume high-stakes work.

`gbrain query` does not expand by default in any mode; --expand forces it and --no-expand skips it. `gbrain config set search.expansion true` turns the default on for the brain in any mode (false turns it off; an explicit --expand or --no-expand still wins). `gbrain search` never expands. An expansion is one call to the configured chat model, a separate provider charge; keyless brains never expand.
Actual expansion needs configured embedding and expansion providers; cloud
expansion sends the query to the configured provider.

You can change this any time with: gbrain config set search.mode <mode>
Per-knob tuning + recommendation engine ships at: gbrain search tune

  Recommended: conservative  (No chat key (Anthropic/OpenAI/Google) and no ready reranker — conservative keeps a tight 4K budget; balanced's reranker could not run.)

Mode [conservative]:
Search mode set to: conservative


Brain ready at /home/codespace/.gbrain/brain.pglite
0 pages. Engine: PGLite (local Postgres).

--- GBrain Mod Status ---
Skills: 76 loaded (router: skills/RESOLVER.md)
GStack: not found (coding skills — see github.com/garrytan/gstack)
Retrieval reflex: on by default. More: `gbrain integrations` (policy skill), skills/soul-audit (identity).

Note [harness_wiring]: gbrain is not connected to an agent here, and this step is not a command the agent runs by itself; say so in the reply that reports the install, without waiting on it. Which agent app should get gbrain memory? The install guide has a one-line command for each. For Claude Code or Codex, run `gbrain setup claude-code` or `gbrain setup codex` (it registers serve behind gbrain's launcher, so the session directory's bunfig.toml and .env never load). For any other host, register `<absolute path to gbrain> serve --surface starter --advertise verbs` as a stdio MCP server in your agent host; the install section lists the exact command per harness (Claude Code, Codex, Grok Build, opencode, OpenClaw).
Note [first_run_decisions]: The brain is ready and these first-run settings are in effect as listed; none blocks memory. Relay them once, in the reply that reports the install, as the current settings and how to change them; do not hold the install open or end it waiting on an answer. When the user picks an option, run its command. Nothing paid turns on from these settings without a key the user supplied.
  Which search mode should this brain use? Estimated downstream input cost of the retrieved payload at 10K queries/month (Haiku 5.5 / Sonnet 5.5 / Opus 5.5): conservative $4 / $80 / $160, balanced $10 / $200 / $400, tokenmax $20 / $400 / $800 per month. (default: conservative)
    - conservative: conservative (applied) (run: gbrain config set search.mode conservative)
    - balanced: balanced (run: gbrain config set search.mode balanced)
    - tokenmax: tokenmax (run: gbrain config set search.mode tokenmax)
  Should agents save important facts the user states (preferences, decisions, commitments) automatically, with provenance? Saved facts are readable by agents connected to this brain; transient facts expire. Off any time with `gbrain config set memory.auto_writeback off`. (default: off)
    - salient: Save durable facts the user states directly (recommended) (run: gbrain config set memory.auto_writeback salient)
    - all: Every direct factual statement (more low-value facts, more extraction spend) (run: gbrain config set memory.auto_writeback all)
    - off: Save only what the user explicitly asks to remember (records the answer) (run: gbrain config set memory.auto_writeback off)
  Upkeep: free upkeep runs on its own while your agent's gbrain session is open. Nothing is deleted or paid for without you. Turn off: gbrain config set maintenance.auto false. Optional schedule: gbrain maintain --schedule. (default: on)
    - on: Keep free upkeep on (in effect now)
    - off: Turn free upkeep off (run: gbrain config set maintenance.auto false)
  Conversation archive: on. gbrain keeps one redacted page per conversation per day from your agent sessions (Claude Code, Codex, OpenClaw, Hermes, Grok) in the conversations source, written by the maintenance pass. Without an embedding key nothing leaves this machine. Turn off: gbrain transcripts archive off. (default: on)
    - on: Keep the conversation archive on (in effect now)
    - off: Turn the conversation archive off (run: gbrain transcripts archive off)

→ Do this next — give your agent memory (copy these three commands):
  gbrain setup claude-code --no-hooks --gbrain-bin /home/codespace/.bun/bin/gbrain
  gbrain remember "gbrain install check" --provenance install-check
  gbrain recall --query "gbrain install check"
Then ask your agent in a NEW session to recall "gbrain install check" — it remembers. Ask it to forget that fact afterwards.

Note: memories agents save are readable by every agent connected to
this brain; use visibility:"private" for local-only facts.
Other harnesses (Codex, OpenClaw): docs/protocol/MEMORY_VERBS_v1.md
If `claude` is not found: install Claude Code first, or use the per-harness blocks in that doc.

More: bulk-load notes `gbrain import <dir> --no-embed` · scale up `gbrain migrate --to postgres --plan` · health `gbrain doctor`
@jazzwang ➜ /workspaces/codespaces-blank (main) $
```
- 看起來有點小複雜，不過就我的理解，會需要用到 LLM 應該是為了生成 embedding 來做 vector search 才會需要花錢。
```bash
@jazzwang ➜ /workspaces/codespaces-blank (main) $
@jazzwang ➜ /workspaces/codespaces-blank (main) $ gbrain doctor --json | jq . | tee gbrain-doctor.json
```
```json
{
  "schema_version": 2,
  "status": "healthy",
  "health_score": 100,
  "brain_checks_score": 100,
  "category_scores": {
    "brain": 100,
    "skill": 100,
    "ops": 100,
    "meta": 100
  },
  "checks": [
    {
      "name": "resolver_health",
      "status": "ok",
      "message": "76 skills, all reachable",
      "elapsed_ms": 235,
      "category": "skill"
    },
    {
      "name": "retrieval_reflex_health",
      "status": "ok",
      "message": "pglite — serve IPC socket not present; enabled but NO resolve path exists right now: the IPC socket is only bound by a running `gbrain serve` (stdio or --http) — until one is up, hooks/reflex degrade to no_serve on this brain (host capability may still supply pointers; policy skill carries otherwise) — policy skill not installed; run `gbrain integrations install retrieval-reflex --target <host-repo>`",
      "severity": "info",
      "readiness_state": "not_applicable",
      "fix": {
        "consent": [
          "persistent_install"
        ],
        "actor": "user",
        "next": "report",
        "why": "For Claude Code or Codex, run `gbrain setup claude-code` or `gbrain setup codex` (it registers serve behind gbrain's launcher, so the session directory's bunfig.toml and .env never load). For any other host, register `<absolute path to gbrain> serve --surface starter --advertise verbs` as a stdio MCP server in your agent host; the install section lists the exact command per harness (Claude Code, Codex, Grok Build, opencode, OpenClaw).",
        "user_message": "Which agent app should get gbrain memory? The install guide has a one-line command for each.",
        "docs": "https://github.com/garrytan/gbrain/blob/v0.60.753.0/docs/protocol/MEMORY_VERBS_v1.md#install-the-4-command-quickstart",
        "requires_exclusive": false
      },
      "details": {
        "enabled": true,
        "engine": "pglite",
        "path": "pglite — serve IPC socket not present",
        "fired_recently": false,
        "last_fired": null,
        "policy_skill_installed": false
      },
      "elapsed_ms": 23,
      "category": "skill"
    },
    {
      "name": "volunteer_channels",
      "status": "ok",
      "message": "no push-context activity in 7 days — if a hook adapter is installed, confirm its registration landed and the harness session was RESTARTED (hooks snapshot at session start); a serve older than this build logs NOTHING for the hook lane — restart serve on the new build to activate the feedback loop",
      "details": {
        "window_days": 7,
        "channels": {}
      },
      "elapsed_ms": 23,
      "category": "skill"
    },
    {
      "name": "memory_verbs_usage",
      "status": "ok",
      "message": "no verb calls recorded yet (sidecar appears on first remember/recall/entity/synthesize/forget)",
      "elapsed_ms": 23,
      "category": "skill"
    },
    {
      "name": "skill_conformance",
      "status": "ok",
      "message": "76/76 skills pass",
      "elapsed_ms": 79,
      "category": "skill"
    },
    {
      "name": "skill_brain_first",
      "status": "ok",
      "message": "76 skill(s) compliant or exempt (note: 3 skill(s) have brain_first typo hints: data-loss-gate, brain-ingest-gate, company-brainify)",
      "elapsed_ms": 79,
      "category": "skill"
    },
    {
      "name": "skills_manifest_integrity",
      "status": "ok",
      "message": "239 bundled skill files match skills.lock.json",
      "elapsed_ms": 79,
      "category": "skill"
    },
    {
      "name": "skill_currency",
      "status": "ok",
      "message": "skill currency not applicable (running inside the gbrain repo)",
      "elapsed_ms": 79,
      "category": "skill"
    },
    {
      "name": "skill_preconditions",
      "status": "ok",
      "message": "2 skill precondition(s) wait for content: the brain has no pages yet, so skills that need a corpus stay idle until the first import or sync.",
      "severity": "info",
      "readiness_state": "not_applicable",
      "details": {
        "unmet": [
          "citation-graph-ingest: source — ingest a corpus first (gbrain sync / gbrain import), then re-run",
          "skill-autobench: dir:conversations/ — populate conversations/ (see the conversation-archive skill), then re-run"
        ]
      },
      "elapsed_ms": 79,
      "category": "skill"
    },
    {
      "name": "skill_health",
      "status": "ok",
      "message": "76 skill(s), 938 KB, 1068 gbrain invocation(s) (400 with undeclared subcommands, flags checked); no findings",
      "details": {
        "scope": "managed",
        "totals": {
          "skills": 76,
          "bytes": 960778,
          "invocations": 1068,
          "subcommands_unverified": 400,
          "drift": 0,
          "size": 0
        }
      },
      "elapsed_ms": 53,
      "category": "skill"
    },
    {
      "name": "memorable_relay_health",
      "status": "ok",
      "message": "memorable relay off (default)",
      "details": {
        "enabled": false,
        "out_of_band_settable": true,
        "reason": "disabled"
      },
      "elapsed_ms": 14,
      "category": "ops"
    },
    {
      "name": "memory_writeback",
      "status": "ok",
      "message": "ambient writeback off (default): Stop-hook turn capture is off, but the compaction harvest and SessionEnd transcripts still extract (installing the harness hooks opted into them; stop them: gbrain config set memory.auto_writeback off). Enable: gbrain config set memory.auto_writeback salient",
      "details": {
        "mode": "off",
        "mode_valid": true,
        "transient_ttl": "3d",
        "ttl_valid": true,
        "instruction_visibility": "world",
        "backstop_visibility": "private",
        "visibility_note": "world = readable by agents authorized on THIS brain, not the public internet",
        "audience": "personal",
        "audience_reasons": [
          "no shared declaration; 0 non-automation client(s) active in 30d, 0 people (0 member(s), 0 unbound client(s))"
        ],
        "nudge_shown": false,
        "capture_lanes": {
          "writeback": "retire",
          "compact": "extract",
          "session_end": "extract"
        },
        "counters_note": "local, append-only, loss-tolerant observability over the last 7d — never a source of truth",
        "cross_lane_duplicates_7d": 0,
        "near_duplicates_shadow_7d": 0,
        "corpus_source_holds": {
          "legacy_unstamped": 0,
          "unresolved": 0,
          "sessions": 0
        }
      },
      "elapsed_ms": 14,
      "category": "brain"
    },
    {
      "name": "connectors",
      "status": "ok",
      "message": "No chat connectors configured (optional).",
      "elapsed_ms": 16,
      "category": "ops"
    },
    {
      "name": "dream_paid_loop",
      "status": "ok",
      "message": "No dream key died 3+ times in 24h",
      "details": {
        "threshold": 3,
        "breaker_enabled": true,
        "inspected_keys": 0,
        "count_exact": true,
        "keys": []
      },
      "elapsed_ms": 16,
      "category": "ops"
    },
    {
      "name": "minions_migration",
      "status": "ok",
      "severity": "info",
      "message": "5 setup migration(s) not run yet on this new brain (pending_fresh_install: 0.11.0, 0.14.0, 0.22.4, 0.28.0, 0.53.0). Expected after gbrain init, not a failed upgrade.",
      "fix": {
        "argv": [
          "gbrain",
          "apply-migrations",
          "--yes",
          "--no-autopilot-install"
        ],
        "command": "gbrain apply-migrations --yes --no-autopilot-install",
        "consent": [],
        "actor": "agent",
        "next": "run",
        "why": "Runs the setup migrations gbrain init left pending (preferences, host-work notes, shared-skill checkpoints) on the brain host, without installing background services.",
        "verify": {
          "argv": [
            "gbrain",
            "doctor",
            "--only",
            "minions_migration",
            "--json",
            "--brain",
            "host"
          ]
        },
        "requires_exclusive": true
      },
      "details": {
        "pending_fresh_install": [
          "0.11.0",
          "0.14.0",
          "0.22.4",
          "0.28.0",
          "0.53.0"
        ]
      },
      "elapsed_ms": 69,
      "category": "meta"
    },
    {
      "name": "self_upgrade_health",
      "status": "ok",
      "message": "mode=notify; channel=stable (config)",
      "elapsed_ms": 69,
      "category": "ops"
    },
    {
      "name": "bun_runtime",
      "status": "ok",
      "message": "Bun 1.4.5 (minimum 1.4.4)",
      "elapsed_ms": 69,
      "category": "ops"
    },
    {
      "name": "nightly_quality_probe_health",
      "status": "ok",
      "message": "disabled (opt-in). Enable with: gbrain config set autopilot.nightly_quality_probe.enabled true",
      "elapsed_ms": 127,
      "category": "brain"
    },
    {
      "name": "extract_health",
      "status": "ok",
      "message": "no extractions in last 7 days",
      "details": {
        "schema_version": 1,
        "kinds": []
      },
      "elapsed_ms": 127,
      "category": "brain"
    },
    {
      "name": "conversation_facts_backlog",
      "status": "ok",
      "message": "disabled (opt-in). Enable with: gbrain config set cycle.conversation_facts_backfill.enabled true",
      "elapsed_ms": 127,
      "category": "brain"
    },
    {
      "name": "extract_atoms_backlog",
      "status": "ok",
      "message": "no pages awaiting atom extraction",
      "details": {
        "backlog": 0,
        "pack_declares_phase": false,
        "known_approximation": "page backlog only; transcript corpus not counted"
      },
      "elapsed_ms": 127,
      "category": "brain"
    },
    {
      "name": "atom_provenance_drift",
      "status": "ok",
      "message": "no atoms to check",
      "details": {
        "total_atoms": 0,
        "slug_unbound": 0,
        "drifted": 0,
        "source_changed": 0,
        "source_gone": 0,
        "body_unchanged": 0,
        "drift_pct": 0
      },
      "elapsed_ms": 127,
      "category": "brain"
    },
    {
      "name": "conversation_format_coverage",
      "status": "ok",
      "message": "No conversation-type pages — coverage check not applicable",
      "elapsed_ms": 127,
      "category": "brain"
    },
    {
      "name": "progressive_batch_audit_health",
      "status": "ok",
      "message": "No progressive-batch operations in the last 7 days",
      "elapsed_ms": 127,
      "category": "ops"
    },
    {
      "name": "conversation_parser_probe_health",
      "status": "ok",
      "message": "disabled (opt-in; default-on only for search.mode=tokenmax). Enable with: `gbrain config set autopilot.conversation_parser_probe.enabled true`",
      "elapsed_ms": 127,
      "category": "brain"
    },
    {
      "name": "home_dir_in_worktree",
      "status": "ok",
      "message": "gbrain home is outside any enclosing git worktree.",
      "elapsed_ms": 232,
      "category": "ops"
    },
    {
      "name": "npm_squat",
      "status": "ok",
      "message": "gbrain on PATH is the real binary (/home/codespace/.bun/bin/gbrain).",
      "elapsed_ms": 232,
      "category": "ops"
    },
    {
      "name": "default_source_local_path",
      "status": "ok",
      "message": "default source local_path is set: /home/codespace/.gbrain/content/9e0ca848-da10-4798-86e8-0acbfd070f53/default",
      "elapsed_ms": 5,
      "category": "meta"
    },
    {
      "name": "embedding_key_source",
      "status": "ok",
      "message": "No embedding key is set here (VOYAGE_API_KEY or voyage_api_key). No environment variable overrides a different config-plane provider key. This check sees only the environment `gbrain doctor` runs in; a daemon (gbrain serve, autopilot) has its own, and reports a mismatch in its log with a startup warning or embedding_auth_failed.",
      "details": {
        "shadows": [],
        "embedding_model": "voyage:voyage-4",
        "embedding_key": {
          "kind": "missing",
          "variable": "VOYAGE_API_KEY",
          "config_key": "voyage_api_key"
        },
        "docs": "docs/guides/repair.md#embedding-key-source"
      },
      "elapsed_ms": 1,
      "category": "brain"
    },
    {
      "name": "provider_consent",
      "status": "ok",
      "message": "No gbrain setup receipt records a provider-use decision for this install; provider calls follow the configured keys.",
      "severity": "info",
      "readiness_state": "not_applicable",
      "details": {
        "decision": null,
        "provider_env": []
      },
      "elapsed_ms": 0,
      "category": "ops"
    },
    {
      "name": "harness_wiring",
      "status": "ok",
      "message": "No agent harness was detected. Wire one when the user picks an agent app.",
      "severity": "info",
      "readiness_state": "missing",
      "fix": {
        "consent": [
          "persistent_install"
        ],
        "actor": "user",
        "next": "report",
        "why": "For Claude Code or Codex, run `gbrain setup claude-code` or `gbrain setup codex` (it registers serve behind gbrain's launcher, so the session directory's bunfig.toml and .env never load). For any other host, register `<absolute path to gbrain> serve --surface starter --advertise verbs` as a stdio MCP server in your agent host; the install section lists the exact command per harness (Claude Code, Codex, Grok Build, opencode, OpenClaw).",
        "user_message": "Which agent app should get gbrain memory? The install guide has a one-line command for each.",
        "docs": "https://github.com/garrytan/gbrain/blob/v0.60.753.0/docs/protocol/MEMORY_VERBS_v1.md#install-the-4-command-quickstart",
        "requires_exclusive": false
      },
      "details": {
        "reason": "no_harness_detected"
      },
      "elapsed_ms": 37,
      "category": "ops"
    },
    {
      "name": "agent_contract",
      "status": "ok",
      "message": "No agent dead ends in the last 7 days (0 non-success event(s) logged).",
      "details": {
        "window_days": 7,
        "events": 0,
        "internal_errors": 0,
        "consent_refused": 0,
        "derived_cap_exhausted": 0,
        "json_document_missing": 0
      },
      "elapsed_ms": 0,
      "category": "meta"
    },
    {
      "name": "connection",
      "status": "ok",
      "message": "Connected, 0 pages",
      "elapsed_ms": 21,
      "category": "ops"
    },
    {
      "name": "persistence_capacity",
      "status": "ok",
      "details": {
        "exact": true,
        "inspected": 2,
        "truncated": false,
        "resources": [],
        "outstanding": [],
        "commands": [],
        "housekeeping": {
          "target_bytes": 8589934592,
          "used_bytes": 19163,
          "compactable_bytes": null,
          "over_target": false,
          "explicit_retention_days": null
        },
        "verify": "gbrain doctor --only persistence_capacity --json",
        "docs": "docs/guides/concurrent-writes.md#quota-near-exhaustion",
        "background_pause_pct": 80,
        "paused_producers": [],
        "forecast": {
          "thresholds": {
            "warn_days": 30,
            "fail_days": 7,
            "warn_pct": 80,
            "fail_pct": 95
          },
          "window_days": 1,
          "retention_days": 30,
          "table_bytes": 344064,
          "rows": []
        }
      },
      "message": "No cumulative write cap is set (the default), so receipt storage never refuses or pauses a write; it holds 19163 reserved bytes, and receipts not yet compacted are under the housekeeping target of 8589934592.",
      "elapsed_ms": 41,
      "category": "ops"
    },
    {
      "name": "persistence_terminal_failures",
      "status": "ok",
      "details": {
        "count": 0,
        "active_blockers": [],
        "unresolved": {
          "rows": 0,
          "distinct_slugs": 0,
          "distinct_intents": 0,
          "oldest_age_seconds": null
        },
        "historical_rows": 0,
        "new_last_24h": 0,
        "spike": {
          "last_24h": 0,
          "median_7d": 0,
          "daily_7d": [
            0,
            0,
            0,
            0,
            0,
            0,
            0
          ],
          "spiking": false
        },
        "defects": [],
        "sources": [],
        "ranked": {
          "blocking": [],
          "unresolved": {
            "rows": 0,
            "pages": 0,
            "groups": [],
            "group_by": []
          },
          "historical": {
            "rows": 0
          }
        },
        "window_days": 7,
        "config": {
          "window_days": {
            "key": "persistence.terminal_failures.window_days",
            "value": 7
          },
          "spike_factor": {
            "key": "persistence.terminal_failures.spike_factor",
            "value": 3
          },
          "spike_min": {
            "key": "persistence.terminal_failures.spike_min",
            "value": 25
          },
          "receipt_retention_days": 30,
          "window_clamped": false
        },
        "docs": "docs/guides/troubleshooting.md#terminal-write-failures"
      },
      "message": "No terminal write failures in the last 7 d.",
      "elapsed_ms": 34,
      "category": "ops"
    },
    {
      "name": "managed_sync_not_moving",
      "status": "ok",
      "message": "No managed sync is pending.",
      "details": {
        "count": 0,
        "parked": 0,
        "stranded": 0,
        "sources": [],
        "docs": "docs/guides/troubleshooting.md#managed-sync-not-moving"
      },
      "elapsed_ms": 17,
      "category": "ops"
    },
    {
      "name": "managed_sync_blocked",
      "status": "ok",
      "message": "No managed sync run is blocked.",
      "elapsed_ms": 10,
      "category": "ops"
    },
    {
      "name": "sync_admission_restricted",
      "status": "ok",
      "message": "sync.admission is normal: managed sync admits everything it classifies.",
      "details": {
        "value": "normal",
        "stored": null,
        "set_at": null,
        "age_seconds": null,
        "docs": "docs/guides/error-codes.md#sync_admission_restricted"
      },
      "elapsed_ms": 1,
      "category": "ops"
    },
    {
      "name": "persistence_compaction",
      "status": "ok",
      "details": {
        "live_consumers": 0,
        "stale_hours": 24,
        "last_compaction": {
          "at": "2026-11-22T02:39:24.642Z",
          "host_id": "19cbe0ec-62ad-4230-baf2-ac388ef37edc",
          "compacted": 0,
          "freed_bytes": 0,
          "skipped_by_reason": {},
          "early": 0
        },
        "last_compaction_age_hours": 0,
        "docs": "docs/guides/repair.md#receipt-compaction"
      },
      "message": "Receipt compaction last ran 0 hour(s) ago (compacted 0, freed 0 bytes).",
      "elapsed_ms": 3,
      "category": "ops"
    },
    {
      "name": "sync_soak_counters",
      "status": "ok",
      "severity": "info",
      "details": {
        "window_days": 7,
        "since": "2026-11-16T00:00:00.000Z",
        "interventions": {
          "sync_non_plain": 0,
          "repair_apply": 0,
          "unblock_apply": 0,
          "retry_held": 0,
          "needs_human": 0,
          "total": 0
        },
        "content_decisions": {
          "file_drift_apply": 0,
          "file_drift_hold": 0,
          "total": 0
        },
        "by_day": [],
        "docs": "docs/guides/sync-unblock-runbook.md#soak-counters"
      },
      "message": "Last 7 days: 0 managed-sync intervention(s), 0 content decision(s).",
      "elapsed_ms": 3,
      "category": "ops"
    },
    {
      "name": "serve_build_drift",
      "status": "ok",
      "message": "PGLite admits one process; no consumer heartbeat rows are kept to compare builds.",
      "details": {
        "count": 0,
        "docs": "docs/guides/troubleshooting.md#serve-build-drift"
      },
      "elapsed_ms": 0,
      "category": "ops"
    },
    {
      "name": "schema_pack_consistency",
      "status": "ok",
      "message": "No pages in any source — schema consistency N/A.",
      "elapsed_ms": 4,
      "category": "meta"
    },
    {
      "name": "embedding_state",
      "status": "ok",
      "message": "Embedding state (exact, column 'embedding'): 0 embedded, 0 pending, 0 keyword-only, 0 quarantined, 0 empty, 0 on deleted pages, 0 chunkless (healable); 0 unsearchable.",
      "severity": "info",
      "readiness_state": "disabled_by_choice",
      "fix": {
        "argv": [
          "gbrain",
          "init",
          "--force",
          "--embedding-model",
          "voyage:voyage-4",
          "--embedding-dimensions",
          "1024",
          "--path",
          "/home/codespace/.gbrain/brain.pglite"
        ],
        "command": "gbrain init --force --embedding-model voyage:voyage-4 --embedding-dimensions 1024 --path /home/codespace/.gbrain/brain.pglite",
        "consent": [
          "credentials",
          "paid"
        ],
        "actor": "user",
        "next": "tell_user_to_run",
        "why": "Embeddings are off, so search is keyword-only, and no configured embedding key fits this brain. Once the key is set this turns on voyage:voyage-4 (1024d) for the PGLite brain at /home/codespace/.gbrain/brain.pglite. Pages, facts and keyword search are kept; existing chunks and facts are queued for vectors, which `gbrain embed --stale` (or the next maintenance cycle) fills.",
        "user_message": "Semantic search needs an embedding API key. Voyage AI works with this brain; if you add a key (VOYAGE_API_KEY), I can turn it on. Embedding costs a little per page; your notes and facts stay as they are.",
        "verify": {
          "argv": [
            "gbrain",
            "doctor",
            "--only",
            "embeddings",
            "--json",
            "--brain",
            "host"
          ]
        },
        "docs": "https://github.com/garrytan/gbrain/blob/v0.60.753.0/docs/guides/search-modes.md",
        "requires_exclusive": true,
        "inputs": [
          {
            "name": "VOYAGE_API_KEY",
            "how": "Ask the user for an API key for Voyage AI; store it with `gbrain config set voyage_api_key <key>` (every gbrain process reads it), or export VOYAGE_API_KEY in the environment of every gbrain process. Then run the command."
          }
        ]
      },
      "details": {
        "status": "known",
        "basis": "exact",
        "reason": "embeddings_disabled",
        "active_column": "embedding",
        "counts": {
          "embedded": 0,
          "pending": 0,
          "keyword_only": 0,
          "quarantined": 0,
          "empty": 0,
          "deleted_page_chunks": 0,
          "chunkless_healable": 0
        },
        "unsearchable": 0,
        "unsearchable_complete": true,
        "omitted_states": [],
        "mode": "full",
        "embeddings_enabled": false,
        "units": "content_chunks rows, plus one unit per page with no chunk rows",
        "covering_index": null,
        "coverage": {
          "basis": "exact",
          "embedded": 0,
          "eligible": 0,
          "ratio": null
        },
        "keyword_only": {
          "reason": "embed_skip",
          "pages": 0,
          "marker_bytes": 0,
          "threshold_bytes": 25165824
        },
        "deleted_page_chunks": {
          "within_window": 0,
          "past_window": 0,
          "purgeable": 0,
          "held": 0,
          "window_hours": 72
        },
        "unstamped_pending": {
          "count": 0,
          "created_at_lower_bound": null,
          "writer_version": "0.60.753.0"
        },
        "exact": true
      },
      "elapsed_ms": 22,
      "category": "brain"
    },
    {
      "name": "links_extraction_lag",
      "status": "ok",
      "message": "Extraction lag not applicable (no pages)",
      "elapsed_ms": 21,
      "category": "brain"
    },
    {
      "name": "partial_embedding",
      "status": "ok",
      "message": "No large page has chunks waiting for embedding approval (held or capped by embed.max_usd_per_page).",
      "elapsed_ms": 8,
      "category": "brain"
    },
    {
      "name": "sync_landing_gaps",
      "status": "ok",
      "details": {
        "docs": "docs/guides/resolve-paths.md#synced-but-not-searchable",
        "sources": [
          {
            "source_id": "default",
            "status": "ok",
            "window_hours": 24,
            "after_seconds": 300,
            "checked": 0,
            "complete": true,
            "gaps": 0,
            "by_state": {},
            "pages": []
          }
        ]
      },
      "message": "Every page managed sync committed past its freshness target in the last 24 h is searchable.",
      "elapsed_ms": 7,
      "category": "brain"
    },
    {
      "name": "pgvector",
      "status": "ok",
      "message": "Extension installed",
      "elapsed_ms": 100,
      "category": "ops"
    },
    {
      "name": "pages_upsert_arbiter",
      "status": "ok",
      "message": "pages has the UNIQUE(source_id, slug) upsert arbiter",
      "elapsed_ms": 100,
      "category": "meta"
    },
    {
      "name": "text_projection_readiness",
      "status": "ok",
      "message": "Visible text projections match their canonical revisions.",
      "details": {
        "readiness": "ready",
        "ready": true,
        "pending": 0,
        "failed": 0,
        "sealable": 0,
        "sealable_with_visual": 0,
        "reimport": 0,
        "ocr_required": 0,
        "protected": 0,
        "archived": 0,
        "oldest_age_seconds": null,
        "as_of": "2026-11-22 02:51:00.266+00"
      },
      "elapsed_ms": 100,
      "category": "brain"
    },
    {
      "name": "persistence_counter_drift",
      "status": "ok",
      "details": {
        "inspected": 2,
        "drift": [],
        "true_up_clamped": 0,
        "docs": "docs/guides/concurrent-writes.md#counter-drift"
      },
      "message": "Receipt-bytes counters match the receipts they account for (2 scope(s)).",
      "elapsed_ms": 100,
      "category": "ops"
    },
    {
      "name": "parked_effects",
      "status": "ok",
      "message": "No Git or withdrawal effect is parked.",
      "details": {
        "parked_effects": 0,
        "exact": true,
        "inspected": 0,
        "truncated": false,
        "effects": [],
        "parked_groups": [],
        "git_push_holds": []
      },
      "elapsed_ms": 100,
      "category": "brain"
    },
    {
      "name": "worktree_refresh_stuck",
      "status": "ok",
      "message": "No worktree refresh is stuck.",
      "details": {
        "refreshes": []
      },
      "elapsed_ms": 100,
      "category": "ops"
    },
    {
      "name": "managed_guard_schema_drift",
      "status": "ok",
      "message": "Guarded tables carry only the columns gbrain creates.",
      "details": {
        "extra_columns": [],
        "columns": [],
        "page_child_source_columns": [],
        "runbook": "docs/guides/write-refusals.md#managed-guard-page-children"
      },
      "elapsed_ms": 100,
      "category": "ops"
    },
    {
      "name": "publication_refusals",
      "status": "ok",
      "message": "No write was refused by a database guard in the last 7 days.",
      "details": {
        "guard_refusals": 0,
        "trigger_refusals": 0,
        "unclassified_p0001": 0,
        "window_days": 7,
        "runbook": "docs/guides/write-refusals.md#managed-guard-page-children"
      },
      "elapsed_ms": 100,
      "category": "ops"
    },
    {
      "name": "links_link_source_check",
      "status": "ok",
      "message": "links_link_source_check has the v114 kebab-case gate",
      "elapsed_ms": 100,
      "category": "meta"
    },
    {
      "name": "pglite_scale",
      "status": "ok",
      "message": "PGLite at 0 pages — comfortable below the 1000-page threshold",
      "elapsed_ms": 100,
      "category": "ops"
    },
    {
      "name": "derived_visibility",
      "status": "ok",
      "details": {
        "unstamped_atoms": 0,
        "unstamped_concepts": 0,
        "looser_atoms": 0,
        "looser_concepts": 0,
        "looser_events": 0,
        "alias_pages_without_visibility": 0,
        "world_facts_from_private_sources": 0,
        "world_facts_remotely_readable": 0,
        "remotely_readable_fact_ids": [],
        "fact_ids_truncated": false,
        "count": "exact",
        "truncated": false,
        "repair": "visibility"
      },
      "message": "Every derived page and fact carries a visibility no looser than its source, and no page relies on a privacy alias alone.",
      "elapsed_ms": 45,
      "category": "brain"
    },
    {
      "name": "git_index_lag",
      "status": "ok",
      "details": {
        "sources": [],
        "warn_seconds": 900,
        "docs": "docs/designs/GIT_CANONICAL_MEMORY.md#the-model"
      },
      "message": "No source is strict (git-canonical), so no index trails a commit.",
      "elapsed_ms": 2,
      "category": "brain"
    },
    {
      "name": "db_ahead_of_git",
      "status": "ok",
      "details": {
        "informational": true,
        "sources": [],
        "partial_sources": [],
        "errors": [],
        "sources_without_git_checkout": 1,
        "newest": 800,
        "timeout_ms": 10000,
        "docs": "docs/designs/GIT_CANONICAL_MEMORY.md#the-git-gap-census"
      },
      "message": "No source has a Git checkout, so there is no commit to compare the database with.",
      "elapsed_ms": 8,
      "category": "brain"
    },
    {
      "name": "strict_facts_outside_git",
      "status": "ok",
      "details": {
        "sources": [],
        "docs": "docs/guides/repair.md#facts-home"
      },
      "message": "No source is strict (git-canonical), so no fact is required to have a Git home.",
      "elapsed_ms": 2,
      "category": "brain"
    },
    {
      "name": "owner_host_stale",
      "status": "ok",
      "details": {
        "count": 0,
        "stale_after_ms": 86400000,
        "stale": [],
        "docs": "docs/guides/troubleshooting.md#owner-host-stale"
      },
      "message": "No managed write is waiting on an owner host.",
      "elapsed_ms": 3,
      "category": "ops"
    },
    {
      "name": "uncommitted_sync_deletions",
      "status": "ok",
      "details": {
        "count": 0,
        "other_writer_count": 0,
        "truncated": false,
        "exact": true,
        "purged": "Pages already purged cannot be restored by this command; only a backup (pg_dump, or gbrain backup create taken before the purge) can bring them back.",
        "docs": "docs/guides/repair.md#uncommitted-deletions",
        "by_source": [
          {
            "source_id": "default",
            "status": "known",
            "sync_deleted": 0,
            "other_writer": 0,
            "tombstones": 0,
            "checked": 0,
            "unknown": 0,
            "truncated": false
          }
        ],
        "samples": []
      },
      "message": "No soft-deleted page was removed by a sync while Git never held its file (0 tombstone(s) checked).",
      "elapsed_ms": 11,
      "category": "brain"
    },
    {
      "name": "access_readers_malformed",
      "status": "ok",
      "message": "Not applicable: no page names readers and no member exists.",
      "severity": "info",
      "readiness_state": "not_applicable",
      "elapsed_ms": 0,
      "category": "brain"
    },
    {
      "name": "access_unknown_readers",
      "status": "ok",
      "message": "Not applicable: no page names readers and no member exists.",
      "severity": "info",
      "readiness_state": "not_applicable",
      "elapsed_ms": 0,
      "category": "brain"
    },
    {
      "name": "access_recent_narrowings",
      "status": "ok",
      "message": "Not applicable: no page names readers and no member exists.",
      "severity": "info",
      "readiness_state": "not_applicable",
      "elapsed_ms": 0,
      "category": "brain"
    },
    {
      "name": "access_page_readers_backfill",
      "status": "ok",
      "message": "Not applicable: no page names readers and no member exists.",
      "severity": "info",
      "readiness_state": "not_applicable",
      "elapsed_ms": 0,
      "category": "brain"
    },
    {
      "name": "access_policy_pending",
      "status": "ok",
      "message": "Not applicable: no source has a folder rule.",
      "severity": "info",
      "readiness_state": "not_applicable",
      "elapsed_ms": 3,
      "category": "brain"
    },
    {
      "name": "access_policy_widening_held",
      "status": "ok",
      "message": "Not applicable: no source has a folder rule.",
      "severity": "info",
      "readiness_state": "not_applicable",
      "elapsed_ms": 3,
      "category": "brain"
    },
    {
      "name": "access_policy_invalid",
      "status": "ok",
      "message": "Not applicable: no source has a folder rule.",
      "severity": "info",
      "readiness_state": "not_applicable",
      "elapsed_ms": 3,
      "category": "brain"
    },
    {
      "name": "access_policy_store_mismatch",
      "status": "ok",
      "message": "Not applicable: no source has a folder rule.",
      "severity": "info",
      "readiness_state": "not_applicable",
      "elapsed_ms": 3,
      "category": "brain"
    },
    {
      "name": "unlabeled_people_folders",
      "status": "ok",
      "message": "Not applicable: this brain serves one person (fewer than two enabled members and no access.serves = several).",
      "severity": "info",
      "readiness_state": "not_applicable",
      "elapsed_ms": 2,
      "category": "brain"
    },
    {
      "name": "open_shared_pages",
      "status": "ok",
      "message": "Not applicable: this brain serves one person, so its own keys read its own pages.",
      "severity": "info",
      "readiness_state": "not_applicable",
      "elapsed_ms": 1,
      "category": "brain"
    },
    {
      "name": "unscoped_shared_reads",
      "status": "ok",
      "message": "Not applicable: this brain serves one person (fewer than two enabled members and no access.serves = several).",
      "severity": "info",
      "readiness_state": "not_applicable",
      "elapsed_ms": 3,
      "category": "brain"
    },
    {
      "name": "shared_stdio_binding",
      "status": "ok",
      "message": "Not applicable: config mcp.stdio_member is unset, so no stdio session on this host reads as a member.",
      "severity": "info",
      "readiness_state": "not_applicable",
      "elapsed_ms": 0,
      "category": "brain"
    },
    {
      "name": "access_may_act_for_wildcard",
      "status": "ok",
      "message": "Not applicable: no page names readers and no member exists.",
      "severity": "info",
      "readiness_state": "not_applicable",
      "elapsed_ms": 1,
      "category": "brain"
    },
    {
      "name": "access_owner_reads_restricted",
      "status": "ok",
      "message": "Not applicable: the owner opt-in (access.owner_reads_restricted) is off; the owner reads a page that names readers or sits under a rule only when listed.",
      "severity": "info",
      "readiness_state": "not_applicable",
      "elapsed_ms": 0,
      "category": "brain"
    },
    {
      "name": "access_raw_only_rules",
      "status": "ok",
      "message": "Not applicable: every folder and page rule also keeps the pages and facts derived from its pages to its readers (no rule has covers_derived: false).",
      "severity": "info",
      "readiness_state": "not_applicable",
      "elapsed_ms": 2,
      "category": "brain"
    },
    {
      "name": "access_audience_members",
      "status": "ok",
      "message": "Not applicable: no member is marked as an audience (gbrain access member kind <id> audience).",
      "severity": "info",
      "readiness_state": "not_applicable",
      "elapsed_ms": 2,
      "category": "brain"
    },
    {
      "name": "access_members_read_lineage",
      "status": "ok",
      "message": "Not applicable: access.members_read_lineage is off; derived pages and facts of a page that names readers or sits under a rule are hidden from every member but the owner.",
      "severity": "info",
      "readiness_state": "not_applicable",
      "elapsed_ms": 2,
      "category": "brain"
    },
    {
      "name": "access_labelled_only_members",
      "status": "ok",
      "message": "Not applicable: no member is labelled-only (gbrain access member labelled-only <id> on).",
      "severity": "info",
      "readiness_state": "not_applicable",
      "elapsed_ms": 1,
      "category": "brain"
    },
    {
      "name": "access_pages_read_by_nobody",
      "status": "ok",
      "message": "Not applicable: this brain has no members (gbrain access member add <id>).",
      "severity": "info",
      "readiness_state": "not_applicable",
      "elapsed_ms": 4,
      "category": "brain"
    },
    {
      "name": "attest_read_shared_scope",
      "status": "ok",
      "message": "Not applicable: no attest credential reads named sources as the person (--attest-read person).",
      "severity": "info",
      "readiness_state": "not_applicable",
      "elapsed_ms": 12,
      "category": "brain"
    },
    {
      "name": "guest_source",
      "status": "ok",
      "message": "Not applicable: this brain has no guest source (gbrain guests init).",
      "severity": "info",
      "readiness_state": "not_applicable",
      "elapsed_ms": 3,
      "category": "brain"
    },
    {
      "name": "rls",
      "status": "ok",
      "message": "Skipped (PGLite — no PostgREST exposure, RLS not applicable)",
      "elapsed_ms": 0,
      "category": "ops"
    },
    {
      "name": "function_search_path",
      "status": "ok",
      "message": "Every gbrain function that pins a search_path ends it with pg_temp",
      "elapsed_ms": 15,
      "category": "ops"
    },
    {
      "name": "guard_ledger_checks",
      "status": "ok",
      "message": "Skipped (PGLite has no row-level security, so every guard reads its ledgers in full)",
      "elapsed_ms": 0,
      "category": "ops"
    },
    {
      "name": "owner_only_marks_triggers",
      "status": "ok",
      "message": "Every owner-only delete trigger exists, so rows derived from a removed owner-only source stay owner-only",
      "details": {
        "closed": false
      },
      "elapsed_ms": 14,
      "category": "ops"
    },
    {
      "name": "database_encoding",
      "status": "ok",
      "message": "Skipped (PGLite is always UTF8)",
      "elapsed_ms": 0,
      "category": "ops"
    },
    {
      "name": "schema_version",
      "status": "ok",
      "message": "Version 330 (latest: 330)",
      "elapsed_ms": 92,
      "category": "meta"
    },
    {
      "name": "schema_columns",
      "status": "ok",
      "message": "1393 column(s) verified against live schema",
      "elapsed_ms": 92,
      "category": "meta"
    },
    {
      "name": "schema_missing_tables",
      "status": "ok",
      "message": "All 191 table(s) the applied migrations create exist.",
      "elapsed_ms": 92,
      "category": "meta"
    },
    {
      "name": "schema_function_bodies",
      "status": "ok",
      "message": "Every function this gbrain's schema defines has its body",
      "elapsed_ms": 5,
      "category": "meta"
    },
    {
      "name": "rls_event_trigger",
      "status": "ok",
      "message": "Skipped (PGLite — no event trigger support)",
      "elapsed_ms": 0,
      "category": "ops"
    },
    {
      "name": "embeddings",
      "status": "ok",
      "message": "Not applicable: embeddings are disabled on this brain (keyword search keeps working).",
      "severity": "info",
      "readiness_state": "disabled_by_choice",
      "fix": {
        "argv": [
          "gbrain",
          "init",
          "--force",
          "--embedding-model",
          "voyage:voyage-4",
          "--embedding-dimensions",
          "1024",
          "--path",
          "/home/codespace/.gbrain/brain.pglite"
        ],
        "command": "gbrain init --force --embedding-model voyage:voyage-4 --embedding-dimensions 1024 --path /home/codespace/.gbrain/brain.pglite",
        "consent": [
          "credentials",
          "paid"
        ],
        "actor": "user",
        "next": "tell_user_to_run",
        "why": "Embeddings are off, so search is keyword-only, and no configured embedding key fits this brain. Once the key is set this turns on voyage:voyage-4 (1024d) for the PGLite brain at /home/codespace/.gbrain/brain.pglite. Pages, facts and keyword search are kept; existing chunks and facts are queued for vectors, which `gbrain embed --stale` (or the next maintenance cycle) fills.",
        "user_message": "Semantic search needs an embedding API key. Voyage AI works with this brain; if you add a key (VOYAGE_API_KEY), I can turn it on. Embedding costs a little per page; your notes and facts stay as they are.",
        "verify": {
          "argv": [
            "gbrain",
            "doctor",
            "--only",
            "embeddings",
            "--json",
            "--brain",
            "host"
          ]
        },
        "docs": "https://github.com/garrytan/gbrain/blob/v0.60.753.0/docs/guides/search-modes.md",
        "requires_exclusive": true,
        "inputs": [
          {
            "name": "VOYAGE_API_KEY",
            "how": "Ask the user for an API key for Voyage AI; store it with `gbrain config set voyage_api_key <key>` (every gbrain process reads it), or export VOYAGE_API_KEY in the environment of every gbrain process. Then run the command."
          }
        ]
      },
      "elapsed_ms": 1,
      "category": "brain"
    },
    {
      "name": "embedding_provider",
      "status": "ok",
      "message": "Not probed: embeddings are disabled on this brain by choice (keyword search keeps working).",
      "severity": "info",
      "readiness_state": "disabled_by_choice",
      "fix": {
        "argv": [
          "gbrain",
          "init",
          "--force",
          "--embedding-model",
          "voyage:voyage-4",
          "--embedding-dimensions",
          "1024",
          "--path",
          "/home/codespace/.gbrain/brain.pglite"
        ],
        "command": "gbrain init --force --embedding-model voyage:voyage-4 --embedding-dimensions 1024 --path /home/codespace/.gbrain/brain.pglite",
        "consent": [
          "credentials",
          "paid"
        ],
        "actor": "user",
        "next": "tell_user_to_run",
        "why": "Embeddings are off, so search is keyword-only, and no configured embedding key fits this brain. Once the key is set this turns on voyage:voyage-4 (1024d) for the PGLite brain at /home/codespace/.gbrain/brain.pglite. Pages, facts and keyword search are kept; existing chunks and facts are queued for vectors, which `gbrain embed --stale` (or the next maintenance cycle) fills.",
        "user_message": "Semantic search needs an embedding API key. Voyage AI works with this brain; if you add a key (VOYAGE_API_KEY), I can turn it on. Embedding costs a little per page; your notes and facts stay as they are.",
        "verify": {
          "argv": [
            "gbrain",
            "doctor",
            "--only",
            "embeddings",
            "--json",
            "--brain",
            "host"
          ]
        },
        "docs": "https://github.com/garrytan/gbrain/blob/v0.60.753.0/docs/guides/search-modes.md",
        "requires_exclusive": true,
        "inputs": [
          {
            "name": "VOYAGE_API_KEY",
            "how": "Ask the user for an API key for Voyage AI; store it with `gbrain config set voyage_api_key <key>` (every gbrain process reads it), or export VOYAGE_API_KEY in the environment of every gbrain process. Then run the command."
          }
        ]
      },
      "elapsed_ms": 1,
      "category": "brain"
    },
    {
      "name": "embedding_column_registry",
      "status": "ok",
      "message": "Registry healthy: 1 columns (embedding_image); primary embeddings disabled",
      "elapsed_ms": 6,
      "category": "brain"
    },
    {
      "name": "embedding_env_override",
      "status": "ok",
      "message": "no embedding env overrides set",
      "elapsed_ms": 4,
      "category": "brain"
    },
    {
      "name": "embedding_migration_state",
      "status": "ok",
      "message": "no embedding migration in flight",
      "elapsed_ms": 4,
      "category": "brain"
    },
    {
      "name": "embedding_identity_unqualified",
      "status": "ok",
      "message": "The brain records its embedding model with its provider (voyage:voyage-4).",
      "elapsed_ms": 1,
      "category": "brain"
    },
    {
      "name": "supersession_calibration",
      "status": "ok",
      "severity": "info",
      "readiness_state": "not_applicable",
      "message": "Embeddings are off on this brain, so facts are only deduplicated by exact text; no supersession threshold applies.",
      "elapsed_ms": 0,
      "category": "brain"
    },
    {
      "name": "fact_admission_floors",
      "status": "ok",
      "severity": "info",
      "readiness_state": "not_applicable",
      "message": "Embeddings are off on this brain, so facts are admitted by keyword and named entity only; no cosine floor applies.",
      "elapsed_ms": 1,
      "category": "brain"
    },
    {
      "name": "chat_fallback_chain",
      "status": "ok",
      "message": "No chat_fallback_chain is set: every chat call uses only its own model.",
      "elapsed_ms": 1,
      "category": "ops"
    },
    {
      "name": "behavior_changes",
      "status": "ok",
      "message": "Nothing to disclose: this brain is a fresh install at v0.60.753.0, after every disclosed behavior change, so the one-time behavior-change notice does not apply.",
      "elapsed_ms": 4,
      "category": "meta"
    },
    {
      "name": "graph_coverage",
      "status": "ok",
      "message": "No entity pages — graph_coverage not applicable (markdown-only brain)",
      "elapsed_ms": 38,
      "category": "brain"
    },
    {
      "name": "brain_score",
      "status": "ok",
      "message": "Brain score 100/100",
      "elapsed_ms": 38,
      "category": "brain"
    },
    {
      "name": "orphan_ratio",
      "status": "ok",
      "message": "Vacuous: 0 entity pages (<100). Orphan ratio not meaningful at this scale.",
      "elapsed_ms": 4,
      "category": "brain"
    },
    {
      "name": "stale_mentions",
      "status": "ok",
      "message": "No by-mention links in this brain.",
      "elapsed_ms": 36,
      "category": "brain"
    },
    {
      "name": "timeline_orphans",
      "status": "ok",
      "message": "No orphaned timeline rows across 0 page(s).",
      "elapsed_ms": 36,
      "category": "brain"
    },
    {
      "name": "slug_collisions",
      "status": "ok",
      "message": "No slug collisions across 1 source checkout(s).",
      "elapsed_ms": 36,
      "category": "brain"
    },
    {
      "name": "segmented_tiling",
      "status": "ok",
      "message": "Every live page stored in segments has segment rows that cover its whole body.",
      "elapsed_ms": 4,
      "category": "brain"
    },
    {
      "name": "timeline_history",
      "status": "ok",
      "details": {
        "materializable_rows": 0,
        "kept_unrenderable_rows": 0,
        "pages_affected": 0,
        "pages_inspected": 0,
        "count": "exact",
        "truncated": false,
        "repair": "timeline"
      },
      "message": "Every timeline row has a bullet in its page (0 page(s) inspected).",
      "elapsed_ms": 305,
      "category": "brain"
    },
    {
      "name": "privacy_label_ignored",
      "status": "ok",
      "details": {
        "pages": 0,
        "values": [],
        "value_count": 0,
        "values_truncated": false,
        "count": "exact",
        "truncated": false,
        "scan_cap": 100000
      },
      "message": "No page relies on an access or confidentiality value gbrain does not recognize.",
      "elapsed_ms": 305,
      "category": "brain"
    },
    {
      "name": "safe_index_pending",
      "status": "ok",
      "details": {
        "pages_pending": 0,
        "kept_pages": 0,
        "count": "exact",
        "truncated": false,
        "repair": "safe-chunks"
      },
      "message": "Every re-sealable page is at the safe-chunk index version.",
      "elapsed_ms": 305,
      "category": "brain"
    },
    {
      "name": "credential_projection_pending",
      "status": "ok",
      "details": {
        "pages_pending": 0,
        "kept_pages": 0,
        "count": "exact",
        "truncated": false
      },
      "message": "No page waits for the credential-safe re-chunk.",
      "elapsed_ms": 305,
      "category": "brain"
    },
    {
      "name": "connector_checkpoints",
      "status": "ok",
      "message": "No orphan connector checkpoint rows older than 7 days.",
      "details": {
        "count": 0,
        "checkpoints": 0,
        "retries": 0,
        "truncated": false,
        "repair": "connector-checkpoints",
        "docs": "docs/guides/repair.md#connector-checkpoints"
      },
      "elapsed_ms": 305,
      "category": "brain"
    },
    {
      "name": "persistence_request_indexes",
      "status": "ok",
      "message": "Request-table indexes are valid.",
      "details": {
        "count": 0,
        "indexes": [
          {
            "name": "persistence_requests_sync_run_open",
            "state": "valid"
          },
          {
            "name": "persistence_requests_sync_run_committed",
            "state": "valid"
          },
          {
            "name": "persistence_requests_slug_intent",
            "state": "valid"
          },
          {
            "name": "persistence_requests_request_id",
            "state": "valid"
          },
          {
            "name": "persistence_requests_foreground_committed",
            "state": "valid"
          },
          {
            "name": "persistence_requests_replay_id",
            "state": "valid"
          },
          {
            "name": "persistence_requests_slug_sequence",
            "state": "valid"
          }
        ],
        "repair": "request-indexes",
        "command": "gbrain repair request-indexes --apply",
        "docs": "docs/guides/repair.md#request-indexes"
      },
      "elapsed_ms": 305,
      "category": "ops"
    },
    {
      "name": "persistence_request_growth",
      "status": "ok",
      "details": {
        "rows": 1,
        "rows_exact": true,
        "window_days": 7,
        "scopes": [],
        "commands": [],
        "verify": "gbrain doctor --json (check persistence_request_growth)",
        "docs": "docs/guides/repair.md#request-growth"
      },
      "message": "1 request row(s); no scope exhausts its lifetime request IDs within 30 days at its last-7-day rate.",
      "elapsed_ms": 305,
      "category": "ops"
    },
    {
      "name": "persistence_write_stall",
      "status": "ok",
      "details": {
        "max_claim_ms": 600000,
        "config_key": "persistence.max_claim_ms",
        "count": 0,
        "stalls": [],
        "docs": "docs/guides/troubleshooting.md#persistence-write-stall",
        "preparation_policy": {
          "sync_preparation_ms": 120000,
          "maintenance_preparation_ms": 120000,
          "preparation_ceiling_ms": 600000,
          "max_preparation_attempts": 2,
          "max_transient_retries": 5
        }
      },
      "message": "No write request has held its claim longer than persistence.max_claim_ms (600000 ms).",
      "elapsed_ms": 305,
      "category": "ops"
    },
    {
      "name": "lost_caller_writes",
      "status": "ok",
      "details": {
        "count": 0,
        "writes": [],
        "compacted_unreplayable": 0,
        "repair": "failed-writes",
        "docs": "docs/guides/repair.md#failed-writes"
      },
      "message": "Every caller write with a retained receipt committed or was superseded.",
      "elapsed_ms": 305,
      "category": "ops"
    },
    {
      "name": "persistence_session_timeouts",
      "status": "ok",
      "details": {
        "configured": "5min",
        "applied": null,
        "docs": "docs/guides/troubleshooting.md#session-timeouts-not-applied"
      },
      "message": "PGLite has no session to time out.",
      "elapsed_ms": 305,
      "category": "ops"
    },
    {
      "name": "connector_held_items",
      "status": "ok",
      "message": "No connector items are held.",
      "details": {
        "held": 0,
        "sources": [],
        "docs": "docs/guides/repair.md#connector-held-items"
      },
      "elapsed_ms": 305,
      "category": "brain"
    },
    {
      "name": "git_held_files",
      "status": "ok",
      "message": "No Git source files are held.",
      "details": {
        "held": 0,
        "source_ids": [],
        "sources": [],
        "escalate_count": 50,
        "docs": "docs/guides/repair.md#held-files"
      },
      "elapsed_ms": 305,
      "category": "brain"
    },
    {
      "name": "frontmatter_hook",
      "status": "ok",
      "message": "No outdated gbrain frontmatter pre-commit hook is installed.",
      "details": {
        "count": 0,
        "hooks": [],
        "docs": "docs/guides/repair.md#held-files"
      },
      "elapsed_ms": 305,
      "category": "ops"
    },
    {
      "name": "url_source_origin",
      "status": "ok",
      "message": "Every URL source clone records who added it, or was cloned where only the local CLI can clone.",
      "details": {
        "count": 0,
        "sources": [],
        "docs": "docs/guides/repair.md#url-source-origin"
      },
      "elapsed_ms": 305,
      "category": "ops"
    },
    {
      "name": "orphan_persistence_bindings",
      "status": "ok",
      "message": "Every persistence source binding belongs to an existing source.",
      "details": {
        "count": 0,
        "truncated": false,
        "bindings": [],
        "repair": "orphan-bindings",
        "docs": "docs/guides/repair.md#orphan-bindings"
      },
      "elapsed_ms": 305,
      "category": "brain"
    },
    {
      "name": "foreign_ownership_marker",
      "status": "ok",
      "message": "Every ownership marker beside a source checkout belongs to this brain.",
      "details": {
        "count": 0,
        "markers": [],
        "docs": "docs/guides/write-refusals.md#foreign-ownership-marker"
      },
      "elapsed_ms": 305,
      "category": "brain"
    },
    {
      "name": "coordination_lock_location",
      "status": "ok",
      "details": {
        "count": 0,
        "checkouts": [],
        "docs": "docs/architecture/topologies.md#coordination-lock"
      },
      "message": "Every checkout's recorded coordination lock agrees with GBRAIN_COORDINATION_HOME, or the variable does not apply.",
      "elapsed_ms": 305,
      "category": "brain"
    },
    {
      "name": "unbound_source",
      "status": "ok",
      "message": "No page was written database-only to an unbound source.",
      "details": {
        "total": 0,
        "sources": []
      },
      "elapsed_ms": 305,
      "category": "brain"
    },
    {
      "name": "dream_write_deferred",
      "status": "ok",
      "message": "No deferred dream writes",
      "details": {
        "enabled": true,
        "bound": 3,
        "pending": 0,
        "items": []
      },
      "elapsed_ms": 305,
      "category": "ops"
    },
    {
      "name": "embedding_restamp_stalled",
      "status": "ok",
      "message": "The embedding signature restamp is running clean",
      "details": {
        "enabled": true,
        "bound": 3
      },
      "elapsed_ms": 305,
      "category": "ops"
    },
    {
      "name": "writer_version",
      "status": "ok",
      "details": {
        "count": 0,
        "truncated": false,
        "hosts": [],
        "window_days": 7,
        "floor": "0.60.5.0",
        "observed": [
          {
            "host_id": "19cbe0ec-62ad-4230-baf2-ac388ef37edc",
            "principal": "local_cli:deef2a9d-8a5d-4954-b82d-d0dc75f2e271",
            "role": "consumer",
            "version": "0.60.753.0",
            "last_seen": "2026-11-22T02:39:24.515Z"
          },
          {
            "host_id": "19cbe0ec-62ad-4230-baf2-ac388ef37edc",
            "principal": "local_cli:deef2a9d-8a5d-4954-b82d-d0dc75f2e271",
            "role": "admitter",
            "version": "0.60.753.0",
            "last_seen": "2026-11-22T02:39:24.228Z"
          }
        ]
      },
      "message": "Every writer that admitted or published a request in the last 7 days is v0.60.5.0 or newer.",
      "elapsed_ms": 305,
      "category": "ops"
    },
    {
      "name": "segmented_storage",
      "status": "ok",
      "details": {
        "configured": "unset",
        "effective": "on",
        "max_bytes": 134217728,
        "floor": "0.60.299.0",
        "window_days": 7,
        "blockers": [],
        "truncated": false,
        "docs": "docs/guides/memory-boundaries.md#segmented-page-storage"
      },
      "message": "Segmented page storage is on: pages over 1 MiB are stored in segments, up to 134217728 bytes on this PGLite brain.",
      "elapsed_ms": 305,
      "category": "ops"
    },
    {
      "name": "self_capture",
      "status": "ok",
      "message": "No session corpus is configured; nothing to classify.",
      "details": {
        "classified": 0,
        "unclassifiable": 0,
        "count": "exact",
        "truncated": false
      },
      "elapsed_ms": 305,
      "category": "brain"
    },
    {
      "name": "vector_plan",
      "status": "ok",
      "message": "Skipped: PGLite runs vector search in-process; the plan check applies to Postgres brains.",
      "details": {
        "outcome": "skipped",
        "reason": "pglite"
      },
      "elapsed_ms": 305,
      "category": "ops"
    },
    {
      "name": "keyword_plan",
      "status": "ok",
      "message": "Skipped: PGLite runs keyword search with no statement timeout; the canary applies to Postgres brains.",
      "details": {
        "outcome": "skipped",
        "reason": "pglite"
      },
      "elapsed_ms": 305,
      "category": "ops"
    },
    {
      "name": "stale_embedding_effects",
      "status": "ok",
      "details": {
        "stale_effects": 0,
        "failed_effects": 0,
        "retry_queued_effects": 0,
        "count": "exact",
        "truncated": false,
        "effects": [],
        "resolution": "repairable",
        "repair": "embedding-effects",
        "command": "gbrain repair embedding-effects",
        "docs": "docs/guides/repair.md#stale-queued-embedding-effects"
      },
      "message": "No committed write has a stale queued or failed embedding effect.",
      "elapsed_ms": 305,
      "category": "ops"
    },
    {
      "name": "google_file_modes",
      "status": "ok",
      "message": "No group- or world-readable gbrain files under Google source directories outside ~/.gbrain.",
      "details": {
        "count": 0,
        "sources": [],
        "repair": "google-file-modes",
        "docs": "docs/guides/google-connect.md"
      },
      "elapsed_ms": 305,
      "category": "ops"
    },
    {
      "name": "google_calendar_readable",
      "status": "ok",
      "message": "No Google source recorded an unreadable calendar at its last sync.",
      "details": {
        "count": 0,
        "sources": [],
        "docs": "docs/guides/google-connect.md#unreadable-calendar"
      },
      "elapsed_ms": 305,
      "category": "ops"
    },
    {
      "name": "google_api_access",
      "status": "ok",
      "message": "No Google source recorded a disabled API or missing scope at its last sync.",
      "details": {
        "count": 0,
        "sources": [],
        "docs": "docs/guides/google-connect.md#api-access"
      },
      "elapsed_ms": 305,
      "category": "ops"
    },
    {
      "name": "atom_retirements_restorable",
      "status": "ok",
      "details": {
        "count": 0,
        "origins": 0,
        "oldest_retired_at": null,
        "newest_retired_at": null,
        "hold_until": null,
        "source_ids": [],
        "by_source": [],
        "ledger_covered": 0,
        "repair": "atoms-restore",
        "docs": "docs/guides/repair.md#atoms-restore"
      },
      "message": "No atom retired by an empty re-extraction is waiting to be restored.",
      "elapsed_ms": 305,
      "category": "brain"
    },
    {
      "name": "atom_fence_rows",
      "status": "ok",
      "details": {
        "count": 0,
        "by_source": [],
        "origin_unread": 0,
        "repair": "atom-fence-rows",
        "docs": "docs/guides/repair.md#atom-fence-rows"
      },
      "message": "No world atom carries a fence row its source page shows only to the owner.",
      "elapsed_ms": 305,
      "category": "brain"
    },
    {
      "name": "generation_retirements",
      "status": "ok",
      "details": {
        "items": 0,
        "keys": 0,
        "restore_days": 30,
        "by_source": [],
        "repair": "generations",
        "docs": "docs/guides/repair.md#generations"
      },
      "message": "No live generation retired items in the last 30 day(s).",
      "elapsed_ms": 305,
      "category": "brain"
    },
    {
      "name": "generation_held",
      "status": "ok",
      "details": {
        "count": 0,
        "releasable": 0,
        "by_reason": [],
        "repair": "generations",
        "docs": "docs/guides/repair.md#generations"
      },
      "message": "No derived generation is held.",
      "elapsed_ms": 305,
      "category": "brain"
    },
    {
      "name": "generation_pending",
      "status": "ok",
      "details": {
        "pending": 0,
        "retire_pending": 0,
        "orphans": 0,
        "pending_items": [],
        "orphan_candidates": [],
        "docs": "docs/guides/repair.md#generations"
      },
      "message": "No activated generation waits on a member request, and no orphan candidate exists.",
      "elapsed_ms": 305,
      "category": "brain"
    },
    {
      "name": "extractor_facts_expired",
      "status": "ok",
      "details": {
        "evidenced": 0,
        "ambiguous": 0,
        "excluded": 0,
        "repair": "extractor-facts",
        "docs": "docs/guides/repair.md#explicit-only-repair-kinds"
      },
      "message": "No conversation-extractor fact is left expired by the pre-v0.60.11.0 projection.",
      "elapsed_ms": 305,
      "category": "brain"
    },
    {
      "name": "unwithdrawn_facts",
      "status": "ok",
      "details": {
        "evidenced": 0,
        "ambiguous": 0,
        "excluded": 0,
        "repair": "unwithdrawn-facts",
        "docs": "docs/guides/repair.md#unwithdrawn-facts"
      },
      "message": "No fact is left retired by a facts-fence generation that no fence withdrew.",
      "elapsed_ms": 305,
      "category": "brain"
    },
    {
      "name": "purged_page_facts",
      "status": "ok",
      "details": {
        "evidenced": 0,
        "ambiguous": 0,
        "capped": false,
        "repair": "purged-page-facts",
        "docs": "docs/guides/repair.md#purged-page-facts"
      },
      "message": "No fact extracted from a page is left active after that page was purged.",
      "elapsed_ms": 305,
      "category": "brain"
    },
    {
      "name": "conversation_label_facts",
      "status": "ok",
      "details": {
        "evidenced": 0,
        "capped": false,
        "repair": "conversation-labels",
        "docs": "docs/guides/repair.md#conversation-labels"
      },
      "message": "No conversation fact carries the pre-fix meeting-label signature (a 1970-01-01 segment on a label page).",
      "elapsed_ms": 305,
      "category": "brain"
    },
    {
      "name": "conversation_outcomes_stale",
      "status": "ok",
      "details": {
        "extractor_version": 1,
        "scanned": 0,
        "capped": false,
        "stale": 0,
        "unstamped": 0,
        "sample": [],
        "docs": "docs/guides/repair.md#conversation-labels"
      },
      "message": "No conversation extraction outcome predates extractor version 1.",
      "elapsed_ms": 305,
      "category": "brain"
    },
    {
      "name": "captured_facts_active",
      "status": "ok",
      "details": {
        "evidenced": 0,
        "ambiguous": 0,
        "excluded": 0,
        "unclassifiable": 0,
        "repair": "captured-facts",
        "docs": "docs/guides/repair.md#explicit-only-repair-kinds"
      },
      "message": "No active fact from a gbrain self-capture or paste candidate remains. This counts facts in the database; the self_capture check counts corpus files.",
      "elapsed_ms": 305,
      "category": "brain"
    },
    {
      "name": "agent_session_facts",
      "status": "ok",
      "details": {
        "evidenced": 0,
        "ambiguous": 0,
        "excluded": 0,
        "unclassifiable": 0,
        "repair": "agent-session-facts",
        "docs": "docs/guides/repair.md#agent-session-facts"
      },
      "message": "No active owner-attributed fact from an agent-launched session remains.",
      "elapsed_ms": 305,
      "category": "brain"
    },
    {
      "name": "facts_redaction_marker",
      "status": "ok",
      "details": {
        "affected": 0,
        "repair": "redacted-facts",
        "docs": "docs/guides/repair.md#redacted-facts"
      },
      "message": "No active fact holds a redaction marker.",
      "elapsed_ms": 305,
      "category": "brain"
    },
    {
      "name": "fact_bulk_dates",
      "status": "ok",
      "details": {
        "days": [],
        "source_ids": [],
        "rule": {
          "min_facts": 200,
          "min_share": 0.25,
          "min_entities": 20
        },
        "repair": "fact-claim-dates",
        "docs": "docs/guides/repair.md#fact-claim-dates"
      },
      "message": "No calendar day holds a bulk-loaded share of any source's facts.",
      "elapsed_ms": 305,
      "category": "brain"
    },
    {
      "name": "loop_facts_drift",
      "status": "ok",
      "details": {
        "drifted": 0,
        "repair": "loop-facts",
        "docs": "docs/guides/repair.md#explicit-only-repair-kinds"
      },
      "message": "Every closed commitment loop has its fact retired.",
      "elapsed_ms": 305,
      "category": "brain"
    },
    {
      "name": "ontology_facts_fenced",
      "status": "ok",
      "details": {
        "fenced": 0,
        "retired": 0,
        "excluded": 0,
        "repair": "ontology-facts",
        "docs": "docs/guides/repair.md#explicit-only-repair-kinds"
      },
      "message": "No ontology observation is held by a page's Facts table.",
      "elapsed_ms": 305,
      "category": "brain"
    },
    {
      "name": "stale_frontmatter_keys",
      "status": "ok",
      "details": {
        "count": 0,
        "sources": [],
        "source_ids": [],
        "repair": "frontmatter-keys",
        "docs": "docs/guides/repair.md#frontmatter-keys"
      },
      "message": "No stored frontmatter carries a parser-reserved key (type, title, tags, slug).",
      "elapsed_ms": 305,
      "category": "ops"
    },
    {
      "name": "maintenance_write_drift",
      "status": "ok",
      "details": {
        "count": 0,
        "concept_skips": 0,
        "sources": [],
        "window_sequences": 20000,
        "repair": "file-drift",
        "docs": "docs/guides/troubleshooting.md#maintenance-write-drift",
        "suppressed": []
      },
      "message": "No page whose writes refuse source_changed still has a canonical file that differs from the database.",
      "elapsed_ms": 305,
      "category": "ops"
    },
    {
      "name": "extraction_date_grounding",
      "status": "ok",
      "message": "Relative dates resolve against each source's observation date in fact extraction, dream synthesis, extract_atoms and propose_takes (the default). life chronicle events keep their current prompt unless extraction.date_grounding is set to true. Facts extracted before this was on keep their original wording; re-extract a source only with the user's consent (gbrain extract-conversation-facts --source-id <id> --dry-run previews it).",
      "elapsed_ms": 1,
      "category": "brain"
    },
    {
      "name": "integrity",
      "status": "ok",
      "message": "Sampled 0 pages; no bare-tweet phrases or external links.",
      "elapsed_ms": 9,
      "category": "brain"
    },
    {
      "name": "jsonb_integrity",
      "status": "ok",
      "message": "All JSONB columns store objects/arrays",
      "elapsed_ms": 41,
      "category": "brain"
    },
    {
      "name": "takes_weight_grid",
      "status": "ok",
      "message": "No takes yet",
      "elapsed_ms": 41,
      "category": "brain"
    },
    {
      "name": "child_table_orphans",
      "status": "ok",
      "message": "All FK-child tables clean (10 tables checked)",
      "elapsed_ms": 41,
      "category": "brain"
    },
    {
      "name": "raw_provenance",
      "status": "ok",
      "message": "All synthesized pages carry a raw trace or explicit exemption",
      "elapsed_ms": 41,
      "category": "brain"
    },
    {
      "name": "source_config_shape",
      "status": "ok",
      "message": "All source config values are JSON objects",
      "elapsed_ms": 41,
      "category": "brain"
    },
    {
      "name": "whoknows_health",
      "status": "ok",
      "message": "whoknows eval fixture present (10 queries). Run `gbrain eval whoknows test/fixtures/whoknows-eval.jsonl` to grade.",
      "elapsed_ms": 3,
      "category": "skill"
    },
    {
      "name": "cross_modal_modality_backfill",
      "status": "ok",
      "message": "All image-asset chunks have modality=image",
      "elapsed_ms": 4,
      "category": "brain"
    },
    {
      "name": "unified_multimodal_coverage",
      "status": "ok",
      "message": "search.unified_multimodal is off; coverage check N/A",
      "elapsed_ms": 4,
      "category": "brain"
    },
    {
      "name": "markdown_body_completeness",
      "status": "ok",
      "message": "No truncated bodies detected",
      "elapsed_ms": 4,
      "category": "brain"
    },
    {
      "name": "oversized_pages",
      "status": "ok",
      "message": "No pages exceed 25165824 bytes (excluding embed_skip pages, which already took the accepted non-embeddable remediation)",
      "elapsed_ms": 9,
      "category": "brain"
    },
    {
      "name": "scraper_junk_pages",
      "status": "ok",
      "message": "No junk-pattern hits in 0 recent page(s) (use --content-audit for full scan)",
      "elapsed_ms": 9,
      "category": "brain"
    },
    {
      "name": "content_sanity_audit_recent",
      "status": "ok",
      "message": "No content-sanity events in last 7 days (audit JSONL is local to this host; share GBRAIN_AUDIT_DIR for multi-host visibility)",
      "elapsed_ms": 9,
      "category": "brain"
    },
    {
      "name": "quarantined_pages",
      "status": "ok",
      "message": "No quarantined pages",
      "elapsed_ms": 3,
      "category": "brain"
    },
    {
      "name": "flagged_pages",
      "status": "ok",
      "message": "No flagged pages",
      "elapsed_ms": 3,
      "category": "brain"
    },
    {
      "name": "unverified_extractions",
      "status": "ok",
      "message": "No stale unverified extraction stubs",
      "details": {
        "count": 0,
        "days": 7,
        "source_id": null
      },
      "elapsed_ms": 3,
      "category": "brain"
    },
    {
      "name": "frontmatter_integrity",
      "status": "ok",
      "message": "1 source(s) clean — no frontmatter issues",
      "elapsed_ms": 11,
      "category": "brain"
    },
    {
      "name": "frontmatter_repairable",
      "status": "ok",
      "details": {
        "repairable": 0,
        "source_ids": [],
        "sources": [],
        "partial": false,
        "unscanned": [],
        "docs": "docs/guides/repair.md#frontmatter"
      },
      "message": "No file has frontmatter gbrain repair frontmatter would fix.",
      "elapsed_ms": 11,
      "category": "brain"
    },
    {
      "name": "eval_capture",
      "status": "ok",
      "message": "No capture failures in the last 24h",
      "elapsed_ms": 2,
      "category": "meta"
    },
    {
      "name": "contradictions",
      "status": "ok",
      "message": "No probe runs in the last 7 days. Run `gbrain eval suspected-contradictions --query \"...\" --top-k 5` to populate.",
      "elapsed_ms": 1,
      "category": "brain"
    },
    {
      "name": "facts_extraction_health",
      "status": "ok",
      "message": "Automatic fact extraction not configured (keyless) — memory comes from agent-authored `## Facts` fences and the `remember` verb. One optional key enables automatic extraction (OpenAI or Anthropic).",
      "elapsed_ms": 28,
      "category": "brain"
    },
    {
      "name": "effective_date_health",
      "status": "ok",
      "message": "Sample of last 1000 pages clean (no fallback-with-parseable-fm-date, no future-dated, no pre-1990)",
      "elapsed_ms": 2,
      "category": "brain"
    },
    {
      "name": "salience_health",
      "status": "ok",
      "message": "Skipped (no pages have emotional_weight > 0; either fresh install or recompute hasn't run yet)",
      "elapsed_ms": 6,
      "category": "brain"
    },
    {
      "name": "queue_health",
      "status": "ok",
      "message": "PGLite: no jobs waiting for a worker.",
      "details": {
        "engine": "pglite",
        "depth": 0,
        "by_queue": {},
        "worker_alive": true
      },
      "elapsed_ms": 16,
      "category": "ops"
    },
    {
      "name": "subagent_capability",
      "status": "ok",
      "message": "Subagent tier resolves to default (claude-sonnet-4-6) — full tool-loop capability",
      "elapsed_ms": 16,
      "category": "ops"
    },
    {
      "name": "facts_health",
      "status": "ok",
      "message": "facts_health(default): 0 active, 0 today, 0 this week, 0 consolidated, top entities —",
      "elapsed_ms": 16,
      "category": "brain"
    },
    {
      "name": "global_maintenance_timeouts",
      "status": "ok",
      "message": "Brain-wide maintenance jobs are finishing within their deadline.",
      "elapsed_ms": 8,
      "category": "ops"
    },
    {
      "name": "global_maintenance_stalled",
      "status": "ok",
      "message": "Brain-wide maintenance has not run yet.",
      "details": {
        "code": "global_maintenance_stalled",
        "reason": "fresh",
        "last_global_at": null,
        "age_minutes": null,
        "warn_after_minutes": 180,
        "fail_after_minutes": 10080,
        "failed_jobs_since": 0,
        "last_failed_job": null,
        "phases": [],
        "resume_phase": null,
        "docs": "docs/guides/troubleshooting.md#global-maintenance-stalled"
      },
      "elapsed_ms": 7,
      "category": "ops"
    },
    {
      "name": "unattended_maintenance",
      "status": "ok",
      "message": "Free upkeep has not run on this brain yet; gbrain maintain --unattended runs it (no model calls, no page purge). Nothing deletes on its own.",
      "severity": "info",
      "readiness_state": "not_applicable",
      "details": {
        "state": "never",
        "runner": null,
        "last_run": null,
        "steps": 0,
        "next_due_at": null,
        "pending_purge_count": 0,
        "paid_phases_opt_in": [
          "extract_atoms",
          "synthesize_concepts",
          "propose_takes",
          "grade_takes",
          "calibration_profile",
          "edge_contradictions",
          "drift",
          "standing_questions",
          "chronicle",
          "facts_drain",
          "conversation_facts_backfill",
          "enrich_thin",
          "skillopt",
          "embed"
        ],
        "embed_spend_today_usd": null,
        "embed_daily_cap_usd": null
      },
      "elapsed_ms": 52,
      "category": "ops"
    },
    {
      "name": "transcript_archive_freshness",
      "status": "ok",
      "message": "Conversation archive is on; no readable sessions for claude-code, codex, openclaw, hermes, grok (gbrain transcripts archive status names each reader).",
      "severity": "info",
      "readiness_state": "not_applicable",
      "details": {
        "enabled": true,
        "enabled_by": "default",
        "reason": "on by default on a personal brain",
        "source_id": "conversations",
        "stale_days": 2,
        "behind": [],
        "held": [],
        "harnesses": [
          {
            "harness": "claude-code",
            "reader": "claude-code-files",
            "readable": false,
            "newest_session_day": null,
            "newest_archived_day": null
          },
          {
            "harness": "codex",
            "reader": "codex-files",
            "readable": false,
            "newest_session_day": null,
            "newest_archived_day": null
          },
          {
            "harness": "openclaw",
            "reader": "openclaw-files",
            "readable": false,
            "newest_session_day": null,
            "newest_archived_day": null
          },
          {
            "harness": "hermes",
            "reader": "hermes-files",
            "readable": false,
            "newest_session_day": null,
            "newest_archived_day": null
          },
          {
            "harness": "grok",
            "reader": "grok-files",
            "readable": false,
            "newest_session_day": null,
            "newest_archived_day": null
          },
          {
            "harness": "openclaw",
            "reader": "openclaw-gateway",
            "readable": false,
            "newest_session_day": null,
            "newest_archived_day": null
          }
        ],
        "docs": "docs/guides/conversation-archive.md#doctor"
      },
      "elapsed_ms": 19,
      "category": "brain"
    },
    {
      "name": "embed_backfill_stalled",
      "status": "ok",
      "message": "No automatic embed-backfill is repeating the same failure.",
      "elapsed_ms": 2,
      "category": "ops"
    },
    {
      "name": "content_drift_sweep",
      "status": "ok",
      "details": {
        "code": "content_drift_sweep",
        "scopes": [],
        "docs": "docs/guides/troubleshooting.md#content-drift-sweep"
      },
      "message": "The content-drift sweep has not run yet; it runs inside embed --stale and the embed jobs.",
      "elapsed_ms": 1,
      "category": "ops"
    },
    {
      "name": "connector_account_mismatch",
      "status": "ok",
      "message": "No connector source is waiting for its account to be repinned.",
      "elapsed_ms": 0,
      "category": "ops"
    },
    {
      "name": "legacy_job_authority",
      "status": "ok",
      "message": "No queued job predates submission authority.",
      "details": {
        "authorizable": {},
        "unsupported_ids": [],
        "unsupported": 0,
        "active_ids": [],
        "terminal_keyed": {},
        "live": 0,
        "authorizable_total": 0,
        "terminal_keyed_total": 0,
        "docs": "docs/guides/repair.md#legacy-job-authority",
        "queued_spend": {
          "by_basis": {},
          "long_waiting_ids": [],
          "long_waiting": 0
        }
      },
      "elapsed_ms": 29,
      "category": "ops"
    },
    {
      "name": "legacy_token_grant_shape",
      "status": "ok",
      "message": "Every active legacy token uses the unified grant columns. The permissions mirror for older gbrain binaries is kept until 2026-11-04.",
      "details": {
        "legacy_shape_count": 0,
        "convertible_count": 0,
        "malformed": [],
        "mirror_window_ends": "2026-11-04",
        "docs": "docs/mcp/ADMIN.md#legacy-token-grants"
      },
      "elapsed_ms": 1,
      "category": "ops"
    },
    {
      "name": "legacy_token_grant_drift",
      "status": "ok",
      "message": "No legacy token grant has drifted from its permissions mirror.",
      "details": {
        "drift": [],
        "mirror_window_ends": "2026-11-04",
        "docs": "docs/mcp/ADMIN.md#legacy-token-grants"
      },
      "elapsed_ms": 1,
      "category": "ops"
    },
    {
      "name": "legacy_token_null_scope",
      "status": "ok",
      "message": "Every active legacy token has explicit scopes.",
      "details": {
        "null_scope_count": 0,
        "tokens": [],
        "docs": "docs/mcp/ADMIN.md#tokens-without-scopes"
      },
      "elapsed_ms": 1,
      "category": "ops"
    },
    {
      "name": "grant_new_ops_available",
      "status": "ok",
      "message": "Every active client and token can call the operations its scopes allow.",
      "details": {
        "grants": [],
        "server_surface": "full",
        "docs": "docs/mcp/ADMIN.md#grants-that-cannot-reach-new-operations"
      },
      "elapsed_ms": 3,
      "category": "ops"
    },
    {
      "name": "unscoped_multi_user_token",
      "status": "ok",
      "message": "Not applicable: this brain serves one person (0 enabled member(s)), so every credential reads that person's own pages.",
      "severity": "info",
      "readiness_state": "not_applicable",
      "elapsed_ms": 1,
      "category": "ops"
    },
    {
      "name": "image_assets",
      "status": "ok",
      "message": "No image assets indexed yet",
      "elapsed_ms": 3,
      "category": "brain"
    },
    {
      "name": "ocr_health",
      "status": "ok",
      "message": "OCR not in use (or no images ingested with OCR opt-in)",
      "elapsed_ms": 3,
      "category": "brain"
    },
    {
      "name": "image_embedding_coverage",
      "status": "ok",
      "message": "No image pages indexed yet.",
      "details": {
        "image_pages": 0,
        "without_image_vector": 0,
        "null_source_path": 0,
        "unsupported_holds": 0,
        "multimodal": false
      },
      "elapsed_ms": 5,
      "category": "brain"
    },
    {
      "name": "sync_freshness",
      "status": "ok",
      "message": "1 writer-owned canonical content source(s): upstream sync is not applicable; see canonical_content_writes for publication status.",
      "details": {
        "unchanged_count": 0,
        "synced_recently_count": 0,
        "stale_count": 0,
        "writer_owned_count": 1
      },
      "elapsed_ms": 48,
      "category": "brain"
    },
    {
      "name": "canonical_content_writes",
      "status": "ok",
      "message": "1 writer-owned content source(s); no pending canonical publication or recovery.",
      "details": {
        "writer_owned_count": 1,
        "pending_count": 0,
        "recovering_count": 0
      },
      "elapsed_ms": 48,
      "category": "ops"
    },
    {
      "name": "backup_coverage",
      "status": "ok",
      "message": "Not urgent yet: the brain holds 0 page(s)+fact(s) and is under 7 days old (backup coaching starts at 25 items or 7 days). 1 knowledge asset(s) lack verified recovery: default (not_a_git_repo). A source repo with a pushed git remote restores its Markdown files only, never DB-only pages, facts, config or credentials. Run `gbrain backup status` for each asset's fix command.",
      "severity": "info",
      "readiness_state": "degraded",
      "fix": {
        "argv": [
          "gbrain",
          "backup",
          "create",
          "--output",
          "<BACKUP_FILE>",
          "--brain",
          "host"
        ],
        "command": "gbrain backup create --output '<BACKUP_FILE>' --brain host",
        "consent": [],
        "actor": "agent",
        "next": "run",
        "why": "Writes a full snapshot of this PGLite brain (every source, page, fact, member, token and rule) to one archive outside the brain.",
        "verify": {
          "argv": [
            "gbrain",
            "doctor",
            "--only",
            "backup_coverage",
            "--json",
            "--brain",
            "host"
          ]
        },
        "docs": "https://github.com/garrytan/gbrain/blob/v0.60.753.0/docs/guides/in-agent-setup.md#6-back-up-the-complete-local-database",
        "requires_exclusive": false,
        "inputs": [
          {
            "name": "BACKUP_FILE",
            "how": "Ask the user for an absolute path to a new archive file, in an existing private directory outside the brain (ideally another disk)."
          }
        ]
      },
      "details": {
        "totals": {
          "assets": 1,
          "no_remote": 0,
          "unpushed": 0,
          "failing": 0,
          "configured_repos": 0,
          "recoverable_repos": 0,
          "remote_timeouts": 0,
          "pages_at_risk": 0
        },
        "checked_at": "2026-11-22T02:47:57.658Z",
        "computed_by": "doctor",
        "cache_age": "under an hour ago",
        "recovery_scope": "Git evidence covers committed repository files only; not a full database backup. DB-only pages, facts, configuration and credentials need a separate backup and restore drill.",
        "degraded": false
      },
      "elapsed_ms": 48,
      "category": "ops"
    },
    {
      "name": "sync_consolidation",
      "status": "ok",
      "message": "Single-source brain — sync --all consolidation not applicable.",
      "elapsed_ms": 48,
      "category": "ops"
    },
    {
      "name": "cycle_freshness",
      "status": "ok",
      "message": "No full cycle yet for 'default': it holds no pages or only pages from the last 24h, so there is nothing to consolidate yet.",
      "severity": "info",
      "readiness_state": "not_applicable",
      "elapsed_ms": 48,
      "category": "brain"
    },
    {
      "name": "content_hash_duplicates",
      "status": "ok",
      "message": "No same-source content-hash duplicate groups",
      "elapsed_ms": 48,
      "category": "brain"
    },
    {
      "name": "code_chunk_metadata",
      "status": "ok",
      "message": "All code-page chunks carry symbol metadata",
      "elapsed_ms": 48,
      "category": "brain"
    },
    {
      "name": "undeclared_db_only_pages",
      "status": "ok",
      "message": "Every DB page is file-backed or under a declared/default db_only path (derive-phase defaults: life/events/ atoms/ concepts/ extracts/ dream-cycle-summaries/ reports/drift-).",
      "elapsed_ms": 48,
      "category": "brain"
    },
    {
      "name": "db_only_collector_collision",
      "status": "ok",
      "message": "No configured collectors declare output paths",
      "elapsed_ms": 48,
      "category": "ops"
    },
    {
      "name": "managed_sync_latency",
      "status": "ok",
      "details": {
        "graded": false,
        "on_commit": false,
        "target_seconds": 300,
        "fail_seconds": 3600,
        "sources": [
          {
            "source_id": "default",
            "window_hours": 24,
            "commit_to_searchable": {
              "samples": 0,
              "p50_seconds": null,
              "p95_seconds": null
            },
            "commit_to_embedded": {
              "samples": 0,
              "p50_seconds": null,
              "p95_seconds": null,
              "pending": 0
            },
            "commits": 0,
            "unresolved_commits": 0,
            "waiting_commits": null,
            "behind": null
          }
        ],
        "docs": "docs/guides/on-commit-sync.md"
      },
      "message": "No commit→searchable samples in the last 24 h (no managed sync imported a new commit).",
      "elapsed_ms": 11,
      "category": "brain"
    },
    {
      "name": "commit_notifier",
      "status": "ok",
      "severity": "info",
      "details": {
        "sync_on_commit": false,
        "docs": "docs/guides/on-commit-sync.md",
        "sources": [
          {
            "source_id": "default",
            "resident": null,
            "state": null,
            "reason": null,
            "stalled": false,
            "pending_markers": 0
          }
        ]
      },
      "message": "sync.on_commit is off; residents still run explicit sync requests. notifier for default: none running; idle.",
      "elapsed_ms": 5,
      "category": "brain"
    },
    {
      "name": "tracked_ownership_marker",
      "status": "ok",
      "details": {
        "checkouts": 0,
        "tracked": []
      },
      "message": "0 Git checkout(s) track no ownership marker (markers on disk stay untracked and are denied on push).",
      "elapsed_ms": 11,
      "category": "brain"
    },
    {
      "name": "foreign_writers",
      "status": "ok",
      "message": "Not applicable: no registered source on this host is a Git checkout, so there are no commits to attribute (the database is the record on a repo-less brain).",
      "severity": "info",
      "readiness_state": "not_applicable",
      "elapsed_ms": 6,
      "category": "brain"
    },
    {
      "name": "decide_health",
      "status": "ok",
      "message": "System One is off (every decide slot is off; nothing is sent).",
      "elapsed_ms": 10,
      "category": "ops"
    },
    {
      "name": "memory_proposals_pending",
      "status": "ok",
      "message": "No memory proposals await the owner.",
      "elapsed_ms": 2,
      "category": "brain"
    },
    {
      "name": "unlinked_facts",
      "status": "ok",
      "message": "No active facts yet; nothing to link.",
      "details": {
        "sources": 1,
        "conversation": null,
        "window": {
          "active": 0,
          "unlinked": 0,
          "fence_owned": 0,
          "conversation": 0,
          "capped": false
        },
        "new_7d": {
          "facts": 0,
          "unlinked": 0,
          "no_subject": 0,
          "conversation_unresolved": 0
        },
        "no_subject": 0,
        "origins": [],
        "inferred_7d": {
          "page": 0,
          "mention": 0
        },
        "relinked_7d": {},
        "fix": "preview links: gbrain facts relink --dry-run"
      },
      "elapsed_ms": 13,
      "category": "brain"
    },
    {
      "name": "edge_validity",
      "status": "ok",
      "message": "relationships: none yet; read policy on; contradiction mode propose (default)",
      "details": {
        "read_policy": "on",
        "contradiction_mode": "propose (default)",
        "relationships": {},
        "lagging": 0,
        "stale_assertions": [],
        "proposals": {
          "proposed": 0,
          "undated": 0,
          "applied": 0
        }
      },
      "elapsed_ms": 15,
      "category": "brain"
    },
    {
      "name": "auto_chronicle",
      "status": "ok",
      "readiness_state": "missing",
      "message": "auto_chronicle is on (default). Last 24 h: 0 of 200 automatic extraction calls. Last 7 days: 0 extracted, 0 failed, 0 skipped; $0.00 known spend. 0 page(s) pending. No chat provider is configured, so nothing will be extracted until one is.",
      "details": {
        "enabled": true,
        "source": "default",
        "daily_limit": 200,
        "job_budget_usd": 0.25,
        "ledger_available": true,
        "pending": 0,
        "auto_calls_24h": 0,
        "principals_24h": [],
        "last_7d": {
          "extracted": 0,
          "failed": 0,
          "skipped": 0,
          "reasons": {},
          "failedReasons": {}
        },
        "spend_7d": {
          "knownUsd": 0,
          "unpricedCalls": 0,
          "incompleteRecords": 0
        },
        "chat_available": false,
        "run_now": [
          "gbrain",
          "dream",
          "--phase",
          "chronicle"
        ],
        "severity": "info",
        "readiness": "missing",
        "docs": "docs/guides/life-chronicle.md"
      },
      "elapsed_ms": 9,
      "category": "brain"
    },
    {
      "name": "chronicle_config_invalid",
      "status": "ok",
      "message": "chronicle.* settings are valid.",
      "elapsed_ms": 9,
      "category": "brain"
    },
    {
      "name": "chronicle_duplicate_events",
      "status": "ok",
      "message": "No page holds live events from an earlier extraction run beside its newest one.",
      "elapsed_ms": 9,
      "category": "brain"
    },
    {
      "name": "auto_chronicle_default_on",
      "status": "ok",
      "message": "Automatic event extraction is on by default and the user has not confirmed it yet. Each eligible new or changed meeting, conversation or calendar page gets one paid chat call (cap $0.25 per page; at most 200 calls per day, so at most $50.00 per day for a priced model; an unpriced model has no cap), and page text goes to the configured chat provider. Relay this to the user, then run `gbrain config set auto_chronicle true` to keep it or `gbrain config set auto_chronicle false` to opt out.",
      "severity": "info",
      "readiness_state": "ok",
      "fix": {
        "argv": [
          "gbrain",
          "config",
          "set",
          "auto_chronicle",
          "true",
          "--brain",
          "host"
        ],
        "command": "gbrain config set auto_chronicle true --brain host",
        "consent": [
          "paid",
          "egress"
        ],
        "actor": "agent",
        "next": "ask_user",
        "why": "Keeping automatic extraction records that the user accepted one paid chat call per eligible page; page text goes to the chat provider.",
        "user_message": "Automatic event extraction is on: each new or changed meeting, conversation or calendar page gets one paid chat call. Keep it on, or turn it off?",
        "verify": {
          "argv": [
            "gbrain",
            "doctor",
            "--only",
            "auto_chronicle_default_on",
            "--json",
            "--brain",
            "host"
          ]
        },
        "requires_exclusive": false
      },
      "details": {
        "code": "auto_chronicle_default_on",
        "severity": "info",
        "ask_user": true,
        "docs": "docs/guides/life-chronicle.md",
        "fix": {
          "argv": [
            "gbrain",
            "config",
            "set",
            "auto_chronicle",
            "true"
          ],
          "consent": [
            "paid",
            "egress"
          ],
          "actor": "agent",
          "requires_exclusive": false,
          "why": "Keeping automatic extraction records that the user accepted one paid chat call per eligible page; page text goes to the chat provider.",
          "user_message": "Automatic event extraction is on: each new or changed meeting, conversation or calendar page gets one paid chat call. Keep it on, or turn it off?",
          "verify": {
            "argv": [
              "gbrain",
              "doctor",
              "--only",
              "auto_chronicle_default_on",
              "--json"
            ]
          }
        },
        "decisions": [
          {
            "id": "keep",
            "label": "Keep automatic extraction on",
            "argv": [
              "gbrain",
              "config",
              "set",
              "auto_chronicle",
              "true"
            ],
            "fix": {
              "argv": [
                "gbrain",
                "config",
                "set",
                "auto_chronicle",
                "true"
              ],
              "consent": [
                "paid",
                "egress"
              ],
              "actor": "agent",
              "requires_exclusive": false,
              "why": "Keeping automatic extraction records that the user accepted one paid chat call per eligible page; page text goes to the chat provider.",
              "user_message": "Automatic event extraction is on: each new or changed meeting, conversation or calendar page gets one paid chat call. Keep it on, or turn it off?",
              "verify": {
                "argv": [
                  "gbrain",
                  "doctor",
                  "--only",
                  "auto_chronicle_default_on",
                  "--json"
                ]
              }
            }
          },
          {
            "id": "opt_out",
            "label": "Turn automatic extraction off",
            "argv": [
              "gbrain",
              "config",
              "set",
              "auto_chronicle",
              "false"
            ],
            "fix": {
              "argv": [
                "gbrain",
                "config",
                "set",
                "auto_chronicle",
                "false"
              ],
              "consent": [],
              "actor": "agent",
              "requires_exclusive": false,
              "why": "Turns automatic extraction off; history stays available on request with chronicle-backfill.",
              "verify": {
                "argv": [
                  "gbrain",
                  "doctor",
                  "--only",
                  "auto_chronicle_default_on",
                  "--json"
                ]
              }
            }
          }
        ],
        "default": "keep"
      },
      "elapsed_ms": 9,
      "category": "brain"
    },
    {
      "name": "facts_drain",
      "status": "ok",
      "message": "No facts-absorb jobs are queued (no run recorded yet).",
      "details": {
        "health": "idle",
        "backlog": {
          "waiting": 0,
          "delayed": 0,
          "active": 0
        },
        "last_run": null,
        "daily_spent_usd": 0,
        "enabled": true,
        "budget_usd": 1,
        "daily_budget_usd": 5,
        "max_jobs": 50,
        "docs": "docs/guides/facts-drain.md"
      },
      "elapsed_ms": 2,
      "category": "brain"
    },
    {
      "name": "wakeshift",
      "status": "ok",
      "severity": "info",
      "readiness_state": "disabled_by_choice",
      "message": "Reporting back through Wakeshift is off (gbrain wakeshift enable turns it on).",
      "details": {
        "enabled": false,
        "key_source": "none",
        "docs": "docs/guides/wakeshift.md#troubleshooting"
      },
      "elapsed_ms": 2,
      "category": "ops"
    },
    {
      "name": "fact_take_vectors",
      "status": "ok",
      "message": "Not applicable: embeddings are disabled on this brain (keyword search keeps working).",
      "details": {
        "applicable": false
      },
      "severity": "info",
      "readiness_state": "disabled_by_choice",
      "elapsed_ms": 1,
      "category": "brain"
    },
    {
      "name": "planner_stats_stale",
      "status": "ok",
      "message": "Planner statistics are fresh on 6 hot tables.",
      "details": {
        "engine": "pglite",
        "auto_analyze": true,
        "checked": [
          "pages",
          "links",
          "facts",
          "takes",
          "content_chunks",
          "timeline_entries"
        ],
        "stale": [],
        "missing_search_statistics": [],
        "expression_indexes_without_statistics": [],
        "fix": "gbrain repair planner-stats --apply"
      },
      "elapsed_ms": 9,
      "category": "ops"
    },
    {
      "name": "retrieval_feedback_health",
      "status": "ok",
      "details": {
        "enabled": false,
        "learn": true,
        "influence": 0.1,
        "implicit": false,
        "answers_recorded": 0,
        "ratings_explicit": 0,
        "ratings_cited": 0,
        "weights": 0,
        "weights_off_neutral": 0,
        "last_rating_at": null,
        "top_client_share_7d": null,
        "docs": "docs/guides/retrieval-feedback.md"
      },
      "message": "Retrieval feedback is off; rankings do not learn from ratings. Turn it on with: gbrain config set feedback.enabled true",
      "elapsed_ms": 5,
      "category": "meta"
    },
    {
      "name": "revision_backfill",
      "status": "ok",
      "details": {
        "column": "not_null",
        "pending": 0,
        "failed": []
      },
      "message": "Every page has its revision; the page revision backfill is complete.",
      "elapsed_ms": 2,
      "category": "meta"
    },
    {
      "name": "belief_ledger_coverage",
      "status": "ok",
      "message": "The belief ledger is off: no source records what this brain had recorded, and when.",
      "severity": "info",
      "readiness_state": "disabled_by_choice",
      "fix": {
        "argv": [
          "gbrain",
          "beliefs",
          "enable",
          "--source",
          "default",
          "--brain",
          "host"
        ],
        "command": "gbrain beliefs enable --source default --brain host",
        "consent": [],
        "actor": "agent",
        "next": "ask_user",
        "why": "Enabling baselines every page of the source and records each later change; only a managed source is certified.",
        "user_message": "Do you want gbrain to keep a belief ledger (a recorded history of facts, takes and links) for this source?",
        "verify": {
          "argv": [
            "gbrain",
            "doctor",
            "--only",
            "belief_ledger_coverage",
            "--json",
            "--brain",
            "host"
          ]
        },
        "docs": "https://github.com/garrytan/gbrain/blob/v0.60.753.0/docs/designs/BELIEF_LEDGER.md#73-the-doctor-coverage-check",
        "requires_exclusive": false
      },
      "elapsed_ms": 3,
      "category": "brain"
    },
    {
      "name": "trust_tiers",
      "status": "ok",
      "details": {
        "rows": 0,
        "by_tier": {
          "user_confirmed": 0,
          "operator_curated": 0,
          "tool_observed": 0,
          "agent_written": 0,
          "unknown": 0,
          "external_untrusted": 0
        },
        "unknown_pct": 0,
        "tables": [
          {
            "table": "pages",
            "rows": 0,
            "by_tier": {
              "user_confirmed": 0,
              "operator_curated": 0,
              "tool_observed": 0,
              "agent_written": 0,
              "unknown": 0,
              "external_untrusted": 0
            }
          },
          {
            "table": "facts",
            "rows": 0,
            "by_tier": {
              "user_confirmed": 0,
              "operator_curated": 0,
              "tool_observed": 0,
              "agent_written": 0,
              "unknown": 0,
              "external_untrusted": 0
            }
          },
          {
            "table": "takes",
            "rows": 0,
            "by_tier": {
              "user_confirmed": 0,
              "operator_curated": 0,
              "tool_observed": 0,
              "agent_written": 0,
              "unknown": 0,
              "external_untrusted": 0
            }
          },
          {
            "table": "timeline_entries",
            "rows": 0,
            "by_tier": {
              "user_confirmed": 0,
              "operator_curated": 0,
              "tool_observed": 0,
              "agent_written": 0,
              "unknown": 0,
              "external_untrusted": 0
            }
          }
        ],
        "backfill": {
          "interrupted": false,
          "completed_at": "2026-11-22T02:39:22.928Z"
        },
        "derived": {
          "rows": 0,
          "external_untrusted": 0,
          "external_pct": 0
        },
        "unknown_pages": 0
      },
      "message": "No facts, takes, timeline entries or pages yet.",
      "elapsed_ms": 8,
      "category": "brain"
    },
    {
      "name": "provenance_stamp_drift",
      "status": "ok",
      "details": {
        "docs": "docs/guides/repair.md#provenance",
        "truncated": false,
        "sources": []
      },
      "message": "No page has provenance stamps or a trust marker that another writer removed.",
      "elapsed_ms": 15,
      "category": "brain"
    },
    {
      "name": "trust_scan",
      "status": "ok",
      "details": {
        "detector_version": 2,
        "unscanned": {
          "pages": 0,
          "facts": 0,
          "takes": 0,
          "timeline_entries": 0
        },
        "total_unscanned": 0,
        "completed_at": null
      },
      "message": "Every agent-written or lower row has been scanned by the current write-gate detector; flagged rows carry their flag, and proactive surfaces withhold them when trust.agent_activation is suppress.",
      "elapsed_ms": 5,
      "category": "brain"
    },
    {
      "name": "trust_sources_unclaimed",
      "status": "ok",
      "details": {
        "unclaimed": [],
        "pending": [],
        "legacy_unknown": 0
      },
      "message": "No unclaimed source holds rows from before trust tiers.",
      "elapsed_ms": 213,
      "category": "brain"
    },
    {
      "name": "trust_release_unpreviewed_fields",
      "status": "ok",
      "details": {
        "total": 0,
        "items": []
      },
      "message": "No released fact was confirmed with fence-row fields its release preview did not show.",
      "elapsed_ms": 3,
      "category": "brain"
    },
    {
      "name": "core_memory",
      "status": "ok",
      "message": "Core memory is off (opt-in). If the user wants a profile loaded in every session: gbrain config set memory.core.enabled true, then gbrain core init.",
      "details": {
        "pages": 0,
        "chars_used": 0,
        "chars_limit": 4000,
        "enabled": false,
        "bad_config": [],
        "compiled": [],
        "docs": "docs/guides/core-memory.md"
      },
      "elapsed_ms": 5,
      "category": "brain"
    },
    {
      "name": "two_consumers_on_host",
      "status": "ok",
      "message": "PGLite admits one process; no consumer heartbeat rows are kept.",
      "details": {
        "count": 0,
        "consumers": [],
        "docs": "docs/guides/troubleshooting.md#two-consumers-on-host"
      },
      "elapsed_ms": 2,
      "category": "ops"
    },
    {
      "name": "consumers_without_heartbeat",
      "status": "ok",
      "message": "PGLite admits one process; no consumer heartbeat rows are kept.",
      "details": {
        "count": 0,
        "owners": [],
        "docs": "docs/guides/troubleshooting.md#two-consumers-on-host"
      },
      "elapsed_ms": 2,
      "category": "ops"
    },
    {
      "name": "host_identity_mismatch",
      "status": "ok",
      "details": {
        "count": 0,
        "host_id": "19cbe0ec-62ad-4230-baf2-ac388ef37edc",
        "host_json_path": "/home/codespace/.gbrain/persistence/host.json",
        "mismatches": [],
        "docs": "docs/guides/troubleshooting.md#host-identity-mismatch"
      },
      "message": "This process's host identity (/home/codespace/.gbrain/persistence/host.json) owns every binding this filesystem holds.",
      "elapsed_ms": 2,
      "category": "ops"
    },
    {
      "name": "session_lane_budget",
      "status": "ok",
      "severity": "info",
      "readiness_state": "not_applicable",
      "details": {
        "docs": "docs/ENGINES.md#pool-sizing"
      },
      "message": "Not applicable: PGLite has no connection pool to share.",
      "elapsed_ms": 0,
      "category": "ops"
    },
    {
      "name": "runtime_build_skew",
      "status": "ok",
      "details": {
        "count": 0,
        "newest": null,
        "builds": [],
        "processes": [],
        "stale": [],
        "job_children": [],
        "earlier_job_children": 0,
        "unknown_builds": [],
        "docs": "docs/guides/troubleshooting.md#runtime-build-skew"
      },
      "message": "No long-running gbrain process (serve, jobs supervisor, worker) is running on this host.",
      "elapsed_ms": 2,
      "category": "ops"
    },
    {
      "name": "cli_socket_refusals",
      "status": "ok",
      "details": {
        "refusals": 0,
        "docs": "docs/guides/cli-socket.md"
      },
      "message": "The warm CLI socket refused no CLI call in the last 24 hours.",
      "elapsed_ms": 0,
      "category": "ops"
    },
    {
      "name": "extract_atoms_held_failed",
      "status": "ok",
      "message": "No managed atom page or transcript is held after repeated extraction failures.",
      "details": {
        "held": 0,
        "items": [],
        "code": "held_failed"
      },
      "elapsed_ms": 3,
      "category": "brain"
    },
    {
      "name": "conversation_detection_ambiguous",
      "status": "ok",
      "message": "No conversation page is held for an undetected format.",
      "details": {
        "pages": 0,
        "samples": []
      },
      "elapsed_ms": 4,
      "category": "brain"
    },
    {
      "name": "extraction_input_truncated",
      "status": "ok",
      "message": "Every page extraction read all of its input (no head-only, tail-window or size-skip receipts).",
      "details": {
        "groups": []
      },
      "elapsed_ms": 4,
      "category": "brain"
    },
    {
      "name": "derivation_unpriced_model",
      "status": "ok",
      "message": "No segmented page derivation is held back by a model without a price.",
      "details": {
        "models": []
      },
      "elapsed_ms": 4,
      "category": "brain"
    },
    {
      "name": "ghost_pages",
      "status": "ok",
      "details": {
        "count": 0,
        "by_source": [
          {
            "source_id": "default",
            "count": 0,
            "status": "known"
          }
        ],
        "samples": [],
        "inspected": 0,
        "truncated": false,
        "exact": true,
        "docs": "docs/guides/repair.md#ghost-pages"
      },
      "message": "No live page is missing its canonical file (0 page(s) inspected).",
      "elapsed_ms": 4,
      "category": "brain"
    },
    {
      "name": "origin_twins",
      "status": "ok",
      "details": {
        "index": "present",
        "docs": "docs/guides/repair.md#origin-twins"
      },
      "message": "pages_live_origin_key is present: no two live pages can record one file.",
      "elapsed_ms": 1,
      "category": "brain"
    },
    {
      "name": "slug_path_mismatch",
      "status": "ok",
      "details": {
        "count": 0,
        "files": {
          "stamped": 0,
          "unstamped": 0,
          "file_missing": 0,
          "no_checkout": 0,
          "not_read": 0
        },
        "inspected": 0,
        "truncated": false,
        "scan_limit": 20000,
        "file_limit": 200,
        "docs": "docs/guides/repair.md#slug-path-mismatch",
        "samples": []
      },
      "message": "Every live page's slug is the one its recorded file path derives (0 candidate(s) inspected).",
      "elapsed_ms": 5,
      "category": "brain"
    },
    {
      "name": "rename_identity_downgrades",
      "status": "ok",
      "details": {
        "count": 0,
        "by_source": [],
        "samples": [],
        "docs": "docs/guides/live-sync.md#renaming-a-page"
      },
      "message": "No rename that lost its page identity is waiting for a disposition.",
      "elapsed_ms": 4,
      "category": "brain"
    },
    {
      "name": "purge_parked_pages",
      "status": "ok",
      "message": "No soft-deleted page is parked by the managed purge.",
      "details": {
        "parked": 0
      },
      "elapsed_ms": 1,
      "category": "brain"
    },
    {
      "name": "derived_origin_parked",
      "status": "ok",
      "message": "No soft-deleted page is kept from the purge to keep a page derived from it private.",
      "details": {
        "parked": 0,
        "origins": []
      },
      "elapsed_ms": 2,
      "category": "brain"
    },
    {
      "name": "purge_mirror",
      "status": "ok",
      "message": "No purge in the last 30 days to check against the purge mirror at /home/codespace/.gbrain/purge-events.jsonl.",
      "details": {
        "path": "/home/codespace/.gbrain/purge-events.jsonl",
        "recent": 0,
        "missing": 0
      },
      "elapsed_ms": 2,
      "category": "brain"
    },
    {
      "name": "derivation_purge_sweeps",
      "status": "ok",
      "message": "No fact purge has a sweep of stored derivation results pending or stalled.",
      "details": {
        "sweeps": 0
      },
      "elapsed_ms": 3,
      "category": "brain"
    },
    {
      "name": "missing_recorded_files",
      "status": "ok",
      "severity": "info",
      "readiness_state": "not_applicable",
      "details": {
        "count": 0,
        "sources": [],
        "docs": "docs/storage-tiering.md#restoring-a-page-whose-file-is-gone"
      },
      "message": "Not applicable: no source is a classic checkout on this host (managed sources are checked by ghost_pages).",
      "elapsed_ms": 1,
      "category": "brain"
    },
    {
      "name": "unindexed_files",
      "status": "ok",
      "message": "Unindexed files are not known for default (not computed yet). The maintenance phase unindexed_files computes them on each run and continues an incomplete scan; to compute them now, run gbrain sources retry-held <id> --unindexed.",
      "severity": "info",
      "readiness_state": "unknown",
      "fix": {
        "argv": [
          "gbrain",
          "sources",
          "retry-held",
          "default",
          "--unindexed",
          "--brain",
          "host"
        ],
        "command": "gbrain sources retry-held default --unindexed --brain host",
        "consent": [],
        "actor": "agent",
        "next": "run",
        "why": "Finds the committed files of default with no page and no hold (bounded; it continues an incomplete scan), schedules them for a re-screen and stores the result this check reads.",
        "verify": {
          "argv": [
            "gbrain",
            "doctor",
            "--only",
            "unindexed_files",
            "--json",
            "--brain",
            "host"
          ]
        },
        "docs": "https://github.com/garrytan/gbrain/blob/v0.60.753.0/docs/guides/repair.md#unindexed-files",
        "requires_exclusive": false,
        "then": {
          "argv": [
            "gbrain",
            "sync",
            "--source",
            "default",
            "--no-pull",
            "--brain",
            "host"
          ],
          "command": "gbrain sync --source default --no-pull --brain host",
          "consent": [],
          "actor": "agent",
          "next": "run",
          "why": "The sync re-screens the scheduled files of default: each one that passes imports, each one that refuses is recorded as a hold that gbrain sources status default lists.",
          "verify": {
            "argv": [
              "gbrain",
              "doctor",
              "--only",
              "unindexed_files",
              "--json",
              "--brain",
              "host"
            ]
          },
          "docs": "https://github.com/garrytan/gbrain/blob/v0.60.753.0/docs/guides/repair.md#unindexed-files",
          "requires_exclusive": false
        }
      },
      "details": {
        "docs": "docs/guides/repair.md#unindexed-files",
        "sources": [
          {
            "source_id": "default",
            "state": "missing"
          }
        ]
      },
      "elapsed_ms": 4,
      "category": "brain"
    },
    {
      "name": "sync_overwritten_db_edits",
      "status": "ok",
      "details": {
        "count": 0,
        "unknown": 0,
        "truncated": false,
        "docs": "docs/guides/repair.md#overwritten-edits",
        "sources": []
      },
      "message": "No page shows a database edit that a sync import overwrote.",
      "elapsed_ms": 7,
      "category": "brain"
    },
    {
      "name": "sync_rows_behind_checkpoint",
      "status": "ok",
      "message": "Not applicable: no managed source has a checkout and a sync checkpoint here (a repo-less brain keeps its pages in the database, which is the record).",
      "severity": "info",
      "readiness_state": "not_applicable",
      "details": {
        "count": 0,
        "unproven": 0,
        "docs": "docs/guides/repair.md#rows-behind",
        "timeout_ms": 10000,
        "sources": [
          {
            "source_id": "default",
            "status": "not_applicable",
            "reason": "no_checkpoint",
            "checkpoint": null,
            "complete": true,
            "stopped_at": null,
            "pages": 0,
            "behind": 0,
            "unproven": 0,
            "counts": {},
            "samples": [],
            "unproven_samples": []
          }
        ],
        "reasons": [
          "no_checkpoint"
        ]
      },
      "elapsed_ms": 4,
      "category": "brain"
    },
    {
      "name": "sync_config_keys",
      "status": "ok",
      "message": "No retired sync config key is stored on this brain.",
      "details": {
        "unapplied": [],
        "rollback": []
      },
      "elapsed_ms": 2,
      "category": "meta"
    },
    {
      "name": "person_title_duplicates",
      "status": "ok",
      "message": "No title-prefixed person page pairs with an unprefixed page (0 titled page(s) examined).",
      "details": {
        "scanned": 0,
        "capped": false,
        "pairs": []
      },
      "elapsed_ms": 5,
      "category": "brain"
    },
    {
      "name": "entity_duplicates",
      "status": "ok",
      "message": "No likely duplicate person or company pages.",
      "details": {
        "counts": {
          "by_kind": {
            "cross_source": 0,
            "in_source": 0,
            "conflict": 0,
            "thin": 0
          },
          "by_class": {
            "clean": 0,
            "likely": 0,
            "weak": 0,
            "thin": 0,
            "conflict": 0
          },
          "crowded_key_values": 0
        },
        "groups": []
      },
      "elapsed_ms": 20,
      "category": "brain"
    },
    {
      "name": "local_edit_adoptions",
      "status": "ok",
      "details": {
        "sources": [],
        "docs": "docs/guides/write-refusals.md#file_database_drift"
      },
      "message": "No local edit was adopted in the last 24 h.",
      "elapsed_ms": 2,
      "category": "brain"
    },
    {
      "name": "outside_content_fences",
      "status": "ok",
      "details": {
        "pages": 0,
        "items": [],
        "docs": "docs/guides/repair.md#outside-content-fences"
      },
      "message": "No fact, take or link is indexed from a fence on an imported email, calendar, GitHub or transcript page.",
      "elapsed_ms": 15,
      "category": "brain"
    },
    {
      "name": "embedding_plane_disagreement",
      "status": "ok",
      "message": "The config file disables embeddings and the database holds no vectors.",
      "details": {
        "file_disabled": true,
        "database_disabled": false,
        "vector_tables": [],
        "docs": "docs/guides/troubleshooting.md#embedding-plane-disagreement"
      },
      "elapsed_ms": 10,
      "category": "brain"
    },
    {
      "name": "mcp_request_log_retention",
      "status": "ok",
      "severity": "info",
      "readiness_state": "disabled_by_choice",
      "details": {
        "retention_days": null,
        "rows": 0,
        "rows_exact": true,
        "bytes": 32768,
        "docs": "docs/mcp/ADMIN.md#request-log-retention"
      },
      "fix": {
        "argv": [
          "gbrain",
          "config",
          "set",
          "cycle.purge.mcp_request_log_retention_days",
          "90",
          "--brain",
          "host"
        ],
        "command": "gbrain config set cycle.purge.mcp_request_log_retention_days 90 --brain host",
        "consent": [
          "destructive"
        ],
        "actor": "agent",
        "next": "ask_user",
        "why": "Turns on the request-log prune: the next cycle purge phase (or, on a PGLite brain, a live serve within the hour) deletes request rows older than 90 days. Per-client lifetime totals and the audit rows (surface, memory-setting and access changes) are kept.",
        "user_message": "Your MCP request log holds 0 row(s) (0.0 MB) and nothing prunes it. Turn on 90-day retention? Request details older than 90 days (operation, status, parameters, errors) will be deleted and cannot be restored; per-client totals and audit rows are kept.",
        "verify": {
          "argv": [
            "gbrain",
            "doctor",
            "--only",
            "mcp_request_log_retention",
            "--json",
            "--brain",
            "host"
          ]
        },
        "docs": "https://github.com/garrytan/gbrain/blob/v0.60.753.0/docs/mcp/ADMIN.md#request-log-retention",
        "requires_exclusive": false
      },
      "message": "The MCP request log holds 0 row(s) (0.0 MB); request-log retention is off, so it keeps every request.",
      "elapsed_ms": 3,
      "category": "ops"
    },
    {
      "name": "storage_manifest",
      "status": "ok",
      "message": "No storage shelf and no interim storage records on this brain.",
      "severity": "info",
      "readiness_state": "not_applicable",
      "details": {
        "docs": "docs/guides/storage-manifest.md#doctor"
      },
      "elapsed_ms": 4,
      "category": "brain"
    },
    {
      "name": "facts_undated_lines",
      "status": "ok",
      "message": "Every fact line on 0 facts page(s) carries a date.",
      "elapsed_ms": 1,
      "category": "brain"
    },
    {
      "name": "secret_store",
      "status": "ok",
      "details": {
        "entries": 0,
        "occurrences": 0,
        "unreferenced": 0,
        "by_rule": {},
        "spooled": 0,
        "docs": "docs/guides/secret-store.md#health-and-backups",
        "keys": {
          "origin": "none",
          "current": null,
          "present": [],
          "in_use": [],
          "missing": [],
          "escrow_exported": []
        },
        "backup": {
          "backend": false,
          "last_success": null,
          "last_failure": null,
          "carried_by": "database_backup"
        },
        "checkouts": []
      },
      "message": "The secret store holds no entries.",
      "elapsed_ms": 12,
      "category": "brain"
    },
    {
      "name": "owner_identity",
      "status": "ok",
      "details": {
        "owner_member_set": false,
        "identifiers": 0,
        "identifier_kinds": [],
        "entity_basis": "reserved_page",
        "identifier_shared": 0,
        "several_pages": false,
        "unbound_google_sources": 0,
        "person_types_unavailable": false
      },
      "message": "No owner identifier yet: set the owner member's email (gbrain access member set <id> --email <addr>) or connect a Google source. The owner page is memory/owner.",
      "elapsed_ms": 15,
      "category": "ops"
    },
    {
      "name": "fence_integrity",
      "status": "ok",
      "details": {
        "total": 0,
        "partial": false,
        "partial_sources": [],
        "sources": [
          {
            "source_id": "default",
            "total": 0,
            "holds": {
              "deterministic": 0,
              "resolver": 0,
              "llm": 0,
              "manual": 0,
              "total": 0
            },
            "pages": {
              "deterministic": 0,
              "resolver": 0,
              "llm": 0,
              "manual": 0,
              "total": 0
            },
            "files": {
              "deterministic": 0,
              "resolver": 0,
              "llm": 0,
              "manual": 0,
              "total": 0
            },
            "by_tier": {
              "deterministic": 0,
              "resolver": 0,
              "llm": 0,
              "manual": 0,
              "total": 0
            },
            "oldest_hold_at": null,
            "sample": [],
            "scan": {
              "complete": true,
              "fresh_at": "2026-11-22T02:51:01.829Z",
              "checked_at": "2026-11-22T02:51:01.829Z",
              "backfill_done": true,
              "walking": false
            }
          }
        ],
        "trend": [
          {
            "source_id": "default",
            "normalized_7d": 0,
            "by_day": [],
            "top_writers": []
          }
        ],
        "warn_at_normalized_7d": 20,
        "model_repair": {
          "max_usd_per_page": 0.3,
          "max_usd_per_day": 1,
          "spent_today_usd": 0,
          "reserved_today_usd": 0
        },
        "timeout_ms": 9998,
        "docs": "docs/guides/write-refusals.md#invalid_fence",
        "uncommitted_repairs": 0,
        "unrenderable_legacy_facts": {
          "total": 0,
          "complete": true,
          "pages": []
        },
        "unbound_legacy_facts": {
          "total": 0,
          "pages": []
        }
      },
      "message": "No malformed facts or takes fence is held, stored or waiting in a checkout (1 source(s) scanned).",
      "elapsed_ms": 63,
      "category": "brain"
    },
    {
      "name": "search_mode",
      "status": "ok",
      "message": "Mode: conservative (no per-key overrides — mode bundle is canonical).",
      "elapsed_ms": 149,
      "category": "ops"
    },
    {
      "name": "synopsis_tier_coverage",
      "status": "ok",
      "message": "Not applicable: the configured contextual-retrieval tier is none, not per_chunk_synopsis.",
      "severity": "info",
      "readiness_state": "not_applicable",
      "details": {
        "configured": false,
        "global_tier": "none"
      },
      "elapsed_ms": 149,
      "category": "brain"
    },
    {
      "name": "hidden_by_search_policy",
      "status": "ok",
      "message": "No pages hidden by search-exclude policy.",
      "details": {
        "prefixes": [
          "test/",
          "attachments/",
          ".raw/"
        ],
        "counts": {}
      },
      "elapsed_ms": 149,
      "category": "brain"
    },
    {
      "name": "eval_drift",
      "status": "ok",
      "message": "Not applicable — gbrain is running as an installed package, not a source checkout; retrieval code changes arrive as version bumps (gbrain --version), not as a git diff.",
      "elapsed_ms": 149,
      "category": "brain"
    },
    {
      "name": "reranker_health",
      "status": "ok",
      "message": "Reranker disabled — no failures expected",
      "elapsed_ms": 149,
      "category": "ops"
    },
    {
      "name": "batch_retry_health",
      "status": "ok",
      "message": "No exhausted batch retries in last 24h.",
      "elapsed_ms": 149,
      "category": "ops"
    },
    {
      "name": "wedged_queue",
      "status": "ok",
      "message": "PGLite — no queue to check",
      "elapsed_ms": 149,
      "category": "ops"
    },
    {
      "name": "orphaned_private_queue",
      "status": "ok",
      "message": "No orphaned private queues",
      "elapsed_ms": 149,
      "category": "ops"
    },
    {
      "name": "autopilot_fanout_concurrency",
      "status": "ok",
      "message": "PGLite — single-writer, fan-out is 1",
      "elapsed_ms": 149,
      "category": "ops"
    },
    {
      "name": "google_oauth",
      "status": "ok",
      "message": "no Google accounts connected (gbrain google connect to start)",
      "elapsed_ms": 149,
      "category": "ops"
    },
    {
      "name": "graph_signals_coverage",
      "status": "ok",
      "message": "graph_signals disabled — coverage not checked",
      "elapsed_ms": 149,
      "category": "brain"
    },
    {
      "name": "junk_entity_hubs",
      "status": "ok",
      "message": "No junk entity hubs (pages with <=2 chunks and >1000 edges)",
      "elapsed_ms": 149,
      "category": "brain"
    },
    {
      "name": "brainstorm_health",
      "status": "ok",
      "message": "Migration v79 applied; tracking enabled. Calibration profile not yet generated — brainstorm/lsd will run unbiased until enough takes are resolved.",
      "elapsed_ms": 149,
      "category": "ops"
    },
    {
      "name": "link_resolution_opportunity",
      "status": "ok",
      "message": "Brain is empty — nothing to scan",
      "elapsed_ms": 149,
      "category": "brain"
    },
    {
      "name": "embedding_width_consistency",
      "status": "ok",
      "message": "Embeddings disabled — no active embedding width to reconcile.",
      "elapsed_ms": 149,
      "category": "brain"
    },
    {
      "name": "facts_embedding_width_consistency",
      "status": "ok",
      "message": "Skipped on PGLite (single bundled pgvector version).",
      "elapsed_ms": 149,
      "category": "brain"
    },
    {
      "name": "source_routing_health",
      "status": "ok",
      "message": "Single-source brain (no federation to check)",
      "elapsed_ms": 149,
      "category": "brain"
    },
    {
      "name": "oauth_confidential_client_health",
      "status": "ok",
      "message": "No OAuth clients registered",
      "elapsed_ms": 149,
      "category": "ops"
    },
    {
      "name": "oauth_client_scope_health",
      "status": "ok",
      "message": "Scoped-client grants consistent (no dangling federated reads, no orphaned workspace sources, no privileged self-registered clients)",
      "elapsed_ms": 149,
      "category": "ops"
    },
    {
      "name": "autopilot_lock_scope",
      "status": "ok",
      "message": "Lock path: /home/codespace/.gbrain/autopilot.lock",
      "elapsed_ms": 149,
      "category": "ops"
    },
    {
      "name": "stale_locks",
      "status": "ok",
      "message": "No stale locks (no rows with ttl_expires_at < NOW())",
      "elapsed_ms": 149,
      "category": "ops"
    },
    {
      "name": "cycle_phase_scope",
      "status": "ok",
      "message": "Phase taxonomy: 12 source-scoped, 18 brain-global, 2 mixed. Source-safe: [lint, backlinks, sync, extract, extract_facts, extract_atoms, recompute_emotional_weight, consolidate, propose_takes, conversation_facts_backfill, enrich_thin, schema-suggest]. Brain-global: [fence_repair, content_repair, unindexed_files, resolve_symbol_edges, synthesize_concepts, grade_takes, calibration_profile, edge_contradictions, claim_conflicts, drift, standing_questions, chronicle, facts_drain, skillopt, embed, orphans, purge, bookkeeping_gc]. Mixed: [synthesize, patterns].",
      "details": {
        "phase_scope_map": {
          "lint": "source",
          "backlinks": "source",
          "sync": "source",
          "fence_repair": "global",
          "content_repair": "global",
          "unindexed_files": "global",
          "synthesize": "mixed",
          "extract": "source",
          "extract_facts": "source",
          "resolve_symbol_edges": "global",
          "patterns": "mixed",
          "recompute_emotional_weight": "source",
          "consolidate": "source",
          "propose_takes": "source",
          "grade_takes": "global",
          "calibration_profile": "global",
          "drift": "global",
          "standing_questions": "global",
          "edge_contradictions": "global",
          "claim_conflicts": "global",
          "chronicle": "global",
          "facts_drain": "global",
          "embed": "global",
          "orphans": "global",
          "purge": "global",
          "bookkeeping_gc": "global",
          "schema-suggest": "source",
          "extract_atoms": "source",
          "synthesize_concepts": "global",
          "conversation_facts_backfill": "source",
          "enrich_thin": "source",
          "skillopt": "global"
        },
        "counts": {
          "source": 12,
          "global": 18,
          "mixed": 2
        }
      },
      "elapsed_ms": 149,
      "category": "meta"
    },
    {
      "name": "embed_staleness",
      "status": "ok",
      "severity": "info",
      "readiness_state": "disabled_by_choice",
      "message": "Not applicable: embeddings are disabled on this brain by choice, so chunks have no vectors by design (keyword search keeps working).",
      "fix": {
        "argv": [
          "gbrain",
          "init",
          "--force",
          "--embedding-model",
          "voyage:voyage-4",
          "--embedding-dimensions",
          "1024",
          "--path",
          "/home/codespace/.gbrain/brain.pglite"
        ],
        "command": "gbrain init --force --embedding-model voyage:voyage-4 --embedding-dimensions 1024 --path /home/codespace/.gbrain/brain.pglite",
        "consent": [
          "credentials",
          "paid"
        ],
        "actor": "user",
        "next": "tell_user_to_run",
        "why": "Embeddings are off, so search is keyword-only, and no configured embedding key fits this brain. Once the key is set this turns on voyage:voyage-4 (1024d) for the PGLite brain at /home/codespace/.gbrain/brain.pglite. Pages, facts and keyword search are kept; existing chunks and facts are queued for vectors, which `gbrain embed --stale` (or the next maintenance cycle) fills.",
        "user_message": "Semantic search needs an embedding API key. Voyage AI works with this brain; if you add a key (VOYAGE_API_KEY), I can turn it on. Embedding costs a little per page; your notes and facts stay as they are.",
        "verify": {
          "argv": [
            "gbrain",
            "doctor",
            "--only",
            "embeddings",
            "--json",
            "--brain",
            "host"
          ]
        },
        "docs": "https://github.com/garrytan/gbrain/blob/v0.60.753.0/docs/guides/search-modes.md",
        "requires_exclusive": true,
        "inputs": [
          {
            "name": "VOYAGE_API_KEY",
            "how": "Ask the user for an API key for Voyage AI; store it with `gbrain config set voyage_api_key <key>` (every gbrain process reads it), or export VOYAGE_API_KEY in the environment of every gbrain process. Then run the command."
          }
        ]
      },
      "elapsed_ms": 149,
      "category": "brain"
    },
    {
      "name": "entity_link_coverage",
      "status": "ok",
      "message": "No entity pages — coverage check vacuous",
      "elapsed_ms": 149,
      "category": "brain"
    },
    {
      "name": "timeline_coverage",
      "status": "ok",
      "message": "No entity pages — coverage check vacuous",
      "elapsed_ms": 149,
      "category": "brain"
    },
    {
      "name": "takes_count",
      "status": "ok",
      "severity": "info",
      "readiness_state": "disabled_by_choice",
      "message": "0 takes (takes.bootstrap_enabled is false; opt in to enable)",
      "fix": {
        "argv": [
          "gbrain",
          "config",
          "set",
          "takes.bootstrap_enabled",
          "true",
          "--brain",
          "host"
        ],
        "command": "gbrain config set takes.bootstrap_enabled true --brain host",
        "consent": [
          "paid"
        ],
        "actor": "agent",
        "next": "ask_user",
        "why": "Takes (typed claims) are opt-in. Enabling the bootstrap lets maintenance extract them from existing pages with a chat model (about $5 on a typical brain), which feeds calibration.",
        "user_message": "gbrain can extract typed claims (\"takes\") from your pages so it can track calibration over time. It uses a paid chat model (roughly $5 once). Turn it on?",
        "verify": {
          "argv": [
            "gbrain",
            "doctor",
            "--only",
            "takes_count",
            "--json",
            "--brain",
            "host"
          ]
        },
        "requires_exclusive": false
      },
      "elapsed_ms": 149,
      "category": "brain"
    },
    {
      "name": "pack_upgrade_available",
      "status": "ok",
      "message": "Active pack gbrain-base-v2@1.7.0+e142684a is current (no successor declared)",
      "elapsed_ms": 149,
      "category": "meta"
    },
    {
      "name": "type_proliferation",
      "status": "ok",
      "message": "no typed pages",
      "elapsed_ms": 149,
      "category": "meta"
    },
    {
      "name": "dangling_aliases",
      "status": "ok",
      "message": "No dangling aliases",
      "elapsed_ms": 149,
      "category": "brain"
    }
  ],
  "top_issues": [],
  "alert": {
    "level": "none",
    "items": [],
    "unknown": [],
    "docs": "docs/guides/troubleshooting.md#doctor-alert"
  },
  "engine": "pglite",
  "db_url_source": null,
  "capped_by": [
    "embeddings_disabled"
  ],
  "elapsed_ms": 4518,
  "complete": true
}
```
- 針對「四、配置 API Key（可選）」，`『如果要啟用語意檢索、自動事實擷取等進階功能，需要配置 API Key。』` 這段描述跟我認知的類似，應該是為了生成 embedding
- 針對「五、匯入和索引」，看起來需要一些測試用的 Markdown 檔案。

## 2026-11-24

- 在 Windows 11 實測
- ( 2026-11-24 11:17:31 )
```bash
~/Documents$ mkdir jbrain
```
- 用 scoop 安裝 `bun` (1.4.5)
```bash
~/Documents$ scoop install bun
Installing 'bun' (1.4.5) [64bit] from 'main' bucket
```
- 用 `bun` 安裝 `gbrain`
```bash
~/Documents$ bun install -g github:garrytan/gbrain#stable
bun add v1.4.5 (a7733435c)

installed gbrain@github:garrytan/gbrain#e585737 with binaries:
 - gbrain

185 packages installed [29.50s]

warn: To run "gbrain", add the global bin folder to $PATH:

C:\Users\jazzw\.bun\bin
```
- 將路徑加到 `~/.bashrc`
```bash
~$ cat >> ~/.bashrc << EOF
## 2026-11-24
PATH=\$PATH:~/.bun/bin
EOF
```
- 開一個新的 Bash session，驗證 `gbrian` 執行檔是否找得到
```bash
~$ which gbrain
/c/Users/jazzw/.bun/bin/gbrain
~$ gbrain --version
gbrain 0.60.765.0
```
- 初始化
```bash
~$ gbrain init --pglite --no-embedding | tee Documents/jbrain/gbrain-init.2026-11-24.log
```
- 檢查健康狀況
```bash
~$ gbrain doctor --json | jq . > Documents/jbrain/gbrain-doctor.2026-11-24.json
```
- 照 `gbrain init` 的建議，測試 `gbrain remember`
```bash
~$ gbrain remember "gbrain install check" --provenance install-check
remembered as fact #1
  note: no embedding provider — duplicate detection degraded
  warning: NO_ENTITY
  hint: Saved without an entity, so entity-scoped recall will not find it. To link it, remember the same claim again with `entity` (the person, company or project it is about): that replaces this copy, so there is nothing to forget. Do not forget it: a claim forgotten without an entity is withdrawn for every entity and cannot be saved again.
Note [degraded_dedup]: No embedding provider is configured, so remember detects only exact duplicates; a near-duplicate phrasing of an existing fact inserts a second fact. Recall first when unsure whether a fact is already saved.
```
- 照 `gbrain init` 的建議，測試 `gbrain recall`
```bash
~$ gbrain recall --query "gbrain install check"
[gbrain degraded: embed_unavailable] This result is partial or degraded: never report "no notes" or "not found" from it.
Facts:
  #1 [fact] gbrain install check — install-check
Pages:
  memory/unattributed [keyword_exact] Unattributed memory
    ## Facts <!--- gbrain:facts:begin --> | # | claim | kind | confidence | visibility | notability | valid_from | valid_until | source | context | |---|-------|---
note: search degraded (keyword_only_embedding_disabled)
```
### 實測「五、匯入和索引」

- 用 `SIGOps` 的文章來驗證「五、匯入和索引」的流程

#### 5.1 匯入 Markdown 檔案

```bash
~$ cd Documents/Obsidian/
~/Documents/Obsidian$ gbrain import SIGOps/ --no-embed
[gbrain phase] import.collect_files start dir=C:\Users\jazzw\Documents\Obsidian\SIGOps strategy=markdown
[gbrain phase] import.collect_files done 53ms files=22
Found 22 markdown files
[import.files] start[gbrain] content-sanity flag (markup_heavy): 3-glia-a-human-inspired-ai-for-systems-design-and-optimization (ratio 0.97) — stays searchable, agent warned
[import.files] 22/22 (100%) done

Import complete (1.9s):
  22 pages imported
  0 pages skipped (0 unchanged, 0 errors, 0 malformed filenames)
  485 chunks created
```
#### 5.2 建立知識圖譜（可選）
```bash
## 預覽
~/Documents/Obsidian$ gbrain extract links --source db --dry-run | head -20
[extract.links_db] 23/23 (100%) done
Links: (dry run) would create 0 from 23 pages (db source)
Skipped 236 candidate(s) whose target page doesn't exist (references to non-pages are never persisted).
~/Documents/Obsidian$ gbrain extract links --source db
[extract.links_db] 23/23 (100%) done
Links: created 0 from 23 pages (db source)
Skipped 236 candidate(s) whose target page doesn't exist (references to non-pages are never persisted).

Done: 0 links, 0 timeline entries from 23 pages
```
```bash
## 正式執行
~/Documents/Obsidian$ gbrain extract timeline --source db
[extract.timeline_db] 23/23 (100%) done
Timeline: created 0 entries from 23 pages (db source)

Done: 0 links, 0 timeline entries from 23 pages
```
```bash
## 驗證
~/Documents/Obsidian$ gbrain stats
Pages:     23
Chunks:    486
Embedded:  0
Links:     0
Tags:      1
Timeline:  0

By type:
  concept: 22
  note: 1
```
#### 5.3 匯入公司知識庫

- 看起來是為了匯入不同目錄的檔案到不同的 bucket，先忽略。

### 實測「六、測試和驗證」

#### 6.1 基本驗證

```bash
## 完整的安裝合約檢查
~/Documents/Obsidian$ gbrain bootstrap verify
gbrain bootstrap verify — FAIL (2026-11-24T04:28:42.245Z)
  [ok  ] doctor_green: engine healthy (schema version 331)
  [ok  ] facts_visibility: facts default visibility: world (set by bootstrap verify — was unset). Governs extraction-path writes only — `remember` defaults to world either way, except from a member-bound credential, whose saves stay private on its member page; pass `visibility` per call to keep a remembered fact private. Flip with `gbrain config set facts.default_visibility private` if less-trusted surfaces will read this brain.
  [ok  ] token_sweep: no unresolved template tokens in rendered identity files
  [FAIL] byte_floors: byte floors: SOUL.md missing; USER.md missing — floors catch skipped interviews, never pad; re-run the interview + render
  [FAIL] writeback_contract: AGENTS.md is missing; render the bootstrap contract before wiring the agent. Fix: run `gbrain bootstrap contract --repair` from the workspace (or pass --workspace explicitly).
  [ok  ] secret_scan: no secrets in 1 workspace file(s)
  [ok  ] deny_globs: not a git repo yet — deny-glob backstop applies at push time
  [ok  ] repo_privacy: local-only (no origin remote) — run `gbrain bootstrap repo` any time to add the private body
  [ok  ] execution_env: local machine — full persistence surface available
  [ok  ] mcp_json_hygiene: no .mcp.json in the workspace
  [ok  ] hook_carrier_overlap: no event fires from more than one hook carrier
  [ok  ] embedding_plane: keyless — no embedding provider configured; writes store no vectors (active column content_chunks.embedding: 1024d)
  [FAIL] roundtrip: put_page wrote the DB but NO file appeared under brain/ (write-through: write-through reported nothing). The workspace source must be registered with its brain/ dir as local_path (gbrain sources add default --path C:\Users\jazzw\Documents\Obsidian\brain) or agent writes never reach the repo.
  [ok  ] capability_report: keyless mode / keyword-only search
  [ok  ] mcp_surface: mcp_surface: full (default) — full op surface for registrations
  [ok  ] hooks_smoke: hooks not installed — smoke not applicable (Codex/pull-mode or declined consent)
  [ok  ] push_probe: local-only mode — no push expected
  [ok  ] inert_skills: no skills/ dir — scaffold not run (optional)
  [ok  ] first_run_tour: tour withheld — prints on PASS

gbrain capabilities: keyless mode
  embeddings: not configured — search runs keyword-only (BM25)
  extraction: not configured — memory comes from agent-authored ## Facts fences and write ops
keyless mode: keyword search, agent-authored memory; one optional key upgrades capabilities — OpenAI: semantic search + auto-extraction; Voyage: semantic search; Anthropic: auto-extraction (see `gbrain providers list` for env-ready options).

Fix the FAIL checks above and re-run — the first-run tour prints on PASS.
```
- 根據失敗的部份，應該主要有三樣： (1) 缺少 `SOUL.md` (2) 缺少 `USER.md` (3) 缺少 `AGENTS.md` (4) 找不到 `brain` 子目錄
- 其次，照 `gbrain bootstrap verify` 的最後寫到 「see `gbrain providers list` for env-ready options 」，跑一次指令。
```bash
~/Documents/Obsidian$ gbrain providers list
PROVIDER              TIER              EMBED   EXPAND  CHAT    RERANK  DECIDE  STATUS
------------------------------------------------------------------------------------------------
openai                native            yes     yes     yes     —       —       ✗ missing OPENAI_API_KEY
google                native            yes     yes     yes     —       —       ✓ ready
anthropic             native            —       yes     yes     —       —       ✗ missing ANTHROPIC_API_KEY
claude-cli            native            —       yes     yes     —       —       ✓ ready
ollama                openai-compat     yes     yes     yes     —       —       ✓ ready
openrouter            openai-compat     yes     yes     yes     yes     —       ✗ missing OPENROUTER_API_KEY
voyage                openai-compat     yes     —       —       yes     —       ✗ missing VOYAGE_API_KEY
litellm               openai-compat     —       yes     —       —       —       ✓ ready
deepseek              openai-compat     —       yes     yes     —       —       ✗ missing DEEPSEEK_API_KEY
groq                  openai-compat     —       yes     yes     —       —       ✗ missing GROQ_API_KEY
together              openai-compat     —       yes     yes     —       —       ✗ missing TOGETHER_API_KEY
llama-server          openai-compat     —       —       —       —       —       ✓ ready
llama-server-reranker openai-compat     —       —       —       yes     —       ✓ ready
lmstudio              openai-compat     —       —       —       —       —       ✓ ready
minimax               openai-compat     yes     —       yes     —       —       ✗ missing MINIMAX_API_KEY
dashscope             openai-compat     yes     —       —       —       —       ✗ missing DASHSCOPE_API_KEY
dashscope-rerank      openai-compat     —       —       —       yes     —       ✗ missing DASHSCOPE_API_KEY
zhipu                 openai-compat     yes     —       yes     —       —       ✗ missing ZHIPUAI_API_KEY
azure-openai          openai-compat     yes     —       —       —       —       ✗ missing AZURE_OPENAI_ENDPOINT
nan                   openai-compat     —       —       —       yes     —       ✗ missing NAN_API_KEY
moonshot              openai-compat     —       yes     yes     —       —       ✗ missing MOONSHOT_API_KEY
mistral               openai-compat     yes     yes     yes     —       —       ✗ missing MISTRAL_API_KEY
nvidia                openai-compat     yes     —       yes     —       —       ✗ missing NVIDIA_API_KEY
perplexity            openai-compat     yes     —       —       —       —       ✗ missing PERPLEXITY_API_KEY
particle              openai-compat     —       yes     yes     —       —       ✗ missing PARTICLE_API_KEY
typesafe              openai-compat     —       —       —       yes     yes     ✗ missing TYPESAFE_API_KEY
```
- 看起來要用 OpenRouter 才能滿足 EMBED, EXPAND, CHAT, RERANK, DECIDE 的全部功能。（跟 Hermes Agent 一樣，用 LLM Gateway 會比較有彈性）
- 檢查配置的模型
```bash
## 檢查配置的模型
~/Documents/Obsidian$ gbrain models
Tier routing:
  tier.utility    anthropic:claude-haiku-4-5-20251001           [default] [newer haiku available: claude-haiku-5-5] (gbrain config set models.tier.utility anthropic:claude-haiku-5-5)
  tier.reasoning  anthropic:claude-sonnet-4-6                   [default] [newer sonnet available: claude-sonnet-5-5] (gbrain config set models.tier.reasoning anthropic:claude-sonnet-5-5)
  tier.deep       anthropic:claude-opus-4-7                     [default] [newer opus available: claude-opus-5-5] (gbrain config set models.tier.deep anthropic:claude-opus-5-5)
  tier.subagent   anthropic:claude-sonnet-4-6                   [default] [newer sonnet available: claude-sonnet-5-5] (gbrain config set models.tier.subagent anthropic:claude-sonnet-5-5)

Global default:
  models.default  (unset)

Per-task overrides:
  models.dream.synthesize            → anthropic:claude-sonnet-4-6                   [tier.reasoning]
  models.dream.synthesize_verdict    → anthropic:claude-haiku-4-5-20251001           [tier.utility]
  models.dream.patterns              → anthropic:claude-sonnet-4-6                   [tier.reasoning]
  models.dream.extract_atoms         → anthropic:claude-haiku-4-5-20251001           [tier.utility (caller-specific)]
  models.drift                       → anthropic:claude-sonnet-4-6                   [tier.reasoning]
  models.standing_questions          → anthropic:claude-opus-4-7                     [tier.deep]
  models.think                       → anthropic:claude-opus-4-7                     [tier.deep]
  models.fence_repair                → none                                          [measured default]
  models.content_repair              → none                                          [measured default]
  models.subagent                    → anthropic:claude-sonnet-4-6                   [tier.subagent]
  facts.extraction_model             → anthropic:claude-haiku-5-5                    [measured default]
  models.eval.longmemeval            → anthropic:claude-sonnet-4-6                   [tier.reasoning]
  models.eval.contradictions_judge   → anthropic:claude-haiku-4-5-20251001           [tier.utility]
  models.expansion                   → anthropic:claude-haiku-4-5-20251001           [tier.utility]
  models.contextual_synopsis         → anthropic:claude-haiku-4-5-20251001           [tier.utility]
  models.chat                        → anthropic:claude-sonnet-4-6                   [tier.reasoning]

Nightly quality probe (autopilot.nightly_quality_probe):
  reader (LongMemEval answers)       → anthropic:claude-sonnet-4-6                   [tier.reasoning]
  extractor (trajectory claims)      → anthropic:claude-haiku-4-5-20251001           [tier.utility]
  judge slot A                       → openai:gpt-5.2                                [panel default]
  judge slot B                       → anthropic:claude-opus-4-7                     [panel default]
  judge slot C                       → deepseek:deepseek-v4-pro                      [panel default]
  Note: Slot availability, substitutes and key-aware defaults are judged from this process's environment; a provider key set only in C:\Users\jazzw\.gbrain\env (sourced by the autopilot daemon's launcher) reads here as unavailable.

Aliases:
  opus     → anthropic:claude-opus-4-7
  sonnet   → anthropic:claude-sonnet-4-6
  haiku    → anthropic:claude-haiku-4-5-20251001
  gemini   → google:gemini-3.5-flash-lite
  gpt      → openai:gpt-5.6

Tip: probe reachability with `gbrain models doctor` (opt-in; spends a minimal request per configured chat/embed/rerank surface).
```

> [!NOTE]
> 1. 越測越覺得 GBrain 要綁 Agent 會比較完整
> 2. 這裡的 `dream` 跟 `autopilot.nightly_quality_probe` 不確定是不是其他 YouTube 影片或一些部落格文章中提到的「作夢模式」跟「在人類睡覺時，執行的工作」

- 模型探針測試
```bash
## 模型探針測試
~/Documents/Obsidian$ gbrain models doctor
Error [unavailable]: This brain has no explicit embedding model. Its stored vectors must not be interpreted using a new default. Run gbrain migrate embeddings --status and preview an explicit migration with --dry-run.
Fix: gbrain doctor --json --brain host
Docs: https://github.com/garrytan/gbrain/blob/v0.60.765.0/docs/guides/error-codes.md#unavailable
```

#### 6.2 記憶測試
- 測試 remember/recall 往返：
```bash
## 記住一個事實
~/Documents/Obsidian$ gbrain remember "GBrain 是一個知識庫系統" --entity "gbrain" --content-origin user_said --provenance "測試"
remembered as fact #3
  entity: gbrain
  note: the entity has no page, so this fact is stored in the database only
  note: no embedding provider — duplicate detection degraded
Note [degraded_dedup]: No embedding provider is configured, so remember detects only exact duplicates; a near-duplicate phrasing of an existing fact inserts a second fact. Recall first when unsure whether a fact is already saved.
```
- 查詢該事實
```bash
~/Documents/Obsidian$ gbrain recall "GBrain 是一個知識庫系統" --json
[recall] no facts for entity 'GBrain 是一個知識庫系統'; matched 1 fact(s) by text — use --grep to force text matching.
{
  "facts": [
    {
      "id": 3,
      "fact": "GBrain 是一個知識庫系統",
      "kind": "fact",
      "entity_slug": "gbrain",
      "visibility": "world",
      "notability": "medium",
      "valid_from": "2026-11-24T05:14:05.669Z",
      "valid_until": null,
      "expired_at": null,
      "superseded_by": null,
      "consolidated_at": null,
      "consolidated_into": null,
      "source": "測試",
      "source_session": null,
      "confidence": 1,
      "effective_confidence": 1,
      "created_at": "2026-11-24T05:14:05.811Z"
    }
  ],
  "total": 1
}
```
- 先忽略「忘掉」事實這一項，因為後面的指令還會用到這一筆 fact

> [!TIP]
> ```bash
> ## 遺忘該事實
> gbrain forget_fact "GBrain 是一個知識庫系統"
> ```

- 關鍵字搜尋測試：
```bash
## 關鍵字搜尋
~/Documents/Obsidian$ gbrain search "GBrain 知識庫" --json
[gbrain] embeddings are off on this brain by choice (embedding_disabled), so search is keyword-only and no query text is sent to an embedding provider. If the user wants semantic search, `gbrain doctor --json` names the enable command; turning it on needs their consent.
Saved facts (remember): about the entity this query names (newest first), then facts those point to, then matches for its words; recall returns more:
- GBrain 是一個知識庫系統 [entity: gbrain; saved 2026-11-24; provenance: 測試]
[
  {
    "slug": "the-next-horizon-of-system-intelligence_6.zh-tw",
    "page_id": 6,
    "title": "長線思考：具有記憶能力的 Agent 如何更快解決作業問題",
    "type": "concept",
    "chunk_text": "tes 上的微服務應用程式：服務間互動會產生突發的、部署特有的失敗模式，這些模式可以從過往知識中受益。\n\nSDO 將未部署和失敗中的應用程式都視為不健康狀態，並遵循相同的分階段工作流程，驅動每個應用程式朝向健康狀態（圖 1）。作業員不像保持單一長壽命 Agent 會議持續運作——這不可避免地會撞擊上下文視窗限制並強制有損濃縮——而是在每個階段轉換和 Agent 交接時啟動全新會議。延續性來自於共享知識庫（詳見下方的知識庫章節）：一個**持久檔案樹**，包含應用程式的架構摘要、整合所有先前事件的長期作業摘要，以及記錄症狀、根本原因和修復措施的每個事件事後檢討（post-mortem）。Agent 可以在會議期間隨時從知識庫讀取，並在解決問題時寫回。\n\n![](https://www.sigops.org/wp-content/uploads/2026/03/image-1600x649.jpeg)\n\n圖 1：SDO Agent 工作流程。相同的階段序列適用於初始部署和回退修復。\n\n### 工作流程",
    "chunk_source": "compiled_truth",
    "chunk_id": 73,
    "chunk_index": 5,
    "score": 1003,
    "stale": false,
    "source_id": "default",
    "effective_date": "2026-03-17",
    "effective_date_source": "published",
    "keyword_hit": true,
    "base_score": 1003,
    "evidence": "keyword_exact",
    "create_safety": "probable",
    "id": "gbrain-page:v1:WyJkZWZhdWx0IiwidGhlLW5leHQtaG9yaXpvbi1vZi1zeXN0ZW0taW50ZWxsaWdlbmNlXzYuemgtdHciLHsiYyI6NzN9XQ",
    "trust_tier": "operator_curated",
    "origin": "managed_file_import"
  },
  {
    "slug": "memory/unattributed",
    "page_id": 1,
    "title": "Unattributed memory",
    "type": "note",
    "chunk_text": "## Facts\n\n<!--- gbrain:facts:begin -->\n\n| # | claim | kind | confidence | visibility | notability | valid_from | valid_until | source | context |\n|---|-------|------|------------|------------|------------|------------|-------------|--------|---------|\n| 1 | gbrain install check | fact | 1.0 | world | medium | 2026-11-24T03:51:42Z |  | install-check |  |\n<!--- gbrain:facts:end -->",
    "chunk_source": "compiled_truth",
    "chunk_id": 1,
    "chunk_index": 0,
    "score": 1000,
    "stale": false,
    "source_id": "default",
    "effective_date": "2026-11-24",
    "effective_date_source": "fallback",
    "keyword_hit": true,
    "base_score": 1000,
    "evidence": "keyword_exact",
    "create_safety": "probable",
    "id": "gbrain-page:v1:WyJkZWZhdWx0IiwibWVtb3J5L3VuYXR0cmlidXRlZCJd",
    "trust_tier": "agent_written",
    "origin": "cli:remember"
  }
]
[gbrain degraded: embed_unavailable] This result is partial or degraded: never report "no notes" or "not found" from it.
Note [degraded_recall]: Recall was degraded (embed_unavailable): semantic (vector) search did not run, so matches phrased differently from the query can be missing. Treat a thin or empty result as "not found with a degraded search", never as "the brain has nothing on this". This brain was set up keyword-only by the user's choice; mention it only if the user asks why something was not found. No query text was sent to an embedding provider. If the user wants semantic search, `gbrain doctor --json` names the enable command; turning it on needs their consent.
```
- 從結果看起來，當把 embedding 語意搜尋(semantic/vector search)關掉時，只能做 keyword 關鍵字搜尋。
- 看起來是只有符合其中一個關鍵字，也就是有點像 SQL 的 `OR` 條件，都會被抓出來。
- 在這個例子裡，只要有 `gbrain` 或 `知識庫` 的都會出現在搜尋結果中
```bash
## 語意查詢（需要 API Key）
~/Documents/Obsidian$ gbrain query "GBrain 的主要功能是什麼？" --json
[gbrain] embeddings are off on this brain by choice (embedding_disabled), so search is keyword-only and no query text is sent to an embedding provider. If the user wants semantic search, `gbrain doctor --json` names the enable command; turning it on needs their consent.
[
  {
    "slug": "memory/unattributed",
    "page_id": 1,
    "title": "Unattributed memory",
    "type": "note",
    "chunk_text": "## Facts\n\n<!--- gbrain:facts:begin -->\n\n| # | claim | kind | confidence | visibility | notability | valid_from | valid_until | source | context |\n|---|-------|------|------------|------------|------------|------------|-------------|--------|---------|\n| 1 | gbrain install check | fact | 1.0 | world | medium | 2026-11-24T03:51:42Z |  | install-check |  |\n<!--- gbrain:facts:end -->",
    "chunk_source": "compiled_truth",
    "chunk_id": 1,
    "chunk_index": 0,
    "score": 1000,
    "stale": false,
    "source_id": "default",
    "effective_date": "2026-11-24",
    "effective_date_source": "fallback",
    "keyword_hit": true,
    "base_score": 1000,
    "evidence": "keyword_exact",
    "create_safety": "probable",
    "id": "gbrain-page:v1:WyJkZWZhdWx0IiwibWVtb3J5L3VuYXR0cmlidXRlZCJd",
    "trust_tier": "agent_written",
    "origin": "cli:remember"
  }
]
[gbrain degraded: embed_unavailable] This result is partial or degraded: never report "no notes" or "not found" from it.
Note [degraded_recall]: Recall was degraded (embed_unavailable): semantic (vector) search did not run, so matches phrased differently from the query can be missing. Treat a thin or empty result as "not found with a degraded search", never as "the brain has nothing on this". This brain was set up keyword-only by the user's choice; mention it only if the user asks why something was not found. No query text was sent to an embedding provider. If the user wants semantic search, `gbrain doctor --json` names the enable command; turning it on needs their consent.
```
- 因為一開始初始化時用了 `--no-embedding` ，也沒有設定 API Key (雖然環境中有 GEMINI_API_KEY 被找到)，但這裡的結果還是用 keyword search 而已

#### 6.3 完整性檢查

- 檢查 Embedding 狀態
```bash
## 檢查嵌入狀態
~/Documents/Obsidian$ gbrain embed --status
Error [unknown_flag]: gbrain embed does not accept --status.
Fix: gbrain embed --stale --dry-run --json --brain host
Why: A single-page run (gbrain embed <slug>) takes only its own flags, and --status is not one of them, so the run stopped before it read a page or asked for spend approval.
Docs: https://github.com/garrytan/gbrain/blob/v0.60.765.0/docs/guides/error-codes.md#unknown_flag
```
> [!WARNING]
> 這裡有幻覺，`gbrain embed` 不支援 `--status` 這個參數

- 檢查資料來源
```bash
## 檢查資料來源
~/Documents/Obsidian$ gbrain sources list --json
{
  "sources": [
    {
      "id": "default",
      "name": "default",
      "local_path": "C:\\Users\\jazzw\\.gbrain\\content\\048f5c6d-2634-4ecc-ad8f-7336819ddba5\\default",
      "federated": true,
      "mirror_read_only": false,
      "strategy": null,
      "pull_strategy": "rebase",
      "page_count": 23,
      "last_sync_at": null,
      "archived": false
    }
  ]
}
```
- 檢查知識圖譜
```bash
## 檢查知識圖譜
~/Documents/Obsidian$ gbrain graph-query "gbrain" --depth 2
No edges found from gbrain.
```
- 查看統計資訊
```bash
## 查看統計資訊
~/Documents/Obsidian$ gbrain stats --json
{
  "page_count": 23,
  "chunk_count": 486,
  "embedded_count": 0,
  "link_count": 0,
  "tag_count": 1,
  "timeline_entry_count": 0,
  "pages_by_type": {
    "concept": 22,
    "note": 1
  }
}
```
#### 6.4 上線檢查（Onboard）

- 檢查知識庫健康狀況
```bash
/Documents/Obsidian$ gbrain onboard --check --json
{
  "schema_version": 1,
  "recommendations": [
    {
      "step": 1,
      "id": "extract.stale",
      "job": "extract",
      "params": {
        "stale": true
      },
      "idempotency_key": "default:extract:e4d556df",
      "severity": "medium",
      "est_seconds": 30.23,
      "est_usd_cost": 0,
      "depends_on": [],
      "rationale": "Materialize link + timeline edges for 23 stale database pages",
      "status": "remediable",
      "apply_policy": "auto_apply",
      "prompt_text": "Materialize link + timeline edges for 23 stale database pages",
      "migration_id": "extract.stale"
    }
  ],
  "summary": {
    "total": 1,
    "auto_eligible": 1,
    "prompt_required": 0,
    "manual_only": 0,
    "est_total_usd": 0
  }
}
```
- 自動修復（需要設定 $MAX_USD 限制）
```bash
~/Documents/Obsidian$ gbrain onboard --auto --max-usd 5
[onboard] target 90/100 unreachable; max autonomous = 50/100. Configure missing prereqs (run gbrain doctor --remediation-plan) or lower --target-score.
```

> [!TODO]
> 待查：這裡的 `onboard` 跟 `MAX_USD` 代表什麼意思？
