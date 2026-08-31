# llmfit 技術摘要

- Git Repo
  - https://github.com/AlexsJones/llmfit

## 2026-08-31

> **Hundreds of models & providers. One command to find what runs on your hardware.**

本文根據 [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) 儲存庫的 README、核心技術文件與 provider/platform 文件整理。模型目錄、硬體 profile 與 benchmark 資料會隨版本更新。

## 1. 專案定位

`llmfit` 是以 Rust 開發的本機 LLM 硬體適配與推薦工具，用來回答：「哪些模型能在這台機器上執行？應該使用哪種量化？預期速度與執行品質如何？」

它會偵測 RAM、CPU、GPU/VRAM 與推論後端，並對模型目錄中的每個模型評估：

- **Quality**：參數量、模型家族品質、任務適配度與量化損失。
- **Speed**：依硬體記憶體頻寬、模型大小、量化格式與執行路徑估算 tokens/sec。
- **Fit**：模型對可用 VRAM/RAM 的使用率與餘裕。
- **Context**：上下文視窗能力與實際目標上下文的匹配程度。

結果可透過互動式 TUI、CLI、JSON 或 REST API 使用；因此既適合互動選型，也適合腳本、Agent 與叢集 scheduler。

- **GitHub**：<https://github.com/AlexsJones/llmfit>
- **授權**：MIT
- **主要語言**：Rust

## 2. 核心分析流程

每個模型大致依下列流程處理：

1. 決定估算上下文長度；未指定時預設上限為 8,192 tokens。
2. 根據模型格式與可用資源選擇推論 runtime。
3. 從量化階層中挑選在記憶體預算內品質最高的格式。
4. 選擇 GPU、MoE offload、CPU/GPU offload、CPU 或 tensor-parallel 路徑。
5. 計算記憶體使用率與 Fit 等級。
6. 估算 decode 速度，以及在資料足夠時估算 prefill/TTFT。
7. 計算 Quality、Speed、Fit、Context，依 use case 權重合成總分。
8. 依總分或其他欄位排序並輸出。

### Fit 等級

Fit 判定使用實際執行路徑所對應的記憶體池：

| 記憶體使用率 | 等級 | 意義 |
|---:|---|---|
| ≤ 60% | `Perfect` | 有充足餘裕且可由 GPU 執行 |
| ≤ 85% | `Good` | 可執行且有合理餘裕 |
| ≤ 98% | `Marginal` | 接近上限，實際載入風險較高 |
| > 98% | `Too Tight` | 超出或幾乎耗盡可用記憶體 |

CPU-only、CPU/GPU offload 與 MoE offload 路徑最多標為 `Good`；`Perfect` 保留給有餘裕的 GPU 執行。98% 門檻也保留 allocator slack 與避免記憶體碎片造成的載入失敗。

## 3. 硬體偵測與推論 runtime

### 硬體偵測

- **NVIDIA**：透過 `nvidia-smi`，支援多 GPU 並彙總 VRAM。
- **AMD**：透過 `rocm-smi`。
- **Intel Arc**：獨立 GPU 使用 sysfs，整合式 GPU 使用 `lspci`。
- **Apple Silicon**：透過 `system_profiler` 偵測 unified memory，VRAM 視為共享系統記憶體。
- **Ascend NPU**：透過 `npu-smi`。
- **CPU/RAM**：透過 `sysinfo` 取得核心數、總 RAM 與可用 RAM。

支援的硬體 backend 包括 CUDA、Metal、ROCm、SYCL、CPU ARM、CPU x86 與 Ascend。

### 推論 runtime

硬體 backend 與模型 runtime 是兩個獨立概念。主要 runtime 為：

- **llama.cpp**：GGUF 模型與常見 Ollama 工作流程。
- **MLX**：Apple Silicon 的 MLX 原生模型。
- **vLLM**：AWQ/GPTQ/AutoRound 預量化模型，以及叢集 tensor parallel。
- **Unsupported**：需要尚未支援的特殊 runtime，例如部分 TTS 模型。

Apple Silicon unified memory 預設偏好 MLX；預量化模型通常使用 vLLM，也可用 `--force-runtime` 覆寫自動選擇。

## 4. 模型資料、量化與 MoE

模型目錄由 Hugging Face REST API scraper 產生，並在編譯時嵌入 binary。模型 metadata 可包含名稱、供應者、參數量、上下文長度、格式、量化、RAM/VRAM 需求、use case、capability，以及完整 Transformer/MoE 架構資訊。

模型分類包括 General、Coding、Reasoning、Chat、Multimodal、Embedding；另外可標記 Vision、Tool Use、Audio 與 TTS 能力。

### 動態量化

一般 GGUF 量化由高品質到高壓縮依序嘗試：

```text
Q8_0 → Q6_K → Q5_K_M → Q4_K_M → Q3_K_M → Q2_K
```

MLX 使用 `mlx-8bit → mlx-4bit`；ONNX 使用 `Q8_0 → Q4_0`。AWQ、GPTQ 與 AutoRound 是固定的預量化格式，不參與一般動態重新量化。

記憶體需求可概括為：

```text
模型權重 ≈ 參數量 × 每參數位元組數
總需求   ≈ 權重 + KV cache + 執行時額外開銷
```

實作會依上下文長度、模型架構與 KV cache 量化進行更細緻估算。

### MoE

MoE 模型會區分總參數與每個 token 實際啟用的 active parameters。若有完整 metadata，速度模型會拆分 expert FFN 與 attention/router/embedding 的記憶體流量；資料不足時則使用 active parameters 與架構修正係數。

可用的 MoE 路徑包括：

- 全部 experts 載入 VRAM。
- active experts 放在 VRAM，inactive experts offload 至系統 RAM。
- 一般 CPU/GPU offload。

這使得 Mixtral、DeepSeek 等稀疏模型不會被單純的總參數量過度高估。

## 5. 評分與速度估算

### 多維度評分

四項分數皆為 0–100，權重依任務調整：

- **General**：品質與整體平衡。
- **Coding**：使用編程模型與任務 benchmark 對齊。
- **Reasoning**：Quality 權重最高，預設為 0.55。
- **Chat**：Speed 權重較高，預設為 0.35。
- **Multimodal**：考量視覺與多模態能力。
- **Embedding**：更重視速度與適配度。

Quality 不只看參數量，也包含模型家族、世代、量化懲罰與任務對應資料，因此較小的專用模型可能勝過較大的通用模型。

### Decode throughput

Token generation 通常受模型權重讀取的記憶體頻寬限制，核心估算可簡化為：

```text
estimated tok/s ≈ (GPU memory bandwidth GB/s ÷ model size GB)
                  × efficiency factor
                  × quantization multiplier
                  × run-mode factor
```

預設 efficiency factor 為 `0.55`，用來反映 kernel overhead、KV cache 讀取與記憶體控制器效率。GPU 頻寬依序取自：

1. `gpu_bandwidth_gbps_override` 使用者覆寫值。
2. GPU 名稱查表。
3. backend fallback 常數。

未辨識 GPU 時，fallback 常數為：CUDA 220、Metal 160、ROCm 180、SYCL 100、CPU ARM 90、CPU x86 70、Ascend 390。每筆結果保留 `estimate_basis`，可由 `llmfit info` 檢查估算假設。

### Prefill、TTFT 與可信度

Prefill 是計算密集工作，不直接套用 decode 的頻寬模型。只有已知 GPU FP16 throughput（`gpu_compute_tflops_fp16`）時才提供 `prefill_tps` 與 `ttft_ms`；未知時回傳 `null`，代表沒有可靠估算，而不是速度為零。

速度資料標記以下來源，信任順序由高至低：

1. `measured_local`：本機實測。
2. `measured_community`：相同硬體的社群實測。
3. `calibrated`：以本機 benchmark 校準公式。
4. `estimated`：只有公式估算。
5. `unsupported`：沒有可用 runtime 或估算方法。

## 6. Runtime provider 整合

llmfit 可偵測本機已安裝模型，也可從 TUI 觸發下載：

| Provider | 預設端點/方式 | 功能 |
|---|---|---|
| Ollama | `http://localhost:11434` | `/api/tags` 列舉、`/api/pull` 下載 |
| llama.cpp | `llama-cli` / `llama-server` | Hugging Face GGUF 下載與本地 cache 偵測 |
| MLX | `mlx-community` cache | Apple Silicon MLX 模型管理 |
| Docker Model Runner | `http://localhost:12434` | 透過 `/engines` 列舉及 pull |
| LM Studio | `http://127.0.0.1:1234` | REST API 列舉、下載與進度追蹤 |

遠端服務可設定 `OLLAMA_HOST`、`DOCKER_MODEL_RUNNER_HOST` 或 `LMSTUDIO_HOST`；LM Studio API key 使用 `LMSTUDIO_API_KEY`。模型目錄以 Hugging Face 名稱為主，並維護與 Ollama tag 的精確映射。

## 7. CLI、TUI 與 REST API

### 常用 CLI

```sh
llmfit                       # 啟動互動式 TUI
llmfit fit                   # 顯示所有模型的適配排名
llmfit recommend --json     # 產生推薦 JSON
llmfit info "Mistral-7B"    # 顯示單一模型詳細分析
llmfit plan "model"        # 規劃模型的硬體需求
llmfit bench                # 實測速度與 TTFT
llmfit system               # 顯示硬體資訊
llmfit doctor               # 輸出硬體診斷報告
```

可使用 `--memory`、`--ram`、`--cpu-cores`、`--max-context` 覆寫或模擬硬體。`--profile` 則可描述整台目標機器，包含 RAM、unified memory、GPU/DDR 頻寬及 FP16 throughput。

### REST API

```sh
llmfit serve --host 0.0.0.0 --port 8787
```

主要 endpoint：

- `GET /health`
- `GET /api/v1/system`
- `GET /api/v1/models`
- `GET /api/v1/models/top`
- `GET /api/v1/models/{search}`

API 可依 `min_fit`、runtime、use case、provider、搜尋字串、速度、參數量、記憶體與 context 篩選，適合節點排程器、聚合服務與 Agent。

## 8. Benchmark 與社群回饋

`llmfit bench` 支援對 Ollama、vLLM、MLX 或 llama-server 進行實測。成功結果會先儲存在本機，並優先取代公式估算。

加上 `--share` 後，llmfit 可透過 GitHub device flow 將結果整理成 PR，不需要 `gh` CLI。合併後的 benchmark 會在下一版本內建，讓相同 CPU/GPU 的使用者直接取得實測資料；可信任的 benchmark anchor 也可用來校準同硬體上的其他模型。

```text
公式估算 → 本機 benchmark → 校準 → 社群 PR → 下一版內建實測資料
```

## 9. 專案結構與資料更新

核心模組職責如下：

| 模組 | 職責 |
|---|---|
| `hardware` | RAM、CPU、GPU/VRAM 與 backend 偵測 |
| `models` | 模型資料、量化階層與記憶體估算 |
| `fit` | 執行路徑、Fit、評分、速度與 MoE offload |
| `analysis` | 建立整批 `ModelFit` 結果 |
| `providers` | 本地 runtime 整合、安裝偵測與下載 |
| `bench` / `benchmarks` | benchmark、社群資料與校準 |
| `plan` | 硬體需求與升級規劃 |
| `hwprofile` | 硬體 profile 管理與模擬 |
| `doctor` | 硬體診斷 |
| TUI/UI | `ratatui`、`crossterm` 終端介面 |

模型目錄由 scraper 更新：

```sh
make update-models
```

更新資料後需重新編譯，因為目錄會在編譯期嵌入 binary。

## 10. 安裝與建置

| 平台/方式 | 指令 |
|---|---|
| Windows | `scoop install llmfit` |
| macOS/Linux Homebrew | `brew install AlexsJones/llmfit/llmfit` |
| 快速安裝 | `curl -fsSL https://llmfit.axjns.dev/install.sh \| sh` |
| uv | `uv tool install -U llmfit` 或 `uvx llmfit` |
| Docker | `docker run ghcr.io/alexsjones/llmfit` |
| 原始碼 | `cargo build --release` |

從原始碼建置：

```sh
git clone https://github.com/AlexsJones/llmfit.git
cd llmfit
cargo build --release
```

## 11. 平台支援與限制

- Linux：NVIDIA、AMD、Intel Arc、Ascend 與 CPU 偵測最完整。
- Apple Silicon macOS：支援 unified memory、Metal 與 MLX。
- Intel macOS：RAM/CPU 可用，GPU 支援較有限。
- Windows：RAM/CPU 可用；NVIDIA 需能使用 `nvidia-smi`。
- Android/Termux/PRoot：通常只能偵測 CPU/RAM，行動 GPU 不一定能被目前介面辨識。

使用時應注意：

1. 速度估算不是所有模型/硬體組合的實測結果。
2. GPU 未辨識時會採用 backend 常數，精確度可能較低。
3. CPU offload 能載入不代表速度理想，Fit 最多為 `Good`。
4. Prefill/TTFT 需要 GPU FP16 throughput，未知時不會硬猜。
5. 特殊 runtime 模型可能被標記為 `unsupported`。
6. 模型資料在編譯期嵌入，需升級 llmfit 才能取得新版目錄。

## 12. 總結

llmfit 將模型規格、動態量化、硬體資源、推論 runtime、速度模型與 benchmark 資料整合成可解釋的選型流程。它的主要價值在於：

- 跨平台偵測多種 GPU、NPU、CPU 與 unified memory。
- 以實際記憶體使用率判斷模型能否穩定載入。
- 針對 MoE 區分總參數與 active parameters。
- 以記憶體頻寬估算 decode，並公開估算依據與可信度。
- 依 Coding、Reasoning、Chat 等任務調整推薦權重。
- 同時支援 TUI、CLI、JSON、REST API 與硬體模擬。
- 透過本機與社群 benchmark 持續校準估算。

因此，llmfit 可作為本機 LLM 選型工具、硬體採購前模擬器、模型部署檢查器、節點級排程 API，以及面向 Agent 的模型推薦服務。

## 參考資料

- [GitHub Repository](https://github.com/AlexsJones/llmfit)
- [How llmfit Works](https://github.com/AlexsJones/llmfit/blob/main/docs/how-it-works.md)
- [CLI & Automation](https://github.com/AlexsJones/llmfit/blob/main/docs/cli.md)
- [Runtime Provider Integration](https://github.com/AlexsJones/llmfit/blob/main/docs/providers.md)
- [Platform Support](https://github.com/AlexsJones/llmfit/blob/main/docs/platform-support.md)
- [Development](https://github.com/AlexsJones/llmfit/blob/main/docs/development.md)

## 2026-08-31 實測

- 先前有測試過 `llmfit` 指令，這個工具應該是從 LinkedIn 看到的。
- 測試環境：
```bash
OS: Windows (Unknown) x86_64
Uptime: 3 days, 14 hours, 57 mins
Packages: 23 (scoop)
Shell: bash 5.3.15
DE: Aero
Terminal: Windows Terminal
CPU: AMD Ryzen 7 7735HS with Radeon Graphics (16) @ 3.200GHz
Memory: 21376MiB / 31994MiB
```
- 安裝方式：
```bash
~/git/snippet/rust/llmfit$ scoop search llmfit
Results from local buckets...

Name   Version Source Binaries
----   ------- ------ --------
llmfit 1.1.12  main


~/git/snippet/rust/llmfit$ winget search llmfit
No package found matching input criteria.
```
```bash
~/git/snippet/rust/llmfit$ scoop install llmfit
```