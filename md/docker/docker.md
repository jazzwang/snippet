# Docker

## 2026-06-12

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI Mode
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
'docker model run hf.co/unsloth/diffusiongemma-26B-A4B-it-GGUF:Q4_K_M' 這個指令需要用到特定版本的 docker 嗎？
</td></tr><tr><td>A:</td><td>

## docker model

是的，這個指令需要用到特定版本（或外掛模組）的 Docker。
指令中的 `docker model run` 並不是傳統 Docker 用來執行容器的 `docker run`。它是 Docker 專門為本地端執行 AI 大模型所推出的新功能，稱為 `Docker Model Runner (DMR)` (1.2.6, 1.3.1)。 [1, 2]
要順利執行這個指令，您的環境必須符合以下版本與設定要求：

### 1\. 版本與安裝要求

-   如果您使用 Docker Desktop（Windows / Mac / Linux）：
        -   必須安裝 `Docker Desktop 版本 4.40 或更高版本`(1.1.1, 1.3.9)。
        -   需要在「Settings」（設定） > 「AI」分頁中，勾選 `Enable Docker Model Runner`(1.3.7, 1.3.10)（啟用模型執行器）。 [3, 4, 5]
-   如果您使用 Linux 伺服器 / Docker CE（無圖形介面）：
    -   您不需要 Docker Desktop，但傳統的 Docker Engine 預設沒有 `model` 這個子指令。
    -   您必須手動安裝專屬的外掛擴充套件 `docker-model-plugin`。例如在 Ubuntu/Debian 上需執行：[2, 6, 7, 8]

```bash
sudo apt-get update && sudo apt-get install docker-model-plugin
```

### 2. 如何檢查您的環境是否支援？

您可以在終端機輸入以下指令進行驗證： [9]

```bash
docker model version
```

-   成功： 如果有正確回傳版本資訊，代表您的 Docker 已經支援此指令。
-   失敗： 如果顯示 `unknown command: docker model`，代表您的 Docker 版本太舊，或者尚未啟用/安裝 DMR 外掛。 [6, 8, 9]

### 💡 額外硬體提醒

您打算執行的 `diffusiongemma-26B-A4B` 是一個具備 260 億參數（26B MoE 架構）的大型多模態模型。雖然 `Q4_K_M` 已經過 4-bit 量化壓縮，但它依然需要相當大的記憶體（RAM / VRAM）才能流暢運行。建議您的電腦至少配備 32GB 以上的系統記憶體（如果是 Mac 則建議 32GB 以上統一記憶體），或配備大顯存的獨立顯卡（如單張或雙張高階顯卡），否則執行時容易因記憶體不足（OOM）而崩潰。 [10, 11, 12, 13]
您目前使用的是哪一種作業系統（例如 Mac, Windows 還是 Linux 伺服器）？我可以為您提供對應作業系統的完整安裝與顯示卡加速設定步驟。

[1] [https://www.youtube.com](https://www.youtube.com/watch?v=4YA1n2zs6XA)
[2] [https://unsloth.ai](https://unsloth.ai/docs/models/tutorials/how-to-run-llms-with-docker)
[3] [https://www.glukhov.org](https://www.glukhov.org/llm-hosting/docker-model-runner/docker-model-runner-cheatsheet/)
[4] [https://vocus.cc](https://vocus.cc/article/67f14bbcfd8978000132a0e5)
[5] [https://dev.to](https://dev.to/sreeni5018/run-open-source-ai-modelswith-docker-model-runner-5hei)
[6] [https://www.reddit.com](https://www.reddit.com/r/docker/comments/1lmh9u1/how_do_i_run_docker_ai_models_like_gemma3_on/)
[7] [https://www.youtube.com](https://www.youtube.com/watch?v=tYg6T_DAP-k&t=266)
[8] [https://www.ajeetraina.com](https://www.ajeetraina.com/docker-model-runner-tutorial-and-cheatsheet-mac-windows-and-linux-support/)
[9] [https://geshan.com.np](https://geshan.com.np/blog/2026/01/docker-model-runner/)
[10] [https://unsloth.ai](https://unsloth.ai/docs/models/diffusiongemma)
[11] [https://unsloth.ai](https://unsloth.ai/docs/models/gemma-4)
[12] [https://huggingface.co](https://huggingface.co/unsloth/diffusiongemma-26B-A4B-it-GGUF)
[13] [https://huggingface.co](https://huggingface.co/unsloth)
</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
如何在 Linux 上配置 NVIDIA GPU 加速，安裝 `NVIDIA Container Toolkit`？
</td></tr><tr><td>A:</td><td>

## NVIDIA Container Toolkit

在 Linux 上配置 NVIDIA GPU 加速並安裝 NVIDIA Container Toolkit，可以讓 Docker 容器直接存取宿主機的 GPU 資源。這樣在執行 docker model run 部署大型 AI 模型時，才能順利調用顯卡進行硬體加速。 [1, 2] 

以下以最常見的 Ubuntu / Debian 系統為例，說明完整的配置步驟（若為 CentOS/RHEL，主要差異在於套件管理器指令改為 dnf 或 yum）：

### 前提條件：檢查 NVIDIA 驅動程式 [3] 

在開始之前，Linux 宿主機必須已安裝 NVIDIA 顯卡驅動程式（但不需要在宿主機安裝 CUDA Toolkit，因為 Container Toolkit 會處理容器與驅動之間的橋樑）。 [4, 5] 
請在終端機輸入：
```bash
nvidia-smi
```
* 成功： 如果有正確顯示您的顯卡型號、VRAM 使用量以及驅動版本（例如 Driver Version: 550.xx），請繼續進行下一步。
* 失敗： 如果顯示 command not found，請先透過 Ubuntu 的「附加驅動」或是指令 `sudo apt install nvidia-driver-xxx` 安裝驅動程式並重啟電腦。 [1, 3] 

### 第一步：新增 NVIDIA 官方套件儲存庫（Repository）

我們需要將 NVIDIA 的官方金鑰與軟體源加入系統，以便透過 apt 安裝最新的 Toolkit。 [6] 
配置步驟可參考 NVIDIA 官方文件 [Installing the NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) 以獲取最新指令，一般包含設定 GPG 金鑰及新增軟體源。 [7, 8] 

### 第二步：安裝與配置 Docker 執行階段 (Runtime)

安裝套件並設定 Docker 以啟用 GPU 支援： [8, 9, 10] 

#### 1. 安裝並配置 toolkit

```bash
sudo apt-get install -y nvidia-container-toolkit
sudo nvidia-ctk runtime configure --runtime=docker# 2. 重啟 Docker
sudo systemctl restart docker
```

### 第三步：驗證 GPU 加速與啟動模型

執行測試容器確認 GPU 可用： [8] 

```bash
docker run --rm --gpus all nvidia/cuda:12.2.2-base-ubuntu22.04 nvidia-smi
```

若能正確顯示顯卡資訊，即可執行您的模型部署指令：

```bash
docker model run hf.co/unsloth/diffusiongemma-26B-A4B-it-GGUF:Q4_K_M
```

如有任何錯誤（如軟體源連接失敗、nvidia-smi 衝突），歡迎補充相關訊息。

[1] [https://www.tencentcloud.com](https://www.tencentcloud.com/zh/document/product/560/75960)
[2] [https://cloud.tencent.com](https://cloud.tencent.com/document/product/560/118463)
[3] [https://comate.baidu.com](https://comate.baidu.com/zh/page/b031zdpetny)
[4] [https://github.com](https://github.com/NVIDIA/nvidia-container-toolkit)
[5] [https://ivonblog.com](https://ivonblog.com/posts/linux-install-nvidia-container-toolkit/)
[6] [https://www.cnblogs.com](https://www.cnblogs.com/SkyXZ/p/18710410)
[7] [https://docs.nvidia.com](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)
[8] [https://www.linkedin.com](https://www.linkedin.com/pulse/setting-up-nvidia-gpu-acceleration-docker-ubuntu-step-by-step-li-xdppc)
[9] [https://docs.nvidia.com](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/1.17.5/install-guide.html)
[10] [https://erhwenkuo.github.io](https://erhwenkuo.github.io/kubernetes/01-getting-started/learning-env/nvidia/nvidia-container-toolkit/)

</td></tr>
</table>
