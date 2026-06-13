# Github Copilot

- Study Guide
  - https://assets.ctfassets.net/wfutmusr1t3h/3i7ISEUsTLBgOGrWrML07y/dd586e2b2b607988e2679ed8cce36a76/github-copilot-exam-preparation-study-guide.pdf

## 2026-06-02

- 緣起：同事們提到使用 Github Copilot 然後讓它分別扮演不同的角色協作，好奇 Copilot 是否支援 subagent 的設計。

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI Mode
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
github copilot 有 sub-agent 的概念嗎？
可以讓 Github Copilot 分別扮演不同的角色進行團隊合作嗎？
例如 Product Manager, Scrum Master, UX Designer, Frontend Developer,
 Backend Developer, Database Developer
</td></tr><tr><td>A:</td><td>

## Github Copilot Sub-agent

是的，[GitHub Copilot](https://github.com/orgs/community/discussions/192232) 完全具備 Sub-agent（子代理）與 Multi-agent（多代理）的架構與概念。 [1, 2]
GitHub 官方推出了 Custom Agents（自訂代理人） 功能，並在 IDE（如 VS Code）中內建了 Sub-agent 編排器（Orchestration）。這意味著你完全可以讓 GitHub Copilot 分別扮演 Product Manager、Scrum Master、UX Designer、Frontend/Backend Developer 及 Database Developer 等角色，並在同一個專案或對話中進行分工與團隊合作。 [2, 3, 4, 5, 6]

以下為您說明其實現原理，以及如何具體配置出一個虛擬的「軟體開發團隊」。

### 一、 GitHub Copilot 的 Sub-agent 運作機制

GitHub Copilot 的多代理架構主要透過以下幾種方式運作：

1. 獨立的上下文視窗（Isolated Context Windows）：
  主代理人（Orchestrator）在收到複雜任務時，會調用多個特定的 Sub-agents。每個子代理都在獨立的沙盒環境中運行，它們擁有自己專屬的提示詞（System Prompt）、工具集與上下文，處理完畢後再將結果回傳給主代理，避免單一對話視窗被海量資訊塞滿（Token 爆炸）。 [2, 7, 8, 9]
2. 客製化團隊角色（Custom Personas）：
  透過在專案中建立 `.agent.md` 或 `.github/agents/` 設定檔，你可以將團隊中的特定職位（如 UX、Backend）參數化。 [3, 10]
3. 模型上下文協定（MCP, Model Context Protocol）：
  每個 Sub-agent 除了看程式碼之外，還可以綁定外部工具。例如：Database Developer 代理可以連接到真實資料庫讀取 Schema；Scrum Master 可以透過 MCP 串接 Jira 或 GitHub Issues 來管理看板。 [11, 12]

### 二、 如何動態建立與調用你的「虛擬開發團隊」？

你可以利用 Custom Agent Profile (Markdown 配置法)，在專案根目錄的 `.github/agents/`（或自訂的 `agents/` 目錄）中建立不同的角色檔案： [10, 13]

#### 1. 建立角色定義檔

你可以為每個職位各寫一個 `.agent.md` 檔案： [3]

* `pm.agent.md` (Product Manager)

```md
---name: pm
description: 產品經理，負責分析 PRD 與撰寫 User Story。
tools: [github-issues-explorer]
---
你是一位資深的產品經理。請遵循 Agile 規範，負責將使用者的模糊需求轉化為明確的 Feature、User Story 與驗收標準（AC）。
```

* `scrum-master.agent.md` (Scrum Master)

```md
---name: scrum-master
description: 敏捷教練，負責拆解任務、估算點數。
---
你是一位 Scrum Master。請將 PM 寫好的 User Story 拆解成前端、後端、資料庫的 sub-tasks，並分配給對應的角色。
```

* `ux-designer.agent.md` (UX Designer)

```md
---name: ux-designer
description: UI/UX 專家，專精元件設計與排版邏輯。
---
你負責設計系統的資訊架構。請根據 PM 的需求提供 JSON 格式的 UI 組件狀態樹、欄位驗證邏輯與無障礙網頁（A11y）指南。
```

* `frontend.agent.md` / `backend.agent.md` / `db-dev.agent.md`

```md
---name: db-dev
description: 資料庫工程師，精通 SQL 與資料庫正規化。
---
你負責設計實體關係圖（ERD）與產出 PostgreSQL 遷移腳本（Migration SQL）。請確保欄位有適當的索引與外鍵約束。
```

#### 2. 調用與團隊合作（Workflow Handoff）

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

## 2026-06-13

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
can I define Agent Skills only for specific SubAgent in Github Copilot?
</td></tr><tr><td>A:</td><td>

## Sub-agent with specific Agent Skills

Yes, you can define Agent Skills specifically for a target custom agent or subagent. By default, subagents are completely opt-in and do not inherit any global or parent-level skills automatically. This architectural isolation ensures you can target exactly which skills load into a specific subagent's execution environment. [1, 2]
Depending on how you are setting up your workspace and Custom Agents (`.agent.md` files or programmatic configuration), you can strictly isolate Agent Skills using the following methods: [1, 3, 4]

### 1.Using the `skills` Field in Agent Manifests

When configuring custom agents or specialized subagents programmatically or via YAML configuration files, you use an explicit `skills` property array. [1, 5, 6, 7]

```js
// Example: Explicitly mapping skills to specific custom agents
const session = await client.createSession({
  customAgents: [
    { name: "security-auditor", skills: ["security-scan"] },
    { name: "docs-writer", skills: ["markdown-lint"] }
  ]
});
```

-   Targeted Injection: Skills listed in the array are injected only into the specified subagent.
-   Isolation: Agents without a defined `skills` array operate with zero skill access. [1, 2]

### 2.Targeting via `SKILL.md` Metadata (Allowlisting) [8, 9, 10]

You can restrict skill discovery by using YAML frontmatter in `SKILL.md` files (typically found in `.github/skills/`) to define which agents are allowed to use it: [9, 10, 11, 12, 13]

```yaml
---
name: db-migrator
main-agent: falseagents:
  - database-specialist-agent
---
```

-   `main-agent: false`: Prevents the global chat agent from using the skill.
-   `agents: <allowlist>`: Limits usage to specific, declared subagents. [10]

Would you like help formatting the YAML frontmatter for a specific `SKILL.md` file, or are you trying to configure a custom agent workflow using an orchestrator pattern? [3, 9, 14, 15]

[1] [https://docs.github.com](https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/custom-agents)
[2] [https://docs.github.com](https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/skills)
[3] [https://github.com](https://github.com/orgs/community/discussions/192232)
[4] [https://docs.langchain.com](https://docs.langchain.com/oss/javascript/deepagents/skills)
[5] [https://github.com](https://github.com/github/copilot-cli/issues/3532)
[6] [https://github.com](https://github.com/agentskills/agentskills/discussions/243)
[7] [https://www.threads.com](https://www.threads.com/@jacquelinetwillie/post/DV-AIpBDl_N/heres-something-that-surprises-people-subagents-dont-automatically-see-your-skil)
[8] [https://arxiv.org](https://arxiv.org/html/2602.14211v1)
[9] [https://docs.github.com](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)
[10] [https://github.com](https://github.com/anthropics/claude-code/issues/12633)
[11] [https://blog.cloud-eng.nl](https://blog.cloud-eng.nl/2025/12/22/copilot-customization/)
[12] [https://devblogs.microsoft.com](https://devblogs.microsoft.com/visualstudio/visual-studio-march-update-build-your-own-custom-agents/)
[13] [https://github.com](https://github.com/github/copilot-cli/issues/3532)
[14] [https://github.com](https://github.com/orgs/community/discussions/183962)
[15] [https://docs.github.com](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills)

</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
可以給我一個實作範例嗎？例如有 Product Manager 跟 Full Stack Developer 兩個 Sub-agent
</td></tr><tr><td>A:</td><td>

## Example: Sub-agent with independent Skills

這裡提供一個使用 GitHub Copilot 擴充功能架構（Copilot Extensions / Custom Agents）的實作範例。

在實務上，我們會透過一個主代理人（Orchestrator Agent）接收使用者的需求，並根據當前的情境，動態呼叫並配置具備特定技能（Skills）的 Product Manager (PM) 與 Full Stack Developer 兩個 Sub-agent。 [1]

### 1. 專案目錄結構

```
copilot-multi-agent/
├── src/
│   ├── agents/
│   │   ├── pmAgent.js        # Product Manager Sub-agent
│   │   └── devAgent.js       # Full Stack Developer Sub-agent
│   └── index.js              # 主代理人 (Orchestrator) 進入點
└── package.json

```

### 2. Product Manager Sub-agent 實作

PM 代理人專注於需求分析與 PRD 撰寫，我們只賦予它 `read-user-stories` 與 `generate-prd` 兩種技能。

```js
// src/agents/pmAgent.js
export async function handlePMAgent(payload) {
  // 1. 定義該 Sub-agent 專屬的技能 (Skills) 與 System Prompt
  const pmSkills = [
    { name: "read-user-stories", description: "分析使用者原始需求與痛點" },
    { name: "generate-prd", description: "產出標準軟體產品需求文件 (PRD)" }
  ];

  const systemPrompt = `你是一位資深的 Product Manager。
  你只能使用以下技能來處理任務：${JSON.stringify(pmSkills)}。
  請將使用者的想法轉化為結構化的 PRD，包含功能範疇與驗收條件。`;

  // 2. 呼叫 GitHub Copilot LLM API (模擬轉發)
  const response = await fetch("https://githubcopilot.com", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${payload.token}`,
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      messages: [
        { role: "system", content: systemPrompt },
        { role: "user", content: payload.prompt }
      ],
      temperature: 0.3    // PM 需要較高的一致性與邏輯
    })
  });

  return response.json();
}
```

### 3. Full Stack Developer Sub-agent 實作

Dev 代理人專注於程式碼實作與架構設計，我們賦予它與 PM 完全不同的技能：`write-code` 與 `database-migration`。

```js
// src/agents/devAgent.js
exportasyncfunction handleDevAgent(payload) {
  // 1. 定義該 Sub-agent 專屬的技能 (Skills)
  const devSkills = [
    { name: "write-code", description: "編寫前端 React 與後端 Node.js 程式碼" },
    { name: "database-migration", description: "設計資料庫 Schema 與產生 Migration 腳本" }
  ];

  const systemPrompt = `你是一位精通全端開發的 Full Stack Developer。
  你只能使用以下技能來處理任務：${JSON.stringify(devSkills)}。
  請根據提供的需求或 PRD，產出乾淨、具備單元測試且符合資安規範的程式碼與資料庫設計。`;

  // 2. 呼叫 GitHub Copilot LLM API
  const response = await fetch("https://githubcopilot.com", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${payload.token}`,
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      messages: [
        { role: "system", content: systemPrompt },
        { role: "user", content: payload.prompt }
      ],
      temperature: 0.2// 程式碼生成需要更低的隨機性
    })
  });

  return response.json();
}
```

### 4. 主代理人 (Orchestrator) 路由邏輯

主代理人負責扮演團隊溝通橋樑，根據使用者的輸入（例如關鍵字或明確指令），將任務分派給綁定特定 Skill 的 Sub-agent。

```js
// src/index.js
import { handlePMAgent } from"./agents/pmAgent.js";
import { handleDevAgent } from"./agents/devAgent.js";

exportasyncfunction orchestratorHandler(req, res) {
  const { prompt, token } = req.body;

  // 簡單的路由邏輯：判斷應該觸發哪一個專屬技能的 Sub-agent
  const isManagerTask = prompt.includes("需求") || prompt.includes("PRD") || prompt.includes("規劃");
  const isDevTask = prompt.includes("寫程式") || prompt.includes("Code") || prompt.includes("資料庫");

  try {
    if (isManagerTask) {
      // 路由至 PM Sub-agent，此時該環境僅載入 PM Skill
      sconst pmResult = await handlePMAgent({ prompt, token });
      return res.json({ agent: "Product Manager", result: pmResult });
    }

    if (isDevTask) {
      // 路由至 Dev Sub-agent，此時該環境僅載入 Dev Skills
      const devResult = await handleDevAgent({ prompt, token });
      return res.json({ agent: "Full Stack Developer", result: devResult });
    }

    // 預設回應（若無法識別則由主代理人直接回答）
    return res.json({
      agent: "Orchestrator",
      result: "我是一個協調器。請告訴我你需要『PM 規劃需求』還是『Dev 撰寫程式碼』？"
    });

  } catch (error) {
    return res.status(500).json({ error: error.message });
  }
}
```

### 架構優勢說明

1.  技能完全隔離：當使用者要求「幫我寫程式」時，`pmAgent` 的 `generate-prd` 技能完全不會被載入，避免 LLM 產生幻覺（Hallucination）去嘗試規劃需求。
2.  Context Token 節省：不需將所有角色（PM + Dev）的 System prompt 和所有 Skills 說明一次全部塞給 Copilot API，大幅節省 Token 消耗並提升回應速度。

請問您目前這套 Agent 是打算部署在 GitHub App 後端服務上，還是想透過本地專案的 `.github/workflows` / 設定檔 來讓團隊在 VS Code 中直接使用呢？

[1] [https://zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/1903376889793455465)

</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
本地端專案. <br/>
問題：為何這是放在 .github/workflows？
</td></tr><tr><td>A:</td><td>

## Sub-agent Project Structure

抱歉，前一個回答讓您產生了混淆！這是我的疏忽，程式碼與技能定義在本地專案中，絕對不是放在 `.github/workflows` 裡。

`.github/workflows` 是用來跑 GitHub Actions CI/CD 自動化腳本（如測試、部署）的地方，並不適合用來存放本地專案的 Agent 程式碼。 [1]

之所以會產生這個混淆，是因為在 GitHub Copilot 的生態系中，本地專案的 Agent 實作分成兩種完全不同的路徑。以下為您釐清正確的檔案存放位置：

### 正確位置 1

如果您使用的是 GitHub 官方最新的「Agent Skills (`SKILL.md`)」架構

如果您希望團隊成員在 VS Code 或 GitHub Copilot Chat 中，直接透過 `.github/` 目錄 的設定檔來限制 Sub-agent 的技能，正確的專案結構與路徑應該如下： [2, 3, 4]

```
您的本地專案根目錄/
└── .github/
    └── skills/                # 這是正確的技能目錄，非 workflows！
        ├── product-manager/   # PM 的技能資料夾
        │   └── SKILL.md       # PM 的技能描述與限制
        └── fullstack-dev/     # Dev 的技能資料夾
            └── SKILL.md       # Dev 的技能描述與限制

```

在這個模式下，不需要寫 Node.js 程式碼。您只需要在各個 `SKILL.md` 的 YAML frontmatter (最上方的設定區) 限制哪個 Sub-agent 可以使用這個技能： [1, 2, 5]
`.github/skills/product-manager/SKILL.md` 的內容：

```yaml
---
name: generate-prd
description: 用於分析需求並產出產品需求文件 (PRD)
main-agent: false            # 禁用全域的 @copilot 主代理人agents:
  - product-manager-agent    # 限制：只有名為 pm-agent 的 Sub-agent 可以載入此技能
---
# 這裡寫 PM 技能的具體 Prompt 指引...
當使用者啟動此技能時，請依照標準模板產出規格書。

```

### 正確位置 2

如果您是用程式碼實作「自訂 Web 服務 (Custom Extension Agent)」

如果您希望像前一個範例一樣，用 JavaScript/Node.js 寫出具有路由邏輯、高度客製化的 Orchestrator，這個服務必須運行在您本地端的後端伺服器上（例如用 Node.js 跑在 `http://localhost:3000`）。 [1]

它的專案結構就是一般的 Node.js 專案：

```
您的 Agent 後端專案/
├── src/
│   ├── agents/
│   │   ├── pmAgent.js
│   │   └── devAgent.js
│   └── index.js             # 本地 Express 或 Fastify 伺服器
├── package.json
└── ...

```

-   怎麼讓 Copilot 抓到它？：在本地開發時，您會使用 `ngrok` 或 `localtunnel` 將本地的 `3000` 埠口暴露成一個臨時的 HTTPS 網址，然後在 GitHub 帳號設定的 Developer Settings > GitHub Apps 中，將「Copilot Agent URL」指向該網址，這樣您在本地 VS Code 輸入 `@your-agent` 時，流量就會打回您本地這台電腦的 Node.js 程式碼了。

### 總結您的下一步

再次為前面的混淆道歉。如果您的目標是最簡單、不需架伺服器、純靠本地專案設定檔讓全團隊在 VS Code 中共享這兩個 Sub-agent 的話：
您可以直接在專案根目錄建立 `.github/skills/` 目錄。想請問您，我們接下來要直接針對 `SKILL.md` 的 YAML 與 Markdown 指引來撰寫 PM 與 Dev 的本地規範嗎？ [2, 4, 5]

[1] [https://www.youtube.com](https://www.youtube.com/watch?v=QcxL0SXILC4)
[2] [https://learn.microsoft.com](https://learn.microsoft.com/zh-tw/visualstudio/ide/copilot-agent-skills?view=visualstudio)
[3] [https://www.youtube.com](https://www.youtube.com/watch?v=-yKALFS5ewY&t=177)
[4] [https://www.youtube.com](https://www.youtube.com/watch?v=fabAI1OKKww&t=83)
[5] [https://pcion123.github.io](https://pcion123.github.io/2026/03/31/vscode-skill-intro/)

</td></tr>
</table>