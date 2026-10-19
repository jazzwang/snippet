# Agent Traces

- 簡介：
  - https://huggingface.co/docs/hub/agent-traces
- 緣起：
  - 先前在研究 [Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF](https://huggingface.co/Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF) 跟 [empero-ai/Qwythos-9B-v2-GGUF](https://huggingface.co/empero-ai/Qwythos-9B-v2-GGUF/) 的時候，看到 fine-tune 的資料集都是用 claude 的 trace 來微調 Qwen 模型，但不懂 trace 是什麼。

## Session Traces Format
 
- https://huggingface.co/docs/hub/session-traces-format

> Agent traces from Claude Code, Codex, and Pi are supported out of the box (see Agent Traces). If you build your own harness, you can make its sessions render in the same viewer by writing them in the Session Trace Simple Format (STS-Format) described below.
>
> The Session Trace Simple Format (STS-Format) is a JSONL file (one JSON object per line) that the Hugging Face Hub detects and renders in its trace viewer. It captures a single agent/chat session as a header line followed by message lines.

> [!NOTE]
> 所以 Pi Agent 存的 JSONL 檔案，就是 Session Trace (Agent Trace)
