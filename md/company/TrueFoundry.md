# TrueFoundry

## 2026-07-09

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI Mode
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
what is TrueFoundry? the context might related to IAM
</td></tr><tr><td>A:</td><td>

TrueFoundry is an enterprise-grade AI Gateway and MLOps platform designed to securely connect, govern, and observe access to Large Language Models (LLMs), AI agents, and underlying data sources. [1] 
In the context of Identity and Access Management (IAM), TrueFoundry serves as a centralized control plane. It bridges traditional enterprise corporate identities (like those managed via Okta, Microsoft Entra ID, or AWS IAM) with the complex authorization requirements of AI workloads and agentic tool executions. [2, 3, 4, 5, 6] 

## The TrueFoundry IAM Mental Model

TrueFoundry structures its security and access architecture around multi-tenant workspace isolation: [7] 

* The Tenant Boundary: Every user, team, virtual service account, and AI resource (e.g., specific LLMs, prompt templates, or databases) belongs to a strictly isolated tenant workspace. Data and access privileges never bleed across different tenants. [7, 8] 
* Decoupled Control vs. Enforcement: The platform separates corporate authentication from local authorization. For instance, an external Identity Provider (IdP) like Okta authenticates who a user or application is, while TrueFoundry acts as the enforcement plane to determine what specific AI tools or models that identity is allowed to interact with. [4, 9] 

## Key IAM Capabilities in TrueFoundry

TrueFoundry solves complex AI security problems using several specialized IAM features: [10, 11] 

## 1. Model and Tool-Level RBAC

Instead of giving developers or AI applications raw API keys (e.g., direct OpenAI or Anthropic keys), requests route through TrueFoundry. Platform teams use Role-Based Access Control (RBAC) to specify exactly which users or teams can call which specific models or third-party APIs. [5, 12, 13, 14] 

## 2. Model Context Protocol (MCP) Access Control

As AI agents increasingly use the [Model Context Protocol (MCP)](https://www.truefoundry.com/blog/truefoundry-and-the-mcp-gateway-revolution-insights-from-gartners-2025-report) to connect with enterprise internal data (like Jira, GitHub, or internal databases), TrueFoundry acts as a protocol gateway. It intercepts JSON-RPC payloads in real-time to ensure an AI agent has explicit permission to execute a specific tool or fetch a certain dataset. [15, 16, 17] 

## 3. On-Behalf-Of (OBO) Token Exchange [18] 

To prevent AI agents from having unrestricted lateral access to company files, TrueFoundry utilizes OBO token exchanges (RFC 8693). When a user prompts an AI agent to fetch a file, TrueFoundry exchanges the user's initial SSO token for an OBO token. The downstream system evaluates the permissions of both the agent and the specific user, ensuring the agent cannot access data the user doesn't personally own. [18] 

## 4. Virtual Accounts & Automated Token Rotation [1] 

For production backend microservices and automated workflows, TrueFoundry provides Virtual Accounts (service accounts). It handles background API token rotations and can automatically sync these rotating credentials natively to enterprise vaults like [HashiCorp Vault](https://www.hashicorp.com/products/vault), AWS Secrets Manager, or GCP Secret Manager. [19, 20, 21] 

## 5. Native Cloud IAM Integration (AWS EKS Example) [2, 22] 

When deployed inside an organization's virtual private cloud (VPC), TrueFoundry works directly with cloud-native IAM setups. For example, on AWS, it creates Kubernetes Service Accounts annotated with specific AWS IAM Roles. Applications exchange these OpenID Connect (OIDC) tokens with the AWS Security Token Service (STS) to receive temporary, safe cloud credentials without hardcoding secrets. [2, 23, 24] 

If you'd like, let me know:

* Is your primary interest around securing user access to LLMs or governing AI agents accessing internal data tools?
* Which Identity Provider (IdP) or Cloud provider (e.g., AWS, Okta, GCP) does your enterprise use?

I can tailor a more specific architectural overview based on your environment.

- [1] [https://www.truefoundry.com](https://www.truefoundry.com/llm-info)
- [2] [https://www.truefoundry.com](https://www.truefoundry.com/docs/use-aws-services-using-iam-serviceaccount)
- [3] [https://www.youtube.com](https://www.youtube.com/watch?v=8FsHo7xoTr4)
- [4] [https://www.truefoundry.com](https://www.truefoundry.com/de/blog/mcp-gateway-cross-app-access-identity-governed-agent-access)
- [5] [https://www.truefoundry.com](https://www.truefoundry.com/blog/api-auth-rbac-in-gateway)
- [6] [https://arxiv.org](https://arxiv.org/html/2505.19301v1)
- [7] [https://www.truefoundry.com](https://www.truefoundry.com/docs/platform/user-team-account-management)
- [8] [https://www.truefoundry.com](https://www.truefoundry.com/docs/platform/user-team-account-management)
- [9] [https://www.youtube.com](https://www.youtube.com/watch?v=f4oqoPE_cqk)
- [10] [https://www.mintmcp.com](https://www.mintmcp.com/blog/mintmcp-vs-truefoundry-vs-ibm-contextforge)
- [11] [https://www.truefoundry.com](https://www.truefoundry.com/blog/ai-security-platforms-and-gateways)
- [12] [https://www.truefoundry.com](https://www.truefoundry.com/ar/blog/how-truefoundry-integrates-with-aws-the-architecture-of-a-control-plane)
- [13] [https://www.truefoundry.com](https://www.truefoundry.com/blog/how-to-host-an-ai-hackathon-without-losing-control-of-your-keys-or-budget-the-truefoundry-architecture)
- [14] [https://www.youtube.com](https://www.youtube.com/watch?v=z_ItF3IBij4)
- [15] [https://www.truefoundry.com](https://www.truefoundry.com/blog/enterprise-mcp-access-control)
- [16] [https://www.truefoundry.com](https://www.truefoundry.com/blog/truefoundry-and-the-mcp-gateway-revolution-insights-from-gartners-2025-report)
- [17] [https://www.truefoundry.com](https://www.truefoundry.com/blog/mcp-access-control)
- [18] [https://www.truefoundry.com](https://www.truefoundry.com/docs/ai-gateway/agents/agent-identity-obo)
- [19] [https://www.truefoundry.com](https://www.truefoundry.com/blog/truefoundry-ml-platform-on-kubernetes)
- [20] [https://www.linkedin.com](https://www.linkedin.com/posts/nikunj-bajaj-10476824_ai-gateway-improvements-virtual-accounts-activity-7397446166034169856-cr_k)
- [21] [https://www.youtube.com](https://www.youtube.com/watch?v=9AbMcuiY-R8&t=738)
- [22] [https://www.truefoundry.com](https://www.truefoundry.com/partners/aws)
- [23] [https://www.truefoundry.com](https://www.truefoundry.com/blog/runlayer-vs-truefoundry)
- [24] [https://www.truefoundry.com](https://www.truefoundry.com/blog/how-truefoundry-integrates-with-aws-the-architecture-of-a-control-plane)

</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
改以中文回答
</td></tr><tr><td>A:</td><td>

TrueFoundry 是一個企業級的 AI 網關與 MLOps 平台，主要用於安全地連接、管理和監控大語言模型（LLMs）、AI 代理（Agents）以及底層的數據源。
在身份與存取管理（IAM）的架構中，TrueFoundry 扮演著中央控制平面的角色。它能將企業現有的傳統身份驗證系統（如 Okta、Microsoft Entra ID 或 AWS IAM），與 AI 工作負載、AI 代理執行工具時所需的複雜授權需求完美橋接。

## TrueFoundry 在 IAM 的核心運作邏輯

TrueFoundry 的安全與存取架構主要基於多租戶工作空間隔離（Multi-tenant Workspace Isolation）：

* 嚴格的租戶邊界：所有用戶、團隊、虛擬服務帳戶（Service Accounts）以及 AI 資源（如特定的 LLM、提示詞模板或資料庫）都被嚴格隔離在各自的租戶空間內，確保數據與存取權限絕不跨租戶外洩。
* 驗證與授權分離：平台將外部身份驗證與內部權限控制分開。例如，由外部身份提供商（IdP，如 Okta）來驗證「用戶是誰」，而 TrueFoundry 則作為執行平面，來決定該身份「被允許使用哪些 AI 工具或模型」。

## 關鍵的 IAM 功能特點

TrueFoundry 透過以下幾項專門的 IAM 機制，來解決 AI 應用帶來的安全挑戰：

### 1. 模型與工具層級的基於角色存取控制（RBAC）

企業不需要直接把 OpenAI 或 Anthropic 的原始 API 金鑰發放給開發者或 AI 應用，所有請求都會經由 TrueFoundry 路由。平台管理員可以透過 RBAC 精細設定哪些用戶或團隊可以呼叫特定的模型或第三方 API。

### 2. 模型上下文協議（MCP）存取控制

當 AI 代理使用 MCP 協議連接企業內部數據（如 Jira、GitHub 或內部資料庫）時，TrueFoundry 會充當協議網關。它會即時攔截並檢查 JSON-RPC 數據包，確保 AI 代理擁有執行該特定工具或獲取該數據的明確授權。

### 3. 代行權限權杖交換（OBO Token Exchange）

為了防止 AI 代理在企業內部系統中擁有過大的橫向移動權限，TrueFoundry 採用了 OBO 權杖交換（RFC 8693） 機制。當用戶要求 AI 代理讀取檔案時，平台會將用戶的 SSO 權杖交換為 OBO 權杖。下游系統會同時驗證「代理」與「該用戶」的權限，確保 AI 代理無法讀取該用戶本身沒權限查看的資料。

### 4. 虛擬帳戶與金鑰自動輪轉

針對自動化工作流或後端微服務，TrueFoundry 提供虛擬帳戶（Virtual Accounts）。平台會自動在背景輪轉 API 金鑰，並能與企業現有的憑證管理中心（如 HashiCorp Vault、AWS Secrets Manager 或 GCP Secret Manager）原生同步。

### 5. 原生雲端 IAM 整合（以 AWS EKS 為例）

當 TrueFoundry 部署在企業的虛擬私有雲（VPC）時，它能與雲端原生的 IAM 完美結合。例如在 AWS 上，它會建立與特定 AWS IAM Roles 關聯的 Kubernetes 服務帳戶，透過 OIDC 機制向 AWS STS 申請臨時且安全的憑證，避免在程式碼中硬編碼（Hardcode）任何敏感金鑰。

如果您想深入了解，可以告訴我：

* 您目前主要關注的是規範員工/用戶存取 LLM 的權限，還是管理 AI Agent 存取內部資料庫工具的權限？
* 貴公司目前使用哪套身份驗證系統（IdP）或雲端平台（例如 Okta、AWS、Azure）？

我可以針對您的具體環境提供更詳細的架構說明。

</td></tr>
</table>
