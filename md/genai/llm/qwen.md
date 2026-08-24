[TOC]

# Qwen

## 2025-03-07

# Qwen2.5-Coder

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

# Qwen2.5-1M

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

# Qwen2.5-Omni

- 2025-03-26: Qwen2.5-Omni Technical Report
  - https://arxiv.org/abs/2503.20215
  - https://huggingface.co/papers/2503.20215
- HuggingFace
  - https://huggingface.co/Qwen/Qwen2.5-Omni-3B
  - https://huggingface.co/Qwen/Qwen2.5-Omni-7B
  - https://huggingface.co/Qwen/Qwen2.5-Omni-7B-AWQ
  - https://huggingface.co/Qwen/Qwen2.5-Omni-7B-GPTQ-Int4
- Git Repo
  - https://github.com/QwenLM/Qwen2.5-Omni

# QwQ-32B

- 2025-03-06: ["QwQ-32B: Embracing the Power of Reinforcement Learning"](https://qwenlm.github.io/blog/qwq-32b/)

## 2025-03-22

### function calling

- https://qwen.readthedocs.io/en/latest/framework/function_call.html
- https://github.com/QwenLM/Qwen/blob/main/examples/function_call_examples.py

# Qwen3

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
6.ollama version is 0.6.5
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

## 2025-05-04

```bash
jazzw@JazzBook:~$ ollama -v
ollama version is 0.6.7
jazzw@JazzBook:~$ ollama run qwen3-8b:q4_k_m
>>> /?
Available Commands:
  /set            Set session variables
  /show           Show model information
  /load <model>   Load a session or model
  /save <model>   Save your current session
  /clear          Clear session context
  /bye            Exit
  /?, /help       Help for a command
  /? shortcuts    Help for keyboard shortcuts

Use """ to begin a multi-line message.

>>> /show
Available Commands:
  /show info         Show details for this model
  /show license      Show model license
  /show modelfile    Show Modelfile for this model
  /show parameters   Show parameters for this model
  /show system       Show system message
  /show template     Show prompt template

>>> /show system
No system message was specified for this model.
>>> /show info
  Model
    architecture        qwen3
    parameters          8.2B
    context length      32768
    embedding length    4096
    quantization        Q4_K_M

  Capabilities
    completion
    tools

  Parameters
    repeat_penalty    1
    stop              "<|im_start|>"
    stop              "<|im_end|>"
    temperature       0.6
    top_k             20
    top_p             0.95

  License
    Apache License
    Version 2.0, January 2004

>>> /show template
{{- if .Messages }}
{{- if or .System .Tools }}<|im_start|>system
{{- if .System }}
{{ .System }}
{{- end }}
{{- if .Tools }}

# Tools

You may call one or more functions to assist with the user query.

You are provided with function signatures within <tools></tools> XML tags:
<tools>
{{- range .Tools }}
{"type": "function", "function": {{ .Function }}}
{{- end }}
</tools>

For each function call, return a json object with function name and arguments within <tool_call></tool_call> XML tags:
<tool_call>
{"name": <function-name>, "arguments": <args-json-object>}
</tool_call>
{{- end }}<|im_end|>
{{ end }}
{{- range $i, $_ := .Messages }}
{{- $last := eq (len (slice $.Messages $i)) 1 -}}
{{- if eq .Role "user" }}<|im_start|>user
{{ .Content }}<|im_end|>
{{ else if eq .Role "assistant" }}<|im_start|>assistant
{{ if .Content }}{{ .Content }}
{{- else if .ToolCalls }}<tool_call>
{{ range .ToolCalls }}{"name": "{{ .Function.Name }}", "arguments": {{ .Function.Arguments }}}
{{ end }}</tool_call>
{{- end }}{{ if not $last }}<|im_end|>
{{ end }}
{{- else if eq .Role "tool" }}<|im_start|>user
<tool_response>
{{ .Content }}
</tool_response><|im_end|>
{{ end }}
{{- if and (ne .Role "assistant") $last }}<|im_start|>assistant
{{ end }}
{{- end }}
{{- else }}
{{- if .System }}<|im_start|>system
{{ .System }}<|im_end|>
{{ end }}{{ if .Prompt }}<|im_start|>user
{{ .Prompt }}<|im_end|>
{{ end }}<|im_start|>assistant
{{ end }}{{ .Response }}{{ if .Response }}<|im_end|>{{ end }}
>>> are you able to call external tool?
<think>
Okay, the user is asking if I can call external tools. Let me think about how to answer this.

First, I need to recall what my capabilities are. I know that I can use tools like Python code execution, but I can't access the internet or external
APIs directly. So, I should clarify that I can't call external tools in the traditional sense.

Wait, but maybe there are some specific tools I can use within the system. For example, if the user is asking about running code, I can do that. But
if they mean external services or APIs, then I can't. I should mention both scenarios.

Also, I should make sure the user understands the limitations. Maybe they're trying to perform a task that requires an external API, so I should let
them know I can't do that but offer to help with other methods.

I should structure the response to first confirm that I can't call external tools, then explain the exceptions like code execution, and finally ask
how I can assist them. That way, the user knows the boundaries but still feels supported.
</think>

I cannot directly call external tools or APIs outside of my system, as I do not have internet access or the ability to interact with external
services. However, I can help you write code or scripts that use external tools (e.g., Python libraries, command-line tools, or APIs) if you provide
the necessary details or instructions. For example:

- If you need to run Python code, I can execute it within my environment.
- If you want to use a specific tool (e.g., `curl`, `wget`, or a library like `requests`), I can guide you on how to implement it.

Let me know what you need, and I’ll do my best to assist!

>>> what is MCP server?
<think>
Okay, the user asked, "what is MCP server?" I need to figure out what they're referring to. MCP could stand for multiple things. Let me think.

First, MCP might be an acronym. Common possibilities include Microsoft Configuration Manager (formerly SMS), which is a systems management tool.
That's a possibility. Alternatively, it could relate to Minecraft, like the Minecraft Pocket Edition server, but that's more of a game server. There's
also the Microsoft Cloud Platform, but that's usually called Azure. Maybe they're referring to a specific service or product.

Wait, the user might be confused because MCP could be a term in different contexts. Let me check the possible meanings. Microsoft Configuration
Manager is a well-known systems management tool used for deploying and managing software, hardware, and operating systems. That's a strong candidate.
Another possibility is the Minecraft server, but the user might be referring to something else.

I should also consider if there's any other context where MCP server is used. For example, in networking, there's a protocol called MCP, but I don't
recall it being a server. Maybe the user is referring to a specific application or service that uses MCP as an acronym. Without more context, it's a
bit tricky.

I should list the main possibilities and explain each to cover the bases. That way, the user can clarify if they meant one of these. Including
Microsoft Configuration Manager and Minecraft Pocket Edition servers makes sense, as those are the two main ones I can think of. Also, mentioning that
MCP could stand for other things depending on the context would be helpful. I should ask for more details if they need a specific explanation.
</think>

The term **"MCP server"** can refer to different things depending on the context. Here are the most common interpretations:

---

### 1. **Microsoft Configuration Manager (MCM) Server**
   - **Full Name**: Microsoft System Center Configuration Manager (SCCM)
   - **Description**: A systems management tool by Microsoft used to manage and deploy software, hardware, and operating systems across enterprise
networks. It allows administrators to:
     - Deploy software updates.
     - Manage user settings and policies.
     - Monitor system health.
     - Automate tasks like patch management.
   - **Use Case**: Often used in IT departments for managing large-scale Windows environments.

---

### 2. **Minecraft Pocket Edition (PE) Server (MCP)**
   - **Context**: In the gaming community, **MCP** can stand for **Minecraft Pocket Edition (PE)**, which is a mobile version of Minecraft. A "MCP
server" might refer to a server hosting a Minecraft PE game.
   - **Note**: This is less likely unless the context is gaming-related. The term "MCP" in this context is more commonly associated with the
**Minecraft modding community** (e.g., **Minecraft Forge** or **Minecraft Mod Pack**).

---

### 3. **Other Possible Interpretations**
   - **MCP in Networking**: A **MCP (Message Control Protocol)** server could exist in niche or proprietary systems, but this is rare.
   - **MCP in Cloud/DevOps**: Some cloud platforms or tools might use "MCP" as an acronym (e.g., **Microsoft Cloud Platform**), but this is not a
server per se.

---

### How to Clarify
If you're referring to a specific tool, service, or context (e.g., IT management, gaming, cloud computing), please provide more details, and I can
give a more precise explanation!

>>> /bye
```

# Qwen3 Coder

- Git Repo
  - https://github.com/QwenLM/Qwen3-Coder
- HuggingFace
  - https://huggingface.co/collections/Qwen/qwen3-coder-687fc861e53c939e52d52d10
  - https://huggingface.co/models?apps=lmstudio&other=base_model:quantized:Qwen%2FQwen3-Coder-30B-A3B-Instruct&sort=trending
  - https://huggingface.co/lmstudio-community/Qwen3-Coder-30B-A3B-Instruct-GGUF
- 2025-07-22:
  - Qwen3-Coder: Agentic Coding in the World
  - https://qwenlm.github.io/blog/qwen3-coder/

## 2025-11-11

- 最近有看到 YouTube 跟一些文章提到整合 Cline 跟 Qwen 3 Coder.
  但根據先前的研究，最小的 30B Q2_K 都大約 16GB 左右，所以目前手邊的硬體跑不動。
  後來在 HuggingFace 上逛了一下，發現了 cerebras_Qwen3-Coder-REAP-25B-A3B-GGUF
- https://huggingface.co/bartowski/cerebras_Qwen3-Coder-REAP-25B-A3B-GGUF
  - 這個把 30B 壓縮到 25B，而最小的 2-bit 是有機會可以塞進 8GB VRAM 顯卡
    | Quant type | File Size|
    |--|--|
    | IQ2_XXS | 6.23 GB |
    | IQ2_XS | 7.11 GB |
    | IQ2_S | 7.19 GB |
    | Q2_K | 8.95 GB |

# Qwen 3.5

- https://huggingface.co/collections/Qwen/qwen35

# Qwen 3.6

- https://huggingface.co/collections/Qwen/qwen36

## Qwen 3.6 35B A3B

最近很熱門的一個模型，特別是想要拿來跑在 6GB 或 8GB 顯卡的地端

### 2026-05-24

- 2026-05-22
  - 8G 視訊記憶體逆天了！RTX3070 成功跑 Qwen3.6-35B 多模態AI大模型！部署教程
  - https://www.freedidi.com/24267.html
- 2026-05-24
  - Qwen3.6-35B-A3B 越獄版來了！目前最強“無審查”開源模型？6G 視訊記憶體都能跑，本地 AI 徹底自由了
  - https://www.freedidi.com/24284.html

# Qwen 3.7

### 2026-05-25

- 2026-05-20
  - Qwen3.7: The Agent Frontier
  - https://qwen.ai/blog?id=qwen3.7
- 2026-05-22
  - Qwen3.7-Max: Features, Benchmarks, and the Agent Frontier
  - https://www.datacamp.com/blog/qwen3-7-max

# Qwen 3.8

- 2026-08-03
  - Qwen3.8-Max: A New Bar for Coding and Cowork
  - https://qwen.ai/blog?id=qwen3.8
- https://huggingface.co/collections/Qwen/qwen38

## Qwen 3.8 27B

- Overview
  - https://www.qwencloud.com/models/qwen3.8-27b
- HuggingFace
  - https://huggingface.co/Qwen/Qwen3.8-27B
- GGUF
  - https://huggingface.co/unsloth/Qwen3.8-27B-GGUF
- 實測：llama.cpp + pi coding agent
  - https://huggingface.co/unsloth/Qwen3.8-27B-GGUF?show_file_info=Qwen3.8-27B-UD-IQ2_XXS.gguf&local-app=pi
```
 4135  [08/24 13:45:09] llama serve -hf unsloth/Qwen3.8-27B-GGUF:UD-IQ2_XXS
 4187  [08/24 18:10:16] llama serve -hf unsloth/Qwen3.8-27B-GGUF:UD-IQ2_XXS
```
```bash
~$ llama serve -hf unsloth/Qwen3.8-27B-GGUF:UD-IQ2_XXS
Downloading mmproj-BF16.gguf ─────────────────────────────────────── 100%
Downloading Qwen3.8-27B-UD-IQ2_XXS.gguf ──────────────────────────── 100%
3.43.292.488 I log_info: verbosity = 3 (adjust with the `-lv N` CLI arg)
3.43.292.692 I device_info:
3.43.299.663 I   - Vulkan0 : AMD Radeon(TM) Graphics (16253 MiB, 15440 MiB free)
3.44.894.828 I   - Vulkan1 : NVIDIA GeForce RTX 4060 Laptop GPU (7956 MiB, 7188 MiB free)
3.44.897.674 I   - CPU     : AMD Ryzen 7 7735HS with Radeon Graphics         (31994 MiB, 16342 MiB free)
3.44.898.364 I system_info: n_threads = 8 (n_threads_batch = 8) / 16 | CPU : SSE3 = 1 | SSSE3 = 1 | AVX = 1 | AVX2 = 1 | F16C = 1 | FMA = 1 | BMI2 = 1 | LLAMAFILE = 1 | OPENMP = 1 | REPACK = 1 |
3.44.898.811 I srv  llama_server: n_parallel is set to auto, using n_parallel = 4 and kv_unified = true
3.44.901.288 I srv          init: running without SSL
3.44.902.371 I srv          init: using 15 threads for HTTP server
3.44.905.995 I srv         start: binding port with default address family
3.44.911.628 I srv  llama_server: loading model
3.44.911.894 I srv    load_model: loading model 'C:\Users\jazzw\.cache\huggingface\hub\models--unsloth--Qwen3.8-27B-GGUF\snapshots\4ca720788d1e01f1bff70c033e0d0028fd02e502\Qwen3.8-27B-UD-IQ2_XXS.gguf'
3.54.721.554 I srv    load_model: [mtmd] estimated worst-case memory usage of mmproj is 1161.02 MiB
3.54.722.776 I common_init_result: fitting params to device memory ...
3.54.722.788 I common_init_result: (for bugs during this step try to reproduce them with -fit off, or provide --verbose logs if the bug only occurs with -fit on)
4.13.696.810 W llama_context: n_ctx_seq (4096) < n_ctx_train (262144) -- the full capacity of the model will not be utilized
4.14.071.733 W sched_reserve: layer 0 is assigned to device CPU but the fused Gated Delta Net tensor is assigned to device Vulkan1 (usually due to missing support)
4.14.071.743 W sched_reserve: fused Gated Delta Net (chunked) not supported, set to disabled
4.14.165.535 I common_init_from_params: warming up the model with an empty run - please wait ... (--no-warmup to disable)
4.22.103.131 W load_hparams: Qwen-VL models require at minimum 1024 image tokens to function correctly on grounding tasks
4.22.103.138 W load_hparams: if you encounter problems with accuracy, try adding --image-min-tokens 1024
4.22.103.138 W load_hparams: more info: https://github.com/ggml-org/llama.cpp/issues/16842

4.23.212.697 I srv    load_model: loaded multimodal model, 'C:\Users\jazzw\.cache\huggingface\hub\models--unsloth--Qwen3.8-27B-GGUF\snapshots\4ca720788d1e01f1bff70c033e0d0028fd02e502\mmproj-BF16.gguf'
4.23.212.718 I srv    load_model: initializing slots, n_slots = 4
4.23.671.707 W srv    load_model: speculative decoding will use checkpoints
4.23.674.827 W common_speculative_init: no implementations specified for speculative decoding
4.23.674.834 I slot   load_model: id  0 | task -1 | new slot, n_ctx = 4096
4.23.674.836 I slot   load_model: id  1 | task -1 | new slot, n_ctx = 4096
4.23.674.837 I slot   load_model: id  2 | task -1 | new slot, n_ctx = 4096
4.23.674.838 I slot   load_model: id  3 | task -1 | new slot, n_ctx = 4096
4.23.674.898 I srv    load_model: prompt cache is enabled, size limit: 8192 MiB
4.23.674.899 I srv    load_model: use `--cache-ram 0` to disable the prompt cache
4.23.674.900 I srv    load_model: for more info see https://github.com/ggml-org/llama.cpp/pull/16391
4.23.674.904 I srv    load_model: context checkpoints enabled, max = 32, min spacing = 256
4.23.674.924 I srv          init: idle slots will be saved to prompt cache and cleared upon starting a new task
4.23.717.815 I init: chat template, example_format: '<|im_start|>system
Reasoning effort is set to xhigh. Please think carefully through the task, validate key assumptions, consider plausible alternatives, and prioritize correctness, consistency, and clarity in the final answer.

You are a helpful assistant<|im_end|>
<|im_start|>user
Hello<|im_end|>
<|im_start|>assistant
<think>

</think>

Hi there<|im_end|>
<|im_start|>user
How are you?<|im_end|>
<|im_start|>assistant
<think>
'
4.23.739.922 I srv          init: init: chat template, thinking = 1
4.23.740.782 I srv  llama_server: model loaded
4.23.740.788 I srv  llama_server: server is listening on http://127.0.0.1:8080
4.23.740.798 I srv  update_slots: all slots are idle
```
- 雖然照著指引，設定 pi 的
```
```
- 進入 pi 以後，用 `/model` 選擇
- 但試了兩個 Prompt 都顯示超過 context window
```bash
 Update Available
 New version 0.84.3 is available. Run pi update
 Changelog: https://pi.dev/changelog
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 Package Updates Available
 Package updates are available. Run pi update --extensions
 Packages:
 - pi-web-access
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

 Model: unsloth/Qwen3.8-27B-GGUF:UD-IQ2_XXS


 使用 python + playwright 首先存取 https://share.google/aimode/c61jOgQXCYJmhkOV9 並將 devtool 的網路互動存成 HAR 檔案


 Error: 400: {"code":400,"message":"request (5827 tokens) exceeds the available context size (4096 tokens), try increasing
 it","type":"exceed_context_size_error","n_prompt_tokens":5827,"n_ctx":4096}


 write a hello world in python


 Error: 400: {"code":400,"message":"request (5838 tokens) exceeds the available context size (4096 tokens), try increasing
 it","type":"exceed_context_size_error","n_prompt_tokens":5838,"n_ctx":4096}

──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
~\AppData\Local\Temp\qwen38-27b-q2
0.0%/128k (auto)                                                                       (llama-cpp) unsloth/Qwen3.8-27B-GGUF:UD-IQ2_XXS
```
- llama.cpp 的 log 也顯示一樣的錯誤訊息
```bash
115.09.901.636 I srv  params_from_: Chat format: peg-native
115.09.913.346 I slot get_availabl: id  3 | task -1 | selected slot by LRU, t_last = -1
115.09.913.355 I srv  get_availabl: updating prompt cache
115.09.913.606 I srv          load:  - looking for better prompt, base f_keep = -1.000, sim = 0.000
115.09.913.611 I srv        update:  - cache state: 0 prompts, 0.000 MiB (limits: 8192.000 MiB, 4096 tokens, 8589934592 est)
115.09.913.614 I srv  get_availabl: prompt cache update took 0.26 ms
115.09.914.418 I reasoning-budget: activated, budget=2147483647 tokens
115.09.914.444 I slot launch_slot_: id  3 | task 0 | processing task, is_child = 0
115.09.914.455 E srv    send_error: task id = 0, error: request (5827 tokens) exceeds the available context size (4096 tokens), try increasing it
115.09.914.459 I slot      release: id  3 | task 0 | stop processing: n_tokens = 0, truncated = 0
115.09.914.462 W srv  update_slots: no tokens to decode
115.09.914.465 I srv  update_slots: all slots are idle
115.09.914.472 W srv          stop: cancel task, id_task = 0
115.09.914.504 I srv  update_slots: all slots are idle
115.49.382.553 I srv  params_from_: Chat format: peg-native
115.49.393.275 I slot get_availabl: id  2 | task -1 | selected slot by LRU, t_last = -1
115.49.393.279 I srv  get_availabl: updating prompt cache
115.49.393.288 I srv          load:  - looking for better prompt, base f_keep = -1.000, sim = 0.000
115.49.393.291 I srv        update:  - cache state: 0 prompts, 0.000 MiB (limits: 8192.000 MiB, 4096 tokens, 8589934592 est)
115.49.393.292 I srv  get_availabl: prompt cache update took 0.01 ms
115.49.393.778 I reasoning-budget: activated, budget=2147483647 tokens
115.49.393.797 I slot launch_slot_: id  2 | task 3 | processing task, is_child = 0
115.49.393.805 E srv    send_error: task id = 3, error: request (5838 tokens) exceeds the available context size (4096 tokens), try increasing it
115.49.393.811 I slot      release: id  2 | task 3 | stop processing: n_tokens = 0, truncated = 0
115.49.393.813 W srv  update_slots: no tokens to decode
115.49.393.815 I srv  update_slots: all slots are idle
115.49.393.822 W srv          stop: cancel task, id_task = 3
115.49.393.849 I srv  update_slots: all slots are idle
```

# Qwen AgentWorld

- 世界模型？
- 2026-06-23
  - Qwen-AgentWorld: Language World Models for General Agents
  - https://qwen.ai/blog?id=qwen-agentworld
- 2026-04-
  - Qwen-AgentWorld: Language World Models for General Agents
  - https://arxiv.org/abs/2606.24597
  - https://huggingface.co/papers/2606.24597 (比較多 Graph 連結 Linked Data)
- https://huggingface.co/collections/Qwen/qwen-agentworld