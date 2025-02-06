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