# RLM（Recursive Language Models）

- 緣起：
  - https://www.linkedin.com/feed/update/urn:li:share:7454164236987043840/
> MIT 發表的 RLM（Recursive Language Models）則給模型一個 Python 沙箱跟互動式直譯器，讓它自己寫程式去呼叫另一個子模型，自己決定要切多大段、要看哪段、要呼叫幾次。結果 RLM 驅動的 GPT-5-mini 居然能打贏 GPT-5。
>
> Trampoline AI 開源的 predict-rlm 除實作 RLM 外，更進一步用 RLM 去優化 RLM。原本的 GEPA 提示優化框架，是靠讀取模型完整的執行軌跡來改寫提示詞；但當執行端換成 RLM，產生的上千萬個Token，普通模型根本塞不下，只能改看壓縮摘要，細節全失。
>
> 團隊索性把優化端也換成RLM，讓它自己寫程式去讀取完整軌跡、決定要看哪些片段。執行的是 RLM、優化的也是 RLM，實現真正「遞迴」。結果優化後的Excel技能，甚至在 SpreadsheetBench Verified 公開排行衝到第三。
- 專案位置
  - https://github.com/Trampoline-AI/predict-rlm