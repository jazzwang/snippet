# cortex.cpp

> Local AI API Platform

- Git Repo
  - https://github.com/menloresearch/cortex.cpp
- Website:
  - https://cortex.so/

## 2025-03-26

- 緣起：
  - 在測試 [Unsloth Qwen 2.5 7B 的 Fine-tune Notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen2.5_(7B)-Alpaca.ipynb) 時，有寫到用 Jan 或 OpenWebUI
  - 從 [Jan](https://github.com/menloresearch/jan) 的 README 看到關於 Cortex.cpp 的連結。
- 從 README 看起來，整體很像 Ollama。從底下這段 Jan README 關於 `Cortex.cpp` 的描述，確認是定位成 Ollama 的 alternative。

> [!NOTE]
>
> ### Cortex.cpp
>
> Jan is powered by **Cortex.cpp**. It is a C++ command-line interface (CLI) designed as <mark>an alternative to [Ollama](https://ollama.com/)</mark>. By default, it runs on the llama.cpp engine but also supports other engines, including ONNX and TensorRT-LLM, making it a multi-engine platform.
>
> -   [Cortex Website](https://cortex.so/)
> -   [Cortex GitHub](https://github.com/menloresearch/cortex.cpp)
> -   [Documentation](https://cortex.so/docs/)
> -   [Models Library](https://cortex.so/models)
> -   API Reference: *Under development*
>

### Install 安裝

- 在 Github Codespace 裡面測試一下
  - 大致上除非有很強的誘因，不然我應該還是會繼續用 Ollama (考量使用者社群的群聚現象，以及新功能支援的開發者人數)
```bash
jazzw@JazzBook:~$ blank ssh
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 6.8.0-1021-azure x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro
Last login: Mon Mar 24 00:35:43 2025 from ::1
@jazzwang ➜ /workspaces/codespaces-blank $ wget -O cortexcpp.deb https://app.cortexcpp.com/download/latest/linux-amd64-local
@jazzwang ➜ /workspaces/codespaces-blank $ sudo dpkg -i cortexcpp.deb
Selecting previously unselected package cortexcpp.
(Reading database ... 70175 files and directories currently installed.)
Preparing to unpack cortexcpp.deb ...
Unpacking cortexcpp (1.0.12) ...

dpkg: dependency problems prevent configuration of cortexcpp:
 cortexcpp depends on openmpi-bin; however:
  Package openmpi-bin is not installed.
 cortexcpp depends on libopenmpi-dev; however:
  Package libopenmpi-dev is not installed.

dpkg: error processing package cortexcpp (--install):
 dependency problems - leaving unconfigured
Errors were encountered while processing:
 cortexcpp
```
- 挺有趣的，因為用到 `OpenMPI` ?? 這應該是為了平行化，支援多台電腦叢集。
```
@jazzwang ➜ /workspaces/codespaces-blank $ sudo apt-get -y install openmpi-bin libopenmpi-dev
Reading package lists... Done
Building dependency tree
Reading state information... Done
You might want to run 'apt --fix-broken install' to correct these.
The following packages have unmet dependencies:
 libopenmpi-dev : Depends: gfortran-mod-15
                  Depends: libopenmpi3 (= 4.0.3-0ubuntu1) but it is not going to be installed
                  Depends: openmpi-common (>= 4.0.3-0ubuntu1) but it is not going to be installed
                  Depends: libibverbs-dev (>= 1.1.7) but it is not going to be installed
                  Depends: libhwloc-dev but it is not going to be installed
                  Depends: libevent-dev but it is not going to be installed
                  Recommends: libcoarrays-openmpi-dev but it is not going to be installed
 openmpi-bin : Depends: libopenmpi3 (>= 4.0.3) but it is not going to be installed
               Depends: openmpi-common (>= 4.0.3-0ubuntu1) but it is not going to be installed
E: Unmet dependencies. Try 'apt --fix-broken install' with no packages (or specify a solution).
@jazzwang ➜ /workspaces/codespaces-blank $ sudo apt --fix-broken install
@jazzwang ➜ /workspaces/codespaces-blank $ dpkg -l | grep cortex
ii  cortexcpp                        1.0.12                            amd64        Cortex
```
```bash
Setting up cortexcpp (1.0.12) ...
Download cortex.llamacpp engines by default for user codespace
Config file not found. Creating one at /home/codespace/.cortexrc
Default data folder path: /home/codespace/cortexcpp
IsEngineVariantReady: cortex.llamacpp, 0.1.55, linux-amd64-avx2
Installed: name: linux-amd64-avx2, version: v0.1.55
Engine llama-cpp installed successfully!

New llama.cpp version available:
To update, run: cortex engines update llama-cpp
```

### Test 測試

- ( 2025-03-26 12:59:05 )
- 先實驗一下 `Mistral 7B`
```bash
@jazzwang ➜ /workspaces/codespaces-blank $ cortex run mistral
Available to download:
    1. mistral:7b (default)

Select a model (1-1): 1
Start downloading..
metadata.yaml       100%[==========================] 00m:00s 173.00 B/173.00 B
metadata.yml        100%[==========================] 00m:00s 56.00 B/56.00 B
model.gguf          66%[=================>        ] 00m:17s 2.72 GB/4.07 GB
model.yml           100%[==========================] 00m:00s 493.00 B/493.00 B
```
```bash
@jazzwang ➜ /workspaces/codespaces-blank $ cortex run mistral
Available to download:
    1. mistral:7b (default)

Select a model (1-1): 1
Start downloading..
metadata.yaml       100%[==========================] 00m:00s 173.00 B/173.00 B
metadata.yml        100%[==========================] 00m:00s 56.00 B/56.00 B
model.gguf          100%[==========================] 00m:00s 4.07 GB/4.07 GB
model.yml           100%[==========================] 00m:00s 493.00 B/493.00 B
Model mistral:7b downloaded successfully!
In order to exit, type `exit()`
> given a json file, could you write a python code to cascade all "line" object grouped by "<v></v>" tag? here is a sample json input: """
To group all "line" objects in a JSON file based on the "<v></v>" tag in Python, you can use the `json` and `collections` libraries. Here's a simple script that reads the JSON file, groups the "line" objects, and writes the grouped data to a new JSON file.

```python
import json
import collections.OrderedDict

def group_lines(data):
    grouped_lines = collections.OrderedDict()
    current_group = None

    for item in data:
        if item.get('tag') == '<v></v>':
            current_group = [] if not current_group else grouped_lines[current_group]
            grouped_lines[item] = current_group
        else:
            current_group.append(item)

    return grouped_lines

def write_to_file(data, file_name):
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    with open('input.json', 'r') as f:
        data = json.load(f)

    grouped_data = group_lines(data)
    write_to_file(grouped_data, 'output.json')

if __name__ == "__main__":
    main()
```

Replace `'input.json'` with the path to your JSON file. This script assumes that the JSON objects are nested and that the "<v></v>" tag represents the grouping key. It will write the grouped data to an `output.json` file.
>
```

### subcommands

```bash
jazzwang ➜ /workspaces/codespaces-blank $ cortex

Cortex.cpp CLI

Usage:
cortex [options] [subcommand]

Options:
  -h,--help                   Print this help message and exit
  --verbose                   Get verbose logs
  --config_file_path TEXT     Configure .rc file path
  --data_folder_path TEXT     Configure data folder path
  -v,--version                Get Cortex version

Common Commands:
  pull                        Download models by HuggingFace Repo/ModelIDSee built-in models: https://huggingface.co/cortexso
  run                         Shortcut: pull, start & chat with a model

Models:
  models                      Subcommands for managing models

Engines:
  engines                     Subcommands for managing engines

Hardware:
  hardware                    Subcommands for managing hardware

Server:
  start                       Start the API server
  stop                        Stop the API server
  ps                          Show active model statuses
  update                      Update cortex version

Configurations:
  config                      Subcommands for managing configurations
```

### `models` subcommand

```bash
@jazzwang ➜ /workspaces/codespaces-blank $ cortex models
Subcommands for managing models
Usage:
cortex models [options] [subcommand]

Options:
  -h,--help                   Print this help message and exit

Subcommands:
  start                       Start a model by ID
  stop                        Stop a model by ID
  list                        List all local models
  get                         Get a local model info by ID
  delete                      Delete a local model by ID
  update                      Update model configurations
  import                      Import a model from a local filepath
  sources                     Subcommands for managing model sources
```
```bash
@jazzwang ➜ /workspaces/codespaces-blank $ cortex models list
Starting server ...
Set log level to INFO
Host: 127.0.0.1 Port: 39281
Failed to load the Vulkan library.
Server started
API Documentation available at: http://127.0.0.1:39281
+---------+------------+
| (Index) | ID         |
+---------+------------+
| 1       | mistral:7b |
+---------+------------+
```
```
@jazzwang ➜ /workspaces/codespaces-blank $ cortex models sources
Subcommands for managing model sources
Usage:
cortex models sources [options] [subcommand]

Options:
  -h,--help                   Print this help message and exit

Subcommands:
  add                         Add a model source
  remove                      Remove a model source
  list                        List all model sources

@jazzwang ➜ /workspaces/codespaces-blank $ cortex models sources list
+---+--------------+
| # | Model Source |
+---+--------------+
```
```
@jazzwang ➜ /workspaces/codespaces-blank $ cortex models sources add
[model_source] is required

terminate called after throwing an instance of 'std::bad_alloc'
  what():  std::bad_alloc
Aborted (core dumped)
```
- ( 2025-03-26 14:20:48 )
- 好久沒看到 `core dumped` 錯誤了～哈！
```bash
@jazzwang ➜ /workspaces/codespaces-blank $ cortex models sources add -h
Add a model source
Usage:
cortex models sources add [model_source]

Positionals:
  source TEXT

Options:
  -h,--help                   Print this help message and exit
@jazzwang ➜ /workspaces/codespaces-blank $
```

### `engines` subcommand

```bash
@jazzwang ➜ /workspaces/codespaces-blank $ cortex engines
A subcommand is required

Subcommands for managing engines
Usage:
cortex engines [options] [subcommand]

Options:
  -h,--help                   Print this help message and exit

Subcommands:
  list                        List all cortex engines
  install                     Install engine
  uninstall                   Uninstall engine
  update                      Update engine
  use                         Set engine as default
  load                        Load engine
  unload                      Unload engine
  get                         Get engine info
```
```bash
@jazzwang ➜ /workspaces/codespaces-blank $ cortex engines list
+---+-----------+---------+------------------+---------+
| # | Name      | Version | Variant          | Status  |
+---+-----------+---------+------------------+---------+
| 1 | llama-cpp | v0.1.55 | linux-amd64-avx2 | Default |
+---+-----------+---------+------------------+---------+
```
```bash
@jazzwang ➜ /workspaces/codespaces-blank $ cortex engines install -h
Install engine
Usage:
cortex engines install [engine_name] [options]

Options:
  -h,--help                   Print this help message and exit

Engines:
  llama-cpp
```

### `hardware` subcommand

- 覺得比較特殊的指令是這個 `hardware` 子命令
```bash
@jazzwang ➜ /workspaces/codespaces-blank $ cortex hardware list
Starting server ...
Set log level to INFO
Host: 127.0.0.1 Port: 39281
Failed to load the Vulkan library.
Server started
API Documentation available at: http://127.0.0.1:39281
CPU Information:
+---+-------+-------+---------------------------------+-----------+------------------------------------------------------------------------+
| # | Arch  | Cores | Model                           | Usage     | Instructions                                                           |
+---+-------+-------+---------------------------------+-----------+------------------------------------------------------------------------+
| 1 | amd64 | 1     | AMD EPYC 7763 64-Core Processor | 37.789265 | fpu mmx sse sse2 sse3 ssse3 sse4_1 sse4_2 pclmulqdq avx avx2 aes f16c  |
+---+-------+-------+---------------------------------+-----------+------------------------------------------------------------------------+

OS Information:
+---+---------------------------+--------------------+
| # | Version                   | Name               |
+---+---------------------------+--------------------+
| 1 | 20.04.6 LTS (Focal Fossa) | Ubuntu 20.04.6 LTS |
+---+---------------------------+--------------------+

RAM Information:
+---+-------------+-----------------+
| # | Total (MiB) | Available (MiB) |
+---+-------------+-----------------+
| 1 | 7938        | 6849            |
+---+-------------+-----------------+

GPU Information:
+---+--------+------+---------+-------------+-----------------+----------------+--------------------+-----------+
| # | GPU ID | Name | Version | Total (MiB) | Available (MiB) | Driver Version | Compute Capability | Activated |
+---+--------+------+---------+-------------+-----------------+----------------+--------------------+-----------+

Storage Information:
+---+-------------+-----------------+
| # | Total (GiB) | Available (GiB) |
+---+-------------+-----------------+
| 1 | 0           | 0               |
+---+-------------+-----------------+

Power Information:
+---+--------------+-----------------+--------------+
| # | Battery Life | Charging Status | Power Saving |
+---+--------------+-----------------+--------------+
| 1 | 0            |                 | No           |
+---+--------------+-----------------+--------------+
```

### `config` subcommand

```bash
@jazzwang ➜ /workspaces/codespaces-blank $ cortex config
Configuration updated successfully!
@jazzwang ➜ /workspaces/codespaces-blank $ cortex config -h
Subcommands for managing configurations
Usage:
cortex config [option] [value]

Options:
  -h,--help                   Print this help message and exit


Proxy:
  --verify_peer_ssl TEXT [on]
                              Verify peer SSL
  --no_proxy TEXT             No proxy for hosts
  --verify_proxy_ssl TEXT [on]
                              Verify SSL for proxy
  --verify_host_ssl TEXT [on]
                              Verify host SSL
  --proxy_username TEXT       Proxy Username
  --proxy_url TEXT            Proxy URL
  --proxy_password TEXT       Proxy Password
  --verify_proxy_host_ssl TEXT [on]
                              Verify SSL for proxy


Token:
  --api_keys TEXT             API header key to get access to server APIs
  --huggingface_token TEXT    HuggingFace token to pull models


CORS:
  --allowed_origins TEXT [*]  Allowed origins for CORS. Comma separated. E.g. http://localhost,https://cortex.so
  --cors TEXT [on]            Cross-Origin Resource Sharing configuration.

Configurations:
  status                      Print all configurations
```
```bash
@jazzwang ➜ /workspaces/codespaces-blank $ cortex config status
Starting server ...
Set log level to INFO
Host: 127.0.0.1 Port: 39281
Failed to load the Vulkan library.
Server started
API Documentation available at: http://127.0.0.1:39281
Failed to get configurations: {"message":"Invalid API Key"}
```