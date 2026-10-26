# OpenAPPA

- Git Repo
  - https://github.com/archestra-ai/openappa
- Website
  - https://www.openappa.com/

> [!NOTE]
> Deterministic guardrails that don't break agents

## 2026-10-27

---
title: "Archestra 发布 OpenAPPA，用于防范提示词注入或模型幻觉引发的数据外泄"
source: "https://www.infoq.cn/article/LQCqiPUzgZyB3v24rsNO"
author:
  - "[[琚克儉 | 火山引擎 AI 資料湖服務 架構師]]"
  - "[[吳翔宇 | 快手 演演演演演算法專家]]"
  - "[[王毅 | 紛享銷客 技術總監]]"
published:
created: 2026-10-26
description: "Archestra 发布开源安全引擎 OpenAPPA，用于防范提示词注入或模型幻觉引发的数据外泄。"
---

Archestra 釋出 [OpenAPPA](https://www.openappa.com/) ，這是一款開源的安全引擎，旨在阻止由提示詞注入或模型幻覺引發的資料外洩。OpenAPPA 在智慧體的提示詞與執行迴圈之外執行。其配置定義了資料來源、 [訪問物件](https://www.openappa.com/contracts#audiences) 、 [信任等級](https://www.openappa.com/contracts#trust) 、 [許可權主體](https://www.openappa.com/contracts#authorities) 等概念，以及與之相關的確定性安全強制執行規則。團隊在安全基準測試 [Bench-Corp](https://github.com/archestra-ai/OpenAPPA/tree/main/bench/corp) （20 項多步驟企業工作流）和 [AgentThreatBench](https://github.com/UKGovernmentBEIS/inspect_evals/tree/main/src/inspect_evals/agent_threat_bench) 中測得攻擊成功率為 0， [https://code.claude.com/docs/en/auto-mode-config](https://code.claude.com/docs/en/auto-mode-config) 的攻擊成功率為 10%， [微軟 FIDES](https://learn.microsoft.com/en-us/agent-framework/agents/security) 為 31%。

OpenAPPA 的檔案解釋了為什麼隨機方法在自動化策略強制執行中會失敗：

> 業界應對審批疲勞的辦法是用第二個模型來判斷每次工具呼叫：Claude Code 的自動模式、Codex 的自動稽核，以及其他 [自動模式](https://www.openappa.com/openappa-vs-auto-mode) 。
> 
> 從設計上看，它們無法跨工具呼叫追蹤資料流。由於分類器本身可能遭受提示詞注入，Harness 會對分類器隱藏工具輸出，因此判斷模型根本看不到資料。
> 
> 由於這種機率化的設計，即使是最優秀的模型也止步於 [99.3%](https://openai.github.io/openai-guardrails-python/ref/checks/prompt_injection_detection/) ：在數百萬次呼叫場景中，0.7% 的機率就意味著大量的資料洩露事件。
> 
> 規則集最終要麼限制過嚴導致智慧體無法正常工作，要麼邏輯過於複雜，沒人能審計它到底允許哪些操作。

一方面，智慧體很擅長繞開簡單但常用的防護手段，例如工具白名單/黑名單：被禁止的 `rm -rf` 命令可能會被等效的 Python 指令碼替代。另一方面，為防範激進的智慧體而不斷擴充黑名單、採用過度嚴苛的策略會降低可用性（例如，智慧體雖然沒有洩露資料，但受限制而無法成功完成任務）。OpenAPPA 的 GitHub 倉庫提醒開發者：

> 智慧體安全存在兩個維度：允許非授權資料流的智慧體是不安全的，而拒絕合法任務的智慧體則毫無用處。

Archestra 希望透過其提出的智慧體許可權策略代數（Agentic Permissions Policy Algebra，APPA）來解決嚴格強制執行與運營實用性之間的矛盾，相關內容在論文中進行了闡述，論文作者為 [Arseny Kravchenko](https://arxiv.org/search/cs?searchtype=author&query=Kravchenko,+A) 、 [Vadim Liventsev](https://arxiv.org/search/cs?searchtype=author&query=Liventsev,+V) 、 [Innokentii Konstantinov](https://arxiv.org/search/cs?searchtype=author&query=Konstantinov,+I) 、 [Ildar Iskhakov](https://arxiv.org/search/cs?searchtype=author&query=Iskhakov,+I) 和 [Matvey Kukuy](https://arxiv.org/search/cs?searchtype=author&query=Kukuy,+M) ，論文地址：\[[https://arxiv.org/abs/2607.24625](https://arxiv.org/abs/2607.24625)\]([https://arxiv.org/abs/2607.24625)。](https://arxiv.org/abs/2607.24625\)%E3%80%82)

OpenAPPA 透過一個可插拔引擎實現了這個方案，引擎在智慧體迴圈之外執行，阻止底層大語言模型檢視、協商或繞過策略規則。安全策略採用單個 配置檔案的形式，詳細定義了資料來源、 [訪問物件](https://www.openappa.com/contracts#audiences) 、 [信任等級](https://www.openappa.com/contracts#trust) 、 [許可權主體](https://www.openappa.com/contracts#authorities) 。

OpenAPPA 會同時標記並監控訪問物件（被授權的資料消費方集合）與信任等級（資料可信核驗程度）。標籤基於格代數實現單調組合：標籤只會變得更加嚴格；讀取受限記錄會縮小可訪問物件範圍；讀取未經核驗的外部網頁會降低信任等級。

每個工具契約定義了三個主要執行屬性： `requires` （執行該工具所需的訪問物件身份與信任等級）、 `delta` （工具返回資料時施加的限制變更）、 `effects` （成功操作的審計日誌）。

下面這個例子透過 `get_ticket_from_crm` 讀取工單，會將這條執行鏈路的訪問物件限制為 `internal` （內部）。後續呼叫 `process_internal_data` ，就要求訪問物件必須屬於 `internal` 。

```
[[policy.tool]]name = "get_ticket_from_crm"delta = { audience = ["internal"] }
[[policy.tool]]name = "publish_update"requires = { audience = { contains = ["public"] } }
[[policy.tool]]name = "process_internal_data"requires = { audience = { within = ["internal"] } }
```

複製程式碼

下面這個例子， `read_web_page` 工具返回的結果會被標記為 `suspicious` （可疑）。OpenAPPA 在收到 `read_web_page` 的返回結果後會阻止執行 `apply_db_migration` ，因為該操作要求資料必須為 `trusted` （可信）。

```
[policy]version = 2trust_chain = ["suspicious", "trusted"]
[[policy.tool]]name = "read_web_page"delta = { trust = "suspicious" }
[[policy.tool]]name = "apply_db_migration"requires = { trust = "trusted" }
```

複製程式碼

OpenAPPA 還有顯式的恢復語義。當智慧體嘗試非法操作時，引擎會停止排程並提供結構化的處理路徑。\*淨化器（Sanitizers）\*可以修改有效載荷，例如剝離個人身份資訊，安全地擴大可訪問物件範圍。\*許可權主體（Authorities）\*將請求路由給人工操作員或內部驗證 API，實現單次操作審批。\*一次性子分支（Disposable Child Branches）\*支援按需隔離：當智慧體必須攝取不受信任的資料時，引擎會在一個臨時的子智慧體分支中隔離讀取操作，僅向父級返回經過模式認證的淨化後的輸出。

[Bench-Corp 和 OWASP AgentThreatBench](https://www.openappa.com/evaluation) 基準測試表明，OpenAPPA 在嚴格的安全約束下保持了高實用性，攻擊成功率為 0%，任務完成率為 89%。Claude Code 的原生自動模式攻擊成功率 10%，任務完成率 90%。微軟 FIDES 的攻擊成功率 31%，任務完成率僅 41%。研究團隊報告稱，消融實驗驗證了恢復策略的價值：當完全禁用補救方案後，任務完成率下降至 35.0%。

Bench-Corp 和 AgentThreatBench 用於測試 [顯式策略違規](https://www.openappa.com/how-it-works#the-core-concepts) ：敏感資料共享、提示詞注入、審批與執行順序、租戶隔離。Bench-Corp 是一個高度專用化的企業助手測試基準，用於評估安全策略在複雜多步驟企業工作流中的表現。 [AgentThreatBench](https://dev.to/vaishnavi_gudur/agentthreatbench-the-first-owasp-agentic-top-10-security-benchmark-6pp) 將 [OWASP 2026 智慧體應用十大安全風險](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) 轉化為可執行的測試任務。該基準最近已合併進入 [英國人工智慧安全研究所官方 倉庫](https://github.com/UKGovernmentBEIS/inspect_evals/pull/1037) 。AgentThreatBench 採用雙指標評分體系，同時評估可用性與安全性。OpenAPPA 在該基準上取得滿分安全成績，攻擊全部失敗。

OpenAPPA 目前處於預覽階段。形式化代數和恢復保證已釋出在 [arXiv（APPA：面向真實世界 LLM 智慧體的可恢復資訊流控制）](https://arxiv.org/abs/2607.24625) 上。讀者可以閱讀該論文和官方檔案，兩者都包含大量額外的技術細節、隨附插圖和實驗結果。

檢視英文原文： [https://www.infoq.com/news/2026/10/open-APPA-zero-security-breach/](https://www.infoq.com/news/2026/10/open-APPA-zero-security-breach/)
