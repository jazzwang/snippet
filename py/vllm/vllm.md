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