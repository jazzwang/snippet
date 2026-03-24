# Databricks 

## 2026-03-20

- 2026-03-11
  - Introducing Genie Code: Your Autonomous AI Partner for Data Work
  - https://www.databricks.com/blog/introducing-genie-code

### 實戰

> could you guide me how to load huggingface model to Databricks as a service endpoint? take https://huggingface.co/fixie-ai/ultravox-v0_5-llama-3_2-1b as an example

Here's a step-by-step guide for deploying the fixie-ai/ultravox-v0\_5-llama-3\_2-1b model to a Databricks Model Serving endpoint. There are **3 main stages**:

**Stage 1 --- Log & Register the Model in Unity Catalog**

Since Ultravox is a multimodal (audio+text) model that isn't a standard HuggingFace pipeline task, the recommended approach is to wrap it as a **custom MLflow PyFunc model**:

```python
import mlflow
import mlflow.pyfunc

mlflow.set_registry_uri("databricks-uc")

class UltravoxModel(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        from transformers import AutoModel, AutoProcessor
        import torch
        self.model = AutoModel.from_pretrained(
            context.artifacts["model_path"],
            trust_remote_code=True
        )
        self.processor = AutoProcessor.from_pretrained(
            context.artifacts["model_path"],
            trust_remote_code=True
        )

    def predict(self, context, model_input):
        # Your inference logic here
        ...

CATALOG = "your_catalog"
SCHEMA = "your_schema"
MODEL_NAME = "ultravox_v05_llama32_1b"

with mlflow.start_run():
    mlflow.pyfunc.log_model(
        artifact_path="model",
        python_model=UltravoxModel(),
        artifacts={"model_path": "/local/path/to/downloaded/model"},
        pip_requirements=["transformers", "torch", "accelerate"],
        registered_model_name=f"{CATALOG}.{SCHEMA}.{MODEL_NAME}",
    )
```

Alternatively, if the model works with a supported transformers pipeline task, you can use the simpler `mlflow.transformers.log_model` with `save_pretrained=False` to avoid duplicating weights (reference-only mode).

**Stage 2 --- Create the Serving Endpoint**

Use the MLflow Deployments SDK or the Serving UI:

```python
import mlflow.deployments

client = mlflow.deployments.get_deploy_client("databricks")
endpoint = client.create_endpoint(
    name="ultravox-endpoint",
    config={
        "served_entities": [{
            "entity_name": f"{CATALOG}.{SCHEMA}.{MODEL_NAME}",
            "entity_version": "1",
            "workload_size": "Small",       # Small / Medium / Large
            "scale_to_zero_enabled": True,
        }]
    },
)
```

Or navigate to **Serving** in the sidebar → **Create serving endpoint** → select the registered model.

**Stage 3 --- Query the Endpoint**

```python
import mlflow.deployments
client = mlflow.deployments.get_deploy_client("databricks")
response = client.predict(endpoint="ultravox-endpoint", inputs={"your_input_key": "value"})
```

**Key tips for this specific model:**

-   **GPU compute** --- This LLM requires GPU-backed serving (choose an appropriate workload size).
-   **Custom PyFunc is recommended** --- Ultravox uses custom architectures (trust\_remote\_code=True) and multimodal inputs, which don't map cleanly to standard transformers pipeline tasks. Wrapping it in mlflow.pyfunc.PythonModel gives you full control over preprocessing and inference logic.
-   **Storage efficiency** --- If you don't modify weights, consider downloading the model once to a Unity Catalog Volume or DBFS path, and reference it via artifacts.
-   **Validate before deploying** --- Use mlflow.models.predict() locally to confirm the model loads and infers correctly before creating the endpoint.

Would you like me to create a notebook with a working end-to-end implementation for this model?

> Create an Ultravox deployment notebook

Now let me navigate to the notebook and populate it with the full deployment code.

I've created `Deploy Ultravox Model to Serving Endpoint` and navigated you there. The notebook agent will now populate it with the full end-to-end implementation covering:

1.  **Configuration** --- model name, catalog/schema, endpoint name
2.  **Dependency installation** --- transformers, torch, accelerate, mlflow
3.  **Model download** --- from HuggingFace with `trust_remote_code=True`
4.  **Custom PyFunc wrapper** --- handles Ultravox's multimodal architecture
5.  **Unity Catalog registration** --- log and register via MLflow
6.  **Serving endpoint creation** --- GPU-backed, with scale-to-zero
7.  **Endpoint readiness polling** and **sample query**

You'll need to fill in your Unity Catalog `CATALOG` and `SCHEMA` values before running.

- Here are the Python Notebook created by Databricks Genie Code
  - [Deploy_Ultravox_Model_to_Serving_Endpoint.ipynb](./Deploy_Ultravox_Model_to_Serving_Endpoint.ipynb)

## 2026-03-23

Genie Code is an AI assistant for Databricks that helps generate, optimize and debug code, while VS Code can be integrated with Databricks for local development, debugging, and workflow management.

### Genie Code Overview

**Genie Code** is a context-aware AI assistant within Databricks that helps with coding, SQL queries, jobs, dashboards, and file editing. It can:

- Generate, explain, and fix code.
- Optimize queries and workflows.
- Operate autonomously in **Agent mode** for complex multi-step tasks like building pipelines or monitoring production systems.
- Access metadata, data lineage, and governance policies via **Unity Catalog**, providing context-aware recommendations.
  Users interact with Genie Code through a **pane in Databricks**, where they can type questions or commands, accept or reject code suggestions, and configure custom instructions.

### Using VS Code with Databricks

The **Databricks extension for VS Code** allows developers to work locally while connecting to Databricks clusters. Key features include:

- Running local Python files and notebooks on Databricks clusters.
- Debugging notebooks cell by cell using **Databricks Connect**.
- Synchronizing local code with Databricks workspace.
- Defining, deploying, and running **Databricks Asset Bundles** for CI/CD workflows.
- Managing Delta Live Tables pipelines and MLOps stacks.

### Setup Steps

1. Install **VS Code** and the **Databricks extension** from the Visual Studio Marketplace.
2. Configure **Databricks CLI** and authenticate with your workspace.
3. Set up **Databricks Connect** to run and debug code locally while executing on remote clusters.
4. Sync notebooks and Python files between VS Code and Databricks workspace.
5. Optionally, enable telemetry to monitor extension performance, which can be disabled in settings.

### Workflow Benefits

- Local development: Edit and test code in VS Code before deploying to Databricks.
- Enhanced debugging: Step through notebooks and Python scripts with Databricks Connect.
- AI-assisted coding: Genie Code can suggest improvements, fix errors, and automate repetitive tasks.
- Seamless CI/CD: Integrate Databricks jobs and pipelines into version-controlled workflows.

By combining Genie Code and VS Code, developers can leverage AI-powered assistance while maintaining a robust local development environment, improving productivity and code quality in Databricks projects. 

### Databricks presents Genie Code: An AI agent to take over work for data teams
> ### Databricks 呈現 Genie Code：一位接手資料團隊工作的 AI 代理

- https://www.heise.de/en/news/Databricks-presents-Genie-Code-An-AI-agent-to-take-over-work-for-data-teams-11210264.html
- 13.03.2026 11:49 Uhr Matthias Parbel

**The AI agent Genie Code is intended to autonomously handle complex tasks in data engineering and analytics -- from pipeline creation to production monitoring.**

Databricks has introduced Genie Code, an AI agent that is set to fundamentally change the work of data teams. Instead of merely assisting developers in writing code, the agent is said to independently take on complex tasks: building data pipelines, troubleshooting production systems, creating dashboards, and maintaining ongoing systems. According to Ali Ghodsi, co-founder and CEO of Databricks, Genie Code points the way towards "agent-based data work."

> Databricks 推出了 Genie Code，一個將從根本上改變資料團隊工作方式的 AI 代理程式。代理不僅協助開發者撰寫程式碼，還能獨立承擔複雜任務：建立資料管線、排除生產系統故障、建立儀表板及維護持續進行中的系統。根據 Databricks 共同創辦人兼執行長 Ali Ghodsi 的說法，Genie Code 為「基於代理的資料工作」指明了方向。

#### What Genie Code is supposed to achieve
> #### Genie Code 應該達成的目標

According to the [**announcement in the Databricks blog [3]**](https://www.databricks.com/blog/introducing-genie-code), Genie Code complements the existing Genie product family, which already allows users to access their company data via a chat interface. Compared to conventional coding agents, Genie Code is said to distinguish itself primarily through its deep integration into the company's own data infrastructure. Via Databricks' Unity Catalog, the agent accesses metadata, data lineage, usage patterns, and governance policies. Conventional coding agents often fail with data tasks because they lack precisely this context, according to Databricks.

> 根據 [**Databricks 部落格的公告 [3]**](https://www.databricks.com/blog/introducing-genie-code) ，Genie Code 補充了現有的 Genie 產品家族，後者已允許用戶透過聊天介面存取公司資料。與傳統編碼代理相比，Genie Code 主要因其深度整合於公司自有資料基礎設施而顯得獨特。透過 Databricks 的 Unity 目錄，代理可存取元資料、資料沿革、使用模式及治理政策。根據 Databricks，傳統編碼代理常因缺乏這種脈絡而在資料任務中失敗。

Genie Code is not a single language model, but an agent-based system that distributes tasks across multiple models and tools. Depending on the requirement, the system is said to automatically select the appropriate model -- whether a proprietary Frontier model, an open-source model, or a custom model hosted on Databricks.

> Genie Code 並非單一語言模型，而是一個基於代理的系統，將任務分配到多個模型與工具之間。根據需求，系統會自動選擇合適的模型無論是專有的 Frontier 模型、開源模型，或是託管在 Databricks 上的自訂模型。

The functions extend across the entire data and ML lifecycle: the agent is intended to be able to handle complete machine learning workflows -- from feature engineering, training, and comparison of multiple model types to deployment on Databricks Model Serving. Experiments are logged in MLflow. In the area of data engineering, Genie Code creates production-ready Spark pipelines according to the manufacturer, considers differences between staging and production environments, and automatically applies data quality checks. Furthermore, the agent is intended to generate dashboards with reusable semantic definitions and autonomously plan and execute multi-stage tasks.

> 這些功能涵蓋整個資料與機器學習生命週期：代理程式旨在處理完整的機器學習工作流程--從特徵工程、訓練、多模型類型的比較，到在 Databricks 的模型服務部署。實驗會記錄在 MLflow 中。在資料工程領域，Genie Code 會根據製造商設定，建立可生產環境的 Spark 管線，考量分階段與生產環境的差異，並自動套用資料品質檢查。此外，代理程式旨在產生具可重複使用語意定義的儀表板，並自主規劃與執行多階段任務。

![Dashboard created by Genie Code with graphics](https://heise.cloudimg.io/v7/_www-heise-de_/imgs/18/5/0/4/4/9/6/8/Databricks_Genie-Code_Dashboard-b7c0b1ca0ebac29f.jpg?force_format=avif%2Cwebp%2Cjpeg&org_if_sml=1&q=70&width=1000)

Genie Code is intended to create visualizations, configure filters, and organize dashboard layouts -- with reusable semantic definitions.

> Genie Code 旨在建立視覺化、設定篩選器及組織儀表板佈局 —  並具備可重複使用的語意定義。

(Image: Databricks)   （圖片來源：Databricks）

Another aspect is proactive monitoring: Genie Code is intended to monitor Lakeflow pipelines and AI models in the background, triage errors, and investigate anomalies before a human needs to intervene. However, so-called "Background Agents" that permanently handle this monitoring in the background are not yet available, according to Databricks -- but are expected to be rolled out soon.

> 另一個面向是主動監控：Genie Code 旨在背景監控 Lakeflow 管線與 AI 模型，分流錯誤，並在人類介入前調查異常。然而，根據 Databricks 的說法，所謂的「背景代理」尚未正式推出，這些代理程式能在背景中永久處理監控，但預計很快會推出。

The agent has persistent storage that automatically updates internal instructions based on past interactions and coding preferences. This is intended to make it "better" over time.

> 代理擁有持久儲存，能根據過去的互動與編碼偏好自動更新內部指令。這是為了讓它隨著時間變得「更好」。

#### Acquisition of Quotient AI
> #### 收購 Quotient AI

Parallel to the introduction of Genie Code, Databricks announced the [**acquisition of Quotient AI [4]**](https://www.databricks.com/blog/databricks-acquires-quotient-ai-power-ai-agent-evaluations). The company specializes in the evaluation and reinforcement learning for AI agents and was previously involved in improving the quality of GitHub Copilot. Through the integration, continuous performance monitoring is to be embedded directly into Genie Code: According to Databricks, Quotient measures response quality, detects regressions early, and identifies errors -- and feeds these findings into an improvement process.

> 與 Genie Code 的推出同時，Databricks 宣布[**收購 Quotient AI [4]**](https://www.databricks.com/blog/databricks-acquires-quotient-ai-power-ai-agent-evaluations)。 該公司專注於 AI 代理的評估與強化學習，過去曾參與提升 GitHub Copilot 的品質。透過整合，持續績效監控將直接嵌入 Genie Code：根據 Databricks，Quotient 衡量回應品質、及早偵測迴歸問題並識別錯誤，並將這些發現納入改進流程。

#### Availability and Extensibility
> #### 可用性與可擴充性

[**According to Databricks, Genie Code is generally available immediately [5]**](https://www.databricks.com/blog/introducing-genie-code) and directly integrated into Databricks workspaces -- in notebooks, the SQL editor, and the Lakeflow Pipelines editor. An elaborate configuration is not required.

> [**根據 Databricks，Genie Code 通常可立即取得 [5]**](https://www.databricks.com/blog/introducing-genie-code)，並直接整合於 Databricks 工作空間中 —  包括筆記本、SQL 編輯器及 Lakeflow Pipelines 編輯器。不需要複雜的配置。

The agent can be extended in three ways: Via the Model Context Protocol (MCP), Genie Code can interact with external tools such as Jira, Confluence, or GitHub. So-called Agent Skills allow domain-specific capabilities to be defined, for example, for handling personal data or company-specific validation frameworks. And via persistent storage, the agent learns from past interactions and adapts to the workflow of the respective team.

> 代理可以透過三種方式擴充：透過模型上下文協定（MCP），Genie Code 能與外部工具如 Jira、Confluence 或 GitHub 互動。所謂的代理技能允許定義領域專屬能力，例如處理個人資料或公司特定的驗證框架。透過持久儲存，代理從過去的互動中學習並適應團隊的工作流程。

Databricks' new functions align with an industry-wide trend. Almost all major providers are now relying on agent-based AI systems that are intended to solve complex tasks autonomously. However, the extent of their actual capabilities is controversial -- especially [**with regard to non-functional requirements [6]**](https://www.heise.de/hintergrund/Zwischen-Tempo-und-Tragfaehigkeit-KI-Agenten-in-der-Softwareentwicklung-11092303.html?from-en=1).

> Databricks 的新功能符合整個產業的趨勢。幾乎所有主要供應商現在都依賴基於代理的 AI 系統，這些系統旨在自主解決複雜任務。然而，其實際能力的範圍仍有爭議 —  尤其是在非 [**功能性需求方面 [6]**](https://www.heise.de/hintergrund/Zwischen-Tempo-und-Tragfaehigkeit-KI-Agenten-in-der-Softwareentwicklung-11092303.html?from-en=1)。

*This article was originally published in [**German [11]**](https://www.heise.de/news/Databricks-legt-Genie-Code-vor-Ein-KI-Agent-soll-Datenteams-die-Arbeit-abnehmen-11209152.html). It was translated with technical assistance and editorially reviewed before publication.

> 本文最初發表於 [**德文 [11]。**](https://www.heise.de/news/Databricks-legt-Genie-Code-vor-Ein-KI-Agent-soll-Datenteams-die-Arbeit-abnehmen-11209152.html) 在技術協助下翻譯並經過編輯審查後才出版。*

* * * *

**URL dieses Artikels:  URL dieses Artikels：**

- https://www.heise.de/-11210264

**Links in diesem Artikel:  本文連結：**
- [1] https://www.data2day.de/?wt_mc=intern.academy.dpunkt.konf_dpunkt_vo_data2day.empfehlung-ho.link.link&LPID=34380
- [2] https://www.data2day.de/cfp.php?wt_mc=intern.academy.dpunkt.konf_dpunkt_vo_data2day.empfehlung-ho.link.link&LPID=34380
- [3] https://www.databricks.com/blog/introducing-genie-code
- [4] https://www.databricks.com/blog/databricks-acquires-quotient-ai-power-ai-agent-evaluations
- [5] https://www.databricks.com/blog/introducing-genie-code
- [6] https://www.heise.de/hintergrund/Zwischen-Tempo-und-Tragfaehigkeit-KI-Agenten-in-der-Softwareentwicklung-11092303.html?from-en=1
- [7] mailto:map@ix.de
- [8] https://www.facebook.com/heiseonlineEnglish
- [9] https://www.linkedin.com/company/104691972
- [10] https://social.heise.de/@heiseonlineenglish
- [11] https://www.heise.de/news/Databricks-legt-Genie-Code-vor-Ein-KI-Agent-soll-Datenteams-die-Arbeit-abnehmen-11209152.html

## 2026-03-24


**Q:** <p style="background-color:lightyellow;">
could you give me a step-by-step instruction to setup Databricks Genie Code and integrate into Visual Studio Code?
</p>

**A:** (Databricks Genie Code on AWS)

Important clarification: **Genie Code** and the **Databricks extension for VS Code** are two separate tools --- <mark>Genie Code is a built-in AI assistant within the Databricks workspace UI (notebooks, SQL editor, dashboards, etc.) and is **not available directly inside VS Code**.</mark> Here's how to set up each:

**Setting up Genie Code (Databricks workspace)**

1.  Ensure **Partner-powered AI features** are enabled at both the account and workspace level (requires an account admin).
2.  Open any Databricks notebook, SQL editor, or dashboard in your workspace.
3.  Click the **Genie Code icon** in the upper-right corner of the workspace to open the chat pane --- it's ready to use.
4.  Optionally, a workspace admin can add custom instructions by creating a file named `.assistant_workspace_instructions.md` in the `Workspace/` directory.

**Setting up the Databricks Extension for VS Code**

1.  **Prerequisites**: VS Code ≥ 1.86.0, a Python interpreter configured, and at least one Databricks workspace with a cluster.
2.  Open **Extensions** (View → Extensions), search for **"Databricks"**, and install the Databricks-verified extension.
3.  Restart VS Code, then click the **Databricks icon** on the sidebar.
4.  Configure a project by connecting to your Databricks workspace (you'll authenticate and select a cluster).
5.  Optionally install **Databricks Connect** for interactive debugging and autocompletion via the extension's Configuration view.

For full details, see the [install guide](https://docs.databricks.com/aws/en/dev-tools/vscode-ext/install/) and the [Genie Code docs](https://docs.databricks.com/aws/en/genie-code/use-genie-code/).

**Q:** 

<p style="background-color:lightyellow;">
Are there Databricks CLI? Can I use CLI to interact with Genie Code?
</p>

**A:** (Databricks Genie Code on AWS)

Yes, there is a **Databricks CLI**, but it **cannot interact with Genie Code** directly. Here's the breakdown:

**Databricks CLI** --- available and well-supported for many Databricks operations. Install it via:

- **macOS/Linux**: 
  ```bash
  brew tap databricks/tap && brew install databricks
  ```
- **Windows**: 
  ```cmd
  winget install Databricks.DatabricksCLI
  ```
- **Any OS**: 
  ```bash
  curl -fsSL https://raw.githubusercontent.com/databricks/setup-cli/main/install.sh | sh
  ```

Verify with `databricks -v` (should be ≥ 0.205.0), then authenticate with databricks configure.

**CLI genie commands exist**, but they are for **Genie spaces** (the AI/BI no-code data room experience), not for Genie Code. The CLI genie subcommands include start-conversation, create-message, get-message, etc. --- all scoped to Genie spaces.

**Genie Code** (the AI coding assistant) is only accessible through the **Databricks workspace UI** --- in notebooks, SQL editor, dashboards, file editor, and jobs. There is no CLI or API to interact with Genie Code programmatically at this time.

In summary: the Databricks CLI is a powerful tool for managing workspace resources, clusters, jobs, pipelines, and more --- but for Genie Code assistance, you'll need to use the Databricks web interface. See the [CLI install guide](https://docs.databricks.com/aws/en/dev-tools/cli/install/) and [CLI commands reference](https://docs.databricks.com/aws/en/dev-tools/cli/commands/) for full details.

[Install the Databricks CLI](https://docs.databricks.com/aws/en/dev-tools/cli/install/)

### Claude Code + Databricks Models

**Q:** 

<p style="background-color:lightyellow;">
could you give me step-by-step instructions to setup Claude Code with Claude model fromDatabricks Service Endpoints?
</p>

**A:** (Databricks Genie Code on AWS)

Here's a step-by-step guide to set up **Claude Code** (Anthropic's CLI coding agent) with **Claude models served from Databricks Foundation Model APIs**.

**Prerequisites**

1.  A Databricks workspace with Foundation Model APIs enabled
2.  A Databricks **Personal Access Token** (PAT) --- generate one from `Settings` → `Developer` → `Access Tokens`
3.  Node.js installed on your local machine
4.  Your Databricks workspace hostname (e.g., `<workspace>.cloud.databricks.com`)

**Step 1 --- Install Claude Code**

```bash
npm install -g @anthropic-ai/claude-code
```

**Step 2 --- Configure environment variables**

Databricks exposes a native **Anthropic Messages API** endpoint at: `https://<workspace\_host>.databricks.com/serving-endpoints/anthropic`

Set the following environment variables:

```bash
export ANTHROPIC_BASE_URL=https://<workspace_host>.databricks.com/serving-endpoints/anthropic
export ANTHROPIC_API_KEY=<your-databricks-pat>
```

**Step 3 --- Launch Claude Code with a Databricks-hosted model**

```bash
claude --model databricks-claude-sonnet-4-5
```

Available Databricks-hosted Claude models include:

| Endpoint Name | Description |
|----|-----|
| databricks-claude-opus-4-6 | Most capable, hybrid reasoning |
| databricks-claude-sonnet-4-6 | Advanced hybrid reasoning, balanced |
| databricks-claude-sonnet-4-5 | Strong general purpose |
| databricks-claude-haiku-4-5 | Fast and lightweight |
| databricks-claude-opus-4-5 | Previous gen flagship |

**Important caveat:** Databricks authenticates via `Authorization: Bearer <token>` header, while the Anthropic SDK by default sends credentials via the `x-api-key` header. If authentication fails, you may need to configure Claude Code to pass custom headers. In the Anthropic Python SDK, this is done via `default_headers={"Authorization": f"Bearer {DATABRICKS_TOKEN}"}` with `api_key="unused"`. Check Claude Code's documentation for equivalent header customization options (e.g., a .claude config file or additional environment variables).

**Step 4 (Optional) --- Connect Databricks MCP server for workspace access**

You can also give Claude Code access to your Databricks workspace tools via MCP:

```bash
claude mcp add-json databricks-mcp-server \
  '{"type":"http","url":"https://<workspace_host>/api/2.0/mcp/functions/{catalog_name}/{schema_name}","oauth":{"clientId":"<client-id>","callbackPort":8080}}' \
  --client-secret <client-secret>
```

This enables Claude Code to call Unity Catalog functions directly. See the [Databricks MCP docs](https://docs.databricks.com/aws/en/generative-ai/mcp/connect-external-services/) and the [Anthropic Messages API on Databricks](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-anthropic-messages/) for full details.