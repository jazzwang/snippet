# Pi Agent 使用 SGLang 設定指南

本文件說明如何讓 Pi coding agent 使用 SGLang 作為 LLM 提供者。

## 目錄

- [方式一：使用 `pi-localllm-provider` 自動設定](#方式一使用-pi-localllm-provider-自動設定)
- [方式二：手動配置 `models.json`](#方式二手動配置-modelsjson)
- [方式三：使用 `owo-local` 套件](#方式三使用-owo-local-套件)
- [常見 SGLang 模型配置範例](#常見-sglang-模型配置範例)
- [實用命令](#實用命令)
- [注意事項](#注意事項)

## 方式一：使用 `pi-localllm-provider` 自動設定（推薦）

這是一個自動化的設定工具，可以自動偵測和配置 SGLang 伺服器。

### 步驟 1：安裝套件

```bash
pi install npm:pi-localllm-provider
```

### 步驟 2：啟動 SGLang 伺服器

```bash
# 啟動 SGLang，例如使用 Qwen 模型
sglang serve --model-path Qwen/Qwen2.5-7B-Instruct --port 30000
```

### 步驟 3：使用 TUI 介面設定

```bash
pi                      # 啟動 Pi
/localllm               # 進入本地 LLM 管理介面
# 選擇 + Add server，按照引導完成設定
```

## 方式二：手動配置 `models.json`

### 步驟 1：啟動 SGLang 伺服器

```bash
# 在終端機 A 啟動 SGLang
sglang serve --model-path Qwen/Qwen2.5-7B-Instruct --port 30000
```

### 步驟 2：編輯 Pi 的 `models.json`

```bash
# 查看現有的 models.json
cat ~/.pi/agent/models.json
```

### 步驟 3：添加 SGLang 提供者配置

```json
{
  "$schema": "https://pi.dev/schemas/models.schema.json",
  "providers": {
    "sglang": {
      "baseUrl": "http://localhost:30000/v1",
      "api": "openai-completions",
      "apiKey": "",
      "models": [
        {
          "id": "Qwen/Qwen2.5-7B-Instruct",
          "name": "Qwen2.5-7B-Instruct",
          "contextWindow": 16384,
          "capabilities": ["chat-completions", "tool-use"]
        }
      ]
    }
  }
}
```

### 步驟 4：在 Pi 中使用該模型

```bash
pi --provider sglang --model Qwen/Qwen2.5-7B-Instruct
```

## 方式三：使用 `owo-local` 套件

另一個支援的套件是 `owo-local`，它也支援 SGLang。

```bash
pi install npm:owo-local
pi --provider owo-local
# 然後按照引導輸入 SGLang 的 URL 和 API key
```

## 常見 SGLang 模型配置範例

### Qwen3.6 35B-A3B FP8

```json
{
  "$schema": "https://pi.dev/schemas/models.schema.json",
  "providers": {
    "sglang-homelab": {
      "baseUrl": "http://localhost:30000/v1",
      "api": "openai-completions",
      "apiKey": "",
      "models": [
        {
          "id": "Qwen/Qwen3.6-35B-A3B-FP8",
          "name": "Qwen3.6-35B-A3B-FP8",
          "contextWindow": 256000,
          "capabilities": ["chat-completions", "tool-use"]
        }
      ]
    }
  }
}
```

### DeepSeek-V4-Flash FP4

```json
{
  "$schema": "https://pi.dev/schemas/models.schema.json",
  "providers": {
    "sglang": {
      "baseUrl": "http://localhost:30000/v1",
      "api": "openai-completions",
      "apiKey": "",
      "models": [
        {
          "id": "deepseek-ai/DeepSeek-V4-Flash-Base",
          "name": "DeepSeek-V4-Flash-Base",
          "contextWindow": 128000,
          "capabilities": ["chat-completions"]
        }
      ]
    }
  }
}
```

### 使用 NVIDIA Dynamo

```json
{
  "$schema": "https://pi.dev/schemas/models.schema.json",
  "providers": {
    "dynamo": {
      "baseUrl": "http://localhost:8080/v1",
      "api": "openai-completions",
      "apiKey": "",
      "models": [
        {
          "id": "dynamo/qwen3.5:256k",
          "name": "Qwen3.5 256K"
        }
      ]
    }
  }
}
```

## 實用命令

```bash
# 查看 Pi 支援的模型
pi /model

# 查看可用的提供者
pi /login

# 查看當前配置
cat ~/.pi/agent/models.json

# 啟動 SGLang（需要 NVIDIA CUDA 支援）
sglang serve --model-path {huggingface_id} --port 30000

# 使用 SGLang
pi --provider sglang --model {model_id}

# 安裝 pi-localllm-provider
pi install npm:pi-localllm-provider

# 安裝 owo-local
pi install npm:owo-local
```

## 注意事項

### 系統要求

1. **SGLang 需要 NVIDIA CUDA 支援**
   - 確保你的系統有 CUDA 支援
   - 安裝 NVIDIA 驅動

2. **記憶體需求**
   - 小型模型（如 Qwen2.5-7B）：需要約 7-8GB VRAM
   - 中型模型（如 Qwen2.5-32B）：需要約 20-24GB VRAM
   - 大型模型（如 Qwen3.6-35B）：需要約 40-60GB VRAM（使用 FP8 量化可減少）

3. **Port 衝突**
   - 確保 30000 端口未被佔用
   - 可更改為其他端口：`--port 8080`

4. **API Key**
   - 本地伺服器通常不需要 API key
   - 可以留空：`"apiKey": ""`

### 下載模型

```bash
# 使用 huggingface-cli 下載模型
pip install huggingface_hub
huggingface-cli download Qwen/Qwen2.5-7B-Instruct --local-dir ./models/Qwen2.5-7B-Instruct

# 或使用 singularity（適合伺服器環境）
singularity pull docker://quodlibet/sglang:latest
```

### 故障排除

```bash
# 檢查 SGLang 是否運行
curl http://localhost:30000/v1/models

# 檢查 Pi 連接
pi /model

# 查看 Pi 日誌
tail -f ~/.pi/agent/*.log
```

### 參考資源

- [pi-localllm-provider GitHub](https://github.com/freeyoung/pi-localllm-provider)
- [pi.dev models 文件](https://pi.dev/docs/latest/models)
- [pi.dev models 配置](https://pi.dev/docs/latest/models-configuration)
- [SGLang 官方文档](https://sgl-project.github.io/)

*最後更新：2024*
