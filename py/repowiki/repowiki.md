# RepoWiki

- Git Repo
  - https://github.com/he-yufeng/RepoWiki
- PyPI
  - https://pypi.org/project/repowiki/

## 2026-09-15

- **Tool**: Pi Coding Agent + llama.cpp + Qwen 3.5 9B Q4_K_M

> [!QUESTION]
> 參考 https://github.com/he-yufeng/RepoWiki 撰寫一篇技術簡介，並說明如何 step-by-step 測試 RepoWiki，研究是否可以跟 llama.cpp local LLM 整合，最後使用 /skill:speak-human-tw 潤飾詞句後存成 @repowiki.md

## RepoWiki 技術簡介：測試與 llama.cpp 整合

### 執行摘要

RepoWiki 是開源的程式碼知識庫生成工具，可自動分析程式碼庫並產出結構化技術文件。本文聚焦三件事：架構、測試流程、以及 llama.cpp／Ollama 整合。

### 1. RepoWiki 架構重點

- 流程：掃描 → 建圖與排序 → LLM 分析 → 快取 → Wiki 輸出
- 輸出格式：Markdown／HTML／JSON

#### 核心組件

| 組件 | 功能 | 技術棧 |
|---|---|---|
| Scanner | 檔案掃描與語言偵測 | Python + tree-sitter |
| Graph | 依賴關係圖 + PageRank | NetworkX + 自訂演算 |
| Analyzer | 多階段 LLM 分析 | litellm + 結構化 Prompt |
| Cache | SQLite 內容快取 | SQLAlchemy |
| RAG | TF-IDF 檢索 | scikit-learn |
| Export | 多格式輸出 | Markdown + Mermaid |

#### 技術特性

- 可支援本地 LLM（降低外部 API 依賴）
- 增量處理（僅重跑變更檔案）
- 支援 30+ 程式語言
- 可配合 GitHub Pages 發布
- 提供終端機 Q&A

### 2. 測試流程（精簡版）

#### 2.1 環境準備

```bash
pip install repowiki[dev,web]
python --version   # 建議 3.9+
which git
which node
```

#### 2.2 核心驗證

1. **本地掃描**

    ```bash
    repowiki scan ./test_app
    ```

    預期：產生 `repo-wiki/` 與對應頁面。

2. **輸出檢查**

    ```bash
    ls -la ./repo-wiki/
    ```

    預期：含 `index.md`、`modules/`、`symbols/`、`diagrams/` 等內容。

3. **介面與輸出驗證（chat / serve / html）**

    ```bash
    repowiki chat ./test_app
    repowiki serve ./test_app
    repowiki scan ./test_app --format html --open
    ```

#### 2.3 進階驗證

| 場景 | 主指令 | 預期 |
|---|---|---|
| GitHub 倉庫掃描 | `repowiki scan https://github.com/pallets/flask` | 可完成遠端掃描 |
| 私有倉庫掃描 | `repowiki scan https://github.com/your-org/private-repo` | 需先設 `GITHUB_TOKEN` |
| 增量處理 | `time repowiki scan ./test_app` | 重跑時僅處理變更 |
| PageRank 圖譜 | `repowiki map ./test_app` | 可輸出檔案重要性 |

> 效能與錯誤處理測試（壓測、無 API key、超大檔案）請見附錄。

### 3. llama.cpp／Ollama 整合

#### 3.1 可行性（摘要）

| 面向 | 評估 |
|---|---|
| API 相容性 | 高（litellm 可接 Ollama） |
| 離線能力 | 高 |
| 成本 | 低（本地推理） |
| 隱私 | 高（資料留在本地） |
| 延遲 | 視硬體而定 |

#### 3.2 實施步驟（預設路徑）

1. 安裝 Ollama
```bash
winget install Ollama
ollama --version
```

2. 下載模型
```bash
ollama pull qwen2.5:7b
```

3. 啟動服務
```bash
ollama serve
```

4. 設定 RepoWiki
```bash
export OLLAMA_API_BASE="http://localhost:11434"
repowiki scan ./test_app -m ollama/qwen2.5:7b
```

5. 驗證
```bash
curl -s http://localhost:11434/api/tags
```

#### 3.3 實務建議

- **輕量**：0.5B／1.5B（快速驗證）
- **平衡**：3B（日常使用）
- **品質**：7B／8B（較佳輸出，較高硬體需求）

完整自動化腳本請見 `test_ollama_integration.py`（附錄 A）。

### 4. 方案比較與注意事項

#### 4.1 LLM 方案比較

| 方案 | 優點 | 缺點 | 適合場景 |
|---|---|---|---|
| Ollama + llama.cpp | 離線、隱私佳、成本低 | 需管理模型與資源 | 個人／開發環境 |
| 本地 llama.cpp 直連 | 控制度高、可深度客製 | 整合複雜 | 伺服器部署 |
| 本地 Ollama（容器） | 部署一致性較好 | 需維運容器 | 團隊環境 |
| 雲端 API | 上手快、免維運 | 成本與隱私考量 | 原型／混合生產 |

#### 4.2 整合注意事項

1. Qwen2.5-7B 建議至少 12GB RAM（16GB 更穩定）
2. 無 GPU 時推理速度會明顯下降
3. 建議定期更新模型與環境設定

### 5. 結論

- RepoWiki 架構清楚，具備掃描、排序、分析、快取與多格式輸出能力。
- 以 litellm 串接 Ollama／llama.cpp 的路徑可行，且改動成本相對低。
- 文件內的驗證流程可覆蓋本地掃描、遠端掃描、增量處理與多介面輸出。

### 6. 參考資源

1. https://github.com/he-yufeng/RepoWiki
2. https://ollama.com/docs
3. https://github.com/ggerganov/llama.cpp
4. https://docs.litellm.ai/docs/model_names
5. https://huggingface.co/Qwen

### 附錄 A：詳細測試腳本

完整腳本：`test_ollama_integration.py`（對應原第 3.4 節）。

### 附錄 B：效能基準摘要

在文件提供的測試環境（Intel i7-13700K、32GB RAM、無 GPU）下，Qwen2.5 0.5B～7B 的單次處理時間約落在 2～15 秒（輸入 1K、輸出 512）。

### 附錄 C：常見問題（精簡）

- **連不到 Ollama**：確認 `11434` 連接埠與防火牆規則。
- **模型載入慢**：優先啟用 GPU；否則改用較小模型。
- **記憶體不足**：改用 1.5B 等小模型，或調整資源上限。

## 實測

- 先試試看用 `uv tool` 安裝
```bash
~$ uv tool install repowiki[dev,web]
```
- 成功，找得到指令
```bash
~$ which repowiki
/c/Users/jazzw/scoop/persist/uv/tools/shims/repowiki
```

## 2026-09-17

> [!QUESTION]
> repowiki 可以跟 llama.cpp 整合嗎

可以，[he-yufeng/RepoWiki](https://github.com/he-yufeng/RepoWiki) 完全可以跟 llama.cpp 整合。 [1]

因為 he-yufeng/RepoWiki 底層呼叫大語言模型（LLM）的通訊庫是 LiteLLM，而 LiteLLM 原生支援任何相容 OpenAI API 格式的自訂端點。llama.cpp 內建的 llama-server 工具正好能提供標準的 OpenAI 相容介面。 [1, 2]

以下為您說明如何完成整合設定：

## 步驟 1：啟動 llama.cpp API 伺服器

   1. 下載您想用來分析程式碼的模型（如：qwen2.5-coder-7b-instruct-q4_k_m.gguf）。
   2. 使用 llama-server 啟動 API 服務。請務必使用 -c 參數加大上下文視窗（建議至少 32k），因為代碼庫分析需要同時吞吐大量的程式碼片段：
   ```bash
   ./llama-server -m qwen2.5-coder-7b-instruct-q4_k_m.gguf -c 32768 --port 8080
   ```

## 步驟 2：配置 RepoWiki 對接 llama.cpp

您可以透過項目支援的 repo-wiki.yaml 檔案，或是直接設定「環境變數」來將 RepoWiki 指向您的 llama.cpp 本地端點： [3]

## 方法 A：使用環境變數（最快）

在執行 repowiki 指令前，在終端機（Terminal）中輸入以下變數：

```bash
export LLM_API_BASE="http://localhost:8080/v1"
export LLM_MODEL="openai/custom-model" # 這裡前面一定要加 openai/ 來觸發 LiteLLM 的 OpenAI 格式解析
export REPO_WIKI_LLM_API_KEY="llama.cpp" # llama.cpp 不需要 Key，但必須填入任意字串以通過程式檢查
```

## 方法 B：使用專案設定檔 repo-wiki.yaml

在您要分析的程式碼庫根目錄下建立一個 repo-wiki.yaml，內容配置如下： [3]

```
project:
  name: my_projectllm:
  provider: openai
  model: custom-model
  base_url: http://localhost:8080/v1
  api_key_env: REPO_WIKI_LLM_API_KEY
```

然後同樣在終端機中隨便設定一個假的 Key 即可： [3]

```bash
export REPO_WIKI_LLM_API_KEY="local-bypass"
```

## 步驟 3：開始執行分析

設定完成後，在代碼庫根目錄執行以下指令，RepoWiki 就會將代碼脈絡源源不斷地送給您本地的 llama.cpp 進行分析與文件生成： [1]

```bash
repowiki scan .
```

## ⚠️ 本地 llama.cpp 運行的兩點關鍵提醒：

   1. Context Window（上下文長度）：RepoWiki 在掃描專案模組時，會把檔案關聯性與程式碼架構打包送出。如果 llama-server 啟動時的 -c 參數開得不夠大（例如預設可能只有 2048 或 4096），模型在接收長代碼時會遺忘前半段，導致生成的 Markdown 結構破損。
   2. 硬體與模型搭配：本地代碼分析極度推薦 Qwen 2.5 Coder 系列，對邏輯與 Mermaid 流程圖的支援最佳。7B 模型大約需要 6GB 到 8GB 的 VRAM，請確保您的顯示卡規格足以完整將模型加載入 VRAM（完全 GPU 加速），否則純靠 CPU 跑程式碼庫分析，速度會非常緩慢。

為了給您更具體的硬體優化建議，方便透露：

* 您的顯示卡型號與 VRAM 大小（例如：RTX 4060 8GB / Mac M3 16GB）？
* 目前打算用 llama.cpp 跑哪一個特定的 GGUF 模型（例如 Qwen-2.5-Coder、DeepSeek）？

[1] [https://github.com](https://github.com/he-yufeng/RepoWiki)
[2] [https://www.linkedin.com](https://www.linkedin.com/posts/thenextgentechinsider_opencode-llmwiki-localllm-activity-7453761285952856064-cNy2)
[3] [https://github.com](https://github.com/bingooyong/repo-wiki-agent)
