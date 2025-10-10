# Claude Code

> Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.

- Git Repo:
  - https://github.com/anthropics/claude-code
- Document:
  - https://docs.anthropic.com/s/claude-code
  - https://docs.anthropic.com/en/docs/claude-code/overview
  - https://docs.anthropic.com/en/docs/claude-code/quickstart
- News:
  - 2025-02-25: 發佈 Claude Code
    - https://www.anthropic.com/news/claude-3-7-sonnet
  - 2025-04-18: Claude Code: Best practices for agentic coding
    - https://www.anthropic.com/engineering/claude-code-best-practices

## 2025-08-26

- 安裝：
  ```bash
  npm install -g @anthropic-ai/claude-code
  ```

## 2025-08-27

- 緣起：
  - 可以讓 Claude Code 支援其他 Local LLM 嗎？
- 解法一：（已失效）
  - https://www.shawnmayzes.com/product-engineering/running-claude-code-with-local-llm/
- 解法二： AnyClaude
  - https://github.com/coder/anyclaude
- 關於 Claude Code 跟 Aider 的一些比較跟討論
  - https://news.ycombinator.com/item?id=43254351
    - https://github.com/ai-christianson/RA.Aid (可以整合 Aider)

## 2025-10-09

- 緣起：
  - 因為看到 Github Spec Kit 支援 Claude Code, Gemini CLI 卻沒有支援 Aider
  - 回到先前想研究 Claude Code 是否支援其他 Local LLM
- 解法三：Term-Code
  - https://github.com/Ishuin/term-code 
  - 2025-03-08
    - From Claude to Ollama: How I Hacked Together an AI Coding Assistant in 2 Days (With Zero TypeScript Knowledge)
    - https://medium.com/@ishu.kumars/from-claude-to-ollama-how-i-hacked-together-an-ai-coding-assistant-in-2-days-with-zero-typescript-712191d6f66e
  - 2025-03-09
    - From Claude to Ollama: Building a Local AI Coding Assistant
    - https://dev.to/ishu_kumar/from-claude-to-ollama-building-a-local-ai-coding-assistant-3c46
- 解法四：
  - https://github.com/musistudio/claude-code-router
- 另類思路：告訴 Claude 用 Ollama + Local LLM 來生成 Web App
  - 2025-06-30
    - From Prompt to Production: Vibe Coding Local AI Apps with Claude + Ollama
    - https://blog.greenflux.us/from-prompt-to-production-vibe-coding-local-ai-apps-with-claude-ollama/