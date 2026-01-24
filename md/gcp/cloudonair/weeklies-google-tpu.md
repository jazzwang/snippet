# Weeklies | Next-level AI/ML performance: surprisingly simple with Cloud TPUs

## 2025-11-18

- Original air date: 2025-11-18 11:30 AM
- https://cloudonair.withgoogle.com/events/weeklies-genai-next-level-ai-ml-performance-with-cloud-tpus-nov-2025
- https://cloudonair.withgoogle.com/events/weeklies-genai-next-level-ai-ml-performance-with-cloud-tpus-nov-2025/watch?talk=talk-1
  - https://youtu.be/SgqBIxMZWZs

## 2026-01-23

### 雲端運算的下一個十年：揭秘 Google Cloud TPU 如何將「超級運算」變成你的日常工具

雲端運算的下一個十年：揭秘 Google Cloud TPU 如何將「超級運算」變成你的日常工具

#### 1. 引言：AI 開發者的夢魘與曙光

在當前的 AI 浪潮中，研發人員正陷入一場無止盡的「規模戰爭」。當模型架構從數十億參數演進至數兆參數時，底層基礎設施的複雜度已成為創新的最大絆腳石。手動同步多節點代碼、處理難解的網路瓶頸，以及在單機實驗與大規模生產之間不可逾越的鴻溝，耗費了無數研究員的精力。

作為基礎設施架構師，我觀察到一種典範轉移：超級運算正從「昂貴且複雜的特權」轉化為「隨手可得的日常」。Google Cloud TPU 的演進不僅僅是晶片的升級，更是一場關於效能、效率與簡潔性的革命。本文將透過以下六大轉型支柱，揭示 Google 如何重新定義 AI 開發的未來。

#### 2. 第七代「Ironwood」：運算規模與硬體限制的徹底解耦

今年四月揭曉的第七代 TPU 加速器 —— Ironwood，並非只是微小的效能迭代，它代表了運算力與硬體約束之間的深度解耦。Ironwood 針對現今主流的 JAX 與 PyTorch 框架進行了深度優化，確保開發者能在最熟悉的生態系中獲得極致效能。

Ironwood 技術規格與部署架構：

* 效能飛躍： 提供較前代提升 5 倍的峰值運算能力 (Peak Compute) 與 2 倍的記憶體容量。
* 經濟指標： 核心設計目標在於極大化「每美元效能 (Performance per dollar)」與「每瓦效能 (Performance per watt)」。
* 物理足跡： 大型分區編制 (Large partition formation) 由 144 個機架 (Racks) 組成，包含 9,216 顆晶片，並透過冷卻分配單元 (CDU) 進行熱管理。
* 彈性配置： 支援從單顆晶片到 256 顆晶片的 Pod，乃至數千顆晶片的大型陣列。

對架構師而言，Ironwood 的意義在於大幅降低了總體擁有成本 (TCO)，同時讓訓練超大型模型的實驗成本不再令人望而生畏。

#### 3. 從筆電到萬顆晶片：Pathways 實現的「互動式超級運算」

以往 AI 開發最痛苦的莫過於「幫派調度 (Gang-scheduling)」模式下的僵化。Pathways 分散式運行環境 (Distributed Runtime) 徹底打破了這個傳統，透過代理程式 (Proxy-based) 的分發機制，實現了真正的互動式開發。

現在，開發者透過 GKE (Google Kubernetes Engine) 管理 TPU 叢集，能獲得以下突破：

* 無縫擴展： 藉由超高頻寬的 Taurus Interchip Interconnect，單一 ICI 域可擴展至 9,000 個以上晶片；透過數據中心網路 (DCN) 甚至可聯動數十萬顆晶片協同作業。
* 消除環境不一致： 開發者可以直接從單一 Python 解譯器或筆電，像操控本地裝置一樣驅動大規模加速器艦隊，無需手動重構代碼。
* 極致的靈活性： 支援跨切片 (Cross-slice) 的彈性訓練與彈性推理，這對於 Gemini 這種等級的模型訓練至關重要。

#### 4. AI 超級電腦（AI Hypercomputer）：共同設計的系統哲學

TPU 的強大不僅來自單一晶片，而在於其「共同設計 (Co-design)」的 AI 超級電腦 哲學。這種將硬體、軟體、網路與儲存視為整體進行優化的路徑，是達成系統級效率的最佳途徑。

* 光路交換 (Optical Circuit Switching, OCS)： 不同於傳統的靜態網路，OCS 允許動態重構網路拓撲，以匹配特定模型的「運算形狀 (Model Shape)」，確保在大規模擴展時仍能維持極低延遲。
* 液體冷卻 (Liquid Cooling)： 基於 Google 超過十年的液冷經驗，這不僅是為了穩定性，更是確保晶片能在高負載下維持最高效率運作。
* 稀疏核心 (Sparse Core)： 這是應對現代 AI 挑戰的神來之筆。專為 Embedding 操作 與稀疏矩陣設計，能顯著加速大規模推薦系統與複雜 LLM 的處理速度。

#### 5. 當 AI 訓練出諾貝爾獎：AlphaFold 的科學實證

AI 基礎設施的價值不應僅以運算速度衡量，更應以其對人類科學的貢獻來定標。DeepMind 的 AlphaFold 便是最佳案例，它利用 TPU 解決了困擾生物學界半世紀的蛋白質結構預測難題。

「DeepMind 團隊的 Demis Hassabis 爵士與 John Jumper 博士，因 AlphaFold 的卓越成就獲得了今年的諾貝爾化學獎。AlphaFold 在 TPU 上進行訓練，成功將科學家的研究工具從實驗室延伸至數位超級電腦，這是基礎設施推動科學進步的終極證明。」

這代表我們正進入一個新紀元：基礎設施不再是工程部門的預算項，而是推動人類科學邊界的關鍵引擎。

#### 6. XPRO：內行人的 AI 艦隊監控系統

為了讓開發者不再對黑盒運算感到無力，Google 將內部最強大的診斷工具藉由 OpenXLA 專案全面開放。XPRO 剖析工具 (Profiling Tool) 與 XLA 編譯器 的組合，為開發者提供了極致的透明度。

* 統一的開發體驗： 無論底層是 JAX、PyTorch 還是 Keras，XPRO 都能提供跨框架的統一監控介面。
* 精準瓶頸定位： 開發者可以即時分析平均步進時間 (Average Step Time)，並釐清框架在加速器與主機端 (Host) 之間的效能佔比。
* 社群驅動： 這些工具目前已整合至 GitHub 的 AI Hypercomputer 儲存庫中，將 Google 與 DeepMind 內部的實戰能力賦予全球每一位開發者。

#### 7. 結論：未來已至，你準備好了嗎？

Google Cloud TPU 正在透過簡單性、規模與效能，徹底重塑雲端運算的遊戲規則。更令人興奮的是，我們正進入一個技術自我進化的奇點：目前的 TPU 正在協助科學家設計下一代的 TPU。

在「計算資源」不再是瓶頸的未來，限制創新的唯一邊界將是你的想像力。當你可以像打開筆電一樣調動九千顆晶片的超級運算力時，你的下一個偉大創意會是什麼？
