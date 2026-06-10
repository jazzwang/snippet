# agentcookie

- Git Repo
  - https://github.com/mvanhorn/agentcookie

## 2026-06-10

- 緣起：
  - Read from https://www.linkedin.com/feed/update/urn:li:activity:7469967297194024960
- 行動：
  - 看了一下 README.md 看到 [cmux](https://github.com/manaflow-ai/cmux)
  - 有點遲疑，因為似乎只支援 macOS

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI Mode
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
does https://github.com/mvanhorn/agentcookie only support macOS?
</td></tr><tr><td>A:</td><td>

Yes, agentcookie currently only supports macOS on both the source and sink ends.
According to the repository documentation, it relies heavily on system-specific features and architectures that restrict it to Apple machines:

* Source Side: It reads Chrome data on macOS using a native, Keychain-backed decrypt path to handle the operating system's security features.
* Sink Side: It relies deeply on macOS LaunchAgent daemons, Apple Developer ID codesigning conventions, and specific macOS Keychain partition mechanisms (like apple-tool: and teamid:) to securely inject synced session data.

If you would like to look into alternatives or see if they plan to change this, let me know if you want me to:

* Find cross-platform alternatives that handle session syncing for AI agents.
* Search the repository issues or roadmap for any future Linux or Windows support plans.

</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
Find cross-platform alternatives that handle session syncing for AI agents.
</td></tr><tr><td>A:</td><td>

## Agentcookie Alternatives

While agentcookie remains uniquely integrated with macOS security APIs, several excellent cross-platform alternatives let AI agents securely capture, sync, and persist browser sessions across Linux, Windows, and macOS.
These alternatives are categorized below by how they handle the infrastructure. [1] 

### 1. Unified Agent Integration Frameworks (Open-Source) [2, 3, 4] 
If you want to orchestrate cross-platform AI web agents that natively sync and preserve browser states (cookies, localStorage, and sessionStorage) between runs without OS lock-in:

* [browser-use](https://github.com/browser-use/browser-use): A widely popular open-source Python framework designed for AI agent web browsing. It features cross-platform storage_state handling that allows your agent to dump its entire authenticated browser session into a portable JSON state file and reload it instantly on any OS. It also supports direct context hijacking using your real, local Chrome browser profiles. [5, 6, 7, 8, 9] 
* [BrowserAct](https://www.youtube.com/watch?v=WvEILN3NPDY): A free, cross-platform CLI tool built explicitly for AI agents. It circumvents strict OS keychain limitations by using stealth Chromium environments to reuse existing browser sessions and inherit live logins from applications like Google, LinkedIn, or Shopify. [10, 11] 

### 2. Managed & Headless Cloud Browsing APIs
For production deployments where you want your agents running entirely headless in the cloud (often on Linux servers) while perfectly syncing desktop authenticated environments: [12, 13] 

* [Browserbase](https://www.firecrawl.dev/blog/best-browser-agents): A platform purpose-built for AI agents that handles end-to-end persistent browser sessions. It handles cookie and session syncing seamlessly across agent runs, entirely abstracted away from the local host OS, and works as a drop-in replacement for standard automation tools. [1, 14, 15] 
* [Steel](https://fast.io/resources/best-web-browsing-tools-ai-agents/): An open-source browser API focused on enterprise data sovereignty. You can self-host Steel inside your own isolated virtual private cloud (Linux/Docker) to persist session cookies and maintain internal app interactions without leaking auth keys to vendor platforms. [16] 

### 3. Core Multi-Platform Libraries (DIY Engineering)
If you prefer building a custom sync utility like agentcookie but need it to run natively across Linux, Windows, and macOS: [17, 18] 

* [Playwright (Browser Contexts)](https://dev.to/stevengonsalvez/browser-tools-for-ai-agents-part-1-playwright-puppeteer-and-why-your-agent-picked-playwright-k71): The modern standard for AI agent automation. Using standard Python or Node.js scripts, you can pull active cookies using context.cookies() and save them to a platform-agnostic file. Agents running on any other machine can spin up an isolated browser.new_context(storage_state="state.json") to inherit those exact credentials instantly. [19, 20, 21] 
* [Selenium (Netscape Cookie Exporters)](https://gist.github.com/ivansaul/40ad4f23ee375b38654be02631902041): A traditional cross-platform framework that can be combined with simple cookie exporter code (like saving driver.get_cookies() to a Netscape-formatted cookies.txt file) to import authenticated parameters into your AI scripts regardless of the OS. [20, 22] 

### Structural Comparison

| Solution [6, 7, 10, 11, 23] | Portability | Auth Security Mechanism | Primary Use Case |
|---|---|---|---|
| browser-use | Pure Cross-Platform (Python) | Portable storage_state JSON | Custom AI agent task-chaining |
| BrowserAct | Pure Cross-Platform (CLI) | Stealth Chrome Profile Hijacking | Bypassing bot detection & CAPTCHAs |
| Browserbase / Steel | Cloud Infrastructure (Docker/VPC) | Centralized, secure remote session pools | Enterprise scale-out & parallel agents |
| Playwright API | Pure Cross-Platform (Python/JS) | Manual context saving/loading | Building your own custom syncing pipeline |

Would you like to see a script example demonstrating how to capture and load portable session states across platforms using Playwright, or are you looking to integrate session syncing with a specific agent framework like LangChain or CrewAI?

[1] [https://www.firecrawl.dev](https://www.firecrawl.dev/blog/best-browser-agents)
[2] [https://www.linkedin.com](https://www.linkedin.com/posts/rachyljones_marching-off-a-cliff-developers-at-microsoft-activity-7331020523310624768-jnXf)
[3] [https://www.linkedin.com](https://www.linkedin.com/pulse/agent-frameworks-microsoft-vs-openai-servicenow-sid-probstein-qkuye)
[4] [https://www.unily.com](https://www.unily.com/features/ai-agents)
[5] [https://github.com](https://github.com/browser-use/browser-use)
[6] [https://sahilkumar1210.medium.com](https://sahilkumar1210.medium.com/mastering-browser-sessions-with-browser-use-the-backbone-of-reliable-ai-automations-f285e449f661)
[7] [https://sahilkumar1210.medium.com](https://sahilkumar1210.medium.com/mastering-browser-sessions-with-browser-use-the-backbone-of-reliable-ai-automations-f285e449f661)
[8] [https://www.skyvern.com](https://www.skyvern.com/blog/automation-anywhere-alternatives-pricing-reviews/)
[9] [https://www.infoworld.com](https://www.infoworld.com/article/3812644/browser-use-an-open-source-ai-agent-to-automate-web-based-tasks.html)
[10] [https://www.youtube.com](https://www.youtube.com/watch?v=WvEILN3NPDY&t=17)
[11] [https://www.youtube.com](https://www.youtube.com/watch?v=sRUtaZ03vSc&t=473)
[12] [https://www.sim.ai](https://www.sim.ai/blog/openai-vs-n8n-vs-sim)
[13] [https://medium.com](https://medium.com/@sandeepratakonda/salesforce-agent-api-bringing-agentforce-data-cloud-to-your-apps-part-7b2f70d28706)
[14] [https://venturebeat.com](https://venturebeat.com/ai/exclusive-browserbase-launches-headless-browser-platform-that-lets-llms-automate-web-tasks)
[15] [https://browser-use.com](https://browser-use.com/posts/web-agent-authentication)
[16] [https://fast.io](https://fast.io/resources/best-web-browsing-tools-ai-agents/)
[17] [https://www.reddit.com](https://www.reddit.com/r/LocalLLaMA/comments/1jmvsm3/local_gpuaccelerated_ai_characters_with_c_onnx/)
[18] [https://thectoclub.com](https://thectoclub.com/tools/best-goodsync-alternative/)
[19] [https://dev.to](https://dev.to/stevengonsalvez/browser-tools-for-ai-agents-part-1-playwright-puppeteer-and-why-your-agent-picked-playwright-k71)
[20] [https://gist.github.com](https://gist.github.com/ivansaul/40ad4f23ee375b38654be02631902041)
[21] [https://fast.io](https://fast.io/resources/best-headless-browsers-ai-agents/)
[22] [https://thunderbit.com](https://thunderbit.com/blog/top-browser-automation-tools)
[23] [https://appsumo.com](https://appsumo.com/products/browseract/)

</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
</td></tr><tr><td>A:</td><td>
</td></tr>
</table>