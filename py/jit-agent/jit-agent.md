# JIT-Agent Technical Summary

**Repository:** https://github.com/bingreeky/JIT
**Paper:** https://arxiv.org/abs/2608.25593
**Hugging Face:** https://huggingface.co/JIT-Agent

![](https://media.licdn.com/dms/image/v2/D4D22AQGbOC4IgHYQ3A/feedshare-shrink_800/B4DaBncVWgJYAc-/0/1788441876144?e=1790208000&v=beta&t=3zTj0z1WqgnnxaoLNTKMmrcfyN3xutCv8mv1Y3KVuSI)

## 1. Overview

**JIT-Agent** is a *compact meta-agent* that generates an **executable, task‑specific agent harness on the fly**.
Given a task specification, a protocol, a tool/skill registry, and a few retrieved prior harnesses, JIT-Agent emits structured code (rather than free‑form prompts) that wraps any off‑the‑shelf agentic LLM — the **Model‑as‑a‑Harness** paradigm.

Key ideas:

- **Harness = four orthogonal modules** (memory, planning, action, capability orchestration) that conform to shared interfaces in `harness_factory/`.
- **Generation = emitting code**, not free‑form agents. The meta model writes Python modules that instantiate these modules for the target task.
- **Test‑time improvement:** as traces and feedback arrive, the generated harness is revised and stored in an archive. The generator itself stays frozen, so the system *learns at runtime*.
- **Orthogonal to base‑model scaling:** the harness‑generation axis provides a new lever for agent intelligence.

---

## 2. Architecture

```
┌─────────────────────────────────────────┐
│           JIT-Agent (meta-agent)        │
│  ──▶ Task spec, protocol, tool registry│
│  ──▶ Prior harnesses (archive)         │
└─────────────────────┬───────────────────┘
                      │
          emits structured harness code
                      │
┌─────────────────────▼─────────────────┐
│         Execution model (agent loop)  │
│  ──▶ Runs the generated harness       │
│  ──▶ Observes traces, feedback        │
└─────────────────────┬─────────────────┘
                      │
   Revise harness → archive update
```

### Core Modules (defined in `harness_factory/`)

| Module | Responsibility |
|--------|-----------------|
| **Memory** | Stores past observations, retrieved experiences, and context for the agent loop. |
| **Planning** | Generates a step‑by‑step plan or sub‑goals for the current task. |
| **Action** | Maps high‑level decisions to concrete tool calls or API calls. |
| **Capability Orchestration** | Coordinates the other three modules, decides when to halt, handles error recovery, etc. |

Each harness produced by JIT‑Agent is a **Python package** that implements these interfaces, allowing the execution model to run it uniformly regardless of the underlying LLM.

---

## 3. Workflow

1. **Input** – User provides a task description, protocol (e.g., “web search → plan → act”), and a registry of available skills/tools.
2. **Harness Generation** – The *meta model* (configurable via `--meta-model`) reads the input and **generates a harness** (a set of Python modules) using prompts stored in `jit/`. The harness is **structured code** that instantiates the four modules.
3. **Selection** – Candidates may be scored by a *judge* model or via *log‑probability* scoring. The best harness is chosen.
4. **Execution** – The *execution model* (configurable via `--exec-model`) runs the generated harness on the benchmark data. Trajectories, tool calls, and outputs are captured.
5. **Feedback & Archive** – After execution, the system records success/failure metrics and appends the harness (or its components) to the archive for future retrieval.
6. **Iteration** – On subsequent runs, retrieved prior harnesses are fed back into the generator, enabling **progressive improvement** at test time.

---

## 4. Repository Layout (high‑level)

```
jit/                 # meta‑agent: generation / repair prompts, best‑of‑N selection
scripts/             # agent kernel, tools, models, evaluation engine, runners
harness_factory/     # hand‑written harness designs + design write‑ups
benchmark/           # one adapter, config & evaluator per benchmark
dataset/             # benchmark data
```

Each sub‑directory contains its own README with detailed instructions.

---

## 5. Quick Setup

```bash
# 1. Clone
git clone https://github.com/bingreeky/JIT.git
cd JIT

# 2. Create environment (Python 3.11)
conda env create -f environment.yml && conda activate jit
# or: pip install -r requirements.txt

# 3. Credentials
cp .env.example .env   # edit with your API keys
```

**Environment groups** (`.env` keys)

| Group | Keys | Purpose |
|-------|------|---------|
| Execution model | `OPENAI_API_BASE`, `OPENAI_API_KEY`, `EXEC_MODEL` | Runs the generated harness’s agent loop |
| Judge model | `JUDGE_MODEL`, optional `JUDGE_API_*` | Grades produced artifacts |
| Meta model | `META_MODEL`, `META_API_BASE`, `META_API_KEY`, `META_TOKENIZER` | Writes the harness (JIT pipeline only) |
| Tools | `SERPER_API_KEY`, `JINA_API_KEY` | Web search / crawl_page |

**Data fetching (optional)**

```bash
python scripts/check_datasets.py          # check presence per benchmark
bash scripts/fetch_datasets.sh travel     # download a benchmark (~1 GB)
```

---

## 6. Usage Scenarios

| Goal | CLI entry point | Meta model | Selection |
|------|-----------------|-----------|-----------|
| Test a fixed `HarnessFactory` design | `python -m scripts.run_seed_harness` | None | None |
| Use a hosted API as the meta‑agent | `python -m scripts.run_jit` | OpenAI‑compatible API | `judge` |
| Evaluate the JIT checkpoint | `bash scripts/serve_meta_model.sh` then `python -m scripts.run_jit` | Local JIT‑27B | `logprob` |

**Example: Run JIT on `xbench`**

```bash
python -m scripts.run_jit --bench xbench \
    --meta-model openai-gpt-4o \
    --meta-base https://api.openai.com/v1 \
    --selector judge \
    --rollouts 3 --max-samples 5
```

**Key CLI arguments**

- `--bench` / `--dataset-path` – benchmark selection
- `--meta-model`, `--meta-base`, `--meta-key` – harness‑generation model
- `--exec-model`, `--exec-base`, `--exec-key` – execution model
- `--judge-model`, `--judge-base`, `--judge-key` – evaluator
- `--rollouts`, `--meta-temperature` – generation diversity
- `--selector` – `judge` or `logprob`
- `--harness-refs` – use description or code references
- `--max-samples`, `--cases`, `--output` – test‑run control
- `--workers-gen`, `--workers-exec` – concurrency tuning

Supported benchmarks: `xbench`, `deepsearchqa`, `agentif`, `officebench`, `odyssey`, `shopping`, `travel`.

**Output structure (per run)**

```
summary.json        # headline metrics + run config
generate/           # N candidate harnesses per case, prompts & responses
select/             # pick per case, rule that produced it, per‑candidate scores
execute/            # harness that actually ran, its trajectory, performance numbers
```

Re‑running the same command **resumes** completed work; `--skip-generate` / `--skip-select` reuse earlier phases.

---

## 7. Results (high‑level)

- **JIT‑Agent‑27B** (the checkpoint released on Hugging Face) lifts a wide range of backbone agents across *deep research, daily‑work, planning, and workspace* benchmarks.
- The paper’s core finding: *“Building the scaffold turns out to be a trainable, transferable axis of agent intelligence — orthogonal to scaling the base model.”*
- Improvements are observed across all supported benchmarks, with the most significant gains on tasks that benefit from **dynamic harness adaptation** (e.g., multi‑step planning, tool‑rich workflows).

---

## 8. References

- **GitHub:** https://github.com/bingreeky/JIT
- **arXiv paper:** https://arxiv.org/abs/2608.25593
- **Hugging Face:** https://huggingface.co/JIT-Agent
- **HarnessFactory guide:** `harness_factory/README.md`