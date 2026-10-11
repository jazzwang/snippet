# tiktoken

- PyPI
  - http://pypi.org/project/tiktoken
- Git Repo
  - https://github.com/openai/tiktoken

## 2025-10-27

- 緣起：
  - 使用不同 LLM 模型時，context window (max token) 會影響輸出結果。所以想知道如何估算 token 個數。
- 搜尋：
  - 問 Gemini 2.5 Flash
> [!NOTE]
> are there python program or library that can count how many tokens does a plain text file have?

Yes, there are several Python programs and libraries that can count tokens in a plain text file, but the correct approach depends on **how you define a "token"**.

Since token counting is crucial for Large Language Models (LLMs), I'll cover both general-purpose tokenization and LLM-specific tokenization.

-----

## 1\. LLM-Specific Token Counting

If you're interested in the token count for use with an **LLM API** (like Gemini, GPT, or Llama), you need to use the **specific tokenizer** associated with that model, as tokens are often **sub-word units** (Byte Pair Encoding or BPE).

### A. For Gemini Models (Google)

You can use the official Google GenAI SDK's `count_tokens` method.

**Library:** `google-genai`

```python
from google import genai
import os

# 1. Initialize the client (Make sure to set your API key as an environment variable)
client = genai.Client()

def count_tokens_gemini(file_path, model_name="gemini-2.5-flash"):
    """Counts tokens in a file using the Gemini tokenizer."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        response = client.count_tokens(
            model=model_name,
            contents=[text]
        )
        return response.total_tokens
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example Usage:
# Assuming you have a file named 'my_text_file.txt'
# token_count = count_tokens_gemini('my_text_file.txt')
# print(f"Token count for Gemini: {token_count}")
```

### B. For OpenAI Models (GPT)

The official library for counting tokens for OpenAI's models (like GPT-4 and GPT-3.5) is **`tiktoken`**.

**Library:** `tiktoken`

```python
import tiktoken

def count_tokens_openai(file_path, model_name="gpt-4"):
    """Counts tokens in a file using the tiktoken library."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        # Get the appropriate encoding for the model
        encoding = tiktoken.encoding_for_model(model_name)

        # Encode the text and count the number of resulting tokens
        tokens = encoding.encode(text)
        return len(tokens)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example Usage:
# token_count = count_tokens_openai('my_text_file.txt')
# print(f"Token count for GPT-4: {token_count}")
```

-----

## 2\. General-Purpose Token Counting (NLP/Words)

If you define a "token" as a **word, punctuation mark, or similar unit** for general Natural Language Processing (NLP), you can use libraries like **NLTK** or **spaCy**.

### Using NLTK (Natural Language Toolkit) 📚

**Library:** `nltk`

```python
import nltk
from nltk.tokenize import word_tokenize

# nltk.download('punkt') # Run this once to download the required resource

def count_tokens_nltk(file_path):
    """Counts tokens (words and punctuation) using NLTK."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        # Tokenize the text into words and punctuation
        tokens = word_tokenize(text)
        return len(tokens)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None

# Example Usage:
# token_count = count_tokens_nltk('my_text_file.txt')
# print(f"NLTK token count: {token_count}")
```

### Simple Word Count (Quick & Dirty)

For a very simple approach where a "token" is defined as any sequence of non-whitespace characters (like using the Unix `wc -w` command), you can use basic Python:

```python
def count_words_simple(file_path):
    """Counts 'words' by splitting on whitespace."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        # Split by any whitespace and filter out empty strings
        words = text.split()
        return len(words)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None

# Example Usage:
# word_count = count_words_simple('my_text_file.txt')
# print(f"Simple word count: {word_count}")
```
---
- 初步從結果可以知道不同的 LLM 模型，可能因為 encoding 的方法不同，所以對於 token 的認定也不同，所以給出三種不同的實作（第四種用空白切 token 的方法不試用中日文語系）
  - Gemini - 用 `google-genai` 函式庫
  - OpenAI - 用 `tiktoken` 函式庫
  - 廣義 - 用 `nltk` 函式庫
- 以下實測 `tiktoken` 的實作
