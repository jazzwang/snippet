# NVIDIA SkillEvaluator 技術報告

## 概述

SkillEvaluator 是 NVIDIA 開發的開源多層級框架，用於評估 AI 代理（AI Agent）工件的品質與效能，從 AI Agent 技能（Agent Skills）開始。該工具提供確定性品質閘道、語意重疊檢測、合成評估資料集生成，以及即時代理評估功能。

SkillEvaluator 是 [NVIDIA 驗證技能管線](https://docs.nvidia.com/skills/) 的一部分，符合 [Agent Skills 規格](https://agentskills.io/)。Tier 1 整合 [SkillSpector](https://github.com/NVIDIA/SkillSpector) 進行專門的安全掃描。

- **專案來源**: [GitHub](https://github.com/NVIDIA/SkillEvaluator)
- **官方文件**: [docs.nvidia.com/skills/skillevaluator](https://docs.nvidia.com/skills/skillevaluator/)
- **授權**: Apache 2.0
- **Python 版本**: 3.12 | 3.13 | 3.14
- **支援層級**: Experimental（實驗性，社區支持）

---

## 三層級架構

SkillEvaluator 採用三層級驗證架構，每一層獨立運作：

| 層級 | 功能 | 主要命令 | 需求 |
|------|------|----------|------|
| **Tier 1: 驗證** | 檢查技能是否安全、格式正確且與驗證器相容 | `tier1`, `quality-check`, `security-scan` | 外部掃描器（Semgrep, SkillSpector, Gitleaks）；LLM 檢查需要提供者金鑰 |
| **Tier 2: 去重** | 檢測指導內容是否重複或重疊 | `context-optimization-check`, `similarity-check` | 嵌入模型提供者；需要聊天式 LLM |
| **Tier 3: 即時評估** | 技能是否實際幫助代理 | `create-eval-dataset`, `tier3 evaluate`, `compare` | LLM 提供者金鑰；代理 CLI；Docker 或本地沙盒環境 |

---

## 安裝步驟

### 前置需求

1. **Git** - 用於程式庫管理
2. **UV 套件管理員** - 現代 Python 套件工具
   - 安裝命令：[https://docs.astral.sh/uv/getting-started/installation](https://docs.astral.sh/uv/getting-started/installation)
3. **Python 3.12/3.13/3.14**

### 方式一：快速安裝（推薦）

使用 UV 進行專案本地安裝：

```bash
# 克隆專案
git clone --depth 1 https://github.com/NVIDIA/SkillEvaluator.git
cd SkillEvaluator

# 使用 UV 運行（自動處理 Python 和依賴）
uv run --python 3.13 skillevaluator quality-check \
  src/skillevaluator/tier3/reference_skills/text-analyzer
```

### 方式二：pip 安裝

```bash
# 安裝主套件
pip install skillevaluator

# 或使用 uv tool 安裝（推薦）
uv tool install skillevaluator
```

### 方式三：包含 LLM 支援的安裝

```bash
# 安裝包含 LLM 支援的額外組件
pip install skillevaluator[llm]

# 或使用 uv
uv tool install skillevaluator[llm]
```

### 方式四：完整套件安裝（所有 Tier）

```bash
# 安裝完整套件（包含所有 Tier 需求）
pip install skillevaluator[all]
# 或
uv tool install skillevaluator[all]
```

### 系統工具（安全掃描需求）

完整安全掃描需要以下外部工具：

| 工具 | 用途 | 安裝方式 |
|------|------|----------|
| **Semgrep** | 程式碼靜態分析 | `pip install semgrep` 或從 [Semgrep](https://semgrep.dev/) 下載 |
| **SkillSpector** | AI 技能安全掃描 | 從 [NVIDIA SkillSpector](https://github.com/NVIDIA/SkillSpector) 安裝 |
| **Gitleaks** | 敏感資訊掃描 | `brew install gitleaks` (macOS) 或從 [Gitleaks](https://gitleaks.io/) 下載 |

### LLM 提供者設定

對於需要 LLM 的 Tier 1、Tier 2 和 Tier 3：

```bash
# NVIDIA Build（免費原型開發）
export SKILL_EVAL_LLM_PROVIDER=nv_build
export NVIDIA_API_KEY='nvapi-...'

# 或其他提供者（OpenAI, Anthropic 等）
export SKILL_EVAL_LLM_PROVIDER=openai
export SKILL_EVAL_API_KEY='sk-...'
```

---

## 測試步驟

### 測試環境準備

#### 環境 1：無 LLM 的基礎測試

```bash
# 克隆專案
git clone --depth 1 https://github.com/NVIDIA/SkillEvaluator.git
cd SkillEvaluator

# 運行基礎品質檢查（不需 API 金鑰）
uv run --python 3.13 skillevaluator quality-check \
  src/skillevaluator/tier3/reference_skills/text-analyzer \
  -r cli -r json -o reports/first-quality
```

**預期結果**：
- 輸出品質分數（例：86.2/100，等級 B）
- 產生 `reports/first-quality/skillevaluator-quality.json`
- 預設通過閾值：70 分

#### 環境 2：使用 NVIDIA Build 進行 LLM 評估

```bash
# 設定 NVIDIA Build 提供者
export SKILL_EVAL_LLM_PROVIDER=nv_build
export NVIDIA_API_KEY='nvapi-...'

# 運行規範評估
uv run --python 3.13 --extra llm skillevaluator rubric-eval \
  src/skillevaluator/tier3/reference_skills/text-analyzer \
  -r cli -r json -o reports/first-build
```

**預期結果**：
- 模型提供規範分數和反饋
- 產生 `reports/first-build/skillevaluator-rubric.json`
- 即使評分完成也可能未達閾值

### 分層測試命令

#### Tier 1：驗證測試

```bash
# 完整 Tier 1 驗證
uv run skillevaluator tier1 ./my-skill --no-llm

# 僅執行確定性檢查（不需 LLM）
uv run skillevaluator quality-check ./my-skill

# 僅執行安全掃描
uv run skillevaluator security-scan ./my-skill

# 僅執行 PII 掃描
uv run skillevaluator pii-scan ./my-skill

# 僅執行程式碼檢查
uv run skillevaluator lint-scripts ./my-skill

# 執行規範評估（需 LLM）
uv run skillevaluator rubric-eval ./my-skill
```

#### Tier 2：去重測試

```bash
# 語意去重檢查（需嵌入模型）
uv run --extra tier2 skillevaluator tier2 ./my-skill

# 上下文最佳化檢查（需聊天式 LLM）
uv run --extra tier2 skillevaluator context-optimization-check ./my-skill

# 使用技能目錄進行跨技能比較
uv run --extra tier2 skillevaluator tier2 ./my-skill \
  --catalog ./skill-catalog.json
```

#### Tier 3：即時評估測試

```bash
# 創建評估資料集（需 LLM）
uv run --extra tier3 skillevaluator tier3 create-eval-dataset \
  ./my-skill --full --prompt eval-guidance.md --force

# 執行 Tier 3 評估（需代理和沙盒）
uv run --extra tier3 skillevaluator tier3 evaluate ./my-skill

# 比較有/無技能的效能差異
uv run --extra tier3 skillevaluator tier3 compare ./my-skill
```

### 完整管線測試

```bash
# 執行所有三層級
uv run --python 3.13 --extra all skillevaluator doctor --env-mode docker
uv run --python 3.13 --extra all skillevaluator validate ./my-skill

# 僅執行 Tier 1 和 Tier 2（跳過即時評估）
uv run --python 3.13 --extra all skillevaluator validate ./my-skill --tiers 1,2

# 僅執行 Tier 1（靜態檢查）
uv run --python 3.13 skillevaluator validate ./my-skill --tiers 1

# 禁用自動駕駛（需現有評估資料）
uv run --extra tier3 skillevaluator tier3 evaluate ./my-skill --no-autopilot
```

---

## 驗證步驟

### 驗證檢查清單

#### 1. 安裝驗證

```bash
# 檢查套件是否安裝
skillevaluator --version

# 檢查可用命令
skillevaluator --help
```

**驗證標準**：
- [ ] `skillevaluator --version` 顯示版本資訊
- [ ] `skillevaluator --help` 列出所有命令
- [ ] 無錯誤訊息

#### 2. 基礎功能驗證

```bash
# 使用參考技能進行測試
uv run --python 3.13 skillevaluator quality-check \
  src/skillevaluator/tier3/reference_skills/text-analyzer \
  -r cli -r json -o reports/verification
```

**驗證標準**：
- [ ] 命令成功執行並返回分數
- [ ] 產生 JSON 輸出檔案
- [ ] 分數符合預期（80-90 分範圍為正常）

#### 3. Tier 1 驗證

```bash
# 執行完整 Tier 1 驗證
uv run skillevaluator tier1 ./my-skill

# 檢查掃描器可用性
uv run skillevaluator security-scan --check-scanners
```

**驗證標準**：
- [ ] Schema 驗證通過
- [ ] 安全掃描完成（SkillSpector, Gitleaks）
- [ ] 無 PII（個人敏感資訊）
- [ ] 程式碼符合規範
- [ ] 若使用 LLM 評分，LLM 檢查完成

#### 4. Tier 2 驗證

```bash
# 執行語意去重檢查
uv run --extra tier2 skillevaluator tier2 ./my-skill

# 檢查嵌入模型可用性
uv run skillevaluator similarity-check --check-embeddings
```

**驗證標準**：
- [ ] 嵌入模型成功加載
- [ ] 無內部重複內容
- [ ] 無跨技能重疊（使用 `--catalog` 時）

#### 5. Tier 3 驗證

```bash
# 創建評估資料集
uv run --extra tier3 skillevaluator tier3 create-eval-dataset \
  ./my-skill --full --prompt eval-guidance.md

# 執行評估
uv run --extra tier3 skillevaluator tier3 evaluate ./my-skill
```

**驗證標準**：
- [ ] 評估資料集成功創建
- [ ] 代理成功執行任務
- [ ] 沙盒環境運作正常
- [ ] 效能提升指標可測量（Skill Lift）

#### 6. 報告生成驗證

```bash
# 生成 CLI 報告
uv run skillevaluator validate ./my-skill -r cli

# 生成 JSON 報告
uv run skillevaluator validate ./my-skill -r json

# 生成 HTML 報告
uv run skillevaluator validate ./my-skill -r html

# 生成 Markdown 報告
uv run skillevaluator validate ./my-skill -r md
```

**驗證標準**：
- [ ] CLI 報告格式正確
- [ ] JSON 報告符合 Schema
- [ ] HTML 報告可視化完整
- [ ] Markdown 報告可讀性良好

### 報告內容驗證

#### 報告包含的指標

| 指標 | 說明 | 驗證方式 |
|------|------|----------|
| **Security** | 安全性分數 | 檢查報告中的安全評分 |
| **Correctness** | 正確性分數 | 檢查正確性指標 |
| **Discoverability** | 可發現性分數 | 檢查可發現性指標 |
| **Effectiveness** | 有效性分數 | 檢查有效性指標 |
| **Efficiency** | 效率分數 | 檢查效率指標 |
| **Skill Lift** | 技能提升值 | 計算有/無技能差異 |
| **pass@k** | 多輪次可靠性 | 檢查 pass@k 指標 |

#### 報告檔案驗證

```bash
# 查看報告內容
cat reports/verification/skillevaluator-quality.json

# 驗證 JSON 結構
python -c "import json; json.load(open('reports/verification/skillevaluator-quality.json'))"

# 檢查報告完整性
skillevaluator reports inspect reports/verification/
```

---

## 輸出與報告

### 輸出格式

SkillEvaluator 支援多種輸出格式：

| 格式 | 用途 | 命令參數 |
|------|------|----------|
| **CLI** | 終端機即時輸出 | `-r cli` |
| **JSON** | 機器可讀取 | `-r json` |
| **HTML** | 網頁報告 | `-r html` |
| **Markdown** | 文件報告 | `-r md` |

### 報告目錄結構

```
reports/
├── first-quality/
│   └── skillevaluator-quality.json
├── first-build/
│   └── skillevaluator-rubric.json
└── my-skill/
    ├── skillevaluator-quality.json
    ├── skillevaluator-rubric.json
    ├── skillevaluator-dedup.json
    └── skillevaluator-eval.json
```

### 報告內容範例

```json
{
  "quality_score": 86.2,
  "grade": "B",
  "security_score": 92.0,
  "findings": [
    {
      "type": "info",
      "message": "Skill documentation is well-structured",
      "severity": "info"
    }
  ],
  "pass_threshold": 70,
  "passed": true
}
```

---

## CI/CD 整合

### GitHub Actions

```yaml
name: SkillEvaluator
on: [pull_request]
jobs:
  skill-eval:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup uv
        uses: astral-sh/setup-uv@v3
      
      - name: Run SkillEvaluator
        run: |
          uv run skillevaluator validate ./my-skill
```

### GitLab CI

```yaml
skill-evaluator:
  image: python:3.13
  stage: test
  script:
    - pip install skillevaluator
    - skillevaluator validate ./my-skill
```

---

## 故障排除

### 常見問題

#### 問題 1：掃描器未找到

```
Error: SkillSpector not found
```

**解決方案**：
```bash
# 安裝 SkillSpector
pip install skill-spector
# 或
uv tool install skill-spector

# 或使用 Docker
docker run --rm nvidia/skillspector
```

#### 問題 2：LLM 提供者未設定

```
Error: LLM provider not configured
```

**解決方案**：
```bash
# 設定 NVIDIA Build
export SKILL_EVAL_LLM_PROVIDER=nv_build
export NVIDIA_API_KEY='nvapi-...'

# 或使用環境變數檔案
echo "export SKILL_EVAL_LLM_PROVIDER=nv_build" >> ~/.bashrc
```

#### 問題 3：沙盒環境無法啟動

```
Error: Docker sandbox failed
```

**解決方案**：
```bash
# 檢查 Docker 狀態
docker ps

# 使用本地 OS 沙盒
skillevaluator tier3 evaluate ./my-skill --sandbox os

# 或使用雲端沙盒
skillevaluator tier3 evaluate ./my-skill --sandbox cloud
```

---

## 參考資源

### 官方文件

- [安裝指南](https://docs.nvidia.com/skills/skillevaluator/installation)
- [Tier 1 驗證](https://docs.nvidia.com/skills/skillevaluator/tier1-validation)
- [Tier 2 去重](https://docs.nvidia.com/skills/skillevaluator/tier2-deduplication)
- [Tier 3 即時評估](https://docs.nvidia.com/skills/skillevaluator/tier3-live-evaluation)
- [CLI 參考](https://docs.nvidia.com/skills/skillevaluator/cli-reference)
- [報告格式](https://docs.nvidia.com/skills/skillevaluator/reports)
- [CI 整合](https://docs.nvidia.com/skills/skillevaluator/ci-integration)

### 相關專案

- [SkillSpector](https://github.com/NVIDIA/SkillSpector) - AI 技能安全掃描
- [Agent Skills Specification](https://agentskills.io/) - 技能規範
- [NVIDIA Verified Skills](https://github.com/NVIDIA/skills) - 驗證技能目錄

### 研究論文

- [arXiv:2608.20614](https://arxiv.org/abs/2608.20614)
- [CITATION.cff](https://github.com/NVIDIA/SkillEvaluator/blob/main/CITATION.cff)

---

## 支援與回饋

- **支援層級**: Experimental（實驗性）
- **支援管道**: [GitHub Issues](https://github.com/NVIDIA/SkillEvaluator/issues)
- **安全回報**: [SECURITY.md](https://github.com/NVIDIA/SkillEvaluator/blob/main/SECURITY.md)（私密回報）
- **社群規範**: [CODE_OF_CONDUCT.md](https://github.com/NVIDIA/SkillEvaluator/blob/main/CODE_OF_CONDUCT.md)

---

*最後更新：2024 年*
