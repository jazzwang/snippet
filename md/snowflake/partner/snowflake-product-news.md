# Snowflake Product News (from Partner Network)

## 2026-08-12

- 2026-07-28
  - Snowflake Launches Cortex AI Gateway and Advanced AI Security at Black Hat 2026
  - https://www.snowflake.com/en/blog/enterprise-ai-security-agentic-mcp-governance/

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Gemini Chat
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
請幫我撰寫中文摘要
</td></tr><tr><td>A:</td><td>

Snowflake 在 Black Hat 2026 大會上發布了 **Cortex AI Gateway** 及一系列生產級 AI 安全防護功能，旨在將安全與治理機制直接建構於資料與 AI 基礎設施核心，協助企業安全擴展自主 Agent 的應用。

**背景與市場痛點**

* **AI 安全疑慮遽增**：根據 Linux Foundation 報告，企業對 AI 安全的關注度從 2024 年的 17% 飆升至 2026 年的 48%，且 57% 的組織面臨安全與風險管理專業缺口。
* **傳統防護不足**：自主 Agent 結合了資料存取、系統執行與資料傳輸權限，大幅擴大了企業受攻擊面，傳統應用層修補工具已難以應付。

**核心發布：[Cortex AI Gateway**](https://www.snowflake.com/en/blog/enterprise-ai-security-agentic-mcp-governance/)
整合集中式 MCP Gateway（Natoma），在工具調用（tool-call）層級落實身分驗證與政策控管，三大特色包括：

* **集中控制 (Control)**：透過單一端點集中授權與稽核；私人預覽版支援多款主流模型（如 GPT、Gemini、Claude、Grok 等）在地化運行，並可統一控管 100+ MCP 伺服器連接。
* **即時可視 (Visibility)**：實時記錄 Agent 的調用工具、接觸系統及執行順序，提供端到端的完整稽核軌跡（私人預覽版）。
* **成本與效能優化 (Cost & Performance)**：依據成本、延遲與需求自動進行智慧模型路由，並能設定團隊與工作負載的預算上限Guardrails（私人預覽版）。

**生產級 AI 安全防護堆疊 (AI Security Stack)**

* **Agent 身分與工作階段安全**：
* **Agent Identity（GA）**：強化 Agent 活動可視性，並支援與 Okta、1Password、SailPoint 等第三方安全平台整合。
* **最小權限工作階段（Restricted Session Scope，即將 GA）**：嚴格將 Agent 權限限制在當前任務範疇（如強制將分析設定為唯讀）。


* **主動式安全姿態管理（GA）**：整合至 [Snowflake Trust Center](https://www.snowflake.com/en/blog/enterprise-ai-security-agentic-mcp-governance/)，提供儀表板主動掃描 AI 配置風險、評估合規性並進行自動化修復。
* **零信任資料外洩防護 (DXP)**：預防 Agent 攔截敏感資料或未授權的資料傳輸；提供用戶端 CLI VM 沙盒（macOS）確保開發環境隔離。
* **多方批准防勒索軟體 (MPA，GA)**：進行破壞性系統變更時需由兩人以上授權，消除單一高階憑證被挾持即遭勒索抹除資料的風險。
</td></tr>
</table>