# pi-ds4 技術報告（audreyt 版）

> 原名：pi-kami  
> 版本：0.8.1  
> 作者：Audrey Tang  
> 原始專案：[https://github.com/audreyt/pi-ds4](https://github.com/audreyt/pi-ds4)  
> 完整指南：[https://pi.audreyt.org/](https://pi.audreyt.org/)

---

## 摘要

pi-ds4（現命名為 pi-kami）是 pi 的 provider 延伸模組，可在地端運行兩個引擎：

1. **DeepSeek V4.1 Flash**：透過 [audreyt/ds4](https://github.com/audreyt/ds4) 運行，針對 128 GB Apple Silicon Mac 優化
2. **Flint**：透過 [recursive-oss/rec](https://github.com/recursive-oss/rec) 運行，適用於 M4 Pro/M5 Pro/M5 Max（48 GB 以上記憶體）

本報告提供完整的安裝、測試與使用步驟。

---

## 系統需求

### 支援的硬體平台

| 平台 | 記憶體 | 支援模式 | 備註 |
|------|--------|----------|-------|
| Apple Silicon | 128 GB | DeepSeek V4.1 Flash | 需先調高 Metal 有線記憶體限制 |
| Apple Silicon | >128 GB | DeepSeek V4.1 Flash | 無需調高限制 |
| M4 Pro / M5 Pro / M5 Max | 48–96 GB | Flint (experimental) | 不支援 DeepSeek 模式 |
| Linux + NVIDIA / AMD | 任意 | 需自行編譯 | 不支援官方的 IQ1_S 權重 |
| CPU 僅有 | 任意 | 需自行啟用 | 僅供參考/除錯使用 |

### 記憶體需求（管理式 DeepSeek Maya-XS）

- **安裝檔案大小**：~366.7 GB（語言模型 341.5 GB + vision 側車 926 MiB）
- **常驻記憶體**：~107.35 GB
- **Engram 表**：~189 GB（保留在磁碟上）
- **建議**：使用內部 SSD 以改善效能

---

## 快速開始

### 步驟 1：安裝延伸模組

```bash
# 移除舊版（如已安裝）
pi remove https://github.com/mitsuhiko/pi-ds4

# 安裝新版本
pi install https://github.com/audreyt/pi-kami
```

> **注意**：GitHub 會自動將 `audreyt/pi-ds4` 重定向到此處，只需安裝其中一個。

### 步驟 2：調高 Metal 有線記憶體限制（128 GB Mac）

```bash
# 立即生效
sudo sysctl iogpu.wired_limit_mb=114688

# 永久生效（加入 /etc/sysctl.conf）
echo "iogpu.wired_limit_mb=114688" | sudo tee -a /etc/sysctl.conf
```

> **注意**：延伸模組會在下載前檢查此設定，並提示執行命令。

### 步驟 3：啟動 pi

```bash
pi
```

首次啟動時，延伸模組會自動：
1. 克隆 `audreyt/ds4` 至 `~/.pi/ds4/support/`
2. 根據平台選擇合適的編譯目標
3. 下載 DeepSeek V4.1 Flash 1017 Maya-XS abliterated 模型
4. 啟動 `ds4-server --vision` 於 `127.0.0.1:8000`

---

## 詳細測試步驟

### 測試 A：DeepSeek V4.1 Flash（128 GB Mac）

#### 步驟 1：確認平台識別

```bash
# 檢查系統資訊
sysctl -n hw.memsize
sysctl -n hw.ncpu
```

#### 步驟 2：啟動 pi 並切換模型

```bash
pi
/model DeepSeek V4.1 Flash
```

#### 步驟 3：基本對話測試

```
pi> 你好
pi> 請用繁體中文解釋機器學習中的過擬配問題
pi> 寫一段 Python 程式碼，計算斐波那契數列前 20 項
```

**預期結果**：
- 回應流暢完整，非空白回應
- 繁體中文語意正確
- 程式碼可執行

#### 步驟 4：視覺能力測試（如適用）

```
pi> /read earth.jpg
```

**預期結果**：
- 正確讀取影像內容
- 視覺側車正常運作
- 上下文長度不超過 128k tokens

#### 步驟 5：效能測試

```bash
# 在終端機運行（需安裝 ds4 CLI）
cd ~/.pi/ds4/support
./ds4-server --vision gguf/DeepSeek-V4.1-Flash-1017-Vision.gguf

# 監控資源使用
sudo sysctl hw.active_pages
top -s 1
```

**預期結果**（M5 Max 128 GB）：
- 預處理（prefill）：~194 tokens/s（533-token 影像）
- 生成（generation）：~37 tokens/s
- 常驻記憶體：~107 GB

#### 步驟 6：生成煙霧測試（非 Metal 平台）

```bash
# 在另一終端機運行
cd ~/.pi/ds4/support
make cuda CUDA_ARCH=sm_90  # 或 sm_121 等
./ds4-server --vision gguf/DeepSeek-V4.1-Flash-1017-Vision.gguf

# 測試生成（不僅僅是 HTTP 200）
curl http://127.0.0.1:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "DeepSeek V4.1 Flash",
    "messages": [{"role": "user", "content": "Hello"}],
    "temperature": 0.7
  }' | jq '.choices[0].message.content'
```

**預期結果**：
- `choices[0].message.content` 非空白
- 非僅 HTTP 200 回應

---

### 測試 B：Flint（M4 Pro/M5 Pro/M5 Max，48 GB+）

#### 步驟 1：選擇 Flint 模式

```bash
pi
/model rec/flint
```

#### 步驟 2：自動安裝 rec

首次切換時，延伸模組會：
1. 檢查 `~/.local/bin/rec`
2. 安裝 rec 0.1.0（如未安裝）
3. 下載 Flint 模型（~23 GB）
4. 啟動 `rec serve` 於 `127.0.0.1:11500`

#### 步驟 3：基本對話測試

```
pi> 你好
pi> 請用繁體中文解釋機器學習中的過擬配問題
```

**預期結果**：
- 回應正常
- 注意：Flint 非 abliterated，無方向性引導（directional steering）

#### 步驟 4：效能測試

```bash
# 監控 rec 伺服器
curl http://127.0.0.1:11500/v1/models
curl http://127.0.0.1:11500/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "rec/flint",
    "messages": [{"role": "user", "content": "Hello"}],
    "temperature": 0.7
  }'
```

**注意**：早期社群回報顯示 Flint 在代理程式編碼（agentic coding）任務上表現弱於 Qwen3.8 27B。

---

### 測試 C：方向性引導（Directional Steering）

#### 步驟 1：啟用引導

```bash
# 設定環境變數
export DS4_DIR_STEERING_FILE=~/.pi/ds4/support/dir-steering/out/candor-v41.f32
export DS4_DIR_STEERING_FFN=0.5
export DS4_DIR_STEERING_ATTN=0
```

**說明**：
- `candor-v41.f32`：40 × 5120 的 float32 向量
- FFN 0.5 為推薦設定（適合編碼與工具使用）
- 測試顯示在 20 道算術/事實/程式碼檢查題全部通過

#### 步驟 2：測試政治敏感問題

```
pi> 請評價中華民國的歷史地位
```

**預期結果**：
- 無迴避性回應
- 提供客觀歷史分析

---

### 測試 D：Flint 伺服器管理

#### 步驟 1：確認伺服器狀態

```bash
# 查看 pi-kami 記錄檔
ls -la ~/.pi/kami/rec/
```

#### 步驟 2：切換回 DeepSeek（伺服器自動停止）

```bash
pi
/model DeepSeek V4.1 Flash
```

延伸模組會在最後一個 pi-kami 視窗關閉時停止 rec 伺服器。

---

### 測試 E：Bring-Your-Own Binary（BYOB）

適合除錯 CUDA 或自訂編譯目標時使用。

#### 步驟 1：克隆 ds4

```bash
git clone https://github.com/audreyt/ds4
cd ds4
git checkout d0c2b43  # 或使用其他 pinned commit
```

#### 步驟 2：編譯目標

```bash
# 根據平台選擇
make ds4-server        # macOS（Metal）
make cuda-spark        # NVIDIA GB10 Spark
make cuda CUDA_ARCH=sm_90  # 其他 NVIDIA
make strix-halo        # AMD ROCm
make cpu               # CPU 僅有
```

#### 步驟 3：指定 runtime 目錄

```bash
export DS4_RUNTIME_DIR=/path/to/ds4/checkout
pi
```

延伸模組不會覆蓋此目錄的二進位檔。

---

### 測試 F：平台錯誤診斷

#### 症狀：CUDA 編譯錯誤

```bash
# 錯誤訊息：
# "wrong-arch / degenerate CUDA output"
```

#### 解決方案：

```bash
# 清除緩存
rm -f ~/.pi/ds4/support/ds4-server
rm -f ~/.pi/ds4/support/ds4-agent
rm -f ~/.pi/ds4/build.json

# 重新編譯（GB10 Spark 示例）
cd ~/.pi/ds4/support
make clean && make cuda-spark

# 或設定環境變數
export DS4_BUILD_TARGET=cuda-spark
export DS4_CUDA_ARCH=sm_121
```

#### 症狀：生成結果空白

```bash
# 檢查回應內容
curl http://127.0.0.1:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "test", "messages": [{"role": "user", "content": "Hello"}]}' | jq '.choices[0].message.content'
```

**預期**：非空白字串

如為空白，可能是編譯目標錯誤（如錯誤的 CUDA arch）。

---

## 配置參數

### 環境變數清單

| 參數 | 說明 | 預設值 |
|------|------|--------|
| `DS4_SUPPORT_REPO` | Git URL | `audreyt/ds4` |
| `DS4_SUPPORT_PIN` | 強制 commit | `0dff39f` |
| `DS4_PROTOCOL` | 通訊協定 | `openai` |
| `DS4_BUILD_TARGET` | 編譯目標 | 自動偵測 |
| `DS4_CUDA_ARCH` | CUDA arch | `sm_XX` |
| `DS4_BACKEND` | 後端 | `metal`/`cuda`/`rocm`/`cpu` |
| `DS4_ALLOW_CPU` | CPU 回退 | `false` |
| `DS4_SKIP_BUILD_SMOKE` | 跳過煙霧測試 | `false` |
| `DS4_REPRODUCIBLE` | 可重複性 | `1` |
| `DS4_REPRODUCIBLE_SEED` | 種子 | `42` |
| `DS4_CONTEXT_KB` | 上下文 | `128` |
| `DS4_KV_DISK_SPACE_MB` | KV 空間 | 自動分層 |
| `DS4_DIR_STEERING_FILE` | 引導向量 | 空 |
| `DS4_DIR_STEERING_FFN` | FFN 強度 | `0.5` |
| `DS4_DIR_STEERING_ATTN` | ATTN 強度 | `0` |
| `DS4_RUNTIME_DIR` | 自帶 runtime | - |
| `DS4_MODEL_QUANT` | 模型選擇 | `maya-xs`/`q1`/`preferred` |
| `PI_KAMI_REC_UNPINNED` | Flint 未鎖定 | `false` |

---

## 已知限制

1. **Flint 僅測試於 128 GB M5 Max**：48–96 GB Mac 尚未測試
2. **工具呼叫品質**：無自動化測試大型工具 schema
3. **CUDA/DSpark 效能**：需正確編譯目標才有效
4. **ABLiterated 品質**：僅通過基本煙霧測試，未運行完整評分套件
5. **上下文長度**：視覺預設 128k，純文字 Maya-XS 支援 262k

---

## 效能參考（M5 Max 128 GB）

| 任務 | 結果 |
|------|------|
| 純文字生成 | ~37.9 tokens/s |
| 影像預處理（533 tokens） | ~194 tokens/s |
| 影像預處理（195 tokens） | ~148 tokens/s |
| 影像生成 | ~37 tokens/s |
| Headroom128 @ 2k ctx | ~622 t/s 預處理 / ~42 t/s 生成 |

> **注意**：以上為單次測試結果，非 `ds4-bench` 掃瞄。

---

## 更新日誌

### v0.8.1（2026-11-01）
- candor 引導預設 0.5
- 編碼與工具使用推薦設定

### v0.8.0（2026-10-23）
- 正式命名為 pi-kami
- 新增實驗性 Flint 層

### v0.7.3
- 鎖定 Maya-XS abliterated 模型與引擎 `0dff39f`
- 128k 視覺上下文預設

### v0.7.0（2026-10-20）
- 管理式模型切換為 DeepSeek V4.1 Flash 1017 abliterated Q1
- 128 GB Mac 以下不支援

---

## 相關專案

| 專案 | 說明 |
|------|------|
| [mitsuhiko/pi-ds4](https://github.com/mitsuhiko/pi-ds4) | 上游延伸模組 |
| [audreyt/ds4](https://github.com/audreyt/ds4) | DeepSeek V4/V4.1 Flash 引擎 |
| [recursive-oss/rec](https://github.com/recursive-oss/rec) | Flint 推理引擎 |
| [Project Maya](https://huggingface.co/peasantsmith/DeepSeek-V4.1-Flash-1017-Maya-GGUF) | IQ1_S 專家與 Q8 張量 |
| [kernelpool/ds4](https://github.com/kernelpool/ds4) | V4.1 Metal 除錯與預處理 |

---

## 授權

MIT，與上游一致。

---

## 參考資源

- 完整指南：[https://pi.audreyt.org/](https://pi.audreyt.org/)
- ds4 官方文件：[https://github.com/audreyt/ds4/blob/main/dir-steering/README.md](https://github.com/audreyt/ds4/blob/main/dir-steering/README.md)
- Reddit 討論：[https://www.reddit.com/r/LocalLLaMA/comments/1xc23iq/](https://www.reddit.com/r/LocalLLaMA/comments/1xc23iq/)

---

**撰寫日期**：2026-11  
**撰寫者**：AI 助手  
**版本**：1.0
