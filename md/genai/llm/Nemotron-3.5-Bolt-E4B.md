# NVIDIA Nemotron-3.5-Bolt-E4B-4GB 技術報告

> **最後更新：** 2026 年 10 月 23 日  
> **來源：** [Hugging Face](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB)  
> **許可證：** [OpenMDW-1.1](https://openmdw.ai/license/1-1/)

## 目錄

1. [模型概述](#模型概述)
2. [系統需求](#系統需求)
3. [安裝步驟](#安裝步驟)
4. [測試與驗證](#測試與驗證)
5. [API 使用範例](#api-使用範例)
6. [效能指標](#效能指標)
7. [最佳實踐](#最佳實踐)

## 模型概述

### 基本資訊

| 項目 | 內容 |
|------|------|
| **開發者** | NVIDIA Corporation |
| **模型名稱** | NVIDIA-Nemotron-3.5-Bolt-E4B-4GB |
| **架構基礎** | Gemma-4-E4B-it |
| **參數量** | 8B (4B 有效參數) |
| **精度** | Q4_K_M (量化) / BF16 (完整精度) |
| **上下文長度** | 輸入/輸出各 64K tokens |
| **輸入類型** | Text |
| **輸出類型** | Text |
| **資料更新截止** | 2026 年 5 月 |
| **發布日期** | 2026 年 10 月 23 日 |

### 設計目標

NVIDIA-Nemotron-3.5-Bolt-E4B-4GB 是 NVIDIA 基於 Gemma-4-E4B-it 進一步後訓練的小型語言模型 (SLM)，專注於：

- ✅ 快速本地語音與裝置助理 (local voice and device assistants)
- ✅ 互動式角色 (interactive personas)
- ✅ 嵌入與邊緣介面 (embedded/edge interfaces)
- ✅ 多輪工具使用 (multi-turn tool use)
- ✅ 指令遵循能力 (instruction following)
- ✅ 輸入接地 (input grounding)

設計用於低記憶體、低首字延遲 (low-TTFT) 運算環境，允許代理快速回應同時保留給應用程式或相鄰模型流程的資源。

## 系統需求

### 硬體需求

| 硬體 | 需求 |
|------|------|
| **GPU 架構** | NVIDIA Ampere (A100) / Hopper (H100-80GB) / Blackwell |
| **記憶體** | 4GB (量化版) / 完整精度依模型大小 |
| **CUDA** | CUDA 13+ (推薦) |
| **作業系統** | Linux |

### 軟體需求

| 軟體 | 版本 |
|------|------|
| **Python** | 3.10+ |
| **PyTorch** | 2.0+ |
| **llama.cpp** | 支援 CUDA 版本 |
| **HF CLI** | huggingface-cli |
| **Docker** | 24.0+ (可選) |

## 安裝步驟

### 前置條件檢查

```bash
# 檢查 CUDA 版本
nvcc --version

# 檢查記憶體
free -h

# 檢查 GPU 可用性
nvidia-smi
```

### 方法一：使用 Docker（推薦）

#### 1. 準備模型檔案

```bash
export MODEL_REPO=nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB
export MODEL_FILE=Nemotron-3.5-Bolt-E4B-Q4_K_M.gguf

export DRAFTER_REPO=nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB-DFlash
export DRAFTER_FILE=Nemotron-3.5-Bolt-E4B-DFlash-BF16.gguf

export MODEL_DIR="$PWD/bolt-models"

# 下載模型主檔案
hf download "$MODEL_REPO" "$MODEL_FILE" \
  --local-dir "$MODEL_DIR"

# 下載 DFlash drafter 模型（用於 speculative decoding）
hf download "$DRAFTER_REPO" "$DRAFTER_FILE" \
  --local-dir "$MODEL_DIR"
```

#### 2. 啟動服務（不使用 DFlash drafter）

```bash
docker run --rm --gpus all \
  -p 8000:8000 \
  -v "$MODEL_DIR:/models:ro" \
  ghcr.io/ggml-org/llama.cpp:server-cuda13-b11459 \
  -m "/models/$MODEL_FILE" \
  --alias nemotron-bolt \
  --host 0.0.0.0 \
  --port 8000 \
  -c 65536 \
  -ngl 999 \
  --jinja
```

#### 3. 啟動服務（使用 DFlash drafter）

```bash
docker run --rm --gpus all \
  -p 8000:8000 \
  -v "$MODEL_DIR:/models:ro" \
  ghcr.io/ggml-org/llama.cpp:server-cuda13-b11459 \
  -m "/models/$MODEL_FILE" \
  --spec-draft-model "/models/$DRAFTER_FILE" \
  --spec-type draft-dflash \
  --spec-draft-n-max 7 \
  --spec-draft-ngl 999 \
  --alias nemotron-bolt \
  --host 0.0.0.0 \
  --port 8000 \
  -c 65536 \
  -ngl 999 \
  --jinja
```

### 方法二：本地安裝（llama.cpp）

#### 1. 克隆並編譯

```bash
git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp

# 編譯 CUDA 版本
make -j$(nproc) LLAMA_CUDA=on -DCUBLAS=on
```

#### 2. 下載模型

```bash
export MODEL_DIR="$PWD/models/bolt"
mkdir -p "$MODEL_DIR"

hf download nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB \
  Nemotron-3.5-Bolt-E4B-Q4_K_M.gguf \
  --local-dir "$MODEL_DIR"
```

#### 3. 啟動服務

```bash
./build/bin/llama-server -m "$MODEL_DIR/Nemotron-3.5-Bolt-E4B-Q4_K_M.gguf" \
  --port 8000 \
  --host 0.0.0.0 \
  -c 65536 \
  -ngl 999 \
  --alias nemotron-bolt \
  --jinja
```

## 測試與驗證

### 方法一：使用 cURL 測試

#### 基本問答測試

```bash
curl --fail-with-body -sS \
  http://localhost:8000/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "nemotron-bolt",
    "messages": [
      {"role": "user", "content": "What is 17 multiplied by 23?"}
    ],
    "temperature": 0.0,
    "max_tokens": 512,
    "chat_template_kwargs": {
      "enable_thinking": true
    }
  }'
```

#### 預期回應格式

```json
{
  "id": "chatcmpl-xxx",
  "object": "chat.completion",
  "created": 1730000000,
  "model": "nemotron-bolt",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Thinking: 17 × 23 = 17 × (20 + 3) = 340 + 51 = 391\n\nAnswer: 17 multiplied by 23 equals 391."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 12,
    "completion_tokens": 25,
    "total_tokens": 37
  }
}
```

### 方法二：使用 Python 測試

#### 1. 安裝依賴

```bash
pip install openai
```

#### 2. 測試程式碼

```python
from openai import OpenAI
import json

client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")
MODEL = "nemotron-bolt"

# 測試基本問答
print("=== 測試 1: 基本數學問題 ===")
response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "What is 17 multiplied by 23?"}],
    max_tokens=512,
    temperature=1.0,
    top_p=0.95,
    extra_body={
        "skip_special_tokens": False,
        "chat_template_kwargs": {"enable_thinking": True},
    }
)
print(response.choices[0].message.content)
print()

# 測試推理關閉模式
print("=== 測試 2: 推理關閉模式 ===")
response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "What is the capital of Japan?"}],
    max_tokens=512,
    temperature=1.0,
    top_p=0.95,
    extra_body={
        "skip_special_tokens": False,
        "chat_template_kwargs": {"enable_thinking": False},
    }
)
print(response.choices[0].message.content)
print()

# 測試流式輸出
print("=== 測試 3: 流式輸出 ===")
stream = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "Explain speculative decoding in two sentences"}],
    max_tokens=512,
    temperature=1.0,
    top_p=0.95,
    stream=True,
    extra_body={"skip_special_tokens": False},
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="", flush=True)
print()
```

### 方法三：完整測試腳本

建立 `test_nemotron.py`：

```python
#!/usr/bin/env python3
"""NVIDIA Nemotron-3.5-Bolt-E4B-4GB 完整測試腳本"""

import requests
import json
import time
from typing import Dict, Any

BASE_URL = "http://localhost:8000/v1"
MODEL = "nemotron-bolt"

def make_request(messages: list, **kwargs: Any) -> Dict[str, Any]:
    """發送 API 請求"""
    payload = {
        "model": MODEL,
        "messages": messages,
        "temperature": 1.0,
        "max_tokens": 512,
        "chat_template_kwargs": {"enable_thinking": True}
    }
    payload.update(kwargs)
    
    response = requests.post(
        f"{BASE_URL}/chat/completions",
        headers={"Content-Type": "application/json"},
        json=payload
    )
    
    response.raise_for_status()
    return response.json()

def test_basic_math():
    """測試基本數學能力"""
    print("測試 1: 基本數學能力")
    print("-" * 50)
    messages = [
        {"role": "user", "content": "Calculate: 17 × 23"}
    ]
    start = time.time()
    result = make_request(messages)
    elapsed = time.time() - start
    
    print(f"回應:\n{result['choices'][0]['message']['content']}")
    print(f"延遲: {elapsed:.2f} 秒")
    print()

def test_reasoning_off():
    """測試推理關閉模式"""
    print("測試 2: 推理關閉模式")
    print("-" * 50)
    messages = [
        {"role": "user", "content": "What is the capital of Japan?"}
    ]
    start = time.time()
    result = make_request(
        messages,
        extra_body={
            "chat_template_kwargs": {"enable_thinking": False}
        }
    )
    elapsed = time.time() - start
    
    print(f"回應:\n{result['choices'][0]['message']['content']}")
    print(f"延遲: {elapsed:.2f} 秒")
    print()

def test_streaming():
    """測試流式輸出"""
    print("測試 3: 流式輸出")
    print("-" * 50)
    messages = [
        {"role": "user", "content": "Explain LLM in one sentence"}
    ]
    
    stream = make_request(
        messages,
        stream=True
    )
    
    start = time.time()
    full_response = ""
    for chunk in stream:
        content = chunk.choices[0].delta.content or ""
        full_response += content
        print(content, end="", flush=True)
    elapsed = time.time() - start
    
    print()
    print(f"完整回應長度: {len(full_response)} 字元")
    print(f"延遲: {elapsed:.2f} 秒")
    print()

def test_long_context():
    """測試長上下文"""
    print("測試 4: 長上下文處理")
    print("-" * 50)
    
    # 建立長上下文
    context = "Here are some facts:\n"
    for i in range(100):
        context += f"{i}. The {i}-th fact is: This is a test sentence number {i}.\n"
    
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Based on the context above, tell me about fact 50."}
    ]
    
    start = time.time()
    result = make_request(messages)
    elapsed = time.time() - start
    
    print(f"回應:\n{result['choices'][0]['message']['content']}")
    print(f"延遲: {elapsed:.2f} 秒")
    print()

def test_conversational_mode():
    """測試對話模式"""
    print("測試 5: 對話模式")
    print("-" * 50)
    messages = [
        {"role": "user", "content": "What is the capital of France?"}
    ]
    
    start = time.time()
    result = make_request(
        messages,
        extra_body={
            "chat_template_kwargs": {"conversational_mode": True}
        }
    )
    elapsed = time.time() - start
    
    print(f"回應:\n{result['choices'][0]['message']['content']}")
    print(f"延遲: {elapsed:.2f} 秒")
    print()

def test_multiple_turns():
    """測試多輪對話"""
    print("測試 6: 多輪對話")
    print("-" * 50)
    
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"},
        {"role": "assistant", "content": "Hi there! How can I help you?"},
        {"role": "user", "content": "What's the weather like in Tokyo?"},
        {"role": "assistant", "content": "I can help with that. Let me check..."}
    ]
    
    start = time.time()
    result = make_request(messages)
    elapsed = time.time() - start
    
    print(f"回應:\n{result['choices'][0]['message']['content']}")
    print(f"延遲: {elapsed:.2f} 秒")
    print()

def validate_response(result: Dict[str, Any]) -> bool:
    """驗證回應格式"""
    required_fields = ["id", "object", "created", "model", "choices"]
    return all(field in result for field in required_fields) and \
           len(result["choices"]) > 0 and \
           "message" in result["choices"][0]

def run_all_tests():
    """執行所有測試"""
    print("=" * 50)
    print("NVIDIA Nemotron-3.5-Bolt-E4B-4GB 測試")
    print("=" * 50)
    print()
    
    tests = [
        test_basic_math,
        test_reasoning_off,
        test_streaming,
        test_long_context,
        test_conversational_mode,
        test_multiple_turns,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            if validate_response(make_request([{"role": "user", "content": "test"}])):
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"測試失敗: {str(e)}")
            failed += 1
    
    print("=" * 50)
    print(f"測試結果: {passed} 通過 / {len(tests)} 總數")
    if failed > 0:
        print(f"警告: {failed} 個測試失敗")
    print("=" * 50)

if __name__ == "__main__":
    run_all_tests()
```

執行測試：

```bash
# 啟動服務後執行
python test_nemotron.py
```

## API 使用範例

### 1. 推理開啟（預設）

```python
response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "Write a haiku about GPUs"}],
    max_tokens=16000,
    temperature=1.0,
    top_p=0.95,
    extra_body={
        "skip_special_tokens": False,
        "chat_template_kwargs": {"enable_thinking": True},
    }
)
print(response.choices[0].message.content)
```

### 2. 推理關閉

```python
response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "What is the capital of Japan?"}],
    max_tokens=16000,
    temperature=1.0,
    top_p=0.95,
    extra_body={
        "skip_special_tokens": False,
        "chat_template_kwargs": {"enable_thinking": False},
    }
)
print(response.choices[0].message.content)
```

### 3. 工具呼叫

```python
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the current weather for a city",
        "parameters": {
            "type": "object",
            "properties": {"city": {"type": "string"}},
            "required": ["city"],
        },
    },
}]

response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "What's the weather in Santa Clara?"}],
    tools=tools,
    max_tokens=16000,
    temperature=1.0,
    top_p=0.95,
    extra_body={
        "skip_special_tokens": False,
        "chat_template_kwargs": {"enable_thinking": True},
    },
)
print(response.choices[0].message.tool_calls)
```

### 4. 對話模式

```python
response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "What is the capital of Japan?"}],
    max_tokens=16000,
    temperature=1.0,
    top_p=0.95,
    extra_body={
        "skip_special_tokens": False,
        "chat_template_kwargs": {"conversational_mode": True},
    }
)
print(response.choices[0].message.content)
```

## 效能指標

### 基準測試結果

| 基準 | Nemotron-3.5 Bolt-E4B (Q4_K_M) | Gemma4 E4B-it (Q4_K_M) | Qwen3.5 4B (Q4_K_M) |
|------|--------------------------------|------------------------|---------------------|
| **MultiChallenge** | 55.60 | 39.36 | 52.23 |
| **RoleBench** | 71.21 | 60.51 | 52.35 |
| **RoleMRC** | 79.12 | 75.24 | 62.61 |
| **EQ-Bench v3** | 39.77 | 32.07 | 19.45 |
| **Brevity Benchmark** | 82.84 | 78.49 | 75.17 |
| **BFCL-v3** | 70.56 | 67.31 | 65.03 |
| **When2Call Multi-Turn** | 61.12 | 42.88 | 35.96 |
| **ToolSandbox** | 74.51 | 68.31 | 59.78 |
| **IHEval** | 82.40 | 66.61 | 62.87 |
| **StructEval-T** | 79.99 | 77.28 | 76.38 |
| **LongMemEval** | 76.60 | 67.95 | 27.15 |

**亮點：**

- ✅ **RoleBench**: 71.21 - 角色扮演表現優異
- ✅ **RoleMRC**: 79.12 - 角色知識問答能力強
- ✅ **EQ-Bench v3**: 39.77 - 情商表現出色
- ✅ **LongMemEval**: 76.60 - 長記憶處理能力優異
- ✅ **Brevity Benchmark**: 82.84 - 簡潔回應能力強

## 最佳實踐

### 1. Prompt 結構與內容

```python
system_prompt = """
# ROLE
You are a helpful AI assistant.

# INPUT FORMAT
- Input will be in natural language
- Support multiple turns

# TASK RULES
- Be concise and direct
- Use clear language
- Follow instructions precisely
"""

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "Your question here"}
]
```

### 2. 明確的限制

```python
# ✅ 推薦：明確限制
extra_body={
    "chat_template_kwargs": {
        "limit_responses_to_1_2_sentences": True
    }
}

# ❌ 不推薦：模糊請求
extra_body={
    "chat_template_kwargs": {
        "be_brief": True
    }
}
```

### 3. 環境狀態傳遞

```python
# 狀態更新必須在前
messages = [
    {"role": "user", "content": "# CURRENT STATE\nInventory: sword, potion\n"},
    {"role": "user", "content": "What items do I have?"}
]

# 工具執行後的狀態更新必須在後
messages = [
    {"role": "tool", "content": "<tool execution result>"},
    {"role": "user", "content": "# CURRENT STATE\nInventory: sword, potion, gold\n"},
    {"role": "user", "content": "What items do I have now?"}
]
```

### 4. 工具定義

```python
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get current weather for a city",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "City name"
                }
            },
            "required": ["city"]
        }
    }
}]
```

### 5. 思考預算控制

```bash
docker run ... \
  --reasoning on \
  --reasoning-budget 1000 \
  ...
```

- ⚠️ 受限的 token 配額可能在句子中途截斷思考過程
- ✅ 執行前使用標準評估提示進行系統性的配額掃描

### 6. 漸進式工具呼叫

```python
# 1. 助手發出工具呼叫
{"role": "assistant", "tool_calls": [{"id": "call_1", ...}]}

# 2. 立即回應待處理狀態
{"role": "tool", "tool_call_id": "call_1", "content": "{\"status\":\"pending\"...}"}

# 3. 後續工具結果
{"role": "user", "content": "TOOL UPDATE: {\"status\":\"completed\"...}"}
```

## 參考資源

- [Hugging Face 模型頁面](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB)
- [NVIDIA Developer 頁面](https://developer.nvidia.com/nemotron)
- [技術報告](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB-Technical-Report.pdf)
- [技術部落格](https://research.nvidia.com/labs/nemotron/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB/)
- [Discord 社群](https://discord.gg/9xpKQtVvrk)

## 附錄：完整 Docker 命令速查表

```bash
# 基礎部署（無 drafter）
docker run --rm --gpus all -p 8000:8000 \
  -v "$MODEL_DIR:/models:ro" \
  ghcr.io/ggml-org/llama.cpp:server-cuda13-b11459 \
  -m "/models/Nemotron-3.5-Bolt-E4B-Q4_K_M.gguf" \
  --alias nemotron-bolt \
  --host 0.0.0.0 --port 8000 \
  -c 65536 -ngl 999 --jinja

# 使用 DFlash drafter
docker run --rm --gpus all -p 8000:8000 \
  -v "$MODEL_DIR:/models:ro" \
  ghcr.io/ggml-org/llama.cpp:server-cuda13-b11459 \
  -m "/models/Nemotron-3.5-Bolt-E4B-Q4_K_M.gguf" \
  --spec-draft-model "/models/Nemotron-3.5-Bolt-E4B-DFlash-BF16.gguf" \
  --spec-type draft-dflash \
  --spec-draft-n-max 7 --spec-draft-ngl 999 \
  --alias nemotron-bolt \
  --host 0.0.0.0 --port 8000 \
  -c 65536 -ngl 999 --jinja \
  --reasoning on --reasoning-budget 1000
```

*報告完成於 2026 年 10 月 23 日*
