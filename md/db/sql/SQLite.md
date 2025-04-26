# SQLite

## 2024-12-13

- 緣起：
  - 先前曾評估過使用 PostgreSQL 的 pgvector (或比較新的 [pgai](https://github.com/timescale/pgai)) 來當作 RAG 的 vector store，但對於一些比較輕量級的 POC 應用，若能用 SQLite 會比較容易移植到 Serverless (Container) 環境。所以查了一下 SQLite 有哪些支援 vector similarity 的實作。
- 查了一下，發現主要有
  - https://github.com/asg017/sqlite-vec
    - 繼承自 https://github.com/asg017/sqlite-vss (基於 Facebook 的 [`Faiss`](https://faiss.ai/))
  - 2024-06-05: [Turso brings Native Vector Search to SQLite](https://turso.tech/blog/turso-brings-native-vector-search-to-sqlite) - Vector Similarity Search is now available!
    - 基於 [libSQL](https://github.com/tursodatabase/libsql) - the Open Contribution fork of SQLite
    - https://turso.tech/libsql
      - https://turso.tech/libsql-manifesto 開發宣言
    - https://turso.tech/vector
      > Native Vector Search for SQLite - No extensions needed.
- 在 libSQL 開發宣言中提到了另外幾個延伸 SQLite 變成分散式資料庫的實作
  - ChiselStore - https://github.com/chiselstrike/chiselstore
    - ChiselStore is an embeddable, distributed SQLite for Rust, powered by Little Raft.
  - rqlite
    - https://github.com/rqlite/rqlite
    - https://rqlite.io/
    > The lightweight, user-friendly, distributed relational database built on SQLite.
  - dqlite
    - https://github.com/canonical/dqlite
    - https://dqlite.io/
    > High-availability SQLite

## 2025-04-26

- 目標：讀取分隔符號是 `TAB (\t)` 字元的檔案
- 參考：https://sqlite.org/forum/forumpost/6b41812741
- 可能作法：
```sql
.mode csv
.separator '\t'
.import file table
```
- 實測一下：
```bash
@jazzwang ➜ /workspaces/codespaces-blank (main) $ printf "Col1\tCol2\tCol3\nA\tB\tC\nD\tE\tF\n" > sample.tsv
@jazzwang ➜ /workspaces/codespaces-blank (main) $ cat sample.tsv
Col1    Col2    Col3
A       B       C
D       E       F
@jazzwang ➜ /workspaces/codespaces-blank (main) $ 
@jazzwang ➜ /workspaces/codespaces-blank (main) $ sudo apt -y install sqlite3
@jazzwang ➜ /workspaces/codespaces-blank (main) $ sqlite3 test.db
SQLite version 3.45.3 2024-04-15 13:34:05
Enter ".help" for usage hints.
sqlite> .mode csv
sqlite> .separator '\t'
sqlite> .import sample.tsv sample
Error: multi-character column separators not allowed for import
sqlite> .separator "\t"
sqlite> .import sample.tsv sample
sqlite> .schema
CREATE TABLE IF NOT EXISTS "sample"(
"Col1" TEXT, "Col2" TEXT, "Col3" TEXT);
sqlite> select * from sample;
A       B       C
D       E       F
sqlite> .quit
@jazzwang ➜ /workspaces/codespaces-blank (main) $
```
- 結果居然卡在單引號跟雙引號的差異，還是動用到 Gemini 解答，哈～
  - https://g.co/gemini/share/4970a3797ead