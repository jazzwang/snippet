# Databricks Genie Ontology

- 2026-06-16
  - Introducing Genie One, Genie Agents, and Genie Ontology
  - https://www.databricks.com/blog/introducing-genie-one-genie-ontology-and-genie-agents

## 2026-07-15

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI Mode
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
Databricks Genie Ontology
</td></tr><tr><td>A:</td><td>

Genie Ontology 是 [Databricks](https://www.databricks.com/blog/introducing-genie-one-genie-ontology-and-genie-agents) 推出的一款自動化、自我完善的企業語境層（Context Layer）。它本質上是一個動態知識圖譜（Knowledge Graph），旨在作為 AI 代理的「大腦」，讓生成式 AI 真正理解你公司的業務術語、指標定義以及數據之間的關聯性。 [1, 2, 3] 
在傳統的「與數據聊天（Chat with Data）」或 RAG（檢索增強生成）架構中，AI 常因缺乏業務背景而給出看似合理卻錯誤的答案（例如分不清財務部和銷售部對「營收」的不同定義）。Genie Ontology 就是為了解決這個信任痛點而誕生。 [4, 5] 

## 💡 核心工作原理

Genie Ontology 不需要數據工程師手動、費時地去定義複雜的語義層，而是透過以下機制自動運作： [6] 

   1. 自動知識提取：它會持續讀取您在 [Databricks 平台](https://medium.com/@sreedeepsinha/genie-ontology-databricks-new-context-layer-for-ai-agents-558d0e451d82) 內留下的「數據足跡」，包括數據表、SQL 查詢紀錄、儀表板（Dashboards）、數據管道（Pipelines），甚至是透過 [Model Model Protocol (MCP)](https://atlan.com/know/ai-agent/databricks/genie-ontology/) 連接的 50 多個外部辦公應用（如 Jira, Slack, Google Drive, SharePoint 等），從中抽取出業務規則、邏輯表達式與概念關係。 [1, 4, 7, 8] 
   2. 語義基礎（Semantic Foundation）：它會直接與 Unity Catalog Metrics 綁定，將團隊定義過一次的關鍵 KPI（如流失率、活躍用戶、淨利等）封裝為可複用的對象，讓 AI 查詢的是被驗證過的定義，而非瞎猜。 [1] 
   3. OntoRank 權威度排序：當同一個詞（例如 “Engagement”）在舊儀表板、Wiki 文檔和正式指標中有不同定義時，Genie 會使用類似 Google PageRank 的 OntoRank 演算法。它會綜合評估：誰創建的、使用頻率、與認證資產的關聯度、以及資訊的新鮮度。最終，最新的官方認證定義會勝出。 [4, 8, 9] 
   4. 安全與權限控制：在過濾出正確定義的同時，它會嚴格執行 Unity Catalog 的權限管理。如果當前用戶沒有權限查看某一項核心財務指標，Ontology 就不會將該語境提供給 AI。 [4, 8] 

## 🚀 帶來的實質效益

* 精準度大幅提升：官方內部測試顯示，有 Ontology 語境層支持的 Genie 代理，在回答數據問題時的準確度提升了 30% 以上。
* 降低 Token 成本與延遲：AI 不需要對散落的文檔碎片進行大範圍、昂貴的開放式推理。Ontology 讓 AI 能直接精準轉譯出正確的 SQL 語句去查詢驗證過的數據，運行時間縮短約一半，且大幅節省 Token 消耗。
* 賦能上層 AI 應用：它是整個 Databricks Genie 生態系底層的基石，全面支撐上層的 Genie One（面向業務團隊的 AI 數據同事）和 Genie Agents（用戶可自定義的自動化工作代理）。 [1, 3, 7, 10] 


## ⚖️ 市場定位與挑戰

在這個「語境層（Context Layer）」的技術浪潮中，Databricks 的 Genie Ontology 與微軟的 Fabric IQ、Snowflake 的相關語義更新幾乎同時推出。 [5, 6] 
不過，分析師也指出其當前的局限性：

* 跨平台治理難題：Genie Ontology 在 Databricks 湖倉（Lakehouse）內部表現極佳，但對於那些廣泛分佈在 Snowflake、Salesforce、SAP 或 dbt 等外部生態系的數據，通常需要搭配如 Atlan Context Layer 這樣的跨平台治理工具協同運作，才能達到全企業級的覆蓋。 [1, 11] 


您目前是打算利用 Genie Ontology 來優化業務團隊的自然語言數據看板查詢，還是打算用它來做自動化 AI Agents 的底層知識庫呢？我可以進一步為您說明與 Unity Catalog Metrics 整合的配置細節。 [6, 12, 13, 14] 

- [1] [https://atlan.com](https://atlan.com/know/ai-agent/databricks/genie-ontology/)
- [2] [https://datamy.co](https://datamy.co/resources/blog/ontology-renaissance-databricks-genie-ontology)
- [3] [https://www.linkedin.com](https://www.linkedin.com/posts/harshitdawar_genie-ontology-vs-genie-one-vs-genie-agents-activity-7475265506887782400-q4Sq)
- [4] [https://medium.com](https://medium.com/@sreedeepsinha/genie-ontology-databricks-new-context-layer-for-ai-agents-558d0e451d82)
- [5] [https://www.youtube.com](https://www.youtube.com/watch?v=QMJqij7ln14)
- [6] [https://www.cio.com](https://www.cio.com/article/4186154/from-rag-to-ontology-databricks-bets-on-context-as-the-key-to-trusted-ai-agents-2.html)
- [7] [https://www.youtube.com](https://www.youtube.com/watch?v=6W3BnCgoYVA&t=417)
- [8] [https://www.databricks.com](https://www.databricks.com/blog/introducing-genie-one-genie-ontology-and-genie-agents)
- [9] [https://www.typedef.ai](https://www.typedef.ai/blog/what-is-genie-ontology-databricks-continuously-learned-context-layer-explained)
- [10] [https://www.databricks.com](https://www.databricks.com/blog/introducing-genie-one-genie-ontology-and-genie-agents)
- [11] [https://atlan.com](https://atlan.com/know/ai-agent/databricks/genie-ontology/)
- [12] [https://www.youtube.com](https://www.youtube.com/watch?v=6W3BnCgoYVA&t=417)
- [13] [https://www.heise.de](https://www.heise.de/en/news/Databricks-Genie-One-AI-agent-to-derive-answers-from-company-data-11337020.html)
- [14] [https://www.reddit.com](https://www.reddit.com/r/AI_Agents/comments/1utgab3/the_engineering_behind_genie_ontology_makes_data/)

</td></tr>
</table>