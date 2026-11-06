# Strata

- Git Repo
  - https://github.com/Niko1221/Strata

## 2026-11-04

- 2026-11-04 12:17:05 PM
- TOOL: Pi Agent + llama.cpp/Ornith-1.5-9B

> [!NOTE]
> 根據 https://github.com/Niko1221/Strata 內容撰寫一篇技術報告，採用繁體中文（台灣用詞）撰寫，包括 step-by-step 測試步驟，存成 c/strata/strata.md

## Strata 技術報告

> **項目**：[Niko1221/Strata](https://github.com/Niko1221/Strata)
> **授權**：MIT　|　**Star**：約 39k　|　**版本**：app/Terminal 0.2.10、Control 與 engine 0.1.56
> **定位**：在自有電腦（Windows / Linux / macOS）本地執行強大的 AI——聊天、寫程式、處理圖片，全部跑在 localhost，不依賴雲端。


### 一、Strata 是什麼

Strata 是一個讓你在**自己的電腦上本地執行強大多模型 AI** 的計畫。它讓你能夠在自家裝置上跑大語言模型（LLM）——聊天、程式協助、圖片理解——而不必把資料送到雲端 API。核心設計哲學是「把資料留在你自己電腦上」，同時讓模型在**顯存（VRAM）吃得更滿**：比起一味追求速度，Strata 認為**多一點顯存通常能換來更好的品質**（概估每多 1GB 顯存約可多載 700 個專家）。

Strata 有三個主要部分：

1. **App**（桌面介面）：以 Tauri 為外殼的跨平台桌面應用程式（`apps/desktop`），提供視覺化的設定與監控，適合一般使用者。
2. **Terminal**（命令列工具）：透過單一 `strata` 指令完成設定、啟動服務與監控，並能連接到你的程式開發工具（例如 MCP）。核心為 `strata.py`、`strata_cli/`、`strata_control/`。適合開發者與自動化。
3. **Engine 與 Server**：
   - **Server**（`serve/`，Python 所寫）：提供 OpenAI 與 Anthropic 相容的 HTTP API，並負責管理模型檔案、記憶體格式、上下文長度、可視化（圖片）等。
   - **Engine**（`src/`、`include/`、`metal/`、`sycl/`，C++/CUDA/HIP/SYCL/Metal）：直接與你的顯示卡溝通、執行推論的引擎。引擎是**與顯示卡相關**的，因此不同顯示卡（或作業系統）需要不同的引擎。

> 一個重要觀念：`strata launch` 指令本身有自己的設定旗標；而**引擎與 server 的設定旗標**則需要放在模型設定檔 `strata-<model>.json` 的 `"args"` 陣列中，或在 `serve/server.py` 的命令列上設定。


### 二、安裝與設定（Terminal）

Strata 提供「一個指令」安裝 `strata` 指令，然後下載並啟動模型。

#### Windows

在 PowerShell 中執行（之後需要開啟**新的**終端機，因為 `strata` 需要加入 PATH）：

```powershell
irm https://github.com/Niko1221/Strata/releases/latest/download/install.ps1 | iex
```

#### Linux / macOS

```sh
curl -fsSL https://github.com/Niko1221/Strata/releases/latest/download/install.sh -o install.sh && sh install.sh
```

安裝器不需要管理員權限，會把 `strata` 指令放到你的 PATH 中。

> 安全提醒：`strata` 安裝器會從 GitHub release 下載並安裝**引擎**（與顯示卡溝通的部分）。第一次執行 `strata launch` 會從相同版本下載對應到你顯示卡的引擎、檢查其簽名並先進行測試啟動，才會實際使用。

#### 常見問題

- **找不到 `strata`**：Windows 請開啟新的 PowerShell；Linux/Mac 請使用完整路徑 `~/.local/bin/strata` 並確認已加入 PATH。
- **警告「找不到適合本機的引擎」**：引擎就是與顯示卡溝通的那部分。通常原因為尚未安裝引擎、安裝了不匹配的引擎，或顯示卡 driver 太舊。在 app 中開啟 Settings → Engine，或在終端機執行 `strata update`。可用 `strata doctor --live` 與 `strata update --check` 來確認顯示卡與 driver 狀態。


### 三、Strata 如何運作（架構原理）

Strata 採用**混合專家（Mixture of Experts, MoE）架構**：

- **專家（Experts）**：模型包含高達 **24,576 個專家**，但**每個 token 只使用其中的 10 個**。這使得模型在保持強大能力的同時，每次預測的計算量相對可控。
- **資料分佈**：
  - **專家權重**（大且稀疏）：主要存放在**記憶體（RAM）**中，由多個 CPU 並行讀取。
  - **N-gram 查表**（一個巨大的查找表）：存放在**SSD**上，不佔用記憶體。
  - **KV Cache**（key-value 緩存）：減少重複計算，提升長上下文的效率。
- **可視化（Vision）**：Strata 支援圖片輸入（以 Qwen 系列模型為主）。圖片讀者預設開啟，約佔 0.9GB；對 **24GB 以下**的顯示卡，圖像理解在 **CPU** 上執行；對 **24GB 及以上**的顯示卡則在**顯示卡**上執行（約保留 1 到 1.4GB 顯存）。

這個分工讓 Strata 能同時利用 CPU 的並行能力與顯示卡的算力，讓大型 MoE 模型在消費級硬體上可行。


### 四、硬體支援

Strata 支援多種顯示卡與平台：

- **NVIDIA**：RTX 30 系列、40 系列、50 系列（CUDA）。
- **AMD**：Radeon AI PRO R9700 等（HIP）。
- **Intel Arc**（CUDA）。
- **Apple Silicon**（macOS 15+，Metal 引擎，安裝檔內含引擎）。
- **AMD Ryzen AI Max / Strix Halo**（APU）。
- **NVIDIA DGX Spark**（Linux ARM64）。

> **Windows 與 Linux 差異**：Windows 的引擎採用 CUDA（Windows 專用），通常需從 release 下載並放到 `~/.local/share/strata/engines/`；Linux 則使用 NVIDIA CUDA 安裝程式，安裝後執行 `strata update`。


### 五、性能與速度

#### 計量方式

Strata 以 **tokens/sec（T/s）** 來衡量速度。`bench/` 資料夾內有計量腳本可用來測量。

#### 影響速度的因素

- **硬體**：顯存容量與速度是最關鍵因素——**比速度更重要的是顯存**，每多 1GB 顯存約可多載 700 個專家。
- **模型**：不同模型（例如 Qwen 系列、DeepSeek）的速度與需求不同。
- **記憶體模式（Memory modes）**：三種模式——
  - **default（auto）**：自動選擇，優先速度，使用較多顯存。
  - **low VRAM**：較慢，適合顯存較小的情況。
  - **high VRAM**：使用更多顯存，通常品質更好。
- **Speed switches**（可放在 `strata-<model>.json` 的 `"args"` 中）：`--experts`、`--kv-cache`、`--cuda-graph` 等，可用來微調速度與品質的平衡。


### 六、使用模型與 API

#### 模型家族

Strata 的模型目錄（與 app 的 `setup.py` 共用）包含以下系列（範例）：

- **Qwen 系列**：Qwen3.8-Flash-Next、Qwen3.6-35B-A3B、IQ3_XXS（小型高效模型）。
- **DeepSeek**：DeepSeek V4.1-Flash 等。
- **其他**：IQ3_XXS、q2_0 等量化版本。

#### OpenAI 相容 API

Server 預設在 `http://127.0.0.1:11434/`，並提供 OpenAI 相容端點 `http://localhost:11434/v1`。預設 API key 為 `sk-localhost`（也可在 `strata-<model>.json` 的 `server → api-key` 中設定）。

```bash
curl http://localhost:11434/v1/models
curl http://localhost:11434/v1/chat/completions -H "Authorization: Bearer sk-localhost"
```

#### Anthropic 相容 API

Server 另於 `http://127.0.0.1:11435/` 提供 Anthropic 相容端點 `http://localhost:11435/v1`。

#### 透過 Terminal 啟動

```sh
strata launch --port 11434 --open                          # OpenAI API + 開啟監控畫面
strata launch --port 11434 --open anthropic                # Anthropic API + 開啟監控畫面
strata launch --plan --family qwen --model q2_0            # 預覽（不做任何更改）
strata launch --family qwen --model q2_0 --yes --no-tui    # 下載、啟動、印出網址後結束
strata launch --status                                     # 查看目前啟動的服務
strata launch --stop                                       # 停止服務
```

> `strata launch --help` 會列出所有旗標及其範例。未知模型或旗標會顯示最近的相似項目。


### 七、可視化（圖片輸入）

Strata 支援圖片輸入（以 Qwen 系列模型為主），預設開啟。

1. 圖片檔案保留在磁碟上，由 server 提供服務，**重啟後仍會保留**。
2. 上傳圖片以取得 base64：

```bash
curl -F "file=@image.jpg" http://127.0.0.1:11435/v1/messages/upload_base64
```

3. 透過 Anthropic 的 `/v1/messages` 或 OpenAI 的 `/v1/chat/completions`（使用 `image_url` 加上 `content` 陣列）傳送圖片。

> 可透過 `--vision off`（或 `--vision cpu` / `--vision gpu`）對每個模型微調可視化功能。


### 八、MCP 工具

Strata 提供一套 MCP（Model Context Protocol）工具，可讓你的程式開發工具直接呼叫本地 AI。

#### 工具清單

`strata_ask`、`strata_chat`、`strata_terminate`、`strata_config`、`strata_info`、`strata_models`、`strata_update`、`strata_engine`。

#### 加入 MCP

把配置加入以下其中一個檔案：

- `mcp.json`
- `.mcp.json`
- `claude_desktop_config.json`
- `~/.config/claude/claude_desktop_config.json`

#### CLI 方式

```sh
strata launch --mcp
strata mcp
```

#### 環境變數（範例）

`STRATA_MODEL`、`STRATA_PORT`、`STRATA_API_KEY`。


### 九、安全與存取

Strata 預設僅在本機（`127.0.0.1`）服務。設定存取選項：

- **this computer only（127.0.0.1）**：預設，僅本機可存取。
- **your network（LAN）**：提供 IP 與 key，允許同網路存取。
- **Cloudflare 快速隧道**：需要 `cloudflared`。
- **Tailscale**：需要已安裝並連上。

關於 API key：

- 預設 key 為 `sk-localhost`。
- 若無 key，server 仍會啟動並警告「任何能連到該端口的任何人都能使用模型與工具」；`--no-api-key` 會直接這樣做而不經畫面。
- 設定 `t` 可關閉 API key（不建議在遠端存取時關閉）。
- 一旦設定，Strata 會產生一個 key；`strata launch` 也有 `--access lan` 等選項。

> 安全原則：模型與工具預設僅在 localhost 服務，避免你的模型與工具被未經授權的人使用。


### 十、效能優化技巧

- **Parallel requests（並行請求）**：預設會「適合你的顯示卡」地設定（約 12GB: 1、20GB: 2、24GB: 3、32GB 及以上: 4），最高支援 8。可手動輸入 1 到 8，但若無法容納會顯示警告，請於啟動後檢查實際的 slots。
- **Context（上下文）**：範圍 8K 到 512K，较长的上下文需要更多顯存。
- **Memory format（記憶體格式）**：8-bit（`m`）或 4-bit，影響品質與顯存占用。
- **CUDA 並行**：Strata 的 CUDA 引擎有自己的 GPU 程序管理員（NVReg），可與其它應用程式並行使用 GPU。
- **Speed switches**：用 `--experts`、`--kv-cache`、`--cuda-graph` 等微調速度與品質。


### 十一、測試步驟（Step-by-Step）

以下為在已安裝環境中驗證 Strata 功能的逐步測試流程。

> **前提條件**：已完成安裝（`strata` 指令在 PATH 中），且電腦有支援的顯示卡並已安裝引擎。

#### 步驟 1：版本檢查

確認安裝是否成功：

```sh
strata --version
```

預期會顯示版本資訊（例如 Control/engine 0.1.56）。

#### 步驟 2：診斷顯示卡與 driver

確認顯示卡狀態與引擎是否匹配：

```sh
strata doctor --live
strata update --check
```

預期會列出顯示卡資訊、driver 版本，以及是否有需要更新的引擎。

#### 步驟 3：啟動服務並查看狀態

```sh
strata launch --status
```

查看目前是否有服務在服務。若無，進行下一步。

#### 步驟 4：選擇模型並啟動（命令列方式）

```sh
strata launch --family qwen --model iq3_xxs --context 128k --parallel 4 --vision off \
              --access lan --port 8080 --save-preset "Office" --no-tui
```

此指令會：下載模型 → 啟動 server → 印出 API 網址 → 結束（`--no-tui`）。

> 使用 `--plan` 可先預覽會發生什麼事，而不實際下載或更改任何東西。

#### 步驟 5：確認 server 正在服務

開啟新的終端機，檢查服務是否啟動：

```sh
curl http://localhost:8080/v1/models
```

預期會列出可使用的模型。

#### 步驟 6：測試 OpenAI 相容 API

```sh
curl http://localhost:8080/v1/chat/completions \
  -H "Authorization: Bearer sk-localhost" \
  -d '{"model":"<你的模型名>","messages":[{"role":"user","content":"你好，請用一句話介紹你自己。"}]}'
```

預期會收到模型的文字回應。

#### 步驟 7：測試 Anthropic 相容 API

Server 預設在 11435 埠提供 Anthropic 相容端點（若變更了端口，請對照實際端口）：

```sh
curl http://localhost:11435/v1/messages \
  -H "x-api-key: sk-localhost" \
  -H "anthropic-version: 2023-06-01" \
  -d '{"model":"<你的模型名>","max_tokens":100,"messages":[{"role":"user","content":"你好"}]}'
```

#### 步驟 8：測試可視化（圖片輸入）

1. 上傳圖片以取得 base64：

```sh
curl -F "file=@image.jpg" http://127.0.0.1:11435/v1/messages/upload_base64
```

2. 以 OpenAI 格式傳送圖片（`image_url` + `content` 陣列）：

```sh
curl http://localhost:8080/v1/chat/completions \
  -H "Authorization: Bearer sk-localhost" \
  -d '{
    "model":"<你的模型名>",
    "messages":[
      {"role":"user",
       "content":[{"type":"text","text":"請描述這張圖片"},
                  {"type":"image_url","image_url":{"url":"data:image/jpeg;base64,<你的base64>"}}]}
    ]}'
```

> 請注意：可視化主要支援 Qwen 系列模型。

#### 步驟 9：開啟監控畫面（桌面方式）

在終端機執行（需要下載引擎與模型）：

```sh
strata launch --open
```

監控畫面會開啟，顯示設定、狀態與性能資訊。

#### 步驟 10：檢查 MCP 工具

```sh
strata mcp
```

確認 MCP 工具（`strata_ask`、`strata_chat` 等）可正常註冊與使用。

#### 步驟 11：停止服務

```sh
strata launch --stop
```


### 十二、總結

Strata 是一個設計簡潔、以「本地執行」為核心的 AI 推論平台。它透過三大組成部分（App、Terminal、Engine/Server）讓不同類型的用家都能輕易使用；透過 MoE 架構與聰明的資料分佈（專家權重在 RAM、n-gram 查表在 SSD）讓大型模型在消費級硬體上可行；並提供 OpenAI / Anthropic 相容的 HTTP API、圖片理解、MCP 工具整合與靈活的存取控制。

對開發者而言，`strata` 指令加上 `strata-<model>.json` 設定檔提供了高度的可自動化與可微調性；對一般用家而言，桌面 app 提供了直觀的視覺化體驗。無論是哪一種用家，Strata 都讓「在自有電腦上執行強大 AI」變得更加容易。


### 參考文件

- [Strata 官方倉庫](https://github.com/Niko1221/Strata)
- `docs/README.md`——安裝與設定指令
- `docs/INSTALL.md`——安裝與設定指南
- `docs/HOW_IT_WORKS.md`——Strata 如何運作
- `docs/DETAILS.md`——Strata engine 與 server 參考
- `docs/AI_REFERENCE.md`——AI 模型參考
- `docs/TROUBLESHOOTING.md`——常見問題排解

## 2026-11-06

- 用 Google Colab 實測
  - 連上 https://colab.research.google.com/ 連上 T4 GPU 的 runtime
  - 在 Python Notebook 裡跑以下指令
```python
!curl -fsSL https://github.com/Niko1221/Strata/releases/latest/download/install.sh -o install.sh
!bash install.sh
!/root/.local/bin/strata --version
!/root/.local/bin/strata doctor --live
!/root/.local/bin/strata update --check
!/root/.local/bin/strata launch --family qwen --model iq3_xxs --context 128k --parallel 4 --vision off --access lan --port 8080 --save-preset "Office" --no-tui
```
- 結果： Colab 空間不足，需要至少 120GB
```bash
[!] Qwen3.8-Flash-Next IQ3_XXS does not fit this computer. It can still start; expect it to be slow or to run out of memory.
[!] 4 requests at once is more than a 15 GB card usually holds (it fits 1). It can still start; the engine keeps less of the model in graphics memory, so each answer is slower.
    Checking the engine for this computer…
  No engine is installed yet. Getting the one for your graphics card…  0%       Reading the signed update feed
    Downloading engine 0.1.57 linux-x86_64-cuda-cuda13 (720 MB)
  Downloading the engine… 100%  100%
    Unpacking 0.1.57 linux-x86_64-cuda-cuda13
    Checking the package signature and every file
    Test-starting engine 0.1.57 linux-x86_64-cuda-cuda13 before switching to it
    Switching to engine 0.1.57 linux-x86_64-cuda-cuda13
    Engine 0.1.57 is installed and will be used on the next start
  The engine is installed.  100%
  Getting Qwen3.8-Flash-Next IQ3_XXS ready (a download may be large; it continues where it stopped if interrupted)…  0%       Getting your model ready
    Checking your computer
strata: The model could not be installed. Not enough free disk space for the low-RAM copy of the experts in /root/.local/share/strata/Strata-data/packs/iq3_xxs: it needs about 120 GB and 119 GB are free there. Free some space, move Strata's data folder to a bigger drive (strata launch --data-dir), or set Low-RAM mode to Automatic to run without the copy. Details: /root/.local/state/strata/launch/office.setup.log
```