---
presentation:
    theme: night.css
    width: 1920
    height: 1080
    slideNumber: true
    hideAddressBar: true
    history: true
---

<style>
.reveal code { color: #e7ad52; }
.reveal strong, .reveal b { color: #ffccff; }
.reveal em { color: #ccff99; }
quote { color: #e7ad52; }
</style>

<!-- slide -->

### [ Part 1 ]

## Building <font color='lightgreen'>Hospital Price Transparency</font> <font color="hotpink">Chatbot</font><br/> with `OpenAI`, `LangChain` and `Chainlit`

|||
|---|---|
| <br/><h4><a href='https://www.facebook.com/opensource4you/posts/pfbid02sKQhB1vJf9euxwPTY7WDHceVt87Ngtsii6o7oDWFetUhEjDcsAmyc4vRbDd5b4nvl' target='_blank'>源來適你 #OpenSource4You。科技開講 TechTalk</a><p/> 2024-09-14 @ HsinChu City, Taiwan</h4> <br/>By [Jazz Yao-Tsung Wang](https://jazzwang.github.io/cv/) <br/>Sr. Director, Heaad of Delivery, Innova Solutions<br/>Chairman, Taiwan Data Engineering Association | ![Jazz Wang](https://jazzwang.github.io/cv/assets/images/profile.jpg)|

<!-- slide -->

## Agenda

<hr/>

<table><tr>
<td>

- **What** is the Business Need? <---- *NEXT*
    - <font color="lightgreen">Hospital Price Transparency</font>
- **Why** building AI Chatbot?
    - Will <font color="hotpink">AI Chatbot</font> be the "new" UI?
    - <font color='lightblue'>Multilingual</font> Support?
- **How**
    - High-level Architecture
    - POC Implementation
</td>
<td>

- **Deep Dive**
    - OpenAI
    - LangChain
    - Chainlit
- **Lesson Learnt**
    - Limitation of LangChain and LocalAI
    - Chainlit Local Cache - SQLite
- **Future Plan**
    - Serverless Architecture
    - Different RAG implimentation
    - Interacting with APIs with LangChain
</td>
</tr></table>

<!-- slide vertical=true -->

## <font color="lightgreen">Hospital Price Transparency</font>

<hr/>

Effective on `2021-01-01`

<img src='https://i.imgur.com/hdI4Wzc.png' height='720'>

<small>Source: https://www.cms.gov/hospital-price-transparency</small>

<!-- slide vertical=true -->

### Civil monetary penalty (CMP) notices issued by CMS

<small>Civil monetary penalty (CMP) = 民事罰款</small>

<hr/>

<img src='https://i.imgur.com/8T45crm.png' height='720'>

<small>Source: https://www.cms.gov/hospital-price-transparency/enforcement-actions</small>

<!-- slide vertical=true -->

### `Shop site` developed by Taipei `DXP SBP` team

<hr/>

#### Patient can search `Procedure Price` based on `Payer Name` and `Medical Network`

<img src='https://i.imgur.com/TlYogEM.png' height='720'>

<small>Source: https://shop.baconcountyhospital.com/</small>

<!-- slide vertical=true -->

### Machine Readable Files (MRFs)

<hr/>

#### Hospitals need to provide their link to MRFs

<img src='https://i.imgur.com/DcpNhML.png' height='720'>

<small>Source: https://shop.baconcountyhospital.com/pt-machinereadable.html</small>

<!-- slide vertical=true -->

### 未能辦成的 2023 Data Architecture Challenge

<img src='https://i.imgur.com/kehhNez.png' height='720'>

https://hackmd.io/IuddDt16T9mw_Q-jFcViqg?view

<!-- slide -->

## Agenda

<hr/>

<table><tr>
<td>

- **What** is the Business Need?
    - <font color="lightgreen">Hospital Price Transparency</font>
- **Why** building AI Chatbot? <---- *NEXT*
    - Will <font color="hotpink">AI Chatbot</font> be the "new" UI?
    - <font color='lightblue'>Multilingual</font> Support?
- **How**
    - High-level Architecture
    - POC Implementation
</td>
<td>

- **Deep Dive**
    - OpenAI
    - LangChain
    - Chainlit
- **Lesson Learnt**
    - Limitation of LangChain and LocalAI
    - Chainlit Local Cache - SQLite
- **Future Plan**
    - Serverless Architecture
    - Different RAG implimentation
    - Interacting with APIs with LangChain
</td>
</tr></table>

<!-- slide vertical=true -->

## [ WHY ] Will <font color="hotpink">AI Chatbot</font> be the "new" UI?

<!-- slide vertical=true -->

## Call Center

<hr/>

<img src='https://storage.needpix.com/rsynced_images/call-3613071_1280.png' height='640'>
<img src='https://openclipart.org/image/800px/321065' height='640'>

> Did you call Help Desk before?

<small>Image Source: ["Telework Guy",by j4p4n, OpenClipArt, 2020-06-05](https://openclipart.org/detail/321065/telework-guy)</small>

<!-- slide vertical=true -->

## Slack Chatbot

<hr/>

<img src='https://techcrunch.com/wp-content/uploads/2017/03/niles.png' height='720'>

<small>Source: ["Niles is a Slack bot that learns your team’s questions <br/>and answers them so you don’t have to", 2017-03-17](https://techcrunch.com/2017/03/17/niles-is-a-slack-bot-that-learns-your-teams-questions-and-answers-them-so-you-dont-have-to/)</small>

<!-- slide vertical=true -->

## ChatOps

<hr/>

<img src='https://cdn.ttgtmedia.com/rms/onlineImages/it_ops-chatops_architecture.jpg' height='720'>

<small>Source: ["Three ChatOps examples demonstrate DevOps efficiency", 2018-02-05](https://www.techtarget.com/searchitoperations/tip/Three-ChatOps-examples-demonstrate-DevOps-efficiency)</small>

<!-- slide vertical=true -->

## LINE Chatbot

<hr/>

<img src='https://developers.line.biz/zh-hant/_media/services/bot-designer-thumb2.png' height='720'>

<small>Source: ["LINE Bot Designer"](https://developers.line.biz/zh-hant/services/bot-designer/)</small>


<!-- slide vertical=true -->

## ChatGPT

<hr/>

#### NLP (Natural language processing)

<img src='https://miro.medium.com/v2/resize:fit:720/format:webp/1*OhWzHPkxXbslpwYyCZ2HKA.png' height='720'>

<small>Source: ["How ChatGPT Works: The Model Behind The Bot", 2023-01-31](https://towardsdatascience.com/how-chatgpt-works-the-models-behind-the-bot-1ce5fca96286)</small>

<!-- slide vertical=true -->

## [ WHY ] <font color='lightblue'>Multilingual</font> Support?

<!-- slide vertical=true -->

## [ Pain ] Complex Architecture

<hr/>

<img src="https://i.imgur.com/djDVJmw.png" width='1280'>

( Note: I removed <font color='hotpink'>confidential diagram</font> shown here )

<small>Source: Reverse Engineering PlantUML diagram by Jazz Wang</small>

<!-- slide vertical=true -->

## [ Gain ] Needs to support multiple langauges

<hr/>

#### ChatGPT supports **95** languages

<img src='https://i.imgur.com/e3Lqoqv.jpg' height='720'>

<small>Source: ["How to Use ChatGPT in Other Languages", 2023-05-25](https://www.makeuseof.com/chatgpt-other-languages/)</small>

<!-- slide vertical=true -->

## Benefits Of Multilingual ChatGPT

<hr/>

<img src='https://i.imgur.com/vEpUkx0.png' height='720'>

<small>Source: ["List of languages supported by ChatGPT",
Botpress Community, 2023-03-23](https://botpress.com/blog/list-of-languages-supported-by-chatgpt)</small>

<!-- slide -->

## Final Result

<hr/>

### Demo site: http://chat.3du.me:8000

<img src='https://i.imgur.com/zU7PWU6.png' height='720'>

<!-- slide -->

## Agenda

<hr/>

<table><tr>
<td>

- **What** is the Business Need?
    - <font color="lightgreen">Hospital Price Transparency</font>
- **Why** building AI Chatbot?
    - Will <font color="hotpink">AI Chatbot</font> be the "new" UI?
    - <font color='lightblue'>Multilingual</font> Support?
- **How** <---- *NEXT*
    - High-level Architecture
    - POC Implementation
</td>
<td>

- **Deep Dive**
    - OpenAI
    - LangChain
    - Chainlit
- **Lesson Learnt**
    - Limitation of LangChain and LocalAI
    - Chainlit Local Cache - SQLite
- **Future Plan**
    - Serverless Architecture
    - Different RAG implimentation
    - Interacting with APIs with LangChain
</td>
</tr></table>

<!-- slide vertical=true -->

## [ HOW ] High-level Architecture

<hr/>

<img src='https://mermaid.ink/img/pako:eNplklFvgjAQx7_KpQvBJZo4km2OhyUCLjFxmUbdHsSHAoc0g5aUks0o330FVDTjoVz__99d2rseSCgiJDYxjIPPARhnyoYmBDBVghmaNpgBLdDsX6ufVDIapFiYF1xbuWQZlXtXpELWeXeOYz1ao3NqR6zwV3VUHMf_EUfICGUHPbtD_V1xKePY2W8jx7JeruwCQ8Gjm9MMh08PNyUUSsVukPoorV3VP71UhuFzn8ep-AkTKhWsvBYoymAnaZ7AjPKdm1DGz3UB3N5FhOVi5lFF6x42wn2HTXraZApPEvKoDcabdYFyC4PB63FRYqGY4Edwel8YwHoKA2gKpUydEp2aBLfduE3aXIosV0fwNh858vEUxvPptgUmLU36JEOZURbp-Tcz9EkzW5_YOtSt-_aJvr_maKnEcs9DYitZYp-UeUQVeozqBmTEjmlaaBUjpoR8bx9U866qP4_UtSc?type=png' height='720' style="background-color: lightgray">

<!--
```mermaid
%%{
init: {
    'theme': 'base',
    'themeVariables': {
    'primaryColor': '#BB2528',
    'primaryTextColor': '#fff',
    'primaryBorderColor': '#7C0000',
    'lineColor': '#F8B229',
    'secondaryColor': '#006100',
    'tertiaryColor': '#fff'
    }
}
}%%

flowchart TD
    subgraph LangChain
        C(LangChain SQLDatabaseChain)
        E(SQLite)
    end
    A[User] -> |Question| B(Web UI - Chainlit)
    B -> C
    C ->|Prompt| D[OpenAI API]
    E -> C
```
-->

<!-- slide vertical=true -->

## [ HOW ] High-level Architecture

<img src="https://mermaid.ink/img/pako:eNp9kcFqAjEQhl9lmLO-QA6CVISC0FrpbS9hd9TAZrJNJoiIh_aoto_gw_kkTQz2UBdz_Ofjy8_MDmvXECoM9BGJa5oYvfLaVgzpvQfyMByN4GmtDbdGFFzOB5hHCmIcF-g2g2EmZ5pX10RBGf8FV9FLRzx-zpojvHpnOylUye8Ul_MnLOazPlOKjVBGTrmQ3xaoxD2iL3ijEFt53Oobps5bLRnuHAd6WO_O9X9XPzDmsCHft6m8XAU4QEvpR9OkI-wyV6GsyVKFyY8NLXUujRXvE6qjuMWWa1TiIw0wdo2W281QLXUbaP8LADaaNA?type=png"  height='720' style="background-color: white">

<!-- slide vertical=true -->

## [ HOW ] POC Implementation

<hr/>


<table><tr>
<td>
PS. I tried to leverage <font color="lightgreen">local GPT4All-J LLM</font> instead of OpenAI GPT-3.5-Turbo LLM

```bash
.
├── LangChain-LocalAI
│   ├── docker-compose.yaml
│   ├── models
│   │   ├── gpt-3.5-turbo.yaml
│   │   ├── gpt4all-chat.tmpl
│   │   └── gpt4all-completion.tmpl
│   ├── requirements.txt
│   ├── titanic.db
│   └── titanic.py
```

</td><td>

```bash
└── LangChain-OpenAI                    ## Today's demo
    ├── Makefile                        ## simplify the step to run
    ├── README.md
    ├── bacon.py
    ├── chainlit.md                     ## Chainlit README page
    ├── chainlit_sample.py
    ├── gen-faiss-index-from-mrf.py
    ├── gen-sqlite-from-mrf.sh          ## create SQLite as data source
    ├── hpt-chat.py                     ## Main Program
    ├── import.sql                      ## used by gen-sqlite-from-mrf.sh
    ├── lanarky_test.py
    ├── requirements.txt                ## required Python packages
    └── templates
        └── index.html

5 directories, 19 files
```
</td></tr></table>

Source Code: https://github.com/jazzwang/hpt-chat


<!-- slide -->

## Agenda

<hr/>

<table><tr>
<td>

- **What** is the Business Need?
    - <font color="lightgreen">Hospital Price Transparency</font>
- **Why** building AI Chatbot?
    - Will <font color="hotpink">AI Chatbot</font> be the "new" UI?
    - <font color='lightblue'>Multilingual</font> Support?
- **How**
    - High-level Architecture
    - POC Implementation
</td>
<td>

- **Deep Dive** <---- *NEXT*
    - OpenAI
    - LangChain
    - Chainlit
- **Lesson Learnt**
    - Limitation of LangChain and LocalAI
    - Chainlit Local Cache - SQLite
- **Future Plan**
    - Serverless Architecture
    - Different RAG implimentation
    - Interacting with APIs with LangChain
</td>
</tr></table>

<!-- slide vertical=true -->

## [Deep Dive] OpenAI API

<hr/>

> Most poeple use ChatGPT (free) / ChatGPT Plus (paid).
> By subscribing OpenAI API, you can create application programatically.

<img src='https://i.imgur.com/gGzp6oG.jpeg' height='640'>

Source: https://platform.openai.com/apps

<!-- slide vertical=true -->

## [Deep Dive] OpenAI API Capability

<hr/>

<img src='https://i.imgur.com/pszPUpe.jpg' height='640'>

https://platform.openai.com/docs/quickstart?context=python

<!-- slide vertical=true -->

## [Deep Dive] OpenAI API Keys

<hr/>

<img src='https://i.imgur.com/pUKwp5W.jpg' height='640'>

https://platform.openai.com/api-keys

<!-- slide vertical=true -->

## [Deep Dive] OpenAI API Usage

<hr/>

<img src='https://i.imgur.com/BcvlGJC.jpg' height='640'>

https://platform.openai.com/usage

<!-- slide vertical=true -->

## [Deep Dive] OpenAI Billing Auto Recharge

<hr/>

> When you don't want to do experiment for a long term,
> you can `Cancel Plan` to reduce cost.

<img src='https://i.imgur.com/tGbAkk9.jpg' height='640'>

https://platform.openai.com/account/billing/overview

<!-- slide -->

## [Deep Dive] LangChain - Introduction

<hr/>

> `LangChain` is a <font color='hotpink'>framework</font> for developing <font color='lightgreen'>applications</font>
> powered by `language models`.

- `LangChain` enables applications that are:
    - Data-aware: **connect** a language model to **other sources of data**
    - Agentic: allow a language model to *interact with its environment*
- The main value props of `LangChain` are:
    - **Components**: *abstractions* for working with language models.
    - **Off-the-shelf chains**: *components* for accomplishing specific higher-level tasks

<small>Source: [LangChain Document - Introduction](https://python.langchain.com/docs/get_started/introduction)</small>

<!-- slide vertical=true -->

## [Deep Dive] LangChain - Modules

<hr/>

- **Model I/O** : *Interface* with language models
- **Data connection** : Interface with application-specific *data*
- **Chains** : Construct *sequences of calls*
- **Agents** : Let chains choose which *tools* to use given high-level directives
- **Memory** : Persist application *state* between runs of a chain
- **Callbacks** : *Log* and stream intermediate steps of any chain

<small>Source: [LangChain Document - Introduction](https://python.langchain.com/docs/get_started/introduction)</small>

<!-- slide vertical=true -->

## [Deep Dive] LangChain - Model I/O

<hr/>

- **Prompts**: Templatize, dynamically select, and manage model *inputs*
- **Language models**: Make ***calls** to language models* through common interfaces
- **Output parsers**: Extract information from model *outputs*

<img src='https://i.imgur.com/vyskQp2.jpeg' height='640'>

<small>Source: [LangChain Document - Model I/O](https://python.langchain.com/docs/modules/model_io/)</small>

<!-- slide vertical=true -->

## [Deep Dive] LangChain - Data Connection

<hr/>

- **Document loaders**: Load documents from many different sources
- **Document transformers**: Split, convert into Q&A format, drop redundant documents
- **Text embedding models**: Turn *unstructured text* into *vector*
- **Vector stores**: *Store* and search over embedded data
- **Retrievers**: *Query* your data

<img src='https://i.imgur.com/uHKspnM.jpg' height='520'>

<small>Source: [LangChain Document - Data connection](https://python.langchain.com/docs/modules/data_connection/)</small>

<!-- slide vertical=true -->

## [Deep Dive] LangChain - Chains

<hr/>

`Chain` = a *sequence of calls* to components, which can include other chains.

```python .line-numbers
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

llm = OpenAI(temperature=0.9)
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)
```

<small>Source: [LangChain Document - Chains](https://python.langchain.com/docs/modules/chains/)</small>

<!-- slide vertical=true -->

## [Deep Dive] LangChain - Memory

<hr/>

> By default, `Chains` and `Agents` are **stateless**

LangChain provides memory components in two forms:
- *helper utilities* for managing and manipulating previous chat messages.
- ways to incorporate these utilities into *chains*.

<small>Source: [LangChain Document - Memory](https://python.langchain.com/docs/modules/memory/)</small>

<!-- slide vertical=true -->

## [Deep Dive] LangChain - Agents

<hr/>

The core idea of agents is to <u>use an *LLM* to **choose a sequence of actions** to take</u>.

> In `chains`, a sequence of actions is *hardcoded* (in code).
> In `agents`, a language model is used as a *reasoning engine*.

<small>Source: [LangChain Document - Agents](https://python.langchain.com/docs/modules/agents/)</small>

- Agent Types:
    - **Zero-shot ReAct**    <-- <font color='hotpink'>We use this for POC</font>
    - Structured input ReAct
    - OpenAI Functions
    - Conversational
    - Self ask with search
    - ReAct document store

<small>Source: [LangChain Document - Agent types](https://python.langchain.com/docs/modules/agents/agent_types/)</small>

<!-- slide -->

## [Deep Dive] Chainlit

<hr/>

> Chainlit is an open-source Python package 
> to *build production ready Conversational AI*.

### Key features

- **Build fast**: Integrate seamlessly with an existing code base or start from scratch in minutes
- **Copilot**: Embed your chainlit app as a Software Copilot
- **Data persistence**: Collect, monitor and analyze data from your users
- **Visualize multi-steps reasoning**: Understand the intermediary steps that produced an output at a glance
- **Iterate on prompts**: Deep dive into prompts in the Prompt Playground to understand where things went wrong and iterate

https://docs.chainlit.io/get-started/overview

<!-- slide vertical=true -->

### [Deep Dive] Chainlit integration with LangChain

<hr/>

> There are reference example code to integrate Chainlit with LangChain

<img src='https://i.imgur.com/MacFO00.jpg' height='640'>

https://docs.chainlit.io/integrations/langchain

<!-- slide -->

## Agenda

<hr/>

<table><tr>
<td>

- **What** is the Business Need?
    - <font color="lightgreen">Hospital Price Transparency</font>
- **Why** building AI Chatbot?
    - Will <font color="hotpink">AI Chatbot</font> be the "new" UI?
    - <font color='lightblue'>Multilingual</font> Support?
- **How**
    - High-level Architecture
    - POC Implementation
</td>
<td>

- **Deep Dive**
    - OpenAI
    - LangChain
    - Chainlit
- **Lesson Learnt** <---- *NEXT*
    - Limitation of LangChain and LocalAI
    - Chainlit Local Cache - SQLite
- **Future Plan**
    - Serverless Architecture
    - Different RAG implimentation
    - Interacting with APIs with LangChain
</td>
</tr></table>

<!-- slide vertical=true -->

## [Learnt] Limitations of LangChain and LocalAI

<hr/>

### Lesson #1: Prompt Observability

> with Chainlit, you can see the `prompt` created by *LangChain* 
> and the `response` from *OpenAI GPT-3.5/4 LLM*

<img src='https://i.imgur.com/JXPERcZ.jpeg' height='640'>


<!-- slide vertical=true -->

### Lesson #2: `GPT4All-J` can't *code* like `GPT-3.5-Turbo`

<hr/>

> *Question:* *which is better?* `Multimodal LLM` vs `Code LLM`?

- **TODO:** explore `Meta's Code Llama-2` LLM

<img src='https://i.imgur.com/M2gFw8x.jpeg' height='640'>

Source: https://huggingface.co/codellama

<!-- slide vertical=true -->

### Lesson #3: Impact of Database Schema

<hr/>

> What if LLM can't understand the meaning of Schema?

<img src='https://i.imgur.com/Xa9rhab.png' height='640'>

<!-- slide vertical=true -->

## [Learnt] Chatlit Local Cache - SQLite

<hr/>

> Chainlit can store user's question into SQLite.
> It helps to reduce the cost of OpenAI API usages.
> You can also use it to analyze user's question and answers saved.

<img src='https://i.imgur.com/RlrYGWi.jpeg' height='640'>

https://docs.chainlit.io/data-persistence/history

<!-- slide -->

## Agenda

<hr/>

<table><tr>
<td>

- **What** is the Business Need?
    - <font color="lightgreen">Hospital Price Transparency</font>
- **Why** building AI Chatbot?
    - Will <font color="hotpink">AI Chatbot</font> be the "new" UI?
    - <font color='lightblue'>Multilingual</font> Support?
- **How**
    - High-level Architecture
    - POC Implementation
</td>
<td>

- **Deep Dive**
    - OpenAI
    - LangChain
    - Chainlit
- **Lesson Learnt**
    - Limitation of LangChain and LocalAI
    - Chainlit Local Cache - SQLite
- **Future Plan** <---- *NEXT*
    - Serverless Architecture
    - Different RAG implimentation
    - Interacting with APIs with LangChain
</td>
</tr></table>

<!-- slide vertical=true -->

## [Future] Serverelss Architecture

<hr/>

- **Serverless Architecture**: Use AWS Lambda instead of AWS EC2
    - reduce operation cost

<img src='https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8y5ecpzy0l02syss96zg.png' height='640'>

Source: [How to Create a FREE Custom Domain Name for Your Lambda URL - A Step by Step Tutorial](https://dev.to/omarcloud20/how-to-create-a-free-custom-domain-name-for-your-lambda-url-a-step-by-step-tutorial-47jl)

<!-- slide vertical=true -->

## [Future] Different RAG implimentation

<hr/>

> **R**etrieval-**A**ugmented **G**eneration (RAG)

<img src='https://i.imgur.com/epDCuMm.jpeg' height='640'>

Source: [RAG Cheatsheet V2.0 🚀](https://www.linkedin.com/feed/update/urn:li:activity:7164902842330275840/), Steve Nouri, 2024-02-18 

<!-- slide vertical=true -->

### [Future] Interacting with APIs with LangChain

<hr/> 

- <font color='hotpink'>Common Enterprise Software InfoSec Pratice</font>: 
Application (backend API) subnet is different from database subnet.
(*Data Security*)
- You can share **OpenAPI (Swagger contract)** with LangChain. 
It helps to reduce internal data leaking. (*Data Privacy*)
> sharing `Interface` instead of `Data`

<img src='https://i.imgur.com/r5lFiln.png'  height='480'>

Source: https://python.langchain.com/docs/use_cases/apis

<!-- slide -->

## Part 1 - Q & A

> <p><h3><b>Learn</b> by <code>Doing</code></h3></p>

|||
|---|---|
| <h4>Building <font color='lightgreen'>Hospital Price Transparency</font> <font color="hotpink">Chatbot</font><br/> with `OpenAI`, `LangChain` and `Chainlit`</h4> <br/>Contact [Jazz Yao-Tsung Wang](https://jazzwang.github.io/cv/) <br/>https://www.linkedin.com/in/jazzwang/ | ![Jazz Wang](https://jazzwang.github.io/cv/assets/images/profile.jpg)|

<!-- slide -->

### [ Part 2 ]

## 從 Hadoop.TW (2008) 到 TDEA (2017) - <br/><del>興衰演化</del> <font color="hotpink">八卦時間</font>

|||
|---|---|
| <br/><h4><a href='https://www.facebook.com/opensource4you/posts/pfbid02sKQhB1vJf9euxwPTY7WDHceVt87Ngtsii6o7oDWFetUhEjDcsAmyc4vRbDd5b4nvl' target='_blank'>源來適你 #OpenSource4You。科技開講 TechTalk</a><p/> 2024-09-14 @ HsinChu City, Taiwan</h4> <br/>By [Jazz Yao-Tsung Wang](https://jazzwang.github.io/cv/) <br/>Sr. Director, Heaad of Delivery, Innova Solutions<br/>Chairman, Taiwan Data Engineering Association | ![Jazz Wang](https://jazzwang.github.io/cv/assets/images/profile.jpg)|

<!-- slide -->

## 嘉平說重點是 <font color="hotpink">『八卦』</font>

<hr/>

### 您如果想看 2018 年之前的歷史，請參考

<table><tr>
<td>

* [2016-12-05 - <br/> Hadoop 生態系十年回顧與未來展望](https://www.slideshare.net/slideshow/hadoop-69818883/69818883)

<img src="https://image.slidesharecdn.com/16-12-05hadoop-161205030501/75/Hadoop-3-2048.jpg" height='720'>
</td>
<td>

* [2018-04-26 - <br/> My journey of Innovation 我的創新之旅](https://www.slideshare.net/slideshow/my-journey-of-innovation/95062230#21)

<img src="https://image.slidesharecdn.com/myjourneyofinnovation-180426054418/75/My-journey-of-Innovation-44-2048.jpg"  height='720'>

</td>
</tr></table>

<!-- slide -->

## Hadoop.TW 現況：DNS 網域 2023 年被搶走了

<hr/>

### 當然， `Apache Hadoop` 已經沒有 `Apache Spark` 那麼熱門。

<table><tr>
<td>
<pre>
# whois.twnic.net.tw

Domain Name: hadoop.tw
   Domain Status: clientTransferProhibited
   Registrant:
    TUBOSCOPE LTD
    m.ponomarenko@futurragroup.com
    CY
    (Redacted for privacy)
   Record expires on 2024-10-16 18:52:26 (UTC+8)
   Record created on 2023-10-16 18:52:26 (UTC+8)
   Domain servers in listed order:
      ns1.alidns.com     （阿里雲）
      ns2.alidns.com     
Registration Service Provider: Dynadot LLC
Registration Service URL: https://www.dynadot.com/
</pre>
</td>
<td>
<img src='https://i.imgur.com/JTcZ3UT.png' height='640'>

Souce: https://hadoop.tw

</td>
</tr></table>



<!-- slide -->

## TDEA 過去：高大上的願景 :P

<hr/>

#### 歷史：[2017-07-11 社群、協會、國際連結](https://www.slideshare.net/slideshow/ss-77743104/77743104)

<img src='https://image.slidesharecdn.com/myjourneyofinnovation-180426054418/75/My-journey-of-Innovation-77-2048.jpg' height='720'>

<!-- slide -->

## TDEA 成立的荊棘

<hr/>

<img src='https://image.slidesharecdn.com/myjourneyofinnovation-180426054418/75/My-journey-of-Innovation-81-2048.jpg' height='720'>

<!-- slide -->

## TDEA 現況：待改選第二屆理監事

<hr/>


<img src='https://i.imgur.com/ZMLZgqU.png' height='720'>

Source: https://grouptw.moi.gov.tw/searchGroup

<!-- slide -->

## Part 2 - Q & A

> <p><h3>『 社會實驗 』仍在繼續 『 進行中 』</h3></p>

|||
|---|---|
| <h4>從 Hadoop.TW (2008) 到 TDEA (2017) - <br/><del>興衰演化</del> <font color="hotpink">八卦時間</font></h4> <br/>Contact [Jazz Yao-Tsung Wang](https://jazzwang.github.io/cv/) <br/>https://www.linkedin.com/in/jazzwang/ | ![Jazz Wang](https://jazzwang.github.io/cv/assets/images/profile.jpg)|
