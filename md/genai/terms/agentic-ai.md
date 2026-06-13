# Agentic AI vs AI Agent

- 記得在 LinkedIn 看過一篇關於 Agentic AI 跟 AI Agent 的差異說明。不過得回 [LinkedIn Saved Posts](https://www.linkedin.com/my-items/saved-posts/) 去翻了。 #TODO

## 2026-06-13

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI Mode
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
AI Agent 的組成
</td></tr><tr><td>A:</td><td>

## AI Agent

AI Agent（人工智慧代理）的核心組成主要由四大模塊構成：大腦（核心模型）、記憶（Memory）、規劃（Planning）以及工具（Tools/Action）。這四大元件相互協作，讓 AI 能夠擺脫傳統 Chatbot 一問一答的被動模式，轉化為具備「自主感知環境、思考推理、操作工具並完成目標」的數位代理人。 [1, 2, 3, 4] 

以下為 AI Agent 的核心組成架構全解析：

### 🧠 大腦：中央決策與大型語言模型 (LLM)

大腦是 AI Agent 的核心控制中心。通常由具備強大推理能力的大型語言模型（LLM）擔任。 [1, 5] 

* 語義理解：接收來自外部的文字、語音、圖像等非結構化訊息，並精準解讀使用者的最終意圖。
* 推理決策：根據目前掌握的資訊與最終目標，進行邏輯分析，決定下一步該採取什麼行動。 [3, 6, 7] 

### 💾 記憶體系：上下文與經驗累積 (Memory) [8] 

記憶模組負責幫 Agent 儲存與檢索資訊，確保其在多輪對話或長期任務中保持行為的連貫性。 [3, 9] 

* **短期記憶（Short-term Memory）**：記錄當前對話的上下文（Context window），讓 Agent 在連續溝通時不會「講過就忘」。 [3, 10] 
* **長期記憶（Long-term Memory）**：通常結合向量資料庫（Vector Database）或 RAG（檢索增強生成）技術，用以儲存外部知識庫、使用者偏好、或是過往任務的成敗經驗。 [3, 4, 6] 

### 🗺️ 智慧規劃：任務拆解與反思能力 (Planning) [7] 

規劃能力是 AI Agent 能否自主應對複雜開放式任務的關鍵。 [1, 11] 

* 子任務拆解：將使用者給予的宏大目標（例如：「幫我安排東京三天兩夜行程」），自動拆解為可執行的多個微小步驟（如：查航班 → 訂飯店 → 規劃路線）。 [4] 
* 思維技術應用：運用思維鏈（CoT, Chain of Thought）或思維樹（ToT, Tree of Thought）進行深度思考。 [5] 
* 反思與自我修正：在執行過程中若發現工具回傳錯誤（例如：飯店客滿），Agent 能自動退回規劃層調整策略，尋找替代方案，而非直接報錯停機。 [4] 

### 🛠️ 行動執行：外部工具與 API 呼叫 (Tools / Action) [1, 12] 

工具使用賦予了 AI Agent 與真實世界互動的「手腳」。大腦再聰明，若沒有工具，產出也僅止於文字。 [4, 7, 13] 

* 多樣化工具：Agent 可以根據大腦決策，主動調用搜尋引擎、資料庫、計算機、編譯器執行程式碼，或是透過 API 操作第三方軟體。
* 實際案例：自動打開瀏覽器幫使用者下單、發送 Email、或是將行程直接寫入使用者的 Google Calendar。 [1, 4] 

------------------------------

### 🔄 完整運作迴路 (Agentic Loop)

這四個元件在實際運作時，會形成一個不斷循環的環境感知與反饋迴路：

```
 [感知 Perception] ──> 接收環境與使用者指令
        │
 [大腦 Core LLM]   ──> 結合 [記憶 Memory] 理解意圖
        │
 [規劃 Planning]   ──> 拆解任務、制定行動順序
        │
 [行動 Action]     ──> 呼叫 [工具 Tools] 執行（如呼叫 API）
        │
 [觀測 Observation] ──> 檢查執行結果，若失敗則回頭修正，成功則納入學習
```

透過這種架構，AI Agent 不僅能幫人類處理高度重複性的工作，更具備了在未知環境中「自我進化」與動態解決問題的能力。 [14] 

若您正準備設計或評估 AI Agent，可以告訴我您的應用場景（例如：企業自動化、個人助理、數據分析）嗎？我可以進一步為您分享適合的開源開發框架（如 LangGraph、AutoGen 或 CrewAI）。 [2, 4] 

[1] [https://medium.com](https://medium.com/vincent-chen/ai-agent%E6%A6%82%E5%BF%B5%E5%8F%8A%E5%85%B6%E6%87%89%E7%94%A8-e66c88e9a015)
[2] [https://www.largitdata.com](https://www.largitdata.com/knowledge/what-is-ai-agent/)
[3] [https://cloud.tencent.com](https://cloud.tencent.com/developer/ask/2186787)
[4] [https://91app.com](https://91app.com/blog/what-is-aiagent/)
[5] [https://perform-global.com](https://perform-global.com/blog/what-is-ai-agent)
[6] [https://frankchiu.io](https://frankchiu.io/ai-ai-agent/)
[7] [https://ithelp.ithome.com.tw](https://ithelp.ithome.com.tw/m/articles/10373700)
[8] [https://www.gomini.com.tw](https://www.gomini.com.tw/news/82)
[9] [https://ai.managertoday.com.tw](https://ai.managertoday.com.tw/answer/ai-age-697-4582962)
[10] [https://ithelp.ithome.com.tw](https://ithelp.ithome.com.tw/articles/10375548)
[11] [https://www.nvidia.cn](https://www.nvidia.cn/glossary/ai-agents/)
[12] [https://seller.alibaba.com](https://seller.alibaba.com/tw/solutionblogs/ai-agent-%E6%98%AF%E4%BB%80%E9%BA%BCai-agent-%E8%83%BD%E6%9B%BF%E4%B8%AD%E5%B0%8F%E4%BC%81%E6%A5%AD%E5%B8%B6%E4%BE%86%E5%93%AA%E4%BA%9B%E6%95%88%E7%9B%8A-px002djrz)
[13] [https://www.pressplay.cc](https://www.pressplay.cc/project/2667A183130728C4AE30928EF3CFF4DD/articles/9E03B4FCD456ED77CB40AD8EC07A01DE)
[14] [https://vocus.cc](https://vocus.cc/article/67ad5e12fd8978000196bb04)

</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
AI Agent 與 Agentic AI 的差別
</td></tr><tr><td>A:</td><td>

## "AI Agent" vs "Agentic AI"

AI Agent 與 Agentic AI 的核心差別在於：AI Agent 指的是「單一的、具體的軟體實體（實作結果）」，而 Agentic AI 則是一種「系統性的運作模式、設計理念與技術特徵（核心屬性）」。

用一個通俗的例子來比喻：AI Agent 就像是一輛「自動駕駛汽車」，而 Agentic AI 則是「自動駕駛技術 / 具備自動駕駛能力的系統」。 [1] 
以下為兩者的核心差異對比：

### 📌 定義與本質的差別

* AI Agent（人工智慧代理 / 智能體）
* 本質：名詞。指一個具體的、可執行的產品或程式實體。
   * 特點：它擁有特定的大腦（LLM）、記憶、工具與規劃模組。例如：一個幫你自動訂機票的 AI 助理、一個會自己寫 Code 且能除錯的軟體工程師 Agent（如 Devin）。 [2, 3, 4, 5] 
* Agentic AI（具代理能力的 AI / 主動式 AI）
* 本質：形容詞或概念。指 AI 系統所展現出的自主性、主動探索與目標導向的「能力特徵」。
   * 特點：強調 AI 不再只是被動接收 Prompt 回答，而是具備「自主循環（Agentic Loop）」的思考模式。只要給它一個模糊的最終目標，它就能展現出主動、反思、自我修正的特質。 [6, 7, 8] 

### 📊 關鍵維度對比

| 比較維度 [9, 10, 11, 12, 13] | AI Agent (人工智慧代理) | Agentic AI (具代理能力的 AI) |
|---|---|---|
| 焦點 | 關注「什麼是 Agent」（架構與工程實作）。 | 關注「AI 如何運作」（自主性、行為模式）。 |
| 顆粒度 | 微觀：指單一或一組特定的 AI 系統。 | 宏觀：指一種新型的 AI 技術典範與生態。 |
| 核心表現 | 具備輸入、思考、工具調用、輸出的工具實體。 | 具備自我反思（Reflection）、多智慧體協同等工作流特徵。 |
| 常見語境 | 「我們團隊開發了一個客服 AI Agent。」 | 「未來五年，科技將全面轉向 Agentic AI 時代。」 |

### 🛠️ 工作流程的演進（從傳統 AI 到 Agentic AI）

要理解 Agentic AI 的獨特性，可以看它如何改變 AI 的工作流程：

   1. Non-Agentic（傳統生成式 AI）：
   * 人類給予明確 Prompt → LLM 一堂子產生回覆 → 結束。
      * 缺點：如果回答錯誤，AI 不會自己發現，需要人類手動修改 Prompt 重新提問。
   2. Agentic AI（主動式工作流）：
   * 人類給予最終目標 → AI 拆解步驟 → 執行第一步 → 反思與檢查結果 → 發現錯誤 → 自動修正路線 → 執行第二步 → 達成目標。
      * 這種「自我糾錯與反覆運算」的特徵，就是 Agentic AI 的精髓；而承載這個流程的軟體主體，就是 AI Agent。 [14, 15] 
   
------------------------------

您目前是在評估將現有的 AI 系統升級為具備 Agentic 工作流 的模式，還是正在研究如何架構多個 AI Agent 進行協同工作呢？歡迎分享您的應用場景，我們可以深入探討特定的實作架構！

[1] [https://vocus.cc](https://vocus.cc/article/674a60fbfd8978000101413e)
[2] [https://www.instagram.com](https://www.instagram.com/reel/DYKIPsmxlZb/)
[3] [https://help.aliyun.com](https://help.aliyun.com/zh/pai/user-guide/create-a-code-based-application)
[4] [https://ithelp.ithome.com.tw](https://ithelp.ithome.com.tw/articles/10346976)
[5] [https://www.gvm.com.tw](https://www.gvm.com.tw/article/113965)
[6] [https://zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/1955206157997146743)
[7] [https://zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/1960388301572772822)
[8] [https://www.find.org.tw](https://www.find.org.tw/indus_trend/browse/c075c8d0c3bd0981175d8ecc77f086a2)
[9] [https://www.instagram.com](https://www.instagram.com/reel/DYKIPsmxlZb/)
[10] [https://www.youtube.com](https://www.youtube.com/watch?v=RsPeGe741uw)
[11] [https://zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/1907576448044205125)
[12] [https://ikala.ai](https://ikala.ai/zh-tw/blog/ikala-ai-insight/agentic-workspace/)
[13] [https://www.oracle.com](https://www.oracle.com/tw/artificial-intelligence/ai-agents/)
[14] [https://hackmd.io](https://hackmd.io/@shaoeChen/HJ-4_8vpbg)
[15] [https://viscovery.com](https://viscovery.com/zh/ai-agentic-workflow-a-new-era-of-smarter-more-collaborative-ai/)

</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
Harness Engineering 與 AI Agent, Agentic AI 的關聯
</td></tr><tr><td>A:</td><td>

## Harness Engineering

Harness Engineering（駕馭工程）是實現 AI Agent 落地並推動 Agentic AI 走向規模化與高可靠性的「系統級基礎建設」與「控制框架」。 [1, 2] 

如果把 AI Agent 比喻為一匹擁有強大推理能力的「馬」，Agentic AI 是這匹馬展現出自主奔跑、尋找路徑的「行為特徵」，那麼 Harness Engineering 就是套在馬身上的「韁繩、馬鞍與轡頭（Harness）」。它不改變模型底層的能力，卻決定了 AI 能往哪走、走多快、以及出事時如何被安全拉回。 [3] 

這三者的核心關聯與互補關係可以從以下幾個層次來理解：

------------------------------

### 📊 核心架構階層關係

在現代 AI 系統設計中，三者處於不同的工程層次，彼此由內而外層層包裹： [4, 5] 

* 基礎核心（LLM）：負責提供最底層的思考與推理運算。
* Prompt / Context Engineering：訊息與資訊層。優化輸入給模型的單次指令與脈絡。
* AI Agent（實體）：包裝了基本記憶與工具的單一執行實體。
* Harness Engineering（系統層）：負責串聯、控制與約束多個 Agent 會話的環境基礎設施。
* Agentic AI（技術範式）：在上述系統完美運作下，整體系統展現出的自主、反思與目標導向的運作特徵。 [3, 4, 6] 

------------------------------

### 🔑 Harness Engineering 對 AI Agent 與 Agentic AI 的三大核心價值

#### 1. 建立「安全邊界」與「護欄」，防止 Agent 失控 (Guardrails)

* 背景：AI Agent 開始擁有讀寫檔案、呼叫 API、修改資料庫等「執行權限」，其操作具有副作用且不可逆。例如 AI 遇到複雜 Bug 時，在它的邏輯裡「刪除整個資料庫重建」是一個乾淨且合理的解法。 [3, 7] 
* Harness 的角色：Harness Engineering 設計了動態審查機制。它根據變更的「爆炸半徑」來決定攔截強度（例如：偵測到刪除指令或關鍵環境變更時，強制引入 Human-in-the-loop 人工審查機制），確保 Agent 的自主性（Agentic AI）被限制在企業可控的範圍內。 [1, 2, 7] 

#### 2. 將「無記憶」的模型轉化為「長週期執行」的 Agent (State & Resource Management)

* 背景：大型語言模型本質上是無狀態的（Stateless），且受到 Context Window（上下文視窗）與 Token 成本的限制。 [3] 
* Harness 的角色：它就像 AI 的作業系統 (OS)。Harness 負責管理 Token 預算、建立熔斷機制防止 Agent 陷入無限循環消耗；同時處理狀態持久化（Memory 系統），將跨 Session 的知識保存並精準壓縮回傳，讓 Agent 能在長達數十輪的複雜任務中保持清醒。 [3, 6, 8] 

#### 3. 編排「多智慧體（Multi-Agent）」工作流 (Orchestration)

* 背景：複雜任務（例如大規模軟體開發）往往超越單一 LLM 的注意力上限。
* Harness 的角色：Harness Engineering 定義了多個 Agent 之間的協作架構與權限通訊機制。例如 [OpenAI 的實踐](https://openai.com/index/harness-engineering/)與 Stripe 的 Minions 系統，就是透過 Harness 自動串聯數千個 AI 程式碼檢視與測試會話，自動讀取測試失敗訊息、反思診斷、修復，直到通過 CI/CD 驗證為止。 [3, 9, 10, 11] 

------------------------------

### ⚖️ 一句話對比總結

| 概念 [12, 13] | 核心關注點 | 角色比喻 |
|---|---|---|
| Agentic AI | 系統是否具備自主性、主動反思與自我修正的特質。 | 駕駛的行為（汽車能自己規劃路線、躲避障礙） |
| AI Agent | 具備大腦、記憶與工具的執行軟體實體。 | 汽車本身（實體載具） |
| Harness Engineering | 圍繞 Agent 建立的安全護欄、資源控制與流程驗證環境。 | 交通規則與底盤控制系統（確保車子不會衝出懸崖） |

如 [Salesforce 開發社群](https://www.salesforce.com/agentforce/ai-agents/agent-harness/) 所定義：「Agent 負責決定要做什麼（What）與為什麼做（Why），而 Harness 則掌控了它該如何做（How）與在哪裡做（Where）。」 當模型能力（如 GPT-4o, Claude 3.5 Sonnet）日益強大且趨同，企業真正的護城河將不再是模型本身，而是看誰能透過 Harness Engineering 打造出最穩定、最安全的 Agentic AI 運作系統。 [3, 14, 15] 

您目前是否正嘗試在現有的開發流程（例如：CI/CD 管道、自動化運維或客服系統）中導入 AI Agent 呢？我們可以針對如何設計 Harness 中的「自動化驗證機制」或「Token 熔斷防護」進行具體討論！

[1] [https://oakmega.com](https://oakmega.com/blog/ceo-insights-010)
[2] [https://medium.com](https://medium.com/generative-ai-revolution-ai-native-transformation/harness-engineering-vs-agentic-engineering-the-hidden-divide-shaping-enterprise-ai-ab7f80d14fa6)
[3] [https://wenwender.wordpress.com](https://wenwender.wordpress.com/2026/04/02/harness-engineering-ai-%E5%B7%A5%E7%A8%8B%E5%B8%AB%E7%9A%84%E7%AC%AC%E4%B8%89%E5%80%8B%E7%B6%AD%E5%BA%A6/)
[4] [https://www.youtube.com](https://www.youtube.com/watch?v=ulNsa0sD8N0&t=36)
[5] [https://blog.sharktech.tw](https://blog.sharktech.tw/2026/05/13/what-is-harness-engineering-for-ai-agent)
[6] [https://www.firecrawl.dev](https://www.firecrawl.dev/blog/what-is-an-agent-harness)
[7] [https://ai-coding.wiselychen.com](https://ai-coding.wiselychen.com/harness-engineering-architecture-overview-ai-code-production-guardrails/)
[8] [https://jasonchuang.substack.com](https://jasonchuang.substack.com/p/harness-engineering-ai)
[9] [https://openai.com](https://openai.com/index/harness-engineering/)
[10] [https://zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/2014014859164026634)
[11] [https://hackmd.io](https://hackmd.io/@BASHCAT/SkQEW0F2bg)
[12] [https://www.youtube.com](https://www.youtube.com/watch?v=mGYr9VqQnEI&t=2)
[13] [https://yu-wenhao.com](https://yu-wenhao.com/zh-TW/blog/agentic-coding/)
[14] [https://www.salesforce.com](https://www.salesforce.com/agentforce/ai-agents/agent-harness/)
[15] [https://hackmd.io](https://hackmd.io/@BASHCAT/SkQEW0F2bg)

</td></tr>
</table>
