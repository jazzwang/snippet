# id-agent

- Git Repo
  - https://github.com/vostride/id-agent
- Website
  - https://vostride.com/

> Token efficient IDs for AI agents. UUID alternative for the agentic era

## Overview

> Where <mark>UUIDs cost ~23 tokens</mark> and get hallucinated by LLMs, id-agent produces memorable word-based IDs at <mark>~14 tokens with equivalent collision resistance</mark>. The first ID library built for the context window, not the database.

> - Human-readable -- word-based IDs that humans and LLMs can actually remember
> - Token-efficient -- every word in the wordlist is exactly 1 BPE token on o200k_base
> - Collision-safe -- configurable entropy from ~12 to ~192 bits
> - Validated inputs -- zod-powered schema validation on all public APIs

## 2026-05-21

- 緣起：Learn from Zhu Lin