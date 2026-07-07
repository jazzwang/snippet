# Edge LLM Leaderboard

## 2026-07-02

- https://huggingface.co/spaces/nyunai/edge-llm-leaderboard

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI mode
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
are there leaderboard of Edge LLM models?
</td></tr><tr><td>A:</td><td>

## Edge LLM Leaderboard

Yes, there are specialized leaderboards designed specifically to rank and evaluate Edge Large Language Models (LLMs). Because edge deployments happen locally on resource-constrained devices, these leaderboards shift their focus from raw cloud intelligence to a balance of size, speed, and hardware-level performance. [1, 2, 3, 4] 
The primary leaderboards and benchmarking resources tracking Edge LLMs include:

### 1. The Edge LLM Leaderboard (by Nyun AI)

This is the most definitive and dedicated leaderboard specifically tracking Edge LLMs. [5, 6] 

* The Platform: Hosted as a [Nyun AI Edge LLM Leaderboard Hugging Face Space](https://huggingface.co/spaces/nyunai/edge-llm-leaderboard). [7] 
* What it Benchmarks: It specifically measures compressed, sub-8B parameter models deployed on real, accessible hardware—starting with popular consumer hobbyist boards like the Raspberry Pi 5. [6] 
* Core Metrics: Unlike standard leaderboards, it ranks models based on hard hardware metrics:
* Prefill Latency (Time to First Token)
   * Decode Latency (Overall Generation Speed)
   * Memory Utilization & Model Size [5, 6] 
* Quantizations Covered: It profiles heavily optimized local model formats running on the llama.cpp framework, focusing on Q8_0, Q4_K_M, and ARM Neon-optimized Q4_0_4_4 formats. [5, 6] 

### 2. Hugging Face Open LLM Leaderboard (Edge Filtering)

While the canonical [Hugging Face Open LLM Leaderboard](https://huggingface.co/open-llm-leaderboard) is famous for tracking massive foundational open-source models, it has been updated with robust data slicing. [8, 9, 10] 

* How to use it: You can use its advanced filters to isolate small/tiny models (typically models in the 1B to 7B parameter range).
* Focus: It ranks these smaller models based on mathematical logic, reasoning, and instruction-following capability (using benchmarks like IFEval, MMLU-Pro, and GPQA). It helps you find which tiny model is the smartest before you compress it for your edge device. [5, 8, 11, 12, 13] 

### 3. LLM-Perf Leaderboard

Maintained by the Hugging Face team, the LLM-Perf Leaderboard serves as a vital cross-reference for edge developers. [8] 

* Focus: It does not measure hardware like a Raspberry Pi directly, but it benchmarks the raw inference speed, throughput (tokens per second), and memory footprint of open-source models under different quantization backends (such as Optimum, ORT, and TensorRT-LLM). [8, 14] 

## Key Edge Metrics to Look For

When reading an Edge LLM leaderboard, standard accuracy percentages take a backseat to physical hardware limits. You will want to filter the tables by: [15] 

* Quantization Level: High-precision models (FP16) rarely fit on the edge. Look for 4-bit (Q4) or 8-bit (Q8) quantized versions which preserve roughly 95%+ of model intelligence while cutting memory needs by up to 75%. [5, 6, 14] 
* Hardware Tier: Be mindful of whether a leaderboard tracks CPU-bound execution (like ARM Cortex architectures on common single-board computers) versus edge NPU/GPU execution (like NVIDIA Jetson hardware). [6, 16] 

Are you planning to deploy an Edge LLM on a specific hardware device (like a Raspberry Pi or NVIDIA Jetson), or are you trying to find the smallest model size that still retains good accuracy? [16, 17, 18] 

[1] [https://osanseviero.github.io](https://osanseviero.github.io/hackerllama/blog/posts/llm_evals/)
[2] [https://huggingface.co](https://huggingface.co/spaces/nyunai/edge-llm-leaderboard)
[3] [https://medium.com](https://medium.com/@adnanmasood/measures-that-matter-correlation-of-technical-ai-metrics-with-business-outcomes-b4a3b4a595ca)
[4] [https://www.ankursnewsletter.com](https://www.ankursnewsletter.com/p/the-past-present-and-future-of-llms)
[5] [https://github.com](https://github.com/ggml-org/llama.cpp/discussions/10865)
[6] [https://www.linkedin.com](https://www.linkedin.com/posts/nyunai_edge-llm-leaderboard-a-hugging-face-space-activity-7274683383190827009-bLKl)
[7] [https://huggingface.co](https://huggingface.co/spaces/nyunai/edge-llm-leaderboard)
[8] [https://dev.to](https://dev.to/suzuki0430/llm-model-selection-made-easy-the-most-useful-leaderboards-for-real-world-applications-27go)
[9] [https://huggingface.co](https://huggingface.co/open-llm-leaderboard)
[10] [https://ithy.com](https://ithy.com/article/top-5-llm-comparison-sites-46zgns54)
[11] [https://www.reddit.com](https://www.reddit.com/r/LocalLLaMA/comments/1f692c8/edge_llm_leaderboard_do_we_need_one/)
[12] [https://huggingface.co](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
[13] [https://dextralabs.com](https://dextralabs.com/blog/best-llm-leaderboard/)
[14] [https://af.net](https://af.net/realtime/llm-leaderboard-2026-ai-model-rankings-benchmarks-and-price-comparison/)
[15] [https://arxiv.org](https://arxiv.org/html/2508.11269v1)
[16] [https://medium.com](https://medium.com/@zlodeibaal/the-ultimate-tier-list-for-edge-ai-boards-running-llms-and-vlms-in-2026-da06573efcd5)
[17] [https://github.com](https://github.com/ggml-org/llama.cpp/discussions/10865)
[18] [https://huggingface.co](https://huggingface.co/spaces/nyunai/edge-llm-leaderboard)

</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
I'm target to compare different LLM for AI Code Agent that can fit in 8GB NVIDIA VRAM
</td></tr><tr><td>A:</td><td>

## Edge LLM Comparison on 8GB NVIDIA GPU

To act as an effective AI Code Agent within 8GB of NVIDIA VRAM, a local Large Language Model (LLM) must have a high instruction-following capability, a solid context window, strong structured output generation (JSON/Tool calling), and a small enough footprint to allow for full GPU offloading. [1, 2]

Because an "Agent" workflow requires the model to read multiple files, execute actions, and loops, filling your entire VRAM with just the model will choke the system once the context window expands.

For an 8GB VRAM constraint, your best options break down into three distinct strategies:

### The Comparative Breakdown

| Model Selection [3, 4, 5, 6, 7] | Architecture & Quantization | Size on Disk / VRAM Footprint | Max Full-GPU Context Window | Agent Strengths & Weaknesses |
|---|---|---|---|---|
| Qwen 3.5 Coder 9B (or Qwen 3 7B/9B variants) | Dense, Q4_K_M GGUF | ~4.7 GB to 5.5 GB | 32K+ Context (Up to 200K possible) | Best Overall: Unrivaled code generation, top frontend layout generation, and excellent native function-calling. |
| DeepSeek R1 Distill Qwen 8B | Dense Reasoning, Q4_K_M GGUF | ~4.8 GB | 16K – 32K Context | Best for Deep Logic: Uses a "Thinking Mode" to reason through complex multi-step bugs before outputting tool calls. |
| Phi-4 Mini (3.8B) | Dense, Q8_0 or FP16 | ~2.3 GB to 3.8 GB | 128K Context | Speed Demon: Lightning fast token execution. Excellent for fast autocomplete or light agents, but struggles with large, multi-file software engineering tasks. |

### The Top Recommendations Explained

#### 1. Qwen 3.5 Coder 9B (Quantized to Q4_K_M) — The Gold Standard [5, 8, 9] 

Hardware benchmarks on 8GB NVIDIA cards (like the RTX 4060/4070) confirm that Qwen's 7B to 9B series models at 4-bit quantization are the absolute best choice for 8GB VRAM. [1, 5, 10, 11] 

* Why it wins for Agents: It fits entirely within VRAM with roughly 2.5 GB to 3 GB left over to handle a sizable context window. It is heavily optimized for agentic coding workflows, achieving high marks on tool calling without breaking the JSON formatting that your agent framework relies on.
* Speed: Delivers an incredibly smooth 54–58 tokens per second on local consumer GPUs when fully offloaded. [3, 5, 12, 13, 14] 

#### 2. DeepSeek R1 Distill Qwen3 8B (Quantized to Q4_K_M) — The Planner

If your agent framework struggles with complex multi-step planning or logical deadlocks, this distilled reasoning model is your best alternative. [3] 

* Why it wins for Agents: Before replying, the model walks through its logic in an internal <think> block. This reduces the chance of the agent generating hallucinated code syntax or writing incorrect file-editing paths. [3, 7, 15] 
* The Catch: Because the model writes out its thoughts, it consumes more tokens per request, meaning your context window will fill up faster than standard models. [16] 

#### 3. Phi-4 Mini 3.8B — The Resource-Saver [17] 

If you are running a heavy frontend framework, multiple Docker containers, and a browser alongside your AI Agent, you might not have a clean 8GB of VRAM available.

* Why it wins for Agents: Sitting at under 3GB of memory usage, it leaves massive headroom for your agent to process massive 128K context files without spilling over into your system RAM. [4, 18, 19] 
* The Catch: It lacks the raw multi-file architectural understanding of Qwen, making it better suited for minor edits and script generation rather than refactoring a whole application.

#### Critical Optimization Tips for 8GB Code Agents

   1. Avoid Mixture of Experts (MoE) Models: You will see a lot of praise for models like Qwen3-Coder-Next (an MoE architecture) or GLM-5.2. While amazing, they require 24GB+ of VRAM. Forcing them onto an 8GB card relies on CPU-offloading, collapsing execution speed down to a grinding 1 to 5 tokens per second—which will cause your AI Agent workflows to time out. [12, 20, 21, 22, 23] 
   2. Use a Light Agent Frontend: Avoid bloated agents that swamp your local LLM with massive pre-prompts. Lightweight terminal tools like Aider are highly recommended by the local community for 8GB setups. Aider works seamlessly with local servers like Ollama or LM Studio and keeps token bloat down. [8, 24, 25, 26, 27] 
   3. Stick to Q4_K_M Quantization: Do not use 8-bit (Q8_0) quants for a 7B/9B model on an 8GB card. A Q8_0 variant will ingest almost all 8GB of your VRAM immediately, leaving zero bytes for the KV Cache (the memory needed to look at your code history), instantly crashing your model the moment you feed it a file longer than 50 lines. [4, 28] 

What Agent Framework or IDE extension (e.g., Aider, Continue.dev, Roo Code) are you planning to run these models through?

[1] [https://www.youtube.com](https://www.youtube.com/watch?v=-koMRSHFnuc)
[2] [https://github.com](https://github.com/Robot-Eyes/flexible-LLM-sharding)
[3] [https://daily.dev](https://daily.dev/blog/best-local-llm-models-run/)
[4] [https://webscraft.org](https://webscraft.org/blog/ollama-na-8-gb-ram-yaki-modeli-pratsyuyut-u-2026?lang=en)
[5] [https://localllm.in](https://localllm.in/blog/best-local-llms-8gb-vram-2025)
[6] [https://pub.towardsai.net](https://pub.towardsai.net/the-ultimate-guide-to-local-llms-for-coding-in-2026-which-model-can-your-machine-actually-run-541b35402e36)
[7] [https://huggingface.co](https://huggingface.co/blog/daya-shankar/open-source-llms)
[8] [https://localllm.in](https://localllm.in/blog/best-local-llms-8gb-vram-2025)
[9] [https://localllm.in](https://localllm.in/blog/best-local-llms-8gb-vram-2025)
[10] [https://www.databasemart.com](https://www.databasemart.com/blog/ollama-gpu-benchmark-rtx4060)
[11] [https://localaimaster.com](https://localaimaster.com/blog/vram-requirements-2026)
[12] [https://www.youtube.com](https://www.youtube.com/watch?v=m3PQd11aI_c&t=26)
[13] [https://www.youtube.com](https://www.youtube.com/watch?v=YAvYCyzJoug&t=180)
[14] [https://arxiv.org](https://arxiv.org/html/2604.13519v2)
[15] [https://medium.com](https://medium.com/@roanmonteiro/the-complete-beginners-guide-to-local-ai-concepts-models-hardware-and-a-working-pipeline-for-4a4b3de7b004)
[16] [https://medium.com](https://medium.com/@amjad.shaikh/ai-in-large-codebase-context-building-enterprise-grade-software-with-ai-coding-assistants-19c0bac87b3c)
[17] [https://www.marktechpost.com](https://www.marktechpost.com/2025/09/27/top-10-local-llms-2025-context-windows-vram-targets-and-licenses-compared/)
[18] [https://www.microcenter.com](https://www.microcenter.com/site/mc-news/article/best-local-llms-8gb-16gb-32gb-memory-guide.aspx)
[19] [https://inventivehq.com](https://inventivehq.com/blog/context-windows-explained-ai-coding)
[20] [https://www.reddit.com](https://www.reddit.com/r/LocalLLaMA/comments/1p2wnh0/which_model_to_choose_for_coding_with_8gb_vram/)
[21] [https://medium.com](https://medium.com/ai-analytics-diaries/top-7-local-llms-that-will-replace-coding-in-2026-a106cc5f5633)
[22] [https://pinggy.io](https://pinggy.io/blog/best_open_source_self_hosted_llms_for_coding/)
[23] [https://whatllm.org](https://whatllm.org/best-local-llm)
[24] [https://www.youtube.com](https://www.youtube.com/watch?v=m3PQd11aI_c)
[25] [https://dev.to](https://dev.to/akash7367/voice-controlled-local-ai-agent-works-even-on-8gb-ram-5goj)
[26] [https://www.augmentcode.com](https://www.augmentcode.com/tools/augment-code-vs-aider-strengths-and-drawbacks)
[27] [https://pinggy.io](https://pinggy.io/blog/best_open_source_self_hosted_llms_for_coding/)
[28] [https://dev.to](https://dev.to/mitchell_cheng/my-learning-notes-choosing-the-right-ai-model-and-hardware-237)

</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
Claude Code CLI
</td></tr><tr><td>A:</td><td>

## Claude Code CLI + Ollama

Running the Claude Code CLI fully locally with an open-source model inside 8GB of NVIDIA VRAM is a popular optimization strategy. [1] 

By default, the Claude Code CLI is built to send requests to Anthropic's cloud endpoints. However, because it reads environment variables to find its base URL, you can intercept its traffic and route it entirely to a local backend like Ollama, LM Studio, or llama.cpp. [1, 2, 3] 

Because Claude Code relies on a dense, multi-step agentic loop (reading terminal output, checking files, and executing shell commands), you must configure your local environment carefully to avoid running out of memory. [1] 

### Step-by-Step Setup: Claude Code CLI + Local 8GB GPU

#### 1. Spin up the Local Backend

You need an inference engine running your quantized 4-bit model to expose an API endpoint. [2, 4] 

* Using LM Studio:
1. Load Qwen 3.5 Coder 9B (Q4_K_M) or DeepSeek R1 Distill Qwen 8B (Q4_K_M).
   2. Set your Context Length to 16,384 or 32,768 (do not go higher initially to prevent VRAM overflow).
   3. Fully offload all layers to your NVIDIA GPU (CUDA).
   4. Start the Local Server (defaults to http://localhost:1234). [2, 5, 6] 
* Using Ollama:
  Run the model in your terminal: [4, 7] 

  ```bash
  ollama run qwen2.5-coder:7b  # (Or your chosen Qwen3 variant)
  ```

#### 2. The Translation Bridge (The Crucial Step)

Claude Code transmits requests formatted for Anthropic's Messages API layout. Local engines like LM Studio or Ollama speak the OpenAI formatting language. You need an open-source adapter proxy to sit between them so the tools/function calling do not break. [2, 5, 8, 9, 10] 
The community uses tools like [fuergaosi233/claude-code-proxy](https://github.com/fuergaosi233/claude-code-proxy) or LiteLLM to translate the commands. [5, 8] 
If using a direct proxy tool, start it up so it listens on a port (e.g., localhost:4000) and targets your back-end port 1234. [5] 

#### 3. Redirect the Claude Code CLI [11] 

Before booting Claude Code, set the environment variables in your terminal to trick the CLI into bypassing Anthropic's cloud servers: [2, 5] 
```bash
# Point this to your proxy port (or direct backend if it supports Anthropic API natively)
export ANTHROPIC_BASE_URL="http://localhost:4000"
export ANTHROPIC_AUTH_TOKEN="local-token-dummy"
# Fire up Claude Code in your project directory
claude
```

(Alternatively, some frontends allow launching directly via commands like ollama launch claude depending on the helper scripts installed). [12, 13] 

#### Important Gotchas for 8GB VRAM + Claude Code

* Watch out for Batch Overlap: Claude Code likes to fire parallel validation checks or background file scans. If it fires two massive files into your 8GB card simultaneously, it will hit an Out of Memory (OOM) crash. If this happens, use smaller codebases or limit the context size in your backend. [10, 13, 14] 
* Tool Formatting is Fragile: Claude Code expects flawless tool-use syntax to read/write files. Qwen 3.5 Coder 9B handles this brilliantly. If you use an unoptimized model, Claude Code will enter a loop where it repeatedly fails to execute bash actions. [1, 14] 
* The "Airplane Mode" Advantage: Running this configuration means you are getting an elite terminal agent executing entirely offline, keeping your proprietary code entirely private. [1, 12] 

Would you like the exact LiteLLM configuration file architecture to map Claude Code's requests over to your local NVIDIA card, or do you need help monitoring the VRAM allocation while it runs? [5] 

[1] [https://codemeetai.substack.com](https://codemeetai.substack.com/p/how-i-run-claude-code-offline-the)
[2] [https://lmstudio.ai](https://lmstudio.ai/blog/claudecode)
[3] [https://code.claude.com](https://code.claude.com/docs/en/network-config)
[4] [https://unsloth.ai](https://unsloth.ai/docs/basics/claude-code)
[5] [https://medium.com](https://medium.com/@luongnv89/setting-up-claude-code-locally-with-a-powerful-open-source-model-a-step-by-step-guide-for-mac-84cf9ab7302f)
[6] [https://www.youtube.com](https://www.youtube.com/watch?v=2B9XgCQlXO8)
[7] [https://www.facebook.com](https://www.facebook.com/groups/timebank.tw/posts/3844908905824214/)
[8] [https://github.com](https://github.com/fuergaosi233/claude-code-proxy)
[9] [https://www.openai-hub.com](https://www.openai-hub.com/news/203/)
[10] [https://www.morphllm.com](https://www.morphllm.com/claude-code-router)
[11] [https://localai.io](https://localai.io/features/mitm-proxy/index.html)
[12] [https://medium.com](https://medium.com/@luongnv89/run-claude-code-on-local-cloud-models-in-5-minutes-ollama-openrouter-llama-cpp-6dfeaee03cda)
[13] [https://www.youtube.com](https://www.youtube.com/watch?v=9cFBVhEqKkE)
[14] [https://medium.com](https://medium.com/@vito.rallo/running-claude-code-with-local-llms-all-lies-until-now-3e9a0084dfe1)

</td></tr>
</table>
