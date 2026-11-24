# PGlite 技術報告

> PGlite - 基於 WebAssembly 的 Postgres 實作，讓您在瀏覽器、Node.js、Bun 和 Deno 中運轉完整的 Postgres 資料庫。

## 簡介

PGlite 是由 Electric 團隊開發的 WebAssembly 版 Postgres，打包成 TypeScript 客戶端庫，無需額外的依賴即可在瀏覽器、Node.js、Bun 和 Deno 中運轉 Postgres。壓縮後僅約 3MB，支援包括 pgvector 和 PostGIS 等許多 Postgres 擴充功能。

### 主要特色

- **輕量級**: 壓縮後不到 3MB 的完整 Postgres WebAssembly 實作
- **可擴展**: 動態擴充功能載入機制，支援 pgvector、PostGIS 等擴充功能
- **即時反應**: 內建資料載入、同步和即時查詢原語
- **跨平台**: 支援瀏覽器、Node.js、Bun、Deno

## 安裝步驟

### 1. 環境準備

#### 系統需求

- Node.js v20 或更高版本（如需自行編譯）
- Docker（如需自行編譯 WebAssembly 模組）
- pnpm（建議用於套件管理）

#### 套件管理

支援以下套件管理器：

```bash
# npm
npm install @electric-sql/pglite

# pnpm
pnpm install @electric-sql/pglite

# yarn
yarn add @electric-sql/pglite

# bun
bun install @electric-sql/pglite

# deno
deno add npm:@electric-sql/pglite
```

### 2. 基本設定

#### 在瀏覽器中使用

使用 CDN（如 JSDeliver）或直接安裝：

```javascript
// 使用 CDN
import { PGlite } from 'https://cdn.jsdelivr.net/npm/@electric-sql/pglite/dist/index.js'

// 或直接安裝
import { PGlite } from '@electric-sql/pglite'
```

#### 在 Node.js/Bun/Deno 中使用

```javascript
import { PGlite } from '@electric-sql/pglite'
```

## 測試步驟

### 1. 建立記憶體中的 Postgres

```javascript
import { PGlite } from '@electric-sql/pglite'

// 建立記憶體中的 Postgres
const db = new PGlite()
await db.query("select 'Hello world' as message;")
console.log(db.queryResult)
// 輸出: { rows: [ { message: "Hello world" } ] }
```

### 2. 使用參數化查詢

```javascript
import { PGlite } from '@electric-sql/pglite'

const db = new PGlite()

// 建立測試表
await db.exec(`
  CREATE TABLE IF NOT EXISTS todo (
    id SERIAL PRIMARY KEY,
    task TEXT,
    done BOOLEAN DEFAULT false
  );
`)

// 插入資料
await db.exec(`
  INSERT INTO todo (task, done) VALUES ('安裝 PGlite', true);
  INSERT INTO todo (task, done) VALUES ('建立測試資料', false);
`)

// 查詢資料
const result = await db.query('SELECT * FROM todo WHERE done = $1', [true])
console.log(result.rows)
```

### 3. 使用持久化儲存

#### 在瀏覽器中使用 IndexedDB

```javascript
import { PGlite } from '@electric-sql/pglite'

// 使用 IndexedDB 持久化
const db = new PGlite('idb://my-pgdata')
await db.query("select '數據已存到 IndexedDB' as message;")
```

#### 在 Node.js 中使用檔案系統

```javascript
import { PGlite } from '@electric-sql/pglite'

// 使用檔案系統持久化
const db = new PGlite('./path/to/pgdata')
await db.query("select '數據已存到檔案系統' as message;")
```

## 驗證步驟

### 1. 驗證基本功能

```javascript
import { PGlite } from '@electric-sql/pglite'

async function testBasicFunctionality() {
  const db = new PGlite()
  await db.waitReady
  
  // 1. 驗證資料庫已準備就緒
  console.log('資料庫狀態:', db.ready, db.closed)
  
  // 2. 建立表
  await db.exec(`
    CREATE TABLE IF NOT EXISTS verification (
      id SERIAL PRIMARY KEY,
      test_name TEXT NOT NULL,
      created_at TIMESTAMP DEFAULT NOW()
    );
  `)
  console.log('✓ 表建立成功')
  
  // 3. 插入測試資料
  await db.query('INSERT INTO verification (test_name) VALUES ($1)', ['基本功能測試'])
  console.log('✓ 資料插入成功')
  
  // 4. 查詢資料
  const result = await db.query('SELECT * FROM verification WHERE id = 1')
  if (result.rows.length === 1 && result.rows[0].test_name === '基本功能測試') {
    console.log('✓ 資料查詢成功')
  }
  
  // 5. 更新資料
  await db.query('UPDATE verification SET test_name = $1 WHERE id = $2', ['更新測試', 1])
  const updated = await db.query('SELECT * FROM verification WHERE id = 1')
  if (updated.rows[0].test_name === '更新測試') {
    console.log('✓ 資料更新成功')
  }
  
  // 6. 關閉資料庫
  await db.close()
  console.log('✓ 資料庫關閉成功')
  
  console.log('\n所有基本功能驗證通過！')
}

testBasicFunctionality().catch(err => {
  console.error('驗證失敗:', err)
  process.exit(1)
})
```

### 2. 驗證參數化查詢

```javascript
import { PGlite } from '@electric-sql/pglite'

async function testParameterizedQueries() {
  const db = new PGlite()
  await db.waitReady
  
  // 建立測試表
  await db.exec(`
    CREATE TABLE IF NOT EXISTS param_test (
      id SERIAL PRIMARY KEY,
      name TEXT,
      value INTEGER,
      active BOOLEAN
    );
  `)
  
  // 使用參數化插入
  await db.query('INSERT INTO param_test (name, value, active) VALUES ($1, $2, $3)', 
    ['測試產品', 100, true])
  
  // 使用參數化查詢
  const result = await db.query(
    'SELECT * FROM param_test WHERE name = $1 AND active = $2',
    ['測試產品', true]
  )
  
  if (result.rows.length === 1 && result.rows[0].value === 100) {
    console.log('✓ 參數化查詢驗證通過')
  } else {
    throw new Error('參數化查詢驗證失敗')
  }
  
  await db.close()
}

testParameterizedQueries()
```

### 3. 驗證持久化儲存（瀏覽器）

```javascript
import { PGlite } from '@electric-sql/pglite'

async function testPersistence() {
  const db = new PGlite('idb://verification-db')
  await db.waitReady
  
  // 建立表並插入資料
  await db.exec(`
    CREATE TABLE IF NOT EXISTS persistence_test (
      id SERIAL PRIMARY KEY,
      data TEXT
    );
    INSERT INTO persistence_test (data) VALUES ('測試數據 1'), ('測試數據 2');
  `)
  
  // 重新建立連接（測試持久化）
  const db2 = new PGlite('idb://verification-db')
  await db2.waitReady
  
  const count = await db2.query('SELECT COUNT(*) FROM persistence_test')
  if (count.rows[0].count === 2) {
    console.log('✓ 持久化儲存驗證通過')
  } else {
    throw new Error('持久化儲存驗證失敗')
  }
  
  await db.close()
  await db2.close()
}

testPersistence()
```

### 4. 驗證持久化儲存（Node.js）

```javascript
import { PGlite } from '@electric-sql/pglite'
import fs from 'fs'
import path from 'path'

async function testFileSystemPersistence() {
  const dataDir = './pglite-test-data'
  
  // 刪除舊資料（如果存在）
  if (fs.existsSync(dataDir)) {
    fs.rmSync(dataDir, { recursive: true, force: true })
  }
  
  // 建立資料庫
  const db = new PGlite(dataDir)
  await db.waitReady
  
  // 建立表並插入資料
  await db.exec(`
    CREATE TABLE IF NOT EXISTS fs_test (
      id SERIAL PRIMARY KEY,
      message TEXT
    );
    INSERT INTO fs_test (message) VALUES ('測試檔案系統持久化');
  `)
  
  // 刪除資料庫
  await db.close()
  fs.rmSync(dataDir, { recursive: true, force: true })
  
  // 重新建立資料庫（從檔案系統載入）
  const db2 = new PGlite(dataDir)
  await db2.waitReady
  
  const result = await db2.query('SELECT message FROM fs_test WHERE id = 1')
  
  if (result.rows[0].message === '測試檔案系統持久化') {
    console.log('✓ 檔案系統持久化驗證通過')
  } else {
    throw new Error('檔案系統持久化驗證失敗')
  }
  
  await db2.close()
}

testFileSystemPersistence().catch(err => {
  console.error('測試失敗:', err)
  process.exit(1)
})
```

### 5. 驗證擴充功能載入

```javascript
import { PGlite } from '@electric-sql/pglite'

async function testExtensions() {
  const db = new PGlite()
  await db.waitReady
  
  // 驗證擴充功能載入
  try {
    // 建立測試表
    await db.exec(`
      CREATE TABLE IF NOT EXISTS extension_test (
        id SERIAL PRIMARY KEY,
        description TEXT
      );
    `)
    
    // 插入資料
    await db.query('INSERT INTO extension_test (description) VALUES ($1)', ['擴充功能測試'])
    
    const result = await db.query('SELECT * FROM extension_test WHERE id = 1')
    if (result.rows.length === 1) {
      console.log('✓ 擴充功能載入驗證通過')
    }
    
    await db.close()
  } catch (error) {
    console.log('注意：擴充功能可能需要額外安裝')
    console.log('錯誤訊息:', error.message)
  }
}

testExtensions()
```

## 完整範例

### 1. 基本範例（Node.js）

```javascript
import { PGlite } from '@electric-sql/pglite'

async function main() {
  // 建立資料庫
  const db = new PGlite()
  await db.waitReady
  
  console.log('=== PGlite 基本範例 ===\n')
  
  // 建立表
  console.log('1. 建立表...')
  await db.exec(`
    CREATE TABLE IF NOT EXISTS users (
      id SERIAL PRIMARY KEY,
      name TEXT NOT NULL,
      email TEXT UNIQUE,
      created_at TIMESTAMP DEFAULT NOW()
    );
  `)
  console.log('   ✓ 表建立完成\n')
  
  // 插入資料
  console.log('2. 插入資料...')
  await db.query('INSERT INTO users (name, email) VALUES ($1, $2)', ['Alice', 'alice@example.com'])
  await db.query('INSERT INTO users (name, email) VALUES ($1, $2)', ['Bob', 'bob@example.com'])
  console.log('   ✓ 資料插入完成\n')
  
  // 查詢資料
  console.log('3. 查詢所有使用者...')
  const users = await db.query('SELECT * FROM users ORDER BY id')
  console.log('   使用者列表:')
  users.rows.forEach(user => {
    console.log(`   - ID: ${user.id}, 名稱: ${user.name}, Email: ${user.email}`)
  })
  console.log()
  
  // 使用參數化更新
  console.log('4. 更新資料...')
  await db.query('UPDATE users SET email = $1 WHERE id = $2', ['alice.updated@example.com', 1])
  console.log('   ✓ 資料更新完成\n')
  
  // 刪除資料
  console.log('5. 刪除資料...')
  await db.query('DELETE FROM users WHERE id = $1', [1])
  const remaining = await db.query('SELECT COUNT(*) FROM users')
  console.log(`   ✓ 剩餘使用者數: ${remaining.rows[0].count}\n`)
  
  // 關閉資料庫
  await db.close()
  console.log('6. 資料庫已關閉')
  console.log('\n=== 範例完成 ===')
}

main().catch(err => {
  console.error('發生錯誤:', err)
  process.exit(1)
})
```

### 2. 即時查詢範例

```javascript
import { PGlite } from '@electric-sql/pglite'

async function realtimeExample() {
  const db = new PGlite()
  await db.waitReady
  
  // 建立表
  await db.exec(`
    CREATE TABLE IF NOT EXISTS todo (
      id SERIAL PRIMARY KEY,
      task TEXT NOT NULL,
      completed BOOLEAN DEFAULT false,
      updated_at TIMESTAMP DEFAULT NOW()
    );
  `)
  
  // 插入初始資料
  await db.query('INSERT INTO todo (task) VALUES ($1)', ['完成第一筆任務'])
  await db.query('INSERT INTO todo (task) VALUES ($1)', ['學習 PGlite'])
  
  // 查詢並即時更新
  const todo = await db.query('SELECT * FROM todo WHERE id = 1')
  console.log('初始狀態:', todo.rows[0])
  
  // 更新資料
  await db.query('UPDATE todo SET completed = true WHERE id = 1')
  const updated = await db.query('SELECT * FROM todo WHERE id = 1')
  console.log('更新後狀態:', updated.rows[0])
}

realtimeExample()
```

## API 使用說明

### 主要建構函式

```javascript
import { PGlite } from '@electric-sql/pglite'

// 記憶體儲存
const db = new PGlite()

// IndexedDB 持久化（瀏覽器）
const db = new PGlite('idb://my-pgdata')

// 檔案系統持久化（Node/Bun/Deno）
const db = new PGlite('./path/to/pgdata')

// 使用靜態方法（推薦）
const db = await PGlite.create()
const db = await PGlite.create('./path/to/pgdata')
```

### 主要方法

#### `query(query, params?, options?)`

執行單一語句，支援參數。

```javascript
const result = await db.query(
  'SELECT * FROM users WHERE id = $1',
  [1],
  {
    rowMode: 'array',  // 或 'object'
  }
)
```

#### `exec(query, options?)`

執行一個或多個語句（不支援參數）。

```javascript
await db.exec(`
  CREATE TABLE test (id SERIAL PRIMARY KEY);
  INSERT INTO test VALUES (1);
  SELECT * FROM test;
`)
```

#### `transaction(callback)`

執行事務。

```javascript
await db.transaction(async (tx) => {
  await tx.query('INSERT INTO test VALUES ($1)', ['data'])
  return await tx.query('SELECT * FROM test')
})
```

#### `listen(channel, callback)`

訂閱通知通道。

```javascript
const unsub = await db.listen('test_channel', (payload) => {
  console.log('收到通知:', payload)
})

// 取消訂閱
await unsub()
```

### 其他重要方法

- `close()` - 關閉資料庫
- `dumpDataDir()` - 匯出資料庫目錄
- `clone()` - 複製當前實例
- `copyToFS(filePath, data, mode)` - 複製資料到虛擬檔案系統

## 限制與注意事項

### 已知限制

1. **單一用戶/連接**: PGlite 僅支援單一用戶/連接模式
2. **不支援進程分叉**: 基於 WebAssembly，無法像原生 Postgres 那樣進程分叉
3. **記憶體限制**: 受限於運行環境的記憶體限制

### 最佳實踐

1. 使用參數化查詢防止 SQL 注入
2. 在長時間運作的應用中定期檢查記憶體使用
3. 使用 `waitReady` 確保資料庫完全初始化後再執行查詢
4. 在測試環境中可使用 `clone()` 快速複製資料庫

## 故障排除

### 常見問題

#### 問題 1: 資料庫未準備就緒

```javascript
// 確保等待資料庫準備就緒
const db = new PGlite()
await db.waitReady  // 添加此行

// 或直接使用（query 方法會自動等待）
await db.query('SELECT 1')  // 會自動等待
```

#### 問題 2: 記憶體不足

```javascript
// 增加初始記憶體配置
const db = new PGlite({
  initialMemory: 1024 * 1024 * 100,  // 100MB
})
```

#### 問題 3: 持久化失敗

確保在持久化環境中：
- Node.js: 使用檔案系統路徑
- 瀏覽器: 使用 `idb://` 前綴
- 不要混合使用不同類型的持久化

## 參考資源

- [官方文件](https://pglite.dev)
- [GitHub 倉庫](https://github.com/electric-sql/pglite)
- [範例頁面](https://pglite.dev/examples)
- [Discord 社群](https://discord.electric-sql.com)

## 授權

PGlite 採用雙授權：
- Apache License 2.0
- PostgreSQL License

可根據需求選擇任一授權。

*報告生成日期: 2026-11-24*
*PGlite 版本: v0.5.13+*
