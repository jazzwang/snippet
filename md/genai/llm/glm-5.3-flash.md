# GLM-5.3-Flash 技術摘要

> 來源：[GLM-5.3-Flash: Frontier Intelligence, Flash Cost](https://z.ai/blog/glm-5.3-flash)
> 發佈日期：2026-08-26
> 開發者：智譜 AI（Z.ai）

## 概述

GLM-5.3-Flash 是 GLM-5 系列首個**原生多模態模型**，總參數量 320B，激活參數僅 18B（MoE 架構）。在多項基準測試中超越 GLM-5.2，且推理成本僅為其十分之一，編程與 Agent 能力接近 Claude Opus 4.8。模型權重以 MIT 授權在 [Hugging Face](https://huggingface.co/zai-org/GLM-5.3-Flash) 開源。

## 核心性能

- **Artificial Analysis Intelligence Index v4.1.1**：57 分，每任務成本僅 $0.045（折扣價），達到前沿模型能力區間
- **編程基準**：
  - Terminal Bench 2.1：84.3（Claude Opus 4.8 為 85.0）
  - DeepSWE v1.1：63.4（GLM-5.2 為 46.2，提升顯著）
  - NL2Repo：56.3
- **Agent 基準**：
  - Toolathlon Verified：78.4
  - AutomationBench v1.0.6：48.8（GLM-5.2 為 26.2）
  - Agents' Last Exam：26.3
- **Z.ai Code Bench v1.0**：在最大努力等級下得分 29.0，接近 Claude Opus 4.8 的 29.5
- **視覺基準**：CharXiv Reasoning 89.4、Chartography 78.0、MMVU 80.5

## 架構創新

### 混合注意力機制（線性 + 稀疏）

GLM-5.3-Flash 首次在 GLM 系列中引入**線性注意力與稀疏注意力的混合架構**：

- **線性注意力**：透過狀態建模捕捉局部依賴
- **稀疏注意力**：透過輕量級索引器（indexer）檢索全域上下文
- **IndexPool**：將四個索引器的 key 向量透過加權池化壓縮為一個，降低 1M token 上下文長度下的延遲與記憶體開銷

與 GLM-5.3 相比：注意力計算量降低 **3.0 倍**，KV 快取減少 **4.4 倍**。

### 流形約束超連接（mHC）

採用 **Manifold-Constrained Hyper-Connections（mHC）** 技術，提升模型的 Scaling 效率。

### 極致效率設計

| 項目 | GLM-4.5 | GLM-5.3-Flash |
|------|---------|---------------|
| 總參數 | 355B | 320B |
| 激活參數 | 32B | 18B |
| 層數 | 92 | 45 |

在類似總參數規模下，激活參數與層數均接近減半。

## 視覺智慧融入編程迴路

GLM-5.3-Flash 將視覺能力原生整合至編程流程中：

- **視覺自我評估**：模型可渲染輸出、檢視使用者實際看到的畫面、辨識視覺問題並修改底層程式碼
- **資料合成管線**：專為視覺編程開發，聚焦於視覺自評估與測試時改進
- **強化學習 + 環境回饋**：前端編程任務中透過 Agent 基礎的驗證機制，根據真實使用者流程進行 GUI 評估
- 支援 **Browser Use Agent（BUA）** 與 **Computer Use Agent（CUA）**，可操控瀏覽器與桌面應用

應用場景涵蓋前端開發、遊戲開發、3D 模擬、簡報製作、Office 文件處理與金融研究工作流。

## 中國 AI 晶片大規模部署

GLM-5.3-Flash 已在國產 AI 晶片叢集上進行大規模推理部署：

- 基於 **SGLang** 建構專用推理引擎
- 使用 GLM-5.3 驅動的基礎設施 Agent 協助工程師開發與優化核心程式
- 採用 **EPD 分離式架構**（Encode–Prefill–Decode），將多模態編碼、提示預填充與逐 token 解碼拆分為可獨立排程的工作池
- 優化技術：W8A8 量化、混合 INT8/FP8/BF16 快取量化、ReplaySSM、Layer Split
- 端到端推理效能提升 **3 倍**，達到與主流 NVIDIA GPU 相當的硬體效率與每 token 成本

## 定價與使用

- **API 價格**：輸入 $0.15 / 輸出 $0.50（每百萬 token），推廣期五折至 2026 年 9 月 9 日
- **上下文視窗**：1M tokens
- **配額**：GLM Coding Plan 使用者可用配額為 GLM-5.3 的 3 倍
- **部署支援**：SGLang、vLLM、TokenSpeed
- 發佈前曾以匿名代號 `ox-alpha` 在 OpenCode 及 OpenRouter 上測試，迅速成為當週最受歡迎模型

## 結論

GLM-5.3-Flash 證明前沿智慧不必伴隨前沿成本。其成功源於三層協同：更高效的混合注意力架構、更豐富的 30T token 多模態預訓練語料庫，以及與推理硬體協同設計的基礎設施。智譜正將此技術路線擴展至更大規模的下一代前沿模型。
