# ADK Crash Course - From Beginner To Expert

- https://codelabs.developers.google.com/onramp/instructions
- read from
  - 2025-11-28
  - Google 免費課教你：如何從零基礎打造 AI 代理！8 堂實用 ADK 課程大綱一次看 
  - https://www.bnext.com.tw/article/85310/google-adk-free-class

> 只要具備一個 Google 帳號即可開始開始學習（首次使用 Google Cloud 的用戶可選擇 3 個月的免費試用，並享有抵免額 $9,180）。

課程共有以下 8 堂課：

| 項目 | 課程名稱 | 課程內容 |
| --- |  --- |  --- |
| 前置作業 | 設定 Google Cloud Platform 和 Gemini API 金鑰 | 基礎環境設定，提供 [Google Cloud 專案](https://console.cloud.google.com/welcome/new?project=rugged-cooler-479502-n5&pli=1)和存取 Gemini 強大模型的 API 金鑰。 |
| 第 1 堂課 | 使用 Runner 建立第一個代理程式 | 建立簡單代理程式 `day_trip_agent` ，介紹代理程式、工作階段、執行器三個核心元件。 |
| 第 2 堂課 | 自訂工具 | 從 Python 函式建立工具，學習如何透過函式說明字串（docstring），讓 LLM 判斷何時及如何使用工具。 |
| 第 3 堂課 | 將代理程式做為工具（Agent-as-a-Tool） | 建構複雜系統的強大模式。主要代理程式（協調器）將工作委派給其他更專注的代理程式，實現模組化與可重複使用。 |
| 第 4 堂課 | 代理程式記憶體（Agent Memory） | 透過適當的工作階段管理，讓代理程式記住對話內容、瞭解背景資訊，並根據意見回饋調整（這類具備記憶的代理程式在 ADK 中也常被稱為稱為「迴圈代理程式」）。 |
| 第 5 堂課 | 路由器代理程式（The Router Agent） | 擔任「主要」調度員，分析使用者查詢，並將其轉送給最適合處理的專業代理團隊，本身不直接回答問題。 |
| 第 6 堂課 | 順序代理程式（SequentialAgent） | 用於處理需依特定順序執行多個步驟的工作。能自動將上一個代理程式的輸出，作為下一個代理程式的輸入。 |
| 第 7 堂課 | 迴圈代理程式（LoopAgent） | 用於解決沒有單一直接解法的問題。此代理程式會重複執行一系列子代理程式（Sub-agents），直到符合特定限制條件。 |
| 第 8 堂課 | 平行代理程式（ParallelAgent） | 當使用者要求多個不相關資訊時，此代理程式會並行執行子代理程式清單，加速工作。所有工作完成後，再收集結果並綜合分析，產生單一的完整回覆。 |
