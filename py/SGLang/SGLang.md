# SGLang

- Git Repo
  - https://github.com/sgl-project/sglang
- Website
  - https://sglang.io

## 2026-10-15

> [!NOTE]
>請根據 https://github.com/sgl-project/sglang 與 https://sglang.io 的內容，撰寫一篇繁體中文技術摘要，並列舉如何 step-by-step 安裝測試。將結果存成 SGLang.md

## SGLang 技術摘要與安裝指南

SGLang 是個開源的高效能框架，專門為大型語言模型（LLM）、視覺語言模型，還有擴散模型量身打造。無論是要處理複雜的代理工作負載、大規模服務，或是 RL 卷積，它都能輕鬆應對。核心技術採用創新的 **SGLang 解釋器** 架構，讓模型服務既能快如閃電，又能同時處理大量請求。

#### 為什麼值得用？

- **跨平台支援**：NVIDIA、AMD、Google TPU、Intel、Apple Silicon、華為昇騰，各種硬體平台都能跑
- **效能優化**：內建 Prefill/Decode 解耦、猜測解碼（Speculative Decoding）、並行處理，速度更快
- **資源利用率高**：零開銷調度器，讓每分每秒的算力都物超所值
- **圖像與視頻生成**：SGLang Diffusion 內建支援，不用額外配置
- **API 友善**：標準 OpenAI API 介面，部署調用超簡單

#### 受信任的企業夥伴

- NVIDIA、xAI、Oracle、AMD、LinkedIn、Google Cloud 等企業已採用 SGLang

### 安裝測試步驟

#### 方法一：使用 Docker（推薦）

##### 步驟 1：準備環境

確保已安裝：
- Docker Engine
- NVIDIA Container Toolkit（用於 NVIDIA GPU）

##### 步驟 2：下載 Docker 映像

```bash
## 拉取最新 stable 版本
docker pull lmsysorg/sglang:latest

## 或使用 nightly 版本（每日更新）
docker pull lmsysorg/sglang:latest-nightly
```

##### 步驟 3：啟動服務器

```bash
## 設定 HF 快取目錄
export HF_CACHE_DIR="/path/to/huggingface-cache"

## 啟動服務器（替換 MODEL_PATH 為您的模型 ID）
docker run -it --gpus all \
  --shm-size 32g \
  -p 30000:30000 \
  -v "$HF_CACHE_DIR:/root/.cache/huggingface" \
  --ipc=host \
  lmsysorg/sglang:latest bash
```

進入容器後：
```bash
## 啟動模型服務器
sglang serve Qwen/Qwen3-0.6B --host 0.0.0.0 --port 30000
```

##### 步驟 4：發送測試請求

在另一個終端執行：
```bash
curl http://localhost:30000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "Qwen/Qwen3-0.6B",
    "messages": [
      {"role": "user", "content": "What is the capital of France?"}
    ]
  }'
```

#### 方法二：使用 pip/uv（Python 環境）

##### 步驟 1：安裝 uv（可選但推薦）

```bash
pip install --upgrade pip
pip install uv
```

##### 步驟 2：建立虛擬環境

```bash
uv venv --python 3.12
source .venv/bin/activate
```

##### 步驟 3：安裝 SGLang

```bash
## 安裝 stable 版本
uv pip install --prerelease=allow sglang

## 或使用 nightly 版本（包含最新功能）
uv pip install --prerelease=allow --index-strategy unsafe-best-match --extra-index-url https://docs.sglang.ai/whl/cu130/ sglang
```

##### 步驟 4：啟動服務器

```bash
## 替換 MODEL_PATH 為您的模型 ID
sglang serve Qwen/Qwen3-0.6B --host 0.0.0.0 --port 30000
```

等待看到訊息：`The server is fired up and ready to roll!`

##### 步驟 5：發送測試請求

```bash
curl http://localhost:30000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "Qwen/Qwen3-0.6B",
    "messages": [
      {"role": "user", "content": "What is the capital of France?"}
    ]
  }'
```

#### 方法三：從源碼編譯（開發環境）

##### 步驟 1：克隆代碼庫

```bash
git clone -b v0.5.21 https://github.com/sgl-project/sglang.git
cd sglang
```

##### 步驟 2：安裝

```bash
pip install --upgrade pip
pip install -e "python"
```

##### 步驟 3：啟動服務器

```bash
sglang serve Qwen/Qwen3-0.6B --host 0.0.0.0 --port 30000
```

#### 方法四：使用 Docker Compose

##### 步驟 1：複製配置文件

```bash
## 從 GitHub 下載 compose 文件
curl -o compose.yaml https://raw.githubusercontent.com/sgl-project/sglang/main/docker/compose.yaml
```

##### 步驟 2：啟動服務

```bash
docker compose up -d
```

#### 方法五：使用 SkyPilot（雲端部署）

##### 步驟 1：安裝 SkyPilot

```bash
pip install "skypilot[all]"
sky check
```

##### 步驟 2：建立部署文件

```yaml
## sglang.yaml
envs:
  HF_TOKEN: null

resources:
  image_id: docker:lmsysorg/sglang:latest
  accelerators: A100
  ports: 30000

run: |
  conda deactivate
  python3 -m sglang.launch_server \
    --model-path meta-llama/Llama-3.1-8B-Instruct \
    --host 0.0.0.0 \
    --port 30000
```

##### 步驟 3：部署

```bash
HF_TOKEN=<your_token> sky launch -c sglang --env HF_TOKEN sglang.yaml

## 獲取 API 端點
sky status --endpoint 30000 sglang
```

### 硬體支援清單

SGLang 支援的主流硬體平台包括：

- **NVIDIA GPU**：從入門的 RTX 30/40/50 系列，到專業級的 A100/H200/H800/H20，再到最新的 B200/B300/GB200/GB300，一應俱全
- **AMD GPU**：Instinct MI300X、MI325X、MI350X、MI355X 等
- **Google TPU**：v6e、v7
- **Intel**：Arc/Arc Pro B-Series GPU 和 Xeon CPU
- **Apple Silicon**：透過 Metal 和 MLX 在 Mac 上運行
- **華為昇騰**：A2、A3、950PR/DT NPU
- **Moore Threads**：MTT S5000 GPU

### 常見問題排錯

#### CUDA_HOME 環境變數未設定

如果遇到這個錯誤：`OSError: CUDA_HOME environment variable is not set`

解決方法：先設定 CUDA_HOME，再重新安裝

```bash
export CUDA_HOME="/usr/local/cuda"
## 如果 CUDA 安裝路徑不同，請自行調整
pip install -e "python"
```

#### FlashInfer 相容性問題

如果您用的是 sm75 或更早的硬體（例如 T4、A10、A100、L4、L40S、H100），可能會遇到 FlashInfer 的相容性問題。這時可以改用 Triton 和 PyTorch 後端：

```bash
sglang serve MODEL_PATH --attention-backend triton --sampling-backend pytorch
```

#### 重新安裝 FlashInfer

如果還是遇到問題，建議重新安裝 FlashInfer：

```bash
pip3 install --upgrade flashinfer-python --force-reinstall --no-deps
rm -rf ~/.cache/flashinfer
```

### Cookbook 與推薦模型

SGLang 提供官方 Cookbook，裡面有各種模型和硬體平台的實戰部署指南。以下是一些值得嘗試的熱門模型：

- **DeepSeek-V4.1-Flash**：稀疏注意力 MoE 架構，效能卓越
- **Qwen3.8-Flash-Next**：支援 262K 上下文長度
- **GLM-5.3-Flash**：多模態模型，同時支援文本、圖像和視頻處理
- **Kimi-K3**：擁有 2.8T 參數的強大模型
- **MiniMax-H3**：專精於視頻和音頻生成

#### 實戰資源

- 📚 **官方文檔**：https://docs.sglang.io/
- 🍳 **Cookbook 實戰指南**：https://cookbook.sglang.io/
- 📝 **技術博客**：https://lmsys.org/blog/

### 參考資源

- 📖 **官方文檔**：https://docs.sglang.io/
- 🍳 **Cookbook 實戰指南**：https://cookbook.sglang.io/
- 💻 **GitHub 倉庫**：https://github.com/sgl-project/sglang
- 💬 **Slack 社群**：https://slack.sglang.io/
- 📦 **PyPI**：https://pypi.org/project/sglang/
- 🐳 **Docker Hub**：https://hub.docker.com/r/lmsysorg/sglang

### 生態系統

SGLang 生態系統不斷成長，除了核心框架外，還整合了以下專案：

- **SGLang Diffusion**：圖像和視頻生成
- **SGLang Omni**：音頻模型服務，支援 TTS（語音合成）和 ASR（語音辨識）
- **SpecForge**：專為猜測解碼設計的草稿模型訓練工具
- **SMG**：部署和編排框架
- **Ray Serve**：整合部署方案
- **NVIDIA Dynamo**：後端支援

*本文檔整理自 SGLang 官方文檔和 GitHub 倉庫，最後更新：2026 年*

---

## 與主流推理引擎比較

### 三引擎技術路線圖對比

| 特性 | llama.cpp | vLLM | SGLang |
|------|-----------|------|--------|
| **主要設計目標** | 單用戶高效能、便攜性 | 高吞吐量、多用戶服務 | 通用模型服務（LLM/VLM/Diffusion） |
| **核心架構** | CPU/GPU 混合，離線優先 | PagedAttention + 持續批處理 | SGLang 解釋器 + 解耦 Prefill/Decode |
| **記憶體管理** | 簡單連續記憶體 | 分頁注意力（PagedAttention） | 圖狀記憶體 + 猜測解碼優化 |
| **硬體支援** | CPU/GPU 全平台（x86/ARM/NPU） | 主要 NVIDIA GPU | NVIDIA/AMD/TPU/Intel/Apple/華為昇騰 |
| **適合場景** | 輕量部署、邊緣設備 | 高併發服務、大規模推論 | 複雜代理、多模態、RL 訓練 |

### 效能比較（2026 年 Benchmark 摘要）

#### 1. 吞吐量（Throughput）

**vLLM 優勢領域**：
- 高併發場景下吞吐量顯著較高（vLLM 在高併發時吞吐量可達 llama.cpp 的 2-3 倍）
- 多用戶共享環境表現優異
- PagedAttention 有效減少記憶體碎片

**SGLang 優勢領域**：
- 單請求 TTFT（Time To First Token）表現更優（多步優化下 TTFT 比 vLLM 快 3 倍）
- ITL（Inter-Token Latency）穩定性更強
- MoE 模型支援更好

**llama.cpp**：
- 單請求效率佳，但吞吐量成長受限
- 適合單用戶或低併發場景

#### 2. 特殊模型類型支援

| 模型類型 | vLLM | SGLang | llama.cpp |
|----------|------|--------|-----------|
| **MoE 模型** | 良好 | ⭐ 優異 | 一般 |
| **量化模型（4-bit）** | 良好 | ⭐ 優異 | ⭐ 極佳 |
| **長上下文（>100K）** | 良好 | ⭐ 優異 | 一般 |
| **多模態（VLM）** | 一般 | ⭐ 優異 | 無支援 |
| **圖像生成（Diffusion）** | 無 | ⭐ 內建支援 | 無 |

#### 3. 啟動與部署

| 項目 | llama.cpp | vLLM | SGLang |
|------|-----------|------|--------|
| **安裝複雜度** | ⭐⭐⭐ 需編譯 | ⭐⭐ pip 安裝 | ⭐ pip/Docker 安裝 |
| **啟動速度** | ⭐⭐ 中等 | ⭐⭐ 中等 | ⭐⭐⭐ 快速 |
| **Docker 支援** | 需自建 | 有官方鏡像 | 有官方鏡像 |
| **雲端部署** | 較複雜 | 成熟 | 成熟（SkyPilot 支援） |

### 使用建議

#### 選擇 llama.cpp 當：
- ✅ 需要輕量級部署（<100MB 記憶體）
- ✅ 邊緣設備或離線環境
- ✅ 單用戶或低併發場景
- ✅ 需要跨平台便攜性（Windows/Linux/macOS）
- ✅ 大量量化模型部署（4-bit/5-bit）

#### 選擇 vLLM 當：
- ✅ 需要高吞吐量、高併發服務
- ✅ 多用戶共享環境
- ✅ 主要使用 NVIDIA GPU
- ✅ 需要成熟生態系統和工具链
- ✅ 企業級生產環境

#### 選擇 SGLang 當：
- ✅ 需要支援多模態、圖像生成
- ✅ 複雜代理工作負載（Agentic Workloads）
- ✅ RL 訓練或 RLHF 卷積
- ✅ MoE 模型或長上下文應用
- ✅ 需要跨平台硬體支援（AMD/TPU/昇騰）
- ✅ 需要標準 OpenAI API 介面

### 性能測試資源

- **官方 Benchmark**：https://github.com/sgl-project/sglang/tree/main/benchmark
- **ree2raz/inference-bench**：可重現的對決測試（vLLM vs SGLang vs llama.cpp）
- **Sothill Strix Halo Benchmark**：2026 年最新硬體測試
- **GPUwerk DGX Spark 指南**：GB10 平台部署建議

### 參考資料

1. [Performance Evaluation of LLM Inference Engines Thesis](https://hps.vi4io.org/_media/research/theses/yining_liu_performance_evaluation_of_llm_inference_engines.pdf)
2. [SGLang vs vLLM: Strix Halo Benchmarks 2026](https://www.soothill.io/blog/2026/08/10/sglang-vllm-llamacpp-evox3/)
3. [Inside the Serving Loop: vLLM vs SGLang Architecture](https://marcus-lau.com/writing/code/)
4. [vLLM or llama.cpp: Choosing the Right Engine](https://developers.redhat.com/articles/2025/09/30/vllm-or-llamacpp-choosing-right-llm-inference-engine-your-use-case)
5. [Benchmarking on Mixed Blackwell/Ada Cluster](https://pivotnews.ai/build/benchmarking-vllm-vs-sglang-vs-llama-cpp-on-a-mixed-blackwel)
6. [GPUwerk: Choosing Inference Engine Guide](https://gpuwerk.com/dgx-spark/guides/choosing-inference-engine-llama-cpp-vllm-sglang/)

---

*本文檔最後更新：2026 年 10 月*
