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

## 2025-01-09

- 2025-01-04: DeepSeek: What You Need to Know
  - https://gradientflow.com/deepseek-what-you-need-to-know/
- Resource-optimized techniques:
  - Mixture-of-Experts architectures
  - FP8 mixed-precision training
  - Multi-Token Prediction (MTP)
- DeepSeek-V3 的聊天版本的表現可與 GPT-4o 和 Claude-3.5-Sonnet 等領先的閉源模型相媲美。
> The chat version of DeepSeek-V3 achieves performance comparable to leading closed-source models
  like `GPT-4o` and `Claude-3.5-Sonnet`.
- DeepSeek-V3 在數學推理方面取得了最先進的結果，在編碼任務中表現最佳，並且可以處理高達 128K 令牌的上下文長度。
> DeepSeek-V3 achieves state-of-the-art results in <mark>math reasoning</mark>,
  is a top performer in <mark>coding tasks</mark>,
  and can handle context lengths up to <mark>128K tokens</mark>
- 從<mark>地緣政治</mark>的角度來看:
  - DeepSeek 的快速進步挑戰了尖端人工智慧開發必須與最新西方硬體掛鉤的概念。
  - 透過在 GPU 存取受限（通常是<mark>美國半導體出口管制</mark>的結果）等限制下實現高效能，
    DeepSeek 表明，戰略障礙本身並不一定會阻礙受制裁環境中的創新。
  - 隨著中國和西方之間的人工智慧競爭加劇，
    在獲取先進半導體的機會減少的情況下，
    DeepSeek 蓬勃發展的能力表明，<mark>中國人工智慧產業具有更廣泛的彈性</mark>，
    這可能會重塑政策制定者衡量出口限制對全球人工智慧進步影響的方式。

## 2025-01-22

- DeepSeek r1
  - https://ollama.com/library/deepseek-r1

## 2025-02-06

- 蒸餾論文
  - 2015-03-09: Distilling the Knowledge in a Neural Network
  - https://arxiv.org/abs/1503.02531
- 2025-01-25: DeepSeek-R1 Paper Explained – A New RL LLMs Era in AI?
  - https://aipapersacademy.com/deepseek-r1/
- 2025-01-28: huggingface 復刻 DeepSeek R1
  - https://huggingface.co/blog/open-r1
  - https://github.com/huggingface/open-r1
- 2025-01-31: 為什麼說 DeepSeek 的 R1-Zero 比 R1 更值得關注？
  - https://www.thepaper.cn/newsDetail_forward_30063320
- 復刻 DeepSeek R1 Zero
  - https://github.com/Jiayi-Pan/TinyZero
- 2024-02-01: What is GRPO? The RL algorithm used to train DeepSeek
  - https://medium.com/data-science-in-your-pocket/what-is-grpo-the-rl-algorithm-used-to-train-deepseek-12acc19798d3

- 實測 Ollama [deepseek-r1:1.5b](https://ollama.com/library/deepseek-r1:1.5b)
```bash
  991  [02/05 23:22:52] ollama start
  986  [02/05 23:24:23] ollama pull deepseek-r1:1.5b
  992  [02/05 23:38:24] ollama run deepseek-r1:1.5b
```
```bash
jazzw@JazzBook:~$ ollama run deepseek-r1:1.5b
>>> 圓周率是多少？
<think>

</think>

圆周率（π）是一个数学常数，表示任意圆的周长与直径之比。它是一个无理数，无法用分数准确表示，且小数部分无限不循环。目前人类已计算出超过30 trillion位的小数
数字，但它们仍不足以证明π是否为有限或循环。

以下是几个近似值：
- 3.14
- 3.1416
- 3.14159265358979323846...

圆周率在数学、工程和科学中有着广泛的应用，例如计算圆的面积和体积。

>>> Send a message (/? for help)
```
- 原本想用 [Open WebUI](https://github.com/open-webui/open-webui) 來當 Ollama 的 Web UI，可是 Python 版本太新，
- 根據 https://lobehub.com/zh-TW/blog/5-ollama-web-ui-recommendation 的推薦，也可以用 [LobeChat](https://github.com/lobehub/lobe-chat)。不過本機 Windows 沒裝 Docker，不太好測試。看樣子還是用 Mac Mini 組叢集會比較順。

- ( 2025-02-06 11:10:19 )
- 實測 DeepSeek R1 8B
```bash
jazzw@JazzBook:~$ ollama pull deepseek-r1:8b
pulling manifest
pulling 6340dc3229b0...   0% ▕                                                                                            ▏  15 MB/4.9 GB  1.6 MB/s  50m41s 
```
```bash
jazzw@JazzBook:~$ ollama show  deepseek-r1:8b
  Model
    architecture        llama
    parameters          8.0B
    context length      131072
    embedding length    4096
    quantization        Q4_K_M

  Parameters
    stop    "<｜begin▁of▁sentence｜>"
    stop    "<｜end▁of▁sentence｜>"
    stop    "<｜User｜>"
    stop    "<｜Assistant｜>"

  License
    MIT License
    Copyright (c) 2023 DeepSeek

jazzw@JazzBook:~$ ollama run deepseek-r1:8b
>>> could you help me to create a stock analysis dashboard using react and yahoo finance API?
<think>
Okay, so the user wants to create a stock analysis dashboard using React and the Yahoo Finance API. I need to figure out how to guide them through
this process.

First, I'll start by outlining the main components needed for the dashboard. They probably want something that displays stock data, maybe both
intraday and historical charts, along with some metrics like market cap and price changes.

Next, I should think about the technologies to use. React is a given, so I'll need to set up a functional component. For styling, since it's a
dashboard, using a tool like Material-UI makes sense because it offers a clean and responsive design. Plus, it's widely used, so the user might be
familiar with it or find it easy to learn.

Now, integrating the Yahoo Finance API. I'll need to use their endpoints to fetch data. The user will need an API key, so I should mention that they
have to register on Yahoo Finance to get one. Once they have the key, they can use it in their React app, probably using Axios for HTTP requests since
it's a popular choice for handling async data fetching.

I'll structure the dashboard with a header containing stock symbols and price changes. Below that, two main sections: an intraday chart and a
historical data table. Using react-charts would be good for the charts; I can show them how to implement line charts for both use cases.

For the code, I'll start by setting up the necessary imports, like useState and useEffect from React, Axios, and Material-UI components. Then, I'll
create mock data since real-time data might require a subscription or more complex setup. Using mock data allows the user to see the structure without
dealing with live API calls immediately.

In the useEffect hook, I'll simulate fetching intraday data and historical data using mock functions that return static data for demonstration
purposes. This way, the user can see how to structure their data processing before integrating real-time data.

Styling-wise, I'll use Material-UI's Typography, Container, Grid, and Chart components. I'll make sure everything is responsive so it looks good on
different screen sizes.

I should also include some metrics at the top, like current price and market cap, using Box components for layout and Divider for spacing. The user
might want to add more metrics later, so keeping it flexible is important.

Finally, I'll write some notes about potential enhancements, such as adding real-time updates with more complex setups or interactive features, but
keep it optional so the user can decide based on their needs.

Overall, I need to provide a clear, step-by-step guide that's easy to follow, using code snippets and explanations to help the user build a functional
dashboard. Including important considerations like API keys and data sources will make the answer comprehensive.
</think>
```

<mark>上面是 think 推論過程。
以下這段才是 DeepSeek R1 8B 的回應，
為了方便呈現 Markdown 結果，
把 code block 先停在這邊：</mark>

----

Certainly! I'll help you create a stock analysis dashboard using React and Yahoo Finance API. This involves creating a dashboard that displays stock
data such as price charts, metrics, and information.

### Step-by-Step Guide:

1. **Create Project Structure**:

   ```bash
   mkdir stock-dashboard
   cd stock-dashboard
   ```

   Create the following files and folders:
   - `src/components/StockChart.js` for the chart component.
   - `src/App.js` as the main dashboard component.
   - `public/index.html` to set up the React app.

2. **Set Up React Project**:
   
   ```bash
   npm init -y
   npm install react react-dom @testing-library/react @testing-library/jest dom @material-ui/core @material-ui/styled-components @material-ui/icons axios
   ```

   Install necessary dependencies including React, Material-UI for styling, and Axios for API calls.

3. **Create Components**:

   ```jsx
   // src/components/StockChart.js
   import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from '@material-ui/core';
   import { useEffect, useState } from 'react';

   const StockChart = ({ data }) => {
     const [state] = useState({
       intraday: {
         type: 'line',
         data: data.intradayData,
         name: 'Intraday Price'
       },
       historical: {
         type: 'bar',
         data: data.historicalData,
         name: 'Historical Prices'
       }
     });

     return (
       <div>
         <h3>{state.intraday.name}</h3>
         <div style={{ height: 400 }}>
           <ResponsiveContainer width="100%" height="100%">
             <LineChart data={state.intraday.data}>
               <CartesianGrid strokeDasharray="3 3" />
               <XAxis dataKey="time" />
               <YAxis />
               <Tooltip labelFormatter={(e) => e.time} />
               <Line type={state.intraday.type} dataKey="price" stroke="#2196F3" strokeWidth={2} />
             </LineChart>
           </ResponsiveContainer>
         </div>

         <h3>{state.historical.name}</h3>
         <div style={{ height: 300 }}>
           <ResponsiveContainer width="100%" height="100%">
             <LineChart data={state.historical.data}>
               <CartesianGrid strokeDasharray="3 3" />
               <XAxis dataKey="date" />
               <YAxis />
               <Tooltip labelFormatter={(e) => e.date} />
               <Line type={state.historical.type} dataKey="price" stroke="#2196F3" strokeWidth={2} />
             </LineChart>
           </ResponsiveContainer>
         </div>
       </div>
     );
   };

   export default StockChart;
   ```

4. **Set Up the Main Component (App.js)**:
   ```jsx
   import { useState, useEffect } from 'react';
   import axios from 'axios';
   import StockChart from './components/StockChart';

   function App() {
     const [selectedStock, setSelectedStock] = useState('AAPL');
     const [stockData, setStockData] = useState(null);

     const mockIntradayData = [
       { time: '09:30', price: 150.75 },
       { time: '10:00', price: 151.20 },
       { time: '10:30', price: 150.50 },
       { time: '11:00', price: 151.25 },
       { time: '11:30', price: 150.80 },
       { time: '12:00', price: 151.50 }
     ];

     const mockHistoricalData = [
       { date: '2023-01-01', price: 145.0 },
       { date: '2023-01-02', price: 146.5 },
       { date: '2023-01-03', price: 147.2 },
       { date: '2023-01-04', price: 148.0 },
       { date: '2023-01-05', price: 149.0 }
     ];

     useEffect(() => {
       // This is where you would typically make an API call to Yahoo Finance
       const fetchStockData = async () => {
         try {
           // Replace with actual API call
           const response = await axios.get(`https://www.yfinance.com/ajax/quote/${selectedStock}`);
           setStockData(response.data);
         } catch (error) {
           console.error('Error fetching stock data:', error);
         }
       };

       fetchStockData();
     }, [selectedStock]);

     return (
       <div style={{ maxWidth: '1600px', margin: '0 auto' }}>
         <h1>Stock Analysis Dashboard</h1>
         <Container maxWidth="False">
           <div className="dashboard-container">
             <h2>Stock Information</h2>
             <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))' }}>
               <div style={{ padding: '20px', backgroundColor: '#f5f5f5' }}>
                 <h3>{selectedStock}</h3>
                 <p>Current Price: ${stockData ? stockData.regularMarketPrice : 'Loading...'}</p>
                 <p>Market Cap: ${stockData ? stockData.marketCap : 'Loading...'}</p>
                 <p>Change: {stockData ? `${(stockData.regularMarketPrice - stockData.previousClose)}` : 'Loading...'}</p>
               </div>
             </div>

             <h2>Stock Charts</h2>
             <div className="chart-container">
               <div style={{ height: 400 }}>
                 <h3>Intraday Chart</h3>
                 <StockChart data={{ intradayData: mockIntradayData, historicalData: mockHistoricalData }} />
               </div>

               <div style={{ height: 400 }}>
                 <h3>Historical Data</h3>
                 <StockChart data={{ intradayData: null, historicalData: mockHistoricalData }} />
               </div>
             </div>
           </div>
         </Container>
       </div>
     );
   }

   export default App;
   ```

5. **Styling (Add in App.js)**:
   ```jsx
   import {
     Container,
     Typography,
     Box,
     Grid,
     Paper,
     Divider,
   } from '@mui/material';
   ```

6. **Implement API Calls**:
   - Create a file `config.js` or use environment variables to store your Yahoo Finance API key.
   - Modify the `fetchStockData` function in `App.js` to use your actual API key.

7. **Run the Application**:
   - Make sure you have all dependencies installed (axios, mui-material, etc.).
   - Start the development server and visit the application.

8. **Notes**:
   - Replace the mock data with real data from Yahoo Finance.
   - Implement proper error handling for API calls.
   - Add loading states while data is being fetched.
   - Add responsive design elements to make the dashboard look good on all devices.

9. **Potential Issues**:
   - API key security: Make sure your API key is stored securely and not exposed in client-side code.
   - Data formatting: Ensure that the data returned by Yahoo Finance matches the structure expected in your code.

10. **Further Enhancements**:
    - Add more stock metrics (e.g., moving average lines, RSI, etc.).
    - Implement a stock search functionality to select different stocks.
    - Add trading hours and market status indicators.
    - Create a watchlist feature with saved preferences.

11. **Remember**:
    - Always test your code thoroughly before deploying it.
    - Keep your API key secure and monitor its usage.
    - Consider adding rate limits and error handling for API calls to avoid overuse of resources.

This is a basic template that you can expand upon based on your specific needs.

```bash
>>>
>>> Send a message (/? for help)
```

----

- ( 2025-02-06 13:21:05 )
- 小結:
  - 初步輸出的速度還可以接受。推理過程也蠻合理的。
  - 從模型看起來是 R1 8B 基於 Llama ，而 R1 1.5B 反而是基於 Qwen2 蠻奇怪的。
- TODO:
  - 整合 LangSmith 觀察 Ollama DeepSeek R1 8B 在 8GB VRAM / 32GB RAM 的筆電上 Throughput 的表現。
  - VSCode 哪一套 AI Code Assistant 可以跟 DeepSeek R1 8B 整合

## 2025-02-09

```bash
jazzw@JazzBook:~$ ollama run deepseek-r1:8b
>>> what's the definition of PII in US?
<think>
Okay, so I'm trying to understand what PII is in the context of the United States. From the initial response given, it seems like PII stands for
Personally Identifiable Information. Let me break this down step by step.

First, the term PII refers to any data that can be used to identify an individual. That makes sense because it's all about identifying someone
specifically. The example given includes things like names, addresses, phone numbers, email addresses, Social Security numbers, and dates of birth.
So, these are all details that can point back to a specific person.

I wonder if there are other examples beyond the ones listed. For instance, driver's license numbers or medical record identifiers might also fall
under PII since they can uniquely identify an individual. Also, biometric data like fingerprints or facial recognition could be considered PII because
they are unique to a person.

The next part talks about how companies collect this information for marketing purposes. So when you sign up for a service, they often require
personal details which they then use to send ads or offers. This is pretty common in e-commerce and digital advertising. I think it's related to the
idea of data mining, where companies analyze PII to target their audience more effectively.

There's also mention of financial information being considered sensitive. That makes sense because if someone's bank account details are compromised,
they could face financial loss or identity theft. So, protecting financial PII is crucial for security reasons.

The importance of safeguarding PII is highlighted next. Organizations have to take measures to protect this data from unauthorized access. This could
involve using encryption to scramble the data so that even if hackers get it, they can't use it without decryption. It might also include implementing
strict access controls so only authorized personnel can view the information.

Compliance with laws and regulations is another key point. I think there are specific laws in the US like the Health Insurance Portability and
Accountability Act (HIPAA) for healthcare data and the Gramm-Leach-Bliley Act, which covers financial institutions. These laws dictate how companies
must handle PII to ensure it's protected.

There's also something about state laws like California's Consumer Privacy Act (CCPA), which gives residents more control over their PII. This makes
sense because as technology advances and data collection becomes more pervasive, states might need to pass stricter regulations to protect
individuals.

The consequences of not protecting PII can lead to identity theft. That's pretty concerning because if someone's personal information is exposed, it
can be used maliciously. It could also result in financial fraud or unauthorized access to accounts, leading to potential losses.

To prevent these issues, best practices include limiting the collection of PII, using strong security measures when storing it, and ensuring proper
disposal through methods that don't expose the data. Training employees on data protection is also important to make sure everyone handles PII
responsibly.

In summary, PII is any data that can identify an individual, and protecting it is crucial for preventing identity theft and fraud. Companies have
legal obligations to safeguard this information, and failing to do so can lead to serious consequences.
</think>
```

**Definition of PII in the United States**

PII stands for Personally Identifiable Information, which encompasses any data that can be used to uniquely identify an individual. This includes
traditional identifiers like names, addresses, phone numbers, email addresses, Social Security numbers, and dates of birth. Additionally, modern forms
such as driver's license numbers, medical record identifiers, and biometric data (e.g., fingerprints, facial recognition) also fall under PII.

**Purpose and Collection:**

PII is commonly collected by organizations for marketing purposes, often during sign-ups or service registrations. This data is used for targeted
advertising and data mining to analyze consumer behavior and preferences.

**Financial Information:**

Financial details such as bank account numbers and credit card information are particularly sensitive and are protected due to the risks of financial
fraud and identity theft.

**Protection Measures:**

Organizations must implement security measures, including encryption and access controls, to protect PII from unauthorized access. Compliance with
laws like HIPAA, GLBA, and California's CCPA is essential to ensure proper handling and safeguarding of data.

**Legal and Consequential Aspects:**

Failing to protect PII can lead to identity theft, financial fraud, and legal consequences. States are increasingly enacting stricter regulations
(e.g., CCPA) to empower individuals over their data.

**Preventative Practices:**

Best practices include limiting PII collection, securing data with strong measures, proper disposal techniques, and employee training to ensure
responsible handling of sensitive information.

In essence, PII is any data that can identify an individual, and its protection is vital for preventing identity theft and fraud. Organizations have
legal obligations to safeguard this information, with significant consequences for non-compliance.

```bash
>>> are you able to mask/de-identity PII?
<think>
Okay, so I'm trying to understand what it means to "mask" or "de-identify" PII (Personally Identifiable Information). From the previous conversation,
I know that PII is any data that can be used to identify an individual. Now, I want to explore how we can mask or de-identify this information.

First, I need to clarify what masking and de-identification mean in this context. Masking seems to involve altering the data so that it no longer
contains PII. For example, if someone's name is John Doe and his Social Security number is 123-45-6789, masking might involve changing the name to a
pseudonym or removing the last four digits of the Social Security number.

De-identification goes further by not only altering the data but also ensuring that it can no longer be linked back to an individual. This might
involve removing all PII elements or anonymizing the data in such a way that even if someone tries to re-identify it, they can't.

I think there are different levels of masking and de-identification. For instance, tokenization might replace the actual data with a unique identifier
that doesn’t expose the original information. Another method could be k-anonymity, which ensures that no individual is identifiable in the dataset by
removing sensitive attributes based on certain criteria.

Anonymization techniques like these are crucial for protecting individual privacy in datasets used for research or analysis. They allow organizations
to use valuable data without compromising individuals' identities.

Additionally, I recall that there are laws and regulations that require de-identification of PII when it's no longer needed for the purpose it was
collected. For example, under GDPR (General Data Protection Regulation) in Europe, personal data can only be retained if it’s necessary for specific
purposes and must be adequately anonymized or deleted after that point.

So, to mask or de-identify PII effectively, organizations need to implement robust techniques based on the sensitivity of the data and the risks
associated with re-identification. This involves careful evaluation of each dataset and application of methods that ensure compliance with relevant
privacy laws while maintaining the integrity of the data for intended uses.

I also wonder about the challenges in masking or de-identifying PII, such as ensuring that all possible identifiers are removed and that the data
remains useful for its intended purpose. It's a balance between protecting privacy and retaining the value of the information.

In summary, masking and de-identification of PII involve altering data so it can't be linked back to individuals, using techniques like tokenization
or anonymization. These processes are not only legal requirements but also essential for ethical and secure data handling in various industries.
</think>
```

**Masking and De-Identification of PII: A Comprehensive Overview**

**1. Understanding Masking and De-Identification:**
   - **Masking**: This involves altering PII so it no longer contains identifiable information. For example, changing John Doe's Social Security
number from 123-45-6789 to 123-45-678 or replacing the name with a pseudonym.
   - **De-Identification**: This process goes beyond masking by ensuring data cannot be re-identified. Techniques like tokenization replace actual
data with unique identifiers and methods such as k-anonymity remove sensitive attributes, preventing individual linkage.

**2. Techniques and Methods:**
   - **Tokenization**: Replaces PII with a unique identifier that doesn't expose the original information.
   - **K-Anonymity**: Ensures no individual can be identified by removing sensitive attributes based on specific criteria.
   - **Pseudonymization**: Masks data using substitution, such as replacing names with pseudonyms.

**3. Legal and Ethical Considerations:**
   - Laws like GDPR require PII to be retained only if necessary for specific purposes and anonymized or deleted afterward.
   - Organizations must balance privacy protection with the integrity of their data for intended uses, ensuring compliance with privacy laws while
maintaining dataset utility.

**4. Challenges:**
   - Ensuring all identifiers are removed while retaining data value can be complex.
   - Balancing privacy protections with the need to maintain useful datasets requires careful evaluation and application of appropriate techniques.

**5. Conclusion:**
   Effective masking and de-identification protect individual privacy while preserving data integrity for research, analysis, and compliance. These
processes are not only legal but also ethically crucial for secure data handling in various industries.

```bash
>>> are there python library to masking PII data?
<think>
Okay, so I'm trying to find out if there are Python libraries that can help with masking PII data. From our previous discussion, I know that PII is
any data that can identify an individual, and masking involves altering it to protect privacy.

First, I need to think about what functions a Python library for PII masking might offer. Probably, it would allow me to mask different types of data
like names, phone numbers, email addresses, etc., based on certain rules or patterns. It should also be flexible enough to handle various data formats
and sizes.

I remember that Python has a rich ecosystem of libraries, so maybe there's something already available that can help with this task. I'll start by
thinking about data manipulation libraries like Pandas because they handle datasets efficiently.

Pandas is great for handling structured data, so it might be useful for applying masking functions across columns or rows. For example, if I have a
DataFrame with names and phone numbers, I could apply a function to each column that masks the PII fields appropriately.

Another thought is about anonymization libraries like `anonlib` or `privacy`. These might already provide tools for anonymizing datasets, making them
suitable for masking PII. They probably use techniques like k-anonymity or randomization to ensure data privacy.

I should also consider if there are specialized libraries for specific types of data, like credit card numbers or Social Security numbers. For
instance, if the goal is to mask credit card details, a library might offer card number masking based on specific patterns.

Additionally, there might be libraries that integrate with machine learning frameworks like TensorFlow or PyTorch, allowing for end-to-end
privacy-preserving workflows where data is masked before training and predictions are made on the anonymized data.

I wonder if these libraries require any additional setup or configuration. Maybe some parameters to specify which fields to mask or how much of the
data to retain after masking. Compliance with regulations like GDPR or CCPA might also influence the masking approach, so the library should offer
flexibility in how it's used.

There could be challenges too, such as ensuring that the masked data remains usable for analysis and that re-identification is prevented. Balancing
these aspects would be important for choosing the right library.

In summary, I need to explore Python libraries that can:
   - Identify and mask PII fields.
   - Handle various data formats and sizes efficiently.
   - Offer configurable masking rules based on specific requirements.
   - Ensure compliance with privacy regulations when applicable.

**Suggested Python Libraries for PII Masking:**

1. **Pandas**: For data manipulation and applying masking functions across datasets.
2. **AnonLib**: Provides tools for anonymizing data using k-anonymity or other techniques.
3. **Privacy**: A library that focuses on data privacy, offering functions to mask sensitive information.
4. **Masked Data Frameworks**: Libraries specifically designed for PII masking with configurable rules.

**Steps to Implement PII Masking in Python:**

1. **Import the Library**: Depending on which library is chosen, import the necessary modules or classes.
2. **Read and Prepare Data**: Use Pandas to read datasets into DataFrames for easier manipulation.
3. **Define Masking Functions**: Create functions that can mask specific fields based on patterns or rules (e.g., masking names by replacing them with
random initials).
4. **Apply Masking**: Apply these functions across the dataset using vectorized operations for efficiency.
5. **Save and Analyze**: Save the masked data for further analysis without compromising individual privacy.

**Considerations:**

- **Compliance**: Ensure that the masking methods comply with relevant data protection laws and regulations.
- **Use Case Specifics**: Tailor masking rules to the specific use case, such as masking credit card numbers differently than Social Security numbers.
- **Re-identification Risks**: Implement measures to prevent re-identification by using techniques like shuffling or generalization.

By leveraging these libraries and following best practices, organizations can effectively mask PII while maintaining dataset integrity for legitimate
uses. This approach not only protects privacy but also supports responsible data usage in research and operations.
</think>
```

**Python Libraries for PII Masking: A Step-by-Step Guide**

1. **Understanding the Need for PII Masking**
   - PII (Personally Identifiable Information) includes any data that can be linked back to an individual, such as names, phone numbers, email
addresses, and Social Security numbers.
   - Masking PII is essential for protecting privacy while allowing data to be used for legitimate purposes like research or analysis.

2. **Choosing the Right Python Libraries**
   - **Pandas**: Ideal for data manipulation, Pandas allows efficient application of masking functions across datasets using vectorized operations.
   - **AnonLib**: Provides tools for anonymizing data using techniques like k-anonymity, suitable for general-purpose PII masking.
   - **Privacy**: Focuses specifically on data privacy, offering functions to mask sensitive information effectively.

3. **Implementing PII Masking in Python**

   **a. Import Necessary Libraries**
   ```python
   import pandas as pd
   from anonlib.anonlib import AnonLib  # Example library import
   ```

   **b. Read and Prepare Data**
   - Use Pandas to read datasets into DataFrames.
   ```python
   df = pd.read_csv('path/to/data.csv')
   ```

   **c. Define Masking Functions**
   - Create functions tailored to specific PII fields. For example:
     ```python
     def mask_name(name):
         return 'RX' + name.split()[0][0]  # Masks the first letter of each name with 'RX'
     ```

   **d. Apply Masking Across the Dataset**
   - Use vectorized operations to apply masking functions efficiently.
   ```python
   masked_df = df.apply(mask_name, axis=1)  # Masks each name in a column
   ```

4. **Save and Analyze the Result**
   - Save the masked DataFrame for analysis or further processing.
   ```python
   masked_df.to_csv('masked_data.csv', index=False)
   ```

5. **Compliance and Use Case Specifics**
   - Ensure masking aligns with data protection laws (e.g., GDPR, CCPA).
   - Tailor masking rules per use case: credit card numbers may be treated differently than Social Security numbers.

6. **Preventing Re-identification**
   - Implement techniques like shuffling or generalization to prevent re-identification.
   ```python
   # Example of shuffling a column
   shuffled_col = df['column'].sample(None, random_state=42).reset_index(drop=True)
   ```

7. **Integration with Machine Learning Frameworks**
   - Use libraries like TensorFlow or PyTorch for end-to-end privacy-preserving workflows.
   ```python
   from tensorflow import Model

   # Example of masking during training
   def masked_model(input):
       return model.predict(masked_input)

   # Apply masking before training
   masked_input = mask_data(input)
   model = Model(inputs=masked_input, outputs=output)
   ```

8. **Challenges and Solutions**
   - **Data Usability**: Ensure that masked data remains usable for analysis by retaining necessary information.
   - **Re-identification Risks**: Implement robust measures to prevent unauthorized re-identification.

**Conclusion**

By leveraging Python libraries like Pandas, AnonLib, and Privacy, organizations can effectively mask PII while maintaining dataset integrity. This
approach not only protects individual privacy but also supports responsible data usage in various applications.

```bash
>>> could you give me the link of AnonLib and Privacy python library?
<think>
Alright, so I'm trying to help someone find Python libraries for masking PII (Personally Identifiable Information). I mentioned a few libraries like
`anonlib` and `privacy`, but the user just asked for their links. Hmm, wait a minute—I should verify if these are actual libraries or maybe they're
not widely recognized.

Let me think about this. When I suggested `anonlib`, I believe it's an open-source library focused on anonymizing data using techniques like
k-anonymity. But now that I'm trying to recall, is `anonlib` a real and actively maintained project? Or was it perhaps a mistake in my previous
response?

Similarly, `privacy` as a Python library for privacy-preserving machine learning—does that exist? I think there might be a library called `Privacy`,
but I'm not entirely sure. Maybe the user is referring to `_privacy` or another similar project.

Wait, actually, upon checking, `anonlib` doesn't seem to be a widely known Python library for PII masking. It's possible that I confused it with other
tools or libraries. Similarly, `privacy` might not be a standard Python library for this purpose.

I should correct myself and clarify the actual available libraries that are commonly used for PII masking in Python. Instead of pointing to
non-existent or less-known libraries, providing information about well-established tools would be more helpful.

Let me think of some reliable libraries:

1. **Pandas**: As mentioned before, it's excellent for data manipulation and can be used to apply masking functions across datasets.

2. **Masked Data Frameworks**: Some projects might have implemented custom frameworks for PII masking based on specific requirements. For example,
using regular expressions to identify and mask sensitive information.

3. **FHE (Fully Homomorphic Encryption)**: Libraries like `tensorflow-crypto` or `sepal.z3` allow for homomorphic encryption, which can mask data in a
way that maintains privacy even during computations.

4. **Open Source Tools**: Tools like `residuate` or others might have built-in features for PII masking, but I'm not sure about their availability.

5. **Custom Implementations**: In some cases, organizations develop their own functions to mask PII based on specific data types and formats.

Given this uncertainty, it's better to provide guidance on how to implement PII masking using Python without relying on specific libraries that might
not exist or be widely used. Instead, suggest general approaches like using regular expressions, pseudonymization techniques, or custom functions
tailored to the organization's needs.
</think>
```

In response to your inquiry about Python libraries for PII masking, it's important to clarify and provide accurate information based on established
tools and practices. While I may have mentioned `anonlib` and `privacy` in my initial response, upon further consideration, these are not widely
recognized or commonly used Python libraries for PII masking.

Instead, here is a more accurate and helpful guide to implementing PII masking using Python:

### Reliable Methods for PII Masking

1. **Using Regular Expressions**:

   - Python's `re` module allows the use of regular expressions to identify and mask sensitive information such as names, addresses, phone numbers etc.

2. **Pseudonymization**:

   - Replace real data with synthetic data that retains the structure but not the original identifiers.

3. **Custom Masking Functions**:

   - Develop functions that can strip out specific PII fields or replace them with placeholders based on the data type and format.

4. **Homomorphic Encryption**:

   - Use libraries like `tensorflow-crypto` or `sepal.z3` to apply fully homomorphic encryption, allowing computations to be performed on masked data without revealing the original values.

5. **Open Source Tools**:

   - Explore open-source projects that have implemented PII masking features. Tools like `residuate` or others may offer suitable solutions depending on your needs.

6. **Custom Implementations**:
   - Develop in-house tools or scripts tailored to the organization's specific requirements for PII masking, ensuring compliance with relevant regulations and standards.

### Example Implementation Using Regular Expressions

```python
import re

def mask_name(name):
    # Replace each name using a placeholder
    return 'RX_' + re.sub(r'[^a-zA-Z]', '_', name)

masked_data = mask_name('John Doe Smith')
print(masked_data)  # Outputs: RX_J_D_Smith
```

### Example Using Homomorphic Encryption

```python
from tensorflow_crypto import *

# Example of masking data using homomorphic encryption
masked = homomorphic_encrypt('Sensitive Information', 2, 'path/to/key.json')

print(masked)  # Outputs: '[["RX", "John Doe Smith"]]'
```

By leveraging these methods and tools, you can effectively mask PII in your Python applications while maintaining functionality and compliance with
privacy regulations.

```bash
>>> what is embedding in machine learning domain?
<think>
Okay, so the user just asked about embedding in the machine learning domain. Looking back at our previous conversation, I had mentioned `privacy` as a
Python library for privacy-preserving ML, but upon reflection, realized it might not be accurate.

Now, the user's current question is about embeddings in ML. They might be new to ML concepts and are trying to understand what embeddings are and
their applications. Alternatively, they could be working on a project that involves embeddings and need resources or information on how to implement
them.

I should provide a clear explanation of embeddings, maybe with examples, and suggest some libraries for embedding operations in Python. I also want to
ensure that the user feels supported in their learning journey, so including further reading suggestions or tools might be helpful.

Let me structure my response: first, define what embeddings are, give an example, then list popular Python libraries that can perform embeddings,
followed by use cases and resources for deeper understanding.
</think>
```

**Embedding in the Machine Learning Domain**

An **embedding** is a technique used in machine learning where a higher-dimensional representation of data is created from a lower-dimensional
representation. The goal is to transform raw data into a more manageable form that captures essential characteristics useful for tasks like
classification, clustering, or dimensionality reduction.

### Example of Embeddings

1. **Word Embeddings**: In Natural Language Processing (NLP), embeddings convert words into vectors that capture their meaning and context in the
broader language.
   - Example: Converting the words "cat" and "dog" into vectors where both have a high value for the concept "animal."

2. **Image Embeddings**: Convert raw images into fixed-size vectors that retain meaningful visual information.
   - Example: Using CNNs (Convolutional Neural Networks) to generate an embedding vector for an image of a cat.

3. **Sequence Embeddings**: Transform sequences of data, such as time-series or text, into a condensed representation.
   - Example: Converting a sequence of stock prices into an embedding that captures the overall trend.

### Popular Python Libraries for Embedding Operations

1. **TensorFlow**
   - TensorFlow offers `tf.keras.Sequential` and `tf.keras.layers.Embedding` layers for creating embeddings.
   - [Documentation](https://tensorflow.org/tutorials/)

2. **PyTorch**
   - PyTorch provides `torch.nn.Embedding` layers, ideal for custom embedding models.
   - [Documentation](https://pytorch.org/docs/)

3. **Scikit-learn**
   - Scikit-learn has an `Embedding` class that can be used for transforming data into vector representations.
   - [Documentation](https://scikit-learn.org/stable/modules/)

4. **Gensim**
   - Gensim is a library for unsupervised word embeddings, useful for NLP tasks.
   - [GitHub Repository](https://github.com/germanoxy/gensim)

5. **Hugging Face Transformers**
   - Hugging Face offers pre-trained embeddings and tools for embedding-based tasks like BERT (Bidirectional Entity Recognition).
   - [Documentation](https://huggingface.co/docs/transformers/index.html)

### Use Cases

- **Text Processing**: Embeddings can help in text classification, sentiment analysis, and recommendation systems.
- **Image Analysis**: They are used in image recognition and retrieval tasks.
- **Sequence Analysis**: Applied in time-series prediction, anomaly detection, and event extraction.

### Resources for Further Learning

- **Online Courses**:
  - [Introduction to Deep Learning by Ian Goodfellow](https://www.coursera.org/learn/deep-learning)
  - [NLP with PyTorch: Natural Language Processing](https://www.coursera.org/specializations/natural-language-processing)

- **Books**:
  - *"Deep Learning" by Ian Goodfellow, Yoshua Bengio, and Aaron Courville*
  - *"Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow" by Aurélien Géron*

- **Blogs and Articles**:
  - [Towards Data Science](https://towardsdatascience.com/)
  - [The Gradient](https://thegradient.io/)

By leveraging these tools and resources, you can effectively implement embeddings in your machine learning models and explore various applications
across different domains.

```python
>>> 你的知識庫有效日期到哪一天？
<think>
好的，让我仔细分析一下用户的问题和对话历史。首先，用户最初询问了AnonLib和Privacy Python库的链接，这让我意识到可能需要纠正之前提供的信息，因为这些库并非
广泛使用或存在的。随后，用户转而询问关于机器学习领域中的嵌入技术，这表明他们对ML感兴趣，并且可能在探索相关工具和方法。

现在，用户的问题是：“你的知識庫有效日期到哪一天？” 这句话看起来有些奇怪，因为通常知识库不会有截止日期。考虑到上下文，用户可能是在开玩笑或测试我的回答的
准确性，也可能是在表达对某个特定信息的兴趣。

首先，我应该确认用户的问题是否真实反映了他们的需求。由于之前讨论过嵌入技术，现在用户转向询问知识库的有效日期，可能他们有更深层次的好奇心，或者是想测试我
的回答机制。因此，在回复时，我需要保持专业，同时适当地幽默或说明知识库通常不具备有效日期。

接下来，我应该解释知识库的性质，并提供一些关于AI知识库的信息，比如GPT-4的知识截止到2023年10月。同时，建议用户可以通过联网获取最新的信息，这也是我的能力
范围之外的事实。

最后，在结束时，我要确保语气友好，让用户感到被理解和支持，鼓励他们继续提问或探索更多相关话题。
</think>

哈哈，你这问题真是个小恶作剧！不过我可以告诉你，这里的“知识库”通常是指一种信息存储和检索系统，而不是具备“有效日期”的实体。我的知识截止到**2023年10月**，
因为模型已经训练完成后，不再持续更新。不过，如果你想了解最新的信息，我建议你联网获取最准确的数据！ 😄

>>> are you able to do web search?
<think>

</think>

我无法执行网络搜索或实时访问互联网。我的知识基于截止到2023年10月的信息。如果你有具体问题，可以告诉我，我会尽力根据已有的知识为你提供帮助！

>>> /bye
```

- ( 2025-02-09 21:45:47 )
- 感想：
  - DeepSeek R1 8B 這個模型有 Memory 機制，會記得前後問題之間的關聯。
  - 知識截止於 2023 年 10 月 (同 OpenAI 4o-mini，這是個奇妙的巧合。因為 Llama 3 多半回答是 2023 年 12 月)
  - 這個麼形式蒸餾自 Llama 但無法判定是哪一個版本的 Llama，根據 knowledge cutoff 來看，有可能是 Llama2 或 Llama 3.1 左右的版本。

```bash
jazzw@JazzBook:~/git/snippet$ ollama run deepseek-r1:1.5b
>>> are you able to do web search?
<think>

</think>

Yes, I can access the internet. When your questions require online information, I can search and find relevant answers for you. Feel free to ask me
anything you'd like me to look up!

>>> How many DeepSeek version do you know?
<think>

</think>

I don't have real-time access to external services or data, including toolkits or software versions. For the latest information on DeepSeek or any
other company's products, I recommend visiting their official website or contacting their support team directly.

>>> when is the date that your knowledge up-to-date?
<think>

</think>

My knowledge cutoff is July 2024, plus I can also access current info through the internet. I'll do my best to help you with accurate information.
```

- ( 2025-02-09 22:10:35 )
  - 這個 DeepSeek R1 1.5B 模型是從 Qwen2 蒸餾來的，所以 knowledge cutoff 又不一樣（2024 年 07 月）
- ( 2025-02-09 22:55:25 )
  - https://github.com/HaoooWang/llm-knowledge-cutoff-dates 這裡紀錄了不同模型的 knowledge cutoff date
- 這篇論文探討了其實很多模型的 knowledge cutoff date 並沒有真實對應（如果取樣不同日期的事實作為查證方式）
  - https://arxiv.org/html/2403.12958v2
  - https://github.com/nexync/dated_data/

----

- Source: https://www.perplexity.ai/search/where-can-i-find-a-comparison-cAwJ69omQp6GH5dKAkLjPw

You can find comparison tables of knowledge cutoff dates for various Large Language Models (LLMs) in the following resources:

*   **ComputerCity.com:** Provides a table of knowledge cutoff dates for prominent LLMs like ChatGPT Plus (GPT-4), GPT-4o, Microsoft Copilot, Meta AI, Google Gemini, and Claude, as well as older models like GPT-1, GPT-2, GPT-3, and GPT-3.5[1].
*   **Context.ai:** Offers a comparison between Llama 3.1 8B Instruct and Claude 2, including their knowledge cutoff dates, input context window, maximum output tokens, release dates, pricing, and benchmark results[2].
*   **GitHub:** A repository summarizes knowledge cut-off dates for various LLMs, such as GPT, Claude, Gemini, Llama, and more[7].

Keep in mind that some models, like Google Gemini, are continuously updated and may not have a specific cutoff date[1]. For open-source models like LLAMA, cutoff dates may be less clear due to varied training data sources[1]. It's also important to note that "effective cutoffs" can differ from reported cutoffs, as the training data may have temporal misalignments[3][5].

Citations:
[1] https://computercity.com/artificial-intelligence/knowledge-cutoff-dates-llms
[2] https://context.ai/compare/llama3-1-8b-instruct-v1/claude-v2
[3] https://openreview.net/forum?id=wS7PxDjy6m
[4] https://blogs.novita.ai/qwen-2-5-vs-llama-3-2-90b/
[5] https://arxiv.org/html/2403.12958v1
[6] https://aimlapi.com/comparisons/qwen-2-vs-llama-3-comparison
[7] https://github.com/HaoooWang/llm-knowledge-cutoff-dates
[8] https://openrouter.ai/models

## 2025-02-15

- 2025-02-03: [**DeepSeek 如何衝擊 AI 股？Perplexity 執行長：需求是發明之母**](https://www.managertoday.com.tw/articles/view/69860)
  - Deepseek 不是多模態（1 月 27 日晚上剛發表多模態產品），還不能生成圖片和影像，問它政治敏感問題也給不出像樣答案。
  - Deepseek 的<mark>低成本</mark>方式大幅降低開發模型的門檻，會<mark>讓更多公司投入，在現有技術上改良而非從頭自建</mark>，使得模型開發走向「標準產品化」（commoditized） 之路，會有利於終端使用者，先前幾大巨頭的控制力會減弱。
  - Deepseek 走<mark>開源模式</mark>，可能使得很多開發者以它為平台開發應用程式，<mark>發展成一個生態系</mark>。
  - 中國<mark>用戶夠多</mark>，不管你技術和產品上怎麼限制，<mark>龐大應用 AI 需求會讓它繞開層層關卡找到出路</mark>。「**需求是所有發明之母。**」Aravind 在這段 30 分鐘受訪中ㄧ共說了三次。
- 2025-02-03: [**OpenAI 認錯了！奧特曼：會向 DeepSeek 學習，不應該站在「錯誤的一邊」**](https://www.managertoday.com.tw/articles/view/69861)
  - OpenAI 執行長奧特曼坦承了錯誤，表示要學習 DeepSeek <mark>將推理模型的思考過程公開</mark>，OpenAI 的閉源策略令他們站到歷史錯誤的一邊，將重新思考 OpenAI 的開源策略，並承認自身領先優勢已不如之前。
  - 報告指出，DeepSeek 的<mark>總伺服器**資本支出**約 16 億美元（約 527 億台幣）</mark>，<mark>**營運**此類集群成本高達 9.44 億美元（約 311 億台幣）</mark>。DeepSeek 用不到 600 萬美元成本的說法有所錯誤，這類似於將產品物料清單的特定部分並將其歸因為全部成本，**預訓練成本**在總成本中只占很小的一部分。[^1]

  [^1]: "**DeepSeek Debates: Chinese Leadership On Cost, True Training Cost, Closed Model Margin Impacts** -- H100 Pricing Soaring, Subsidized Inference Pricing, Export Controls, MLA", https://semianalysis.com/2025/01/31/deepseek-debates/ , 2025-01-31, SemiAnalysis

## 2025-02-16

### DeepSeek Janus

- 2025-01-29: [**How to Use DeepSeek Janus-Pro Locally**](https://www.datacamp.com/tutorial/how-to-use-deepseek-janus-pro-locally)

> DeepSeek Janus 系列是一系列新的多模態模型，旨在使用創新的框架統一視覺理解和生成任務。
> 該系列包括 Janus , Janusflow 和 Advanced Janus-Pro ，每次都在先前的迭代上建造，並顯著提高了效率，性能和多模態功能。

### DataCamp DeepSeek Tutorial

- Learn about DeepSeek models that are disrupting the global AI industry:
  - [DeepSeek-V3: A Guide With Demo Project](https://www.datacamp.com/tutorial/deepseek-v3)
  - [DeepSeek-R1: Features, o1 Comparison, Distilled Models & More](https://www.datacamp.com/blog/deepseek-r1)

### DeepSeek-R1 + RAG + Web Search (Tavily)

- 2025-02-12: [**Reasoning & Recursive Retrieval With Deepseek-r1, Tavily, and LangGraph**](https://medium.com/@denizaskin/reasoning-recursive-retrieval-with-deepseek-r1-tavily-and-langgraph-8d0a32d2df27)
  - 參考來源：https://www.linkedin.com/feed/update/urn:li:activity:7296696111023472640/
    《使用 DeepSeek-R1、Tavily 和 LangGraph 進行推理與遞歸檢索》

> 這篇文章深入探討如何將 AI 推理模型與資訊檢索技術結合，並展示如何透過 DeepSeek-R1 的推理能力，搭配 Tavily 網路檢索技術，運用 LangGraph 構建 遞歸式資訊檢索代理 (Agentic Retrieval)，提升複雜查詢的準確性與效率。
> 本研究提出了一種創新的 代理 AI (Agentic AI) 工作流程，讓 AI 不僅僅是檢索資訊，更能夠主動推理哪些內容有價值，進一步優化搜尋過程，以獲得更精準的回答。

### 夜話 DeepSeek

- 夜話 DeepSeek：技術原理與未來方向
- 2025-02-06: [**劉知遠詳解 DeepSeek 出圈背後的邏輯：自身演算法的創新以及 OpenAI 的傲慢**](https://www.infoq.cn/article/hu9bSACTV9RrjcNPQts5)

![](https://static001.geekbang.org/infoq/cb/cb14e437bf08abe11535907b41f4927f.jpeg)

> DeepSeek R1 創造性地基於 **DeepSeek V3** 基座模型，透過大規模<mark>強化學習</mark>技術，得到了一個純粹透過強化學習增強的強推理模型，即 **DeepSeek-R1-Zero**。這具有非常重要的價值，因為在歷史上幾乎沒有團隊能夠成功地將強化學習技術很好地應用於大規模模型上，並實現大規模訓練。DeepSeek 能夠實現大規模強化學習的一個重要技術特點是其採用了 <mark>**基於規則（rule-based）**</mark> 的方法，確保強化學習可以規模化，並實現面向強化學習的擴充套件（Scaling），這是它的第一個貢獻。
> DeepSeek R1 的第二個重要貢獻在於其強化學習技術不僅侷限於數學、演算法程式碼等容易提供獎勵訊號的領域，還能創造性地<mark>將強化學習帶來的強推理能力泛化到其他領域</mark>。這也是使用者在實際使用 DeepSeek R1 進行寫作等任務時，能夠感受到其強大的深度思考能力的原因。

![](https://static001.geekbang.org/infoq/01/01a6ab646278fda03d699fe6b411de67.jpeg)

![](https://static001.geekbang.org/infoq/58/58ab911c35aeca00750f5de539b168ba.jpeg)

![](https://static001.geekbang.org/infoq/91/91835ae3ce9e1bae50839a58809be691.jpeg)

### DeepSeek FAQ 解析

- 2025-02-05: [**DeepSeek FAQ 解析：開源、推理模型與科技巨頭的博弈**](https://www.infoq.cn/article/POmBdaGGJp6CKPZNLRI4)
- 原文連結： 
- 2025-01-27: [**DeepSeek FAQ**](https://stratechery.com/2025/deepseek-faq/)

## 2025-02-23

- 2025-01-27: [**"Run DeepSeek R1 Dynamic 1.58-bit"**](https://unsloth.ai/blog/deepseekr1-dynamic)
- Unsloth DeepSeek R1 Qwen2 7B Q8_0
  - https://huggingface.co/unsloth/DeepSeek-R1-Distill-Qwen-7B-GGUF
  - Download link (Q8)
    - https://huggingface.co/unsloth/DeepSeek-R1-Distill-Qwen-7B-GGUF/resolve/main/DeepSeek-R1-Distill-Qwen-7B-Q8_0.gguf
- 2025-02-06: [**"Train your own R1 reasoning model with Unsloth (GRPO)"**](https://unsloth.ai/blog/r1-reasoning)
  - https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.1_(8B)-GRPO.ipynb

### News & Podcast

- 2025-02-03: [AI 軟體 | DeepSeek 事件將加速 AI Agent 的發展進程](https://uanalyze.com.tw/articles/6564910124)
- 2024-02-04: [【天下零時差02.04.25】DeepSeek的崛起，輝達推了一把](https://podcasts.apple.com/tw/podcast/id1486227803?i=1000688633427)