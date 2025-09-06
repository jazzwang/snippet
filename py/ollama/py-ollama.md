# Ollama Python Library

- Git Repo
  - https://github.com/ollama/ollama-python
- PyPI
  - https://pypi.org/project/ollama/

## 2025-09-06

- 這個 Python 的 Ollama 函式庫定位是 Ollama Client，也就是拿來讓 Python 程式與本地 Golang 寫的 Ollama Server 互動使用。
- 從 [README](https://github.com/ollama/ollama-python/blob/main/README.md) 的說明看起來，除了基本的指令操作，像是 list, show 等指令有對應的函數。也可以用這個函式庫跟指定的 Ollama 模型的 API 做互動。支援 Streaming Mode 跟 Async Client，還有一個用 httpx.Client 的 Custom Client 暫時看不懂。