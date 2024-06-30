# DEVELOPMENT NOTES

[TOC]

## 2024-06-29

### Embedding Visualization

#### t-SNE (t-distributed stochastic neighbor embedding)

- https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding
    - scikit-learn, a popular machine learning library in Python implements t-SNE with both exact solutions and the Barnes-Hut approximation.
    - 從 https://www.kaggle.com/code/colinmorris/visualizing-embeddings-with-t-sne/notebook 可以看到 scikit-learn 有 t-SNE 的實作
    ```python
    from sklearn.manifold import TSNE
    ```
    - https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html
- https://lvdmaaten.github.io/tsne/
- https://towardsdatascience.com/neural-network-embeddings-explained-4d028e6f0526
    - https://github.com/lmcinnes/umap

### Vector Database

- 2024-06-29 22:01:08

- Goal #1: pgvector 安裝
    - Action #1: 用 docker-compose + Dockerfile 實作自動化
    - https://github.com/pgvector/pgvector?tab=readme-ov-file#installation
    - https://ithelp.ithome.com.tw/m/articles/10328071
- Goal #2: get started pgvector 使用
    - https://github.com/pgvector/pgvector?tab=readme-ov-file#getting-started
    - 範例裡給的是三維的向量。
    - https://github.com/pgvector/pgvector?tab=readme-ov-file#querying
    - 基本的 Query
- Questions:
    - Q1: 有 embedding 的 data type 嗎？
        - A: https://github.com/pgvector/pgvector?tab=readme-ov-file#getting-started 看起來就是 `vector`
    - Q2: 透過 Schema 設計能做到反查資料來源？(e.g. 若以某個網址為例)
    - Q3: PostgreSQL 可以靠 Role-based Access Control 或 fine-grained access control 控制查詢結果嗎？
        - https://www.postgresql.org/docs/current/ddl-rowsecurity.html
    - Q4: PostgreSQL 的加密 Encryption 與 稽核 Audit 是否有 Best Practice
        - https://www.enterprisedb.com/postgresql-best-practices-encryption-monitoring

### Ollama

- https://github.com/ollama/ollama

### vLLM

- https://github.com/vllm-project/vllm
- https://docs.vllm.ai/en/stable/

## 2024-06-30

### pgvector + pgvectorscale vs pinecone

- 本來想說來比較一下 pgvector 跟 pinecone 兩個效能會差多少呢？
- 2024-04-17 : [Pinecone vs. Postgres pgvector: For vector search, easy isn’t so easy](https://www.pinecone.io/blog/pinecone-vs-pgvector/)
    - 本文提到了一些 pgvector 的缺點，像是用 HNSW index 太耗費記憶體（所以成本太高）
- 2024-06-13: [Pgvector vs. Pinecone: Vector Database Performance and Cost Comparison](https://www.timescale.com/blog/pgvector-vs-pinecone/)
    - 結果六月 Timescale 開發了 [pgvectorscale](https://github.com/timescale/pgvectorscale)
- 2024-06-27: [PostgreSQL and Pgvector: Now Faster Than Pinecone, 75% Cheaper, and 100% Open Source](https://www.timescale.com/blog/pgvector-is-now-as-fast-as-pinecone-at-75-less-cost/)
    - 宣稱

- ANN-Benchmarks is a benchmarking environment for approximate nearest neighbor algorithms search
    - https://ann-benchmarks.com/
    - 實作: https://github.com/erikbern/ann-benchmarks/

### more fun stuff from TimeScale

- [How to Collapse Your Stack Using PostgreSQL for Everything](https://www.timescale.com/blog/how-to-collapse-your-stack-using-postgresql-for-everything/)
- https://github.com/timescale/timescaledb - 在 https://db-engines.com/en/system/PostgreSQL 只有列到 Document store, Graph DBMS, Spatial DBMS, Vector DBMS。TimeScale 讓 PostgreSQL 變成 time-series SQL database，挺有趣的。真的是「多模態 Multimodal 資料庫」，而且用 extension 的方式存在，確實有種讓 PostgreSQL 能適應各種應用場景的感覺。