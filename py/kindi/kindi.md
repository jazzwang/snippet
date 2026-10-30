# Kindi

- Git Repo
  - https://github.com/ahtx/kindi
- Website
  - https://amirhusain.com/software/kindi/

## 2026-10-30

- 緣起：看到這個 YouTube 影片，用 NotebookLM 生成摘要介紹
  - title: "27B AI on a $400 AMD Mini PC | Kindi 0.3 is OUT"
  - source: https://www.youtube.com/watch?v=8_TkKTcWKg0
  - created: 2026-10-30

## 400 美元 Mini PC 也能跑 27B 大模型？Kindi 0.3 重磅釋出：平價硬體推動區域端 AI 大革命

### 1. 引言：打破高昂硬體壁壘，人人都能擁有的區域端 AI

不必再眼紅企業機房裡動輒數萬美元的 Nvidia H100 或 A100 機櫃！在大語言模型（LLM）狂飆的時代，許多開發者與機構常被高不可攀的硬體成本擋在門外。然而，區域端 AI 的未來不該只是少數巨頭或富裕實驗室的專利。

最新正式於 GitHub 上架的 **Kindi 0.3**，正是為了打破這個高昂硬體壁壘而生。身為一個以極致優化為核心的開源專案，Kindi 0.3 的哲學非常明確：**用軟體架構的創新賦能平價硬體，讓人人都能在本地端順暢運行高效能 AI**。無論你是預算有限的獨立開發者、學校教室，還是手邊只有二手老卡、舊款 CPU 或一台 400 美元 Mini PC 的玩家，區域端 AI 的革命都已經在你桌上發生。

### 2. 硬體支援大躍進：從百元中古老卡到 AMD Mini PC

Kindi 專案最早僅支援一張老舊的 Nvidia 420 顯示卡，但在最新的 0.3 版本中，團隊在硬體相容性上實現了跨越式的突破，從平價的小型主機到二手市場的「神卡」均全面解鎖。

#### 2.1 邁向 AMD 平台與 Mini PC
Kindi 0.3 正式納入對 AMD 平台的支援，特別是搭載 **AMD 780M** 內顯的平價小型主機（例如搭載 AMD Ryzen 9 7940HS、售價僅約 400 美元的 Mini PC）。在測試中，AMD 780M 運行大模型時的寫入速度可高達 **106 tokens/sec**（比 Llama 快上 230% 至 10 倍不等）。

更具架構價值的是，Kindi 支援異構協同運算：使用者能讓 Mini PC 的 GPU 運行 27B（270 億參數）大模型，同時讓同一台機器的 CPU 運行 2B 小模型。在 Agentic 多模組架構中，這種「大模型負責複雜推理、小模型負責快速路由分類」的雙模組協同，提供了極高實用性的解法。

#### 2.2 eBay 神卡現身：Nvidia K6000
對於預算極度吃緊但需要大顯存（VRAM）的開發者，二手市場上僅需約 80 美元（含運費 100 美元以內）即可購得擁有 12GB VRAM 的 **Nvidia K6000**。Kindi 0.3 完美支援此卡，在小 Prompt 下能以 **20 tokens/sec** 的穩定速度運行 27B 大模型。相比於串聯兩張 K1200 僅能湊出 8GB VRAM，12GB 的 K6000 提供了更充裕的長文本上下文（Context Window）運算空間。

#### 2.3 CPU 成為一等加速平台
針對完全沒有獨立顯卡的舊設備（例如舊款 Intel i7-8700 CPU 主機），Kindi 0.3 將 CPU 提升為一等加速平台（First-class Accelerated Platform）。在運行 2B 模型時，i7-8700 能達到 **42.5 tokens/sec 的讀取速度（Read Speed）**，且寫入效能為 Llama 的 1.6 倍，讓學校教室或舊設備重新煥發 AI 生產力。

| 硬體裝置 / 晶片 | 預算與規格特點 | 支援模型與效能表現 |
| :--- | :--- | :--- |
| **AMD 780M** (如 Ryzen 9 7940HS Mini PC) | 約 $400 美元 / 平價小型主機 | GPU 支援 27B / Neotron 35（寫入達 **106 tokens/sec**）；可同時搭配 CPU 運行 2B 模型 |
| **Nvidia K6000** | 約 $80-$100 美元 (二手含運) / 12GB VRAM | 以 **20 tokens/sec** 順暢運行 27B 模型，提供極高 CP 值的長 Context 空間 |
| **Intel i7-8700** | 舊款平價 CPU / 無獨立 GPU | 運行 2B 模型時，讀取速度達 **42.5 tokens/sec**，寫入效能為 Llama 的 **1.6 倍** |

### 3. 核心效能與機制優化：多分支快取與 GPU 解鎖

Kindi 0.3 透過底層軟體架構的重新設計，實現了推理速度與記憶體利用率的極致提升：

*   **多分支快取（Multibranch Cache）**：在 Agentic 工作流程（如搭配 Pi 框架）中，系統常需發送重複的根提示詞（Root Prompt）。Kindi 0.3 的多分支快取能將對話樹狀結構的根部 Prompt 鎖定在記憶體中，當多條 Agent 對話分支發散時，無需重複計算根部，且**完全不額外佔用 VRAM**，為多 Agent 協同對話帶來爆發性的加速。
*   **GPU 解鎖（GPU Unlock）整合**：直接整合由社群開發者 Zagita 打造的 GPU 解鎖模組。系統能自動檢測並解鎖 Nvidia 30 系列（如 3060、3080、3090）及 20 系列顯示卡中隱藏的 Tensor 運算單元，直接釋放硬體潛藏的物理算力。
*   **記憶體與 OOM 管理**：針對 VRAM 臨界點進行了深度的記憶體分配修復，大幅降低在極限記憶體邊緣運算時發生 Out-of-Memory (OOM) 崩潰的風險。

### 4. 體驗全面升級：極簡安裝、顯卡資料庫與 Kindi Bridge

除了核心效能，Kindi 0.3 對開發者工具鏈與 UI/UX 體驗進行了全方位補強：

#### 官網與顯卡資料庫
全新的官方下載頁面新增了線上顯卡資料庫。使用者可以直接輸入顯卡型號（例如 P2000、K6000），系統會比對官方測試與社群回報（Community Reports）數據，即時顯示該卡片支援的模型清單與預期推理速度。

#### 智慧安裝與 Dry Run 模式
保持單行 Bash 指令安裝的便利性，同時加入安全 `--dry-run` 模式（僅顯示預計執行的系統操作而不實際修改）。此外，安裝程式具備智慧硬體偵測功能，例如偵測到雙張 4GB 的 K1200 顯卡時，會自動給出最佳配置建議，將 27B 模型自動拆分至兩張卡上**加載運行**。

#### CLI 模型目錄
提供極簡的命令列工具：

```bash
kindi models
kindi use
```

系統會列出適合當前硬體的模型清單，並自動完成模型下載、量化（Quantization）與切換，無需人工設定複雜參數。

#### 前瞻搶先看：Kindi Bridge
即將推出的 Terminal UI 工具 Kindi Bridge（底層基於 Linux 經典的 `tmux` 終端機複用技術打造），支援平鋪視窗（Tiled Windows）與硬體即時監控（Hardware Vitals）。在實測演示中，於舊款 GTX 1080 顯卡上運行 27B GGUF 量化模型，能以 **28 tokens/sec** 的速度分析 C 語言程式碼，精準找出 `LL1.c` 中被賦值卻未被讀取的指標變數 `last`。該 UI 極為輕量，甚至能在 Raspberry Pi 上作為前端遠端操控後端運算。

### 5. 新一代模型生態系支援：Nvidia Neotron

除了原有的 Prism 系列模型外，Kindi 0.3 正式擴展對最新模型生態系的支援，全面相容 **Nvidia Neotron** 系列（如 Neotron 35）。使用者只需透過 CLI 選取，Kindi 便會在背景自動完成下載、量化與設定，讓平價硬體也能無縫銜接最新的 AI 模型研究成果。

### 6. 總結與核心帶走點（Takeaways）

Kindi 0.3 的發布證明了一件事：**AI 推理的瓶頸往往不是硬體不夠貴，而是軟體優化不夠深**。透過架構創新，平價與中古硬體同樣能承載大模型的重任。

1. **平價硬體解放巨量算力**：400 美元的 AMD 780M Mini PC 可順暢執行 27B 模型，低於 100 美元的 Nvidia K6000 憑藉 12GB VRAM 實現 20 tokens/sec 推理，連舊款 Intel CPU 也能煥發新生。
2. **底層架構雙重突破**：透過多分支快取（Multibranch Cache）節省 VRAM 並優化 Agent 流程，結合 Zagita GPU Unlock 模組直接釋放 Tensor 核心潛能。
3. **極致友善的開發者體驗**：提供線上顯卡 Benchmark 資料庫、智慧多卡加載建議、CLI 自動下載量化（`kindi models` / `kindi use`），以及基於 tmux 的輕量級 Kindi Bridge 終端機介面。
4. **新一代生態無縫升級**：原生支援包含 Nvidia Neotron 35 在內的新一代模型，推動普及型區域端 AI 的應用落地。

**開源社群共建呼籲**：專案發起人 Amir Husain 熱烈邀請全球開發者與玩家回報各自顯示卡的測試數據（Community Benchmarks），充實官方線上資料庫。如果你手邊也有各式中古卡或 Mini PC，不妨立即下載 Kindi 0.3 進行測試，一同推動平價區域端 AI 的民主化浪潮！

-----

- 接著用 Pi Agent + llama.cpp/unsloth/Qwen3.5-9B 生成以下測試指南

> [!NOTE]
> 請根據 https://github.com/ahtx/kindi 撰寫一篇技術報告並包含 step-by-step 測試步驟，經 /skill:speak-human-tw 潤飾詞句後，儲存至 kindi.md

## Kindi 技術報告：為舊式 GPU 量身打造的推理引擎

### 1. 專案概述

Kindi 是由 Amir Husain 開發的專屬推理引擎，專為 Prism ML 的 **Ternary-Bonsai-2** 語言模型（2B、4B、9B 和 27B 參數，採用三元權重）設計。該專案最引人注目的成就是讓 10 年前的 **NVIDIA Quadro K420**（僅 1 GB 顯存）能實現 22.9 tokens/秒的推播速度，與現代推理引擎相比快上 13 倍。

#### 核心優勢

| 指標 | Kindi 0.2.0 | llama.cpp (Vulkan) | 性能提升 |
|------|------------|-------------------|---------|
| 生成速度 (512 token) | 20.8 tokens/s | 1.65 tokens/s | **13x 快** |
| 提示讀取 (512 token) | 33.3 tokens/s | 1.2 tokens/s | **28x 快** |
| 最大上下文 (K420) | 24,576 tokens | 8,192 tokens (崩潰) | **3x 深** |

### 2. 支援硬體

#### NVIDIA GPU
| GPU | 記憶體 | 最佳模型 | 生成速度 (tokens/s) |
|-----|--------|---------|-------------------|
| Quadro K420 (Kepler, sm_30) | 1 GB | 2B | 22.9 @ 2K ctx |
| Quadro K420 (2 GB) | 2 GB | 4B | - |
| Quadro K1200 | 4 GB | 9B | 23.4 |
| 2× Quadro K1200 | 8 GB | 27B (Tensor Parallel) | 12.6 |
| GeForce GTX 1080 | 8 GB | 27B | 27.9 @ 512 ctx |
| GeForce RTX 3080 | 10 GB | 27B (Tensor Core) | 63.2 @ 1K ctx |
| Quadro K6000 | 12 GB | 27B | 20.4 @ 156K ctx |

#### AMD GPU
| GPU | 記憶體 | 最佳模型 | 生成速度 (tokens/s) |
|-----|--------|---------|-------------------|
| Radeon 780M (gfx1103) | 需 32GB+ RAM | 27B | 9.7 @ 24K ctx |

#### CPU 引擎
| CPU | 模型 | 生成速度 | 相比 llama.cpp 提升 |
|-----|------|---------|-------------------|
| Ryzen 9 7940HS (8 核心) | 2B | 64.8 tokens/s | **2.7x** |
| Core i7-8700 (6 核心) | 2B | 28.9 tokens/s | **1.6x** |

### 3. 技術原理

#### 3.1 三元權重表查 (Ternary GEMV by Table Lookup)

Kindi 從不 unpack 三元權重。每 4 個三元權重壓縮為 1 個字節（81 種可能值：t0 + 3t1 + 9t2 + 27t3）。

**關鍵優化：**
- **每線程專屬表**：避免 32 個 warp 線程競爭共享記憶體
- **無衝突表建構**：三元遞迴構造（類同三分康托集）
- **單指令尋址**：256 字節 stride 搭配 `__byte_perm` 直接計算地址
- **交錯行存儲**：每 16 字節 4 行，達到 24 GB/s 的記憶體寬度
- **延遲預取**：在當前階段計算時載入下一階段輸入
- **融合運算**：q/k/v、gate/up、qkv/gate 等最多三枚矩陣融合為一次 launch

#### 3.2 核心技術

| 技術 | 描述 |
|------|------|
| GDN glue | 閘門、因果 conv + SiLU、L2 範數和 delta 規則更新，僅需四個 kernel |
| 融合 RMSfold + Hadamard | 在正規化 kernel 中同時應用旋轉 |
| fp16 K/V cache | 記憶體减半，支援 24,576 token 上下文 |
| GQA 感知 kernel | 每個 K/V 行只讀一次供 4 個 query head |
| 短列表輸出頭 | 球形 k-means 聚類成 1,024 群，最佳 256 群 (~13% 行) 才計算 GEMV |
| 無詞表複製採樣 | GPU 上用二元搜尋找 top-k threshold，僅複製候選者到 host |

#### 3.3 提示緩存

三層緩存機制：
1. **檢查點（Recurrent-state checkpoints）**：保持 GDN 層的狀態
2. **停車對話（Parked conversations）**：保存活躍對話
3. **已存開啟（Saved openings）**：存盤的系統提示

效能對比（GTX 1080，Nemotron）：
| 作業 | Kindi 緩存關 | Kindi 緩存開 | llama.cpp 緩存開 |
|------|------------|------------|-----------------|
| Agent turn 2 | 2.76s | 0.67s | 1.29s |
| 文件 Q3 | 10.71s | 0.42s | 3.10s |

### 4. 安裝與使用

#### 4.1 一鍵安裝

```bash
curl -fsSL https://amirhusain.com/kindi/install.sh | bash
```

**預先驗證（推薦）：**
```bash
curl -fsSLO https://amirhusain.com/kindi/install.sh
echo "4079515dd373384cd4e68e8a747ba9e667bf36d81ac3132f87886273ae96d38a  install.sh" | sha256sum -c -
bash install.sh --dry-run
```

#### 4.2 Docker 安裝（推薦）

```bash
git clone https://github.com/ahtx/kindi.git && cd kindi
docker build -t kindi:0.3.0 -f docker/Dockerfile .
```

檢查 GPU 識別：
```bash
mkdir -p ~/.kindi
docker run --rm --gpus all -u $(id -u):$(id -g) -v ~/.kindi:/data kindi:0.3.0 info
```

#### 4.3 原生安裝（需要 CUDA 10.2 + CuPy 9.6）

```bash
curl -fsSLO https://amirhusain.com/kindi/install.sh
bash install.sh --yes
```

### 5. 測試步驟（Step-by-Step）

#### 測試 1：安裝驗證

**目標**：確認安裝腳本正常執行且識別到 GPU

```bash
## 步驟 1：下載並驗證 checksum
curl -fsSLO https://amirhusain.com/kindi/install.sh
echo "4079515dd373384cd4e68e8a747ba9e667bf36d81ac3132f87886273ae96d38a  install.sh" | sha256sum -c -

## 步驟 2：預覽安裝步驟（不實際執行）
bash install.sh --dry-run

## 步驟 3：執行完整安裝（或 --auto 自動選擇推薦方案）
bash install.sh --auto
```

**預期結果**：
- 顯示每台 GPU 的支援設定
- 下載並驗證 GGUF 模型 sha256
- 執行 `kindi convert` 和 `kindi verify`
- 啟動 Docker 容器，監聽 127.0.0.1:8093

#### 測試 2：基本資訊檢查

**目標**：確認服務正常啟動並識別模型參數

```bash
## 檢查服務狀態
docker ps | grep kindi

## 獲取服務資訊
curl http://127.0.0.1:8093/info

## 檢查模型配置
curl http://127.0.0.1:8093/models
```

**預期結果**：
- 返回 JSON 格式的系統資訊
- 列出已載入模型及其參數
- 顯示 GPU 記憶體使用情況

#### 測試 3：llama.cpp 準確性驗證

**目標**：確認輸出與 llama.cpp 完全一致

```bash
## 測試驗證命令
kindi verify

## 或指定模型進行驗證
kindi verify -m 2b
```

**預期結果**：
- 顯示 token 完全匹配的統計
- 如 README 所述，與 llama.cpp 逐 token 一致

#### 測試 4：效能基準測試

**目標**：測量生成和讀取速度

```bash
## 生成速度基準
kindi bench -w 256  # 生成 256 tokens

## 提示讀取速度基準
kindi bench -r 2000  # 讀取 2000 token 提示
```

**預期結果**：
- 輸出 tokens/秒的統計數據
- 生成速度應與 WHY.md 中的數值相符（K420: ~22.9 tokens/s）

#### 測試 5：OpenAI API 介面測試

**目標**：確認 chat 和 tool call 功能正常

```bash
## 基本聊天測試
curl http://127.0.0.1:8093/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "2b",
    "messages": [{"role": "user", "content": "Hello, how are you?"}],
    "stream": true
  }'

## 工具調用測試
curl http://127.0.0.1:8093/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "2b",
    "messages": [
      {"role": "user", "content": "What is the current temperature?"},
      {"role": "assistant", "content": null, "tool_calls": [{"id": "tool_123", "type": "function", "function": {"name": "get_temperature", "arguments": {}}}]},
      {"role": "tool", "tool_call_id": "tool_123", "content": "25°C"}
    ],
    "stream": false
  }'
```

**預期結果**：
- 流式輸出 JSON Lines
- 工具調用正確執行並返回結果

#### 測試 6：提示緩存效能測試

**目標**：驗證三層緩存機制

```bash
## 使用基準測試腳本
cd examples
python prompt_cache_bench.py

## 或使用 API 模擬多輪對話
curl http://127.0.0.1:8093/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "2b",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "What is Python?"}
    ]
  }'

curl http://127.0.0.1:8093/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "2b",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "What is NumPy?"}
    ]
  }'
```

**預期結果**：
- 第二個請求應比第一個快（提示緩存生效）
- 參考數據：Kindi 緩存開 vs 關，提升約 80-90%

#### 測試 7：Agent 工作流測試

**目標**：驗證在自動化代理環境中的表現

```bash
## 模擬 pi coding agent 工作流
## 1. 檢查 GPU
curl http://127.0.0.1:8093/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "2b", "messages": [{"role": "user", "content": "Run nvidia-smi"}], "stream": false}'

## 2. 執行 Python 腳本
curl http://127.0.0.1:8093/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "2b", "messages": [{"role": "user", "content": "Write a Python script to check disk space"}], "stream": false}'

## 3. 檢查結果
curl http://127.0.0.1:8093/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "2b", "messages": [{"role": "user", "content": "What is the disk space?"}], "stream": false}'
```

**預期結果**：
- 多輪對話流暢無延遲
- 工具調用正確執行
- 參考數據：Kindi 緩存開，Agent turn 2 仅需 0.67s（vs 關緩存的 2.76s）

#### 測試 8：上下文長度測試

**目標**：驗證不同上下文大小的表現

```bash
## 使用較長提示（例如 8K tokens）
curl http://127.0.0.1:8093/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "2b",
    "messages": [{"role": "user", "content": "（8K token 的長文檔內容）"}],
    "stream": true
  }'

## 測試 27B 模型的長上下文
curl http://127.0.0.1:8093/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "27b",
    "messages": [{"role": "user", "content": "（8K token 的長文檔內容）"}],
    "stream": true
  }'
```

**預期結果**：
- K420: 最大 24,576 tokens
- RTX 3080: 可達 90K+ tokens
- 輸出應與提示內容相關且無截斷

### 6. 故障排除

#### 常見問題

**問題 1：安裝腳本失敗**
```bash
## 檢查 GPU 驅動
nvidia-smi
## 或
amdgpu_info

## 手動驗證 CUDA
nvcc --version
```

**問題 2：Docker 無法識別 GPU**
```bash
## 檢查 Docker 配置
docker run --rm --gpus all -v ~/.kindi:/data kindi:0.3.0 info

## 安裝 NVIDIA Container Toolkit
sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker
```

**問題 3：RTX 30 系列 GPU 效能未達預期**
```bash
## 安裝 gpu-unlock 模組
git clone https://github.com/Zagitta/gpu-unlock
sudo dpkg -i gpu-unlock_*.deb
```

**問題 4：AMD Radeon 780M 配置問題**
```bash
## 驗證 kernel 參數
grep amdgpu /proc/cmdline

## 需要設定：amdgpu.cwsr_enable=0
## 安裝時會提示此選項
```

### 7. 配置選項

| 選項 | 說明 | 範例 |
|------|------|------|
| `--dry-run` | 預覽步驟，不執行 | `bash install.sh --dry-run` |
| `--auto` | 自動選擇推薦設定 | `bash install.sh --auto` |
| `--yes` | 自動回答所有確認問題 | `bash install.sh --yes` |
| `--config N` | 指定設定編號 | `bash install.sh --config 2,8` |
| `--gpu G` | 選擇 GPU | `--gpu 0,1` 或 `--gpu all` 或 `--gpu cpu` |
| `--port P` | 指定服務端口 | `--port 8094` |
| `--ctx N` | 設定上下文長度 | `--ctx 40960` |

### 8. 開源與授權

- **授權協議**：AGPL-3.0（商業授權可洽）
- **模型來源**：Prism ML 的 Ternary-Bonsai-2-2B（Qwen3.5-2B 架構，Apache 2.0）
- **專案頁**：https://amirhusain.com/kindi/
- **YouTube 影片**：https://youtu.be/ddAnghj8HpE

### 9. 參考資源

- 安裝說明：[docs/INSTALL.md](docs/INSTALL.md)
- 技術原理：[docs/HOW-IT-WORKS.md](docs/HOW-IT-WORKS.md)
- 性能基準：[docs/BENCHMARKS.md](docs/BENCHMARKS.md)
- Docker 配置：[docs/DOCKER.md](docs/DOCKER.md)
- 故障排除：[docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)
- AMD 支援：[docs/AMD.md](docs/AMD.md)

*報告撰寫日期：2026-10-30*
*Kindi 版本：0.3.0*

-----

## 自己動手測測看

- 環境：Windows 11 + WSL + Docker CE
```bash
~/git/snippet/py/kindi$ wsl
Welcome to Ubuntu 24.04.2 LTS (GNU/Linux 6.18.33.2-microsoft-standard-WSL2 x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Fri Oct 30 12:09:04 PM CST 2026

  System load:  0.0                 Processes:             68
  Usage of /:   5.3% of 1006.85GB   Users logged in:       0
  Memory usage: 4%                  IPv4 address for eth0: 172.29.78.252
  Swap usage:   0%

 * Canonical Workshop gives developers fast, composable, reproducible, and
   secure developer environments that are perfect for agentic workflows.

   https://ubuntu.com/workshop

This message is shown once a day. To disable it please create the /home/jazz/.hushlogin file.
/mnt/c/Users/jazzw/git/snippet/py/kindi$ cd /tmp
/tmp$ git clone https://github.com/ahtx/kindi.git && cd kindi
/tmp$ docker build -t kindi:0.3.0 -f docker/Dockerfile .
Successfully built 842cebf58576
Successfully tagged kindi:0.3.0

/tmp/kindi$ docker images
REPOSITORY               TAG             IMAGE ID       CREATED          SIZE
kindi                    0.3.0           842cebf58576   41 minutes ago   2.81GB
```
```bash
/tmp/kindi$ docker run --rm --gpus all -u $(id -u):$(id -g) -v .kindi:/data kindi:0.3.0 info
docker: Error response from daemon: could not select device driver "" with capabilities: [[gpu]]

Run 'docker run --help' for more information
```
```bash
/tmp/kindi$ sudo apt-get install -y nvidia-container-toolkit
[sudo] password for jazz:
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
E: Unable to locate package nvidia-container-toolkit
```
- https://share.google/aimode/PTrVb0BdFda1KNTbM
```bash
/tmp/kindi$ curl -fsSL https://github.io | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg   && curl -s -L https://github.io |     sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' |     sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
File '/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg' exists. Overwrite? (y/N) y
gpg: no valid OpenPGP data found.
```
```bash
/tmp/kindi$ sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
E: Unable to locate package nvidia-container-toolkit
```
- https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html
