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