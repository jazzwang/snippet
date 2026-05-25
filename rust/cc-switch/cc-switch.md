# cc-switch

- Git Repo
  - https://github.com/farion1231/cc-switch
- Website
  - https://ccswitch.io/

## 2026-05-23

- 緣起
  - 100%免費！Claude Code 跑本地模型，無需 API！免翻牆使用超強AI Agent｜Ollama｜CC Switch｜零度解說
  - https://www.youtube.com/watch?v=6iONJKrFs1k
  - Claude Code + Ollama 太強了！免費本地 AI 開發助手來了！無需 Claude API！｜零度解說
  - https://www.freedidi.com/24192.html
  > 使用 Ollama 本地模型，直接接管 Claude Code。
  > 而實現這一切的核心工具，就是最近很火的：CC Switch
- CC Switch 一键切换 API
  - https://www.runoob.com/ai-agent/cc-switch.html
- ⭐️ A cross-platform CLI All-in-One assistant tool for Claude Code, Codex & Gemini CLI.
  - https://github.com/saladday/cc-switch-cli

## 2026-05-24

<table><tr><td>Q:</td><td>
what's the difference between https://github.com/farion1231/cc-switch and https://github.com/BerriAI/litellm
</td></tr><tr><td>Tool & Model</td><td>
Google Search AI Mode | Gemini 3
</td></tr><tr><td>A:</td><td>
While both tools are designed to simplify how developers manage and switch between different Large Language Model (LLM) API providers, they operate at completely different layers of the software stack. **The main difference is that `cc-switch` is a desktop application for configuring local terminal-based coding tools, whereas `litellm` is a backend code library and proxy server used to connect applications to multiple LLM APIs.**

A detailed breakdown of their unique purposes, targets, and operations includes:

### Direct Comparison Overview

| Feature | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | [BerriAI/litellm](https://github.com/BerriAI/litellm) |
| :-- |  :-- |  :-- |
| **Core Nature** | Cross-platform **Desktop GUI App** (built with Tauri/Rust) | **Python SDK** & Network **Proxy Server** |
| **Primary Target** | Software developers using **AI coding CLI tools** | Software engineers building **AI-powered applications** |
| **How it Works** | Rewrites local configuration files (`.env`, JSON, TOML) | Translates multi-provider APIs into a single OpenAI format |
| **Data Storage** | Local SQLite database (`~/.cc-switch/cc-switch.db`) | No local storage (passed via application code/memory) |
| **Key Capability** | System tray switching, Model Context Protocol (MCP) syncing | Load balancing, budget tracking, and fallback handling |

### [farion1231/cc-switch](https://github.com/farion1231/cc-switch): The Local CLI Configuration Manager

[CC Switch](https://github.com/farion1231/cc-switch) is an All-in-One desktop assistant focused on making life easier for developers who use **terminal-based AI coding agents**.

-   **The Problem It Solves:** Tools like `Claude Code` or `Gemini CLI` require you to manually edit hidden system configuration files or environment variables if you want to switch your backend provider from Anthropic/Google to a cheaper or local alternative (like DeepSeek or a local Ollama instance).
-   **What It Does:** It provides a visual dashboard and a desktop system tray menu. With one click, it automatically handles the back-end configuration files for 5 specific tools: **Claude Code, Codex, Gemini CLI, OpenCode, and OpenClaw**.
-   **Extra Features:** It manages your Model Context Protocol (MCP) servers, syncs custom AI prompt markdowns, and lets you back up configurations to cloud providers like Dropbox or iCloud.

### [BerriAI/litellm](https://github.com/BerriAI/litellm): The Universal API Gateway

[LiteLLM](https://github.com/BerriAI/litellm) is a backend developer tool designed to sit between an application you are building and over 100+ LLM APIs.

-   **The Problem It Solves:** If you write code to call OpenAI, your code uses `openai.chat.completions.create`. If you want to use Anthropic, you have to rewrite your code using the `anthropic` SDK.
-   **What It Does:** It acts as a translator. You write your backend application entirely using OpenAI's format, and LiteLLM intercepts the request and instantly dynamically translates it to AWS Bedrock, HuggingFace, Azure, Cohere, or any other provider.
-   **What It Does (Proxy Mode):** It can be deployed as a live network proxy server. Your apps send web requests to `litellm`, and it handles enterprise features like **load-balancing across multiple API keys**, setting spend budgets for users, tracking token usage, and automatic failover routing if an API goes down.

* * * *

### Summary of When to Use Which

-   Use **`cc-switch`** if you are a programmer looking for a quick graphical way to change API keys and presets for your terminal coding assistants without manually digging into hidden configuration files.
-   Use **`litellm`** if you are writing a piece of software (like a web app or web bot) and you want your software to seamlessly call multiple LLM providers using a single unified coding framework.

To help me give you more relevant details, are you looking to **configure your own local development environment**, or are you **building a software application** that needs to connect to different AI models?
</td></tr></table>