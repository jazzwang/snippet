# AI Code Generator and Code Assistant

- ( 2024-10-24 22:48:39 )
- 2024-08-19: [Magic Quadrant for AI Code Assistants](https://www.gartner.com/doc/reprints?id=1-2IJXRJH7&ct=240816&st=sb)

![](https://www.gartner.com/resources/808000/808075/Figure_1_Magic_Quadrant_for_AI_Code_Assistants.png?reprintKey=1-2IJXRJH7)

## Local Copilots?

- https://github.com/ErikBjare/are-copilots-local-yet - 這個人整理了一些不同的

## VS Code + Codeium

- https://codeium.com/ 
  - 這個先前用起來就感覺不錯，比 TabNine 直覺，又有 Chat。
  - 當然 TabNine 最開始吸引我是 Local Model，不必相依外部網路。
  - 這點也是後續如果想改用 Local LLM 的話，就看 Codeium 擴充套件可否指向 Ollama 自己本機跑的模型。
- https://marketplace.visualstudio.com/items?itemName=Codeium.codeium
  - ( 2024-10-24 23:17:59 )  1,752,792 installs

## VS Code + SourceGraph Cody

- https://github.com/sourcegraph/cody
- https://sourcegraph.com/cody
- https://marketplace.visualstudio.com/items?itemName=sourcegraph.cody-ai
  - ( 2024-10-24 23:17:26 )  410,330 installs

## VS Code + Continue

- https://github.com/continuedev/continue
- https://marketplace.visualstudio.com/items?itemName=Continue.continue
  - ( 2024-10-24 23:18:53 ) 385,358 installs
- [本地模型][指南一] https://www.imaginexdigital.com/post/unlocking-coding-magic-setting-up-your-own-local-llm-in-vs-code
  - VS Code + Continue + Llama.cpp + `Deepseek Coder 7B Instruct GGUF`
  - https://huggingface.co/LoneStriker/deepseek-coder-7b-instruct-v1.5-GGUF/tree/main
- 2024-03-04 [本地模型][指南一] https://pdfcrun.ch/blog/2024-03-04-local-llm-to-replace-copilot/
  - VS Code + Continue + Ollama + `StarCoder2`
  - https://huggingface.co/blog/starcoder2

> Another great thing about Continue is that it indexes your entire codebase, so you can ask the model high-level questions about your codebase, like “Do I use X anywhere?” or “Is there any code written already that does X?”.

- https://www.youtube.com/watch?v=F1bXfnrzAxM
  - VS Code + Continue + LMStudio + Dolphin Mixtral 
- https://www.linkedin.com/pulse/alternatives-github-co-pilot-jay-gangawane-f8qkf/
  - VS Code + Continue + LMStudio + codeqwen-1_5-7b-chat-q4_0
- https://patrickwthomas.net/inline-llm-code-completions-in-vscode-without-github-c/
  - VS Code + Continue + Ollama + codeqwen:code
- https://chriskirby.net/run-a-free-ai-coding-assistant-locally-with-vs-code/
  - VS Code + Continue + LMStudio + Mixtral-8x7B | CodeLlama-7B | OpenHermes-2.5-Mistral-7B
- https://medium.com/@smfraser/how-to-use-a-local-llm-as-a-free-coding-copilot-in-vs-code-6dffc053369d
  - VS Code + Continue + LMStudio + Code Llama 7B — Instruct
- https://medium.com/@soniom2002.os/how-to-set-up-local-ai-code-auto-completion-in-vs-code-with-ollama-647cdb16c298
  - VS Code + Continue + Ollama + starcoder2:3b | llama3
    
## VS Code + AskCodi

- https://www.askcodi.com/docs/extensions/vscode/install

## VS Code + CodeGPT

- https://codegpt.co/
- https://marketplace.visualstudio.com/items?itemName=DanielSanMedium.dscodegpt&ssr=true#overview
  - ( 2024-10-24 23:31:47 ) 1,463,524 installs
- [本地模型] https://blog.codegpt.co/free-and-private-copilot-the-future-of-coding-with-llms-in-vscode-372330c5b163
  - VS Code + CodeGPT + ollama + Mistral / Codellama
- https://joeattardi.dev/steps-for-installing-a-local-ai-copilot-in-visual-studio-code
  - VS Code + CodeGPT + ollama + Code Llama 7B


## VS Code + Github Copilot

- [本地模型] [Running GitHub Copilot VSCode extension against local Code Llama model](https://gist.github.com/Birch-san/666a60eacbd9095902f99874622767be)
  - VS Code + Github Copilot (修改) + ialacol + 

## VS Code + Cline

- ( 2024-11-06 22:26:22 )
- 在 [Aider & Cline + Github Models FREE API : AI Coding with GPT-4O for FULLY FREE IS AMAZING!](https://www.youtube.com/watch?v=Y4UuCmZFJZo) 看到 Cline 的運作情形。
- Git Repo: https://github.com/cline/cline
- VS Code extension:
  - https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev
  - 以前叫做 `Claude Dev`

> Meet Cline, an AI assistant that can use your **CLI** a**N**d **E**ditor.

所以一開始的訴求是可以用 CLI 跟 Editor 互動的 AI assistant。