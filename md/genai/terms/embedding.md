# Embedding

## 2025-04-11

### Embedding Models

- 在看 [llama-index](https://docs.llamaindex.ai) 的[文件](https://docs.llamaindex.ai/en/latest/examples/embeddings/huggingface/#huggingfaceembedding)時，看到這一段：
> The base `HuggingFaceEmbedding` class is a generic wrapper around any HuggingFace model for embeddings. All [embedding models](https://huggingface.co/models?library=sentence-transformers) on Hugging Face should work. You can refer to the [embeddings leaderboard](https://huggingface.co/spaces/mteb/leaderboard) for more recommendations.
  - 這陣子在做一些 GenAI Use Case 的時候，特別是 text-to-text 的案例，突然覺得 embedding 的品質會決定 RAG 的回答品質。
  - https://huggingface.co/models?library=sentence-transformers&sort=downloads
    - 2025-04-11 HuggingFace Embedding Model 下載量前十大依序為：
      - https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
      - https://huggingface.co/sentence-transformers/all-mpnet-base-v2
      - https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
      - https://huggingface.co/sentence-transformers/multi-qa-MiniLM-L6-cos-v1
      - https://huggingface.co/cross-encoder/ms-marco-MiniLM-L6-v2
      - https://huggingface.co/sentence-transformers/paraphrase-MiniLM-L6-v2
      - https://huggingface.co/intfloat/multilingual-e5-small
      - https://huggingface.co/sentence-transformers/all-MiniLM-L12-v2
      - https://huggingface.co/BAAI/bge-m3
      - https://huggingface.co/BAAI/bge-small-en-v1.5
    - 感想：也難怪 Gemini 回答我怎麼分析 WebVTT 時，會選擇用 [sentence-transformers](https://pypi.org/project/sentence-transformers/)

### Embedding Leaderboard

- https://huggingface.co/spaces/mteb/leaderboard
  - 第一名是 Google Gemini 商用模型 - [gemini-embedding-exp-03-07](https://developers.googleblog.com/en/gemini-embedding-text-model-now-available-gemini-api/)
  - 第二名是 整合 E5 跟 Mistral 開源模型 - [Linq-Embed-Mistral](https://huggingface.co/Linq-AI-Research/Linq-Embed-Mistral)
  - 第三名是 Qwen 開源模型 - [gte-Qwen2-7B-instruct](https://huggingface.co/Alibaba-NLP/gte-Qwen2-7B-instruct)
  - 第四名是 Microsoft E5 開源模型 - [gte-Qwen2-7B-instruct](https://huggingface.co/Alibaba-NLP/gte-Qwen2-7B-instruct)
  - 第五名是 混合了 E5 跟 Mistral 開源模型 [SFR-Embedding-Mistral](https://huggingface.co/Salesforce/SFR-Embedding-Mistral)