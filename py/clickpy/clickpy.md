# ClickPy

- Git Repo
  - https://github.com/ClickHouse/clickpy
- Website
  - https://clickpy.clickhouse.com

## 2025-11-18

- 緣起：
  - 印象在某一篇文章看到 Clickhouse 的這個服務，可以用來觀察 PyPI 上套件的下載次數與趨勢
  - 今天想要比較 aider-chat (PyPI) 跟 claude-code (Antronic), gemini-cli (Google), opencode-ai (HuggingFace CTO 推薦), 甚至 (OpenAI) Codex 等的「下載量」趨勢。
- Aider 的歷史下載量
  - https://clickpy.clickhouse.com/dashboard/aider-chat
- 思路：
  - 先用 DeepWiki 分析一下 ClickPy 背後是怎麼取得套件的資料
- DeepWiki
  - https://deepwiki.com/ClickHouse/clickpy
- 結論：
  - 資料源是 BigQuery Public Data 700B rows -> 存到 GCS Parquet (15TB), 再 load 進 ClickHouse
  - 感覺上除了 BigQuery Public Data 外，還有另外設計一條 incremental update (遞增更新) 的機制
- 感想：
  - 這是個有趣的 Data Engineering 範例 + Data Analysis & Data Visualization 應用
