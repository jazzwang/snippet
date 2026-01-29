## What you'll learn

-   Create reusable skills using the open standard format and best practices, and compose them to create complex workflows.

-   Build custom skills for code generation and review workflows, data analysis, and research that your agent loads on-demand.

-   Combine skills with MCP and subagents to create powerful agentic systems with specialized knowledge and access to external data sources.

## About this course

Join this new short course on Agent Skills, built in partnership with Anthropic and taught by Elie Schoppik.

Skills are folders of instructions that extend agent capabilities with specialized knowledge. Instead of repeatedly explaining the same workflow, you can package it as a skill so your agent automatically knows what to do. Because skills follow an open standard format, you can build them once and deploy across any skills-compatible agent.

In this course, you'll learn how skills work, explore best practices for creating them, and build skills for different use cases. You'll see skills in action across Claude.ai, Claude Code, the Claude API, and the Claude Agent SDK, and learn how to combine them with MCP and subagents for complex workflows.

**In detail, you'll:**

-   Understand how skills transform general-purpose agents into specialists when needed.
-   Learn the structure of a skill folder, the format of [SKILL.md](http://skill.md/) file, and how skills use progressive disclosure to manage context efficiently.
-   Understand how Agent Skills compares to tools, MCP, and subagents.
-   Explore Anthropic's pre-built skills for Excel, PowerPoint and Skill Creation, and use them with Claude.ai to build a marketing campaign analysis workflow.
-   Create custom skills following best practices: build skills for generating practice questions from lecture notes and analyzing time series data characteristics.
-   Use custom and pre-built skills with the Claude API, by integrating the code execution tool and files API to equip Claude with filesystem access and bash for executing python scripts.
-   Build code generation, review, and testing workflows with Claude Code using skills, and set up subagents equipped with skills for specialized tasks with isolated context.
-   Create a research agent using the Claude Agent SDK that leverages a skill to generate a learning guide for an open-source tool based on its documentation, GitHub repo, and web search.

Whether you're automating code reviews, standardizing data analysis workflows, or building research agents, this course gives you hands-on experience creating skills that make general-purpose agents more reliable and capable.

## Who should join?

Any AI builder who wants to extend agent capabilities with reusable workflows and specialized knowledge.

## Course Outline

10 Lessons・0 Code Examples

-   Introduction
    - Video・2 mins
    - https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/lesson/ldn5c3/introduction
-   Course Materials
    - Reading・1 min
    - https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/lesson/53z7ulp0/course-materials
-   Why Use Skills - Part I
    - Video・11 mins
    - https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/lesson/bv2ekh/why-use-skills---part-i
-   Why Use Skills - Part II
    - Video・8 mins
    - https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/lesson/eg4sac/why-use-skills---part-ii
-   Skills vs Tools, MCP, and Subagents
    - Video・7 mins
    - https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/lesson/9iovmn/skills-vs-tools%2C-mcp%2C-and-subagents
-   Exploring Pre-Built Skills
    - Video・18 mins
    - https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/lesson/cniu9q/exploring-pre-built-skills
-   Creating Custom Skills
    - Video・16 mins
    - https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/lesson/txwyf5/creating-custom-skills
-   Skills with the Claude API
    - Video・17 mins
    - https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/lesson/3sq9za/skills-with-the-claude-api
-   Skills with Claude Code
    - Video・24 mins
    - https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/lesson/cniu9b/skills-with-claude-code
-   Skills with the Claude Agent SDK
    - Video・20 mins
    - https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/lesson/rmykgh/skills-with-the-claude-agent-sdk
-   Conclusion
    - Video・1 min
    - https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/lesson/dea3n4/conclusion
-   Quiz
    - Graded・Quiz・10 mins
    - https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/lesson/shjiq0/quiz

## Instructor

![Elie Schoppik](https://learn.deeplearning.ai/_next/image?url=https%3A%2F%2Fhome-wordpress.deeplearning.ai%2Fwp-content%2Fuploads%2F2025%2F05%2FInstructors-profile-picture-62.png&w=256&q=75)

### Elie Schoppik

Head of Technical Education at [Anthropic](https://www.anthropic.com/)

-----


## Unlocking AI's True Potential: 3 Surprising Revelations About Agent Skills

In the rapidly evolving world of artificial intelligence, we often marvel at the breadth of what large language models can do. From drafting emails to generating code, their generalist capabilities are astounding. But what if you need an AI to truly excel at *your* specific, complex workflows? What if you want it to become a specialist, not just a jack-of-all-trades, without constant hand-holding?

Enter "Agent Skills," a powerful concept that's quietly revolutionizing how we interact with intelligent agents. Built on open standards and designed for reusability, skills are changing the game. We've distilled some of the most impactful and perhaps counter-intuitive insights about this emerging paradigm, offering a glimpse into how AI is becoming more reliable, capable, and, frankly, smarter.

### Skills Aren't Just Features; They're Portable, Open-Standard Folders of Instructions

When you hear "AI skills," you might picture abstract capabilities or sophisticated algorithms hardcoded into a system. The reality, as it turns out, is far more practical and empowering for developers. Skills are defined as "folders of instructions," following an "open standard format." This means they're not black boxes but modular, transparent, and designed for interoperability.

This is a game-changer because it means you can build a skill once and deploy it across various "skills-compatible" agents, much like a plugin or a library. This standard offers a path to democratized agent development, moving away from proprietary, walled-garden approaches.

> "Because skills follow an open standard format, you can build them once and deploy across any skills-compatible agent."

Imagine writing a complex data analysis workflow as a skill, and then having any compliant agent, regardless of its underlying model, execute it flawlessly. This portability drastically reduces duplicated effort and accelerates the development of specialized AI applications.

### Transforming Generalists into On-Demand Specialists

One of the most profound benefits of agent skills is their ability to dynamically alter an agent's expertise. Instead of being perpetually loaded with every conceivable piece of knowledge, an agent can "load" a skill only when it's relevant, effectively transforming from a generalist into a specialist for the task at hand.

Consider a code review agent. Initially, it might have broad programming knowledge. But when presented with a pull request, it could load a "code review skill" tailored to specific best practices, security checks, or framework conventions. This approach avoids overburdening the agent with irrelevant context or requiring a separate, bespoke agent for every niche.

> "Instead of repeatedly explaining the same workflow, you can package it as a skill so your agent automatically knows what to do."

This dynamic specialization is crucial for creating efficient, focused, and adaptable AI systems. It's about empowering agents to intelligently self-configure for optimal performance, leading to more precise outputs and fewer errors.

### Intelligent Context Management Through "Progressive Disclosure"

A perennial challenge in working with large language models is managing the "context window"—the limit on how much information an AI can process at one time. Agent skills introduce a sophisticated solution: "progressive disclosure." This means that information is revealed to the agent only as it becomes necessary, rather than presenting everything upfront.

This intelligent filtering prevents the agent from getting overwhelmed or distracted by irrelevant data, which can degrade performance and increase computational costs. For instance, when analyzing a complex document, a skill might first ask for a summary, then specific sections, and only delve into minute details if explicitly prompted.

This approach is counter-intuitive to the "more data is always better" mindset often prevalent in AI. Instead, it champions a lean, just-in-time information delivery system. It suggests that a more deliberate and structured interaction with information, guided by skills, can lead to more accurate, efficient, and ultimately, more "thoughtful" AI responses.

---

The advent of agent skills marks a significant step forward in making AI agents not just powerful, but also practical and extensible. By embracing open standards, dynamic specialization, and intelligent context management, we're moving beyond simple prompts to building truly intelligent, adaptive systems. As these capabilities become more widespread, how will they reshape the way we design and interact with AI in our daily lives and work?

