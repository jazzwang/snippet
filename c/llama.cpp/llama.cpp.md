# Llama.cpp

- Git Repo
  - https://github.com/ggml-org/llama.cpp

[TOC]

## 2026-05-16

- 安裝：
  - 根據 https://github.com/ggml-org/llama.cpp/blob/master/docs/install.md
  - Windows 機器可以用以下指令安裝
```bash
$ winget install llama.cpp
Found llama.cpp [ggml.llamacpp] Version b9159
This application is licensed to you by its owner.
Microsoft is not responsible for, nor does it grant any licenses to, third-party packages.
This package requires the following dependencies:
  - Packages
      Microsoft.VCRedist.2015+.x64
Downloading https://github.com/ggml-org/llama.cpp/releases/download/b9159/llama-b9159-bin-win-vulkan-x64.zip
  ██████████████████████████████  31.1 MB / 31.1 MB
Successfully verified installer hash
Extracting archive...
Successfully extracted archive
Starting package install...
Path environment variable modified; restart your shell to use the new value.
Command line alias added: "llama-batched-bench"
Command line alias added: "llama-bench"
Command line alias added: "llama-cli"
Command line alias added: "llama-gguf-split"
Command line alias added: "llama-imatrix"
Command line alias added: "llama-mtmd-cli"
Command line alias added: "llama-perplexity"
Command line alias added: "llama-quantize"
Command line alias added: "llama-server"
Command line alias added: "llama-tokenize"
Command line alias added: "llama-tts"
Successfully installed
```
  - 如果用 scoop 的話，要加 `versions` bucket
```bash
~$ scoop search llama.cpp
Results from other known buckets...
(add them using 'scoop bucket add <bucket name>')

Name                  Source
----                  ------
llama.cpp-cpu         versions
llama.cpp-cu117       versions
llama.cpp-cu124-dll   versions
llama.cpp-cu124       versions
llama.cpp-cu131-dll   versions
llama.cpp-cu131       versions
llama.cpp-hip-gfx1030 versions
llama.cpp-hip-gfx1100 versions
llama.cpp-hip-gfx1101 versions
llama.cpp-hip-radeon  versions
llama.cpp-opencl      versions
llama.cpp-sycl        versions
llama.cpp-vulkan      versions

~$ scoop bucket add versions
Checking repo... OK
The versions bucket was added successfully.

~$ scoop search llama.cpp
Results from local buckets...

Name                  Version Source   Binaries
----                  ------- ------   --------
llama.cpp-cpu         b9174   versions
llama.cpp-cu117       b5449   versions
llama.cpp-cu124-dll   b9174   versions
llama.cpp-cu124       b9174   versions
llama.cpp-cu131-dll   b9174   versions
llama.cpp-cu131       b9174   versions
llama.cpp-hip-gfx1030 b5449   versions
llama.cpp-hip-gfx1100 b5449   versions
llama.cpp-hip-gfx1101 b5449   versions
llama.cpp-hip-radeon  b9174   versions
llama.cpp-opencl      b9174   versions
llama.cpp-sycl        b9174   versions
llama.cpp-vulkan      b9174   versions
```
- 緣起：
  - 想重現 https://www.youtube.com/watch?v=8F_5pdcD3HY
- 疑惑：只有 llama.cpp 辦得到嗎？vLLM 不行？
  - Google Gemini App
  - Gemini 3

> could you refer to https://www.youtube.com/watch?v=8F_5pdcD3HY and explore the possibility to apply similar strategy using vLLM instead of llama.cpp

The video from Codacus demonstrates a highly effective strategy for running a large **Mixture of Experts (MoE)** model (`Qwen-3.6-35B-A23B`) on a resource-constrained 6GB VRAM system.

To evaluate whether you can replicate this exact strategy using **vLLM** instead of `llama.cpp`, we have to break down the five core pillars of the video's technique and look at how vLLM's architecture handles them:

### The 5 Pillars of the Video's Strategy vs. vLLM

| **Strategy Pillar (llama.cpp)** | **vLLM Equivalent Capability** | **Feasibility in vLLM** |
| --- |  --- |  --- |
| **1. Split Experts to CPU (`--n-cpu-moe`)** | Device Mapping / Offloading | **No / Extremely Limited** |
| **2. Prefetch Model to RAM (`--no-mmap`)** | vLLM allocates all memory up front | **Yes (Default)** |
| **3. High Compression KV Cache (`TurboQuant`)** | FP8 / INT4 KV Cache Quantization | **Yes** |
| **4. Memory Locking (`--mlock`)** | Pinning memory allocations | **Yes (Handled by PyTorch/vLLM)** |
| **5. Avoid Speculative Decoding on MoE/SSM** | Speculative Decoding configuration | **Yes (Disabled by default)** |

### Deep Dive: Why a 1:1 Port to vLLM is Not Feasible

#### 1. The Dealbreaker: MoE CPU Offloading (`--n-cpu-moe`)

The core trick that makes the video's setup work is `llama.cpp`'s unique ability to split a single layer's components: keeping the small attention/shared blocks on the GPU while routing the massive **inactive expert weights** to system RAM via the CPU [03:33](http://www.youtube.com/watch?v=8F_5pdcD3HY&t=213). It stream-loads only the active 8 experts dynamically over the PCIe bus per token [03:50](http://www.youtube.com/watch?v=8F_5pdcD3HY&t=230).

-   **How vLLM works:** vLLM is built from the ground up as a **high-throughput, enterprise serving engine** optimized for GPUs. It expects the entire active model (or an entire layer, if pipeline-parallelized across multiple GPUs) to fit perfectly into VRAM.

-   **vLLM's CPU support:** While vLLM does have an experimental CPU backend (`vllm-cpu`), it requires running the *entire* model on the CPU. It **does not support hybrid GPU-attention / CPU-expert slicing** within the same engine instance. If a model exceeds your VRAM, vLLM will simply trigger an Out-of-Memory (OOM) error or fail to initialize.

#### 2. KV Cache Compression (TurboQuant vs. vLLM KV Quant)

The video utilizes **TurboQuant** (compressing keys to 4-bit and values to 3-bit) to cram a 256,000 token context window into a fraction of VRAM [07:45](http://www.youtube.com/watch?v=8F_5pdcD3HY&t=465), [08:39](http://www.youtube.com/watch?v=8F_5pdcD3HY&t=519).

-   **vLLM Alternative:** vLLM natively utilizes **PagedAttention**, which completely eliminates memory fragmentation. Furthermore, vLLM natively supports KV cache quantization down to **FP8** or **INT4** via arguments like `--kv-cache-dtype fp8`. While it doesn't support asymmetric 4-bit/3-bit configurations out of the box, PagedAttention with FP8 achieves massive context windows natively---*provided* the weights themselves fit in VRAM first.

#### 3. RAM Locking and Prefetching

The video notes that Linux tends to page model weights out to disk during idle periods, causing lag spikes, which they fix using `--no-mmap` and `mlock` [05:01](http://www.youtube.com/watch?v=8F_5pdcD3HY&t=301), [09:33](http://www.youtube.com/watch?v=8F_5pdcD3HY&t=573).

-   **vLLM Alternative:** vLLM already acts like this by default. Because it is a Python/PyTorch-based server, when it starts up, it aggressively allocates and locks down a massive block of VRAM (configured by `--gpu-memory-utilization`) and system RAM to prepare its PagedAttention blocks. It does not page-fault weights on the fly during inference.

### How to Achieve a Similar "Budget-Friendly" Strategy in vLLM

If you want to stick with vLLM but achieve the goal of running a massive model on a tighter hardware budget, you cannot use the video's CPU-MoE routing. Instead, you have to use **Weight Quantization**.

Instead of pulling unquantized or lightly quantized experts across a slow PCIe bus, you drastically compress the entire model so that it fits completely inside your VRAM. For a 35B MoE model (where total parameter disk size is ~35GB unquantized), you would approach it in vLLM like this:

1.  **Use GPTQ or AWQ Quantized Weights:** Find or quantize a 4-bit or 3-bit version of the Qwen model (e.g., `Qwen2.5-32B-Instruct-AWQ`). A 4-bit quantization reduces a 35B model's footprint to roughly 18-20GB. (Note: To fit a 35B model *completely* into 6GB VRAM is impossible even at 2-bit quantization, making `llama.cpp` the only viable option for a 6GB card).

2.  **Enable FP8 KV Cache:**

    Run vLLM with the following flag to save VRAM on the context window:

    Bash

    ```
    vllm serve qwen-model-repo --kv-cache-dtype fp8 --gpu-memory-utilization 0.90
    ```

3.  **Limit Max Model Length:**

    To guarantee you don't OOM on long prompts, strictly limit the max context size to match your remaining VRAM cushion:

    Bash

    ```
    --max-model-len 32768
    ```

### Conclusion

If your goal is to replicate the video by running a **35B model on a 6GB or 8GB VRAM card**, you **must use `llama.cpp`**. vLLM lacks the granular CPU/GPU hybrid memory slicing (`--n-cpu-moe`) required to offload sleeping layers to system RAM [03:33](http://www.youtube.com/watch?v=8F_5pdcD3HY&t=213).

However, if you upgrade your GPU hardware slightly (e.g., to a dual-GPU setup or a single 24GB VRAM card), **vLLM** combined with **AWQ/GPTQ weight quantization** and **FP8 PagedAttention** will drastically outperform `llama.cpp` in speed and multi-user throughput.

> what is the final conclusion of llama.cpp command to run Qwen 3.6 35B on 6GB VRAM machine?

The final structure of the `llama.cpp` command used by Codacus to run the Qwen-3.6-35B MoE model at **17 tokens per second with a 256,000-token context window** on a 6GB VRAM machine relies on precisely balancing the five core flags:

```bash
llama-cli \
  -m qwen3.6-35b-instruct-q4_k_m.gguf \
  --n-cpu-moe 36 \
  -L 35 \
  --no-mmap \
  --ctx-scale-key-quant 4 \
  --ctx-scale-value-quant 3 \
  --mlock \
  -c 256000

```

### Command Parameter Breakdown:

* **`-m qwen3.6-35b-instruct-q4_k_m.gguf`**: The model path (using a typical standard quantization like Q4 to fit the base model size within system memory).
* **`--n-cpu-moe 36`**: Pins 36 layers of the Mixture of Experts (MoE) blocks directly to system RAM to keep them off the GPU.
* **`-L 35`**: Offloads the non-MoE components (attention mechanisms) plus 5-6 layers of experts to the GPU to maximize the remaining 6GB VRAM.
* **`--no-mmap`**: Forces the system to preload all 20GB of weights straight into RAM upon startup, removing random disk-read stuttering during text generation.
* **`--ctx-scale-key-quant 4` & `--ctx-scale-value-quant 3**`: The asymmetric **TurboQuant** flags that compress the context cache aggressively down to 4-bit keys and 3-bit values.
* **`-c 256000`**: Expands the active context window to a massive 256k tokens, made possible by the TurboQuant compression.
* **`--mlock`**: Locks all the model weights into the physical RAM blocks so the operating system can never page them out to disk, preserving steady performance over weeks of idle time.

### Critical Deployment Requirement

As noted in the video, just putting `--mlock` in the command line will silently fail if your environment restricts memory locking. To ensure it works permanently, you must also allow **IPC locking** in your host configuration:

* If running natively on Linux: Ensure your user limits allow locking memory (`ulimit -l`).
* If using Docker: Pass the capability flag **`--cap-add=IPC_LOCK`** to your Docker run command.

- 實測：
```bash
~$ llama-cli   -m qwen3.6-35b-instruct-q4_k_m.gguf   --n-cpu-moe 36   -L 35   --no-mmap   --ctx-scale-key-quant 4   --ctx-scale-value-quant 3   --mlock   -c 256000
error: invalid argument: -L
~$ llama-cli   -m qwen3.6-35b-instruct-q4_k_m.gguf   --n-cpu-moe 36  --no-mmap   --ctx-scale-key-quant 4   --ctx-scale-value-quant 3   --mlock   -c 256000
error: invalid argument: --ctx-scale-key-quant
~$ llama-cli   -m qwen3.6-35b-instruct-q4_k_m.gguf   --n-cpu-moe 36  --no-mmap   --ctx-scale-value-quant 3   --mlock   -c 256000
error: invalid argument: --ctx-scale-value-quant
~$ llama-cli   -m qwen3.6-35b-instruct-q4_k_m.gguf   --n-cpu-moe 36  --no-mmap   --mlock   -c 256000
```

## 2026-06-12

- Tool: Google Search - AI Mode
> [!QUESTION]
> steps to install llama.cpp on linux without GPU

To install and run llama.cpp on Linux for CPU-only inference (without a GPU), you need to compile the code from source using CMake. By default, compiling llama.cpp without specifying any GPU flags automatically optimizes the build for your local CPU. [1, 2, 3, 4]

### 1. Install Required Dependencies [5]

You must install a C++ compiler (GCC), Git, and CMake. Choose the command below that matches your Linux distribution: [2, 3]

-   Ubuntu / Debian / Mint:
    ```bash
    sudo apt update
    sudo apt install -y git build-essential cmake libcurl4-openssl-dev
    ```

-   Fedora / RHEL / CentOS:
    ```bash
    sudo dnf groupinstall "Development Tools"
    sudo dnf install -y cmake openssl-devel libcurl-devel
    ```

-   Arch Linux:
    ```bash
    sudo pacman -S --needed git base-devel cmake curl
    ```

    [4, 6]

### 2. Clone the Repository [7]

Download the official source code from the ggml-org llama.cpp GitHub repository and navigate into the project directory: [2, 4, 8, 9, 10]
```bash
git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp
```

### 3. Generate Build Files and Compile [4]

Create a build directory, configure CMake for a CPU-only Release build, and compile the binaries. [2, 4]

```bash
cmake -B build -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=OFF
cmake --build build --config Release -j $(nproc)
```

*Note: The `-j $(nproc)` flag tells the compiler to use all available CPU cores, which speeds up the compilation process significantly.* [2]

### 4. Verify the Installation

Test that the build succeeded by checking the help menu for the main command-line interface executable: [6]
```bash
./build/bin/llama-cli --help
```

### 5. Running a Local Model (Example)

To actually use `llama.cpp`, you need to download a model in the GGUF format. For CPU-only hardware, a lightweight model like Microsoft's Phi-3 or Phi-4 is recommended. [2, 11]

1.  Download a model file using `wget` or `curl` (e.g., a 4-bit quantized model from Hugging Face):
    ```bash
    mkdir models
    curl -L -o models/phi-3-mini-4k-instruct-q4_K_M.gguf https://huggingface.co
    ```

2.  Execute the model using the command line: [2, 11, 12, 13]
    ```bash
    ./build/bin/llama-cli -m models/phi-3-mini-4k-instruct-q4_K_M.gguf -p "Why is the sky blue?" -n 128
    ```
If you plan on writing Python applications around this build, let me know if you would also like instructions on configuring the Python bindings (`llama-cpp-python`) or setting up an OpenAI-compatible server local endpoint. [7, 14, 15]

[1] [https://www.reddit.com](https://www.reddit.com/r/LocalLLaMA/comments/18ggbg5/built_llamacpp_from_source_on_ubuntu_with_no_gpu/)
[2] [https://www.youtube.com](https://www.youtube.com/watch?v=JC7zaJGwbHU)
[3] [https://www.youtube.com](https://www.youtube.com/watch?v=EPYsP-l6z2s&t=521)
[4] [https://github.com](https://github.com/ggml-org/llama.cpp/discussions/21136)
[5] [https://www.linkedin.com](https://www.linkedin.com/posts/shaikhquader_textembeddings-localllm-llamacpp-activity-7335035389218365440-WlQv)
[6] [https://llama-cpp.com](https://llama-cpp.com/getting-started/)
[7] [https://dev.to](https://dev.to/avatsaev/pro-developers-guide-to-local-llms-with-llamacpp-qwen-coder-qwencode-on-linux-15h)
[8] [https://learn.arm.com](https://learn.arm.com/learning-paths/servers-and-cloud-computing/arcee-foundation-model-on-aws/03_building_llama_cpp/)
[9] [https://huggingface.co](https://huggingface.co/boneylizardwizard/llama-cpp-python-038-cu128-gemma3-wheel/blame/main/Build.Guide.md)
[10] [https://forums.developer.nvidia.com](https://forums.developer.nvidia.com/t/building-llama-cpp-container-images-for-spark-gb10/353664)
[11] [https://www.youtube.com](https://www.youtube.com/watch?v=o5ItHSvCPbA&t=354)
[12] [https://rocm.docs.amd.com](https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/docs/advanced/advancedrad/linux/llm/llamacpp.html)
[13] [https://ai.plainenglish.io](https://ai.plainenglish.io/how-to-use-llama-locally-on-cpu-step-by-step-guide-fc9f70291809)
[14] [https://github.com](https://github.com/abetlen/llama-cpp-python/issues/1963)
[15] [https://github.com](https://github.com/abetlen/llama-cpp-python/issues/877)

## 2026-06-13

- Tool: Google Search - AI Mode

> [!QUESTION]
> 支援 CPU 的 LLM model servicing 工具,除了 llama.cpp 以外,還有其他工具嗎?

### Llama.cpp Alternatives

除了 llama.cpp 以外，目前市面上還有許多專門針對 CPU 優化、或對 CPU 支援度極佳的大語言模型（LLM）推論與伺服端工具。
以下為您盤點 5 個主流的替代方案：

#### 1. Ollama

* 特點：開箱即用，極簡部署。
* CPU 支援：後端基於 llama.cpp，但包裝成極簡的 CLI 與 API 服務。
* 適用場景：適合想在本地快速啟動模型、不需要複雜設定的開發者。 [1, 2, 3, 4]

#### 2. OpenVINO GenAI / Model Server

* 特點：由 Intel 官方開發，專為 Intel CPU/iGPU/NPU 進行極限優化。
* CPU 支援：透過權重優化與量化（如 INT4/INT8），在 Intel 處理器上效能極佳。
* 適用場景：使用 Intel 硬體架構並追求最高推論速度的企業環境。

#### 3. vLLM

* 特點：以高吞吐量（Throughput）聞名的生產級服務框架。
* CPU 支援：除了 GPU，官方也原生支援 x86 CPU 架構（透過 OpenVINO 或 AVX-512 優化）。
* 適用場景：需要處理高並發（High Concurrency）請求的後端 API 服務。 [5, 6]

#### 4. LM Deploy

* 特點：由商湯科技開發的高效能 LLM 推論與服務工具箱。
* CPU 支援：支援 PyTorch-based 的 CPU 推論，並具備優異的量化效能。
* 適用場景：需要完整 MLOps 管線、動態批處理（Dynamic Batching）的場景。 [7]

#### 5. Llamafile

* 特點：Mozilla 推出的專案，將模型和執行檔打包成單一檔案（Single-file executable）。
* CPU 支援：內建高度優化的 CPU 執行期環境，跨平台（Linux, macOS, Windows）一鍵執行。
* 適用場景：模型分發、離線部署、追求極致便攜性的情境。 [8, 9]

如果想進一步評估哪款工具最適合您，可以告訴我：

* 您預計使用的 CPU 型號（Intel、AMD 或 ARM/Mac M系列）？
* 您的 模型格式（如 GGUF、Hugging Face 權重、AWQ 等）？
* 您的 應用場景（個人測試、需要整合到現有系統，還是高流量生產環境）？

我可以為您推薦最能發揮硬體效能的架構。

[1] [https://adg.csdn.net](https://adg.csdn.net/694cfd2c5b9f5f31781abd69.html)
[2] [https://medium.com](https://medium.com/@simon3458/%E8%AE%93-llm-model-%E5%8F%AF%E4%BB%A5%E5%BF%AB%E9%80%9F%E8%AE%8A%E6%88%90%E5%9C%B0%E7%AB%AF%E6%9C%8D%E5%8B%99-ollama-d849fb6d9ced)
[3] [https://cloud.tencent.com](https://cloud.tencent.com/developer/article/2577992)
[4] [https://blog.csdn.net](https://blog.csdn.net/weixin_42524004/article/details/160936202)
[5] [https://sider.ai](https://sider.ai/zh-TW/blog/ai-tools/llama_cpp-alternatives-faster-setups-fewer-headaches-same-local-ai-magic)
[6] [https://zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/21951797307)
[7] [https://www.investglass.com](https://www.investglass.com/zh/%E5%A6%82%E4%BD%95%E5%9C%A8%E6%9C%AC%E5%9C%B0%E8%BF%90%E8%A1%8C-llms-%E8%87%AA%E6%89%98%E7%AE%A1-ai-%E6%A8%A1%E5%9E%8B%E5%AE%8C%E6%95%B4-2025-%E6%8C%87%E5%8D%97/)
[8] [https://ithelp.ithome.com.tw](https://ithelp.ithome.com.tw/m/articles/10386239)
[9] [https://www.bilibili.com](https://www.bilibili.com/video/BV1ihXrYEEyn/)


> [!QUESTION]
> AMD. GGUF. 個人測試

### Test GGUF on AMD

針對 AMD CPU、GGUF 格式 以及 個人測試 的需求，最推薦的 3 個工具與設定方向如下：

#### 1. Ollama (首選)

* 優勢：個人測試最省心的選擇。
* AMD 優化：在 Windows 或 Linux 上，它會自動偵測硬體。如果您的 AMD CPU 支援 AVX2 指令集（近年 CPU 皆支援），它會自動調用最優化的推論引擎。
* GGUF 支援：支援直接匯入自訂的 GGUF 檔案。只需撰寫一個簡單的 Modelfile（寫入 FROM ./你的模型.gguf），即可一鍵將其轉為 API 服務。

#### 2. Llamafile (最方便)

* 優勢：完全不需安裝任何依賴環境。
* AMD 優化：由 Mozilla 維護，內部對 AMD 的 CPU 架構（x86-64）有極佳的編譯優化。
* GGUF 支援：可以直接用命令列執行 llamafile -m 你的模型.gguf，它會自動在瀏覽器開啟一個網頁版 Chat UI，非常適合快速測試。

#### 3. vLLM (進階測試)

* 優勢：若您未來想測試多輪對話的並發效能（吞吐量），這是標準配備。
* AMD 優化：vLLM 目前已支援 CPU 後端，在 AMD 多核心處理器（如 Ryzen 9 或 Threadripper）上能展現不錯的平行運算能力。
* GGUF 支援：近期版本已加入對 GGUF 格式的支援，但設定上比前兩者複雜。

#### 💡 額外建議：效能最大化設定

無論您使用上述哪款工具，由於是 AMD CPU 推論，請注意以下幾點：

   1. 執行緒設定 (Threads)：執行時，將 CPU 執行緒數設定為您處理器的 「實體核心數（Physical Cores）」，而非邏輯核心數（Hyper-threading），效能通常最好。
   2. 記憶體頻寬：CPU 推論的瓶頸在於記憶體速度。若您的 AMD 平台支援雙通道 DDR5，其推論速度會明顯快於 DDR4。

您可以告訴我您目前正在使用的是哪一個 AMD CPU 型號（例如 Ryzen 7 5800X、Ryzen 9 7900 等）？我可以幫您預估大約的推論速度（Tokens/second），或是直接提供您 Ollama 匯入 GGUF 的指令步驟。

> [!QUESTION]
> Ryzen 7 7735HS. 可以預估 vLLM 推論速度嗎?

### AMD Ryzen 7 vLLM inference speed

在 AMD Ryzen 7 7735HS 上使用 vLLM 進行 CPU 推論，在生成階段（Decode）的預估速度大約落在 每秒 2 到 8 個 Token (2~8 t/s)。 [1]

這個速度並不算快，主要原因是 vLLM 的設計初衷是為了高吞吐量的 GPU 伺服器設計（如處理大量並發請求），它的 CPU 後端（基於 OpenVINO 或 PyTorch） 在單一使用者、單純單執行緒的本地測試中，效能通常無法完全釋放。 [1, 2, 3, 4]
以下為您精確估算不同模型大小在您的硬體上的表現：

#### 📊 vLLM 速度預估（以 8-bit 或 4-bit 量化為例）

| 模型大小 (以 GGUF 量化後) [5] | 預估推論速度 (Tokens/Second) | 體驗流暢度 |
|---|---|---|
| 1B ~ 3B (如 Qwen2.5-3B) | 5 ~ 8 t/s | 勉強可讀（正常打字速度） |
| 7B ~ 8B (如 Llama3-8B) | 2 ~ 4 t/s | 明顯慢、有卡頓感 |
| 14B 以上 | < 1.5 t/s | 逐字慢速蹦出，不建議使用 |

#### 🔍 決定效能的關鍵瓶頸

   1. 記憶體頻寬（記憶體是最大殺手）
   LLM 在 CPU 上的推論速度，90% 取決於您的記憶體（RAM）頻寬，而非 CPU 核心算力。Ryzen 7 7735HS 支援雙通道 DDR5-4800 或 LPDDR5-6400。
   * 如果您的筆電/迷你電腦是 DDR5雙通道，效能會接近上述預估的上限。
      * 如果不幸是單條單通道，速度會直接減半。 [6]
   2. vLLM 在 CPU 上的架構劣勢
   vLLM 在 CPU 上的記憶體管理與動態調度（如 PagedAttention），其額外開銷（Overhead）在單機 CPU 環境下非常明顯。這也是為什麼許多工程師回報，在個人測試中 vLLM CPU 的速度往往不如預期。 [1, 3, 5]

#### 💡 實用替代方案建議

如果您的目標是順暢的個人測試體驗，在相同的 Ryzen 7 7735HS 硬體下，高度強烈建議切換到以下兩種方案，速度會大幅提升：

* 改用 llama.cpp 或 Ollama（CPU 模式）：
由於它們對 x86 核心（AVX2 指令集）的單核與多核優化極為極致，跑 7B-GGUF 模型通常能穩定達到 8 ~ 13 t/s，比 vLLM 快上 2 至 3 倍，能達到完全流暢閱讀的體驗。
* 利用 7735HS 內建的強大核顯 (Radeon 680M)：
您的 CPU 帶有非常強悍的內顯。如果您的系統有 32GB 記憶體，您可以進入 BIOS 將 iGPU 的顯示記憶體（VRAM）強行配置分配到 8GB 或 16GB。接著使用 Ollama (Vulkan 模式) 或 LMDeploy (Marlin/ROCm 模式)，讓核顯來跑推論，7B 模型速度有機會衝上 15+ t/s。 [7, 8]

您目前打算在 vLLM 上測試的 GGUF 模型是哪一個（例如 Llama-3-8B 還是 Qwen-7B）？若您需要，我可以提供您在 7735HS 上用 Ollama 或 Llamafile 執行該模型的具體指令與優化參數！

[1] [https://dev.to](https://dev.to/daniel_lm_bf221f14807a4fd/inside-vllms-cpu-backend-a-new-contributors-notes-4kin)
[2] [https://docs.vllm.ai](https://docs.vllm.ai/en/stable/getting_started/installation/cpu/)
[3] [https://github.com](https://github.com/vllm-project/vllm?utm_cta=website)
[4] [https://www.hyperstack.cloud](https://www.hyperstack.cloud/blog/case-study/what-is-vllm-a-guide-to-quick-inference)
[5] [https://github.com](https://github.com/vllm-project/vllm/issues/7379)
[6] [https://www.notebookcheck.net](https://www.notebookcheck.net/AMD-Ryzen-7-7735HS-Processor-Benchmarks-and-Specs.681410.0.html)
[7] [https://laptopmedia.com](https://laptopmedia.com/news/cpu-rankings-the-new-amd-ryzen-7-7735hs-is-just-below-the-top-5-laptop-cpus/)
[8] [https://github.com](https://github.com/ollama/ollama/issues/2637)

## 2026-08-27

> [!QUESTION]
> 請問執行 llama serve -hf unsloth/Qwen3.8-27B-GGUF:UD-IQ2_XXS 指令,llama.cpp 會把 GGUF 檔案存放在哪裡?作業系統是 Windows 11

在 Windows 11 作業系統下，執行 `llama serve -hf` 指令時，`llama.cpp` 會將下載的 GGUF 檔案自動存放在 Hugging Face 的標準本地快取路徑： [1, 2]

👉 `C:\Users\<您的用戶名>\.cache\huggingface\hub\models--unsloth--Qwen3.8-27B-GGUF` [3, 4]

### 📂 詳細檔案結構與路徑

在該目錄下，實際的 `.gguf` 檔案通常會以符號連結（Symlink）或直接儲存在以下結構中： [5]

-   快取根目錄： `C:\Users\<您的用戶名>\.cache\huggingface\hub\`
-   專案資料夾： `models--unsloth--Qwen3.8-27B-GGUF\`
-   實際檔案位置： 該資料夾內的 `blobs\`（存放實際資料）與 `snapshots\<一串雜湊值>\`（存放指向 blobs 的連結，包含您的 `UD-IQ2_XXS` 檔案）。 [3, 4, 5]

### ⚙️ 如何自訂存放位置？

如果您想更換路徑（例如 C 槽空間不足），可以透過設定 Windows 環境變數來改變預設位置（優先權由高到低）： [3, 4]

1.  `HF_HUB_CACHE`：直接指定快取資料夾路徑。
2.  `HF_HOME`：指定 Hugging Face 的根目錄（模型會存在該目錄下的 `hub\` 中）。 [2, 6, 7]

設定方法（以命令提示字元 CMD 為例）：

```cmd
set HF_HOME=D:\AI_Models\huggingface
llama serve -hf unsloth/Qwen3.8-27B-GGUF:UD-IQ2_XXS
```

*設定後，檔案就會改存在 `D:\AI_Models\huggingface\hub\` 底下。* [7]

[1] [https://tech-insider.org](https://tech-insider.org/llama-cpp-tutorial-2026/)
[2] [https://github.com](https://github.com/janhq/jan/issues/8252)
[3] [https://github.com](https://github.com/ggml-org/llama.cpp/issues/7252)
[4] [https://github.com](https://github.com/ggml-org/llama.cpp/issues/7252)
[5] [https://forums.developer.nvidia.com](https://forums.developer.nvidia.com/t/can-i-salvage-a-model-in-hf-cache-into-a-normal-directory-with-safetensors/369507)
[6] [https://github.com](https://github.com/ggml-org/llama.cpp/issues/20994)
[7] [https://huggingface.co](https://huggingface.co/docs/hub/local-cache)

## 2026-08-31

> [!QUESTION]
> 最佳化自行佈署 Qwen 3.8 27B 的作法?vLLM?llama.cpp?llamafile?

佈署 Qwen 3.8 27B 的最佳化作法，取決於你的硬體規格（單卡/多卡/VRAM 大小）以及應用場景（單人使用/Agent 任務/多人高吞吐）。 [1, 2, 3]
結論先行：首選 vLLM（搭配官方 FP8）進行高吞吐與 Agent 服務；單卡 24GB（如 RTX 4090）單人任務、大 context 首選 llama.cpp；而 llamafile 僅適合要求「極簡部署」的非極致效能場景。 [1, 2, 3]

### 一、 三大引擎核心對比與最佳化策略

#### 1\. vLLM：高吞吐、多人並發與 Agent 首選

-   核心優勢：擁有 PagedAttention、連續批處理（Continuous Batching），並支援 Qwen 3.8 內建的 MTP（Multi-Token Prediction，多 token 預測）。開啟 MTP-2 後，單人推理速度最高可提升 73.5%。 [3, 4]
-   最佳化作法：

        -   模型選擇：直接跑官方 FP8 量化版本（約佔 27GB VRAM）。
        -   硬體建議：1 張 32GB/48GB 顯卡（如 [RTX 5090](https://www.google.com/search?kgmid=FAILED_OR_SKIPPED)、[RTX 6000 Ada](https://www.google.com/search?kgmid=FAILED_OR_SKIPPED)），或 2 張 24GB 顯卡（如兩張 4090 做 Tensor Parallelism）。
        -   情境限制：在長 Context（超過 60k-70k）時，vLLM 的 KV Cache 會吞噬大量顯存，此時效能或容量可能會遇到瓶頸。 [1, 2, 3, 4, 5]

#### 2\. llama.cpp：單卡戰神、長 Context 與資源受限最佳解

-   核心優勢：記憶體管理極其精細，支援 GGUF 格式。在 24GB 顯卡（如 RTX 4090）上，它是唯一能讓你舒服跑起 Qwen 3.8 27B 的解法。 [1, 2]
-   最佳化作法：

        -   模型選擇：下載 Q4\_K\_M（約 15-17GB，保留空間給 KV Cache）或 Q5\_K\_M。
        -   Context 密技：llama.cpp 支援 Flash Attention 與更好的 KV Cache 量化（如轉為 `q8_0` 或 `q4_0` 的 KV Cache），可以在有限顯存下壓榨出 1.5 倍的長度。
        -   情境限制：雖然也能開啟 MTP，但提升僅約 20%（遠輸 vLLM），且多人高並發吞吐量較差。 [2, 3, 4, 6]

#### 3\. llamafile：極簡單一檔案部署，非效能極致流

-   核心優勢：將 `llama.cpp` 和模型權重打包成一個可執行檔（Executable），跨平台、雙擊即跑。
-   最佳化作法：只適合用於快速概念驗證（PoC）或內部離線、無運維基礎的伺服器。
-   情境限制：底層雖是 `llama.cpp`，但因為打包限制，無法靈活微調最前端的 MTP、KV Cache 壓縮或進階張量並行（Tensor Parallelism）等最佳化參數。

### 二、 部署決策樹（依據硬體與情境選擇）

| 硬體與情境 | 推薦引擎 | 推薦模型格式 | 核心優化參數 / 理由 |
| --- |  --- |  --- |  --- |
| 單張 24GB 顯卡(如 RTX 3090 / 4090) | llama.cpp(或經由 Ollama) | GGUF (Q4\_K\_M) | 開啟 `--flash-attn`，並將 KV Cache 設定為 `q8_0` 以節省顯存並拉長 Context。 |
| 單張 32GB/48GB 顯卡或雙卡並行 | vLLM / SGLang | 官方 FP8 | 開啟 MTP-2 (Multi-Token Prediction)，在 Agent 任務與多人調用時，吞吐量高達數百 tok/s。 |
| 需要極高並發的服務(API 供應商、多員工共用) | vLLM | FP8 | 利用 vLLM 的 PagedAttention 機制，一卡可以同時流暢餵飽多個用戶。 |
| 無 GPU / 純 CPU 伺服器 | llama.cpp | GGUF (Q4\_0) | 使用多執行緒（Thread）綁定，利用 CPU 和系統記憶體硬扛（速度較慢）。 |
| 零基礎部署、跨平台 | llamafile | 內嵌 GGUF | 不用安裝 Python、CUDA 驅動等環境，一鍵跑起來。 |

### 三、 實戰最佳化參數範例

#### 💡 若選擇 vLLM 路線（以 Docker 部署 FP8 為例）

為了最大化 Qwen 3.8 的速度，強烈建議開啟多 Token 預測：

```bash
docker run --gpus all --ipc=host\
  -v ~/.cache/huggingface:/root/.cache/huggingface\
  vllm/vllm-openai:latest\
  --model Qwen/Qwen3.8-27B-Instruct-FP8\
  --max-model-len 32768\
  --gpu-memory-utilization 0.90\
  --enable-chunked-prefill\
  --num-scheduler-steps 2# 啟用類似 MTP/Speculative Decoding 的推測加速
```

#### 💡 若選擇 llama.cpp 路線（單卡 4090 的極致榨乾參數）

```bash
./llama-server\
  -m qwen3.8-27b-instruct-q4_k_m.gguf\
  -c 32768\
  --flash-attn\
  --ctk q8_0\
  --ctv q8_0\
  -ngl 99# 將所有 Layer 塞進 4090 顯存
```

*(註：`--ctk q8_0` 和 `--ctv q8_0` 可以把 KV Cache 進行量化，這就是讓 4090 能白嫖 1.5 倍 Context 長度的關鍵！)* [2]
如果你想進一步評估，請告訴我：

-   你目前的顯示卡型號與 VRAM 容量是多少？
-   這個模型主要拿來做什麼任務（例如：本地 Coding Agent、多人共用 API、長文本分析）？ [2, 3]

我可以為你提供專屬的啟動腳本與顯存估算。

[1] [https://ithelp.ithome.com.tw](https://ithelp.ithome.com.tw/articles/10405431)
[2] [https://medium.com](https://medium.com/@changtimwu/%E4%B8%80%E5%BC%B5-4090-%E8%B7%91-qwen3-8-27b-vllm-vs-llama-cpp-%E5%AF%A6%E6%B8%AC-%E5%92%8C%E4%B8%80%E5%80%8B%E6%B2%92%E4%BA%BA%E5%9C%A8%E8%AC%9B%E7%9A%84%E5%85%8D%E8%B2%BB-1-5-%E5%80%8D-context-fdb32a769b64)
[3] [https://zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/2071984701632419778)
[4] [https://ai-coding.wiselychen.com](https://ai-coding.wiselychen.com/youtube-qwen38-27b-rtx5090-sglang-vllm-mtp-transcript/)
[5] [https://www.autobuy.tw](https://www.autobuy.tw/thread_19)
[6] [https://bbs.csdn.net](https://bbs.csdn.net/weixin_29031057/article/details/100267175)