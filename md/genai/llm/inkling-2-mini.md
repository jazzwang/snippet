# Inkling-2-Mini 技術報告

## 1. 模型概述

**Inkling-2-Mini** 是由 Thinking Machines Lab 開發的快速、強大的開源模型，專為在筆記型電腦上運行而設計。這是第一個採用 **循環變換器（Looped Transformer）** 架構的開源模型，在 100B 以下參數的開源模型中表現領先。

### 核心特點

| 項目 | 規格 |
|------|------|
| **總參數** | 264 億（26.4B） |
| **激活參數** | 34 億（3.4B） |
| **每 token 有效激活** | 54 億（5.4B，含循環） |
| **架構類型** | 24 層解碼變換器，稀疏 MoE 前饋層 |
| **循環層數** | 中間 12 層（層 6-17）每 token 運行 3 次 |
| **專家路由** | 每 token 路由至 128 個專家中的 8 個 |
| **上下文視窗** | 100 萬 tokens（1M） |
| **精度格式** | NVFP4（主要）+ MXFP8（最後 4 層） |
| **記憶體足跡** | ~20GB |
| **發布日期** | 2026 年 11 月 20 日 |
| **授權協議** | Apache 2.0 |

### 循環變換器架構

Inkling-2-Mini 採用獨特的循環變換器設計，其中層 6-17 在每個 token 生成時會運行 3 次。這使模型能夠：

- 在不需輸出推理過程的情況下進行更長期的思考
- 提升 agentic coding 等需要高推理品質的任務表現
- 保持更短的 Chain of Thought（CoT），便於監控和理解模型行為

## 2. 硬體要求

### 最低硬體配置

| 量化等級 | 記憶體需求 (RAM/VRAM) | 說明 |
|----------|---------------------|------|
| 1-bit | 9 GB | 高度量化 |
| 2-bit | 10-11 GB | 高度量化 |
| 3-bit | 13-15 GB | 中等量化 |
| 4-bit | 17-18 GB | 推薦：UD-Q4_K_XL（17.63 GB） |
| 8-bit (Lossless) | 24 GB | 完整精度 |

### 推薦硬體環境

- **Apple Silicon**：32GB 以上統一記憶體（MacBook、Mac mini、Mac Studio）
  - 支援：Ollama、Exo Labs
- **NVIDIA GPU**：RTX 20 系列至 RTX 50 系列，V100、T4、A100、H100、B200
  - 需要 CUDA 12 或 CUDA 13
- **AMD GPU**：Radeon RX 9000 系列（gfx120X）
  - 需要 ROCm 支援
- **其他平台**：需 32GB VRAM 以上

### 量化版本

- **UD-Q8_K_XL**：完整精度（24GB）
- **UD-Q4_K_XL**：推薦量化（17.63 GB）
- **GGUF 版本**：支援 llama.cpp

## 3. 軟體環境

### 支援的推理框架

| 框架 | 說明 |
|------|------|
| **Hugging Face** | 原生支援 |
| **SGLang** | 高效推理 |
| **vLLM** | 批處理推理 |
| **TokenSpeed** | 加速推理 |
| **NVIDIA Dynamo** | 優化推理 |
| **Unsloth** | 最佳化推理（~1.9 倍加速） |
| **llama.cpp** | GGUF 量化版本 |
| **Llama App** | 桌面應用程式 |
| **Ollama** | Apple Silicon 專用 |

### 安裝方式

#### 方式一：Unsloth Desktop（推薦）

```bash
# macOS
brew install --cask unsloth

# Windows
winget install --id UnslothAI.Unsloth -e

# Linux/macOS/WSL
curl -fsSL https://unsloth.ai/install.sh | sh

# Docker
docker pull unsloth/unsloth
docker run -it --rm -p 8080:8080 unsloth/unsloth
```

#### 方式二：llama.cpp 專用版本

**Apple Silicon：**
```bash
curl -L -o llama.tar.gz https://github.com/unslothai/llama.cpp/releases/download/b12649-mix-c7059d6/llama-b12649-mix-c7059d6-bin-macos-arm64.tar.gz
mkdir -p llama.cpp
tar -xzf llama.tar.gz -C llama.cpp --strip-components=1
./llama.cpp/llama-server --version
```

**NVIDIA GPU：**
```bash
# CUDA 12
curl -L -o llama.tar.gz https://github.com/unslothai/llama.cpp/releases/download/b12649-mix-c7059d6/app-b12649-mix-c7059d6-linux-x64-cuda12-portable.tar.gz
mkdir -p llama.cpp
tar -xzf llama.tar.gz -C llama.cpp
./llama.cpp/llama-server --version
```

**AMD GPU：**
```bash
curl -L -o llama.tar.gz https://github.com/unslothai/llama.cpp/releases/download/b12649-mix-c7059d6/app-b12649-mix-c7059d6-linux-x64-rocm-gfx120X.tar.gz
mkdir -p llama.cpp
tar -xzf llama.tar.gz -C llama.cpp
./llama.cpp/llama-server --version
```

## 4. 模型下載

### Unsloth GGUF 版本

```bash
pip install -U huggingface_hub
hf download unsloth/Inkling-2-Mini-GGUF \
    Inkling-2-Mini-UD-Q4_K_XL.gguf mmproj-F16.gguf \
    dspark-Inkling-2-Mini-Q8_0.gguf \
    --local-dir Inkling-2-Mini-GGUF
```

### 所需檔案清單

| 檔案 | 說明 | 大小 |
|------|------|------|
| `Inkling-2-Mini-UD-Q4_K_XL.gguf` | 4 位量化模型 | ~17.6GB |
| `mmproj-F16.gguf` | 視覺投影器（F16） | 639 MB |
| `dspark-Inkling-2-Mini-Q8_0.gguf` | DSpark drafter（可選） | ~0.4GB |

## 5. 安裝步驟

### 步驟一：安裝 Unsloth

1. **下載 Unsloth Desktop**
   - macOS：https://unsloth.ai/download/mac
   - Windows：https://unsloth.ai/download/windows
   - Linux：https://unsloth.ai/download/linux

2. **或透過命令行安裝**
   ```bash
   curl -fsSL https://unsloth.ai/install.sh | sh
   ```

### 步驟二：搜尋並下載模型

1. 在 Unsloth Desktop 中打開 **Select model** 或前往 **Model hub**
2. 搜尋 **Inkling 2 Mini**
3. 選擇 **[unsloth/Inkling-2-Mini-GGUF](https://huggingface.co/unsloth/Inkling-2-Mini-GGUF)**
4. 下載適合您設備的量化版本
5. 下載完成後，在 Chat 中選擇模型並開始對話

### 步驟三：透過 Unsloth API 服務模型

```bash
unsloth run --model unsloth/Inkling-2-Mini-GGUF:UD-Q4_K_XL \
    --temp 1.0 --top-p 1.0 --top-k 0 --min-p 0.0
```

- 終端機會列印端點 URL 和 API key
- 使用 Unsloth API 指南進行客戶端連接

## 6. 使用步驟（llama.cpp）

### 步驟一：啟動本地聊天伺服器

**macOS/Linux/WSL：**
```bash
./llama.cpp/llama-server \
    --model Inkling-2-Mini-GGUF/Inkling-2-Mini-UD-Q4_K_XL.gguf \
    --mmproj Inkling-2-Mini-GGUF/mmproj-F16.gguf \
    --model-draft Inkling-2-Mini-GGUF/dspark-Inkling-2-Mini-Q8_0.gguf \
    --spec-type draft-dspark --spec-draft-n-max 2 --n-gpu-layers-draft 99 \
    --temp 1.0 --top-p 1.0 --top-k 0 --min-p 0.0 \
    --host 127.0.0.1 --port 8080
```

**Windows PowerShell：**
```powershell
.\llama.cpp\llama-server.exe `
    --model Inkling-2-Mini-GGUF/Inkling-2-Mini-UD-Q4_K_XL.gguf `
    --mmproj Inkling-2-Mini-GGUF/mmproj-F16.gguf `
    --model-draft Inkling-2-Mini-GGUF/dspark-Inkling-2-Mini-Q8_0.gguf `
    --spec-type draft-dspark --spec-draft-n-max 2 --n-gpu-layers-draft 99 `
    --temp 1.0 --top-p 1.0 --top-k 0 --min-p 0.0 `
    --host 127.0.0.1 --port 8080
```

### 步驟二：開啟網頁介面

- 瀏覽器開啟 <http://127.0.0.1:8080>
- 開始聊天或上傳圖片

### 參數說明

| 參數 | 值 | 說明 |
|------|-----|------|
| `--temp` | 1.0 | 溫度參數 |
| `--top-p` | 1.0 | Nucleus sampling |
| `--top-k` | 0 | Top-k sampling |
| `--min-p` | 0.0 | Min-p sampling |
| `--model-draft` | dspark-Inkling-2-Mini-Q8_0.gguf | DSpark 推測解碼 |
| `--spec-draft-n-max` | 2 | 推解碼深度（最快） |
| `--n-gpu-layers` | 全部 | GPU 層數（CPU 則設為 0） |

### 簡易模式（不含 DSpark）

移除 `--model-draft`、`--spec-type`、`--spec-draft-n-max`、`--n-gpu-layers-draft` 參數，並可省略 `--mmproj` 參數（純文字聊天）。

## 7. 測試步驟

### 測試一：基本文字對話

**提示詞範例：**
```
你好！請簡單介紹一下 Python 的資料結構有哪些。
```

**預期回應：**
- 模型應能列出 Python 主要資料結構（list、dict、tuple、set 等）
- 提供基本說明和用途

### 測試二：程式碼生成

**提示詞範例：**
```
請寫一個 Python 函數，計算斐波那契數列的第 n 項，並使用動態規劃優化。
```

**驗證重點：**
- 程式碼語法正確
- 使用動態規劃或記憶體優化
- 時間複雜度為 O(n)

### 測試三：視覺理解（如有圖片輸入）

**提示詞範例：**
```
請分析這張圖片中的內容，並描述主要特徵。
```

**上傳：**
- 選擇符合要求的圖片（40px - 4096px）

### 測試四：長上下文處理

**提示詞範例：**
```
以下是長篇文章，請總結主要觀點：
[在此貼上長篇文章內容，可達 100 萬 tokens]
```

**驗證重點：**
- 能否正確理解全文脈絡
- 摘要是否準確完整

### 測試五：Agentic 任務

**提示詞範例：**
```
請幫我解讀這個程式碼問題並提供修復建議。
```

**驗證重點：**
- 問題診斷能力
- 修復建議的準確性

## 8. 驗證步驟

### 8.1 效能測試

#### 解碼速度測試（llama.cpp）

```bash
# 測量每秒 token 數
./llama.cpp/llama-bench \
    -m Inkling-2-Mini-GGUF/Inkling-2-Mini-UD-Q4_K_XL.gguf \
    --ctx-size 8192 --batch-size 512 \
    -ngl 99 -t 16
```

**預期指標：**
- GPU 上每秒 token 數（tokens/sec）
- 記憶體占用情況

#### 記憶體使用測試

```bash
# 監控記憶體使用
./llama.cpp/llama-server \
    --model Inkling-2-Mini-GGUF/Inkling-2-Mini-UD-Q4_K_XL.gguf \
    --mem-f16-mmap 1 --verbose-llama

# 或透過系統監控工具
watch -n 1 free -h
```

**預期記憶體占用：**
- UD-Q4_K_XL：~17.6GB
- 完整精度：~24GB

### 8.2 模型效能驗證

#### DeepSWE v1.1 驗證

**測試命令：**
```bash
# 使用 mini-swe-agent v2.4.6 環境
python -m mini_swe_agent.evaluation --model Inkling-2-Mini --benchmark DeepSWE v1.1
```

**預期指標：** **48.2%**（開源模型中領先）

#### SWEBench Pro v2 (Hard) 驗證

**測試命令：**
```bash
python -m swe_bench.evaluation --model Inkling-2-Mini --benchmark SWEBench Pro v2 Hard
```

**預期指標：** **77.9%**

#### Terminal Bench v4.0

**測試命令：**
```bash
python -m terminal_bench.evaluation --model Inkling-2-Mini
```

**預期指標：** **5.6%**（Terminal Bench 4.0）

### 8.3 量化品質驗證

#### KLD 驗證

```bash
# 使用 huggingface_hub 檢查量化品質
pip install huggingface_hub
hf-cli download unsloth/Inkling-2-Mini-GGUF \
    --repo-type model
```

**預期結果：**
- UD-Q4_K_XL：MXFP8 dequantized 至 Q8_0，KLD 接近 0
- UD-Q8_K_XL：完整精度，KLD = 0

#### 語意相似度測試

```python
import torch
from transformers import AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained(
    "unsloth/Inkling-2-Mini-GGUF",
    device_map="auto",
    torch_dtype=torch.float16
)

# 測試輸出語意一致性
prompt = "寫一個 Python 排序函數"
response = model.generate(prompt, max_new_tokens=200)
# 檢查回應的語意是否合理
```

### 8.4 硬體兼容性測試

#### Apple Silicon 測試

```bash
# 檢查 M-series CPU 支援
sysctl -n hw.memsize
# 應 > 32GB

# 啟動模型
ollama run inkling-2-mini
```

#### NVIDIA GPU 測試

```bash
# 檢查 CUDA 支援
nvidia-smi

# 檢查 CUDA 版本
nvcc --version

# 啟動模型
python -c "import torch; print(torch.cuda.is_available())"
```

#### AMD GPU 測試

```bash
# 檢查 ROCm 支援
rocm-smi

# 啟動模型
# 使用 ROCm 版本的 llama.cpp
```

## 9. 效能 benchmark 結果

### 模型比較

| 模型 | 參數 | Vals Index | DeepSWE v1.1 | SWEBench Pro v2 | Terminal Bench v4.0 |
|------|------|-----------|-------------|-----------------|---------------------|
| **Inkling-2-Mini** | 26.4B (5.4B 激活) | **46.5%** | **48.2%** | **77.9%** | **5.6%** |
| Gemma 4 31B | 30.7B | - | - | - | - |
| Muse Glimmer | 30.0B | - | 4.4% | - | - |
| Qwen3.8-27B | 27.0B | 29.8% | 42.2% | 73.8% | 5.6% |
| Nemotron 3.5 Super VL | 12.0B (124.5B) | - | 24.7% | 44.1% | - |

### 其他 benchmark 結果

| Benchmark | Inkling-2-Mini | 備註 |
|-----------|---------------|------|
| **AA Index v5.0** | 20.1 | 最佳（與 Qwen3.8-27B 並列） |
| **MMMU Pro** | 74.9% | 標準 10 |
| **OmniDocBench v1.6** | 92.8% | 文件理解 |
| **PerceptionBench** | 57.5% | 視覺理解 |
| **MCP Atlas Public** | 82.7% | 工具使用 |
| **DeepSearchQA** | 85.3% | 搜尋任務 |
| **BrowseComp** | 79.0% | 網頁瀏覽 |
| **GDP.pdf** | 16.8% | 文件處理 |
| **ARC-AGI v1** | 84.5% | 推理能力 |
| **FORTRESS (adversarial)** | 89.5% | 安全性 |

## 10. 安全性評估

### 安全性測試結果

| 測試項目 | Inkling-2-Mini | 說明 |
|----------|---------------|------|
| **FORTRESS (adversarial)** | 89.5% | 惡意攻擊抵禦 |
| **FORTRESS (benign)** | 96.4% | 正常請求處理 |
| **StrongREJECT** | 97.8% | 拒絕不當請求 |
| **Misbehavior (Internal)** | 9.8% | 誤用行為（越低越好） |
| **Covert misbehavior** | 8.3% | 隱蔽誤用（越低越好） |
| **Destructive actions** | 10.2% | 破壞行為（越低越好） |

### 安全性防護

- 使用 on-policy distillation 進行對齊訓練
- 評估自殺、自我傷害、飲食紊亂等敏感請求處理
- 評估 CBRN（化學、生物、放射、核）和網路安全知識
- 評估 agentic sabotage（代理破壞）潛力

## 11. 故障排除

### 常見問題

#### 問題一：記憶體不足

**症狀：** 啟動模型時報錯 "Out of memory"

**解決方案：**
1. 使用更低量化版本（如 2-bit 或 1-bit）
2. 減少 `--ctx-size` 參數
3. 在 llm.cpp 中設定 `--n-gpu-layers 0` 使用 CPU
4. 確認系統記憶體 > 32GB

#### 問題二：DSpark drafter 啟動失敗

**症狀：** `--model-draft` 參數報錯

**解決方案：**
1. 確保已下載 `dspark-Inkling-2-Mini-Q8_0.gguf`
2. 移除 `--model-draft`、`--spec-type` 等相關參數
3. 使用純文字聊天模式

#### 問題三：視覺功能不工作

**症狀：** 上傳圖片後無法處理

**解決方案：**
1. 確認已下載 `mmproj-F16.gguf` 視覺投影器
2. 檢查圖片尺寸是否在 40px - 4096px 範圍內
3. 確認 GPU 支援視覺處理

#### 問題四：解碼速度慢

**症狀：** 每秒 token 數低於預期

**解決方案：**
1. 檢查 CUDA/ROCm 版本
2. 確認使用 Unsloth 優化版本而非主線 llama.cpp
3. 增加 `--batch-size` 提升批處理效率

## 12. 參考資源

### 官方資源

- **Thinking Machines AI**：https://thinkingmachines.ai/news/inkling-2-mini/
- **Hugging Face**：https://huggingface.co/thinkingmachines/Inkling-2-Mini
- **Unsloth 文件**：https://unsloth.ai/docs/models/inkling-2-mini
- **Tinker Cookbook**：https://github.com/thinking-machines-lab/tinker-cookbook
- **Tinker Playground**：https://tinker.thinkingmachines.ai/playground

### 模型資源

- **GGUF 版本**：https://huggingface.co/unsloth/Inkling-2-Mini-GGUF
- **Hugging Face 原模型**：https://huggingface.co/thinkingmachines/Inkling-2-Mini

### 相關工具

- **Ollama**：https://ollama.com/library/inkling-2-mini
- **TokenSpeed**：https://lightseek.org/tokenspeed/recipes/models#inkling-2-mini

## 13. 總結

Inkling-2-Mini 是 Thinking Machines Lab 推出的開源模型，其獨特的 **循環變換器架構** 使其在 100B 以下參數的開源模型中表現領先。主要特點：

- **高效推理**：~20GB 記憶體足跡，可在筆記型電腦運行
- **強大 agentic 能力**：DeepSWE v1.1 達 48.2%，SWEBench Pro v2 達 77.9%
- **多模態支援**：文字與圖片輸入
- **1M 上下文視窗**：支援長文檔處理
- **Apache 2.0 授權**：自由商用

推薦使用 **Unsloth Desktop** 或 **llama.cpp** 進行本地部署，並根據硬體選擇合適的量化版本。
