# GRPO 與 PPO 演算法說明

## 目錄
- [PPO (近端策略優化)](#ppo-近端策略優化)
- [GRPO (群體相對策略優化)](#grpo-群體相對策略優化)
- [GRPO vs PPO 比較](#grpo-vs-ppo-比較)

---

## PPO (近端策略優化)

### 簡介
**Proximal Policy Optimization (PPO)** 是 OpenAI 在 2017 年提出的強化學習演算法，如今已成為 LLM 強化學習最主流的方案之一。

### 核心概念

PPO 其實是 TRPO (Trust Region Policy Optimization) 的「輕量化版本」，主要做了兩件事：

1. **Clipped Surrogate Objective (剪枝目標)**
   - 把 TRPO 那套昂貴的二階優化換成一階方法，簡單高效
   - 透過限制每次更新的步長，避免一次跳太遠把性能搞壞
   - 可以在多個 epoch 上用 mini-batch 反覆調整

2. **策略比值 (Policy Ratio)**
   - 用這個比值來衡量「現在的策略」跟「以前的策略」差多少
   - 把比值壓在 `[1-ε, 1+ε]` 範圍內，避免一次改太多出問題

### 目標函數

PPO 的核心公式：

```
L^(CLIP)(θ) = E[min(r(θ)·Ĥt, clip(r(θ), 1-ε, 1+ε)·Ĥt)·Ĥt]
```

關鍵變數：
- `r(θ) = π_θ(a|s) / π_θ_old(a|s)`：策略比值，表示新舊策略的差距
- `Ĥt`：優勢估計值（Advantage Estimate）
- `ε`：截斷係數，一般設為 0.2

### 關鍵特點

| 特性 | 說明 |
|------|------|
| **好上手** | 比 TRPO 簡單多了，不用搞二階優化 |
| **省樣本** | 在很多控制任務上比 TRPO 省數據 |
| **穩** | 截斷機制讓訓練不容易翻車 |
| **要有 Critic** | 得學一個價值函數 (critic) 來估計優勢 |
| **On-policy** | 每次都得重新採樣數據，不能reuse

### 運作流程

1. **採樣**：跟環境玩，收集 (狀態、動作、獎勵) 數據
2. **優化**：拿這些數據做多次 epoch 的策略更新
3. **截斷**：卡住更新的幅度，別一次改太多
4. **更新 critic**：同時調整價值函數網絡，算狀態價值

---

## GRPO (群體相對策略優化)

### 簡介
**Group Relative Policy Optimization (GRPO)** 是 DeepSeek 在 2024 年提出的新演算法，專門針對 LLM 的微調任務設計。

### 核心概念

GRPO 最大的突破就是**砍掉 Critic (價值函數)**，改用**群體相對獎勵**來算優勢。

1. **沒 Critic**
   - 不用像 PPO 那樣學價值函數
   - 用群體歸一化的獎勵當優勢估計
   - 同一任務生成多條軌跡，彼此比較

2. **群體歸一化 (Group Normalization)**
   - 對同一任務的 N 條軌跡算平均獎勵和方差
   - 優勢估計：`A_t = r_t - mean(r_group)`
   - 省掉訓練額外價值網絡的麻煩

### 目標函數

GRPO 的公式：

```
L_GRPO(θ) = E[1/N * Σ_i min(r_i · Ĥt_i, clip(r_i, 1-ε, 1+ε) · Ĥt_i) · Ĥt_i]
```

變數說明：
- `r_i`：第 i 條軌跡的群體相對獎勵
- `Ĥt_i = r_i - mean(r_group)`：優勢估計
- 用 N 條軌跡做群體歸一化

### 關鍵特點

| 特性 | 說明 |
|------|------|
| **沒 Critic** | 省掉價值函數的訓練和存儲 |
| **公式簡單** | 目標函數乾淨，參數少 |
| **跑得快** | 計算負擔小，適合 LLM 微調 |
| **On-policy** | 一樣得重新採樣數據 |
| **群體歸一化** | 跟群體比，不是跟絕對獎勵比

### 運作流程

1. **批次採樣**：每個任務生成 N 條不同的軌跡
2. **群體歸一化**：算平均獎勵和方差
3. **優勢估計**：用 `r_i - mean(r_group)` 當優勢
4. **策略更新**：用跟 PPO 差不多的 clip 機制更新

---

## GRPO vs PPO 比較

### 主要差異

| 項目 | PPO | GRPO |
|----------|-----|------|
| **價值函數** | 要學價值函數 | 不要 |
| **優勢估計** | Critic 網絡算 | 群體相對獎勵算 |
| **計算複雜度** | 高（兩個網絡） | 低（單網絡） |
| **存儲** | 吃記憶體 | 省記憶體 |
| **難易度** | 中等 | 簡單 |
| **提出年份** | 2017 | 2024 |
| **主打應用** | 通用 RL | LLM 推理 |

### GRPO 的優勢

1. **跑得快**
   - 省掉 critic 網絡的訓練和推理
   - 顯存和算力需求都下降

2. **寫起來順**
   - 公式更乾淨
   - 不用煩惱價值函數不穩定的問題

3. **群體相對學習**
   - 靠群體相對獎勵拿優勢信號
   - 可驗證獎勵任務（數學、程式）表現不錯

### GRPO 的局限

1. **理論基礎**
   - GRPO 的更新規則其實是算「舊策略」的梯度，不是「當前策略」
   - 需要 old policy refresh

2. **適合的場景**
   - 可驗證獎勵（binary rewards）任務表現更好
   - 連續動作空間或複雜 RL 環境可能不如 PPO

3. **探索能力**
   - 群體歸一化可能讓採樣分佈不均
   - 探索與開發的平衡可能受影響

### 怎麼選

**選 PPO 的情況：**
- 要做通用強化學習
- 需要精確的價值估計
- 連續動作空間
- 已有成熟的 PPO 實現

**選 GRPO 的情況：**
- LLM 推理任務
- 可驗證獎勵任務（數學推理、程式生成）
- 算力或記憶體吃緊
- 想快速迭代微調

### GRPO 的優勢

1. **計算效率**
   - 省去 critic 網絡的訓練和推理
   - 降低顯存和計算資源需求

2. **實現簡潔**
   - 目標函數更簡單
   - 無需處理價值函數的穩定性問題

3. **群體相對學習**
   - 透過群體相對獎勵獲得優勢信號
   - 在可驗證獎勵任務中表現良好

### GRPO 的局限性

1. **理論基礎**
   - GRPO 的更新規則實際上是估計舊策略的梯度而非當前策略
   - 需要 old policy refresh

2. **適用範圍**
   - 在可驗證獎勵（binary rewards）任務中表現更佳
   - 在連續動作空間或複雜 RL 環境中可能不如 PPO

3. **探索能力**
   - 群體歸一化可能導致分佈不均的採樣
   - 可能影響探索與開發的平衡

### 怎麼選

**選 PPO：**
- 通用強化學習
- 需要精確價值估計
- 連續動作空間
- 已有成熟實現

**選 GRPO：**
- LLM 推理
- 可驗證獎勵任務（數學、程式）
- 算力記憶體吃緊
- 想快速迭代

---

## 參考資料

### PPO 相關

1. **原始論文**: [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347)
   - Schulman et al. (2017), arXiv:1707.06347

2. **OpenAI 官方**: [OpenAI Baselines - PPO](https://openai.com/index/openai-baselines-ppo/)
   - 官方實現與說明

3. **詳細教程**: [Spinning Up - PPO](https://spinningup.openai.com/en/latest/algorithms/ppo.html)
   - OpenAI 教育資源

4. **實現細節**: [PPO 的 37 個細節](https://iclr-blog-track.github.io/2022/03/25/ppo-implementation-details/)
   - ICLR Blog Track

5. **HuggingFace**: [PPO for Deep RL](https://huggingface.co/blog/deep-rl-ppo)

### GRPO 相關

6. **原始論文**: [DeepSeekMath](https://arxiv.org/pdf/2402.03300)
   - Shao et al. (2024), arXiv:2402.03300

7. **理論與實踐**: [On the Theory and Practice of GRPO](https://arxiv.org/html/2508.02833v2)
   - GRPO 理論分析與改進

8. **損失分析**: [GRPO's Effective Loss, Dynamics, and Success Amplification](https://arxiv.org/html/2503.06639v4)
   - 損失函數動態分析

9. **PRM 視角**: [GRPO is Secretly a Process Reward Model](https://arxiv.org/html/2509.21154v2)
   - GRPO 作為 PRM 的分析

10. **經典環境**: [Learning Without Critics?](https://arxiv.org/html/2511.03527)
    - GRPO 在經典 RL 環境的表現

11. **LLM 推理比較**: [PPO, GRPO, DAPO for LLM Reasoning](https://arxiv.org/html/2512.07611)
    - 三種算法在 LLM 推理的比較

12. **基本原理**: [A First-Principles Derivation of LLM Policy Optimization](https://arxiv.org/html/2606.16733)
    - 從基本原理推導 GRPO

13. **ICLR 2026**: [REINFORCE ALGORITHM: GRPO](https://proceedings.iclr.cc/paper_files/paper/2026/file/6cad062f78120689e8a678b8af9c6d92-Paper-Conference.pdf)

### 比較研究

14. **環境比較**: [GRPO vs PPO in RL Environments](https://openreview.net/forum?id=7aMGU8kCX1)
    - OpenReview 比較研究

---

*更新時間：2026*
