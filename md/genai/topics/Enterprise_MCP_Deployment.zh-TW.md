---
title: "企業部署 MCP 的複雜因素"
source: "https://goteleport.com/blog/complicating-mcp-enterprise/"
author:
  - "[[Teleport]]"
published: 2026-03-20
created: 2026-10-07
description: "關於企業部署 MCP 的技術挑戰"
tags:
  - "clippings"
---

> [!NOTE]
> ### 關於作者：
> Boris Kurktchiev 是 Teleport 的現場 CTO，專注於雲端與 AI 的零信任身分驗證，並參與 CNCF 雲端原生 AI 工作組。

Doyensec 上週發布了一篇 [MCP 身分驗證/授權噩夢](https://blog.doyensec.com/2026/03/05/mcp-nightmare.html)，這篇對生產環境部署 MCP 有幫助。

完整披露：Teleport 贊助了這項研究。我們認為 MCP 可能成為企業 AI 的重要工具，因此支持相關安全研究。Francesco Lacerenza 和 Doyensec 團隊進行了迄今為止技術上最嚴謹的公共 MCP 身分驗證架構分析，並附有詳細的序列圖，繪製了 OAuth 2 流程中的每個注入點。

基於證書的身分驗證和 [mTLS](https://goteleport.com/learn/what-is-mtls/) 是企業 MCP 的前進之路。

我對此事有看法（我所在的公司開發相關產品）。我們贊助這項研究，因為研究結果與我在部署 MCP 時遇到的問題一致。

因此，我不重述他們的文章，而是想討論另一個問題：在企業中部署 MCP 時，實際會遇到什麼困難？不是理論性的攻擊分類，而是與 CISO 或企業架構師對話時的現實挑戰。

## MCP 的身分驗證功能仍在發展

MCP 於 2024 年 11 月推出時[沒有任何身分驗證機制](https://goteleport.com/blog/securing-model-context-protocol-with-teleport-and-aws/)，僅支援標準輸入，客戶端與伺服器間基於隱含信任。

最初的用例是本地工具，例如 Claude Desktop 與本地檔案系統對話。當時沒人將其部署到網路環境。

隨後 MCP 轉向遠端使用，在約 13 個月中規格經歷五個版本，每個版本都增加了資安功能。

2025 年 3 月的版本引入了 [OAuth 2.1](https://goteleport.com/learn/what-is-oauth-2/)，但讓 MCP 伺服器同時扮演資源伺服器和授權伺服器（如果您曾從事任何企業 IdP 工作，您就知道這是一個不可能開始的事情）。2025 年 6 月的版本修復了這種分離。最後，2025 年 11 月的版本（當前穩定版本）帶來了全新的客戶端註冊機制、企業外延和強制 PKCE。

MCP 團隊快速迭代，但快速變化也意味著企業身分驗證仍在發展。確實存在差距，我合作的企業正在遇到這些問題。

## OAuth 問題是結構性的

Doyensec 指出，問題不在於人們以不良方式實施 OAuth（儘管有 492 個公開的 MCP 伺服器沒有身分驗證，Obsidian Security 也報告過單鍵帳戶接管漏洞），而是 OAuth 本身的設計問題。

OAuth 的設計假設是基於不同的信任模型。

OAuth 假設使用者會閱讀同意畫面並做出決定。但企業環境中的 MCP 是由 LLM 在執行時自行決定需要的範圍。

這是不同的情況。OAuth 的設計確實存在困難，規格團隊正在處理這個問題。

## 企業授權仍有一些開放問題

[企業管理授權外延 (JAG)](https://github.com/modelcontextprotocol/ext-auth/blob/main/specification/draft/enterprise-managed-authorization.mdx) 嘗試透過將同意與授權解耦，讓企業政策代替使用者做決定來解決問題。

Doyensec 識別了四個問題：

### 1. 沒有存取無效機制

當代理表現異常（提示注入、濫用範圍等）時，沒有標準化方式撤銷 ID-JAG 令牌。每個供應商都必須建立自己的復原機制，這增加了事件回應的複雜性。

### 2. LLM 濫用範圍而無需使用者同意

LLM 可以自主請求企業政策允許的任何範圍，包括與當前任務無關的範圍。在經典的 M2M 環境中，人會直接下令執行任務；但在 MCP 中，模型自行做決定，這是根本不同的信任模型。

### 3. IdP 之間範圍名稱空間碰撞

多個 IdP 管理具有相同範圍名稱的重疊授權伺服器，例如 `files:read and create`，這會產生跨伺服器存取問題。如果受眾驗證不嚴格，來自伺服器 B 的低權限令牌可能會誤用進入伺服器 A。

### 4. ID-JAG 重播放大

單一 ID-JAG 可以生成多個存取令牌，每個令牌都能呼叫高影響工具。規格未強制要求對 `JTI` 聲明進行單次使用檢查，這可能擴大損害範圍。

這不是假設。這些是規格最終化時的開放決策，目前會造成安全差距。

## 企業安全主要依靠外延

這可能是最常被忽略的重要問題。

Anthropic 維護者 David Soria Parra 上週發布的 [2026 MCP 路線圖](http://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/) 指出，企業功能不應該增加基礎協議重量，因此大部分將作為外延推出。

這種設計哲學是合理的，不應該讓 90% 使用者不需要的需求增加協議重量，保持核心規格輕便會更容易採用。

實際情況是核心規格目前：

- **沒有 mTLS 或基於證書的身分驗證：** mTLS 只是保安最佳實踐建議，還沒有作為機制實現。（詳 [claude-code #9869](https://github.com/anthropics/claude-code/issues/9869)）
- **沒有每工具授權：** OAuth 範圍只授權伺服器存取，而不是個別工具。連接到伺服器就能呼叫任何工具，這對擁有 20+ 工具的企業來說太粗糙。
- **沒有稽核軌道規格：** 路線圖承認這是差距。如果您在受法規管制的行業（大多數企業都是），您需要每個 MCP 互動的結構化稽核記錄。
- **沒有網關行為規格：** 每個在 API 網關後面部署 MCP 的企業都必須自行執行政策。雖然每天都有公司建立 MCP 網關，但規格層級缺乏指導。

查看 [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)，十個風險中有五個與身分驗證和授權直接相關。一半的威脅模型涉及規格正在處理的領域。

## 部署障礙

我大部分時間都在與企業保安和基礎設施團隊談論如何實際部署這些東西。

我常看到這種模式：團隊對 MCP 興奮並用本地伺服器建立原型，一切運作良好。但當他們試圖將遠端 MCP 伺服器部署到生產環境時，會遇到身分複雜性的障礙。

Doyensec 的 [序列圖](https://blog.doyensec.com/public/images/MCP_Authz_SequenceDiagram.pdf) 顯示每個步驟都是注入點，這是身分複雜性的視覺表示。

## Teleport 的 MCP 部署方法

Teleport 不參與 OAuth 遊戲，不嘗試修復令牌交換鏈，而是作為協議級代理處理身分、身分驗證、授權和稽核。

實際機制的工作方式如下：

1. MCP 伺服器註冊為 Teleport 應用程式。
2. [tbot 代理](https://goteleport.com/docs/machine-workload-identity/) 使用平台簽名的身分文件（AWS IAM、Kubernetes API 伺服器、GCP、Azure、TPM）進行身分驗證，確保不使用共享機密。
3. 加入後，它持有自動旋轉的短效 X.509 證書。

使用者或代理通過 Teleport 連接到 MCP 伺服器時，代理使用 CA 簽署的 JWT 處理外發身分驗證。客戶端不與 MCP 伺服器直接協商 OAuth。

Doyensec 的序列圖大部分問題因此不再相關。

最關鍵的是 [兩級 MCP RBAC 模型](https://goteleport.com/docs/enroll-resources/mcp-access/rbac/)：

- 第一級控制您可以連接的 MCP 伺服器。
- 第二級控制您可以呼叫的伺服器內部的特定工具，使用文字名稱、glob（`read_*`）或正則表達式（`^(get|query|list)_.*$`）。

這是 MCP 規格沒有每工具授權。

新的 MCP 伺服器預設拒絕所有工具。您可以看到伺服器並列出工具，但在角色策略明確允許之前無法呼叫任何內容。這與大多數 MCP 實現相反，後者會立即向所有客戶端暴露工具。

對於 JAG 同意問題，特別是 LLM 自行選擇範圍，工具級 RBAC 解決了這個問題。即使模型請求 `slack_post_message`，除非角色策略明確允許，否則會被拒絕。授權決定基於加密身分，而不是根據 LLM 的請求。

每個 [MCP JSON-RPC 請求](https://goteleport.com/docs/reference/audit-events/#mcpsessionrequest) 都記錄為結構化稽核事件，包含工具名稱、輸入參數、客戶端身分、授權決定、時間戳和會話情境。這是預設行為。

## MCP 目前的情況

MCP 仍然處於早期。

規格正在演變。SEP 流程有提案用於 [DPoP](https://datatracker.ietf.org/doc/html/rfc9449)、工作負載身分聯邦和驗證的客戶端註冊。Dick Hardt 也提出了使用 [HTTP 訊息簽名](https://www.ietf.org/archive/id/draft-hardt-httpbis-signature-key-01.html) 的伺服器端授權管理替代方案。

「可以改善」和「已準備好用於企業生產」是不同的事情。

MCP 規格將企業安全委派給外延，沒有專門的工作組。Teleport 的 [2026 調查](https://goteleport.com/resources/surveys/infrastructure-identity-survey-2026/) 發現 67% 的 AI 系統仍依賴靜態憑證，過權限系統的事件率比最權限部署高出 4.5 倍。

我合作的企業無法等待規格成熟，需要現在部署 MCP，同時擁有他們對其他系統需要的安全屬性：[加密身分](https://goteleport.com/blog/best-practices-secretless-engineering-automation/)、最小權限存取、全面稽核和集中政策執行。

Doyensec 文章的結論是基於證書的身分驗證和 mTLS。這不僅是因為我在 Teleport 工作，而是我們花了十年為 SSH、Kubernetes、數據庫和應用程式建立這些技術。

Anthropic 團隊和 MCP 維護者在整個過程中回應了社區反饋。

Anthropic 團隊和 MCP 維護者在整個過程中回應了社區反饋。規格在短時間內大幅改善；SEP 流程開放並持續移動。Doyensec 的 PR 也獲得了建設性參與。對於早期協議來說，這種開放性很重要。

我們贊助 Doyensec 研究是因為我們認為 MCP 值得投資，維護者的回應性增加了我們的信心。

### 進一步閱讀：

→ [Doyensec：The MCP AuthN/Z Nightmare](https://blog.doyensec.com/2026/03/05/mcp-nightmare.html)
→ [Teleport 代理身分框架](https://goteleport.com/docs/agentic-identity-framework/)
→ [Teleport MCP 存取、可串流 HTTP](https://goteleport.com/docs/enroll-resources/mcp-access/enrolling-mcp-servers/streamable-http/)
→ [企業管理授權外延草稿](https://github.com/modelcontextprotocol/ext-auth/blob/main/specification/draft/enterprise-managed-authorization.mdx)

### 備註

- 緣起：
  - 2026-10-07 - AlphaSignal newsletter "Teleport ▸ Why MCP Breaks Between Prototype and Production"
- 整理：
  - Tool: Pi Agent + llama.cpp/Qwen3.5-9B:32K, llama.cpp/Qwen3.5-9B:48K

> [!NOTE]
> 請將 "The Complicating Factors of Deploying MCP in the Enterprise.md" 重新撰寫成中文
> 請務必保留原文 markdown 語法有外部連結的部份
> 使用 speak-human-tw skill 來處理這個翻譯結果，這次直接套用，不用先問
> ，並存成 Enterprise_MCP_Deployment.zh-TW.md