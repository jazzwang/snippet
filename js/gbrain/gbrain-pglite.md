# GBrain 與 PGLite 關係

## 問題：GBrain 使用 SQLite 還是 PGLite？

## 答案：GBrain 主要使用 PostgreSQL，PGLite 是預設嵌入式回退方案

根據 GBrain 官方文件與技術報告，GBrain 支援多種數據庫引擎，依優先順序自動選擇：

## 數據庫引擎優先順序

| 順序 | 引擎 | 條件 |
|------|------|------|
| 1 | **現有 PostgreSQL** | 設定 `GBRAIN_DATABASE_URL` |
| 2 | **Supabase** | 發現現有的 Supabase 專案 |
| 3 | **本地 PostgreSQL** | 設定環境變數或 `--local-postgres` |
| 4 | **Docker PostgreSQL** | 使用 `gbrain-postgres` 容器 |
| 5 | **PGLite** | 預設嵌入式方案（終端回退） |

## 命令範例

### 預設使用 PGLite（嵌入式方案）

```bash
gbrain init --pglite --no-embedding
```

### 優先使用 PostgreSQL

```bash
gbrain init --prefer-postgres [--allow-docker] [--allow-create-db]
```

## 什麼是 PGLite？

**PGLite** 是由 ElectricSQL 開發的嵌入式 PostgreSQL 數據庫，將完整的 Postgres 編譯為 WebAssembly (WASM) 後打包成 TypeScript 客戶端庫。

### 核心特性

| 特性 | 說明 |
|------|------|
| **體量輕小** | 壓縮後僅 3MB |
| **零依賴** | 無需安裝後端數據庫服務 |
| **跨平台** | 支援瀏覽器、Node.js、Bun、Deno |
| **響應式** | 內建數據加載、同步和即時查詢 |
| **可擴展** | 支援 pgvector、PostGIS 等擴展 |

### 使用範例

```javascript
import { PGlite } from "@electric-sql/pglite";

// 創建數據庫
const db = new PGlite();

// 執行查詢
await db.query("SELECT 'Hello world' as message");
```

## GBrain 中的 PGLite 使用

### 初始化知識庫

```bash
## 獨立 CLI 模式（無需 Agent）
gbrain init --pglite --no-embedding

## 驗證健康狀態
gbrain doctor --json
```

### 故障排除

**PGLite 啟動失敗：**

```bash
## 自動修復
gbrain pglite-repair --dry-run
gbrain pglite-repair --yes

## 重建
gbrain reinit-pglite

## 切換到 PostgreSQL
gbrain migrate --to postgres
```

## 總結

- **主要數據庫**：PostgreSQL（完整版的 Postgres）
- **預設方案**：PGLite（輕量級 WASM 嵌入式 Postgres）
- **目的**：PGLite 作為終端回退，讓 GBrain 可以在沒有完整 Postgres 環境時仍能運作

## 參考資源

- [GBrain 官方文件](https://github.com/garrytan/gbrain)
- [PGLite 官方文件](https://pglite.dev/)
