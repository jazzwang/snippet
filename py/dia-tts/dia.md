# Nari Labs - Dia

> Dia is a 1.6B parameter text to speech model created by Nari Labs.

> A TTS model capable of generating ultra-realistic dialogue in one pass.

- Learn from https://www.linkedin.com/feed/update/urn:li:activity:7320822069850517506/
```
模型：
https://huggingface.co/nari-labs/Dia-1.6B

程式碼：
https://github.com/nari-labs/dia/

官方網站：
https://yummy-fir-7a4.notion.site/dia
```
- Git Repo
  - https://github.com/nari-labs/dia/
- HuggingFace
  - https://huggingface.co/nari-labs/Dia-1.6B

## 2025-07-21

### Quick Start

- 根據 [HuggingFace 說明的 Quick Start](https://huggingface.co/nari-labs/Dia-1.6B#%E2%9A%A1%EF%B8%8F-quickstart)
```
~/git$ git clone https://github.com/nari-labs/dia.git
Cloning into 'dia'...
remote: Enumerating objects: 421, done.
remote: Counting objects: 100% (292/292), done.
remote: Compressing objects: 100% (114/114), done.
remote: Total 421 (delta 256), reused 178 (delta 178), pack-reused 129 (from 2)
Receiving objects: 100% (421/421), 740.32 KiB | 474.00 KiB/s, done.
Resolving deltas: 100% (272/272), done.
~/git$ cd dia && uv run app.py
Using CPython 3.10.17
Creating virtual environment at: C:\Users\jazzw\git\dia\.venv
      Built nari-tts @ file:///C:/Users/jazzw/git/dia
      Built randomname==0.2.1
      Built fire==0.7.0
      Built julius==0.2.7
      Built argbind==0.3.9
~/git/dia$ uv run app.py
Using device: cuda
Loading Nari model...
Using device: cuda, attempting to load model with float16
config.json: 1.40kB [00:00, ?B/s]
pytorch_model.bin:   0%|▏                                                                                           | 10.5M/6.44G [00:10<1:45:20, 1.02MB/s]
KeyboardInterrupt

~/git/dia$ uv run cli.py --help
usage: cli.py [-h] --output OUTPUT [--repo-id REPO_ID] [--local-paths] [--config CONFIG] [--checkpoint CHECKPOINT] [--audio-prompt AUDIO_PROMPT]
              [--max-tokens MAX_TOKENS] [--cfg-scale CFG_SCALE] [--temperature TEMPERATURE] [--top-p TOP_P] [--seed SEED] [--device DEVICE]
              text

Generate audio using the Dia model.

positional arguments:
  text                  Input text for speech generation.

options:
  -h, --help            show this help message and exit
  --output OUTPUT       Path to save the generated audio file (e.g., output.wav).
  --repo-id REPO_ID     Hugging Face repository ID (e.g., nari-labs/Dia-1.6B-0626).
  --local-paths         Load model from local config and checkpoint files.
  --config CONFIG       Path to local config.json file (required if --local-paths is set).
  --checkpoint CHECKPOINT
                        Path to local model checkpoint .pth file (required if --local-paths is set).
  --audio-prompt AUDIO_PROMPT
                        Path to an optional audio prompt WAV file for voice cloning.

Generation Parameters:
  --max-tokens MAX_TOKENS
                        Maximum number of audio tokens to generate (defaults to config value).
  --cfg-scale CFG_SCALE
                        Classifier-Free Guidance scale (default: 3.0).
  --temperature TEMPERATURE
                        Sampling temperature (higher is more random, default: 0.7).
  --top-p TOP_P         Nucleus sampling probability (default: 0.95).

Infrastructure:
  --seed SEED           Random seed for reproducibility.
  --device DEVICE       Device to run inference on (e.g., 'cuda', 'cpu', default: auto).
~/git/dia$ ls
app.py  cli.py  dia  docker  example  example_prompt.mp3  hf.py  LICENSE  pyproject.toml  README.md  uv.lock
~/git/dia$ uv run cli.py --output script-01.wav script-01.txt
Using device: cuda
Loading model...
Loading from Hugging Face Hub: repo_id='nari-labs/Dia-1.6B-0626'
pytorch_model.bin:  58%|██████████████████████████████████████████████████████▊                                       | 3.75G/6.44G [33:45<22:53, 1.96MB/s]
```

## 2025-07-22

- 下載好久，試試看在 Github Codespace 跑跑看
```bash
Welcome to Ubuntu 24.04.2 LTS (GNU/Linux 6.8.0-1027-azure x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro
Last login: Thu Jul 17 07:57:46 2025 from ::1
@jazzwang ➜ /workspaces/aider-labs (main) $ cd /tmp/
@jazzwang ➜ /tmp $ git clone https://github.com/nari-labs/dia.git
Cloning into 'dia'...
remote: Enumerating objects: 421, done.
remote: Counting objects: 100% (292/292), done.
remote: Compressing objects: 100% (114/114), done.
remote: Total 421 (delta 257), reused 178 (delta 178), pack-reused 129 (from 2)
Receiving objects: 100% (421/421), 740.04 KiB | 22.42 MiB/s, done.
Resolving deltas: 100% (273/273), done.
@jazzwang ➜ /tmp $ cd dia
@jazzwang ➜ /tmp/dia (main) $ uv run cli.py --help
Using CPython 3.10.18
Creating virtual environment at: .venv
      Built nari-tts @ file:///tmp/dia
      Built argbind==0.3.9
      Built fire==0.7.0
      Built julius==0.2.7
      Built randomname==0.2.1
░░░░░░░░░░░░░░░░░░░░ [0/123] Installing wheels...                                                                                                           warning: Failed to hardlink files; falling back to full copy. This may lead to degraded performance.
         If the cache and target directories are on different filesystems, hardlinking may not be supported.
         If this is intentional, set `export UV_LINK_MODE=copy` or use `--link-mode=copy` to suppress this warning.
Installed 123 packages in 9.09s
Traceback (most recent call last):
  File "/tmp/dia/.venv/lib/python3.10/site-packages/torch/__init__.py", line 318, in _load_global_deps
    ctypes.CDLL(global_deps_lib_path, mode=ctypes.RTLD_GLOBAL)
  File "/home/codespace/.local/share/uv/python/cpython-3.10.18-linux-x86_64-gnu/lib/python3.10/ctypes/__init__.py", line 374, in __init__
    self._handle = _dlopen(self._name, mode)
OSError: libcudart.so.12: cannot open shared object file: No such file or directory

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/tmp/dia/cli.py", line 7, in <module>
    import torch
  File "/tmp/dia/.venv/lib/python3.10/site-packages/torch/__init__.py", line 404, in <module>
    _load_global_deps()
  File "/tmp/dia/.venv/lib/python3.10/site-packages/torch/__init__.py", line 362, in _load_global_deps
    _preload_cuda_deps(lib_folder, lib_name)
  File "/tmp/dia/.venv/lib/python3.10/site-packages/torch/__init__.py", line 302, in _preload_cuda_deps
    raise ValueError(f"{lib_name} not found in the system path {sys.path}")
ValueError: libcublas.so.*[0-9] not found in the system path ['/tmp/dia', '/home/codespace/.local/share/uv/python/cpython-3.10.18-linux-x86_64-gnu/lib/python310.zip', '/home/codespace/.local/share/uv/python/cpython-3.10.18-linux-x86_64-gnu/lib/python3.10', '/home/codespace/.local/share/uv/python/cpython-3.10.18-linux-x86_64-gnu/lib/python3.10/lib-dynload', '/tmp/dia/.venv/lib/python3.10/site-packages', '/tmp/dia']
@jazzwang ➜ /tmp/dia (main) $ uv run cli.py --help
Traceback (most recent call last):
  File "/tmp/dia/.venv/lib/python3.10/site-packages/torch/__init__.py", line 318, in _load_global_deps
    ctypes.CDLL(global_deps_lib_path, mode=ctypes.RTLD_GLOBAL)
  File "/home/codespace/.local/share/uv/python/cpython-3.10.18-linux-x86_64-gnu/lib/python3.10/ctypes/__init__.py", line 374, in __init__
    self._handle = _dlopen(self._name, mode)
OSError: libcudart.so.12: cannot open shared object file: No such file or directory

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/tmp/dia/cli.py", line 7, in <module>
    import torch
  File "/tmp/dia/.venv/lib/python3.10/site-packages/torch/__init__.py", line 404, in <module>
    _load_global_deps()
  File "/tmp/dia/.venv/lib/python3.10/site-packages/torch/__init__.py", line 362, in _load_global_deps
    _preload_cuda_deps(lib_folder, lib_name)
  File "/tmp/dia/.venv/lib/python3.10/site-packages/torch/__init__.py", line 302, in _preload_cuda_deps
    raise ValueError(f"{lib_name} not found in the system path {sys.path}")
ValueError: libcublas.so.*[0-9] not found in the system path ['/tmp/dia', '/home/codespace/.local/share/uv/python/cpython-3.10.18-linux-x86_64-gnu/lib/python310.zip', '/home/codespace/.local/share/uv/python/cpython-3.10.18-linux-x86_64-gnu/lib/python3.10', '/home/codespace/.local/share/uv/python/cpython-3.10.18-linux-x86_64-gnu/lib/python3.10/lib-dynload', '/tmp/dia/.venv/lib/python3.10/site-packages', '/tmp/dia']
@jazzwang ➜ /tmp/dia (main) $ sudo apt-get install apt-file
@jazzwang ➜ /tmp/dia (main) $ sudo apt-file update
@jazzwang ➜ /tmp/dia (main) $ apt-file search libcudart
libcudart12: /usr/lib/x86_64-linux-gnu/libcudart.so.12
libcudart12: /usr/lib/x86_64-linux-gnu/libcudart.so.12.0.146
libcudart12: /usr/share/doc/libcudart12/changelog.Debian.gz
libcudart12: /usr/share/doc/libcudart12/copyright
libcudart12: /usr/share/lintian/overrides/libcudart12
nvidia-cuda-dev: /usr/lib/x86_64-linux-gnu/libcudart.so
nvidia-cuda-dev: /usr/lib/x86_64-linux-gnu/libcudart_static.a
nvitop: /usr/lib/python3/dist-packages/nvitop/api/libcudart.py
@jazzwang ➜ /tmp/dia (main) $ sudo apt-get install libcudart12
@jazzwang ➜ /tmp/dia (main) $ uv run cli.py --help
Traceback (most recent call last):
  File "/tmp/dia/cli.py", line 7, in <module>
    import torch
  File "/tmp/dia/.venv/lib/python3.10/site-packages/torch/__init__.py", line 405, in <module>
    from torch._C import *  # noqa: F403
ImportError: libcudnn.so.9: cannot open shared object file: No such file or directory
@jazzwang ➜ /tmp/dia (main) $ apt-file search libcudnn
libcudnn-frontend-dev: /usr/share/doc/libcudnn-frontend-dev/changelog.Debian.gz
libcudnn-frontend-dev: /usr/share/doc/libcudnn-frontend-dev/copyright
nvidia-cudnn: /usr/lib/x86_64-linux-gnu/libcudnn.so
nvidia-cudnn: /usr/lib/x86_64-linux-gnu/libcudnn.so.8
@jazzwang ➜ /tmp/dia (main) $ sudo apt-get install nvidia-cudnn
Errors were encountered while processing:
 /tmp/apt-dpkg-install-iP5p2U/189-nvidia-cuda-dev_12.0.146~12.0.1-4build4_amd64.deb
E: Sub-process /usr/bin/dpkg returned an error code (1)
@jazzwang ➜ /tmp/dia (main) $ sudo apt --fix-broken install
dpkg: unrecoverable fatal error, aborting:
 unable to fill /var/lib/dpkg/updates/tmp.i with padding: No space left on device
E: Sub-process /usr/bin/dpkg returned an error code (2)
@jazzwang ➜ /tmp/dia (main) $ df -h .
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       118G  8.8G  103G   8% /tmp
@jazzwang ➜ /tmp/dia (main) $ cd /var/lib/
@jazzwang ➜ /var/lib $ df -h .
Filesystem      Size  Used Avail Use% Mounted on
overlay          32G   31G     0 100% /
@jazzwang ➜ /var/lib $ exit
```
- 好吧，把硬碟空間全用光了 :(

- 就只好繼續讓程式繼續下載 Pytorch 模型。

```bash
[07/22 00:20:07] ~/git/dia$ uv run cli.py --output script-01.wav script-01.txt
```

- Windows 本地端的程式經過一晚的下載，總算拿到 `pytorch_model.bin`，可以正常跑 `cli.py`。

```bash
[07/22 08:54:31] ~/git/dia$ uv run cli.py
usage: cli.py [-h] --output OUTPUT [--repo-id REPO_ID] [--local-paths] [--config CONFIG] [--checkpoint CHECKPOINT] [--audio-prompt AUDIO_PROMPT]
              [--max-tokens MAX_TOKENS] [--cfg-scale CFG_SCALE] [--temperature TEMPERATURE] [--top-p TOP_P] [--seed SEED] [--device DEVICE]
              text
cli.py: error: the following arguments are required: text, --output
[07/22 08:55:21] ~/git/dia$ uv run cli.py --local-paths
[07/22 08:56:09] ~/git/dia$ uv run cli.py --output script-01.wav --local-paths $(cat script-01.txt)
~/git/dia$ uv run cli.py --output script-01.wav --local-paths $(cat script-01.txt)
usage: cli.py [-h] --output OUTPUT [--repo-id REPO_ID] [--local-paths] [--config CONFIG] [--checkpoint CHECKPOINT] [--audio-prompt AUDIO_PROMPT]
              [--max-tokens MAX_TOKENS] [--cfg-scale CFG_SCALE] [--temperature TEMPERATURE] [--top-p TOP_P] [--seed SEED] [--device DEVICE]
              text
cli.py: error: unrecognized arguments: Today I'll demo the reverse engineering that's done using local LLM. [S1] This is ....
```
- 發現 `example\simple.py` 可以簡單地產生 MP3
```bash
[07/22 11:54:26] ~/git/dia/example$ uv run simple.py
[07/22 12:24:13] ~/git/dia/example$ ls
[07/22 12:24:20] ~/git/dia/example$ open simple.mp3
```
- 用 Aider 改寫 `example\simple.py` 讓它支援可以讀取 input 檔名，跟設定 output mp3 檔名。
```bash
[07/22 12:26:26] ~/git/dia$ export OLLAMA_API_BASE="http://127.0.0.1:11434"
[07/22 12:26:28] ~/git/dia$ ollama list
[07/22 12:26:32] ~/git/dia$ aider --no-auto-commits --no-gitignore --model ollama/gemma3:1b simple.py
```
- Prompt:
```
# 2025-07-22 12:28:06.904310
+rewrite example\simple.py to read 2 command line options (1) input text file (2) output mp3 filename
```
- 結果
```python
~/git/dia$ cat example/simple.py
import argparse
from dia.model import Dia

def main():
    parser = argparse.ArgumentParser(description="Generate audio from text using the Dia model.")
    parser.add_argument("input_text_file", type=str, help="Path to the input text file.")
    parser.add_argument("output_mp3_file", type=str, help="Path to save the output MP3 file.")

    args = parser.parse_args()

    model = Dia.from_pretrained("nari-labs/Dia-1.6B-0626", compute_dtype="float16")

    with open(args.input_text_file, 'r', encoding='utf-8') as file:
        text = file.read().strip()

    output = model.generate(
        text,
        use_torch_compile=False,
        verbose=True,
        cfg_scale=3.0,
        temperature=1.8,
        top_p=0.90,
        cfg_filter_top_k=50,
    )

    model.save_audio(args.output_mp3_file, output)

if __name__ == "__main__":
    main()
```
```bash
[07/22 12:43:09] ~/git/dia/example$ uv run simple.py ../script-01.txt script-01.mp3
[07/22 12:51:49] ~/git/dia/example$ open script-01.mp3
[07/22 12:52:40] ~/git/dia/example$ code ../script-01.txt
[07/22 12:53:14] ~/git/dia/example$ code script-02.txt
[07/22 12:53:39] ~/git/dia/example$ code script-03.txt
[07/22 12:56:24] ~/git/dia/example$ code script-04.txt
[07/22 12:56:54] ~/git/dia/example$ cp ../script-01.txt .
[07/22 12:57:07] ~/git/dia/example$ uv run simple.py script-01.txt script-01.mp3
[07/22 13:11:45] ~/git/dia/example$ uv run simple.py script-02.txt script-02.mp3
[07/22 13:18:42] ~/git/dia/example$ uv run simple.py script-01.txt script-01.mp3
```

### 硬碟空間分析

- 為了要跑 Dia ，光是 Pytorch 也要 `4.4 GB`。
```bash
~/git/dia/.venv/Lib/site-packages$ du -s * | sort -nr | head -n 5
4531296 torch
163995  gradio
112297  triton
101594  scipy
87196   llvmlite
~/git/dia/.venv/Lib/site-packages$ du -sh torch
4.4G    torch
~/git/dia/.venv/Lib/site-packages$ du -sh gradio
161M    gradio
```
- 從 HuggingFace 下載的 `pytorch_model.bin` 實際上放在 `~/.cache/huggingface/hub` 底下
```bash
~/.cache/huggingface/hub$ du -sh .
6.1G    .
~/.cache/huggingface/hub$ tree
.
└── models--nari-labs--Dia-1.6B-0626
    ├── blobs
    │   ├── 0e31928c93bec291911314d4c6a21bf7914134ba
    │   └── 8a5106c06899aeea013a7f6ef32e84a15a30f965be676b97996b3ddaf1eb55b9
    ├── refs
    │   └── main
    └── snapshots
        └── ef2795fcc29c5abe6ffc91fd33808588b49bbc66
            ├── config.json -> ../../blobs/0e31928c93bec291911314d4c6a21bf7914134ba
            └── pytorch_model.bin -> ../../blobs/8a5106c06899aeea013a7f6ef32e84a15a30f965be676b97996b3ddaf1eb55b9

6 directories, 5 files
```

## 2025-07-23

- 實測後，再重新看了一次 README，發現一些缺點：
  - 一次不能放太多 transcript ，不然語速會太快。大約一秒 80 個 token
    - https://token-calculator.net/token-speed-simulator 我用這個網站來計算 token 數目
  - `[S1]` 跟 `[S2]` 必須交錯。不可以 `[S1]....[S1].....[S2].....`
  - 每次產生的 `[S1]` 跟 `[S2]` 聲音沒辦法控制。但是可以用 `Voice Clone` 的方式控制。
    - 參考範例：https://github.com/nari-labs/dia/blob/main/example/voice_clone.py

## 2025-07-27

- 六月又有發布一版新的模型
  - https://huggingface.co/nari-labs/Dia-1.6B-0626