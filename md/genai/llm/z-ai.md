# GLM

智譜 AI (Zhipu AI)

[TOC]

## GLM 4.5

- 2025-07-28:
  - https://z.ai/blog/glm-4.5
- 2025-08-06:
  - GLM-4.5: Agentic, Reasoning, and Coding (ARC) Foundation Model
  - https://arxiv.org/abs/2508.06471
- HuggingFace
  - https://huggingface.co/zai-org/GLM-4.5
- Document
  - https://zhipu-ai.feishu.cn/wiki/Gv3swM0Yci7w7Zke9E0crhU7n7D
- Git Repo
  - https://github.com/zai-org/GLM-4.5

## GLM 4.6

- 2025-09-30
  - GLM-4.6: Advanced Agentic, Reasoning and Coding Capabilities
  - https://z.ai/blog/glm-4.6
- HuggingFace
  - https://huggingface.co/zai-org/GLM-4.6
- GGUF
  - https://huggingface.co/unsloth/GLM-4.6-GGUF
- 2025-11-10T13:51:47.178Z
  - GLM-4.6: How to Run Locally
  - https://docs.unsloth.ai/models/glm-4.6-how-to-run-locally

## GLM 5.2

- https://docs.z.ai/guides/llm/glm-5.2
- HuggingFace
  - https://huggingface.co/zai-org/GLM-5.2
- Git Repo
  - https://github.com/zai-org/GLM-5
- GGUF
  - https://huggingface.co/unsloth/GLM-5.2-GGUF

### 2026-06-23

- Source: https://www.youtube.com/watch?v=jP_NTND4EKs

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
NotebookLM
</td></tr><tr><td>A:</td><td>

### GLM 5.2 開源旗艦模型技術簡報

本簡報旨在分析最新發布的 GLM 5.2 旗艦大模型。該模型作為全球首個在特定測試中突破 80% 成績的開放權重模型，標誌著開源模型在 Agent 编程與長文本處理能力上已進入全球頂尖梯隊，甚至在多項指標上超越了傳統的閉源模型。

#### 執行摘要

GLM 5.2 的發布徹底改變了開發者對於開源模型「僅能追趕」的刻板印象。該模型不僅在 Agent 能力測試中衝入全球前三，更實現了穩定的「百萬級上下文（1 Million Tokens）」處理能力。其實際應用測試涵蓋了從高度複雜的遊戲開發（如 Minecraft、GTA 風格遊戲）到 3D 交互場景與專業網站設計。然而，其強大性能伴隨著極高的硬體門檻，滿血版模型大小接近 1TB，對本地部署提出了巨大的挑戰。

#### 核心主題詳細分析

##### 1. 全球領先的開源效能與 Agent 格局轉變
GLM 5.2 在技術指標上取得了重大突破，打破了過往最強 Agent 歸屬於 OpenAI、最強編程歸屬於其餘閉源模型的壟斷局面。
*   **基準測試表現：** 在相關測試（如 HumanEval 等編程測試）中，它是全球首個突破 80% 分數的開放權重模型。
*   **Agent 實力：** 在 BCH 的 Agent 測試中，GLM 5.2 進入全球前三名，與頂尖模型並列第一梯隊。這顯示開源模型已具備與頂級閉源模型正面競爭的實力。

##### 2. 百萬級（1M）穩定長文本能力

相較於許多僅將長文本作為宣傳噱頭的模型，GLM 5.2 強調的是「穩定運行」。

*   **應用場景：** 用戶可同時輸入長篇小說、大型項目代碼庫或多個文檔資料庫。
*   **長週期任務優化：** 該模型專為需要連續工作數小時甚至數天的長週期任務設計，解決了傳統模型在處理數十萬 token 後容易「遺忘」前文的問題。這對於未來 AI Agent 執行複雜工作流至關重要。

##### 3. 多維度 Agent 編程與實測表現

根據實測數據，GLM 5.2 的核心競爭力在於「實作」而非僅僅是「聊天」。

| 測試項目 | 實測效果描述 | 技術亮點 |
| :--- | :--- | :--- |
| **Minecraft 遊戲開發** | 生成可運行的遊戲架構。 | 支援跳躍、方塊切換與場景交互，功能完整。 |
| **3D 清明上河圖** | 基於 Three.js 構建 3D 交互場景。 | 成功重現虹橋、城門等元素；支援視角拖拽與漫遊模式。 |
| **機場飛行模擬** | 包含專業跑道、座艙視角與飛行控制。 | 支援油門控制（W 鍵）、轉彎、翻轉與視角切換，功能全正常。 |
| **地鐵 FPS 遊戲** | 構建具有音效與迷宮地圖的射擊遊戲。 | 具備動態腳本能力，包含射擊機制與地圖導覽。 |
| **網頁與 UI 設計** | 設計專業射箭網站官網。 | 自動配置文案、會員套餐方案與響應式布局，視覺風格成熟。 |

*註：在 3D 場景測試中仍存在部分邏輯瑕疵，例如人物穿牆或位移異常，但整體產出效率與準確率已極高。*

##### 4. 本地部署要求與硬體挑戰
雖然模型開源，但其部署門檻對個人用戶而言極高。

*   **部署架構支援：** 支援 SGL（推薦用於 Agent 部署，推理速度最佳）、vLLM 與 Transformers（如 Llama.cpp、Ollama）。
*   **硬體規格需求：**
    *   **滿血版：** 模型大小約 1TB。
    *   **FP8 量化版：** 大小約 740GB，需 8 張 H200 或 H100 顯卡方可部署。
    *   **Q4 量化版：** 顯存要求約 240GB 至 280GB，需 Mac Studio M 級別版本或 RTX 4090 搭配 256GB 記憶體方可運行。
    *   **最低量化門檻：** 即使是最低精度量化，仍需至少 180GB 顯存。

#### 關鍵引述與背景

> 「這一次做的優化就是長週期任務。簡單來說，你可以把一邊小說、一個大型項目代碼庫，甚至是多個文檔資料庫同時塞進去。」

*   **背景：** 針對 GLM 5.2 百萬上下文能力的實用性說明，強調其在長度與穩定性上的提升。

> 「未來 AI 競爭的核心已經不但只是誰更會聊天，而是誰更會幹活。」

*   **背景：** 分析 AI 發展趨勢，指出 Agent 的執行能力（如編程、自動化工作流）已成為衡量旗艦模型的新指標。

> 「如果放（在）兩年前的話，幾乎是不可想像的事情。因為目前大家普遍認為最強 Agent 一定屬於 OpenAI……但現在這個格局真正發生了變化。」

*   **背景：** 評論 GLM 5.2 在全球 Agent 測試中取得前三名對產業格局的衝擊。

#### 行動洞察與建議

1.  **企業端戰略調整：** 由於 GLM 5.2 具備極強的代碼理解與 Agent 執行力，企業應考慮將其應用於大型代碼庫維護、複雜文檔自動化分析等長週期任務。
2.  **部署決策：**
    *   對於多數個人或中小型開發團隊，建議優先使用 **API 調用**。
    *   除非有極高的數據隱私需求且具備百萬級硬體預算，否則不建議輕易嘗試本地部署滿血版。
3.  **開發者測試建議：** 可先透過 Hugging Face 等平台進行免費測試。在編程任務中，應充分利用其長上下文特性，將整個項目的 context 同時輸入，以獲得更精確的代碼生成結果。
4.  **技術選型：** 部署時若追求推理速度與信令效率，首選 **SGL** 架構，這對發揮 GLM 5.2 的 Agent 潛力至關重要。

</td></tr>
</table>