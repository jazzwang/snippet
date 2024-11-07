# Github Models

## 2024-11-06

- ( 2024-11-06 12:22:43 )
- 緣起：
  - 在 https://youtu.be/hE_CeOUY2h0?si=3AtoX7AeJSwRRP25&t=470 看到 Github Model Free GPT-4o 可以用。來研究一下。
  - 參考：https://blog.stoeng.site/20241104.html

- https://docs.github.com/en/github-models
- 啟用：因為我已經有裝 Github CLI ，也已經完成 `gh auth login` 身份認證了，看起來比較簡單的是啟用 [GitHub Models Copilot Extension](https://github.com/marketplace/models-github).
 - 參考：https://docs.github.com/en/github-models/integrating-ai-models-into-your-development-workflow#installing-the-extension
```bash
jazzw@JazzBook:~/git/snippet/md/github$ gh extension install https://github.com/github/gh-models
✓ Installed extension https://github.com/github/gh-models
jazzw@JazzBook:~/git/snippet/md/github$ gh extension list
NAME       REPO              VERSION
gh models  github/gh-models  v0.0.5
```
- ( 2024-11-06 13:35:26 )
- 挺有趣的，居然已經有 500 個以上的 Github extension
```
jazzw@JazzBook:~/git/snippet/md/github$ gh extension
GitHub CLI extensions are repositories that provide additional gh commands.

The name of the extension repository must start with `gh-` and it must contain an
executable of the same name. All arguments passed to the `gh <extname>` invocation
will be forwarded to the `gh-<extname>` executable of the extension.

An extension cannot override any of the core gh commands. If an extension name conflicts
with a core gh command, you can use `gh extension exec <extname>`.

For the list of available extensions, see <https://github.com/topics/gh-extension>.


USAGE
  gh extension [flags]

ALIASES
  gh extensions, gh ext

AVAILABLE COMMANDS
  browse:      Enter a UI for browsing, adding, and removing extensions
  create:      Create a new extension
  exec:        Execute an installed extension
  install:     Install a gh extension from a repository
  list:        List installed extension commands
  remove:      Remove an installed extension
  search:      Search extensions to the GitHub CLI
  upgrade:     Upgrade installed extensions

INHERITED FLAGS
  --help   Show help for command

LEARN MORE
  Use `gh <command> <subcommand> --help` for more information about a command.
  Read the manual at https://cli.github.com/manual
  Learn about exit codes using `gh help exit-codes`

jazzw@JazzBook:~/git/snippet/md/github$ gh ext browse
```
- `gh ext browse` 這個 Text UI 真的有打到重度文字界面愛好者的點 :)
![]()
```bash
jazzw@JazzBook:~/git/snippet/md/github$ gh ext search usage
Showing 3 of 3 extensions

  REPO                       DESCRIPTION
  codiform/gh-actions-usage  GitHub CLI Extension to display Github Actions Usage. Go version of gh-actuse.
  geoffreywiseman/gh-actuse  GitHub CLI Extension to display Github Actions Usage
  ssulei7/gh-runner-usage    A GH extension to calculate average minutes consumed by a runner across workflows across an entire organization.

jazzw@JazzBook:~/git/snippet/md/github$ gh ext exec models
GitHub Models extension

ℹ︎ Azure hosted. AI powered, can make mistakes. Not intended for production/sensitive data.
For more information, see https://github.com/github/gh-models

Usage:
  gh models [command]

Available Commands:
  completion  Generate the autocompletion script for the specified shell
  help        Help about any command
  list        List available models
  run         Run inference with the specified model
  view        View details about a model

Flags:
  -h, --help   help for models

Use "gh models [command] --help" for more information about a command.
```
- ( 2024-11-06 13:44:28 )
- 那看起來 `gh models` 等於 `gh ext exec models`
- 我們來列一下目前 Github Models 有哪些模型吧！
```bash
jazzw@JazzBook:~/git/snippet/md/github$ gh models list

Showing 32 available chat models

DISPLAY NAME                    MODEL NAME
AI21 Jamba 1.5 Large            AI21-Jamba-1.5-Large
AI21 Jamba 1.5 Mini             AI21-Jamba-1.5-Mini
Cohere Command R                Cohere-command-r
Cohere Command R 08-2024        Cohere-command-r-08-2024
Cohere Command R+               Cohere-command-r-plus
Cohere Command R+ 08-2024       Cohere-command-r-plus-08-2024
JAIS 30b Chat                   jais-30b-chat
Llama-3.2-11B-Vision-Instruct   Llama-3.2-11B-Vision-Instruct
Llama-3.2-90B-Vision-Instruct   Llama-3.2-90B-Vision-Instruct
Meta-Llama-3-70B-Instruct       Meta-Llama-3-70B-Instruct
Meta-Llama-3-8B-Instruct        Meta-Llama-3-8B-Instruct
Meta-Llama-3.1-405B-Instruct    Meta-Llama-3.1-405B-Instruct
Meta-Llama-3.1-70B-Instruct     Meta-Llama-3.1-70B-Instruct
Meta-Llama-3.1-8B-Instruct      Meta-Llama-3.1-8B-Instruct
Ministral 3B                    Ministral-3B
Mistral Large                   Mistral-large
Mistral Large (2407)            Mistral-large-2407
Mistral Nemo                    Mistral-Nemo
Mistral Small                   Mistral-small
OpenAI GPT-4o                   gpt-4o
OpenAI GPT-4o mini              gpt-4o-mini
OpenAI o1-mini                  o1-mini
OpenAI o1-preview               o1-preview
Phi-3-medium instruct (128k)    Phi-3-medium-128k-instruct
Phi-3-medium instruct (4k)      Phi-3-medium-4k-instruct
Phi-3-mini instruct (128k)      Phi-3-mini-128k-instruct
Phi-3-mini instruct (4k)        Phi-3-mini-4k-instruct
Phi-3-small instruct (128k)     Phi-3-small-128k-instruct
Phi-3-small instruct (8k)       Phi-3-small-8k-instruct
Phi-3.5-mini instruct (128k)    Phi-3.5-mini-instruct
Phi-3.5-MoE instruct (128k)     Phi-3.5-MoE-instruct
Phi-3.5-vision instruct (128k)  Phi-3.5-vision-instruct
```
- ( 2024-11-06 13:45:25 )
```bash
jazzw@JazzBook:~/git/snippet/md/github$ gh models view gpt-4o
Display name:            OpenAI GPT-4o
Model name:              gpt-4o
Publisher:               OpenAI
Summary:                 OpenAI's most advanced multimodal model in the GPT-4 family. Can handle both text and image inputs.
Context:                 up to 131072 input tokens and 16384 output tokens
Rate limit tier:         high
Tags:                    multipurpose, multilingual, multimodal
Supported input types:   text, image, audio
Supported output types:  text
Supported languages:     English, Italian, Afrikaans, Spanish, German, French, Indonesian, Russian, Polish, Ukrainian, Greek, Latvian, Chinese,
Arabic, Turkish, Japanese, Swahili, Welsh, Korean, Icelandic, Bangla, Urdu, Nepali, Thai, Punjabi, Marathi, Telugu

License:                 custom
License description:     Use of Azure OpenAI Service is subject to applicable Microsoft
Product Terms https://www.microsoft.com/licensing/terms/welcome/welcomepage including the Universal License Terms for
Microsoft Generative AI Services and the service-specific terms for the Azure OpenAI product offering.

Description:             GPT-4o offers a shift in how AI models interact with multimodal inputs. By seamlessly combining text, images, and audio,
GPT-4o provides a richer, more engaging user experience.

Matching the intelligence of GPT-4 Turbo, it is remarkably more efficient, delivering text at twice the speed and at half
the cost. Additionally, GPT-4o exhibits the highest vision performance and excels in non-English languages compared to
previous OpenAI models.

GPT-4o is engineered for speed and efficiency. Its advanced ability to handle complex queries with minimal resources can
translate into cost savings and performance.

The introduction of GPT-4o opens numerous possibilities for businesses in various sectors:

1Enhanced customer service: By integrating diverse data inputs, GPT-4o enables more dynamic and comprehensive customer
support interactions.
2Advanced analytics: Leverage GPT-4o's capability to process and analyze different types of data to enhance decision-
making and uncover deeper insights.
3Content innovation: Use GPT-4o's generative capabilities to create engaging and diverse content formats, catering to a
broad range of consumer preferences.

Note: updated version 2024-08-06
GPT-4o has been released under a new version 2024-08-06 which brings new functionalities and a larger output size (from
4,096 to 16,384).

In addition to features such as:

Text, image processing
JSON Mode
parallel function calling
Enhanced accuracy and responsiveness
Parity with English text and coding tasks compared to GPT-4 Turbo with Vision
Superior performance in non-English languages and in vision tasks
Support for enhancements

This new version has been trained to support complex structured outputs.

Resources
"Hello GPT-4o" (OpenAI announcement) https://openai.com/index/hello-gpt-4o/
Introducing GPT-4o: OpenAI's new flagship multimodal model now in preview on Azure https://azure.microsoft.com/en-
us/blog/introducing-gpt-4o-openais-new-flagship-multimodal-model-now-in-preview-on-azure/

Notes:                   Model Provider
This model is provided through the Azure OpenAI service.

Relevant documents
The following documents are applicable:

Overview of Responsible AI practices for Azure OpenAI models https://learn.microsoft.com/en-us/legal/cognitive-
services/openai/overview
Transparency Note for Azure OpenAI Service https://learn.microsoft.com/en-us/legal/cognitive-services/openai/transparency-
note

Responsible AI Considerations
GPT-4o has safety built-in by design across modalities, through techniques such as filtering training data and refining
the model's behavior through post-training. We have also created new safety systems to provide guardrails on voice
outputs.

We've evaluated GPT-4o according to our Preparedness Framework https://openai.com/preparedness and in line with our
voluntary commitments https://openai.com/index/moving-ai-governance-forward/. Our evaluations of cybersecurity, CBRN,
persuasion, and model autonomy show that GPT-4o does not score above Medium risk in any of these categories. This
assessment involved running a suite of automated and human evaluations throughout the model training process. We tested
both pre-safety-mitigation and post-safety-mitigation versions of the model, using custom fine-tuning and prompts, to better
elicit model capabilities.

GPT-4o has also undergone extensive external red teaming with 70+ external experts https://openai.com/index/red-teaming-
network in domains such as social psychology, bias and fairness, and misinformation to identify risks that are
introduced or amplified by the newly added modalities. We used these learnings to build out our safety interventions in
order to improve the safety of interacting with GPT-4o. We will continue to mitigate new risks as they're discovered.

We recognize that GPT-4o's audio modalities present a variety of novel risks. Today we are publicly releasing text and
image inputs and text outputs. Over the upcoming weeks and months, we'll be working on the technical infrastructure,
usability via post-training, and safety necessary to release the other modalities. For example, at launch, audio outputs
will be limited to a selection of preset voices and will abide by our existing safety policies.

Content Filtering
Prompts and completions are passed through a default configuration of Azure AI Content Safety classification models to
detect and prevent the output of harmful content. Learn more about Azure AI Content Safety
https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview. Additional classification models and
configuration options are available when you deploy an Azure OpenAI model in production; learn more
https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/content-filter?tabs=warning%2Cuser-prompt%2Cpython-new.

Evaluation:              As measured on traditional benchmarks, GPT-4o achieves GPT-4 Turbo-level performance on text, reasoning, and coding
intelligence, while setting new high watermarks on multilingual, audio, and vision capabilities.

       MODEL       | MMLU | GPQA | MATH | MGSM | DROP | HUMANEVAL
-------------------+------+------+------+------+------+------------
  GPT-4o           | 88.7 | 53.6 | 76.6 | 90.5 | 83.4 |      90.2
  GPT-4T           | 86.5 | 48.0 | 72.6 | 88.5 | 86.0 |      87.1
  GPT-4            | 86.4 | 35.7 | 42.5 | 74.5 | 80.9 |      67.0
  Claude3 Opus     | 86.8 | 50.4 | 60.1 | 90.7 | 83.1 |      84.9
  Gemini Pro 1.5   | 81.9 | --   | 58.5 | 88.7 | 78.9 |      71.9
  Gemini Ultra 1.0 | 83.7 | --   | 53.2 | 79.0 | 82.4 |      74.4
  Llama3 400b      | 86.1 | 48.0 | 57.8 | --   | 83.5 |      84.1

Source: the OpenAI announcement https://openai.com/index/hello-gpt-4o/.
```
- 根據文件說明 [Using the extension](https://docs.github.com/en/github-models/integrating-ai-models-into-your-development-workflow#using-the-extension)，可以從 command line 直接用 `gh models run` 然後選 Model，在純文字模式下跟不同的 Model 對話。
```bash
jazzw@JazzBook:~/git/snippet/md/github$ gh models run
? Select a model: OpenAI GPT-4o
>>> 
```
- ( 2024-11-06 14:02:06 )
- 原本一直找不到該在哪裡取得 API Key
- 好吧，對照 [影片二](https://www.youtube.com/watch?v=Y4UuCmZFJZo) 與 [影片一](https://www.youtube.com/watch?v=hE_CeOUY2h0&t=470s) 後，總算知道這還真是剛 open for public preview 的事情。
  - 2024-08-01: [Introducing GitHub Models: A new generation of AI engineers building on GitHub](https://github.blog/news-insights/product-news/introducing-github-models/)
  - 2024-10-29: [GitHub Models is now available in public preview](https://github.blog/changelog/2024-10-29-github-models-is-now-available-in-public-preview/)
  - 參考說明：https://docs.github.com/en/github-models/prototyping-with-ai-models#experimenting-with-ai-models-using-the-api
  - 要查有哪些模型，首先可以到 https://github.com/marketplace/models
  - 在已經登入 Github 的狀態下，就可以去不同的模型，取得 API Key
    - 例如：https://github.com/marketplace/models/azure-openai/gpt-4o 就可以在右上角選「Playground」試玩，或者「Get API Key」還取得 API Key 透過 [LiteLLM] 當 API Proxy/Gateway 指到微軟的 `GPT-4o` API 去。
- **感嘆：** 好個『養。套。殺』策略 :) [最近 LINE Notify API 也是被嘲諷](https://www.managertoday.com.tw/articles/view/69296)。
  - Source: https://www.instagram.com/1mimi_financial/p/CaG3LmllAqj/?img_index=2
