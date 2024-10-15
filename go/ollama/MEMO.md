# Ollama

- Source: https://github.com/ollama/ollama
- Web site: https://ollama.com/

## 2024-10-15

### Lab #1 -- 在 Google Colab 跑 Ollama

- 測試環境：Google Colab
- 參考：https://medium.com/@abonia/running-ollama-in-google-colab-free-tier-545609258453
- 開啟 https://colab.research.google.com/github/infuseai/colab-xterm/blob/main/demo.ipynb
- 安裝 colab-xterm 以後，在 `%xterm` 的視窗裡安裝 Ollama
```bash
/content# curl https://ollama.ai/install.sh | sh
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0>>> Installing ollama to /usr/local
100 13320    0 13320    0     0  27775      0 --:--:-- --:--:-- --:--:-- 27750
>>> Downloading Linux amd64 bundle
##################################################################################################################################################### 100.0%##################################################################################################################################################### 100.0%
>>> Creating ollama user...
>>> Adding ollama user to video group...
>>> Adding current user to ollama group...
>>> Creating ollama systemd service...
WARNING: Unable to detect NVIDIA/AMD GPU. Install lspci or lshw to automatically detect and install GPU dependencies.
>>> The Ollama API is now available at 127.0.0.1:11434.
>>> Install complete. Run "ollama" from the command line.
/content# lspci
bash: lspci: command not found
/content# apt-get -y install lshw
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  pci.ids usb.ids
The following NEW packages will be installed:
  lshw pci.ids usb.ids
0 upgraded, 3 newly installed, 0 to remove and 49 not upgraded.
Need to get 790 kB of archives.
After this operation, 2,988 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu jammy/main amd64 lshw amd64 02.19.git.2021.06.19.996aaad9c7-2build1 [321 kB]
Get:2 http://archive.ubuntu.com/ubuntu jammy/main amd64 pci.ids all 0.0~2022.01.22-1 [251 kB]
Get:3 http://archive.ubuntu.com/ubuntu jammy/main amd64 usb.ids all 2022.04.02-1 [219 kB]
Fetched 790 kB in 1s (1,246 kB/s)
Selecting previously unselected package lshw.
(Reading database ... 123621 files and directories currently installed.)
Preparing to unpack .../lshw_02.19.git.2021.06.19.996aaad9c7-2build1_amd64.deb ...
Unpacking lshw (02.19.git.2021.06.19.996aaad9c7-2build1) ...
Selecting previously unselected package pci.ids.
Preparing to unpack .../pci.ids_0.0~2022.01.22-1_all.deb ...
Unpacking pci.ids (0.0~2022.01.22-1) ...
Selecting previously unselected package usb.ids.
Preparing to unpack .../usb.ids_2022.04.02-1_all.deb ...
Unpacking usb.ids (2022.04.02-1) ...
Setting up pci.ids (0.0~2022.01.22-1) ...
Setting up lshw (02.19.git.2021.06.19.996aaad9c7-2build1) ...
Setting up usb.ids (2022.04.02-1) ...
Processing triggers for man-db (2.10.2-1) ...
/content# 
/content# whoami
root
/content# 
```
- 
```
/content# ollama serve &
[1] 4951
/content# Couldn't find '/root/.ollama/id_ed25519'. Generating new private key.
Your new public key is: 

ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICbuazAXhCQ1plZ/3iB8NVjBg1dqoh2tVR4xKvad5jCp

2024/10/15 09:17:27 routes.go:1158: INFO server config env="map[CUDA_VISIBLE_DEVICES: GPU_DEVICE_ORDINAL: HIP_VISIBLE_DEVICES: HSA_OVERRIDE_GFX_VERSION: HTTPS_PROXY: HTTP_PROXY: NO_PROXY: OLLAMA_DEBUG:false OLLAMA_FLASH_ATTENTION:false OLLAMA_GPU_OVERHEAD:0 OLLAMA_HOST:http://127.0.0.1:11434 OLLAMA_INTEL_GPU:false OLLAMA_KEEP_ALIVE:5m0s OLLAMA_LLM_LIBRARY: OLLAMA_LOAD_TIMEOUT:5m0s OLLAMA_MAX_LOADED_MODELS:0 OLLAMA_MAX_QUEUE:512 OLLAMA_MODELS:/root/.ollama/models OLLAMA_MULTIUSER_CACHE:false OLLAMA_NOHISTORY:false OLLAMA_NOPRUNE:false OLLAMA_NUM_PARALLEL:0 OLLAMA_ORIGINS:[http://localhost https://localhost http://localhost:* https://localhost:* http://127.0.0.1 https://127.0.0.1 http://127.0.0.1:* https://127.0.0.1:* http://0.0.0.0 https://0.0.0.0 http://0.0.0.0:* https://0.0.0.0:* app://* file://* tauri://*] OLLAMA_SCHED_SPREAD:false OLLAMA_TMPDIR: ROCR_VISIBLE_DEVICES: http_proxy: https_proxy: no_proxy:]"
time=2024-10-15T09:17:27.814Z level=INFO source=images.go:754 msg="total blobs: 0"
time=2024-10-15T09:17:27.814Z level=INFO source=images.go:761 msg="total unused blobs removed: 0"
time=2024-10-15T09:17:27.814Z level=INFO source=routes.go:1205 msg="Listening on 127.0.0.1:11434 (version 0.3.13)"
time=2024-10-15T09:17:27.815Z level=INFO source=common.go:135 msg="extracting embedded files" dir=/tmp/ollama2899235374/runners

/content# 
/content# time=2024-10-15T09:18:18.263Z level=INFO source=common.go:49 msg="Dynamic LLM libraries" runners="[cpu cpu_avx cpu_avx2 cuda_v11 cuda_v12 rocm_v60102]"
time=2024-10-15T09:18:18.264Z level=INFO source=gpu.go:199 msg="looking for compatible GPUs"
time=2024-10-15T09:18:18.299Z level=INFO source=gpu.go:347 msg="no compatible GPUs were discovered"
time=2024-10-15T09:18:18.299Z level=INFO source=types.go:107 msg="inference compute" id=0 library=cpu variant=avx2 compute="" driver=0.0 name="" total="12.7 GiB" available="11.5 GiB"

```
- ( 2024-10-15 17:21:12 )
- 預設只有用 CPU, 會比較慢。改 Runtime 成 `T4 v2-8` 試試看
```bash
/content# ollama
bash: ollama: command not found
/content# curl https://ollama.ai/install.sh | sh
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0>>> Installing ollama to /usr/local
100 13320    0 13320    0     0  52785      0 --:--:-- --:--:-- --:--:-- 52857
>>> Downloading Linux amd64 bundle
##################################################################################################################################################### 100.0%##################################################################################################################################################### 100.0%
>>> Creating ollama user...
>>> Adding ollama user to video group...
>>> Adding current user to ollama group...
>>> Creating ollama systemd service...
WARNING: Unable to detect NVIDIA/AMD GPU. Install lspci or lshw to automatically detect and install GPU dependencies.
>>> The Ollama API is now available at 127.0.0.1:11434.
>>> Install complete. Run "ollama" from the command line.
/content# apt-get -y install lspci
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
E: Unable to locate package lspci
/content# apt-get update; apt-get -y install lshw
Get:1 https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/ InRelease [3,626 B]
Ign:2 https://r2u.stat.illinois.edu/ubuntu jammy InRelease                                                                                                  
Get:3 https://r2u.stat.illinois.edu/ubuntu jammy Release [5,713 B]                                                                                          
Get:4 http://security.ubuntu.com/ubuntu jammy-security InRelease [129 kB]                                                               
Get:5 https://r2u.stat.illinois.edu/ubuntu jammy Release.gpg [793 B]                                                                   
Hit:6 http://archive.ubuntu.com/ubuntu jammy InRelease                                                                                             
Get:7 http://archive.ubuntu.com/ubuntu jammy-updates InRelease [128 kB]                                           
Get:8 https://r2u.stat.illinois.edu/ubuntu jammy/main all Packages [8,387 kB]             
Hit:9 https://ppa.launchpadcontent.net/ubuntugis/ppa/ubuntu jammy InRelease                                                
Get:10 https://r2u.stat.illinois.edu/ubuntu jammy/main amd64 Packages [2,595 kB]                                           
Get:11 http://security.ubuntu.com/ubuntu jammy-security/universe amd64 Packages [1,160 kB]   
Hit:12 http://archive.ubuntu.com/ubuntu jammy-backports InRelease                
Get:13 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 Packages [2,602 kB]
Get:14 http://security.ubuntu.com/ubuntu jammy-security/main amd64 Packages [2,326 kB]        
Get:15 http://archive.ubuntu.com/ubuntu jammy-updates/universe amd64 Packages [1,449 kB]
Fetched 18.8 MB in 2s (10.0 MB/s)                                                                
Reading package lists... Done
W: Skipping acquire of configured file 'main/source/Sources' as repository 'https://r2u.stat.illinois.edu/ubuntu jammy InRelease' does not seem to provide it (sources.list entry misspelt?)
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  pci.ids usb.ids
The following NEW packages will be installed:
  lshw pci.ids usb.ids
0 upgraded, 3 newly installed, 0 to remove and 2 not upgraded.
Need to get 790 kB of archives.
After this operation, 2,988 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu jammy/main amd64 lshw amd64 02.19.git.2021.06.19.996aaad9c7-2build1 [321 kB]
Get:2 http://archive.ubuntu.com/ubuntu jammy/main amd64 pci.ids all 0.0~2022.01.22-1 [251 kB]
Get:3 http://archive.ubuntu.com/ubuntu jammy/main amd64 usb.ids all 2022.04.02-1 [219 kB]
Fetched 790 kB in 1s (759 kB/s)  
Selecting previously unselected package lshw.
(Reading database ... 119626 files and directories currently installed.)
Preparing to unpack .../lshw_02.19.git.2021.06.19.996aaad9c7-2build1_amd64.deb ...
Unpacking lshw (02.19.git.2021.06.19.996aaad9c7-2build1) ...
Selecting previously unselected package pci.ids.
Preparing to unpack .../pci.ids_0.0~2022.01.22-1_all.deb ...
Unpacking pci.ids (0.0~2022.01.22-1) ...
Selecting previously unselected package usb.ids.
Preparing to unpack .../usb.ids_2022.04.02-1_all.deb ...
Unpacking usb.ids (2022.04.02-1) ...
Setting up pci.ids (0.0~2022.01.22-1) ...
Setting up lshw (02.19.git.2021.06.19.996aaad9c7-2build1) ...
Setting up usb.ids (2022.04.02-1) ...
Processing triggers for man-db (2.10.2-1) ...

/content# curl https://ollama.ai/install.sh | sh
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0>>> Installing ollama to /usr/local
100 13320    0 13320    0     0  12516      0 --:--:--  0:00:01 --:--:-- 12518
>>> Downloading Linux amd64 bundle
##################################################################################################################################################### 100.0%##################################################################################################################################################### 100.0%
>>> Adding ollama user to video group...
>>> Adding current user to ollama group...
>>> Creating ollama systemd service...
>>> The Ollama API is now available at 127.0.0.1:11434.
>>> Install complete. Run "ollama" from the command line.
WARNING: No NVIDIA/AMD GPU detected. Ollama will run in CPU-only mode.
>>> The Ollama API is now available at 127.0.0.1:11434.
>>> Install complete. Run "ollama" from the command line.
```
- 從 `WARNING: No NVIDIA/AMD GPU detected. Ollama will run in CPU-only mode.` 看來，Ollama 在 colab 只能做陽春的實驗，因為無法使用 Google 的 `TPU`
- ( 2024-10-15 17:27:10 )
- 實驗 Llama 3.2 2b 模型
```bash
/content# ollama serve &
[1] 3754
/content# 
/content# Couldn't find '/root/.ollama/id_ed25519'. Generating new private key.
Your new public key is: 

ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJ4vbJSYREk43yQDwAUWkZqvQmbE/PHYZfhOTAyNGro6

2024/10/15 09:28:46 routes.go:1158: INFO server config env="map[CUDA_VISIBLE_DEVICES: GPU_DEVICE_ORDINAL: HIP_VISIBLE_DEVICES: HSA_OVERRIDE_GFX_VERSION: HTTPS_PROXY: HTTP_PROXY: NO_PROXY: OLLAMA_DEBUG:false OLLAMA_FLASH_ATTENTION:false OLLAMA_GPU_OVERHEAD:0 OLLAMA_HOST:http://127.0.0.1:11434 OLLAMA_INTEL_GPU:false OLLAMA_KEEP_ALIVE:5m0s OLLAMA_LLM_LIBRARY: OLLAMA_LOAD_TIMEOUT:5m0s OLLAMA_MAX_LOADED_MODELS:0 OLLAMA_MAX_QUEUE:512 OLLAMA_MODELS:/root/.ollama/models OLLAMA_MULTIUSER_CACHE:false OLLAMA_NOHISTORY:false OLLAMA_NOPRUNE:false OLLAMA_NUM_PARALLEL:0 OLLAMA_ORIGINS:[http://localhost https://localhost http://localhost:* https://localhost:* http://127.0.0.1 https://127.0.0.1 http://127.0.0.1:* https://127.0.0.1:* http://0.0.0.0 https://0.0.0.0 http://0.0.0.0:* https://0.0.0.0:* app://* file://* tauri://*] OLLAMA_SCHED_SPREAD:false OLLAMA_TMPDIR: ROCR_VISIBLE_DEVICES: http_proxy: https_proxy: no_proxy:]"
time=2024-10-15T09:28:46.185Z level=INFO source=images.go:754 msg="total blobs: 0"
time=2024-10-15T09:28:46.185Z level=INFO source=images.go:761 msg="total unused blobs removed: 0"
time=2024-10-15T09:28:46.185Z level=INFO source=routes.go:1205 msg="Listening on 127.0.0.1:11434 (version 0.3.13)"
time=2024-10-15T09:28:46.185Z level=INFO source=common.go:135 msg="extracting embedded files" dir=/tmp/ollama1573333462/runners

/content# 
/content# time=2024-10-15T09:28:57.961Z level=INFO source=common.go:49 msg="Dynamic LLM libraries" runners="[cpu_avx cpu_avx2 cuda_v11 cuda_v12 rocm_v60102 cpu]"
time=2024-10-15T09:28:57.961Z level=INFO source=gpu.go:199 msg="looking for compatible GPUs"
time=2024-10-15T09:28:57.993Z level=INFO source=gpu.go:347 msg="no compatible GPUs were discovered"
time=2024-10-15T09:28:57.993Z level=INFO source=types.go:107 msg="inference compute" id=0 library=cpu variant=avx2 compute="" driver=0.0 name="" total="334.6 GiB" available="330.1 GiB"

/content# ollama pull llama3.2
/content# ollama serve &
```
- 用 LangChain 去測試：
```python
!ollama list

NAME               ID              SIZE      MODIFIED      
llama3.2:latest    a80c4f17acd5    2.0 GB    5 minutes ago    

%pip install -U langchain-ollama

from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

template = """Question: {question}

Answer: Let's think step by step."""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="llama3.2")

chain = prompt | model

chain.invoke({"question": "What is MoE in AI?"})
```
- 回應：
```
Let's break it down.

MoE stands for Meta Optimizer, but I believe you might be referring to Multi-Objective Optimization (MoO), which is related to the concept of Multi-Objectives in Machine Learning and AI.

However, another possibility is MoE being an acronym for a specific algorithm or technique used in some AI applications. 

Could you please clarify or provide more context about MoE in AI?
```
