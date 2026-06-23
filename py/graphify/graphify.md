# Graphify

- Git Repo
  - https://github.com/safishamsi/graphify
- Website
  - https://graphifylabs.ai/

> AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, and more). Turn any folder of code, SQL schemas, R scripts, shell scripts, docs, papers, images, or videos into a queryable knowledge graph. App code + database schema + infrastructure in one graph.

## 2026-06-22

- 緣起：
  - learn from Jeriel
- 查過平常訂閱的 Newsletter 只出現在 DevPost 一次
- 比較好奇用什麼 Tech Stack 來存 Knowledge Graph
  - SQLite?
  - Neo4j?

## 2026-06-23

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI Mode
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
could you describe the technical stack of graphify https://graphifylabs.ai/? how does graphify store Knowledge Graph? in SQLite? or Neo4j?
</td></tr><tr><td>A:</td><td>

By default, Graphify does not store its core knowledge graph in a standalone database like SQLite or Neo4j. Instead, it uses NetworkX to construct the graph entirely in-memory and outputs serialized data as portable JSON (`graph.json`) and HTML files (`graph.html`) directly into your project's local directory. [1, 2]
However, Graphify is a highly extensible tool that supports push/sync integrations to external graph platforms like Neo4j and FalkorDB for advanced querying and RAG workloads. [2, 3]

### The Core Technical Stack

Graphify operates as a three-pass local orchestration layer designed to map codebases and context files efficiently without heavy system prerequisites: [4]

-   Parsing Layer ([Tree-sitter](https://tree-sitter.github.io/tree-sitter/)): Parses source code across 20+ programming languages. It extracts Abstract Syntax Trees (AST) locally and deterministically. This pass uses no LLMs or API tokens. [4]
-   Graph Engine ([NetworkX](https://networkx.org/)): The underlying data structure framework. Graphify maps nodes (functions, classes, docs) and edges (dependencies, calls) in-memory inside a NetworkX graph instance. [1, 2, 5]
-   Clustering Engine (Leiden Algorithm): Groups interconnected code paths and concepts into logical structural communities. Unlike traditional RAG tools, it uses structural topology for similarity grouping instead of costly vector embeddings. [4]
-   Semantic Layer (Configured LLM): For non-code assets (PDFs, Markdown, images), it utilizes your AI assistant's existing model API (such as Anthropic Claude or OpenAI) to extract metadata. [4]
-   Transcription Layer (Faster-Whisper): Local audio and video processing for meeting transcripts. [6]

### How Graphify Handles Storage

#### 1. Standard Default Storage: Portable Files

Graphify's local design is optimized to match your Git workflow. When you execute `graphify .`, it writes outputs directly to a local folder (typically `graphify-out/`): [7, 8]

-   `graph.json`: The complete raw snapshot of the structural graph. It maps all relative directory paths so the graph can be committed to Git and immediately shared across team members. [1, 7]
-   `graph.html`: A standalone visualization UI featuring interactive network maps and community clusters. [1, 9]
-   `GRAPH_REPORT.md`: A plain-language text document describing the architecture and "god-nodes" (high impact blast-radii) for the AI assistant to read instantly. [9, 10]

#### 2. Neo4j Integration

Graphify provides built-in sink support to export its extracted snapshot to an instance of Neo4j (such as Neo4j Aura or local Docker instances). This lets you run complex graph traversals, structural path-finding algorithms, and Cypher queries on your codebase. [2, 3, 11]

#### 3. Where SQLite Fits In

Graphify itself does not use SQLite for graph state. However, SQLite often appears alongside Graphify in development environments because: [2]

-   Developers use Graphify alongside complementary plugins like code-review-graph (CRG), which *does* utilize a SQLite-backed AST engine to run local semantic search metrics. [12]
-   Graphify provides documentation blueprints for bundling a SQLite Model Context Protocol (MCP) server alongside its graph toolkit, creating a unified relational + graph workspace for tools like Claude Code. [13]

If you would like to explore setting this up for your project, let me know:

-   What AI assistant or IDE you are integrating it with?
-   Whether your primary codebase files are local or part of a shared team repository?
-   If you plan to scale into millions of edges, which would benefit from turning on the Neo4j or FalkorDB sinks? [2]

[1] [https://medium.com](https://medium.com/@aitoolinsight/graphify-solves-claudes-biggest-limitation-finally-turning-your-codebase-into-a-knowledge-graph-36433a9360f7)
[2] [https://github.com](https://github.com/safishamsi/graphify/issues/1175)
[3] [https://www.youtube.com](https://www.youtube.com/watch?v=HQEm4rBKdec)
[4] [https://medium.com](https://medium.com/how-to-profit-ai/graphify-one-command-turns-any-folder-into-a-knowledge-graph-7b0602b09bee)
[5] [https://graphify.net](https://graphify.net/)
[6] [https://www.youtube.com](https://www.youtube.com/watch?v=BkHps04qGgc)
[7] [https://github.com](https://github.com/safishamsi/graphify?ref=aiposthub.com)
[8] [https://tayipturk.medium.com](https://tayipturk.medium.com/claude-has-no-memory-so-we-built-one-cut-token-costs-70x-with-graphify-obsidian-8efffd8b8ecb)
[9] [https://pi.dev](https://pi.dev/packages/@gaodes/pi-graphify)
[10] [https://github.com](https://github.com/lucasrosati/claude-code-memory-setup)
[11] [https://github.com](https://github.com/cklam12345/wisdomGraph)
[12] [https://dev.to](https://dev.to/mir_mursalin_ankur/graphify-code-review-graph-build-a-self-updating-knowledge-graph-for-claude-code-and-other-ai-j1m)
[13] [https://github.com](https://github.com/safishamsi/graphify/blob/v8/docs/docker-mcp-sqlite.md)

</td></tr>
</table>