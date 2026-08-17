# Artificial Analysis Intelligence Index

- https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index
  - 還蠻常看到的模型評測指標，特別是最近在比較不同模型能力與 Token 成本的時候
- 方法論：
  - Artificial Analysis Intelligence Benchmarking Methodology
  - https://artificialanalysis.ai/methodology/intelligence-benchmarking

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Gemini Live Chat
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
幫我生成中文摘要 https://artificialanalysis.ai/methodology/intelligence-benchmarking#artificial-analysis-intelligence-index
</td></tr><tr><td>A:</td><td>

[Artificial Analysis Intelligence Index v4.1.1](https://artificialanalysis.ai/methodology/intelligence-benchmarking#artificial-analysis-intelligence-index) 是由 Artificial Analysis 建立的語言模型智力評測框架，結合 9 項基準測試來評估 AI 在推理、知識、數學與程式設計等面向的綜合能力，重點偏重於 Agent（代理人）任務。

**四大評測類別與權重**

* **Agents 代理任務 (34%)**：包含 GDPval-AA v2 (20%) 與 $\tau^3$-Banking (14%)，測試 AI 在複雜環境下的文件產出、資料檢索與雙向代理模擬能力。
* **Coding 程式編程 (24%)**：包含 Terminal-Bench v2.1 (16%) 與 SciCode (8%)，評估終端機指令執行與科學計算程式碼寫作。
* **Scientific Reasoning 科學推理 (24%)**：包含 Humanity's Last Exam (12%)、GPQA Diamond (6%) 與 CritPt (6%)，測試高難度的跨學科科學推理與符號運算。
* **General 通用能力 (18%)**：包含 AA-Omniscience (12%) 與 AA-LCR (6%)，衡量模型回答的準確度、幻覺抑制率與長文本理解力。

**核心評測原則**

* **標準化與零樣本 (Zero-Shot)**：所有模型皆在一致的條件下測試，不給予範例（Few-shot），直接檢驗模型理解並執行指令的能力。
* **客觀與透明**：結合測試集比對與專家模型（LLM Judge）評分，並完全公開提示詞範本與測試條件。

**測試參數與環境**

* **溫度（Temperature）設定**：一般模型設定為 0；推理型模型設定為 0.6。
* **執行環境與計分**：程式評測統一於 Ubuntu 22.04 LTS / Python 3.12 環境運行，計分主要採用 pass@1（首次嘗試正確率）。

</td></tr>
</table>
