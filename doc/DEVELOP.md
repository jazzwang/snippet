# DEVELOPMENT NOTES

[TOC]

## 2024-06-29

### Vector Database

- 2024-06-29 22:01:08

- Goal #1: pgvector 安裝
    - Action #1: 用 docker-compose + Dockerfile 實作自動化
- Goal #2: get started pgvector 使用
    - Referemce: 
- Questions:
    - Q1: 有 embedding 的 data type 嗎？
    - Q2: 透過 Schema 設計能做到反查資料來源？(e.g. 若以某個網址為例)
    - Q3: PostgreSQL 可以靠 Role-based Access Control 或 fine-grained access control 控制查詢結果嗎？
    - Q4: PostgreSQL 的加密 Encryption 與 稽核 Audit 是否有 Best Practice