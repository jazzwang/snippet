# Collecting Visual Studio Code Extension Installs

## 2025-01-07

- 緣起：
  - 想要觀察目前 VS Code Marketplace 上的 AI Coding Agent 被下載的趨勢。
- **作法**：
  - 預計模仿 https://github.com/gabrielchua/daily-ai-papers.git 用 Github Action 的 cron job 去跑一隻 Python 程式。下載特定的 extension installs 數字。
  - 使用 vscode marketplace api 取得下載/安裝次數
    - https://gist.github.com/jossef/8d7681ac0c7fd28e93147aa5044bc129
    - https://stackoverflow.com/a/76993808
  - Data Model:
    - 預計用 `str(itemName).lower()` 當檔名
    - 格式：為了方便一天 append 一行，一則是用 NDJSON (JSONL)，一則是用 CSV。
      - JSONL 不確定 pandas 是否好讀？ 
        - A: `df = pd.read_json("test.jsonl", lines=True)` 
        - https://stackoverflow.com/a/78446709/4209274
        - https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#line-delimited-json
      - CSV 應該 `d3.js` 還算好處理。
        - 參考範例： https://gist.github.com/3dd9d8952f52dbcfbd72de763da2097c 顯示用 `d3.queue` 讀取兩個不同的 CSV
        ```javascript
        d3.queue()
        .defer(d3.csv, "people.csv")
        .defer(d3.csv, "fruits.csv")
        .await(function(error, people, fruits) {
        ```
- **蒐集對象**： 選自 [2025-01-07 VS Code Marketplace - Tag = `AI Coding Assistant` 的擴充套件](https://marketplace.visualstudio.com/search?term=tag%3A%22ai+coding+assistant%22&target=VSCode&category=All+categories&sortBy=Installs)
  - GitHub Copilot - https://marketplace.visualstudio.com/items?itemName=GitHub.copilot
  - GitHub Copilot Chat - https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat
  - TONGYI Lingma - https://marketplace.visualstudio.com/items?itemName=Alibaba-Cloud.tongyi-lingma
  - Amazon Q - https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.amazon-q-vscode
  - CodeGeeX - https://marketplace.visualstudio.com/items?itemName=aminer.codegeex
  - BLACKBOXAI - https://marketplace.visualstudio.com/items?itemName=Blackboxapp.blackbox
  - Tabnine - https://marketplace.visualstudio.com/items?itemName=TabNine.tabnine-vscode
  - Codeium - https://marketplace.visualstudio.com/items?itemName=Codeium.codeium
  - CodeGPT - https://marketplace.visualstudio.com/items?itemName=DanielSanMedium.dscodegpt&ssr=true#overview
  - Continue - https://marketplace.visualstudio.com/items?itemName=Continue.continue
  - Bito AI Code Assistant - https://marketplace.visualstudio.com/items?itemName=Bito.Bito
  - Mintlify - https://marketplace.visualstudio.com/items?itemName=mintlify.document (僅專注於生成文件)
  - Qodo Gen (Codium) - https://marketplace.visualstudio.com/items?itemName=Codium.codium
  - Cline (prev. Claude Dev) - https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev
  - MarsCode - https://marketplace.visualstudio.com/items?itemName=MarsCode.marscode-extension (中國大陸，豆包)
  - Supermaven - https://marketplace.visualstudio.com/items?itemName=supermaven.supermaven
  - Genie AI - https://marketplace.visualstudio.com/items?itemName=genieai.chatgpt-vscode
  - Sourcery - https://marketplace.visualstudio.com/items?itemName=sourcery.sourcery (專注於 Code Review，[使用 Claude 3.5, Gemini 1.5, GPT4-o](https://docs.sourcery.ai/LLM-Usage/))
  - Cody - https://marketplace.visualstudio.com/items?itemName=sourcegraph.cody-ai
    - [Supported local Ollama models with Cody](https://sourcegraph.com/docs/cody/clients/install-vscode#supported-local-ollama-models-with-cody)