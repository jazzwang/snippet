# Qwen

## 2025-03-07

## Qwen2.5-Coder

- 2024-11-12: ["Qwen2.5-Coder Series: Powerful, Diverse, Practical"](https://qwenlm.github.io/blog/qwen2.5-coder-family)

- https://qwenlm.github.io/blog/qwen2.5-coder-family/#diverse-rich-model-sizes

| Models | Params | Non-Emb Params | Layers | Heads (KV) | Tie Embedding | Context Length | License |
| --- |  --- |  --- |  --- |  --- |  --- |  --- |  --- |
| Qwen2.5-Coder-0.5B | 0.49B | 0.36B | 24 | 14 / 2 | Yes | 32K | Apache 2.0 |
| --- |  --- |  --- |  --- |  --- |  --- |  --- |  --- |
| Qwen2.5-Coder-1.5B | 1.54B | 1.31B | 28 | 12 / 2 | Yes | 32K | Apache 2.0 |
| Qwen2.5-Coder-3B | 3.09B | 2.77B | 36 | 16 / 2 | Yes | 32K | Qwen Research |
| Qwen2.5-Coder-7B | 7.61B | 6.53B | 28 | 28 / 4 | No | <mark>128K</mark> | Apache 2.0 |
| Qwen2.5-Coder-14B | 14.7B | 13.1B | 48 | 40 / 8 | No | <mark>128K</mark> | Apache 2.0 |
| Qwen2.5-Coder-32B | 32.5B | 31.0B | 64 | 40 / 8 | No | <mark>128K</mark> | Apache 2.0 |

![](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen2.5/Qwen2.5-Coder-Family/qwen2.5-coder-family-base.png#center)

- ( 2025-03-07 23:16:39 )
- Q: `Tie Embedding` 是什麼意思？

### context window of Qwen2.5 Coder 7B Instruct Q4_K_M

- 原始阿里巴巴釋出的 https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct
    - Context Length: Full 131,072 tokens
        - Please refer to [this section](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct#processing-long-texts) for detailed instructions on how to deploy Qwen2.5 for handling long texts.
  - [這段文件](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct#processing-long-texts) 有寫到預設是 32,768 ，如果要改的話，必須修改 `config.json` 來啟用 [YaRN](https://arxiv.org/abs/2309.00071)
    - 2023-11-01: [YaRN: Efficient Context Window Extension of Large Language Models](https://arxiv.org/abs/2309.00071)
    - The current `config.json` is **set for context length up to <mark>32,768 tokens</mark>.** To handle extensive inputs exceeding 32,768 tokens, we utilize [YaRN](https://arxiv.org/abs/2309.00071), a technique for enhancing model length extrapolation, ensuring optimal performance on lengthy texts.
  - [這段文件](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct#processing-long-texts) 也特別提到推薦使用 vLLM
    - For deployment, we **recommend using vLLM**. Please refer to our [Documentation](https://qwen.readthedocs.io/en/latest/deployment/vllm.html) for usage if you are not familiar with vLLM. Presently, <mark>vLLM only supports static YARN</mark>, which means the scaling factor remains constant regardless of input length, **potentially impacting performance on shorter texts**. <mark>We advise adding the `rope_scaling` configuration only when processing long contexts is required.</mark>
- https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct-GGUF 有寫到
  - Context Length: <mark>Full `32,768` tokens</mark>
    - Note: Currently, only **vLLM** supports YARN for length extrapolating. If you want to <mark>process sequences up to `131,072` tokens, please refer to **non-GGUF models**.<mark>

- ( 2025-03-07 23:20:18 )
- 用 Github Blank 範本開一台 Codespace，登入後安裝 ollama
```
jazzw@JazzBook:~/git/snippet/go/ollama$ gh auth switch
✓ Switched active account for github.com to jazzwang
jazzw@JazzBook:~/git/snippet/go/ollama$ gh cs list
NAME                                      DISPLAY NAME  REPOSITORY               BRANCH  STATE      CREATED AT
glowing-garbanzo-wrvwr4q55hgg5            snippet       jazzwang/snippet         master  Shutdown   about 1 month ago
legendary-space-guacamole-r47j4xj4jcx475  ollama        github/codespaces-blank  main    Available  about 1 minute ago
jazzw@JazzBook:~/git/snippet/go/ollama$ cat ~/bin/snippet
#!/bin/sh
gh cs $1 -R jazzwang/snippet
jazzw@JazzBook:~/git/snippet/go/ollama$ gh cs ssh -R github/codespaces-blank
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 6.5.0-1025-azure x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

@jazzwang ➜ /workspaces/codespaces-blank $ curl -fsSL https://ollama.com/install.sh | sh
>>> Installing ollama to /usr/local
>>> Downloading Linux amd64 bundle
######################################################################## 100.0%
>>> Creating ollama user...
>>> Adding ollama user to video group...
>>> Adding current user to ollama group...
>>> Creating ollama systemd service...
WARNING: systemd is not running
WARNING: Unable to detect NVIDIA/AMD GPU. Install lspci or lshw to automatically detect and install GPU dependencies.
>>> The Ollama API is now available at 127.0.0.1:11434.
>>> Install complete. Run "ollama" from the command line.
@jazzwang ➜ /workspaces/codespaces-blank $ ollama start
Couldn't find '/home/codespace/.ollama/id_ed25519'. Generating new private key.
```
```
curl -fsSL https://ollama.com/install.sh | sh
```
- 下載 LM Studio 社群，由 做的 `Qwen2.5-Coder-7B-Instruct-GGUF:Q4_K_M`
```bash
@jazzwang ➜ /workspaces/codespaces-blank $ ollama run hf.co/lmstudio-community/Qwen2.5-Coder-7B-Instruct-GGUF:Q4_K_M
```
- 實驗觀察 context window 還是 `32,768` 不是 `128K`
```bash
@jazzwang ➜ /workspaces/codespaces-blank $ ollama show hf.co/lmstudio-community/Qwen2.5-Coder-7B-Instruct-GGUF:Q4_K_M
  Model
    architecture        qwen2
    parameters          7.6B
    context length      32768
    embedding length    3584
    quantization        unknown
```

## Qwen2.5-1M

- 2025-01-27: ["Qwen2.5-1M: Deploy Your Own Qwen with Context Length up to 1M Tokens"](https://qwenlm.github.io/blog/qwen2.5-1m/)
- ( 2025-03-08 00:16:50 )
- https://huggingface.co/lmstudio-community/Qwen2.5-7B-Instruct-1M-GGUF
```
@jazzwang ➜ /workspaces/codespaces-blank $ ollama pull hf.co/lmstudio-community/Qwen2.5-7B-Instruct-1M-GGUF:Q4_K_M
pulling 9c24f135b149... 100% ▕████████████████████████████████████████████████████████████████████████████████████████████▏ 4.7 GB
pulling e94a8ecb9327... 100% ▕████████████████████████████████████████████████████████████████████████████████████████████▏ 1.6 KB
pulling 9ae14bd2c052... 100% ▕████████████████████████████████████████████████████████████████████████████████████████████▏  193 B
@jazzwang ➜ /workspaces/codespaces-blank $ ollama list
NAME                                                              ID              SIZE      MODIFIED
hf.co/lmstudio-community/Qwen2.5-7B-Instruct-1M-GGUF:Q4_K_M       99558383a8de    4.7 GB    14 seconds ago
hf.co/lmstudio-community/Qwen2.5-Coder-7B-Instruct-GGUF:Q4_K_M    e7ac4b421833    4.7 GB    About an hour ago
@jazzwang ➜ /workspaces/codespaces-blank $ ollama show hf.co/lmstudio-community/Qwen2.5-7B-Instruct-1M-GGUF:Q4_K_M
  Model
    architecture        qwen2
    parameters          7.6B
    context length      1010000
    embedding length    3584
    quantization        unknown
```

## QwQ-32B

- 2025-03-06: ["QwQ-32B: Embracing the Power of Reinforcement Learning"](https://qwenlm.github.io/blog/qwq-32b/)

## 2025-03-22

### function calling

- https://qwen.readthedocs.io/en/latest/framework/function_call.html
- https://github.com/QwenLM/Qwen/blob/main/examples/function_call_examples.py

## Qwen3

## 2025-05-02

- 2025-04-29: [Qwen3: Think Deeper, Act Faster](https://qwenlm.github.io/blog/qwen3/)

| Models | Layers | Heads (Q / KV) | Tie Embedding | Context Length |
| --- |  --- |  --- |  --- |  --- |
| Qwen3-0.6B | 28 | 16 / 8 | Yes | 32K |
| --- |  --- |  --- |  --- |  --- |
| Qwen3-1.7B | 28 | 16 / 8 | Yes | 32K |
| Qwen3-4B | 36 | 32 / 8 | Yes | 32K |
| **Qwen3-8B** | **36** | **32 / 8** | **No** | **128K** |
| Qwen3-14B | 40 | 40 / 8 | No | 128K |
| Qwen3-32B | 64 | 64 / 8 | No | 128K |

- Git Repo
  - https://github.com/QwenLM/Qwen3
- HuggingFace
  - https://huggingface.co/collections/Qwen/qwen3-67dd247413f0e2e4f653967f

可惜查了一下，官方沒有釋出 8B 的 GGUF，只有 32B 跟 14B

## 2025-05-03

- 果然 LMStudio 社群跟得很快。（當然 Ollama 也有啦～只是因為下載很慢，所以能拉 HuggingFace 會比較好做事）
  - https://huggingface.co/lmstudio-community/Qwen3-8B-GGUF

```bash
@jazzwang ➜ /workspaces/codespaces-blank (main) $ ollama start &
@jazzwang ➜ /workspaces/codespaces-blank (main) $ df -h
Filesystem      Size  Used Avail Use% Mounted on
overlay          32G   26G  4.4G  86% /
tmpfs            64M     0   64M   0% /dev
shm              64M     0   64M   0% /dev/shm
/dev/root        29G   13G   17G  44% /vscode
/dev/sdc1        44G  1.7G   41G   4% /tmp
/dev/loop4       32G   26G  4.4G  86% /workspaces
@jazzwang ➜ /workspaces/codespaces-blank (main) $ ollama pull qwen3
Error: mkdir /home/codespace/.ollama/models/manifests/registry.ollama.ai: no space left on device
@jazzwang ➜ /workspaces/codespaces-blank (main) $ df -h
Filesystem      Size  Used Avail Use% Mounted on
overlay          32G   30G     0 100% /
tmpfs            64M     0   64M   0% /dev
shm              64M     0   64M   0% /dev/shm
/dev/root        29G   13G   17G  44% /vscode
/dev/sdc1        44G   31G   11G  75% /tmp
/dev/loop4       32G   30G     0 100% /workspaces
```
- 可能前陣子測試 ChromaDB 裝太多套件，只好 rebuild 一下。rebuild 以後，系統碟有 9G 左右。
```bash
@jazzwang ➜ /workspaces/codespaces-blank (main) $ df -h
Filesystem      Size  Used Avail Use% Mounted on
overlay          32G   21G  9.0G  70% /
tmpfs            64M     0   64M   0% /dev
shm              64M  8.0K   64M   1% /dev/shm
/dev/root        29G   13G   17G  45% /vscode
/dev/sdc1        44G   31G   11G  75% /tmp
/dev/loop4       32G   21G  9.0G  70% /workspaces
```
- 重新安裝 Ollama
```
@jazzwang ➜ /workspaces/codespaces-blank (main) $ curl -fsSL https://ollama.com/install.sh | sh
@jazzwang ➜ /workspaces/codespaces-blank (main) $ ollama start &
@jazzwang ➜ /workspaces/codespaces-blank (main) $ ollama pull qwen3
@jazzwang ➜ /workspaces/codespaces-blank (main) $ ollama show qwen3 --modelfile > qwen3-8b-q4_k_m
```
- 下載到 local
```
jazzw@JazzBook:~$ gh cs cp -e 'remote:/workspaces/codespaces-blank/qwen3-8b-q4_k_m' ./qwen3-8b-q4_k_m
? Choose codespace: github/codespaces-blank [main*]: blank
qwen3-8b-q4_k_m                                                                                                           100%   13KB  46.2KB/s   00:00
jazzw@JazzBook:~$ mv qwen3-8b-q4_k_m git/snippet/go/ollama/
```
- 下載 GGUF 然後匯入 ollama
```bash
jazzw@JazzBook:~$ cd .ollama/
jazzw@JazzBook:~/.ollama$ wget -c https://huggingface.co/lmstudio-community/Qwen3-8B-GGUF/resolve/main/Qwen3-8B-Q4_K_M.gguf
jazzw@JazzBook:~/.ollama$ head -n 12 qwen3-8b-q4_k_m
# Modelfile generated by "ollama show"
# To build a new Modelfile based on this, replace FROM with:
# FROM qwen3:latest

## LMStudio Community
# https://huggingface.co/lmstudio-community/Qwen3-8B-GGUF/blob/main/Qwen3-8B-Q4_K_M.gguf
# ```
# wget -c https://huggingface.co/lmstudio-community/Qwen3-8B-GGUF/resolve/main/Qwen3-8B-Q4_K_M.gguf
# ```

FROM Qwen3-8B-Q4_K_M.gguf
TEMPLATE """{{- if .Messages }}
jazzw@JazzBook:~/.ollama$ ollama create qwen3-8b:q4_k_m -f qwen3-8b-q4_k_m
```
- 測試一下 `aider` 相容性：
  - 看樣子不相容 `aider 0.75.2`
```bash
$ aider --model ollama/qwen3-8b:q4_k_m --no-auto-commits --auto-lint
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Newer aider version v0.82.2 is available.
Run this command to update:

C:\Users\jazzw\AppData\Roaming\uv\tools\aider-chat\Scripts\python.exe -m pip install --upgrade --upgrade-strategy only-if-needed aider-chat
You can skip this check with --no-gitignore
Add .aider* to .gitignore (recommended)? (Y)es/(N)o [Yes]:
Added .aider* to .gitignore
Aider v0.75.2
Model: ollama/qwen3-8b:q4_k_m with whole edit format
Git repo: .git with 23 files
Repo-map: using 4096.0 tokens, auto refresh
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
> /ask could you give me a high-level overview of this git repository?

litellm.APIConnectionError: OllamaException - {"error":"unable to load model:
C:\\Users\\jazzw\\.ollama\\models\\blobs\\sha256-a7676d257b10f3ce23aedba45e64ba61a5aa295f0009d87c5627f6c026a8f35f"}
Retrying in 0.2 seconds...
litellm.APIConnectionError: OllamaException - {"error":"unable to load model:
C:\\Users\\jazzw\\.ollama\\models\\blobs\\sha256-a7676d257b10f3ce23aedba45e64ba61a5aa295f0009d87c5627f6c026a8f35f"}
Retrying in 0.5 seconds...
litellm.APIConnectionError: OllamaException - {"error":"unable to load model:
C:\\Users\\jazzw\\.ollama\\models\\blobs\\sha256-a7676d257b10f3ce23aedba45e64ba61a5aa295f0009d87c5627f6c026a8f35f"}
Retrying in 1.0 seconds...
litellm.APIConnectionError: OllamaException - {"error":"unable to load model:
C:\\Users\\jazzw\\.ollama\\models\\blobs\\sha256-a7676d257b10f3ce23aedba45e64ba61a5aa295f0009d87c5627f6c026a8f35f"}
Retrying in 2.0 seconds...
litellm.APIConnectionError: OllamaException - {"error":"unable to load model:
C:\\Users\\jazzw\\.ollama\\models\\blobs\\sha256-a7676d257b10f3ce23aedba45e64ba61a5aa295f0009d87c5627f6c026a8f35f"}
Retrying in 4.0 seconds...
litellm.APIConnectionError: OllamaException - {"error":"unable to load model:
C:\\Users\\jazzw\\.ollama\\models\\blobs\\sha256-a7676d257b10f3ce23aedba45e64ba61a5aa295f0009d87c5627f6c026a8f35f"}
Retrying in 8.0 seconds...


^C again to exit
```

- 測試一下 ollama 相容性：
  - 備註：在 Github Codespace 想要 `ollama pull qwen3` 時，有錯誤訊息，要求安裝最新版本的 ollama
```
jazzw@JazzBook:~/.ollama$ ollama -v
ollama version is 0.6.5
jazzw@JazzBook:~/.ollama$ ollama pull qwen3
pulling manifest
Error: pull model manifest: 412:

The model you are attempting to pull requires a newer version of Ollama.

Please download the latest version at:

        https://ollama.com/download

jazzw@JazzBook:~/.ollama$ ollama list
NAME                      ID              SIZE      MODIFIED
qwen3-8b:q4_k_m           9ee5c4941145    5.0 GB    About an hour ago
qwen25-7b-it-1m:q4_k_m    80b818033c9f    4.7 GB    2 weeks ago
jazzw@JazzBook:~/.ollama$ ollama run qwen3-8b:q4_k_m
Error: unable to load model: C:\Users\jazzw\.ollama\models\blobs\sha256-a7676d257b10f3ce23aedba45e64ba61a5aa295f0009d87c5627f6c026a8f35f
```
- 所以看樣子從 Gemma3 以後，這些版本相依性變得越來越高了。

## Qwen2.5-Omni
