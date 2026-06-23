# Antigravity CLI

- Close Source
- Github Repo is only for bug tracking

---

[TOC]

---

## 2026-06-23

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI Mode
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
Gemini CLI 與 Antigravity CLI 的差異
</td></tr><tr><td>A:</td><td>

## Gemini CLI vs Antigravity CLI

Antigravity CLI 是 Google 推出用來全面取代舊版 Gemini CLI 的新世代工具。 兩者最核心的本質差異在於，舊版 Gemini CLI 定位為「對話式的終端機 AI 助手」（偏向 Vibe Coding）；而新版 Antigravity CLI 則是「Agent（代理人）導向的開發平台」，專門為了多工編排、背景自動化與大型重構而設計。 [1, 2, 3, 4, 5]
Google 在 Google I/O 2026 正式推出 Antigravity 2.0，並宣布舊版的 Gemini CLI 於 2026 年 6 月 18 日 停止對一般消費者開放，全面強制用戶遷移至 Antigravity CLI（指令改為 `agy`）。 [2, 3, 6]
這兩個命令列工具有以下幾項核心差異：

### 核心底層與架構

-   開發語言與速度： 舊版 Gemini CLI 執行速度較一般；新版 Antigravity CLI 改用 Go 語言重新打造，在終端機的執行速度與回應效能上顯著提升。 [1, 3]
-   共用核心 Runtime (Harness)： Antigravity CLI 與 Antigravity 桌面版共用同一個 Agent 執行緒底層。當桌面版的 Agent 能力升級（如自動排程、自主衍生子代理人），CLI 端的 AI 代理人能力也會同步自動升級。 [1]

### 任務編排與多 Agent 能力

-   多工處理： 舊版 Gemini CLI 在執行大型代碼重構或複雜研究時，終端機會被鎖死，開發者需要手動開多個 `tmux` 視窗來切換。
-   異步平行排程： Antigravity CLI 內建多 Agent 編排功能。當你交付任務後，它會自動在背景將任務拆分給多個子代理（Dynamic Subagents）平行執行（例如同時修改多個專案 Repo），而主終端機不會被鎖死。 [1]

### 專案設定與工作區邏輯

專案初始化與結構設定進行了全面重構，具體對照如下： [6]

| 功能維度 [6, 7] | 舊版 Gemini CLI (Legacy) | 新版 Antigravity CLI (`agy`) |
| --- |  --- |  --- |
| 執行指令 | `gemini` | `agy` |
| 環境初始化 | 手動輸入 `/init` 觸發 | 使用 `agy init` 初始化（自動載入專案規則） |
| 工作區規則檔案 | 僅讀取單一 `GEMINI.md` | 使用 `.agents/rules/` 目錄（支援多檔案規則） |
| 自訂技能 (Skills) | 全域存在 `~/.gemini/gemini-cli/skills/` | 支援專案本地 `.agents/skills/` 與全域設定 |
| 工具協定 (MCP) | 僅支援全域 MCP 設定檔 | 支援專案本地獨立的 `.agents/mcp_config.json` |

### 模型與權杖 (Token) 特性

-   搭配模型： Antigravity CLI 預設導入最新代的 Gemini 3.5 Flash 模型，反應速度極快，不過部分開發者評論其思維較急躁，需搭配精細的 Prompt 指引。 [2, 8]
-   權杖上限差異： 根據開發者反饋，舊版 Gemini CLI 的 Token 輸出限制較為寬鬆（適合長篇大論的思路探討）；而 Antigravity CLI 為了追求「快狠準」的 Agent 執行效率，單次輸出的 Token 上限感官上較窄。 [9, 10]

如果你目前仍在使用舊的工作流程，請儘速將專案環境與 Skill 腳本遷移至 `agy` 體系，以避免既有的指令失效。 [3, 11]
如果想了解更多細節，想請問你目前有打算將特定的舊專案腳本遷移過去，還是想了解如何配置新版 `.agents` 目錄底下的 Skills 或是 MCP 工具呢？

[1] [https://medium.com](https://medium.com/@simon3458/google-io-2026-antigravity-cli-cb19b42706a6)
[2] [https://www.youtube.com](https://www.youtube.com/watch?v=vTsadVEDKPE)
[3] [https://pcrookie.com](https://pcrookie.com/google-antigravity-2-intro/)
[4] [https://www.youtube.com](https://www.youtube.com/watch?v=24e_L19fxvA)
[5] [https://zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/2040316906180241378)
[6] [https://lukehou.com](https://lukehou.com/tutorials/gemini-cli-to-antigravity-migration-checklist)
[7] [https://www.evanlin.com](https://www.evanlin.com/antigravity-cli/)
[8] [https://www.threads.com](https://www.threads.com/@mengqiutu/post/DSUi0I5CTHp/antigravity-%E5%92%8C-gemini-cli-%E7%9A%84%E9%A1%8D%E5%BA%A6%E6%98%AF%E5%88%86%E9%96%8B%E8%A8%88%E7%AE%97%E7%9A%84antigravity%E5%85%8D%E8%B2%BB7%E5%A4%A9%E5%88%B7%E6%96%B0%E4%BB%98%E8%B2%BB%E7%B4%84-5-%E5%B0%8F%E6%99%82%E5%88%B7%E6%96%B0%E5%8F%AF%E7%94%A8%E6%A8%A1%E5%9E%8B%E5%8C%85%E5%90%AB-claude-code-)
[9] [https://www.reddit.com](https://www.reddit.com/r/googlecloud/comments/1qvs1dd/choosing_antigravity_or_gemini_cli/?tl=zh-hant)
[10] [https://www.reddit.com](https://www.reddit.com/r/GeminiCLI/comments/1tuqr05/switched_to_antigravitycli_goodbye_geminicli/?tl=zh-hant)
[11] [https://www.facebook.com](https://www.facebook.com/mukispace/posts/%E6%88%91%E5%AF%A6%E5%9C%A8%E6%90%9E%E4%B8%8D%E6%87%82-gemini-cli-%E5%92%8C-antigravity-cli-%E5%B7%AE%E5%9C%A8%E5%93%AA-/1430942695715476/)

</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
Antigravity CLI 是 open source 嗎?可以在哪裡找到原始碼?
</td></tr><tr><td>A:</td><td>

## Antigravity CLI source code

Antigravity CLI 本身並不是開源軟體（Open Source）。與過去由社群維護或部分開源的 gemini-cli 不同，Antigravity 是 Google 專門為其 AI Agent 生態系打造的專有軟體（Proprietary Software）。 [1, 2] 
雖然它不是開源的，但 Google 有在 GitHub 上建立官方的 Repository 來作為問題追蹤、功能許願與提供官方文件的管道。 [3, 4] 
以下是與其原始碼、下載及相關資源對應的地點：

### 1. 官方 GitHub 專案頁面（非開源原始碼）

雖然裡面沒有包含核心的 Go 語言編譯原始碼，但你可以透過這個 Repo 查看官方 README、回報 Bug，或參與討論：

* 官方 GitHub 倉庫：[google-antigravity/antigravity-cli](https://github.com/google-antigravity/antigravity-cli) [5] 

### 2. 官方安裝與下載管道

因為它是閉源的二進位檔案（Go Binary），你需要透過 Google 的官方管道直接下載安裝腳本或安裝檔： [6, 7] 

* 官方網站與文件：antigravity.google
* 終端機一鍵安裝（Linux / macOS）：
```bash
curl -fsSL https://antigravity.google/cli/install.sh | bash
```
[3, 6] 

### 3. 可以參考的「開源」週邊

如果你想尋找與 Antigravity CLI 相關的開源程式碼來參考（例如怎麼寫它的擴充技能），可以在 GitHub 上尋找社群或開發者分享的 Skills 腳本或 MCP 伺服器設定（例如 [jacob-bd/antigravity-cli-skill](https://github.com/jacob-bd/antigravity-cli-skill)），這些周邊設定檔與擴充套件才是開源且供大家自由修改的。 [7] 

想請問你原本是想修改 CLI 的核心功能，還是希望研究如何開發自訂的擴充工具（Skills / MCP） 來搭配它使用呢？

[1] [https://medium.com](https://medium.com/@simon3458/google-io-2026-antigravity-cli-cb19b42706a6)
[2] [https://thenewstack.io](https://thenewstack.io/google-antigravity-cli/)
[3] [https://github.com](https://github.com/google-antigravity/antigravity-cli)
[4] [https://www.51cto.com](https://www.51cto.com/article/844564.html)
[5] [https://github.com](https://github.com/google-antigravity/antigravity-cli)
[6] [https://medium.com](https://medium.com/google-cloud/getting-started-with-antigravity-cli-3565d5db1e92)
[7] [https://github.com](https://github.com/jacob-bd/antigravity-cli-skill)

</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
需要確認 Antigravity CLI 是否能通過 Enterprise Security Audit, Data Privacy Policy, License compliance 等
</td></tr><tr><td>A:</td><td>

## Antigravity CLI - Enterprise Security Audit

可以，但前提是必須將 Antigravity CLI 綁定至 Google Cloud (GCP) 企業架構下，並搭配 Gemini Code Assist Standard/Enterprise 或 Gemini Enterprise Agent Platform 授權。 [1, 2]
若直接使用個人帳戶（如 Google One AI Premium）登入，會適用消費者條款，這無法通過企業的合規審查。 [3, 4]
以下針對企業三大合規面向（Enterprise Security Audit、Data Privacy Policy、License Compliance）的詳細評估與配置建議：

### 1. 企業安全審查 (Enterprise Security Audit)

由於 Antigravity CLI (`agy`) 具備 AI Agent 自主執行終端機指令與編排的能力，在安全審核上需要特別注意其防禦機制：

-   自主執行風險控制（最大審查重點）：
        -   預設安全模式： 預設為 `request-review`（審查模式），AI 在修改專案檔案或執行指令前，會在終端機顯示 Git Diff 差異對照，必須由人類開發者手動點擊「Yes, apply changes」才會執行。這能確保程式碼異動具備可審查性，符合 ISO 27001 等合規規範。
        -   權限分級： 企業可透過設定檔或命令（`/config`）強制鎖定為 `strict` 或 `request-review` 模式，禁止開發者開啟 `always-proceed`（完全自動化執行）以免發生供應鏈漏洞風險。 [5, 6, 7]
-   憑證與驗證安全性：
        -   `agy` 核心基於 Go 語言打造，驗證時會直接整合系統內建的 System Keyring（如 macOS Keychain、Linux Secret Service）。
        -   支援遠端（Remote/SSH）安全驗證模式，不會在伺服器上留下明文憑證。 [8]
-   工作區信任機制：
        -   初次執行時具備 Workspace Trust 機制（類似 VS Code 信任資料夾模式），AI 代理人必須在獲得明確授權的目錄下才能進行讀取、編輯與指令執行，防止惡意 Prompt 注入（Prompt Injection）導致橫向越權攻擊。 [7, 9]

### 2. 資料隱私權政策 (Data Privacy Policy)

隱私權審查是企業能否導入的關鍵卡關點，其隱私邊界完全取決於你的帳戶登入類型：

-   ⚠️ 消費者/個人方案（無法合規）：
        -   若使用個人 Google 帳戶登入，其服務條款載明：Google 會收集使用者的 Interaction Data（包含輸入的 Prompts、前後文 Source Code 等）用於改進產品與訓練機器學習模型。雖然提供 Telemetry 關閉選項，但原始碼訓練的隱私風險依然存在。 [3, 10]
-   企業商業方案（可合規）：
        -   必須透過 `agy` 登入綁定組織的 Google Cloud Project ID 並驗證計費（Billing）。
        -   一旦切換為企業通道，所有的數據傳輸將完全繼承 GCP 企業級隱私政策（GCP Data Governance & Security）。Google 承諾不會將企業的程式碼、 prompts、或任何上下文數據用於訓練 Google 的基礎模型。
        -   資料傳輸與儲存全面採用企業級加密：傳輸中為 TLS 1.3，靜態儲存為 AES-256。 [7, 11, 12, 13]

### 3. 授權合規性 (License Compliance)

企業在盤點軟體資產與合法授權時，可從以下兩點向法務/採購部門呈報：

-   專有閉源軟體 (Proprietary Software)：
        -   如前所述，Antigravity CLI 並非 open-source，核心二進位檔歸屬於 Google。這意味著企業不需要擔心第三方開源許可證（如 GPL 傳染性、AGPL 商業限制）帶來的智慧財產權與程式碼污染風險。 [12]
-   企業授權綁定 (License Entitlement)：
        -   企業必須向 Google 採購 Gemini Code Assist Standard/Enterprise 或者是 Gemini Enterprise Agent Platform 的 API 授權。
        -   當員工透過 CLI 登入時，系統會自動核對企業 IAM 權限。若無有效企業訂閱，則會觸發 `#3501` 授權錯誤碼（You do not have a valid license of this product），這可防範員工私自安裝盜版或未授權商業軟體的合規漏洞。 [1, 2, 4, 11]

### 💡 企業導入建議清單

如果你的公司近期要針對 Antigravity CLI 進行審查，建議直接建構以下架構：

1.  環境統一： 強制要求同仁一律使用公司的 GCP 專案帳號透過 `agy login`，切勿使用 @gmail.com 登入。
2.  派送配置： 透過 CI/CD 或內部派送工具，統一在專案中建立 `.agents/rules/`，並在設定中限制 `Tool Permission` 為 `request-review`。 [5, 11, 12]

請問你們公司目前已有 Google Cloud (GCP) 企業組織與 Gemini Code Assist 的授權，還是需要從頭評估如何向 Google 申請企業版的 Poc（概念驗證）呢？ [11, 14]

[1] [https://developers.googleblog.com](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)
[2] [https://developers.googleblog.com](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)
[3] [https://github.com](https://github.com/google-antigravity/antigravity-cli)
[4] [https://discuss.ai.google.dev](https://discuss.ai.google.dev/t/help-me-with-a-problem-in-antigravity-cli/172133)
[5] [https://codelabs.developers.google.com](https://codelabs.developers.google.com/antigravity-cli-hands-on)
[6] [https://medium.com](https://medium.com/google-cloud/from-gemini-cli-to-antigravity-cli-automated-owasp-security-compliance-and-agentic-remediation-in-1874b5982dd4)
[7] [https://agentpedia.codes](https://agentpedia.codes/blog/antigravity-cli-deep-dive)
[8] [https://github.com](https://github.com/google-antigravity/antigravity-cli)
[9] [https://codelabs.developers.google.com](https://codelabs.developers.google.com/antigravity-cli-hands-on)
[10] [https://discuss.ai.google.dev](https://discuss.ai.google.dev/t/urgent-data-deletion-opt-out-request-ignored-missing-privacy-settings/121602)
[11] [https://antigravity.google](https://antigravity.google/docs/enterprise)
[12] [https://www.reddit.com](https://www.reddit.com/r/google_antigravity/comments/1sn4845/anitgravity_privacy_policy/)
[13] [https://www.antigravityide.help](https://www.antigravityide.help/privacy)
[14] [https://dev.to](https://dev.to/arindam_1729/antigravity-cli-a-hands-on-guide-to-googles-terminal-coding-agent-5bc7)

<tr style="background-color:lightyellow;"><td>Q:</td><td>
Antigravity CLI 支援哪些 LLM model?
</td></tr><tr><td>A:</td><td>

## Antigravity CLI - LLM support

Antigravity CLI (`agy`) 打破了過去工具只能使用單一模型家族的限制，它採開放式的「多模型」架構。 [1]
除了核心預設的 Google Gemini 系列 之外，它甚至打破門戶之見，直接整合支援了 Anthropic Claude 系列 以及專為開源設計的 GPT-OSS 系列 模型。 [2, 3, 4]
你可以透過在終端機輸入指令 `agy models` 來查詢當前系統可用的模型清單。以下為目前 Antigravity CLI 支援的核心模型列表： [2]

### 1. Google Gemini 核心系列

身為 Google 的親生子，此系列在平台上的整合度與反應速度最為極致：

-   Gemini 3.5 Flash (低 / 中 / 高)： Antigravity CLI 的預設主力模型。在 Google I/O 2026 發表，其執行速度比前代快上 4 倍，特別針對 Agent 的快速局部迭代、偵錯而設計。 [1, 5, 6]
-   Gemini 3.1 Pro (低 / 高)： 適用於需要更高推理解析度、大規模上下文（Context Window）的複雜程式碼分析任務。

> *註：模型後方標註的「低 / 中 / 高」為 Variant 變體機制（例如透過 `--variant` 參數），用來動態調整模型的「思考深度（Thinking Level）」與資源配額，免去頻繁更換模型名稱的麻煩。* [7]

### 2. Anthropic Claude 思考系列

最讓開發者驚豔的是，Google 在 Antigravity 中大方地引入了競爭對手的頂級程式碼模型，供開發者進行複雜的重構工作： [3]

-   Claude Sonnet 4.6 (思考 / Thinking)： 具備極強的邏輯推理與架構規劃能力，是目前許多工程師進行大型 codebase 重構的首選。 [2]
-   Claude Opus 4.6 (思考 / Thinking)： 針對極端複雜演算法、邏輯死結（Deadlock）除錯所使用的最高階推理模型。 [2, 3]

### 3. 開源社群模型 (Open-Source)

-   GPT-OSS 120B (中型 / Medium)： 專為支援開源社群及特定無網/地端合規需求所相容的大型開源權重模型。 [2, 3]


### 🛠️ 如何切換與使用特定模型？

在操作 Antigravity CLI 時，你有兩種方式可以切換模型：

1.  啟動時指定模型（非互動模式 / 腳本自動化）：
    你可以在啟動指令後面加上 `--model` 參數來指定本次 Terminal Session 要運作的模型。例如：
    ```
    agy --model "Gemini 3.5 Flash (Low)"
    ```

2.  互動介面中即時切換（TUI 模式）：
    如果你已經在 `agy` 的互動對話視窗內，可以直接輸入 Slash 指令 `/model` 進行即時切換。例如：
    ```
    > /model gemini-3.1-pro
    ```
    [2, 4]

請注意，您可以使用的模型範圍與額度限制，會取決於你綁定的 Google Cloud 企業方案 或是您的 Antigravity 訂閱層級（如 AI Plus, Pro 或是 Ultra 方案）。 [4, 6]
如果想了解更多細節，想請問你目前是在哪一種付費方案（如 Google Cloud 企業版、或個人 Pro 版）下使用，需要我為你查詢特定模型的權杖（Token）配額限制嗎？

[1] [https://www.aibuilderclub.com](https://www.aibuilderclub.com/blog/antigravity-cli-guide)
[2] [https://codelabs.developers.google.com](https://codelabs.developers.google.com/antigravity-cli-hands-on?hl=zh-tw)
[3] [https://www.darrelltw.com](https://www.darrelltw.com/google-antigravity-ide/)
[4] [https://dev.to](https://dev.to/arindam_1729/antigravity-cli-a-hands-on-guide-to-googles-terminal-coding-agent-5bc7)
[5] [https://antigravity.google](https://antigravity.google/docs/cli-overview)
[6] [https://pcrookie.com](https://pcrookie.com/google-antigravity-2-intro/)
[7] [https://lzw.me](https://lzw.me/docs/opencodedocs/zh-tw/NoeFabris/opencode-antigravity-auth/platforms/available-models/)

</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
Antigravity CLI 與 OpenAI Codex CLI 的 side-by-side comparison
</td></tr><tr><td>A:</td><td>

## Antigravity CLI vs OpenAI Codex CLI

Google Antigravity CLI (`agy`) 與 OpenAI Codex CLI 兩者皆為 2026 年終端機 AI 代理人（AI Coding Agent）的主流競爭者。 雖然兩者都能讀取本地程式碼、寫入檔案並自動執行測試，但其核心架構、開發語言、沙盒安全性以及計費模式有著顯著的差異。 [1, 2, 3, 4, 5, 6, 7]
以下針對兩款 CLI 工具進行 Side-by-Side 的全面對比：

### 📊 核心規格與架構對比

| 比較維度 [1, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13] | Google Antigravity CLI (`agy`) | OpenAI Codex CLI |
| --- |  --- |  --- |
| 開發商 | Google | OpenAI |
| 底層開發語言 | Go 語言（極為輕量，執行續運作穩定） | Rust 語言（記憶體安全與運算效率高） |
| 軟體授權模式 | 專有閉源軟體（由 Google 集中維護發布） | 開源軟體（程式碼託管於 GitHub） |
| 主要底層模型 | 預設 Gemini 3.5 Flash / 3.1 Pro | 預設 GPT-5-Codex |
| 第三方模型支援 | 內建整合 Claude Sonnet 4.6 與 GPT-OSS | 開放支援 Claude、Gemini、DeepSeek、Ollama |
| 執行安全機制 | 本地端 Workspace Trust，需手動審查 Diff | 完全沙盒化執行（Cloud Sandbox 運作更安全） |
| 多代理編排 | 強項，支援背景平行任務與多 Subagents | 支援 Subagents，但單次執行線程較直線性 |
| 生態系連動 | 與 Antigravity 2.0 桌面端共用 Agent Harness | 與 ChatGPT 桌面端、Web 端、IDE 擴充套件連動 |

### 🔍 關鍵差異深究

#### 1. 跨模型包容性與儲存綑綁 (Antigravity 的優勢)

-   Antigravity CLI： 雖然由 Google 開發，但採取極度開放的模型策略。只要每個月花費 $20 美元，除了享有極高的 Gemini 3.5 Token 配額，還能直接調用 Anthropic Claude Sonnet 系列，甚至綑綁了 2TB 的 Google One 雲端空間，CP 值對於重度開發者極具破壞力。 [5]
-   Codex CLI： 預設搭載 OpenAI 專為程式碼優化的 GPT-5-Codex 引擎。雖然近期也開放支援第三方模型，但需要開發者自己準備對應的 API 金鑰或訂閱 ChatGPT Plus/Enterprise 方案才能完整解鎖高階能力。 [5, 10, 11, 14, 15]

#### 2. 安全性與執行環境 (Codex 的優勢)

-   Codex CLI： OpenAI 在 Codex 體系中提供了非常強大的 Cloud Sandbox（雲端沙盒環境）。AI Agent 在幫你執行、測試程式碼時是在一個完全隔離的沙盒內運作，避免惡意程式碼直接破壞開發者的本機系統。 [6]
-   Antigravity CLI： 採用本地端執行機制。雖然有 `Workspace Trust` 信任目錄機制防護，並在每一次下達 Shell 指令、修改檔案前都會要求人類開發者手動點擊（`Y/N`）確認，但安全性本質上較依賴使用者的肉眼審查。 [12, 13]

#### 3. 當前已知的產品痛點

-   Codex CLI（硬體耗損風險）： As of June 2026，根據科技媒體報導與 GitHub 社群回報，Codex CLI 存在一個嚴重的 SQLite 記錄檔寫入錯誤（預設開啟最高噪聲的 TRACE 等級），如果長時間在背景運行，會對開發者的 SSD 硬碟造成極大量的寫入操作，有縮短硬碟壽命的隱憂，使用時需額外注意防範。 [16]
-   Antigravity CLI（語意細緻度）： 其預設的 Gemini 3.5 Flash 雖然速度極快，但部分社群開發者反映其思維較為急躁，在處理非常刁鑽的資料庫邏輯或複雜演算法死結時，表現有時不如 Claude Sonnet 或 Codex。 [5, 6, 17]

### 💡 總結：企業與開發者該如何選擇？

-   建議選擇 Antigravity CLI，如果：
        1.  你的團隊已經深度綁定 Google Cloud (GCP) 企業生態系，需要統一的企業安全與隱私政策。
        2.  你預算有限，但希望在同一個平台內同時切換使用 Gemini 與 Claude 思考模型。
        3.  你高度依賴多專案、多 repo 的背景自動化平行重構。 [5, 6, 9, 18]
-   建議選擇 OpenAI Codex CLI，如果：
        1.  你高度重視 Open Source（開源） 屬性，希望 CLI 工具本身的原始碼完全透明、可受社群公評。
        2.  你需要一個完全沙盒化（Sandbox） 的安全環境來執行 AI 產出的 shell 指令，避免本機環境受損。
        3.  你的工作流高度與 ChatGPT 桌面版、GitHub、Slack 或 OpenAI 的 Assistants 生態系整合。 [1, 6]

想請問你目前評估這兩款工具，主要是為了提升個人日常 Vibe Coding 的開發效率，還是為了幫企業研發團隊尋找標準化的 AI Agent 命令列工具呢？

[1] [https://kilo.ai](https://kilo.ai/articles/claude-code-alternatives-for-terminal)
[2] [https://antigravitylab.net](https://antigravitylab.net/en/articles/antigravity/antigravity-codex-cli-six-month-production-comparison)
[3] [https://www.darrelltw.com](https://www.darrelltw.com/google-antigravity-ide/)
[4] [https://antigravitylab.net](https://antigravitylab.net/en/articles/antigravity/antigravity-vs-codex-comparison-2026)
[5] [https://www.openai-hub.com](https://www.openai-hub.com/news/742)
[6] [https://www.reddit.com](https://www.reddit.com/r/GoogleAntigravityIDE/comments/1qmk0ep/antigravity_vs_opencode_vs_gemini_cli_vs_chatgpt/)
[7] [https://terminaltrove.com](https://terminaltrove.com/compare/ai-coding-agents/antigravity-cli-vs-codex-cli/)
[8] [https://www.sherlock.stanford.edu](https://www.sherlock.stanford.edu/docs/software/ai/coding-agents/)
[9] [https://www.youtube.com](https://www.youtube.com/watch?v=KLI880-L4OU)
[10] [https://developers.openai.com](https://developers.openai.com/learn/codex)
[11] [https://tw.news.yahoo.com](https://tw.news.yahoo.com/openai-codex-cli-%E9%96%8B%E6%94%BE%E6%94%AF%E6%8F%B4%E7%AC%AC%E4%B8%89%E6%96%B9%E6%A8%A1%E5%9E%8B-deepseek-230326172.html)
[12] [https://www.youtube.com](https://www.youtube.com/watch?v=WiWDrTujl_w)
[13] [https://antigravity.google](https://antigravity.google/docs/cli-overview)
[14] [https://www.aiocopilot.com](https://www.aiocopilot.com/blog/best-ai-coding-tools-2026-comparison)
[15] [https://www.stackhawk.com](https://www.stackhawk.com/blog/openai-codex-security/)
[16] [https://hk.news.yahoo.com](https://hk.news.yahoo.com/openai-codex-cli-%E5%AD%98%E5%9C%A8%E5%9A%B4%E9%87%8D%E9%8C%AF%E8%AA%A4-%E5%B9%B4%E5%85%A7%E5%8F%AF%E6%90%8D%E6%AF%80-164720617.html)
[17] [https://www.openai-hub.com](https://www.openai-hub.com/news/742/)
[18] [https://cloudmile.ai](https://cloudmile.ai/tw/resource_blog/gemini-code-assist-enterprise-deployment-google-antigravity-strategy)

</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
有辦法查到 Antigravity CLI 的歷史下載量嗎?
</td></tr><tr><td>A:</td><td>

## Antigravity CLI Download Trend

無法直接查到精確的官方全平台歷史總下載量。 [1]

因為 Antigravity CLI 採用閉源專有軟體模式，官方提供的主流安裝管道都是透過 Google 自身的伺服器（例如 `antigravity.google` 域名下的 CDN）直接下載 `install.sh` 或二進位檔案。這類私有伺服器的後台下載流量統計數據屬於 Google 的內部商業機密，並沒有對大眾公開。 [1, 2]
儘管無法取得全面、實時的官方數據，你仍可以透過以下幾種「側面指標」與公開數據來評估其熱度：

### 1. 第三方鏡像下載站的局部數據

部分平台會上架 Antigravity 相關的桌面端或包裝檔案。例如第三方軟體下載站 [Uptodown 上的 Google Antigravity (Windows 版)](https://google-antigravity.en.uptodown.com/windows/download) 頁面，截至 2026 年 6 月初單一平台的公開下載量紀錄約為 24,771 次。但這僅代表該特定非官方管道，不包含最大宗的 Linux 與 macOS 終端機一鍵安裝量。 [2, 3]

### 2. 官方 GitHub 專案的 Star 與 Issue 互動率

Google 有在 GitHub 上建立用來追蹤社群回報的專案頁面：[google-antigravity/antigravity-cli](https://github.com/google-antigravity/antigravity-cli)。 [1]

-   雖然這裡不提供二進位檔下載，但透過觀測該儲存庫的 Stars 增長速度、Forks 數量 以及日常活躍的 Issues/Discussions 討論密度，可以等同轉化為核心重度使用者的基數發展趨勢。

### 3. 強制遷移潮的估算（最大使用基數）

由於 Google 在 2026 年 5 月 19 日宣布全面淘汰個人版的 `gemini-cli`，並強制要求所有人在 2026 年 6 月 18 日 前全數遷移至 `agy` (Antigravity CLI)。 [4, 5]

-   這意味著原先 Gemini CLI 的數十萬名個人開發者與企業用戶，已在這一個月內被迫全數轉換為 Antigravity CLI 的下載量。 [6, 7]

總結來說，若需要向公司呈報或進行市場研究，目前無法取得如 npm 或 GitHub Releases 那樣透明的官方計數器。建議以「Google I/O 2026 主打次世代工具」、以及「Gemini CLI 用戶全面強制遷移完成」 作為其已經具備龐大開發者基數的佐證。 [6, 8]

如果需要評估這款工具，想請問你是想用下載量來向主管證明工具的市佔率與穩定度，還是單純對新型 AI 代理人工具的社群熱度感到好奇呢？

[1] [https://github.com](https://github.com/google-antigravity/antigravity-cli)
[2] [https://medium.com](https://medium.com/@simon3458/google-io-2026-antigravity-cli-cb19b42706a6)
[3] [https://google-antigravity.en.uptodown.com](https://google-antigravity.en.uptodown.com/windows/download)
[4] [https://medium.com](https://medium.com/@simon3458/google-io-2026-antigravity-cli-cb19b42706a6)
[5] [https://developers.googleblog.com](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)
[6] [https://ithelp.ithome.com.tw](https://ithelp.ithome.com.tw/m/articles/10398920)
[7] [https://medium.com](https://medium.com/@simon3458/google-io-2026-antigravity-cli-cb19b42706a6)
[8] [https://techcrunch.com](https://techcrunch.com/2026/05/19/google-launches-antigravity-2-0-with-an-updated-desktop-app-and-cli-tool-at-io-2026/)

</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
想用下載量來像主管證明不同 AI Code Agent 的市場佔有率走勢,
像 https://npmtrends.com/ 可以顯示 Claude Code CLI, OpenAI Codex CLI, Github Copilot CLI 與 OpenCode CLI 的下載量差異
</td></tr><tr><td>A:</td><td>

## AI Code Agent Market Share Trends

利用下載量走勢向主管證明 AI Coding Agent 的市場佔有率，確實是最具說服力的客觀數據。
然而在向主管報告時，有一個至關重要的技術落差（Data Gap）必須先向主管說明：

> 📊 市場上的 CLI 工具分為「NPM 分發家族」與「原生編譯二進位檔家族」。
> 像 Claude Code、OpenAI Codex、GitHub Copilot 等工具主要是透過 `npm install` 安裝，因此能在 [npm trends](https://www.npmtrends.com/) 查到 100% 精確的每週下載走勢。
> 但 Google 的 Antigravity CLI 是用 Go 語言 編譯的閉源二進位檔，走的是 Google 自身的 CDN（`antigravity.google`），因此無法在 npm 趨勢圖上呈現。 [1, 2, 3]

為了幫您產出一份可以直接提交給主管的「市場佔有率與下載量趨勢分析報告」，以下為您整理截至 2026 年 6 月 最新 npm 趨勢與各大工具的走勢解讀： [2, 3]

### 📈 2026 年最新 AI Code Agent 下載量與市佔走勢

若您在 npm trends 輸入對應的官方 Package 名稱，會呈現以下三大梯隊的曲線走勢： [2]

#### 第一梯隊：絕對霸主（指數型增長）

-   搜尋 Package 名稱： `@anthropic-ai/claude-code`
-   走勢特徵： 自 2025 年發布以來一路上揚，目前在 npm 的下載量高居第一，且與第二名拉開極大差距。
-   主管報告重點： Claude Code 是目前開發者社群公認「複雜、多檔案重構邏輯最強」的工具。今年 3 月底雖然經歷了 npm 原始碼對照檔（Source Map）外洩的資安風波，但其下載量不減反增，顯示市場對 Anthropic 程式碼推理能力的極高依賴度。 [1, 2, 3, 4, 5, 6]

#### 第二梯隊：大廠標準配備（穩健高昂）

-   搜尋 Package 名稱： `@github/copilot`（新版正式 CLI） 與 `@openai/codex`（或舊稱 `@openai/codex-cli`） [1, 7]
-   走勢特徵：
        -   GitHub Copilot CLI： 曲線非常穩定。由於 GitHub 官方在 2025 年底將舊的擴充組件全面轉向新版 Copilot CLI，並將其納入企業既有的 Copilot 訂閱中，因此其下載量與企業用戶的普及率呈正相關。
        -   OpenAI Codex CLI： 自從底層升級至 GPT-5 / GPT-5.5 引擎並推出更具競爭力的費率後，近幾個月的下載量加速反彈，斜率明顯變陡。在多項 Terminal Agent 基準測試（如 Terminal-Bench 2.1）中更是拿下高達 83.4% 的勝率榜首，是不可忽視的強勁追擊者。 [1, 2, 4, 7, 8, 9]

#### 第三梯隊：開源與黑馬陣營

-   搜尋 Package 名稱： `opencode`（或社群開源核心 `openhands` / `aider`）
-   走勢特徵： 走勢平緩但基數龐大，OpenCode 的 GitHub Stars 已突破 15 萬顆，是開源領域的領頭羊。
-   主管報告重點： 適合重視隱私、不想被單一模型廠商綁定、或是想在內網透過 Ollama 跑地端模型的企業團隊。 [3, 4, 9]

### 🎯 如何向主管補足 Google Antigravity CLI 的數據？

由於主管在 npm trends 上看不到 Antigravity CLI（因為它是 Go 二進位檔），您可以提供以下關鍵數據與時間點向主管說明 Google 的市佔潛力：

1.  強制遷移帶來的基本盤：
    Google 於 2026 年 6 月 18 日 正式關閉了舊版開源的 `gemini-cli` 個人免費層。原先 Gemini CLI 擁有僅次於 Claude Code 的第二大使用基數，這數十萬名開發者已在今年 5~6 月被迫全數下載並遷移至新版 Antigravity CLI，這代表它一上線就直接繼承了巨大的市場份額。 [2, 3, 4]
2.  打破門戶之見的生態優勢：
    Antigravity CLI 不僅支援 Google 自身的 Gemini 3.5 Flash，甚至內建整合了龍頭 Claude Sonnet 的調用。這意味著訂閱 Google 的服務就能同時用到市佔第一和第二的模型能力，對企業採購（License Compliance）來說是極大的成本與管理優勢。 [3, 4]

### 📝 給主管的報告總結建議（您可以直接複製這段）

> 「報告主管，從當前的市場下載量與技術趨勢（npm trends）來看：
>
> -   工程品質導向： 若我們團隊追求最強的邏輯推理與多檔案複雜重構，Claude Code 是目前市場下載量市佔最高的絕對首選。 [2, 3]
> -   生態整合與沙盒安全： 若考量到程式碼執行的安全性，OpenAI Codex CLI 提供雲端沙盒環境，且近期因 GPT-5 升級，市場下載量正在瘋狂飆升。GitHub Copilot CLI 則最適合與我們既有的 GitHub 工作流無縫整合。 [1, 2, 3, 4]
> -   架構多工與多模型包容： Google Antigravity CLI 雖然因採用 Go 原生編譯而未列在 npm 下載量中，但它是 Google 2026 年主推的旗艦級工具，具備 100 萬 Token 超大上下文與背景平行多代理人編排能力。 [3, 4, 10]
>
> 建議我們可以先針對 [選定 1~2 款工具，例如：Claude Code 或 Antigravity] 進行內部的 Poc 安全性與效能測試。」

想請問您，主管目前比較看重「開源可控性（如 OpenCode）」、「大廠合規與安全防護（如 Codex / Antigravity）」，還是「純粹的開發產出效率（如 Claude Code）」呢？我可以針對該面向為您準備更詳細的比較數據。

[1] [https://intuitionlabs.ai](https://intuitionlabs.ai/articles/claude-code-vs-codex-vs-gemini-cli-comparison)
[2] [https://generativeai.pub](https://generativeai.pub/claude-leads-codex-rises-and-gemini-npm-downloads-on-ai-agent-clis-1ad0e8e94437)
[3] [https://devtoollab.com](https://devtoollab.com/blog/top-cli-ai-coding-agents)
[4] [https://pinggy.io](https://pinggy.io/blog/top_cli_based_ai_coding_agents/)
[5] [https://www.npmjs.com](https://www.npmjs.com/package/@anthropic-ai/claude-code)
[6] [https://threatlabz.zscaler.com](https://threatlabz.zscaler.com/blogs/security-research/anthropic-claude-code-leak)
[7] [https://github.com](https://github.com/features/copilot/cli)
[8] [https://www.ithome.com.tw](https://www.ithome.com.tw/news/171416)
[9] [https://www.morphllm.com](https://www.morphllm.com/ai-coding-agent)
[10] [https://xn--uy0a.tw](https://xn--uy0a.tw/AI/ai-cli-coding-tool-pricing-comparison-2026/)

</td></tr>
</table>