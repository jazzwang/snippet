# Installing nvidia-container-toolkit in WSL2

## 2026-10-30

- 緣起：
  - 測試 Kindi 時，遇到這個狀況 
```bash
/tmp/kindi$ sudo apt-get install -y nvidia-container-toolkit 
[sudo] password for jazz: 
Reading package lists... Done 
Building dependency tree... Done 
Reading state information... Done 
E: Unable to locate package nvidia-container-toolkit
```
- 尋求 Gemini 協助，不過指令不正確
  - https://share.google/aimode/Ve59pKnvMRmcA9yi8

## 2026-11-23

- 改參考 Nvidia 的網站
  - https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html
- 確認 WSL Kernel 版本與 Nvidia Driver 狀態
```bash
~/git/snippet/md/windows$ uname -a
Linux JazzBook 6.18.58.1-microsoft-standard-WSL2 #1 SMP PREEMPT_DYNAMIC Tue Oct 27 00:24:11 UTC 2026 x86_64 x86_64 x86_64 GNU/Linux
~/git/snippet/md/windows$ nvidia-smi
Mon Nov 23 14:24:56 2026
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 590.62                 Driver Version: 592.00         CUDA Version: 13.1     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 4060 ...    On  |   00000000:01:00.0 Off |                  N/A |
| N/A   39C    P0             18W /   95W |       0MiB /   8188MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
```
- 原本 `apt-cache search nvidia-container-toolkit` 找不到套件 
```bash
~/git/snippet/md/windows$ history | tail -n 20
[11/23 14:14:18] nvidia-smi
[11/23 14:15:18] apt-cache search nvidia-container-toolkit
[11/23 14:15:38] sudo apt-get update && sudo apt-get install -y --no-install-recommends    ca-certificates    curl    gnupg2
[11/23 14:15:59] curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg   && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list |     sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' |     sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
[11/23 14:16:13] cat /etc/apt/sources.list.d/nvidia-container-toolkit.list
[11/23 14:16:16] sudo apt-get update
[11/23 14:16:21] apt-cache search nvidia-container-toolkit
[11/23 14:16:49] export NVIDIA_CONTAINER_TOOLKIT_VERSION=1.20.2-1
```
- 實際上，複製 [Nvidia 網站](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) 的步驟，就可以正確安裝成功了
```bash
sudo apt-get update && sudo apt-get install -y --no-install-recommends \
   ca-certificates \
   curl \
   gnupg2

curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list

sudo apt-get update

export NVIDIA_CONTAINER_TOOLKIT_VERSION=1.20.2-1
  sudo apt-get install -y \
      nvidia-container-toolkit=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
      nvidia-container-toolkit-base=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
      libnvidia-container-tools=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
      libnvidia-container1=${NVIDIA_CONTAINER_TOOLKIT_VERSION}
```
- 根據 [Gemini 建議步驟](https://share.google/aimode/Ve59pKnvMRmcA9yi8)，讓 Docker 能夠識別並調用 NVIDIA GPU： [[1](https://www.gpu-mart.com/blog/install-nvidia-container-toolkit)]
```bash
~/git/snippet/md/windows$ sudo nvidia-ctk runtime configure --runtime=docker
INFO[0000] Config file does not exist; using empty config
INFO[0000] Wrote updated config to /etc/docker/daemon.json
INFO[0000] It is recommended that docker daemon be restarted.
```
- 接著，重啟 Docker 服務
```bash
~/git/snippet/md/windows$ sudo systemctl restart docker
```
- 用以下指令驗證
```bash
~/git/snippet/md/windows$ sudo docker run --rm --gpus all nvidia/cuda:12.0.0-base-ubuntu22.04 nvidia-smi
Unable to find image 'nvidia/cuda:12.0.0-base-ubuntu22.04' locally
12.0.0-base-ubuntu22.04: Pulling from nvidia/cuda
aece8493d397: Pull complete
cb5efdcf30fe: Pull complete
6c0deaabac71: Pull complete
56cb4663b3f5: Pull complete
0a0d0d55d972: Pull complete
Digest: sha256:4e9da312e1f5affc0ab1b2cb3f1141e163849dcd850d66fe315138e82e85427d
Status: Downloaded newer image for nvidia/cuda:12.0.0-base-ubuntu22.04
Mon Nov 23 06:32:18 2026
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 590.62                 Driver Version: 592.00         CUDA Version: 13.1     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 4060 ...    On  |   00000000:01:00.0 Off |                  N/A |
| N/A   42C    P0             17W /   91W |       0MiB /   8188MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
```
- 看樣子成功了！！