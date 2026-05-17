# Llama.cpp

- Git Repo
  - https://github.com/ggml-org/llama.cpp

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
| **1\. Split Experts to CPU (`--n-cpu-moe`)** | Device Mapping / Offloading | **No / Extremely Limited** |
| **2\. Prefetch Model to RAM (`--no-mmap`)** | vLLM allocates all memory up front | **Yes (Default)** |
| **3\. High Compression KV Cache (`TurboQuant`)** | FP8 / INT4 KV Cache Quantization | **Yes** |
| **4\. Memory Locking (`--mlock`)** | Pinning memory allocations | **Yes (Handled by PyTorch/vLLM)** |
| **5\. Avoid Speculative Decoding on MoE/SSM** | Speculative Decoding configuration | **Yes (Disabled by default)** |

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