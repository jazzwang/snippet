# Latent Scope

- Git Repo
  - https://github.com/enjalot/latent-scope  
- Document
  - https://enjalot.github.io/latent-scope/install-and-config
- PyPI
  - https://pypi.org/project/latentscope/
- Related Link
  - https://builders.mozilla.org/latent-scope/
  - https://youtu.be/rSM_tGNBs7M

## Installation

### 2025-09-04

- 測試環境：Windows 11 + Git Bash
- 想說應該有命令列工具，所以就用 `uv tool install latent-scop` 安裝。不過 3.13.2 版本會有找不到相依套件的問題，所以必須強制指定 3.12.7 的 Python 版本。
```bash
[09/04 14:43:07] uv tool install latentscope ## 失敗
[09/04 14:53:23] uv tool install --python 3.12.7 latentscope ## 成功
```
- 根據同事讀書會分享的步驟，下 `ls-serve` 指定資料目錄，就可以正常運作。
- 原本想要把 WebVTT-to-JSON 的結果直接餵進去當資料集，可是報錯。
- 範例資料集要從網路下載，因為抓得很慢，就直接中斷掉。

## Test

### 2025-09-05

- https://enjalot.github.io/latent-scope/your-first-scope
  - Sample CSV
    - https://storage.googleapis.com/fun-data/latent-scope/examples/dvs-survey/datavis-notunderstood.csv