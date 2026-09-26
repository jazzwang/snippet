## 2026-09-24

- Date: 9/24/2026, 10:20:27 AM
- Models: llama.cpp/Qwen3.5-9B:32K, github-copilot/gpt-5.6-luna
- Messages: 12 user, 60 assistant, 49 tool results, 2 custom
- Tool Calls: 49
- Tokens: ↑168 ↓40k R4.6M W128k

> [!QUESTION]
> /skill:firecrawl-deep-research let's research AI Code Agent Data Privacy issue, start from the following links
> - https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/
> - https://the-agent-report.com/2026/07/grok-build-cli-repo-upload-privacy-july-2026/
> - https://arize.com/blog/ai-coding-agent-privacy/
> - https://www.dexpose.io/ai-data-leaks/
> save the output to a markdown file

## Deep Research: AI Code Agent Data Privacy

**Depth:** Quick
**Scope:** Privacy risks in AI coding agents, beginning with the four supplied articles and cross-checking against independent reporting and vendor documentation.

### Executive Summary

AI coding agents should not be treated as purely local developer tools. Even when an agent runs locally, it may send task-related files, prompts, telemetry, repository indexes, session state, or entire Git repositories to vendor infrastructure.

The most serious issue in the incidents reviewed is not simply that code was transmitted. Cloud inference necessarily requires some code or context to leave the machine. The more important distinction is between:

1. **Task-scoped transmission** — files or code excerpts needed for a specific request.
2. **Background collection** — repository indexing, telemetry, traces, or session snapshots.
3. **Retention** — whether the provider stores the transmitted data.
4. **Training use** — whether the data is used to improve models.
5. **User verifiability** — whether users can independently determine what was sent and whether it was deleted.

The ZCode and Grok Build cases demonstrate a particularly dangerous failure mode: a privacy or training opt-out may not prevent source code from leaving the workstation. In the reported tests, entire Git repositories—including historical commits and files the agent had not read—were uploaded through separate background channels.

The practical conclusion is straightforward: organizations should evaluate AI coding agents as privileged data-processing and networked automation tools, not as ordinary local IDE extensions.

### Key Findings

#### 1. Full-repository uploads are materially different from normal AI context transmission

The ZCode investigation reports that the client packaged workspaces containing:

- Complete `.git` history
- Git LFS objects
- Reflogs
- Deleted or superseded source files
- Internal branches and repository metadata
- Potentially sensitive global configuration data

One reported snapshot contained approximately **42,411 files** and **313 MB** of compressed data, with **86.6% attributed to Git data**. The investigator also reported that the upload mechanism used server-provided encryption keys, meaning the provider—not the user—held the capability to decrypt the archive.

The independent ZCode coverage from The Hacker News similarly describes full repository snapshots and notes that the reported behavior was associated with repository indexing and Repo Wiki functionality.

**Why this matters:** Git history routinely contains credentials, internal hostnames, customer identifiers, unreleased features, and code that has since been deleted from the working tree. Removing a secret from the current filesystem does not remove it from Git history.

Sources:

- [Ferstar: ZCode silent workspace snapshot upload](https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/)
- [The Hacker News: ZCode uploaded full Git repositories](https://thehackernews.com/)
- [The Terminal: ZCode silently uploaded users’ full Git history](https://theterminal.space/software/zcode-silent-git-upload)

#### 2. Grok Build reportedly uploaded repositories independently of files read by the agent

The Grok Build investigation describes two separate data channels:

- A model-request channel containing files relevant to the current task
- A storage channel uploading a Git bundle of the repository

In the reported experiment, the researcher instructed the agent to reply without reading files. The agent reportedly read nothing, but a captured Git bundle still contained a canary file that had never been opened, together with repository history.

A scale test reportedly transferred approximately:

| Channel | Reported data |
|---|---:|
| Model request | Approximately 192 KB |
| Storage upload | Approximately 5.10 GB |
| Relative difference | Approximately 27,800× |

The report also states that a test `.env` file containing fake credentials appeared unredacted in captured traffic.

Independent coverage from Hive Security and The Hacker News supports the central distinction: the test showed transmission and server acceptance of repository data, but did **not** prove that xAI trained on the data or that an employee accessed it.

Sources:

- [The Agent Report: Grok Build repository upload](https://the-agent-report.com/2026/07/grok-build-cli-repo-upload-privacy-july-2026/)
- [Hive Security: What the Grok Build wire capture proved](https://hivesecurity.gitlab.io/blog/grok-build-repository-upload-2026/)
- [The Hacker News: Grok Build uploaded entire Git repositories](https://thehackernews.com/2026/07/grok-build-uploads-entire-git.html)

#### 3. Training opt-out, retention controls, and transmission controls are separate

A recurring source of user confusion is the assumption that disabling model training means code remains local.

The reported Grok Build test found that disabling **“Improve the model”** did not stop repository uploads. The supplied Arize analysis makes the broader point: a setting may govern training consent while a separate service continues to transmit or retain operational data.

These are distinct questions:

| Question | Meaning |
|---|---|
| Was data transmitted? | Did it leave the workstation? |
| Was it retained? | Was it stored after processing? |
| Was it used for training? | Did it enter model improvement pipelines? |
| Was it shared? | Could contractors, subprocessors, or other systems access it? |
| Can deletion be verified? | Can the user independently confirm removal? |

Zero Data Retention (ZDR) generally addresses storage after receipt. It does not necessarily mean that code never reaches the provider.

Vendor documentation reflects this separation:

- Cursor documents that Privacy Mode governs retention and training, while codebase indexing still involves sending code to backend systems to create embeddings.
- GitHub documentation distinguishes individual-plan data use from Business and Enterprise contractual controls.
- OpenAI documentation distinguishes personal-plan data controls from Business, Enterprise, and API handling.

Sources:

- [Arize: AI coding agent privacy](https://arize.com/blog/ai-coding-agent-privacy/)
- [Cursor: Data use](https://cursor.com/data-use)
- [GitHub: Copilot policies for individual subscribers](https://docs.github.com/copilot/how-tos/manage-your-account/managing-copilot-policies-as-an-individual-subscriber)
- [OpenAI: Business data privacy](https://openai.com/business-data/)

#### 4. Encryption does not automatically provide user privacy

Both the ZCode and Grok reports discuss encrypted uploads. Encryption protects data in transit and may protect stored objects from unauthorized third parties, but it does not answer the central governance questions:

- Who controls the decryption key?
- Can the user decrypt or audit the archive?
- What exactly was included?
- How long was it retained?
- Who could access the plaintext?
- Can deletion be independently verified?

In the ZCode case, the investigator reported that the server supplied the public key and retained the corresponding private key. That architecture may protect the upload from outsiders while leaving the provider with exclusive decryption authority.

This is not equivalent to end-to-end encryption controlled by the customer.

#### 5. Agentic permissions create a second, separate leakage path

Full-repository uploads are only one category of risk. AI coding agents also have the ability to:

- Read arbitrary files
- Execute shell commands
- Inspect environment variables
- Access Git history
- Use network tools
- Modify source code
- Interact with package managers and cloud CLIs
- Follow instructions embedded in files, pull requests, or websites

The DeXpose overview identifies prompt injection, excessive permissions, model-output leakage, and misconfigured agents as common AI data-leak mechanisms. Its discussion of GitHub Copilot’s reported “CamoLeak” vulnerability illustrates how malicious instructions hidden in repository content could cause an agent to search for secrets and exfiltrate them.

This risk exists even if the vendor does not intentionally upload the entire repository. A malicious README, issue, pull request, dependency, or generated file may influence an agent with broad permissions.

Source:

- [DeXpose: AI data leaks](https://www.dexpose.io/ai-data-leaks/)

### Risk Model

#### Highest-risk data

Organizations should assume the following may be exposed if an agent can access a repository or its history:

- API keys and cloud credentials
- Database passwords and connection strings
- Signing keys and certificates
- OAuth secrets and webhook tokens
- Proprietary source code
- Unreleased product plans
- Customer data embedded in fixtures or logs
- Security vulnerabilities and exploit research
- Licensed or regulated content
- Internal infrastructure details
- Deleted secrets remaining in Git history

#### Highest-risk product behaviors

The following behaviors deserve heightened scrutiny:

1. Background uploads not initiated by an explicit user action
2. Full-workspace or Git-bundle uploads
3. Server-controlled feature flags that can activate collection remotely
4. Privacy controls that only affect training, not transmission
5. Undocumented storage buckets or telemetry endpoints
6. Encryption where the vendor exclusively controls the keys
7. No local network or upload audit trail
8. Broad shell, filesystem, or network permissions
9. Repository indexing with unclear retention and deletion behavior
10. Consumer plans used for commercial or regulated code

### Recommended Controls

#### For individual developers

- Do not run an agent in a directory containing production credentials.
- Use a clean working copy containing only the minimum files needed.
- Remove secrets from both the current tree and Git history.
- Rotate credentials that may have been present in repositories used by affected agents.
- Inspect agent configuration directories and upload queues.
- Monitor outbound connections when evaluating a new agent.
- Treat `.gitignore` as a commit-prevention mechanism, not a data-loss-prevention control.
- Prefer short-lived credentials injected at runtime rather than `.env` files.
- Use disposable VMs or containers for untrusted repositories and high-autonomy agents.

#### For organizations

- Approve agents by **data-flow behavior**, not product name alone.
- Require a documented data-flow diagram covering model requests, repository indexing, telemetry, session traces, crash reports, storage providers, and subprocessors.
- Separate policies for transmission, retention, training, human access, and deletion.
- Prefer business, enterprise, or API arrangements with contractual data protections.
- Enforce network egress allowlists for development environments.
- Log bulk uploads from developer tools.
- Use DLP controls to detect credentials and regulated data.
- Restrict agent permissions using least privilege.
- Require confirmation before network access, credential access, or destructive commands.
- Re-test network behavior after client updates and remote configuration changes.
- Establish an incident process for code-agent exposure, including credential rotation and legal review.

### Contrarian Views and Limitations

- The supplied articles and independent reports are primarily investigative or journalistic sources, not formal third-party audits.
- Reported behavior is often version-specific and may differ by operating system, plan, region, server configuration, or account type.
- A captured upload proves transmission and, in some cases, server acceptance; it does not by itself prove model training, employee access, or malicious intent.
- Vendor remediation claims may be genuine, but server-side feature flags are not a durable assurance unless independently retested.
- Codebase indexing is not inherently improper. It becomes a privacy concern when scope, retention, access, and deletion are unclear or when users cannot disable it meaningfully.
- Cloud inference inherently requires some data transmission. The appropriate baseline is not “nothing leaves the machine,” but “only the minimum necessary data leaves, under explicit and enforceable controls.”

### Open Questions

1. How many users and repositories were affected in the ZCode and Grok Build incidents?
2. Were historical uploads actually deleted, and can deletion be independently verified?
3. What exact retention periods applied to uploaded snapshots and session traces?
4. Did any subprocessors or human operators access the data?
5. Which other coding agents have undocumented background upload channels?
6. Can remote feature flags reactivate disabled upload code?
7. What contractual protections apply to individual versus enterprise plans?
8. Are vendor privacy policies precise enough to distinguish task context from repository-wide collection?

### Bottom Line

The central privacy issue is not that AI coding agents send code to remote models. It is that users may grant an agent access to a repository while unknowingly granting the vendor permission to copy the repository, its history, and its secrets.

A safe evaluation standard should therefore ask:

> **Exactly what data leaves the machine, through which channels, under whose control, for how long, and how can the user verify the answer?**

If a vendor cannot answer those questions clearly—and if the behavior cannot be independently tested—the repository should be treated as potentially exposed.

### Sources

1. [Ferstar — ZCode silent workspace snapshot upload](https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/) — primary technical investigation supplied by the user.
2. [The Agent Report — Grok Build repository upload](https://the-agent-report.com/2026/07/grok-build-cli-repo-upload-privacy-july-2026/) — wire-level investigation and follow-up claims.
3. [Arize — AI coding agent privacy](https://arize.com/blog/ai-coding-agent-privacy/) — comparison of coding-agent privacy practices.
4. [DeXpose — AI data leaks](https://www.dexpose.io/ai-data-leaks/) — broader AI leakage and prompt-injection context.
5. [Hive Security — Grok Build wire capture](https://hivesecurity.gitlab.io/blog/grok-build-repository-upload-2026/) — independent analysis of the Grok Build evidence.
6. [The Hacker News — Grok Build uploaded Git repositories](https://thehackernews.com/2026/07/grok-build-uploads-entire-git.html) — independent reporting.
7. [Cursor — Data use](https://cursor.com/data-use) — vendor documentation on indexing, Privacy Mode, and data handling.
8. [GitHub — Copilot individual subscriber policies](https://docs.github.com/copilot/how-tos/manage-your-account/managing-copilot-policies-as-an-individual-subscriber) — vendor documentation on interaction data.
9. [OpenAI — Business data privacy](https://openai.com/business-data/) — vendor documentation on business and API data handling.

### Rerun Inputs

```yaml
workflow: firecrawl-deep-research
topic: AI Code Agent Data Privacy
depth: quick
output: markdown
starting_sources:
  - https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/
  - https://the-agent-report.com/2026/07/grok-build-cli-repo-upload-privacy-july-2026/
  - https://arize.com/blog/ai-coding-agent-privacy/
  - https://www.dexpose.io/ai-data-leaks/
```

> [!QUESTION]
> 改以中文輸出至 ai-code-agent-data-privacy.zh_TW.md
> 使用 speak-human-tw skill 不列清單，請直接修改 ai-code-agent-data-privacy.zh_TW.md

## 深度研究：AI 程式碼代理的資料隱私

**研究深度：** 快速
**範圍：** 以使用者提供的四篇文章為起點，並交叉比對獨立報導與供應商文件，研究 AI 程式碼代理的隱私風險。

### 摘要

AI 程式碼代理不能只當成裝在電腦裡的開發工具。它可能把工作檔案、提示內容、遙測資料、儲存庫索引、工作階段狀態，甚至整個 Git 儲存庫送到供應商的伺服器。

雲端模型要處理程式碼，確實需要收到部分上下文。問題在於，送出去的到底是完成任務所需的內容，還是額外的背景資料；資料送達後是否會被保留、拿去訓練模型，以及使用者能不能確認它已被刪除。這幾件事不能混為一談：

1. **任務範圍內的傳輸**：完成特定要求所需的檔案或程式碼片段。
2. **背景收集**：儲存庫索引、遙測、追蹤資料或工作階段快照。
3. **保留**：供應商是否在處理後繼續儲存傳送的資料。
4. **訓練用途**：資料是否被用來改進模型。
5. **使用者可驗證性**：使用者是否能獨立確認傳送了什麼，以及資料是否真的被刪除。

ZCode 與 Grok Build 案例顯示了一種特別危險的失效模式：關閉隱私或模型訓練選項，並不一定能阻止程式碼離開工作站。根據報導中的測試，完整 Git 儲存庫——包括歷史提交，以及代理程式從未讀取的檔案——可能透過獨立的背景通道被上傳。

因此，組織在評估 AI 程式碼代理時，應把它當成能處理敏感資料、擁有高權限並且會連網的自動化工具，而不是普通的 IDE 擴充功能。

### 這次看到的問題

#### 1. 上傳整個儲存庫，和傳送任務所需的程式碼不是同一回事

ZCode 調查指出，客戶端會打包包含以下內容的工作區：

- 完整的 `.git` 歷史
- Git LFS 物件
- reflog（參照日誌）
- 已刪除或已被取代的原始碼檔案
- 內部分支與儲存庫中繼資料
- 可能敏感的全域設定資料

其中一個被報導的快照包含約 **42,411 個檔案**，壓縮後約 **313 MB**，其中 **86.6% 被歸類為 Git 資料**。調查者也指出，上傳機制使用由伺服器提供的加密金鑰；換句話說，具備解密能力的是供應商，而非使用者。

《The Hacker News》的獨立報導同樣描述了完整儲存庫快照，並指出相關行為與儲存庫索引及 Repo Wiki 功能有關。

**這件事的風險在於：** Git 歷史裡常常還留著憑證、內部主機名稱、客戶識別資料、未公開功能，以及已從目前工作樹刪掉的程式碼。把秘密從現在的檔案中刪掉，不代表它也從 Git 歷史消失。

來源：

- [Ferstar：ZCode 靜默上傳工作區快照](https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/)
- [The Hacker News：ZCode 上傳完整 Git 儲存庫](https://thehackernews.com/)
- [The Terminal：ZCode 靜默上傳使用者完整 Git 歷史](https://theterminal.space/software/zcode-silent-git-upload)

#### 2. Grok Build 被測到會上傳代理根本沒讀過的檔案

Grok Build 調查描述了兩個獨立的資料通道：

- 模型請求通道：包含目前任務相關的檔案
- 儲存通道：上傳儲存庫的 Git bundle

在報導中的實驗裡，研究人員要求代理只回覆內容、不要讀取檔案。代理據稱沒有讀取任何檔案，但攔截到的 Git bundle 仍包含一個代理從未開啟過的測試檔案，以及儲存庫歷史。

一項規模測試據稱傳輸了以下資料：

| 通道 | 報導中的資料量 |
|---|---:|
| 模型請求 | 約 192 KB |
| 儲存上傳 | 約 5.10 GB |
| 相對差異 | 約 27,800 倍 |

報導也指出，一個包含虛構憑證的測試 `.env` 檔案，以未經遮罩的形式出現在攔截到的流量中。

Hive Security 與《The Hacker News》的獨立報導支持這個核心區分：測試顯示儲存庫資料確實被傳送並被伺服器接受，但**沒有**證明 xAI 使用這些資料訓練模型，也沒有證明員工曾存取這些資料。

來源：

- [The Agent Report：Grok Build 上傳儲存庫](https://the-agent-report.com/2026/07/grok-build-cli-repo-upload-privacy-july-2026/)
- [Hive Security：Grok Build 網路封包分析所證明的事項](https://hivesecurity.gitlab.io/blog/grok-build-repository-upload-2026/)
- [The Hacker News：Grok Build 上傳完整 Git 儲存庫](https://thehackernews.com/2026/07/grok-build-uploads-entire-git.html)

#### 3. 關閉模型訓練，不代表程式碼不會離開電腦

最容易搞混的地方，是把「不拿去訓練」理解成「不會離開本機」。這兩件事並不相同。

據報 Grok Build 的測試發現，關閉 **「改善模型」** 並不能阻止儲存庫上傳。使用者提供的 Arize 分析則指出，更廣泛的問題是：某個設定可能只管理訓練同意，另一個獨立服務仍然可以傳輸或保留營運資料。

應分別追問以下問題：

| 問題 | 意義 |
|---|---|
| 資料是否被傳送？ | 資料是否離開工作站？ |
| 資料是否被保留？ | 處理後是否仍被儲存？ |
| 資料是否被用於訓練？ | 是否進入模型改進流程？ |
| 資料是否被分享？ | 承包商、子處理者或其他系統是否能存取？ |
| 能否驗證刪除？ | 使用者能否獨立確認資料已移除？ |

「零資料保留」（Zero Data Retention，ZDR）通常處理的是資料送到供應商之後要不要留下來，不代表程式碼根本沒有送到供應商。

供應商文件也反映了這種區分：

- Cursor 說明，Privacy Mode 管理保留與訓練；但程式碼庫索引仍會把程式碼傳送至後端，以建立嵌入向量。
- GitHub 文件區分個人方案的資料使用方式，以及 Business 與 Enterprise 方案的合約控制。
- OpenAI 文件區分個人方案的資料控制，以及 Business、Enterprise 與 API 的資料處理方式。

來源：

- [Arize：AI 程式碼代理的隱私](https://arize.com/blog/ai-coding-agent-privacy/)
- [Cursor：資料使用方式](https://cursor.com/data-use)
- [GitHub：Copilot 個人訂閱者政策](https://docs.github.com/copilot/how-tos/manage-your-account/managing-copilot-policies-as-an-individual-subscriber)
- [OpenAI：Business 資料隱私](https://openai.com/business-data/)

#### 4. 有加密，不等於使用者掌握了資料

ZCode 與 Grok 報導都討論了加密上傳。加密可以保護傳輸中的資料，也可能降低儲存物件被第三方未授權取得的風險；但它沒有回答以下治理問題：

- 誰控制解密金鑰？
- 使用者能否解密或稽核封存檔？
- 實際包含了哪些資料？
- 資料保留多久？
- 誰能存取明文？
- 能否獨立驗證資料確實被刪除？

在 ZCode 案例中，調查者指出公鑰由伺服器提供，而對應的私鑰由伺服器保留。這種架構可能可以防止外部人士讀取上傳內容，但也代表供應商擁有唯一的解密能力。

這不等同於由客戶掌握金鑰的端對端加密。

#### 5. 代理本身的權限，也可能造成另一條外洩路徑

完整儲存庫上傳只是其中一類風險。AI 程式碼代理也可能具備以下能力：

- 讀取任意檔案
- 執行 Shell 指令
- 檢查環境變數
- 存取 Git 歷史
- 使用網路工具
- 修改原始碼
- 與套件管理器及雲端 CLI 互動
- 遵循嵌入檔案、Pull Request 或網站中的指令

DeXpose 的分析將提示注入、權限過大、模型輸出洩漏，以及代理設定錯誤列為常見的 AI 資料外洩機制。其對 GitHub Copilot 所謂「CamoLeak」漏洞的討論顯示，隱藏在儲存庫內容中的惡意指令，可能誘使代理搜尋秘密並將其外洩。

就算供應商沒有主動上傳整個儲存庫，惡意的 README、Issue、Pull Request、相依套件或產生檔案，仍可能誘導一個權限過大的代理做出不該做的事。

來源：

- [DeXpose：AI 資料外洩](https://www.dexpose.io/ai-data-leaks/)

### 哪些資料最需要小心

#### 容易出事的資料

如果代理能存取儲存庫或其歷史，組織應假設以下資料可能被暴露：

- API 金鑰與雲端憑證
- 資料庫密碼與連線字串
- 簽署金鑰與憑證
- OAuth 秘密與 Webhook Token
- 專有原始碼
- 尚未公開的產品計畫
- 測試資料或日誌中的客戶資料
- 安全漏洞與漏洞研究資料
- 受授權或法規管制的內容
- 內部基礎設施資訊
- Git 歷史中殘留的已刪除秘密

#### 值得警覺的產品行為

以下行為應受到特別審查：

1. 沒有明確使用者操作卻在背景上傳資料
2. 上傳完整工作區或 Git bundle
3. 可由伺服器控制、遠端啟用資料收集的功能旗標
4. 只影響訓練、不影響傳輸的隱私控制
5. 未文件化的儲存貯體或遙測端點
6. 由供應商單方面控制金鑰的加密方式
7. 沒有本機網路或上傳稽核軌跡
8. 廣泛的 Shell、檔案系統或網路權限
9. 保留與刪除行為不清楚的儲存庫索引
10. 將個人方案用於商業或受法規管制的程式碼

### 實際可以怎麼做

#### 如果你是個別開發者

- 不要在包含正式環境憑證的目錄中執行代理。
- 使用只包含完成任務所需檔案的乾淨工作副本。
- 從目前工作樹及 Git 歷史中移除秘密。
- 旋轉可能出現在代理使用過之儲存庫中的憑證。
- 檢查代理程式的設定目錄與上傳佇列。
- 評估新代理時監控對外連線。
- 將 `.gitignore` 視為防止誤提交的機制，而不是防止資料外洩的控制措施。
- 優先使用執行時注入的短效憑證，而不是 `.env` 檔案。
- 對不受信任的儲存庫與高自主性代理，使用一次性虛擬機或容器。

#### 如果是公司或團隊

- 依據**資料流行為**而非產品名稱核准代理。
- 要求供應商提供資料流圖，涵蓋模型請求、儲存庫索引、遙測、工作階段追蹤、錯誤報告、儲存供應商及子處理者。
- 分別制定傳輸、保留、訓練、人工存取與刪除政策。
- 優先選擇具有合約資料保護的 Business、Enterprise 或 API 方案。
- 對開發環境強制執行網路對外連線允許清單。
- 記錄開發工具的大量上傳行為。
- 使用 DLP 控制偵測憑證與受法規管制的資料。
- 依最小權限原則限制代理權限。
- 在網路存取、憑證存取或破壞性指令執行前要求確認。
- 在客戶端更新及遠端設定變更後重新測試網路行為。
- 建立程式碼代理暴露事件的處理流程，包括憑證輪換與法律審查。

### 這份整理的限制

- 使用者提供的文章與獨立報導主要是調查或新聞來源，不是正式的第三方稽核報告。
- 報導中的行為通常與特定版本有關，可能因作業系統、方案、地區、伺服器設定或帳戶類型而不同。
- 攔截到上傳行為可以證明資料被傳送，在某些情況下也能證明伺服器接受了資料；但單憑這點不能證明資料被用於模型訓練、被員工查看，或存在惡意意圖。
- 供應商的修復聲明可能是真實的，但伺服器端功能旗標不是持久的安全邊界，除非能透過獨立測試重新驗證。
- 程式碼庫索引本身並非一定不當；當其範圍、保留、存取及刪除方式不清楚，或使用者無法真正關閉時，才會成為嚴重的隱私問題。
- 雲端推論本來就需要傳輸部分資料。合理的基準不是「完全沒有資料離開本機」，而是「只有必要的最少資料，在明確且可執行的控制下離開本機」。

### 還有幾件事沒有答案

1. ZCode 與 Grok Build 事件實際影響了多少使用者與儲存庫？
2. 歷史上傳資料是否真的被刪除？能否獨立驗證？
3. 上傳快照與工作階段追蹤資料的確切保留期限為何？
4. 子處理者或人工操作員是否存取過這些資料？
5. 還有哪些程式碼代理具有未文件化的背景上傳通道？
6. 遠端功能旗標是否能重新啟用已停用的上傳程式碼？
7. 個人方案與 Enterprise 方案分別提供哪些合約保障？
8. 供應商隱私政策是否足以區分任務上下文與整個儲存庫的收集？

### 最後

AI 程式碼代理把部分程式碼送到遠端模型，本身不一定不合理；模型總得拿到它要分析的內容。真正不能含糊帶過的是：使用者以為自己只是讓代理讀取儲存庫，供應商卻可能因此取得整個儲存庫、完整歷史，甚至其中的秘密。

評估這類工具時，至少要問：

> **究竟有哪些資料會離開本機？透過哪些通道？由誰控制？保留多久？使用者如何驗證答案？**

如果供應商說不清楚，使用者也無法自行測試，那就應該先把這個儲存庫當成可能已經暴露來處理。

### 來源

1. [Ferstar — ZCode 靜默上傳工作區快照](https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/) — 使用者提供的主要技術調查。
2. [The Agent Report — Grok Build 上傳儲存庫](https://the-agent-report.com/2026/07/grok-build-cli-repo-upload-privacy-july-2026/) — 網路層級調查與後續說明。
3. [Arize — AI 程式碼代理的隱私](https://arize.com/blog/ai-coding-agent-privacy/) — 程式碼代理隱私實務比較。
4. [DeXpose — AI 資料外洩](https://www.dexpose.io/ai-data-leaks/) — AI 資料外洩與提示注入的廣泛背景。
5. [Hive Security — Grok Build 網路封包分析](https://hivesecurity.gitlab.io/blog/grok-build-repository-upload-2026/) — 對 Grok Build 證據的獨立分析。
6. [The Hacker News — Grok Build 上傳 Git 儲存庫](https://thehackernews.com/2026/07/grok-build-uploads-entire-git.html) — 獨立新聞報導。
7. [Cursor — 資料使用方式](https://cursor.com/data-use) — 供應商關於索引、Privacy Mode 與資料處理的文件。
8. [GitHub — Copilot 個人訂閱者政策](https://docs.github.com/copilot/how-tos/manage-your-account/managing-copilot-policies-as-an-individual-subscriber) — 供應商關於互動資料的文件。
9. [OpenAI — Business 資料隱私](https://openai.com/business-data/) — 供應商關於 Business 與 API 資料處理的文件。

### 重新執行參數

```yaml
workflow: firecrawl-deep-research
topic: AI 程式碼代理的資料隱私
depth: quick
output: markdown
starting_sources:
  - https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/
  - https://the-agent-report.com/2026/07/grok-build-cli-repo-upload-privacy-july-2026/
  - https://arize.com/blog/ai-coding-agent-privacy/
  - https://www.dexpose.io/ai-data-leaks/
```
