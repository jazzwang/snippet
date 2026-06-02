# Github Copilot

- Study Guide
  - https://assets.ctfassets.net/wfutmusr1t3h/3i7ISEUsTLBgOGrWrML07y/dd586e2b2b607988e2679ed8cce36a76/github-copilot-exam-preparation-study-guide.pdf

## 2026-06-02

- 緣起：同事們提到使用 Github Copilot 然後讓它分別扮演不同的角色協作，好奇 Copilot 是否支援 subagent 的設計。

<table><tr style="background-color:lightyellow;"><td>Q:</td><td>
github copilot 有 sub-agent 的概念嗎？可以讓 Github Copilot 分別扮演不同的角色進行團隊合作嗎？例如 Product Manager, Scrum Master, UX Designer, Frontend Developer, Backend Developer, Database Developer
</td></tr><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI Mode
</td></tr><tr><td>A:</td><td>

是的，[GitHub Copilot](https://github.com/orgs/community/discussions/192232) 完全具備 Sub-agent（子代理）與 Multi-agent（多代理）的架構與概念。 [1, 2] 
GitHub 官方推出了 Custom Agents（自訂代理人） 功能，並在 IDE（如 VS Code）中內建了 Sub-agent 編排器（Orchestration）。這意味著你完全可以讓 GitHub Copilot 分別扮演 Product Manager、Scrum Master、UX Designer、Frontend/Backend Developer 及 Database Developer 等角色，並在同一個專案或對話中進行分工與團隊合作。 [2, 3, 4, 5, 6] 
以下為您說明其實現原理，以及如何具體配置出一個虛擬的「軟體開發團隊」。

## 一、 GitHub Copilot 的 Sub-agent 運作機制

GitHub Copilot 的多代理架構主要透過以下幾種方式運作：

   1. 獨立的上下文視窗（Isolated Context Windows）：
   主代理人（Orchestrator）在收到複雜任務時，會調用多個特定的 Sub-agents。每個子代理都在獨立的沙盒環境中運行，它們擁有自己專屬的提示詞（System Prompt）、工具集與上下文，處理完畢後再將結果回傳給主代理，避免單一對話視窗被海量資訊塞滿（Token 爆炸）。 [2, 7, 8, 9] 
   2. 客製化團隊角色（Custom Personas）：
   透過在專案中建立 .agent.md 或 .github/agents/ 設定檔，你可以將團隊中的特定職位（如 UX、Backend）參數化。 [3, 10] 
   3. 模型上下文協定（MCP, Model Context Protocol）：
   每個 Sub-agent 除了看程式碼之外，還可以綁定外部工具。例如：Database Developer 代理可以連接到真實資料庫讀取 Schema；Scrum Master 可以透過 MCP 串接 Jira 或 GitHub Issues 來管理看板。 [11, 12] 


## 二、 如何動態建立與調用你的「虛擬開發團隊」？

你可以利用 Custom Agent Profile (Markdown 配置法)，在專案根目錄的 .github/agents/（或自訂的 agents/ 目錄）中建立不同的角色檔案： [10, 13] 

### 1. 建立角色定義檔

你可以為每個職位各寫一個 .agent.md 檔案： [3] 

* pm.agent.md (Product Manager)

```md
---name: pm
description: 產品經理，負責分析 PRD 與撰寫 User Story。
tools: [github-issues-explorer]
---
你是一位資深的產品經理。請遵循 Agile 規範，負責將使用者的模糊需求轉化為明確的 Feature、User Story 與驗收標準（AC）。
```

* scrum-master.agent.md (Scrum Master)

```md
---name: scrum-master
description: 敏捷教練，負責拆解任務、估算點數。
---
你是一位 Scrum Master。請將 PM 寫好的 User Story 拆解成前端、後端、資料庫的 sub-tasks，並分配給對應的角色。
```

* ux-designer.agent.md (UX Designer)

```md
---name: ux-designer
description: UI/UX 專家，專精元件設計與排版邏輯。
---
你負責設計系統的資訊架構。請根據 PM 的需求提供 JSON 格式的 UI 組件狀態樹、欄位驗證邏輯與無障礙網頁（A11y）指南。
```

* frontend.agent.md / backend.agent.md / db-dev.agent.md

```md
---name: db-dev
description: 資料庫工程師，精通 SQL 與資料庫正規化。
---
你負責設計實體關係圖（ERD）與產出 PostgreSQL 遷移腳本（Migration SQL）。請確保欄位有適當的索引與外鍵約束。
```

## 2. 調用與團隊合作（Workflow Handoff）

當這些 Agent 配置完成後，你可以在 VS Code 的 Copilot Chat 視窗或 GitHub PR 介面中，透過 @ 語法 或 Agent picker 直接指派任務與進行接力： [4, 14] 

* 流程 1（PM 起頭）：

「@pm 我想在電商網站上加入一個『買一送一限時搶購』的功能，請幫我寫出完整的 User Story 與 AC。」

* 流程 2（SM 拆單）：

「@scrum-master 請根據剛剛 @pm 產出的 User Story，將任務拆解為前端、後端與資料庫的開發票，並估算 Story Points。」

* 流程 3（專家協作）：

「@db-dev 針對 @scrum-master 的資料庫任務，請產生本次功能所需的 Schema 變更腳本。」
「@backend 請依據 @db-dev 的 Schema 撰寫 API；@frontend 請協同 @ux-designer 的設計完成前端畫面。」


在最新的 Agent Sessions 介面中，主代理人甚至能根據你的總體指令（例如：「請幫我實作這個新功能並上線」），自動並行（Parallelization） 調用底下的各個 Sub-agents 共同作業。你可以在畫面上點開 View Session，看到 PM 正在規劃、Backend 正在寫程式、DBA 正在審查 SQL 的多線程執行進度！ [3, 7, 15, 16] 

想立即動手試試看嗎？我可以幫你撰寫特定角色（例如 Product Manager 或 Backend Developer）的完整配置檔案內容，或者教你如何將這些 Custom Agents 與你們團隊內部的資料庫/ API 文件（透過 MCP）進行綁定。請告訴我你想先建立哪一個角色！

[1] [https://iambigd.tw](https://iambigd.tw/agent-subagent-multi-agent-copilot-use-story)
[2] [https://www.facebook.com](https://www.facebook.com/will.fans/posts/%E5%93%87%E5%93%87%E5%93%87-vs-code-insiders-%E7%9A%84-github-copilot-%E5%B7%B2%E7%B6%93%E5%85%A7%E5%BB%BA%E4%BA%86-subagent-%E5%B7%A5%E5%85%B7%E4%BA%86%E8%80%B6%E7%86%B1%E9%A8%B0%E9%A8%B0%E7%9A%84%E6%98%A8%E5%A4%A9%E6%89%8D%E5%89%9B%E6%8E%A8%E5%87%BAgithub-copilo/1264365775717509/)
[3] [https://github.com](https://github.com/orgs/community/discussions/192232)
[4] [https://code.visualstudio.com](https://code.visualstudio.com/docs/copilot/customization/custom-agents)
[5] [https://docs.github.com](https://docs.github.com/en/enterprise-cloud@latest/copilot/concepts/agents/cloud-agent/about-custom-agents)
[6] [https://docs.github.com](https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/copilot-sdk/use-copilot-sdk/custom-agents)
[7] [https://visualstudiomagazine.com](https://visualstudiomagazine.com/articles/2026/02/09/hands-on-with-new-multi-agent-orchestration-in-vs-code.aspx)
[8] [https://docs.github.com](https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/copilot-sdk/features/custom-agents)
[9] [https://medium.com](https://medium.com/ricos-note/github-copilot-agent-skills-%E8%AE%93-ai-%E7%9C%9F%E6%AD%A3%E6%9B%BF%E4%BD%A0%E5%81%9A%E4%BA%8B-dedcc90e1dbf)
[10] [https://github.blog](https://github.blog/changelog/2025-10-28-custom-agents-for-github-copilot/)
[11] [https://learn.microsoft.com](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-specialized-agents?view=visualstudio)
[12] [https://github.com](https://github.com/features/copilot/agents)
[13] [https://docs.github.com](https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/create-custom-agents)
[14] [https://learn.microsoft.com](https://learn.microsoft.com/zh-tw/visualstudio/ide/copilot-specialized-agents?view=visualstudio)
[15] [https://code.visualstudio.com](https://code.visualstudio.com/blogs/2026/02/05/multi-agent-development)
[16] [https://ucomedu.blogspot.com](https://ucomedu.blogspot.com/2025/11/github-copilot-2.html)

</td></tr>
</table>
