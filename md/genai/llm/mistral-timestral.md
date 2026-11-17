# Mistral Timestral 時間序列基礎模型

- Git Repo
  - https://github.com/mistralai/timestral 
- News/Blog
  - https://mistral.ai/news/timestral/
- Paper
  - https://arxiv.org/html/2610.37585v1

> [!NOTE]
> 根據 "https://github.com/mistralai/timestral https://mistral.ai/news/timestral/" 內容，用繁體中文（台灣技術用詞）撰寫一篇技術報告，含 step-by-step 安裝、測試、驗證步驟，存成 "md/genai/llm/mistral-timestral.md" .

## Mistral Timestral 時間序列基礎模型技術報告

### 概述

**Timestral** 是 Mistral AI 推出的第一個時間序列基礎模型（Time-Series Foundation Model）系列，專為多變量機率預測設計。該模型系列支援過去變數（past-only covariates）和已知未來變數（known-future covariates）的條件化輸入，可在 CPU 或 GPU 上高效運行。

#### 主要特點

- **多變量聯合預測**：同一序列的各個變量（variates）共同預測，捕捉變量間的相依關係
- **機率預測**：每個時間步輸出 21 個不交疊的分位數（quantiles）
- **長上下文**：支援高達 32,768 個時間步的上下文
- **無需 GPU**：推論可在標準 CPU 伺服器上運行
- **四大規模**：5M、28M、123M、209M 參數，均位於準確率與模型大小的 Pareto frontier 上

#### 基準測試表現

在三大公共預測基準測試中，Timestral-209M 在預訓練和零樣本（zero-shot）模型中均排名第一：

| 基準測試 | 表現 |
|---------|------|
| **GIFT-Eval** | 97 個配置中排名第一 |
| **TIME** | 98 個任務中排名第一 |
| **fev-bench** | 100 個任務中排名第一 |

### 系統要求

- **Python**：>= 3.10
- **PyTorch**：>= 2.4
- **硬體**：CPU 或 GPU（推論無需 GPU）
- **記憶體**：根據模型規模（5M: 21MB, 28M: 111MB, 123M: 490MB, 209M: 837MB）

### Step-by-Step 安裝步驟

#### 方法一：直接 pip 安裝

```bash
pip install git+https://github.com/mistralai/timestral.git
```

此方法會自動下載依賴套件，需要網路連線。

#### 方法二：使用 uv 安裝（推薦）

```bash
## 克隆儲存庫
git clone https://github.com/mistralai/timestral.git
cd timestral

## 使用 uv 同步依賴（使用 uv.lock 中固定版本）
uv sync --frozen

## 啟動虛擬環境
source .venv/bin/activate
```

**uv 方法優點**：
- 使用 `uv.lock` 中固定的套件版本，確保可重複性
- 安裝速度更快
- 適合持續整合（CI）環境

### 模型權重載入

#### 可用模型版本

| 模型 | Hugging Face 儲存庫 | 權重大小（fp32） |
|------|-------------------|----------------|
| Timestral-5M | [`mistralai/Timestral-5M`](https://huggingface.co/mistralai/Timestral-5M) | 21 MB |
| Timestral-28M | [`mistralai/Timestral-28M`](https://huggingface.co/mistralai/Timestral-28M) | 111 MB |
| Timestral-123M | [`mistralai/Timestral-123M`](https://huggingface.co/mistralai/Timestral-123M) | 490 MB |
| Timestral-209M | [`mistralai/Timestral-209M`](https://huggingface.co/mistralai/Timestral-209M) | 837 MB |

權重以 `model.safetensors` 格式存在 Hugging Face Hub 上，`from_pretrained` 會自動下載 `config.json` 和 `model.safetensors` 至 Hub 快取目錄。

### Step-by-Step 測試與驗證

#### 1. 基本推論測試

```python
import numpy as np
from timestral import TimestralForecaster

## 載入模型（預設使用 CPU，可指定 device="cuda" 使用 GPU）
forecaster = TimestralForecaster.from_pretrained("mistralai/Timestral-209M")

## 生成測試上下文：(序列數, 變量數, 時間步)
## 使用累積和產生模擬時間序列，NaN 表示缺失值
context = np.random.randn(2, 1, 2000).cumsum(-1)

## 執行預測，prediction_length=96 表示預測未來 96 個時間步
forecast = forecaster.forecast(context, prediction_length=96)

## 驗證輸出形狀
assert forecast.quantiles.shape == (2, 1, 96, 21)  # (序列數, 變量數, 預測範圍, 分位數)

## 驗證分位數水準
expected_levels = [0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99]
assert list(forecast.quantile_levels) == expected_levels

## 驗證中位數輸出
assert forecast.median.shape == (2, 1, 96)  # 50% 分位數

## 驗證特定分位數輸出
assert forecast.quantile(0.9).shape == (2, 1, 96)  # 90% 分位數
```

**驗證檢查點**：
- ✅ 輸出形狀正確：`(B, V, T, 21)`
- ✅ 分位數水準正確：13 個標準分位數
- ✅ 中位數計算正確

#### 2. 包含過去變數（past covariates）的測試

```python
from timestral import TimestralForecaster

forecaster = TimestralForecaster.from_pretrained("mistralai/Timestral-209M")

## 生成上下文：(序列數, 變量數, 時間步)
context = np.random.randn(2, 1, 2000).cumsum(-1)

## 生成過去變數：(序列數, 變量數, 時間步)，僅在上下文中已知
past_covariates = np.random.randn(2, 1, 2000).cumsum(-1)

## 執行預測
forecast = forecaster.forecast(
    context=context,
    prediction_length=96,
    past_covariates=past_covariates
)

## 驗證
assert forecast.quantiles.shape == (2, 1, 96, 21)
print(f"過去變數預測驗證通過，輸出形狀：{forecast.quantiles.shape}")
```

**驗證檢查點**：
- ✅ 過去變數僅在上下文中可用（不滲漏未來資訊）
- ✅ 輸出形狀正確

#### 3. 包含已知未來變數（known-future covariates）的測試

```python
from timestral import TimestralForecaster

forecaster = TimestralForecaster.from_pretrained("mistralai/Timestral-209M")

## 生成上下文
context = np.random.randn(2, 1, 2000).cumsum(-1)

## 生成已知未來變數：(序列數, 變量數, 上下文 + 預測範圍)
known_covariates = np.random.randn(2, 1, 2000 + 96).cumsum(-1)

## 執行預測
forecast = forecaster.forecast(
    context=context,
    prediction_length=96,
    known_covariates=known_covariates
)

## 驗證
assert forecast.quantiles.shape == (2, 1, 96, 21)
print(f"已知未來變數預測驗證通過，輸出形狀：{forecast.quantiles.shape}")
```

**驗證檢查點**：
- ✅ 已知未來變數在整個預測範圍內可用
- ✅ 輸出形狀正確

#### 4. 包含分類變數（categorical covariates）的測試

```python
from timestral import TimestralForecaster

forecaster = TimestralForecaster.from_pretrained("mistralai/Timestral-209M")

## 生成上下文
context = np.random.randn(2, 1, 2000).cumsum(-1)

## 生成分類變數代碼（例如：星期幾、機器狀態）
## NaN 表示缺失值，填充位置使用 NaN
categorical_past = np.random.choice([0, 1, 2, np.nan], size=(2, 1, 2000))
categorical_known = np.random.choice([0, 1, 2, np.nan], size=(2, 1, 2000 + 96))

## 執行預測
forecast = forecaster.forecast(
    context=context,
    prediction_length=96,
    categorical_past_covariates=categorical_past,
    categorical_known_covariates=categorical_known
)

## 驗證
assert forecast.quantiles.shape == (2, 1, 96, 21)
print(f"分類變數預測驗證通過，輸出形狀：{forecast.quantiles.shape}")
```

**分類變數編碼說明**：
- 分類變數以數值代碼形式傳遞（例如 `pandas.factorize` 的結果）
- NaN 表示缺失值或填充位置
- 單一變量目標：每個分類行針對序列進行目標編碼（target-encoded）
  - 類別 `c` 編碼為：`(mean + sum_c) / (1 + count_c)`
  - 缺失值形成獨立類別
  - 上下文中未出現的類別映射為序列平均值
- 多變量目標：直接使用原始代碼

#### 5. 缺失值處理測試

```python
from timestral import TimestralForecaster

forecaster = TimestralForecaster.from_pretrained("mistralai/Timestral-209M")

## 生成上下文，NaN 表示缺失值
context_with_missing = np.random.randn(2, 1, 2000).cumsum(-1)
context_with_missing[0, 0, 500:600] = np.nan  # 引入缺失區間

## 生成觀察掩碼（與上下文相同形狀，False = 缺失）
observation_mask = ~np.isnan(context_with_missing)

## 執行預測
forecast = forecaster.forecast(
    context=context_with_missing,
    observation_mask=observation_mask,
    prediction_length=96
)

## 驗證
assert forecast.quantiles.shape == (2, 1, 96, 21)
print(f"缺失值處理測試通過，輸出形狀：{forecast.quantiles.shape}")
```

**驗證檢查點**：
- ✅ NaN 值被正確識別為缺失
- ✅ 觀察掩碼正確處理
- ✅ 輸出形狀正確

#### 6. 從本地目錄載入模型

```python
from timestral import TimestralForecaster

## 方法一：指定 Hugging Face 儲存庫 ID
forecaster = TimestralForecaster.from_pretrained("mistralai/Timestral-209M")

## 方法二：指定本地目錄（需包含 config.json 和 model.safetensors）
local_path = "/path/to/local/timestral/model"
forecaster = TimestralForecaster.from_pretrained(local_path)

## 方法三：使用 revision 指定分支、標籤或提交
forecaster = TimestralForecaster.from_pretrained(
    "mistralai/Timestral-209M",
    revision="main"  # 或指定 tag、commit hash
)

## 方法四：使用 offline 模式（需先下載到快取）
import os
os.environ["HF_HUB_OFFLINE"] = "1"
forecaster = TimestralForecaster.from_pretrained("mistralai/Timestral-209M", local_files_only=True)
```

**載入選項參數**：
- `revision`：固定分支、標籤或提交
- `cache_dir`：指定快取目錄
- `token`：Hugging Face 認證令牌
- `local_files_only=True`：僅使用快取中的檔案（不需網路）

#### 7. 完整整合測試腳本

```python
import numpy as np
import torch
from timestral import TimestralForecaster

def test_timestral():
    """完整的 Timestral 測試與驗證腳本"""
    
    print("=" * 60)
    print("Timestral 測試腳本")
    print("=" * 60)
    
    # 載入模型
    print("\n[1/7] 載入模型...")
    forecaster = TimestralForecaster.from_pretrained(
        "mistralai/Timestral-209M",
        device="cuda" if torch.cuda.is_available() else "cpu"
    )
    print(f"  ✓ 模型載入完成：{forecaster}")
    
    # 測試 1：基本預測
    print("\n[2/7] 測試基本預測功能...")
    context = np.random.randn(2, 1, 2000).cumsum(-1)
    forecast = forecaster.forecast(context, prediction_length=96)
    assert forecast.quantiles.shape == (2, 1, 96, 21)
    print(f"  ✓ 基本預測通過，輸出形狀：{forecast.quantiles.shape}")
    
    # 測試 2：過去變數
    print("\n[3/7] 測試過去變數條件化...")
    past_cov = np.random.randn(2, 1, 2000).cumsum(-1)
    forecast = forecaster.forecast(context, prediction_length=96, past_covariates=past_cov)
    assert forecast.quantiles.shape == (2, 1, 96, 21)
    print(f"  ✓ 過去變數測試通過")
    
    # 測試 3：已知未來變數
    print("\n[4/7] 測試已知未來變數條件化...")
    known_cov = np.random.randn(2, 1, 2000 + 96).cumsum(-1)
    forecast = forecaster.forecast(context, prediction_length=96, known_covariates=known_cov)
    assert forecast.quantiles.shape == (2, 1, 96, 21)
    print(f"  ✓ 已知未來變數測試通過")
    
    # 測試 4：分類變數
    print("\n[5/7] 測試分類變數條件化...")
    cat_past = np.random.choice([0, 1, 2, np.nan], size=(2, 1, 2000))
    cat_known = np.random.choice([0, 1, 2, np.nan], size=(2, 1, 2000 + 96))
    forecast = forecaster.forecast(
        context,
        prediction_length=96,
        categorical_past_covariates=cat_past,
        categorical_known_covariates=cat_known
    )
    assert forecast.quantiles.shape == (2, 1, 96, 21)
    print(f"  ✓ 分類變數測試通過")
    
    # 測試 5：缺失值處理
    print("\n[6/7] 測試缺失值處理...")
    context_missing = np.random.randn(2, 1, 2000).cumsum(-1)
    context_missing[0, 0, 500:600] = np.nan
    mask = ~np.isnan(context_missing)
    forecast = forecaster.forecast(context_missing, observation_mask=mask, prediction_length=96)
    assert forecast.quantiles.shape == (2, 1, 96, 21)
    print(f"  ✓ 缺失值處理測試通過")
    
    # 測試 6：中位數計算
    print("\n[7/7] 測試中位數計算...")
    assert forecast.median.shape == (2, 1, 96)
    assert forecast.quantile(0.9).shape == (2, 1, 96)
    print(f"  ✓ 中位數和分位數計算測試通過")
    
    print("\n" + "=" * 60)
    print("所有測試通過！✓")
    print("=" * 60)

if __name__ == "__main__":
    test_timestral()
```

### 性能參考

在標準伺服器 CPU（8 個線程）上，從三週（15 分鐘間隔）的歷史資料預測未來一天：

| 模型 | 參數量 | 推論時間 |
|------|--------|---------|
| Timestral-5M | 5M | 17 ms |
| Timestral-28M | 28M | 64 ms |
| Timestral-123M | 123M | 83 ms |
| Timestral-209M | 209M | 113 ms |

**速度對比**：
- 28M 模型是 209M 模型的 3.6 倍速度
- 123M 模型在 209M 模型的 75% 時間內達到 99.8% 的準確率

### 技術架構概述

Timestral 採用以下核心技術：

1. **Decoupled Horizon Forecasting (DHF)**：因果編碼，預測從獨立的預測 token 生成，完整歷史保留在序列中

2. **Covariate-aware attention**：
   - 每個輸入序列分配角色：目標變量、過去變數或已知未來變數
   - 資訊僅從變數流向目標，不滲漏未來目標值

3. **Synthetic-first data**：主要使用合成數據訓練，包含趨勢、季節性和多樣化噪聲模式

4. **Two-stage training**：
   - 階段一：在純合成數據上預訓練，上下文長度 8192
   - 階段二：在混合真實/合成數據上後訓練，上下文長度 32768

5. **量化輸出**：21 個分位數的 pinball loss 作為訓練目標（CRPS 的離散近似）

### 參考資源

- **官方儲存庫**：https://github.com/mistralai/timestral
- **官方部落格**：https://mistral.ai/news/timestral/
- **Hugging Face 模型集合**：https://huggingface.co/collections/mistralai/timestral
- **技術報告**：https://arxiv.org/abs/2610.37585
- **基準測試**：
  - GIFT-Eval：https://github.com/SalesforceAIResearch/gift-eval
  - TIME：https://github.com/zqiao11/TIME
  - fev-bench：https://github.com/autogluon/fev

### 授權說明

- **程式碼**：Apache License 2.0
- **模型權重**：Modified MIT License（每個模型儲存庫有獨立授權文件）

*作者：Mistral AI*
