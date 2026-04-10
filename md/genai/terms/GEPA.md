> What is gepa in the following conversation?

```
DS1:  another use case for registering prompts on UC - prompt optimization https://mlflow.org/prompt-optimization 
Jazz: Interesting link of mlflow. Is the prompt optimization powered by DSPy? :)
DS2:  yup but it only support gepa 
```

A:

In the context of that conversation, **GEPA** refers to **Genetic-Pareto Prompt Evolution** (also known as the **GepaPromptOptimizer**), a state-of-the-art prompt optimization algorithm researched by the Mosaic Research team at Databricks and implemented within the **DSPy** framework.

### What is GEPA?

GEPA is an **evolutionary optimizer** that automates the refinement of LLM prompts. Instead of a human manually tweaking words, GEPA uses an LLM to "reflect" on why certain prompts failed and then systematically rewrites them to improve performance.

Key characteristics include:

-   **Reflective Mutation:** It analyzes full execution traces (reasoning steps, tool calls, and errors) to diagnose failures in natural language rather than just relying on a simple numerical score.

-   **Pareto-Based Selection:** It maintains a "Pareto frontier" of high-performing prompt candidates, ensuring it explores multiple effective strategies rather than settling for just one.

-   **Efficiency:** It is designed to be significantly more efficient than traditional Reinforcement Learning (RL), often requiring only hundreds of "rollouts" (test runs) to find an optimal prompt compared to the tens of thousands needed by RL.

### Relationship with MLflow and DSPy

As mentioned in your conversation:

-   **Powered by DSPy:** GEPA is a core optimizer within the **DSPy** framework (`dspy.GEPA`).

-   **Integrated into MLflow:** Databricks has integrated this into the **MLflow Prompt Registry**. Using the `mlflow.genai.optimize_prompts()` API, you can call the `GepaPromptOptimizer` to automatically improve prompts stored in your registry.

The user in your snippet is noting that while MLflow supports prompt optimization, it currently defaults to or specifically supports the **GEPA** algorithm for that process.

### Reference

- LLM Prompt optimization: Genetic Pareto (GEPA) — Paper Review
  - https://sulbhajain.medium.com/llm-prompt-optimization-genetic-pareto-gepa-paper-reviw-29ee52d9b5db
- Prompt Optimizing with GEPA and Databricks for 90x cheaper inference
  - https://medium.com/@AI-on-Databricks/prompt-optimizing-with-gepa-and-databricks-for-90x-cheaper-inference-0068a2909d86