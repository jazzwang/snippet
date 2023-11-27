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

## Building <font color='lightgreen'>Hospital Price Transparency</font> <font color="hotpink">Chatbot</font><br/> with `OpenAI`, `LangChain` and `Chainlit`

|||
|---|---|
| <h3>AI Hobbyists Internal Sharing</h3> <br/>By [Jazz Yao-Tsung Wang](https://jazzwang.github.io/cv/) <br/> 2023-07-27 @ Taipei, Taiwan | ![](https://jazzwang.github.io/cv/assets/images/profile.jpg)|

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
    - Chaitlit
- **Findings**
    - Chaitlit Local Cache - SQLite
    - Embedding / Vector Store

</td>
</tr></table>

<!-- slide -->

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

<!-- slide -->

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

<!-- slide -->

## [ WHY ] <font color='lightblue'>Multilingual</font> Support?

<!-- slide vertical=true -->

## [ Pain ] Complex Architecture

<hr/>

<img src='http://www.plantuml.com/plantuml/png/tPNVRjis5CRlzHG7AROcs28wHbEi1hBMQrolnLPxbf7S171fwbXY8v42ITbrNcFFiZtGdcH7j1GbNk8WGtEn6RuGZW-_x_pvcNfZ7JUkpBCWAEX12bbmvU0derSMJH3CzHVOkr1GV_fNfS4BTQ7s-mKNAS9ty84l-S65seDdlyWaTKF3rm70JR6zADK5HD8X_FNx7oHskbOybm9ME0TRXIcMSyKJZ66-XlxWrptW5gAVH-DjgI5tkEAKCtvFOd_ImNVQmDjeyWwSlaH50QvY-12DFe91MsXbaRIBGgh4YmxF0wG4wkjsn_r29eXrm_tp2FR7az7fGTiMejekPcfAF9EuWbDfK3ZeXfsgi6ew931u6nruo-dPra6lFofGHSYDI7tI86hh2khnm-6FVWWz60wcm0Ab7OAfoY5131CVJfqhR8ynIqCEyGlFYmnpZANWMIXqphniTVA6AasXripatBB4S2KTCc7DWlanXf-jLl_ERvTYMylmV5C6z23J-h8iu1BNXqkUbJ5kV3DSE7X6UxiaytsHILHk9kFleNwqA0ow0_gH6mJhjC4OjDeWkcLKRvVCngEeRO4NqeOYvIh157dcKa5IlWcqBFOxPSkkhtzh62lfqjr5JN211fN0thNTPsbus1f95ofqREwtmWO4pk6Bboyx0JJLLiGik70FAP0fjSouSroaEIh7VdXrr3r-mGRHR4FcRDcT6LmUpxgTRcTsHD_Zy4eMxPHgnsOb1brf56mQRrUrcV8c35BHvcZf8CZrhfsv50r2NaqCvWWJOiHMONrBPg4D82b0nPE_3NO3EvwovH4h-1gDzKozNXYTdtI-jV8AJuuwdNzG6pw8xCEQz-549JsIfjfcs-7c_BAgziGWgeOqbzRZQZYNgXxx7HkSdjM5tMT52PGsY2Yjj58by5k9PWrJfBbmX_09xRWwsGG-1PJhXUkZtkisDDUKz9hRjkqeW2O6zzoOrrUrvsFhzbwbt5Nl18WQGa0XnjixgM7P0Gr5br9WlMA79ZzvFnbzV3mmk_LsmlByaRGq7ipwLmMh39u_2IntELsZyZycm6ZrJRSpHUk-AWYjxDUyF1gdrpAk_ihTLq-AGklod-JW3SNBFFiR' height='720'>

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

## [ HOW ] High-level Architecture

<hr/>

<img src='https://mermaid.ink/img/pako:eNplklFvgjAQx7_KpQvBJZo4km2OhyUCLjFxmUbdHsSHAoc0g5aUks0o330FVDTjoVz__99d2rseSCgiJDYxjIPPARhnyoYmBDBVghmaNpgBLdDsX6ufVDIapFiYF1xbuWQZlXtXpELWeXeOYz1ao3NqR6zwV3VUHMf_EUfICGUHPbtD_V1xKePY2W8jx7JeruwCQ8Gjm9MMh08PNyUUSsVukPoorV3VP71UhuFzn8ep-AkTKhWsvBYoymAnaZ7AjPKdm1DGz3UB3N5FhOVi5lFF6x42wn2HTXraZApPEvKoDcabdYFyC4PB63FRYqGY4Edwel8YwHoKA2gKpUydEp2aBLfduE3aXIosV0fwNh858vEUxvPptgUmLU36JEOZURbp-Tcz9EkzW5_YOtSt-_aJvr_maKnEcs9DYitZYp-UeUQVeozqBmTEjmlaaBUjpoR8bx9U866qP4_UtSc?type=png' height='720'>

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

## [ HOW ] POC Implementation

<hr/>


<table><tr>
<td>

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

<!-- slide -->

## OpenAI API

<!-- slide -->

## LangChain - Introduction

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

## LangChain - Modules

<hr/>

- **Model I/O** : *Interface* with language models
- **Data connection** : Interface with application-specific *data*
- **Chains** : Construct *sequences of calls*
- **Agents** : Let chains choose which *tools* to use given high-level directives
- **Memory** : Persist application *state* between runs of a chain
- **Callbacks** : *Log* and stream intermediate steps of any chain

<small>Source: [LangChain Document - Introduction](https://python.langchain.com/docs/get_started/introduction)</small>

<!-- slide vertical=true -->

## LangChain - Model I/O

<hr/>

- **Prompts**: Templatize, dynamically select, and manage model *inputs*
- **Language models**: Make ***calls** to language models* through common interfaces
- **Output parsers**: Extract information from model *outputs*

<img src='https://python.langchain.com/assets/images/model_io-1f23a36233d7731e93576d6885da2750.jpg' height='720'>

<small>Source: [LangChain Document - Model I/O](https://python.langchain.com/docs/modules/model_io/)</small>

<!-- slide vertical=true -->

## LangChain - Data Connection

<hr/>

- **Document loaders**: Load documents from many different sources
- **Document transformers**: Split, convert into Q&A format, drop redundant documents
- **Text embedding models**: Turn *unstructured text* into *vector*
- **Vector stores**: *Store* and search over embedded data
- **Retrievers**: *Query* your data

<img src='https://python.langchain.com/assets/images/data_connection-c42d68c3d092b85f50d08d4cc171fc25.jpg' height='640'>

<small>Source: [LangChain Document - Data connection](https://python.langchain.com/docs/modules/data_connection/)</small>

<!-- slide vertical=true -->

## LangChain - Chains

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

## LangChain - Memory

<hr/>

> By default, `Chains` and `Agents` are **stateless**

LangChain provides memory components in two forms:
- *helper utilities* for managing and manipulating previous chat messages.
- ways to incorporate these utilities into *chains*.

<small>Source: [LangChain Document - Memory](https://python.langchain.com/docs/modules/memory/)</small>

<!-- slide vertical=true -->

## LangChain - Agents

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