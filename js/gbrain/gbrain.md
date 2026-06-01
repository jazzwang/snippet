# GBrain

- Git Repo
  - https://github.com/garrytan/gbrain

> Garry's Opinionated OpenClaw/Hermes Agent Brain

## 2026-05-28

- 2026-05-26 看到這篇
  - 2026-04-11
  - YC 總裁開源生產級 AI 記憶系統「GBrain」，獨創夢循環機制讓 OpenClaw 具備第二大腦
  - https://www.blocktempo.com/yc-president-garry-tan-open-sources-gbrain-ai-agent-memory-system/
- 2026-05-28 看到這篇
  - https://www.linkedin.com/feed/update/urn:li:activity:7463420156019359744/
![](https://media.licdn.com/dms/image/v2/D4D22AQFvEy4HuhXXNA/feedshare-shrink_800/B4DZ5NlFK8J8Ac-/0/1779418027797?e=1781740800&v=beta&t=Wykwt2LFqjyAAZ_9PJRHqJBk5lgeX3j4wG7uF1TYQ9U)

## 2026-06-01

<table><tr style="background-color:lightyellow;"><td>Q:</td><td>

could you compare 2 Agent Memory tool: GBrain (https://github.com/garrytan/gbrain) and Mempalace (https://mempalaceofficial.com)? try to create side-by-side comparison.

</td></tr><tr style="background-color:lightgreen;"><td>Tool:</td><td>

- Google Gemini App
- Gemini 3.5 Flash (Thinking: Extend)

</td></tr><tr><td>A:</td><td>

Both **GBrain** and **MemPalace** represent cutting-edge approaches to **AI Agent Memory Systems**. While they solve the same core problem---giving AI agents long-term context and perfect recall---they lean on completely opposite engineering philosophies.

**GBrain** is built around **practical minimalism**, leveraging local-first developer tools like Markdown and Git. **MemPalace** is inspired by the **cognitive Method of Loci**, relying on a rigid, highly structured spatial metaphor and literal "verbatim" data preservation to score record-breaking retrieval benchmarks.

### Side-by-Side Comparison

| **Feature / Dimension** | **GBrain (github.com/garrytan/gbrain)** | **MemPalace (mempalaceofficial.com)** |
| --- |  --- |  --- |
| **Creator / Origin** | Garry Tan (President & CEO of Y Combinator) | Enterprise/Open-source advanced research project |
| **Core Philosophy** | **Practical Minimalism / "Second Brain"**Offload agent memory to lightweight, local-first developer files. | **Spatial Architecture / "Memory Palace"**Structure memory into distinct architectural metaphors to optimize semantic indexing. |
| **Storage & Tech Stack** | **Markdown Files + Git Repositories** as the source of truth, backed by **Postgres** for semantic retrieval. | Hierarchical structure spanning **4 layers (L0-L3)**, utilizing Knowledge Graphs with vector search. |
| **Memory Retention** | Commits structural truths to Git; updates are tracked cleanly via code repository history. | **Verbatim Storage (No Decay)**.Permanently keeps all raw text without discarding or fading. |
| **Structural Hierarchy** | Flat or folder-based Markdown structures mapping to personal files. | **Wing $\\rightarrow$ Hall $\\rightarrow$ Room**- *Wing:* Complete multi-tenant/agent isolation.- *Hall:* 5 types (`facts`, `events`, `discoveries`, `preferences`, `advice`).- *Room:* Topic containers. |
| **Key Innovation** | **"Dream Cycle" (夢循環)** background processing and Compiled Truth engine. | **AAAK Compression Dialect** & Temporal Validity Windows for non-destructive change tracking. |
| **Performance / Benchmark** | Optimised for massive localized scale (flawless recall across 10,000+ personal markdown notes). | **LongMemEval:** 96.6% raw R@5 (100% with Haiku rerank).**ConvoMem:** 92.9% (doubling tools like Mem0). |
| **Best For** | Independent developers building local, highly private "mini-AGIs" or personal assistants (e.g., OpenClaw, Hermes). | Multi-agent networks, complex workflows requiring strict agent isolation, and enterprise token-budgeting systems. |

### In-Depth Architectural Breakdown

#### 1\. GBrain: The Developer's Pragmatic Approach

GBrain rejects heavy SaaS overhead and complex, closed-source memory clouds. It views an AI's memory the same way a developer views a codebase: as text files that change over time.

-   **The Git + Postgres Hybrid:** By storing information in standardized Markdown files inside a Git repo, GBrain allows humans and agents to edit memory natively. Postgres sits on top as an efficient indexer/retrieval layer.

-   **The "Dream Cycle" Mechanism:** Instead of constantly calculating embeddings or rewriting databases synchronously during a conversation, GBrain uses an asynchronous background loop (the "Dream Cycle"). This cycle processes raw logs, updates knowledge states, resolves contradictions, and "compiles" the absolute truth back into the repository.

-   **Local Control:** It is purpose-built for local or heavily controlled agents (like OpenClaw). It gives an LLM seamless access to thousands of markdown documents without choking its context window.

#### 2\. MemPalace: The Cognitive Architecture Strategy

MemPalace approaches the token limit problem through strict organization rather than pruning. It maps data to a virtual building to drastically minimize the need for expensive LLM re-ranking steps.

-   **Rigid Spatial Isolation (Wings, Halls, Rooms):** \* **Wings** isolate memory entirely. If you have a specialist code-reviewer agent and an operations agent, they each live in separate "Wings" so their contexts never bleed.

        -   **Halls** act as hardcoded semantic categories. By strictly bucketing an injection into `preferences` or `discoveries`, the retrieval engine bypasses the noise of a flat vector database.

-   **Verbatim Storage vs. Decay:** Many modern memory tools use an Ebbinghaus forgetting curve to artificially "decay" and delete older, unused agent memories to save tokens. MemPalace takes the opposite stance: *never throw away text*.

-   **Token Budgeting via Compression:** Because it saves everything verbatim, MemPalace utilizes its **L0-L3 layout** paired with a specialized **AAAK compression dialect** to manage the agent's token usage, ensuring it stays mathematically efficient over millions of tokens of interaction.

### Summary: Which one should you use?

-   **Choose GBrain if:** You want a private, lightweight, local-first memory setup. It is perfect if your goal is to feed your AI agent a massive existing knowledge base (like an Obsidian or Notion vault of thousands of Markdown notes) and you want your agent's memory to be easily human-readable and trackable via Git commits.

-   **Choose MemPalace if:** You are building a complex, commercial multi-agent framework where agents play different roles (architect, reviewer, user), and you require industry-leading retrieval accuracy (96%+ benchmarks) without paying massive LLM-as-a-judge reranking fees.

</td></tr>
</table>

## 2026-06-02

<table><tr style="background-color:lightyellow;"><td>Q:</td><td>
Agent Memory alternatives to GBrain or Mempalace
</td></tr><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search AI Mode
</td></tr><tr><td>A:</td><td>
Several powerful agent memory alternatives can replace GBrain (known for its opinionated execution logic) or MemPalace (known for structured spatial archiving). The best choice depends on whether a plug-and-play memory layer, a graph-based reasoning system, or a completely local footprint is required. [1, 2, 3, 4]
------------------------------
## 1. The Best General Memory Layers (Plug-and-Play)
These frameworks are highly flexible and serve as an external memory tier that can be bolted onto existing agent architectures. [4, 5, 6]

* Mem0 (Mem-Zero): The primary alternative to standard memory layers. It continuously extracts user preferences, platform behaviors, and organization facts across sessions. It maintains distinct scopes for User, Session, and Agent memory. [7, 8, 9, 10]
* Zep (Powered by Graphiti): Tailored specifically for low-latency conversational AI and production workloads. It uses a temporal knowledge graph where time is a first-class dimension, allowing memories to update naturally over time without clogging the context window. [7, 11, 12, 13, 14]

## 2. Graph & Structure-Driven Frameworks (Advanced Context)
If the exact spatial archiving mechanics of MemPalace are preferred but deeper conceptual reasoning is needed, these frameworks use graph technology. [1, 15]

* Cognee: A prominent memory engine that transforms unstructured text and document flows into a hybrid vector + graph knowledge layer. It enables agents to execute logical cross-session recall and reason through conceptual relationships rather than simple keyword matches. [2, 15]
* Letta (Formerly MemGPT): An entire agent runtime rather than a simple layer. It employs a hierarchical operating-system-like architecture with working memory, short-term context windows, and deep archival storage spaces that agents actively query and write back to. [4, 8, 16, 17, 18]

## 3. Lightweight & Fully Local Alternatives
If running local agents (such as Nous Research's Hermes or OpenClaw) without cloud dependencies or expensive API configurations is preferred, these tools offer light architectures. [2, 3, 19]

* [Mnemosyne](https://github.com/TeleAI-UAGI/Awesome-Agent-Memory): Highly rated by open-source agent developers for its lightweight SQLite-in-process framework. It structures memory using a balanced 50% vector, 30% full-text search, and 20% importance metric. [3, 20]
* Hindsight: An agent memory layer built to learn directly from agent execution logs and interaction feedback. Instead of endlessly gathering notes, it actively updates and overwrites outdated conclusions across execution loops. [2, 3, 21]
* agentmemory: A persistent, fast memory utility designed specifically for AI coding agents that relies on a local vector store + Key-Value system. [2, 22, 23, 24, 25]

------------------------------
## Strategic Comparison Table

| Framework [2, 3, 4, 7, 8, 12, 15, 20, 26, 27, 28] | Primary Strength | Architecture Type | Best Fit For |
|---|---|---|---|
| Mem0 | Cross-session user preferences | External Multi-tier Layer | Rapid MVP & multi-platform user tracking |
| Zep | Temporal awareness (Time tracking) | Graph Store Engine | Long production-grade customer support chat |
| Cognee | Relational & concept linking | Graph + Vector | Deep document knowledge & factual reasoning |
| Letta | Autonomous self-editing memory | OS-style Agent Runtime | Stateful agents doing complex multi-step jobs |
| Mnemosyne | Ultra-fast execution, zero cloud costs | Local In-process SQLite | Local hobbyist deployments or edge computing |

To narrow this down, please let me know what specific agent framework (e.g., LangGraph, CrewAI, or local scripts) you are pairing this with, and whether your agents need to track historical facts or evolving user behaviors. [21, 29]

[1] [https://alexlavaee.me](https://alexlavaee.me/blog/attention-memory-coding-agents/)
[2] [https://github.com](https://github.com/TeleAI-UAGI/Awesome-Agent-Memory)
[3] [https://www.reddit.com](https://www.reddit.com/r/hermesagent/comments/1tms3g6/memory_providers_i_tested_them_all/)
[4] [https://vectorize.io](https://vectorize.io/articles/mem0-vs-letta)
[5] [https://zbrain.ai](https://zbrain.ai/enterprise-ai-development-with-zbrain-agnostic-architecture/)
[6] [https://www.linkedin.com](https://www.linkedin.com/pulse/missing-layer-every-agent-harness-vectorizeio-x2hye)
[7] [https://machinelearningmastery.com](https://machinelearningmastery.com/the-6-best-ai-agent-memory-frameworks-you-should-try-in-2026/)
[8] [https://evermind.ai](https://evermind.ai/blogs/memgpt-alternative)
[9] [https://vectorize.io](https://vectorize.io/articles/mempalace-alternatives)
[10] [https://vectorize.io](https://vectorize.io/articles/zep-alternatives)
[11] [https://powerdrill.ai](https://powerdrill.ai/blog/best-free-ai-memory-tools)
[12] [https://vectorize.io](https://vectorize.io/articles/mem0-vs-zep)
[13] [https://fountaincity.tech](https://fountaincity.tech/resources/blog/agent-memory-knowledge-systems-compared/)
[14] [https://neo4j.com](https://neo4j.com/blog/developer/meet-lennys-memory-building-context-graphs-for-ai-agents/)
[15] [https://machinelearningmastery.com](https://machinelearningmastery.com/the-6-best-ai-agent-memory-frameworks-you-should-try-in-2026/)
[16] [https://machinelearningmastery.com](https://machinelearningmastery.com/the-6-best-ai-agent-memory-frameworks-you-should-try-in-2026/)
[17] [https://atlan.com](https://atlan.com/know/mem0-alternatives/)
[18] [https://python.plainenglish.io](https://python.plainenglish.io/memory-management-strategies-and-tools-for-ai-chatbots-and-agents-77ec9063ed92)
[19] [https://pub.towardsai.net](https://pub.towardsai.net/ai-agent-amnesia-heres-the-open-source-fix-that-works-41a78d1aa834)
[20] [https://www.reddit.com](https://www.reddit.com/r/hermesagent/comments/1tms3g6/memory_providers_i_tested_them_all/)
[21] [https://www.reddit.com](https://www.reddit.com/r/openclaw/comments/1rec2g7/best_memory_frameworks/)
[22] [https://github.com](https://github.com/rohitg00/agentmemory/blob/main/benchmark/COMPARISON.md)
[23] [https://github.com](https://github.com/topics/agentmemory)
[24] [https://www.mindstudio.ai](https://www.mindstudio.ai/blog/hermes-agent-five-pillars-memory-skills-soul-crons)
[25] [https://www.youtube.com](https://www.youtube.com/watch?v=oslSQiHCKUI)
[26] [https://github.com](https://github.com/topoteretes/awesome-ai-memory)
[27] [https://www.reddit.com](https://www.reddit.com/r/AI_Agents/comments/1sva2ww/which_platforms_offer_the_easiest_way_to_manage/)
[28] [https://blog.gazzurelli.com](https://blog.gazzurelli.com/from-predictive-coding-to-digital-brain-the-technology-stack-and-architectural-patterns-part-2-9334d09d08a9)
[29] [https://www.firecrawl.dev](https://www.firecrawl.dev/blog/best-open-source-agent-frameworks)

</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
which one is suitable for a researcher who might focus on multiple domain with linked data
</td></tr><tr><td>A:</td><td>
For a researcher working across multiple domains with heavily linked data, the clear standout choice is Cognee, closely followed by [Zep](https://www.getzep.com/) (powered by Graphiti) as the best alternative. [1, 2]
Traditional vector-based memory layers (like Mem0) collapse complex cross-discipline data into "flat" semantic similarities, which causes cross-domain confusion. A researcher needs graph-driven structures that preserve strict semantic relationships, cross-references, and ontology rules. [2, 3, 4]
------------------------------
## 🥇 The Best Choice: Cognee
Cognee is uniquely optimized for multi-domain research because it replaces standard vector retrieval with an ontology-guided Graph-Vector hybrid pipeline (called ECL: Extract, Cognify, Load). [3, 5]

* Custom Domain Ontologies: You can define strict structural boundaries using Pydantic. If you study Virology in one domain and Machine Learning in another, Cognee validates data using explicit schemas so your agent does not cross-contaminate domain-specific facts. [3, 6]
* Deterministic Multi-Hop Reasoning: Instead of relying on fuzzy text similarities, your agent can traverse explicit data paths (e.g., Protein X $\rightarrow$ Inhibits $\rightarrow$ Virus Y $\rightarrow$ Evaluated By $\rightarrow$ Research Paper Z). [7]
* Massive Document Integration: Cognee natively ingests and maps over 30+ disparate data sources, linking PDFs, audio transcripts, and tabular files into a unified knowledge graph. [6]
* Local Graph Visualization: It includes built-in interactive notebooks so you can visually audit and query the exact relationships your agent has mapped out. [6]

## 🥈 The Alternative: Zep (Powered by Graphiti) [2, 8]
If your multi-domain research is highly chronological (e.g., tracking historical events, evolving medical trials, or changing financial regulations over time), Zep is the superior tool. [9, 10]

* Temporal Graphiti Engine: It treats time as a first-class dimension. Facts are assigned valid_at and invalid_at timestamps, preventing old data from conflicting with new discoveries. [9, 10]
* Dynamic Custom Entity Types: You can programmatically inject custom nodes (e.g., ChemicalCompound, StatuteID) across multiple domains, making cross-referencing structured and business-grade fast. [8, 10]
* Global Observations: Zep reads across the entire graph to surface hidden co-occurrences and structural patterns, looking past simple summaries to give you a true macro perspective. [11]

------------------------------
## Strategic Comparison for Researchers

| Feature Requirement [3, 6, 8, 9, 10, 12] | Cognee | Zep / Graphiti |
|---|---|---|
| Primary Mechanism | Ontology-based Entity Validation | Temporally-aware Knowledge Graph |
| How Data is Linked | Semantic relations & cross-source mapping | Episodic changes & timeline tracking |
| Handling Diverse Data | Excellent for mixed PDFs, tables, & code graphs | Optimized for conversational data + JSON payloads |
| Custom Schemas | High (Supports native Pydantic schemas) | Moderate (Supports Custom Entity Types) |

## Recommendation

* Choose Cognee if your research relies on building an authoritative, complex encyclopedia of interconnected definitions, academic literature, and precise multi-domain logic. [3, 13]
* Choose Zep if your research focuses heavily on a timeline of events, streaming changes, or analyzing how data in different domains shifts over time. [9, 10]

To help you get set up, what kinds of documents or data types (e.g., markdown files, academic PDFs, SQL databases) are you looking to connect? I can provide an initialization pattern for either tool.

[1] [https://evermind.ai](https://evermind.ai/blogs/zep-alternative)
[2] [https://papers.ssrn.com](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6616122)
[3] [https://www.cognee.ai](https://www.cognee.ai/blog/deep-dives/grounding-ai-memory)
[4] [https://arxiv.org](https://arxiv.org/html/2602.05665v1)
[5] [https://medium.com](https://medium.com/@vanitaaiofficial/cognee-powerful-memory-for-ai-agents-in-just-6-lines-of-code-14b0e12b6830)
[6] [https://www.linkedin.com](https://www.linkedin.com/posts/sumanth077_build-dynamic-memory-for-ai-agents-in-just-activity-7378334554169737216-OrHN)
[7] [https://www.linkedin.com](https://www.linkedin.com/posts/jaintarun75_google-adk-agents-activity-7412507547125088256-tfAs)
[8] [https://blog.getzep.com](https://blog.getzep.com/entity-types-structured-agent-memory/)
[9] [https://arxiv.org](https://arxiv.org/html/2501.13956v1)
[10] [https://www.falkordb.com](https://www.falkordb.com/blog/graphiti-falkordb-multi-agent-performance/)
[11] https://www.getzep.com
[12] [https://medium.com](https://medium.com/@whynesspower/complete-guide-to-knowledge-context-graphs-via-zep-graphiti-c6da7ce8b13b)
[13] [https://www.cognee.ai](https://www.cognee.ai/blog/fundamentals/building-blocks-of-knowledge-graphs)

</td></tr>
</table>