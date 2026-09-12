# Opik

> Open source LLM evaluation framework

- Website:
  - https://www.comet.com/site/products/opik/
- Document:
  - https://www.comet.com/docs/opik/
- Git Repo:
  - https://github.com/comet-ml/opik

> From RAG chatbots to code assistants to complex agentic pipelines and beyond, build LLM systems that run better, faster, and cheaper with tracing, evaluations, and dashboards.

## 2025-01-20

- 在 DevOps 文化中，`Observibility` 很重要，Opik 可以用 `Trace` 來提供可觀測性。
- Evaluation - opik 提供了 `Dataset` 跟 `Experiment` 來衡量 LLM Application，甚至可以靠 LLM 當裁判來計算「幻覺」的分數。
- 初步覺得這是 production 環節中重要的一個工具

## 2025-01-21

- Logging traces with Opik (from LlamaIndex)
  - https://docs.llamaindex.ai/en/stable/examples/observability/OpikCallback/
- 2024-10-09: Evaluating and Monitoring LLM & RAG Applications with Opik
  - https://www.analyticsvidhya.com/blog/2024/10/opik/
- Comet Opik - Logging + Evals (from LiteLLM)
  - https://docs.litellm.ai/docs/observability/opik_integration
- Trace and evaluate your Haystack pipelines with Opik
  - https://haystack.deepset.ai/integrations/opik

## 2026-09-12

## Opik 平台：開源 LLM 觀測與評估工具

### 一鍵了解

Opik 是由 Comet 開發的開源工具，主要用於 LLM 觀測、評估和 AI Agent 的追蹤。它支援從開發到上線的全流程，包含 AI Agent tracing、LLM 評估、提示詞與 Agent 優化、生產環境監控，還有 Guardrails 防護。

- 採用 Apache-2.0 license
- 可自訂部署
- GitHub 上有 20,000+ stars

### 主要功能

#### AI Agent 追蹤與觀測

- **追蹤詳細記錄**：記錄 LLM 呼叫、對話歷史和 Agent 的活動，支援多步驟 Agent 和 tool call 的完整追蹤樹
- **第三方整合**：整合了 Google ADK、Autogen、Flowise AI 等框架，詳情看 [Integrations](https://www.comet.com/docs/opik/integrations/overview/)
- **標註與評分**：用 Python SDK 或 UI 直接為 trace/spans 加 feedback score
- **Prompt Playground**：在介面中測試不同的提示詞和模型

#### 評估與測試

- **資料集與實驗**：用 Dataset 管理評估資料，用 Experiment 呼叫 LLM 應用並收集結果
- **LLM-as-a-Judge**：能偵測 hallucination、內容過濾、RAG 評估（例如答案相關性、上下文精準度）
- **CI/CD 整合**：提供 PyTest 整合，每次 commit 時自動測試 LLM pipeline

#### 生產環境監控

- **大規模追蹤**：設計能處理每日 40M+ traces
- **線上監控**：用 LLM-as-a-Judge 監控 production 環境問題（feedback score、追蹤數量、token 用量等）
- **Opik Agent Optimizer**：持續優化提示詞和 Agent
- **Opik Guardrails**：協助實作安全的 AI 實務

#### 適用對象

- 用 LLM 驅動 Agent 的 ML engineers
- 需要評估和監控的 AI 團隊


### 快速開始

1. **直接使用**：透過 Comet 服務啟用 Opik，或自行部署 Opik Server
2. **安裝 Python SDK**：
   ```bash
   pip install opik
   ```
3. **初始化專案**：
   ```python
   from opik import Opik
   client = Opik()
   client.start_trace(...)
   ```
4. **查看 UI**：開啟 http://localhost:5173（自訂部署）或 Comet 雲端介面


### 自訂部署

```bash
git clone https://github.com/comet-ml/opik
cd opik
./opik.sh
```

啟動後，Web UI 在 `http://localhost:5173`。更多安裝說明看官方文件。


### Python SDK

- **Logging traces with integrations**：支援多個 LLM 框架（OpenAI、Anthropic、Cohere、LLamaIndex、LangChain 等），詳情見 [Integrations](https://www.comet.com/docs/opik/integrations/overview/)
- **標註 traces**：
  ```python
  import opik
  client = opik.init()
  with client.start_trace() as trace:
      response = llm.invoke("...")
      client.annotate_trace(trace.id, score=0.9, comment="good answer")
  ```
- **評估**：
  ```python
  from opik import evals
  result = evals.evaluate(...)
  ```

### LLM-as-a-Judge

- **Hallucination detection**：檢查生成的文字是否與上下文矛盾
- **內容過濾**：檢查是否有違規內容
- **RAG 指標**：answer relevance、context precision、context recall

*根據 https://github.com/comet-ml/opik 的 README 和文件整理，最後更新 2026-07-17。*
