# vllm

> A high-throughput and memory-efficient inference and serving engine for LLMs

- Git Repo
  - https://github.com/vllm-project/vllm
- Document
  - https://docs.vllm.ai/en/latest/

## 2025-03-21

### Install 安裝

- ( 2025-03-21 00:15:00 )
- 有鑑於 aider 版本造成的 ollama 相容性問題，這裡試著用類似的方式安裝 vllm
- 參考：https://docs.vllm.ai/en/latest/getting_started/quickstart.html
```bash
jazzw@JazzBook:~/git/snippet/py/vllm$ uv tool install --force --python python3.12 vllm@latest
   Building vllm==0.8.1
⠴ Preparing packages... (104/113)
transformers ------------------------------ 7.16 MiB/9.51 MiB            <-------------- PS. 會裝 transformers
numpy      ------------------------------ 7.21 MiB/14.80 MiB
ray        ------------------------------ 7.31 MiB/24.38 MiB
llvmlite   ------------------------------ 7.30 MiB/26.81 MiB
opencv-python-headless ------------------------------ 7.23 MiB/37.58 MiB
scipy      ------------------------------ 7.26 MiB/39.05 MiB
cupy-cuda12x ------------------------------ 7.20 MiB/78.26 MiB
torch      ------------------------------ 7.29 MiB/194.66 MiB
```
- ( 2025-03-21 00:29:02 )
- 檢查 `vllm` 指令
```bash
jazzw@JazzBook:~/git/snippet/py/vllm$ which vllm
/c/Users/jazzw/.local/bin/vllm
jazzw@JazzBook:~/git/snippet/py/vllm$ vllm serve -h
INFO 03-21 00:33:17 [__init__.py:256] Automatically detected platform cuda.
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\jazzw\.local\bin\vllm.exe\__main__.py", line 4, in <module>
  File "C:\Users\jazzw\AppData\Roaming\uv\tools\vllm\Lib\site-packages\vllm\__init__.py", line 11, in <module>
    from vllm.engine.arg_utils import AsyncEngineArgs, EngineArgs
  File "C:\Users\jazzw\AppData\Roaming\uv\tools\vllm\Lib\site-packages\vllm\engine\arg_utils.py", line 22, in <module>
    from vllm.executor.executor_base import ExecutorBase
  File "C:\Users\jazzw\AppData\Roaming\uv\tools\vllm\Lib\site-packages\vllm\executor\executor_base.py", line 16, in <module>
    from vllm.model_executor.layers.sampler import SamplerOutput
  File "C:\Users\jazzw\AppData\Roaming\uv\tools\vllm\Lib\site-packages\vllm\model_executor\layers\sampler.py", line 23, in <module>
    from vllm.spec_decode.metrics import SpecDecodeWorkerMetrics
  File "C:\Users\jazzw\AppData\Roaming\uv\tools\vllm\Lib\site-packages\vllm\spec_decode\metrics.py", line 9, in <module>
    from vllm.model_executor.layers.spec_decode_base_sampler import (
  File "C:\Users\jazzw\AppData\Roaming\uv\tools\vllm\Lib\site-packages\vllm\model_executor\layers\spec_decode_base_sampler.py", line 10, in <module>
    from vllm.platforms import current_platform
  File "C:\Users\jazzw\AppData\Roaming\uv\tools\vllm\Lib\site-packages\vllm\platforms\__init__.py", line 288, in __getattr__
    _current_platform = resolve_obj_by_qualname(
                        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jazzw\AppData\Roaming\uv\tools\vllm\Lib\site-packages\vllm\utils.py", line 1899, in resolve_obj_by_qualname
    module = importlib.import_module(module_name)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jazzw\AppData\Roaming\uv\python\cpython-3.12.9-windows-x86_64-none\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jazzw\AppData\Roaming\uv\tools\vllm\Lib\site-packages\vllm\platforms\cuda.py", line 15, in <module>
    import vllm._C  # noqa
    ^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'vllm._C'
jazzw@JazzBook:~/git/snippet/py/vllm$
```
- ( 2025-03-21 10:40:40 )
- 看起來這種安裝方式有點問題，再試試看 `venv` 的作法。
```bash
jazzw@JazzBook:~$ uv venv vllm --python python3.12
Using CPython 3.12.9
Creating virtual environment at: vllm
Activate with: vllm\Scripts\activate
jazzw@JazzBook:~$ source vllm/Scripts/activate
(vllm) jazzw@JazzBook:~$ uv pip install vllm
Using Python 3.12.9 environment at: vllm
Resolved 113 packages in 2.53s
⠴ Preparing packages... (0/2)
ray        ------------------------------ 5.72 MiB/24.49 MiB
cupy-cuda12x ------------------------------ 5.92 MiB/78.26 MiB
```
- https://docs.vllm.ai/en/latest/serving/engine_args.html
```bash
(vllm) jazzw@JazzBook:~$ vllm serve
INFO 03-21 17:35:19 [__init__.py:256] Automatically detected platform cuda.
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\jazzw\vllm\Scripts\vllm.exe\__main__.py", line 4, in <module>
  File "C:\Users\jazzw\vllm\Lib\site-packages\vllm\__init__.py", line 11, in <module>
    from vllm.engine.arg_utils import AsyncEngineArgs, EngineArgs
  File "C:\Users\jazzw\vllm\Lib\site-packages\vllm\engine\arg_utils.py", line 22, in <module>
    from vllm.executor.executor_base import ExecutorBase
  File "C:\Users\jazzw\vllm\Lib\site-packages\vllm\executor\executor_base.py", line 16, in <module>
    from vllm.model_executor.layers.sampler import SamplerOutput
  File "C:\Users\jazzw\vllm\Lib\site-packages\vllm\model_executor\layers\sampler.py", line 23, in <module>
    from vllm.spec_decode.metrics import SpecDecodeWorkerMetrics
  File "C:\Users\jazzw\vllm\Lib\site-packages\vllm\spec_decode\metrics.py", line 9, in <module>
    from vllm.model_executor.layers.spec_decode_base_sampler import (
  File "C:\Users\jazzw\vllm\Lib\site-packages\vllm\model_executor\layers\spec_decode_base_sampler.py", line 10, in <module>
    from vllm.platforms import current_platform
  File "C:\Users\jazzw\vllm\Lib\site-packages\vllm\platforms\__init__.py", line 288, in __getattr__
    _current_platform = resolve_obj_by_qualname(
                        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jazzw\vllm\Lib\site-packages\vllm\utils.py", line 1899, in resolve_obj_by_qualname
    module = importlib.import_module(module_name)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jazzw\AppData\Roaming\uv\python\cpython-3.12.9-windows-x86_64-none\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jazzw\vllm\Lib\site-packages\vllm\platforms\cuda.py", line 15, in <module>
    import vllm._C  # noqa
    ^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'vllm._C'
```
- 仍舊失敗～看樣子是其他問題（找不到 CUDA）~待解

## 2026-08-31

> [!QUESTION]
> 除了 FP8, INT16 以外,有近似 Q4_K_M 的 vLLM 支援?

有的，而且非常多。如果您希望在 vLLM 中獲得類似 GGUF Q4\_K\_M 的低 VRAM 佔用（約 4-bit 體積），但又想保有 vLLM 的高吞吐量與高併發優勢，您最完美的替代方案是 AWQ 和 GPTQ（尤其是搭配 Marlin 核心加速 的版本）。 [1, 2, 3]
此外，vLLM 近期也推出了原生載入 GGUF 的實驗性功能。以下為您詳細拆解這些在 vLLM 上能替代 Q4\_K\_M 的 4-bit 方案： [4, 5]

### 1\. AWQ (Activation-Aware Weight Quantization) ------ 最佳首選 🌟

-   對應 GGUF 的級別： 非常接近 Q4\_K\_M 的模型體積（W4A16，即 4-bit 權重、16-bit 活化值）。 [6]
-   運作原理： 它非常聰明，在量化時會觀察模型運行，找出最關鍵的 1% 權重通道（Salient Weights）並保留高精準度，只對其餘 99% 的權重進行 4-bit 壓縮。 [6, 7]
-   精準度（對比 Q4\_K\_M）： 通常優於或等於 Q4\_K\_M。尤其在推理、程式碼生成（Coding）和數學任務上，AWQ 是 4-bit 中表現最好的，幾乎沒有降智感。 [6, 8, 9]
-   vLLM 效能表現： 這是 vLLM 官方最推薦的 4-bit 格式。在 vLLM 中，AWQ 預設會啟用 Marlin 高效能 CUDA 核心，其速度（TPS）會比傳統 4-bit 快上數倍，非常適合單卡 NVIDIA 部署。 [1, 10, 11, 12]
-   使用方式： 啟動指令加上 `--quantization awq`。 [2]

### 2\. GPTQ (with Marlin Kernel) ------ 老牌吞吐量王者 🏎️

-   對應 GGUF 的級別： 精準對標常規的 4-bit 量化。
-   運作原理： 採用逐層錯誤最小化的數學方法進行靜態量化。
-   精準度（對比 Q4\_K\_M）： 稍微遜於 AWQ 與 Q4\_K\_M。GPTQ 在部分複雜的長文本或程式碼任務中，精準度會比 AWQ 有更明顯的滑落。
-   vLLM 效能表現： 如果在 vLLM 中搭配 `marlin` 核心（`--quantization gptq --kv-cache-dtype fp8` 等配置），它的極致吞吐量（TPS）會非常高，在多用戶併發時表現極具侵略性。
-   使用方式： 啟動指令加上 `--quantization gptq`。 [1, 2, 8, 10, 12]

### 3\. vLLM 原生支援 GGUF (Experimental) ------ 直接搬移 📦

-   對應 GGUF 的級別： 就是您提到的 Q4\_K\_M 本尊。
-   運作原理： vLLM 近期版本（需安裝 `vllm-gguf-plugin`）已經支援直接載入單一檔案的 .gguf 模型。
-   優點： 您不需要重新下載或轉換模型，可以直接用 vLLM 的 PagedAttention 機制來 serve 您的 GGUF 檔案。
-   缺點（致命傷）： 效能（TPS）目前非常低落。因為 GGUF 的記憶體布局是為了 CPU/Apple Silicon 優化的，當 vLLM 在 NVIDIA GPU 上執行它時，每一輪計算（Forward Pass）都需要在 VRAM 裡即時轉換布局，這會造成極大的效能瓶頸。現階段僅適合用來「降低記憶體測試」，不適合高流量生產環境。 [2, 4, 5, 7, 10, 13]

### 總結：以 Qwen 3.8 27B 在 vLLM 上的實務建議

如果您決定要用 vLLM 來部署 Qwen 3.8 27B，且 VRAM 預算卡在 20GB~24GB 左右：

1.  不要直接餵 GGUF 給 vLLM：雖然會動，但速度會非常慢（吞吐量可能只有幾十，甚至低於 llama.cpp）。 [4, 10]
2.  請在 Hugging Face 上尋找 `Qwen3-27B-Instruct-AWQ` 版本的權重檔：

    -   體積與 VRAM：跟 Q4\_K\_M 一模一樣（約 17~18GB 模型體積）。
    -   速度 (TPS)：在 vLLM 的 Marlin 加速下，吞吐量會是 GGUF 在 vLLM 跑的數倍以上。
    -   精準度：完美保留 Qwen 3.8 27B 的多模態與邏輯推理實力。 [1, 6, 7, 8, 9, 10, 12]

您目前手邊的顯示卡是 RTX 3090 / 4090 (24GB) 還是企業級顯示卡 (如 A10G / L4) 呢？如果是 NVIDIA 顯示卡，我可以幫您確認該顯卡支援 AWQ + Marlin 的效能表現。

[1] [https://jarvislabs.ai](https://jarvislabs.ai/blog/vllm-quantization-complete-guide-benchmarks)
[2] [https://medium.com](https://medium.com/@kimdoil1211/speeding-up-large-language-models-a-deep-dive-into-gptq-and-awq-quantization-0bb001eaabd4)
[3] [https://university.tenten.co](https://university.tenten.co/t/gguf-vs-gptq-vs-awq-llm-2026/2408)
[4] [https://www.reddit.com](https://www.reddit.com/r/LocalLLaMA/comments/1q7ysj2/we_benchmarked_every_4bit_quantization_method_in/)
[5] [https://docs.vllm.ai](https://docs.vllm.ai/en/latest/features/quantization/gguf/)
[6] [https://fahim.bd](https://fahim.bd/blog/llm-quantization-demystified/)
[7] [https://lyceum.technology](https://lyceum.technology/magazine/gguf-vs-gptq-vs-awq-quantization/)
[8] [https://gingerlabs.ai](https://gingerlabs.ai/blog/gguf-vs-awq-vs-gptq)
[9] [https://www.linkedin.com](https://www.linkedin.com/pulse/demystifying-llm-quantization-gptq-awq-gguf-explained-xiao-fei-zhang-1lmbe)
[10] [https://pub.towardsai.net](https://pub.towardsai.net/i-tested-gguf-vs-awq-vs-gptq-the-fastest-4-bit-collapses-on-code-at-46-d65c271d7cdf)
[11] [https://gigagpu.com](https://gigagpu.com/awq-vs-gptq-vs-gguf-vs-exl2-2026/)
[12] [https://www.reddit.com](https://www.reddit.com/r/LocalLLaMA/comments/1s9iyrw/has_anyone_tested_the_quantization_quality/)
[13] [https://docs.vllm.ai](https://docs.vllm.ai/en/v0.8.5/features/quantization/gguf.html)

> [!QUESTION]
> 如果用 AMD 顯示卡,vLLM 也跑得動 Qwen 3.8 27B AWQ 嗎?

答案是：可以跑得動，但這並非最佳解，且體驗可能非常痛苦。
將 AMD 顯示卡（Radeon 晶片組如 7900 XTX） 與 vLLM (AWQ) 結合來跑 Qwen 3.8 27B，會面臨軟體支援度、硬體架構以及效能上的三大隱憂。 [1, 2, 3]
以下為您盤點 AMD 顯卡在 vLLM 上執行 AWQ 的真實狀況與最合適的替代方案：

### 1\. 為什麼用 AMD 顯卡跑 vLLM AWQ 會很痛苦？

-   消費級顯卡（Radeon）非一等公民： vLLM 官方對 AMD ROCm 的 AWQ 核心優化，主要是針對資料中心級別的 Instinct 系列（如 [MI300X](https://www.google.com/search?kgmid=FAILED_OR_SKIPPED)、[MI320](https://www.google.com/search?kgmid=FAILED_OR_SKIPPED)）。如果是消費級的 [RX 7900 XTX](https://www.google.com/search?kgmid=FAILED_OR_SKIPPED) / 7900 XT，雖然透過最新版的 vLLM 能勉強載入，但很容易遇到 Triton 核心報錯、引擎崩潰（Segfault）或陷入死循環。 [1, 2, 4, 5, 6]
-   缺乏專屬加速核心： NVIDIA 跑 AWQ 之所以快，是因為有 Marlin 核心加持。而在 AMD 平台上，您必須加上環境變數 `VLLM_USE_TRITON_AWQ=1` 來改用 Triton 編譯的通用核心。這會導致推論速度（TPS）顯著變慢，失去了 vLLM 原有的速度優勢。 [2, 5]
-   VRAM 邊緣卡死： Qwen 3.8 27B AWQ 的權重約 17GB ~ 18GB。雖然 [7900 XTX](https://www.google.com/search?kgmid=FAILED_OR_SKIPPED) 有 24GB VRAM，但在 vLLM 中扣除權重後只剩 6GB，這時 PagedAttention 能分配給多用戶（Concurrency）或長文本的 KV Cache 空間會極度壓縮，很容易頻繁觸發系統不穩定。 [1, 7, 8]

### 2\. 替代方案 A：改用 GPTQ (在 vLLM 上更穩定)

如果您堅持要用 vLLM 來建立生產級 API（為了高吞吐與多用戶併發），在 AMD 消費級顯卡上，GPTQ 的相容性與成熟度通常高於 AWQ。 [2]

-   實務建議： 在 Hugging Face 上尋找 `Qwen3-27B-Instruct-GPTQ` 或透過開源工具（如 AMD Quark 或 AutoRound）轉換為 4-bit GPTQ 格式。
-   效能表現： 許多 [7900 XTX](https://www.google.com/search?kgmid=FAILED_OR_SKIPPED) 用戶在社群回饋中表示，GPTQ 在 ROCm 環境下的穩定度明顯更好，且速度比 AWQ 快。 [2, 9]

### 3\. 替代方案 B：回歸 llama.cpp (對 AMD 消費級顯卡的黃金解)

如果您這台 AMD 顯卡機器主要是個人開發、單人測試，強烈建議放棄 vLLM，回歸 llama.cpp 跑 GGUF Q4\_K\_M。

-   完美的 ROCm 支援： llama.cpp 對於 AMD Radeon 顯示卡的 ROCm HIP 支援度極高且非常成熟，開箱即用，不容易崩潰。
-   官方 Day-0 背書： AMD 官方在發布 Qwen 3.8 27B 時，就是使用 llama.cpp 在其最新的 AI PC（Ryzen AI Max）與 Radeon PRO 顯卡上進行示範。 [3]
-   長文本優勢： 27B 的 4-bit 在 24GB 顯卡上，llama.cpp 能夠非常精準地榨乾剩下的 6GB VRAM，如果上下文超出，還能自動把 KV Cache 分流到系統記憶體（RAM），完全不會有 OOM（記憶體溢出）的斷頭風險。 [3, 7]

### 總結建議

1.  如果是商業/團隊用途、需要多人同時接 API：請想辦法將模型轉成 4-bit GPTQ，並使用最新版支援 ROCm 7.x 的 vLLM 容器啟動。 [2, 6]
2.  如果是個人本地開發、求穩、求簡單：請不要折騰 vLLM AWQ。直接用 llama.cpp / Ollama 下載 GGUF Q4\_K\_M，在 AMD 24GB 顯卡上可以跑出 50+ TPS 的流暢體驗。 [2, 3, 7]

如果您打算試試看 vLLM，需要我提供在 AMD ROCm 環境下啟動 vLLM 的 Docker 指令與環境變數設定（例如 `HSA_OVERRIDE_GFX_VERSION`）嗎？

[1] [https://github.com](https://github.com/vllm-project/vllm/issues/11249)
[2] [https://www.reddit.com](https://www.reddit.com/r/LocalLLaMA/comments/1l5pab6/vllm_gptqawq_setups_on_amd_7900_xtx_did_anyone/)
[3] [https://www.amd.com](https://www.amd.com/en/blogs/2026/run-qwen-3-8-27b-on-amd-ryzen-ai-max-and-radeon-graphics-cards-day-0.html)
[4] [https://github.com](https://github.com/vllm-project/vllm/issues/39348)
[5] [https://rocm.docs.amd.com](https://rocm.docs.amd.com/projects/ai-ecosystem/en/latest/optimization/vllm-v1-optimization.html)
[6] [https://github.com](https://github.com/vllm-project/vllm/issues/37151)
[7] [https://www.yottalabs.ai](https://www.yottalabs.ai/post/qwen-3-8-27b-specs-hardware-requirements-how-to-run-2026)
[8] [https://unsloth.ai](https://unsloth.ai/docs/models/qwen3.8)
[9] [https://docs.vllm.ai](https://docs.vllm.ai/en/v0.26.0/features/quantization/quark/)