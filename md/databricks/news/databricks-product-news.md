# Databricks Product News

## 2026-08-14

- From Erik
- 2026-08-13
  - Smart Routing in Unity AI Gateway: Match frontier quality with 30%+ lower cost per task
  - https://www.databricks.com/blog/smart-routing-unity-ai-gateway-match-frontier-quality-30-lower-cost-task
> Databricks 推出 Unity AI Gateway「智慧路由（Smart Routing）」測試版功能，能根據編碼任務複雜度自動選擇適用模型，在保持頂尖模型品質的同時，顯著降低 30% 以上成本。該技術結合「任務感知路由」與 Omnigent 框架，將簡單任務交由快速低成本模型，有效提升每美元的 AI 生產力。深入了解該功能請造訪 [Databricks 官方部落格](https://www.databricks.com/blog/smart-routing-unity-ai-gateway-match-frontier-quality-30-lower-cost-task)。 [1, 2] 
>
> [1] [https://www.databricks.com](https://www.databricks.com/blog/smart-routing-unity-ai-gateway-match-frontier-quality-30-lower-cost-task)
> [2] [https://www.databricks.com](https://www.databricks.com/blog/smart-routing-unity-ai-gateway-match-frontier-quality-30-lower-cost-task)

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search AI Mode
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
</td></tr><tr><td>A:</td><td>

[Databricks](https://www.databricks.com/blog/smart-routing-unity-ai-gateway-match-frontier-quality-30-lower-cost-task) 推出 Unity AI Gateway「智慧路由（Smart Routing）」功能，透過任務感知與 Omnigent 元框架整合，在編碼任務中動態媒合最經濟模型。此機制能在維持前沿模型品質的同時，實現高達 56% 的成本節約，並優化生產力。 [1, 2, 3] 

```markmap.js
# Databricks 智慧路由 (Smart Routing)

## 核心痛點
### 模型爆發與選擇過載
- 2026 年已釋出超過 33 個新模型
- 開發者傾向直接選擇最貴的頂尖模型
- 導致日常簡單任務花費不必要的高昂成本
### 傳統控管缺點
- 手動配置費時，且增加認知負載
- 限制預算硬上限會阻礙開發者生產力

## 智慧路由機制 (Smart Routing)
### 平台定位
- 整合於 Unity AI Gateway 平台 (目前為 Beta 測試版)
- 模型選擇權由應用層移轉至平台層控管
### 技術實現：任務感知路由 (Task-aware routing)
- 會話開始時，由快、省的小模型先分析任務中繼資料
- 依據程式碼脈絡、系統領域、錯誤類型進行任務分類
- 動態媒合最經濟且足夠勝任的模型
- 保持模型快取 (Cache) 效率，優化推理成本

## 跨層級擴充：Omnigent 整合
### 元框架角色
- 位於個別編碼會話之上的協調層
### 雙重最佳化
- 同步動態選擇「最佳模型」與「最佳編碼框架 (Harness)」
- 例如：簡單總結交給低成本模型；架構設計交給頂尖模型

## 顯著效益
### 成本大幅降低
- 整體平均節省 30% 以上的編碼任務成本
- Databricks 內部測試：成本節省 35% (相比頂尖前沿模型)
- 公開基準測試：成本節省高達 56%
### 生產力與資源優化
- 免去開發者手動評估與切換模型的時間
- 優化「每美元帶來的生產力輸出」，而非單純優化 Token 量
- 保留稀缺的前沿模型算力給真正需要的複雜任務

## 當前挑戰與未來研究
### 基準測試落差
- 公開測試集過於理想化，與真實使用者行為不符
### 邊界狀況優化
- 初始提問過於模糊的引導
- 會話重複利用
- 會話中途切換模型的昂貴成本

```

請至 Databricks 官方部落格 閱讀原文。

[1] [https://alphasignal.ai](https://alphasignal.ai/news/databricks-smart-routing-cuts-ai-coding-costs-by-56-without-sacrificing-quality)
[2] [https://www.startuphub.ai](https://www.startuphub.ai/ai-news/artificial-intelligence/2026/databricks-cuts-ai-costs-with-smart-routing)
[3] [https://www.databricks.com](https://www.databricks.com/blog/smart-routing-unity-ai-gateway-match-frontier-quality-30-lower-cost-task)

</td></tr>
</table>