# id-agent

- Git Repo
  - https://github.com/vostride/id-agent
- Website
  - https://vostride.com/

> Token efficient IDs for AI agents. UUID alternative for the agentic era

## Overview

> Where <mark>UUIDs cost ~23 tokens</mark> and get hallucinated by LLMs, id-agent produces memorable word-based IDs at <mark>~14 tokens with equivalent collision resistance</mark>. The first ID library built for the context window, not the database.
>
> - Human-readable -- word-based IDs that humans and LLMs can actually remember
> - Token-efficient -- every word in the wordlist is exactly 1 BPE token on o200k_base
> - Collision-safe -- configurable entropy from ~12 to ~192 bits
> - Validated inputs -- zod-powered schema validation on all public APIs

## 2026-05-21

- 緣起：Learn from Zhu Lin

Based on the repository, here is the token cost comparison (measured on the `o200k_base` tokenizer used by models like GPT-4o, GPT-4.1, o1, and o3) between traditional UUIDs and `id-agent`:

| **Format** | **Example** | **Avg. Tokens (o200k\_base)** | **Collision Resistance / Entropy** | **Token Savings vs UUID** |
| --- |  --- |  --- |  --- |  --- |
| **UUID v4** | `89b842d9-6df9-4cf4-8db0-9dc3aed3cfd7` | **~23** | 122 bits | \-- |
| **id-agent (10 words)** | *Custom word string* | **~17** | 120 bits | ~6 tokens saved (26%) |
| **id-agent (8 words, default)** | `urd-antes-sorry-pac-dire-total-expire-going` | **~14** | ~96 bits | ~9 tokens saved (39%) |
| **id-agent (5 words)** | `frame-beer-bell-tog-hoot` | **~8** | ~60 bits | ~15 tokens saved (65%) |
| **id-agent (3 words)** | `front-reject-tho` | **~5** | 36 bits | ~18 tokens saved (78%) |

### Why Word-Based IDs are More Efficient

Byte-Pair Encoding (BPE) tokenizers are trained primarily on natural language, meaning short English words are naturally compressed into a single token.

Conversely, random hexadecimal strings like UUIDs split unpredictably and inefficiently. For example, the 18-character string `storm-delta-stone` costs only **4 tokens** (3 words + separators), whereas a random 18-character hex string like `dc193952-186a-4645` balloon to **11 tokens**.