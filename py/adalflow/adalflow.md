# AdalFlow

> The PyTorch-like Library to Build and Auto-Optimize LLM Applications

## 🔗 Project Links

- **PyPI** 
  - https://pypi.org/project/adalflow/
- **Git Repository** 
  - https://github.com/SylphAI-Inc/AdalFlow
- **Website**
  - https://adalflow.sylph.ai/
- **Documentation**
  - https://adalflow.sylph.ai/

## 🚀 Quick Start Example

This example demonstrates how to install AdalFlow and run a basic query using the `Generator` component with an OpenAI model.

### 1. Installation

Install the core package. You may also need to install the package for your specific LLM provider (e.g., `openai`).

```bash
pip install adalflow
# For this example, you will also need the openai library
pip install openai
````

### 2\. Run Your First Query

You must set up your LLM API key as an environment variable (e.g., `OPENAI_API_KEY`) for this example to work. AdalFlow's `setup_env()` utility will load it from your environment.

```python
import adalflow as adal
from adalflow.utils import setup_env
from typing import Dict

# 1. Set up your environment variables (loads from .env or system)
setup_env() 

# 2. Define the LLM Generator component
# Generator is the core orchestrator for LLM prediction.
openai_llm = adal.Generator(
    model_client=adal.OpenAIClient(),
    # Pass model configuration
    model_kwargs={"model": "gpt-3.5-turbo"} 
)

# 3. Define the input prompt
input_prompt = {"input_str": "Explain the concept of 'zero-shot optimization' in LLM frameworks in one sentence."}

# 4. Call the generator
# The output will be a GeneratorOutput object
response = openai_llm(prompt_kwargs=input_prompt)

# 5. Print the LLM's answer
print(response.answer)

# Example Output (varies based on LLM):
# Zero-shot optimization in LLM frameworks is the process of automatically refining the prompt
# (e.g., instructions or parameters) without relying on any specific training data or examples.
```

## 2025-10-20

- 從 [deepwiki-open](https://github.com/AsyncFuncAI/deepwiki-open) 學到的
- 作者應該是博士班中輟，加入 Meta ，然後出來開公司的 [Li Yin](https://github.com/liyin2015)
  - 她寫了一本書 open-source book [Hands-on Algorithmic Problem Solving](https://github.com/liyin2015/Hands-on-Algorithmic-Problem-Solving) 還教人家怎麼做 [Python Coding Interview](https://github.com/liyin2015/python-coding-interview).
    - 提到 https://interviewing.io/ 可以線上約人幫忙面試
  - fork 了 https://github.com/DataExpert-io/data-engineer-handbook （剛好就是我有追蹤的一個資料工程社群）
  - 另一個早期的作品是 https://github.com/SylphAI-Inc/GithubChat
    - A practical RAG where you can download and chat with github repo
    - 我覺得這個應該是 DeepWiki-Open 的前身，因為核心還是 git repo 怎麼生成 index (embedding) 供 RAG 使用。
- Adalflow [致謝](https://github.com/SylphAI-Inc/AdalFlow?tab=readme-ov-file#acknowledgements)裡提到 DSPy 啟發了 few-shot optimizer
  > 📚 DSPy for inspiring the __{input/output}__fields in our DataClass and the bootstrap few-shot optimizer.
