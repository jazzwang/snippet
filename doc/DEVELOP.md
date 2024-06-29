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