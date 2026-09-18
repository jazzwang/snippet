- Source: https://harnesstax.github.io/
- Learn from ZhuLin

## 2026-09-18

> [!QUESTION]
> 請根據 https://harnesstax.github.io/ 內容撰寫一篇繁體中文的技術摘要，並經 /skill:speak-human-tw 潤飾詞句後存成 HarnessTax.md

## HarnessTax 研究技術摘要

### 研究概述

**HarnessTax** 是由加州大學柏克萊分校（UC Berkeley）與 LMSYS Arena 的研究人員共同進行的聯合研究，主要探討 AI 編碼代理的「harness」（即管理系統提示、工具架構、載入上下文以及命令執行的包裝器）如何影響編碼代理的成本與成功率。

### 研究方法論

#### 評估架構

研究共評估了 **3 種 harness** 與 **7 個模型** 的組合：

**Harness（3 種）：**
- Claude Code
- Codex CLI
- Pi

**模型（7 個）：**
- Claude Fable 5
- Claude Opus 4.8
- Claude Sonnet 4.6
- Claude Haiku 4.5
- GPT-5.6 Sol
- GPT-5.6 Luna
- Kimi K3

#### 測試基準

| 基準 | 任務類型 |
|------|----------|
| SWE-bench Lite | 軟體修改任務 |
| Terminal-Bench 2.0 | CLI 執行任務 |

#### 實驗設定

- 每個基準隨機選擇 **30 個任務**
- 每種模型 - harness 組合進行 **3 次重複執行**
- 每回合最多 **100 次轉換（turns）**

### 主要發現

#### 1. 任務成功率影響極小

更換 harness 對任務成功率的影響微乎其微：
- SWE-bench Lite：僅在 **±2%** 範圍內變動
- Terminal-Bench 2.0：僅在 **±5%** 範圍內變動

#### 2. 成本差異巨大（最高可達 5 倍）

儘管成功率幾乎相同，但根據所使用的 harness 不同，代幣成本差異可達 **5 倍**。

#### 3. 「Harness Tax」（harness 稅）的形成原因

額外的成本來自於：
- 工具造成的額外負載
- 未優化的對話歷史
- 龐大的初始上下文/系統提示

例如，Claude Code 等工具可產生高達 **27,000 個輸入代幣**的額外負載。

#### 4. 預設 harness 並非總是最佳選擇

在非原生 harness 上運行模型，有時能獲得更好的成本效益或更高的成功率：

| 模型 | harness | 成功率 |
|------|---------|--------|
| Claude Sonnet 4.6 | Codex CLI | 68.9% |
| Claude Sonnet 4.6 | Claude Code | 67.7% |
| GPT-5.6 Sol | Pi harness | 83.3% |
| GPT-5.6 Sol | Codex CLI | 78.9% |

#### 5. 成本效益實例

在 SWE-bench Lite 上測試 Claude Fable 5 時：
- **Claude Code** 平均需要約 **15.3** 回合
- **Pi** 平均需要約 **15.4** 回合
- 但 Pi 的成本僅為 Claude Code 的一半
- 成功率差距僅為 1.1 個百分點

### 研究限制

- 評估僅基於每個基準的 **30 個任務子集**，而非完整基準全面測試
- 結果反映 harness 在 **高推論配置** 下的標準預設設定
- 自訂提示或自訂上下文剪輯可能會改變這些效率權衡

### 參考來源

- [HarnessTax 官方網站](https://harnesstax.github.io/)
- [Hacker News 討論](https://news.ycombinator.com/item?id=49733726)
- [Gigazine 摘要報告](https://gigazine.net/gsc_news/en/20260917-harnesstax-ai-coding-agents/)

---

*註：本研究結果顯示，在選擇 AI 編碼代理時，harness 的選擇對成本效益的影響遠大於對任務成功率的影響。開發者應根據實際需求，靈活選擇最適合的 harness 配置。