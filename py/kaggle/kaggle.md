# Kaggle API

- https://github.com/Kaggle/kaggle-api

> Official Kaggle API

# kaggle-cli

- Git Repo
  - https://github.com/Kaggle/kaggle-cli

```
pip install kaggle
```

## 2024-12-28

- 在 https://www.kaggle.com/competitions/wsdm-cup-multilingual-chatbot-arena/data 看到這一行

```
kaggle competitions download -c wsdm-cup-multilingual-chatbot-arena
```

- 猜想應該是有 CLI 指令，所以查了一下。有兩個實作：
  - https://github.com/Kaggle/kaggle-api (Kaggle 官方的)
  - https://github.com/floydwch/kaggle-cli (An unofficial Kaggle command line tool - 已於 2024-01-28 設為 `Archived`)

### 安裝

```bash
@jazzwang ➜ /workspaces/snippet (master) $ pip install kaggle
@jazzwang ➜ /workspaces/snippet (master) $ which kaggle
/home/codespace/.python/current/bin/kaggle
```

### 下載資料集

```bash
@jazzwang ➜ /workspaces/snippet (master) $ kaggle competitions download -c wsdm-cup-multilingual-chatbot-arena
Traceback (most recent call last):
  File "/home/codespace/.python/current/bin/kaggle", line 5, in <module>
    from kaggle.cli import main
  File "/home/codespace/.python/current/lib/python3.10/site-packages/kaggle/__init__.py", line 7, in <module>
    api.authenticate()
  File "/home/codespace/.python/current/lib/python3.10/site-packages/kaggle/api/kaggle_api_extended.py", line 407, in authenticate
    raise IOError('Could not find {}. Make sure it\'s located in'
OSError: Could not find kaggle.json. Make sure it's located in /home/codespace/.config/kaggle. Or use the environment method. See setup instructions at https://github.com/Kaggle/kaggle-api/
```
- ( 2024-12-28 12:01:34 )
- 看樣子需要設定 `~/.config/kaggle/kaggle.json`
- ( 2024-12-28 15:42:49 )
- 參考: https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md#api-credentials
- 到 https://www.kaggle.com/settings/account 搜尋 `Create API Token`，點選後就會下載 `kaggle.json`
- 因為 Github Codespace 的家目錄基本上是會被抹除的，所以不好把 `kaggle.json` 上傳到 `/home/codespace/.config/kaggle`
- 根據文件，替代方案是設定環境變數：
```bash
export KAGGLE_USERNAME=datadinosaur
export KAGGLE_KEY=xxxxxxxxxxxxxx
```
- 實際測驗一次，確實可以下載 competition 的 dataset
```bash
@jazzwang ➜ /workspaces/snippet (master) $ export KAGGLE_USERNAME=jazzwang
@jazzwang ➜ /workspaces/snippet (master) $ export KAGGLE_KEY=略略略略略
@jazzwang ➜ /workspaces/snippet (master) $ kaggle competitions download -c wsdm-cup-multilingual-chatbot-arena
Downloading wsdm-cup-multilingual-chatbot-arena.zip to /workspaces/snippet
 91%|████████████████████████████████████████████████████████████████████████████████████████████████████████▍          | 98.0M/108M [00:01<00:00, 86.8MB/s]
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 108M/108M [00:01<00:00, 67.3MB/s]
@jazzwang ➜ /workspaces/snippet (master) $ unzip wsdm-cup-multilingual-chatbot-arena.zip
Archive:  wsdm-cup-multilingual-chatbot-arena.zip
  inflating: sample_submission.csv
  inflating: test.parquet
  inflating: train.parquet
```
- 挺有趣的，dataset 居然是 CSV + parquet 格式。
- 根據 https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md#commands 有不同的指令
```
@jazzwang ➜ /workspaces/snippet (master) $ kaggle --help
usage: kaggle [-h] [-v] [-W] {competitions,c,datasets,d,kernels,k,models,m,files,f,config} ...

options:
  -h, --help            show this help message and exit
  -v, --version         Print the Kaggle API version
  -W, --no-warn         Disable out-of-date API version warning

commands:
  {competitions,c,datasets,d,kernels,k,models,m,files,f,config}
                        Use one of:
                        competitions {list, files, download, submit, submissions, leaderboard}
                        datasets {list, files, download, create, version, init, metadata, status}
                        kernels {list, files, init, push, pull, output, status}
                        models {instances, get, list, init, create, delete, update}
                        models instances {versions, get, files, init, create, delete, update}
                        models instances versions {init, create, download, delete, files}
                        config {view, set, unset}
    competitions (c)    Commands related to Kaggle competitions
    datasets (d)        Commands related to Kaggle datasets
    kernels (k)         Commands related to Kaggle kernels
    models (m)          Commands related to Kaggle models
    files (f)           Commands related files
    config              Configuration settings
```
- 測試查詢 models，看起來還真不少呀！！
```bash
@jazzwang ➜ /workspaces/snippet (master) $ kaggle models list
Next Page Token = CfDJ8L3o_FPsMQlKvPRAcaVvXWOGjDVlrsv754XkIVgNzsHChWIMMsXnCzGZlJP4xf9O5kaIseaBCMomgLo5W-uXuTw
    id  ref                                 title                 subtitle
                                                                                                                                   author
------  ----------------------------------  --------------------  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  ---------
176602  qwen-lm/qwq-32b-preview             QwQ-32B-Preview       QwQ-32B-Preview is an experimental research model developed by the Qwen Team, focused on advancing AI reasoning capabilities.                                                                                                QwenLM
164048  qwen-lm/qwen2.5                     Qwen2.5               Qwen2.5 is the latest series of Qwen large language models. Qwen2.5 has a number of base language models and instruction-tuned language models ranging from 0.5 to 72 billion parameters.                                    QwenLM
164716  google/paligemma-2                  PaliGemma 2           The PaliGemma family of models is inspired by PaLI-3 and based on open components such as the SigLIP vision model and Gemma 2 language models.                                                                               Google
172131  shelterw/qwen2.5                    Qwen2.5
                                                                                                                                   ShelterW
184945  google/gemini-2.0-flash-api         Gemini 2.0 Flash API  A new family of multimodal models from Google DeepMind
                                                                                                                                   Google
 76277  google/gemma-2                      Gemma 2               Gemma is a family of lightweight, state-of-the-art open models from Google, built from the same research and technology used to create the Gemini models.                                                                    Google
161088  qwen-lm/qwen2.5-coder               Qwen2.5 Coder         Qwen2.5-Coder is the latest series of Code-Specific Qwen large language models, Qwen2.5-Coder has covered six mainstream model sizes, 0.5, 1.5, 3, 7, 14, 32 billion parameters, to meet the needs of different developers.  QwenLM
171919  keras/paligemma2                    PaliGemma 2           Keras implementation of the PaliGemma 2 model. This Keras 3 implementation will run on JAX, TensorFlow and PyTorch.                                                                                                          Keras
  3301  google/gemma                        Gemma                 Gemma is a family of lightweight, open models built from the research and technology that Google used to create the Gemini models.                                                                                           Google
171434  anhvth226/qw14b-awq                 qw14b-awq
                                                                                                                                   Anh Vo
188868  metaresearch/llama-3.3              Llama 3.3             The Meta Llama 3.3 multilingual large language model (LLM) is an instruction tuned generative model in 70B (text in/text out).                                                                                               Meta
196275  qwen-lm/qvq-72b-preview             QVQ-72B-Preview       QVQ-72B-Preview is an experimental research model developed by the Qwen team, focusing on enhancing visual reasoning capabilities.                                                                                           QwenLM
171421  anhvth226/2211-lora-14b             2211-lora-14b
                                                                                                                                   Anh Vo
165390  trainld/qwen2.5-14                  qwen2.5-14
                                                                                                                                   trainLD
168862  xuanleekaggle/jane-street-5-and-7_  jane street 5&7_
                                                                                                                                   Fire Bird
163622  Microsoft/phi-3                     Phi-3                 Tiny but Mighty: The Phi-3 small language models with big potential.
                                                                                                                                   Microsoft
167966  thelionai/medimageinsight           MedImageInsight       Open-Source Medical Image Embedding Model
                                                                                                                                   thelionai
  3533  keras/gemma                         Gemma                 Keras implementation of the Gemma model. This Keras 3 implementation will run on JAX, TensorFlow and PyTorch.                                                                                                                Keras
169361  qwen-lm/qwen2.5-math                Qwen2.5 Math          Qwen2.5-Math series is expanded to support using both CoT and Tool-integrated Reasoning (TIR) to solve math problems in both Chinese and English.                                                                            QwenLM
 62319  google/gemini-1.5-flash-api         Gemini 1.5 Flash API  A new family of multimodal models from Google DeepMind
                                                                                                                                   Google
```
- 比較特殊的是看到這個訊息：
```
Next Page Token = CfDJ8L3o_FPsMQlKvPRAcaVvXWOGjDVlrsv754XkIVgNzsHChWIMMsXnCzGZlJP4xf9O5kaIseaBCMomgLo5W-uXuTw
```
- 代表這些 Model 存在類似 Athena 這種 Lakehouse 裡？既然是 Google 的，那會是放在 BigQuery？
- API 實作 pagination 確實是常見的作法，但目前從文件沒特別看到怎麼用 `Page Token`

### 下載模型

- 若使用 `models get` 拿到的只有 metadata (JSON) 字串
```bash
@jazzwang ➜ /workspaces/snippet (master) $ kaggle m get google/gemma
```
- 從 https://www.kaggle.com/models/google/codegemma 按 `Download` 在「同意」授權以後，可以選擇不同方式下載模型，我選 Kaggle CLI 後，顯示要用以下指令
```bash
#!/bin/bash
kaggle models instances versions download keras/codegemma/keras/code_gemma_2b_en/2
```
```bash
@jazzwang ➜ /workspaces/snippet (master) $ cd /tmp
@jazzwang ➜ /tmp $ kaggle models instances versions download keras/codegemma/keras/code_gemma_2b_en/2
Downloading codegemma.tar.gz to /tmp
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████▊| 3.73G/3.74G [00:44<00:00, 136MB/s]
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 3.74G/3.74G [00:44<00:00, 90.4MB/s]
```
- 這個沒有選格式，應該是 `Keras` 的版本。從指令可以看得出來：
```
                                            +---- keras (organization?)
                                            |       +----- model family
                                            |       |       +----- model format
                                            |       |       |        +------ model name (包含多少參數)
                                            |       |       |        |           +----- version
                                            |       |       |        |           |
kaggle models instances versions download keras/codegemma/keras/code_gemma_2b_en/2
```
- 如果在 Model 頁面選擇 GGUF 並選擇用 `cURL` 指令下載，顯示的指令是
```bash
#!/bin/bash
# Export your Kaggle username and API key
# export KAGGLE_USERNAME=<YOUR USERNAME>
# export KAGGLE_KEY=<YOUR KAGGLE KEY>

curl -L -u $KAGGLE_USERNAME:$KAGGLE_KEY\
  -o ~/Downloads/model.tar.gz\
  https://www.kaggle.com/ai/v1/models/google/codegemma/gguf/1.1-2b/1/download
```
- 看起來 Model 格式有 Keras, PyTorch, Transformers, Gemma C++, GGUF, Flax 這麼多種格式。

### 初步測試感想

- 測試了 Kaggle CLI 才突然覺得 Kaggle 跟 HuggingFace 的概念有點像，都有 Dataset, Model 跟 Code 的部份。
  - 不同的是 HuggingFace 的 Code Space 是類似 Github 的 Git repo，而 Kaggle 的 Code 就都是 Python Notebook
  - 在 HuggingFace 比較常看到 Transformers 格式的 Model

## 2026-06-14

- Learned from Kaggle Discord
  - 2026-05-28
  - Kaggle CLI Update: Forums, Competition Topics, Benchmarks, and OAuth! (v2.2.0)
  - https://www.kaggle.com/discussions/product-announcements/702989
- 安裝 - 文件是寫 `pip install kaggle` 我先試試看用 `uv` 安裝看看
```bash
~/git/snippet$ uv tool install kaggle
```
- 驗證
```bash
~/git/snippet$ which kaggle
/c/Users/jazzw/scoop/persist/uv/tools/shims/kaggle
~/git/snippet$ kaggle -h
usage: python.exe C:\Users\jazzw\scoop\persist\uv\tools\shims\kaggle [-h] [-v] [-W]
                                                                     {competitions,c,datasets,d,kernels,k,models,m,files,forums,f,benchmarks,b,config,auth,quota} ...

options:
  -h, --help            show this help message and exit
  -v, --version         Print the Kaggle CLI version
  -W, --no-warn         Disable out-of-date API version warning

commands:
  {competitions,c,datasets,d,kernels,k,models,m,files,forums,f,benchmarks,b,config,auth,quota}
                        Use one of:
                        competitions {list, files, download, submit, submissions, leaderboard, team-submissions, episodes, replay, logs, pages, topics, topic-messages}
                        competitions topics {list, show}
                        datasets {list, files, download, create, version, init, metadata, status, delete, topics}
                        datasets topics {list, show}
                        kernels {list, files, get, init, push, pull, output, status, logs, update, delete}
                        models {instances, i, variations, v, get, list, init, create, delete, update, topics}
                        models topics {list, show}
                        models variations {versions, v, get, files, list, init, create, delete, update}
                        models variations versions {init, create, download, delete, files, list}
                        forums {list, topics}
                        forums topics {list, show}
                        benchmarks {tasks, t, auth, init, topics}
                        benchmarks topics {list, show}
                        config {view, set, unset}
                        auth {login, print-access-token, revoke}
                        quota
    competitions (c)    Commands related to Kaggle competitions
    datasets (d)        Commands related to Kaggle datasets
    kernels (k)         Commands related to Kaggle kernels
    models (m)          Commands related to Kaggle models
    files               Commands related files
    forums (f)          Commands related to Kaggle discussion forums
    benchmarks (b)      Commands related to Kaggle benchmarks
    config              Configuration settings
    auth                Commands related to authentication
    quota               Show the current user's weekly GPU and TPU accelerator quota
```
- 登入
```bash
~/git/snippet$ kaggle auth
Authentication required to call the Kaggle API.

First, you will need a Kaggle account. You can sign up at
  https://www.kaggle.com/account/login

Recommended: log in with OAuth via a web-based authorization flow.
No token to manage; credentials are cached locally for you.
    kaggle auth login

If you'd rather not use OAuth, generate an API token at
  https://www.kaggle.com/settings/api  (click "Generate New Token" under "API")
and supply it to the CLI in one of these ways:

  Option A: Environment variable
    export KAGGLE_API_TOKEN=xxxxxxxxxxxxxx  # token copied from the settings UI

  Option B: API token file
    Save the token to ~/.kaggle/access_token
~/git/snippet$ kaggle auth login
Your browser has been opened to visit: ...
You are now logged in as [jazzwang]
```
- 論壇
```bash
~/git/snippet$ kaggle forums list
     id  name                   subtitle
-------  ---------------------  -----------------------------------------------------
     15  General                Announcements, resources, and interesting discussions
    208  Getting Started        The first stop for new Kagglers
    809  Product Feedback       Tell us what you love, hate, and wish for
    978  Product Announcements  New product features & updates from the Kaggle Team
   2239  Questions & Answers    Technical advice from other data scientists
2605300  Competition Hosting    Advice and support on running your own competitions
3831795  Accomplishments        Celebrate success, share achievements!
~/git/snippet$ kaggle forums topics list
    id  title                                                                                      authorName               commentCount  votes  postDate   
------  -----------------------------------------------------------------------------------------  -----------------------  ------------  -----  --------------------------
708114  [Welcome + Setup Instructions] 5-Day AI Agents: Intensive Vibe Coding Course With Google   Kinjal Parekh                       0    206  2026-06-13 16:43:49.614000
708107  Codelabs FAQs                                                                              Kinjal Parekh                       0     95  2026-06-13 15:36:54.249000
```
- 論壇：應景一下 2026-06-13 的 5-Day AI Agents 開課公告
```bash
~/git/snippet$ kaggle forums topics show 708114
Topic #708114: [Welcome + Setup Instructions] 5-Day AI Agents: Intensive Vibe Coding Course With Google
  Author: Kinjal Parekh
  Posted: 2026-06-13 16:43:49.614000
  Votes: 206  Comments: 0

Welcome to our 5-Day AI Agents: Intensive Vibe Coding Course With Google!

Here’s a brief summary of how the course works and detailed instructions on how to get set up. You’ll receive your first assignment on Sunday, June 14, 2026.

How the Course Works

The course is designed to be flexible and interactive, allowing you to learn at your own pace while benefiting from live sessions and community engagement.
```
- Benchmark
  - 2026-06-04
  - Build AI Evals Locally with Kaggle Benchmarks
    - https://www.youtube.com/watch?v=c7B8vyehyUA
      - 👉 Install the write-kaggle-benchmarks skill: https://github.com/Kaggle/kaggle-skills/tree/main/write-kaggle-benchmarks
      - 👉 Get started on: https://www.kaggle.com/benchmarks
  - Build Kaggle Benchmarks from your own local dev environment — with your AI agent
    - https://www.kaggle.com/blog/build-kaggle-benchmarks-local-dev 
```bash
~/git/snippet$ kaggle benchmarks -h
usage: python.exe C:\Users\jazzw\scoop\persist\uv\tools\shims\kaggle benchmarks [-h] {tasks,t,auth,init,topics} ...

options:
  -h, --help            show this help message and exit

commands:
  {tasks,t,auth,init,topics}
    tasks (t)           Commands related to benchmark tasks
    auth                Fetch and persist Model Proxy credential information
    init                Fetch and persist  Model Proxy credentials and other Kaggle Benchmarks environment variables
    topics              List discussion topics for a benchmark
```