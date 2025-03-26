# cortex.cpp

> Local AI API Platform

- Git Repo
  - https://github.com/menloresearch/cortex.cpp
- Website:
  - https://cortex.so/

## 2025-03-26

- 緣起：
  - 在測試 [unsloth Qwen 2.5 7B 的 Fine-tune Notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen2.5_(7B)-Alpaca.ipynb) 時，有寫到用 Jan 或 
  - 從 [Jan](https://github.com/menloresearch/jan) 的 README 看到關於 Cortex.cpp 的連結。
- 從 README 看起來，整體很像 Ollama。從底下這段 Jan README 關於 `Cortex.cpp` 的描述，確認是定位成 Ollama 的 alternative。

> [!INFO]
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
Preparing to unpack coretex.deb ...
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