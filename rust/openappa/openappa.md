# OpenAPPA

- Git Repo
  - https://github.com/archestra-ai/openappa
- Website
  - https://www.openappa.com/

> [!NOTE]
> Deterministic guardrails that don't break agents

## 2026-10-27

---
title: "Archestra 推出 OpenAPPA，防范提示詞注入與模型幻覺導致的資料外洩"
source: "https://www.infoq.cn/article/LQCqiPUzgZyB3v24rsNO"
author:
  - "[[琚克儉 | 火山引擎 AI 資料湖服務 架構師]]"
  - "[[吳翔宇 | 快手 演演演演演算法專家]]"
  - "[[王毅 | 紛享銷客 技術總監]]"
published:
created: 2026-10-26
description: "Archestra 推出開源安全引擎 OpenAPPA，有效防護提示詞注入與模型幻覺所引發的資料外洩。"
tags:
  - "clippings"
---
Archestra 推出 [OpenAPPA](https://www.openappa.com/)，一款開源安全引擎，用於抵禦提示詞注入與模型幻覺造成的資料外洩風險。OpenAPPA 在智慧體的提示詞與執行循環之外運作，透過配置定義資料來源、[訪問物件](https://www.openappa.com/contracts#audiences)、[信任等級](https://www.openappa.com/contracts#trust)、[權限主體](https://www.openappa.com/contracts#authorities) 等核心概念，以及相關的確定性安全強制執行規則。在安全基準測試 [Bench-Corp](https://github.com/archestra-ai/OpenAPPA/tree/main/bench/corp)（20 項多步驟企業工作流）和 [AgentThreatBench](https://github.com/UKGovernmentBEIS/inspect_evals/tree/main/src/inspect_evals/agent_threat_bench) 中，OpenAPPA 攻擊成功率為 0，而 [Claude Code 自動模式](https://code.claude.com/docs/en/auto-mode-config) 為 10%，[微軟 FIDES](https://learn.microsoft.com/en-us/agent-framework/agents/security) 則達 31%。

OpenAPPA 的技術文檔闡述了為何隨機式方法在自動化策略強制執行中難以奏效：

> 業界為緩解審批疲勞，常採用第二模型判斷每次工具調用：如 Claude Code 的自動模式、Codex 的自動稽核，以及其他 [自動模式](https://www.openappa.com/openappa-vs-auto-mode)。
>
> 從設計上看，這些方法無法跨工具調用追蹤資料流。此外，分類器本身可能遭受提示詞注入，因此 Harness 會向分類器隱藏工具輸出，導致判斷模型根本無法看到資料。
>
> 這種機率式設計即便配合最優秀的模型，準確率也止步於 99.3%：在百萬級調用場景中，0.7% 的失誤率意味著大量的資料洩漏風險。
>
> 規則集最終面臨兩難：限制過嚴導致智慧體無法正常運作，或邏輯過於複雜而無人能審計其允許的操作。

一方面，智慧體擅長繞過簡單常用的防護手段，例如工具白名單或黑名單：被禁止的 `rm -rf` 命令可能改用等效的 Python 代碼。另一方面，為防範激進智慧體而不斷擴充黑名單、採用過度嚴苛的策略，反而降低系統可用性（例如，智慧體未洩露資料，卻因限制過嚴而無法成功完成任務）。OpenAPPA 的 GitHub 倉庫指出：

> 智慧體安全存在兩個維度：允許非授權資料流的智慧體不安全，而拒絕合法任務的智慧體則失去實用價值。

Archestra 提出「智慧體權限策略代數」（Agentic Permissions Policy Algebra，APPA），旨在解決嚴格強制執行與營運實用性之間的矛盾，相關論文由 [Arseny Kravchenko](https://arxiv.org/search/cs?searchtype=author&query=Kravchenko,+A)、[Vadim Liventsev](https://arxiv.org/search/cs?searchtype=author&query=Liventsev,+V)、[Innokentii Konstantinov](https://arxiv.org/search/cs?searchtype=author&query=Konstantinov,+I)、[Ildar Iskhakov](https://arxiv.org/search/cs?searchtype=author&query=Iskhakov,+I) 和 [Matvey Kukuy](https://arxiv.org/search/cs?searchtype=author&query=Kukuy,+M) 撰寫，論文地址：[https://arxiv.org/abs/2607.24625](https://arxiv.org/abs/2607.24625)。

OpenAPPA 透過可插拔引擎實現此方案，在智慧體循環之外執行，阻止底層大語言模型檢視、協商或繞過策略規則。安全策略以單一配置檔案形式定義資料來源、[訪問物件](https://www.openappa.com/contracts#audiences)、[信任等級](https://www.openappa.com/contracts#trust)、[權限主體](https://www.openappa.com/contracts#authorities) 等設定。

OpenAPPA 同時標記並監控「訪問物件」（獲授權的資料消費方集合）與「信任等級」（資料可信核驗程度）。標籤基於格代數實現單調組合：標籤只會更嚴格；讀取受限記錄會縮小可訪問物件範圍；讀取未經驗證的外部網頁則降低信任等級。

每個工具契約定義三項主要執行屬性：`requires`（執行工具所需的訪問物件身份與信任等級）、`delta`（工具返回資料時施加的限制變更）、`effects`（成功操作的審計日誌）。

以下範例透過 `get_ticket_from_crm` 讀取工單，將該執行鏈路的訪問物件限制為 `internal`（內部）。後續呼叫 `process_internal_data` 時，要求訪問物件必須屬於 `internal`。

```
[[policy.tool]]name = "get_ticket_from_crm"delta = { audience = ["internal"] }
[[policy.tool]]name = "publish_update"requires = { audience = { contains = ["public"] } }
[[policy.tool]]name = "process_internal_data"requires = { audience = { within = ["internal"] } }
```

複製程式碼

另一範例中，`read_web_page` 工具返回的結果會被標記為 `suspicious`（可疑）。OpenAPPA 在收到此結果後，會阻止執行 `apply_db_migration`，因為該操作要求資料必須為 `trusted`（可信）。

```
[policy]version = 2trust_chain = ["suspicious", "trusted"]
[[policy.tool]]name = "read_web_page"delta = { trust = "suspicious" }
[[policy.tool]]name = "apply_db_migration"requires = { trust = "trusted" }
```

複製程式碼

OpenAPPA 提供明確的恢復語義：當智慧體嘗試非法操作時，引擎會暫停調度並提供結構化處理路徑。-*淨化器（Sanitizers）*：修改有效載荷，例如剝離個人身份資訊，安全擴大可訪問物件範圍。-*權限主體（Authorities）*：將請求路由至人工操作員或內部驗證 API，實現單次操作審批。-*一次性子分支（Disposable Child Branches）*：支援按需隔離。當智慧體需處理不受信任的資料時，引擎在臨時子分支中隔離讀取操作，僅向父層級返回經模式認證的淨化輸出。

[Bench-Corp 與 OWASP AgentThreatBench](https://www.openappa.com/evaluation) 基準測試顯示，OpenAPPA 在嚴格安全約束下仍保持高實用性：攻擊成功率為 0%，任務完成率達 89%。相比之下，Claude Code 原生自動模式攻擊成功率 10%、任務完成率 90%；微軟 FIDES 則為攻擊成功率 31%、任務完成率僅 41%。消融實驗驗證了恢復策略的價值：完全禁用補救方案後，任務完成率跌至 35.0%。

Bench-Corp 與 AgentThreatBench 用於測試 [顯式策略違規](https://www.openappa.com/how-it-works#the-core-concepts)，包括敏感資料共享、提示詞注入、審批與執行順序、租戶隔離等場景。Bench-Corp 專為企業助手設計，評估安全策略在複雜多步驟工作流中的表現。[AgentThreatBench](https://dev.to/vaishnavi_gudur/agentthreatbench-the-first-owasp-agentic-top-10-security-benchmark-6pp) 則將 [OWASP 2026 智慧體應用十大安全風險](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) 轉化為可執行測試。該基準已併入 [英國人工智慧安全研究所官方倉庫](https://github.com/UKGovernmentBEIS/inspect_evals/pull/1037)。AgentThreatBench 採用雙指標評分，同時衡量可用性與安全性。OpenAPPA 在該基準上獲得滿分安全成績，所有攻擊均失敗。

OpenAPPA 現已進入預覽階段。形式化代數與恢復保證已在 [arXiv 論文（APPA：面向真實世界 LLM 智慧體的可恢復資訊流控制）](https://arxiv.org/abs/2607.24625) 發表。讀者可閱讀論文與官方文檔，兩者均提供額外技術細節、圖示與實驗結果。

檢視英文原文：[https://www.infoq.com/news/2026/10/open-APPA-zero-security-breach/](https://www.infoq.com/news/2026/10/open-APPA-zero-security-breach/)
