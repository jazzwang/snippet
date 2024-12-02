# Verilog

- https://zh.wikipedia.org/zh-tw/Verilog

## 用 LLM 進行 Verilog 晶片設計的相關文章

| Publish Date | Link                                                                                                      |
|--------------|-----------------------------------------------------------------------------------------------------------|
| 2023-06-19   | [用 ChatGPT 設計一顆晶片](https://www.xktang.com/article/182)                                            |
| 2023-10-30   | [Silicon Volley: Designers Tap Generative AI for a Chip Assist](https://blogs.nvidia.com/blog/llm-semiconductors-chip-nemo/) |
| 2023-12-19   | [AI Is Reshaping Chip Design. But Where Will It End?](https://cambrian-ai.com/ai-is-reshaping-chip-design-but-where-will-it-end/) |
| 2024-01-11   | [LLMs and the Future of Chip Design: Unveiling Security Risks and Building Trust](https://arxiv.org/pdf/2405.07061v1) |
| 2024-08-26   | [LLMs, autonomous AI agents speed up Nvidia chip design](https://www.eenewseurope.com/en/llms-autonomous-ai-agents-speed-up-nvidia-chip-design/) |
| 2024-08-26   | [IBM Presents Advanced AI Chip Tech at Hot Chips 2024](https://www.hpcwire.com/off-the-wire/ibm-presents-advanced-ai-chip-tech-at-hot-chips-2024/) |
| 2024-10-16   | [AI in Chip Design: from Basic Tools to LLMs and AI Agents](https://www.sigarch.org/ai-in-chip-design-from-basic-tools-to-llms-and-ai-agents/) |

## Public Data Set ?

there are several public datasets available for Verilog code that can be utilized for training and evaluating large language models (LLMs). Below is a summary of notable Verilog datasets, including their features and where to access them.

| Dataset Name | Description | Key Features | Access Link |
|--------------|-------------|--------------|-------------|
| **MG-Verilog** | A multi-grained dataset designed to enhance LLM-assisted Verilog code generation. | Contains natural language descriptions for each Verilog code sample, automated dataset generation flow, and supports fine-tuning of LLMs. | [GitHub Repository](https://github.com/GATECH-EIC/mg-verilog) [1][2] |
| **VerilogEval** | A benchmarking dataset for evaluating LLMs in Verilog code generation tasks. | Includes 156 problems covering various complexities, with a focus on functional correctness and syntax validation. | [GitHub Repository](https://github.com/NVlabs/verilog-eval) [3] |
| **Verilog Dataset v2** | A collection of Verilog modules generated from natural language prompts. | Contains diverse examples including complex designs like SHA-256 digester and AXI processing systems. | [Hugging Face Dataset](https://huggingface.co/datasets/emilgoh/verilog-dataset-v2) [5] |
| **GitHub Verilog Corpus** | A large corpus of open-source Verilog code gathered from GitHub repositories. | Comprises approximately 50,000 files with a focus on high-quality, syntactically correct Verilog code. | Not directly linked; referenced in academic papers [4] |

These datasets provide a valuable resource for researchers and developers working on LLMs for Verilog code generation. They encompass a range of examples and benchmarks that can be used to evaluate the performance of models trained on Verilog tasks, contributing to advancements in automated hardware design.

Citations:
[1] https://responsible.computing.gatech.edu/mg-verilog-won-the-best-paper-award-at-the-first-workshop-on-llm-aided-design/
[2] https://github.com/GATECH-EIC/mg-verilog
[3] https://github.com/NVlabs/verilog-eval
[4] https://par.nsf.gov/servlets/purl/10419705
[5] https://huggingface.co/datasets/emilgoh/verilog-dataset-v2

## Comparison of LLMs for Verilog Design

Several large language models (LLMs) have been developed specifically for Verilog code generation, and benchmarks have been established to evaluate their performance. Below is a comparison table summarizing notable LLMs, their capabilities, benchmarks, and publication timelines.

| **Model/Tool**             | **Description**                                                                 | **Benchmarking Framework**                                 | **Training Dataset**                                            | **Publication Timeline**       | **Reference Links**                                           |
|----------------------------|---------------------------------------------------------------------------------|-----------------------------------------------------------|----------------------------------------------------------------|--------------------------------|--------------------------------------------------------------|
| **CodeGen-16B**            | A large model fine-tuned for improved performance in generating Verilog code.   | Custom evaluation framework with test benches for syntax and functionality.| GitHub and textbooks; fine-tuned on specific tasks.           | 2023-04-19                           | [NSF PDF](https://par.nsf.gov/servlets/purl/10419705)<br/>[IEEE Xplore](https://ieeexplore.ieee.org/abstract/document/10137086) |
| **MEV-LLM**                | Multi-expert architecture designed to enhance Verilog code generation accuracy. | Evaluated against various complexity levels in Verilog tasks.| A newly created dataset focusing on diverse Verilog examples.   | 2024-04-21                | [MEV-LLM Paper](https://www.aimodels.fyi/papers/arxiv/multi-expert-large-language-model-architecture-verilog) |
| **VeriGen**                | A fine-tuned LLM for generating high-quality Verilog code.                     | Custom test suite for functional correctness.              | Datasets from GitHub and Verilog textbooks.                   | 2024-07-28                 | [VeriGen Paper](https://paperswithcode.com/paper/verigen-a-large-language-model-for-verilog)  |
| **VerilogEval**            | Benchmarking framework for evaluating LLMs in Verilog code generation.         | 156 problems from HDLBits for diverse tasks.               | Synthetic problem-code pairs generated by LLMs.               | 2023-09-14            | [VerilogEval Paper](https://arxiv.org/pdf/2309.07544.pdf)   |

- https://research.nvidia.com/publication/2023-09_verilogeval-evaluating-large-language-models-verilog-code-generation
