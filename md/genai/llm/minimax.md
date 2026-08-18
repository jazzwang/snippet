# MiniMax

## MiniMax M2

- News
  - 2025-10-27
    - MiniMax M2 & Agent，大巧若拙
    - https://www.minimaxi.com/news/minimax-m2
  - 2025-10-28
    - MiniMax M2：為何說它是 LLM 模型性價比之王？
    - MiniMax M2: Why is it the king of cost-effectiveness for LLM models?
    - https://www.cometapi.com/zh-TW/minimax-m2-why-is-it-the-king-of-cost-effectiveness-for-llm/
- HuggingFace
  - https://huggingface.co/MiniMaxAI/MiniMax-M2
- GGUF
  - https://huggingface.co/unsloth/MiniMax-M2-GGUF
- Git Repo
  - https://github.com/MiniMax-AI/MiniMax-M2

## MiniMax H3

- Git Repo
  - https://github.com/MiniMax-AI/MiniMax-H3

### 2026-08-07

- Source: https://www.youtube.com/watch?v=UXEjocWEfiM

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Notebook LM
</td></tr><tr><td>A:</td><td>

### MiniMax H3 開源影片生成模型技術簡報

本報告針對最新開源的 **MiniMax H3** 影片生成模型進行深度分析，涵蓋其技術優勢、效能表現、硬體需求及本地部署流程。該模型被視為開源社群在 AI 影片生成領域的重大突破，具備極高的創意控制力與電影級質感。

#### 1. 執行摘要 (Executive Summary)

MiniMax H3 是一款正式開放原始碼且可免費下載的影片生成模型，標榜「人人皆可在本地部署」。該模型在 **Video Arena** 排行榜中位居開源模型首位，其生成品質已逼近 Seedance 2.0 等頂尖閉源模型。MiniMax H3 的核心亮點在於其強大的整合工作流（涵蓋文本、圖像、音頻、角色參考等）以及對硬體的高度適應性，最低僅需 8GB 顯存即可運行。此外，社群推出的「越獄版」模型進一步解除內容限制，為創作者提供極大的發揮空間。

#### 2. 核心功能與競爭優勢分析

##### 2.1 卓越的市場排名

根據 Video Arena 的最新數據，MiniMax H3 在多項指標上均表現優異：

*   **圖生影片 (Image-to-Video)：** 得分 1476 分，位居排行榜首位，與頂尖閉源模型 Seedance 2.0 僅有 2 分之差。
*   **文生影片 (Text-to-Video)：** 得分 1455 分，在開源模型中排名第一。

##### 2.2 全方位的工作流整合

MiniMax H3 展現了極高的精確度與創意控制，能將以下元素整合至單一工作流中：

*   文本、圖像、影片、音訊輸入。
*   角色參考 (Character Reference) 與相機移動 (Camera Movement) 控制。
*   語音克隆 (Voice Cloning)。
*   自帶高品質音效配音，實現音畫同步的一站式生成。

##### 2.3 高度可控的電影質感

該模型生成的影片具備「電影級」質感，特別是在人物臉部特寫與細節刻畫上非常清晰，能達到類似真人拍攝的效果。其應用場景廣泛，包括廣告創建、音樂影片 (MV)、品牌內容、遊戲開發及電影製作。

#### 3. 模型版本與硬體需求

MiniMax H3 提供多種精度的版本，以適應不同層次的硬體設備：

| 模型版本 | 檔案大小 | 說明 | 顯存建議 |
| :--- | :--- | :--- | :--- |
| **BF16 完整版** | 50GB+ | 最高畫質，精度最高 | 高階顯卡 (如 3090/4090) |
| **量化版本 (Quantized)** | 26.4GB | 主流推薦版本，兼顧效能與品質 | 12GB - 16GB 顯存 |
| **FP4 量化版** | 較小 | 專為低顯存優化 | **8GB 顯存** (最低門檻) |
| **尾部模組 (Tail Module)** | 7.6GB | 用於越獄版生成的必要組件 | 需搭配主模型使用 |

*註：若 Windows 系統顯存不足，可透過設置虛擬內存來協助運行。*

#### 4. 本地部署流程指南

部署 MiniMax H3 主要透過 **ComfyUI 桌面客戶端** 進行。

##### 4.1 官方版部署步驟

1.  **安裝 ComfyUI：** 下載並完成客戶端安裝。
2.  **下載模型：** 在左側模板中心進入「視頻」分類，下載 MiniMax H3 的圖生影片、參考生成影片及文生影片模型。
3.  **運行測試：** 輸入提示詞並設置長度（如 15 秒），系統會自動生成含音效的影片。

##### 4.2 越獄版（無限制版）特殊配置

越獄版需要手動配置自定義節點與模型存放路徑：
1.  **放置自定義節點：** 
    *   路徑：`C:\Users\[用戶名]\AppData\Local\ComfyUI_desktop\app\ComfyUI\custom_nodes`
2.  **放置模型文件：**
    *   路徑：`C:\Users\[用戶名]\AppData\Local\ComfyUI_desktop\app\ComfyUI_shared\models\text_encoders` (放入下載的越獄模型文件)。
3.  **導入工作流：** 重啟客戶端後，導入專屬的越獄版 JSON 工作流。

#### 5. 重要引言與上下文

> 「這可能是我迄今為止用過的、最可控的 AI 視頻生成模型之一。最讓我印象深刻的，不僅僅是電影般的質感，而是它能輕鬆將文本、圖像、視頻、音頻、角色參考、相機移動、甚至語音克隆，整合到一個工作流中。」

*   **上下文：** 這是對 MiniMax H3 技術領先性的評價，強調其在「精確度」與「創意控制」上的進步。

> 「無論是文生視頻，還是圖生視頻都位居榜首……這絕對是開源模型的一個巨大進步。」

*   **上下文：** 引用 Video Arena 的客觀評分數據，證明 MiniMax H3 已縮小了與閉源模型之間的差距。

#### 6. 效能實測表現

*   **生成效率：** 在實測中，生成一段 15 秒的 864x480 分辨率影片（含配音與特效）大約需要 **6 分鐘**。
*   **視覺品質：** 人物特寫清晰，轉場自然，音效與畫面配合度高。
*   **優化建議：** 
    *   **解析度策略：** 建議先以較低解析度（如 0.4 倍率）生成以縮短等待時間。
    *   **後期處理：** 影片生成後，配合使用免費的「影片高清放大工具」進行後期高級放大，以獲得最佳觀看體驗。

#### 7. 行動建議 (Actionable Insights)

1.  **硬體門檻評估：** 對於顯存僅有 8GB 的用戶，應優先下載 **FP4 量化版** 模型以確保穩定運行。
2.  **內容創作策略：** 對於需要極大創意空間（如特殊題材）的用戶，建議部署「越獄版」模型以繞過官方限制。
3.  **效率提升：** 建議將 MiniMax H3 作為初剪工具，利用其一次性生成音效與畫面的特性，快速產出廣告或短片原型，再輔以高清放大工具進行精修。
</td></tr>
</table>
