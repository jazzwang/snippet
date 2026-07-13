# LLM Token Usage Efficiency of different AI Code Agents

## 2026-07-09

- 緣起：同仁分享 Benchmarking Coding Agents on Databricks’ Multi-Million Line Codebase
  - https://www.databricks.com/blog/benchmarking-coding-agents-databricks-multi-million-line-codebase
  - 提到 Pi harness 比較省 token
  <img src='https://www.databricks.com/sites/default/files/inline-images/pareto.png?v=1783530297'>
  <img src='https://www.databricks.com/sites/default/files/inline-images/dumbell.png?v=1783530297'>
- 查證：
  - 是否有其他研究結果也存在類似的結論呢？

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI Mode
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
are there study on token effeciency of different AI Code Agent CLI, such as Claude Code, Github Copilot, OpenClaw, Hermus Agent, Pi Agent, OpenCode?
</td></tr><tr><td>A:</td><td>

Yes, multiple comparative studies, academic benchmarks, and community tests track the token efficiency of these AI command-line interfaces (CLIs). [1, 2]

A foundational study from the [Stanford Digital Economy Lab](https://digitaleconomy.stanford.edu/publication/how-do-ai-agents-spend-your-money-analyzing-and-predicting-token-consumption-in-agentic-coding-tasks/) highlighted that autonomous code agents consume up to 1,000x more tokens than simple code autocomplete tools. This massive burn rate is driven by input context (swapping files, checking errors, and re-reading codebases) rather than output code generation. [3, 4, 5]
Because token efficiency translates directly to project costs and execution speeds, the architecture of an agent CLI heavily determines its token footprint. [6, 7]

### Comparative Breakdown: Token Management Across Agent CLIs

| Agent CLI | Baseline Token Usage Trend | Core Context Management Mechanism | Best Suited For |
|---|---|---|---|
| Pi Agent | 🟢 Lowest (Highly Optimized) | Strict AgentMessage conversion & aggressive history pruning. | Local LLMs and resource-constrained environments. |
| Hermes Agent | 🟡 Medium-Low (Decreases over time) | Automated self-learning loops; condenses actions into lightweight reusable skills. | Long-term automation & routine developer operations. |
| OpenCode | 🟡 Medium (Configurable) | Stripped-down architecture; users must explicitly add tools to avoid system prompt bloat. | Privacy-centric developers using self-hosted open-source models. |
| Claude Code | 🔴 High (Dense reasoning overhead) | 1-million-token window; manages context using structural graph summaries and Grep. | Deep architectural changes & multi-file repository refactoring. |
| OpenClaw | 🔴 High (Unfiltered search loops) | Post-execution truncation; trims oversized tool responses after the token expense is incurred. | Complex cross-model orchestrations with deep customization. |
| GitHub Copilot CLI | Variable (Billing-dependent) | Batching multiple tool requests into single execution threads (copilot-codeact-plugin). | Day-to-day inline assistance and native GitHub workflows. |

### Key Findings on Specific Agents

#### 1. Pi Agent & OpenCode: The Local LLM Champions

In tests evaluating local developer footprints, such as data compiled on the [r/LocalLLM community](https://www.reddit.com/r/LocalLLM/comments/1tebx71/those_who_use_it_why_open_code_over_pi_and_hermes/), Pi Agent consistently emerges as the least token-hungry framework. It uses a specific code architecture (pi-agent-core) that processes internal configurations using custom message structures, converting them to standard LLM tokens only at the absolute boundary of an API call. Similarly, developer benchmarks show that stripping OpenCode down into a custom "minimal agent" layout can slash baseline token consumption by up to 96% by eliminating unnecessary system prompts. [8, 9, 10]

#### 2. Hermes Agent vs. OpenClaw: Structural vs. Reactive Savings

Independent evaluations emphasize a sharp philosophical divide in how these two open-source frameworks manage tokens: [11, 12]

* Hermes Agent features a specialized "Curator" loop. The first time it tackles a problem, token usage is standard. However, it immediately writes its solution into a condensed "Procedural Memory Skill". On subsequent repetitions, it calls that lightweight skill directly, reducing recurring token costs significantly. [12, 13, 14]
* OpenClaw relies on a reactive method. When using code search tools, it frequently dumps unranked, massive chunks of files into the context window. While it utilizes hooks (transformContext) to compress old chat history, it does so after the initial expensive token query has already been executed and billed. [15, 16]

#### 3. Claude Code: Maximizing Context via Knowledge Graphs [17]

While Claude Code boasts a massive 1-million-token context window capable of loading entire repositories, it can easily burn through heavily metered plans during long sessions. To combat this, developers frequently use open-source indexers like Graphify or Code-Graph. These tools map out repository structures into pre-indexed knowledge graphs. Instead of Claude Code scanning whole files to understand codebase relationships, it reads the dense graph guide—cutting ambient token consumption by up to 60%–95%. [18, 19, 20, 21, 22]

#### 4. GitHub Copilot CLI: Message-Based Optimization

Copilot CLI is unique because of its hybrid billing strategy. Historically insulated by flat-rate subscriptions, recent optimization frameworks for Copilot rely heavily on tool collapsing. Using techniques like the `copilot-codeact-plugin`, the CLI strings sequential shell instructions together before querying the backend, avoiding the repetitive token overhead of back-and-forth prompt cycles. [3, 18, 23, 24, 25]

### Hidden Metric: The Clean Code Premium

A notable study by SonarSource quantified a critical human factor in agent efficiency. In a controlled trial of 660 agent execution paths, researchers discovered that clean basecode structures make AI agents roughly 34% more efficient. Well-maintained, modular repositories minimized file-revisitations by the agents, reducing context-window refresh cycles and trimming baseline token overhead by 7% to 8% without any changes to the agent software itself. [26]

Would you like details on how to set up context compression tools for a specific CLI, or are you looking to optimize a local model setup?

[1] [https://medium.com](https://medium.com/@unicodeveloper/10-must-have-clis-for-your-ai-agents-in-2026-51ba0d0881df)
[2] [https://link.springer.com](https://link.springer.com/chapter/10.1007/978-3-032-01402-3_26)
[3] [https://dev.to](https://dev.to/webmaxru/a-practitioners-guide-to-getting-more-value-out-of-ai-coding-agent-quality-token-optimization-3n7j)
[4] [https://digitaleconomy.stanford.edu](https://digitaleconomy.stanford.edu/publication/how-do-ai-agents-spend-your-money-analyzing-and-predicting-token-consumption-in-agentic-coding-tasks/)
[5] [https://davefriedman.substack.com](https://davefriedman.substack.com/p/nobody-reads-the-tokens)
[6] [https://medium.com](https://medium.com/@nprasads/token-efficiency-in-ai-coding-agents-12d4e3b00f00)
[7] [https://medium.com](https://medium.com/@jakenesler/context-compression-to-reduce-llm-costs-and-frequency-of-hitting-limits-e11d43a26589)
[8] [https://www.reddit.com](https://www.reddit.com/r/LocalLLM/comments/1tebx71/those_who_use_it_why_open_code_over_pi_and_hermes/)
[9] [https://zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/2043727154320499415)
[10] [https://www.youtube.com](https://www.youtube.com/watch?v=FX7jcd3GYtI&t=439)
[11] [https://latenode.com](https://latenode.com/blog/openclaw)
[12] [https://www.linkedin.com](https://www.linkedin.com/posts/brandonkellyrx_ai-development-agents-activity-7457082945074429952-Zhzh)
[13] [https://www.youtube.com](https://www.youtube.com/watch?v=86Dfgazdu-0)
[14] [https://www.youtube.com](https://www.youtube.com/watch?v=jOK10k70XWE&t=164)
[15] [https://milvus.io](https://milvus.io/blog/why-ai-agents-like-openclaw-burn-through-tokens-and-how-to-cut-costs.md)
[16] [https://medium.com](https://medium.com/@techlatest.net/openclaw-agent-masterclass-66d6a4f88cd5)
[17] [https://www.instagram.com](https://www.instagram.com/reel/DZUjy7ISS0i/)
[18] [https://www.reddit.com](https://www.reddit.com/r/GithubCopilot/comments/1rttkzw/claude_code_vs_github_copilot_limits/)
[19] [https://kilo.ai](https://kilo.ai/articles/top-ai-coding-agents)
[20] [https://www.instagram.com](https://www.instagram.com/reel/DY0cOXvNI9O/)
[21] [https://www.linkedin.com](https://www.linkedin.com/posts/hafshari_github-juliusbrusseecaveman-why-use-activity-7470677242168098816--XfP)
[22] [https://tech-insider.org](https://tech-insider.org/claude-code-vs-github-copilot-2026/)
[23] [https://www.youtube.com](https://www.youtube.com/watch?v=UMRUu7pjdug)
[24] [https://windowsforum.com](https://windowsforum.com/threads/github-copilot-ai-credits-usage-based-billing-starts-june-1-2026.415470/)
[25] [https://calvinfo.substack.com](https://calvinfo.substack.com/p/the-coding-agent-metagame)
[26] [https://www.developersdigest.tech](https://www.developersdigest.tech/blog/code-cleanliness-affects-ai-coding-agents)

</td></tr>
</table>

## 2026-07-13

- 2026-07-12
  - Claude Code Is Way More Token-Hungry Than OpenCode. We Measured Exactly How Much
  - https://systima.ai/blog/claude-code-vs-opencode-token-overhead 
  - 測驗工具：https://github.com/systima-ai/agentic-coding-tools-comparison