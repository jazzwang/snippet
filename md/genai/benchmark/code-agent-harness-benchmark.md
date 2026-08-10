# Coding Agent Harness Benchmark

## 2026-08-04

- Learn from ZhuLin when we evaluate token efficiency of different AI Coding Agents.
- 2026-04-28
  - [WIP] Benchmarking Local LLMs Against Coding Agent Harnesses
  - https://neuralnoise.com/2026/harness-bench-wip/

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search AI Mode
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
https://neuralnoise.com/2026/harness-bench-wip/ 幫我用 markmap.js syntax 整理一份中文的心智圖，並附上中文摘要
</td></tr><tr><td>A:</td><td>

Harness-Bench 是一個針對 LLM Agent 系統外殼（Harness）配置效果的診斷性基準測試，包含 106 個沙盒化離線任務，旨在評估真實開發場景下「模型 + 外殼」的組合效能。此基準測試強調將外殼管理視為獨立維度，透過相同的任務環境與資源約束，診斷系統的魯棒性與高效率執行能力。詳情請參閱 [arXiv 論文](https://arxiv.org/abs/2605.27922)。 [1, 2, 3] 

### 🚀 Harness-Bench 核心架構與評估機制

#### 📌 什麼是 Harness（系統外殼）？- **系統層角色**
  - 管理 Prompt 上下文與 Token 預算
  - 協調外部工具調用與權限管理
  - 維持工作區狀態與記憶維護
  - 錯誤追蹤與異常修復機制- **核心觀點**
  - 💡 **AI 智慧體能力 = 底層模型 + 外殼配置**
  - 效能表現不能單純歸功於底層模型
#### 🎯 傳統基準測試的痛點- **缺乏執行層度量**
  - 抽象化了程式碼或環境的實際執行過程- **邊界模糊**
  - 容易將外殼層與完整的智慧體系統混為一談- **配置固定**
  - 在對比不同模型時將外殼固定，難以研究外殼配置的變異效應
#### 🛠️ Harness-Bench 設計特點- **共享測試環境**
  - 統一的任務環境、權限及預算上限- **保留原生行為**
  - 在外部條件一致下，允許各個外殼維持其內部特有的編排與執行邏輯- **多維度診斷**
  - 不僅看最終成功率，還分析 Token 成本、魯棒性與可追蹤性
#### 📋 任務數據庫與驗證- **數據規模**
  - 包含 106 個沙盒化的離線任務- **任務來源**
  - 根據實際 AI 智慧體使用模式構建- **人工審查標準**
  - 真實性（Realism）
  - 可解性（Solvability）
  - 驗證合規性（Oracle-checkability）
  - 數據完整性（Integrity）
#### 📊 數據記錄與分析- **執行證據追蹤**
  - 最終生成的產物檔案
  - 完整的執行軌跡日誌（Traces）
  - API 與 Token 使用量統計
  - 驗證器（Validator）輸出結果- **解決對齊失敗**
  - 診斷「合理解理」與「工具反饋/工作區狀態」脫節的執行對齊問題

[1] [https://arxiv.org](https://arxiv.org/abs/2605.27922)
[2] [https://cobusgreyling.medium.com](https://cobusgreyling.medium.com/agent-model-harness-0d018f3d5014)
[3] [https://arxiv.org](https://arxiv.org/html/2605.27922v1)

</td></tr>
</table>