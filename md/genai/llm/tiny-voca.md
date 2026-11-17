# tiny-voca 技術報告

> **最後更新日期**: 2026-11-17T00:36:19+08:00

## 模型概述

`tiny-voca` 是由 Muhammed Nazeem 開發的小型英語文字轉語音（Text-to-Speech, TTS）模型，具有兩個固定聲線（F2 女聲、M2 男聲）。該模型總計 **453.7 萬參數**，完全基於 17.6 小時合成語音數據訓練，不包含任何預訓練權重。

### 主要特性

| 項目 | 說明 |
|------|------|
| **模型大小** | 4,537,291 參數 |
| **聲線** | F2（女聲）、M2（男聲） |
| **輸出規格** | 24 kHz 單聲道 |
| **執行速度** | CPU 4 核心約 70 倍實時速度 |
| **授權** | Apache-2.0 |
| **訓練成本** | 單一 RTX 4090 GPU，7.7 小時，約 $9.56 |

---

## 安裝步驟

### 前置條件

- Python 3.8+
- pip 封裝管理工具
- 至少 100 MB 可用儲存空間
- 測試環境建議：GPU（可選）、CPU（推薦 4 核心以上）

### 步驟 1：安裝相依套件

```bash
# 安裝語音轉換器（phonemizer）
pip install git+https://github.com/n4ze3m/dizione

# 安裝 tiny-voca 模型
pip install git+https://github.com/n4ze3m/tiny-voca
```

### 步驟 2：下載模型權重

```bash
# 使用 HuggingFace Hub 下載模型檔案
hf download n4ze3m/tiny-voca --local-dir tiny-voca
```

下載完成的檔案包含：

- `tiny-voca.pt` (18.2 MB) - PyTorch 權重
- `onnx/model.onnx` (21.4 MB) - ONNX 格式
- `config.json` - 模型設定與音節詞典
- `phonemizer/` (5.4 MB) - 語音轉換資料
- `samples/` - 示範音訊檔案

### 步驟 3：設定環境變數

```bash
# 設定語音轉換器資料路徑
export DIZIONE_DATA=tiny-voca/phonemizer
```

---

## 測試步驟

### 測試 1：PyTorch 推理測試

```bash
python -m tiny_voca.infer \
  --checkpoint tiny-voca/tiny-voca.pt \
  --voice F2 \
  --text "Hello! This is tiny voca." \
  --output hello.wav
```

### 測試 2：ONNX 推理測試

```python
import numpy as np
import onnxruntime as ort
import soundfile as sf
import dizione  # 需要設定 DIZIONE_DATA 環境變數

# 設定環境變數（Python 中）
import os
os.environ['DIZIONE_DATA'] = 'tiny-voca/phonemizer'

# 文字轉音節
phones = dizione.phonemize("Hello! This is tiny voca.")

# 建立 ONNX 推理會話
session = ort.InferenceSession("tiny-voca/onnx/model.onnx")

# 準備輸入
one = lambda value: np.array([value], dtype=np.float32)

input_data = {
    "tokens": np.array([phones.ids], dtype=np.int64),
    "stress": np.array([phones.stress], dtype=np.int64),
    "voice": np.array([0], dtype=np.int64),      # 0 = F2, 1 = M2
    "speed": one(1.0),
    "pitch_shift": one(0.0),
    "pitch_range": one(1.0),
}

# 執行推理
audio, durations = session.run(None, input_data)

# 音量歸一化（避免超過 1.0）
audio = audio[0]
audio = audio * min(1.0, 0.99 / np.abs(audio).max())

# 儲存音訊
sf.write("hello.wav", audio, 24000)
```

### 測試 3：批量測試不同聲線

```bash
# 女聲 F2
python -m tiny_voca.infer \
  --checkpoint tiny-voca/tiny-voca.pt \
  --voice F2 \
  --text "這是台灣語音合成測試。" \
  --output f2_test.wav

# 男聲 M2
python -m tiny_voca.infer \
  --checkpoint tiny-voca/tiny-voca.pt \
  --voice M2 \
  --text "這是台灣語音合成測試。" \
  --output m2_test.wav
```

---

## 驗證步驟

### 驗證 1：功能性測試

```bash
# 測試不同參數組合

# 調整語速（1.5 倍速）
python -m tiny_voca.infer \
  --checkpoint tiny-voca/tiny-voca.pt \
  --voice F2 \
  --text "快速測試語速。" \
  --speed 1.5 \
  --output fast.wav

# 調整音高（降低半音）
python -m tiny_voca.infer \
  --checkpoint tiny-voca/tiny-voca.pt \
  --voice F2 \
  --text "調整音高測試。" \
  --pitch-shift 0.058 \
  --output lowpitch.wav
```

### 驗證 2：檔案格式驗證

```python
import numpy as np
import soundfile as sf

# 讀取產生的 WAV 檔案
audio, sample_rate = sf.read("hello.wav")

# 驗證參數
assert sample_rate == 24000, "採樣率應為 24 kHz"
assert audio.ndim == 1, "應為單聲道"
assert np.max(np.abs(audio)) <= 1.0, "音量不應超過 1.0"

print(f"✓ 採樣率: {sample_rate} Hz")
print(f"✓ 聲道數: {audio.ndim}")
print(f"✓ 音訊長度: {len(audio)} 樣本")
print(f"✓ 最大音量: {np.max(np.abs(audio)):.4f}")
```

### 驗證 3：效能測試

```bash
# 測試 CPU 執行速度
python -c "
import time
import subprocess

start = time.time()
subprocess.run([
    'python', '-m', 'tiny_voca.infer',
    '--checkpoint', 'tiny-voca/tiny-voca.pt',
    '--voice', 'F2',
    '--text', '效能測試'
])
end = time.time()

elapsed = end - start
print(f'執行時間: {elapsed:.2f} 秒')
print(f'預估 FPS: {1/elapsed:.2f}')
"
```

### 驗證 4：音質評分（客觀）

```python
# 使用 Whisper 進行詞錯誤率評估（需額外安裝）
from transformers import WhisperProcessor, WhisperForConditionalGeneration

processor = WhisperProcessor.from_pretrained("openai/whisper-small")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-small")

# 載入音訊
audio, sr = sf.read("hello.wav")
if sr != 16000:
    audio = audio * sr / 16000

# 轉文字
transcription = model.transcribe(audio)
print(f"識別文字: {transcription['text']}")
```

---

## 模型架構

### 組件參數分配

| 組件 | 參數數量 |
|------|----------|
| 音節/語調/聲線嵌入 | 16,704 |
| 文字編碼器 | 1,588,864 |
| 時長與停頓預測器 | 123,906 |
| 框架轉換器 A（韻律頭） | 795,971 |
| 框架轉換器 B | 1,985,984 |
| 源濾波器波形生成器 | 25,862 |
| **總計** | **4,537,291** |

### 訓練架構

- **模型類型**：Transformer 編碼器 + 源濾波器合成器
- **訓練步驟**：104,737
- **硬體**：單一 RTX 4090 GPU
- **訓練時間**：7.7 小時
- **損失函數**：多解析度頻譜損失 + 對抗性損失

---

## 執行參數說明

| 參數 | 預設值 | 說明 |
|------|--------|------|
| `--text` / `--text-file` | - | 輸入文字或檔案路徑 |
| `--voice` | `F2` | 聲線選擇（F2/M2） |
| `--speed` | `1.0` | 說話速率倍數 |
| `--pitch-shift` | `0` | 音高偏移（0.058 ≈ 半音） |
| `--pitch-range` | `1.0` | 音高變動幅度縮放 |

### 進階 Python API

```python
from tiny_voca.infer import speak_text

# 直接使用 Python API（自動分句）
speak_text(
    text="這是長文字測試。這是第二句。這是第三句。",
    checkpoint="tiny-voca/tiny-voca.pt",
    voice="F2",
    output="long_text.wav",
    speed=1.0
)
```

---

## 性能指標

### Open TTS Leaderboard 排名（2026 年 11 月 16 日）

| 聲線 | 排名 | 參數 | 平均 WER ↓ | UTMOS22 ↑ |
|------|------|------|------------|-----------|
| M2 | 8 | 4.5M | 0.733% | 4.34 |
| F2 | 13 | 4.5M | 0.773% | 4.43 |

> 註：M2 在英語語音合成中排名第 8，F2 排名第 13，均為 CPU 執行。

### 測試集表現

| 測試集 | 句子數 | WER (tiny-voca) | WER (錄音參考) |
|--------|--------|-----------------|----------------|
| 驗證集 | 8 | 0.6% | 0.6% |
| 測試集 | 8 | 0.9% | 0.9% |
| 新句子 | 16 | 0.0% | - |

---

## 已知限制

1. **語言支援**：僅支援英語，無語音複製功能
2. **聲線固定**：僅 F2 女聲與 M2 男聲兩種聲線
3. **音質**：語音清晰但略帶人工感
4. **語調固定**：相同文字永遠以相同方式朗讀，無韻律變化
5. **發音**：外文人名與特殊拼寫常被誤讀
6. **串流支援**：無串流推論能力
7. **訓練數據**：基於合成數據訓練，無法超越生成模型品質

---

## 參考資源

- **模型倉庫**: https://huggingface.co/n4ze3m/tiny-voca
- **原始碼**: https://github.com/n4ze3m/tiny-voca
- **語音轉換器**: https://github.com/n4ze3m/dizione
- **訓練數據**: https://huggingface.co/datasets/n4ze3m/tiny-voca
- **Open TTS Leaderboard**: https://huggingface.co/spaces/hf-audio/open_tts_leaderboard

---

## 引用

```bibtex
@software{nazeem2026tinyvoca,
  author = {Nazeem, Muhammed},
  title  = {tiny-voca: a 4.5M-parameter two-voice English text-to-speech model},
  year   = {2026},
  url    = {https://huggingface.co/n4ze3m/tiny-voca}
}
```
