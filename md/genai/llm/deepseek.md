# DeepSeek

- GitHub Repo：
  - https://github.com/deepseek-ai/DeepSeek-V3
- Model:
  - https://huggingface.co/deepseek-ai/DeepSeek-V3-Base

## 2025-01-03

- 2024-12-26: [DeepSeek’s new AI model appears to be one of the best ‘open’ challengers yet](https://techcrunch.com/2024/12/26/deepseeks-new-ai-model-appears-to-be-one-of-the-best-open-challengers-yet/)
> DeepSeek 的新人工智慧模型似乎是迄今為止最好的「開放」挑戰者之一

- 2024-12-27: [Why DeepSeek’s new AI model thinks it’s ChatGPT](https://techcrunch.com/2024/12/27/why-deepseeks-new-ai-model-thinks-its-chatgpt/)
> 為什麼 DeepSeek 的新 AI 模型認為它是 ChatGPT
>> DeepSeek 並未透露太多有關 DeepSeek V3 訓練資料來源的資訊。但不乏包含 GPT-4 透過 ChatGPT 產生的文字的公共資料集。如果 DeepSeek V3 接受過這些訓練，該模型可能已經記住了 GPT-4 的一些輸出，現在正在逐字複述它們。
>> 
>> 「顯然，該模型在某個時刻看到了來自 ChatGPT 的原始回應，但尚不清楚那是在哪裡，」倫敦國王學院專門研究人工智慧的研究員 Mike Cook 告訴 TechCrunch。 「這可能是『意外』……但不幸的是，我們已經看到人們直接根據其他模型的輸出來訓練他們的模型，以嘗試利用他們的知識。」
>>
>> 誠然，DeepSeek V3 遠遠不是第一個錯誤辨識自己的模型。谷歌的 Gemini 和其他公司有時聲稱自己是競爭模型。例如，在國語提示下，Gemini 宣稱是中國公司百度的文心一言聊天機器人。

- 2024-12-27: [把訓練成本打下來 99%！吊打 GPT 又 “征服” OpenAI 創始成員，DeepSeek “國產之光” 實至名歸？](https://mp.weixin.qq.com/s/YCUdbf5AvrBeXUFN0CGJbQ)

> 在程式設計競賽平臺 Codeforces 主辦的編碼競賽子集中，DeepSeek 的表現優於 Meta 的 Llama 3.1 405B、OpenAI 的 GPT-4o 和阿里巴巴的 Qwen 2.5 72B 等模型。DeepSeek V3 還在 Aider Polyglot 測試中擊敗了競爭對手，該測試旨在衡量模型是否能成功編寫新程式碼，並將其整合到現有程式碼中。

- 2024-12-29: [科技圈驚嘆！陸製 AI 大模型 DeepSeek-V3 只花 588 萬美元 性能直追 GPT-4o](https://www.ctwant.com/article/386280/)

- Aider Polyglot 測試 - https://aider.chat/docs/leaderboards/#polyglot-leaderboard

| Model	| Percent completed correctly | Percent using correct edit format | Command | Edit format |
|---|---|---|---|---|
| DeepSeek Chat V3	| 48.4% | 98.7% | aider --model deepseek/deepseek-chat | diff |

> Jazz 備註: 這裡應該是用 DeepSeek 提供的官方 API Key 來跑 Aider。目前還沒有看到 Ollama 有 DeepSeek v3 的官方模型

![](https://mmbiz.qpic.cn/mmbiz_png/ZBjVrHIdkOnp4icpdv8l46q1CMzHJzcHPd54rOf7IsMobuCu0yXo7u0LKBYEhtC4WibDZnmQVAj74Gb1xxBiaRYuQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

* 性價比: "ZeroEval Score" vs "API 價格/ 1M Token" 

![](https://mmbiz.qpic.cn/mmbiz_png/ZBjVrHIdkOnp4icpdv8l46q1CMzHJzcHPaX8BXNmoyo3lzoHE7bHq9Cx6UtX8UuEtibFTK1XXuluaibiawIjCmluRg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)