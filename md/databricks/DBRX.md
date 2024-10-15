# DBRX

- [DBRX: A New Standard for Open Source LLMs](https://www.databricks.com/resources/demos/videos/dbrx-new-standard-open-source-llms)
- [Announcing DBRX: A new standard for efficient open source LLMs](https://www.databricks.com/blog/announcing-dbrx-new-standard-efficient-open-source-customizable-llms)
- 2024-03-27: [Introducing DBRX: A New State-of-the-Art Open LLM](https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm)
- 2024-0[DBRX 101: Overview of Databricks 132B Parameter Open LLM (2024)](https://www.chaosgenius.io/blog/dbrx/)
- https://ollama.com/library/dbrx - Ollama 有 DRBX 的模型，大小是 48 GB ~ 263 GB。這個模型不僅吃硬碟空間，也吃 GPU 記憶體。看起來定位是商用的開源大語言模型。

## Hardware Requirement

> Before accessing DBRX, ensure your system has at least **320GB** of memory.

- 2024-05-09: [Databricks DBRX Tutorial: A Step-by-Step Guide](https://www.datacamp.com/tutorial/databricks-dbrx-tutorial-a-step-by-step-guide)

## Databricks Model Serving

- 要跑 DBRX 的硬體要求太高，所以若要實驗的話，最好先從 Databricks Model Serving 著手。底下這篇文章，採用 LiteLLM (LLM Proxy) 來呼叫 Databricks 提供的 DBRX
- https://community.databricks.com/t5/technical-blog/simplifying-multi-model-llm-development-a-developer-s-guide-to/ba-p/80623