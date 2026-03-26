# Day 2: The Specification Phase and Semantic Alignment

Day Two focuses on the transition from high-level intent to structured, verifiable requirements. In the SDD workflow, the goal is to achieve human-agent alignment on "What" needs to be built before addressing "How" it will be implemented. This is managed through the creation of a "Change" folder, which acts as an isolated sandbox for all planning artifacts.   

## 原始規劃

### 2.1 The Change Proposal Mechanism

Initiating a feature or architectural refactor begins with the `/opsx:propose` command (or `openspec new` in standalone CLI mode). This command scaffolds a directory within `openspec/changes/<change-name>/` and generates the initial `proposal.md`. The proposal serves to clarify the "Intent" and "Scope" of the work, defining the business problem and the high-level capabilities required to solve it.   

The effective use of the `/opsx:propose` command requires high-reasoning models such as Opus4.5 or GPT5.2. These models are better equipped to handle the "Consensual Planning" process, where the agent investigates the existing codebase (using the `explore` subagent) and suggests an approach that minimizes technical debt and maintains backwards compatibility.   

### 2.2 Drafting Verifiable Scenarios (Gherkin Implementation)

OpenSpec formalizes requirements through the use of "Delta Specs". Instead of maintaining a monolithic documentation file, OpenSpec creates modular specifications that describe only the behavior being added, modified, or removed in a specific change. These specs utilize Gherkin-style scenarios (Given/When/Then) to ensure that requirements are not just descriptive, but testable.   

| Spec Section | Purpose | Example Requirement |
| --- |  --- |  --- |
| `## ADDED` | New features or behaviors | "The system SHALL support OAuth2 login." |
| `## MODIFIED` | Changes to existing logic | "Session timeouts are reduced from 60 to 30 minutes." |
| `## REMOVED` | Deprecated or deleted functionality | "Legacy basic auth is no longer supported." |
| `#### Scenario` | Concrete examples of the behavior | "GIVEN a user... WHEN they login... THEN..." |

The significance of the scenario-based approach lies in its ability to support automated verification. When the agent later implements the code, it can refer to these scenarios to ensure that edge cases, such as session expiration or invalid credentials, are handled as specified.   

### 2.3 Context Hygiene and Verification Logic

As the number of specification artifacts grows, the "Context Window" of the agent can become saturated with irrelevant data. This degradation of context is a primary cause of agentic hallucination. To counteract this, OpenSpec benefits from a "Clean Room" approach where the agent is encouraged to "refresh" its context before starting implementation.   

The developer should run `openspec validate <change-id> --strict` at the end of Day Two. This command identifies any logical inconsistencies between the `proposal.md` and the `spec.md`. For example, if the proposal mentions a "mobile-first" approach but the specs do not include scenarios for responsive layouts, the validation tool will flag the omission, forcing the agent to align the artifacts before proceeding to the design phase.   

## 實測

### 2.1 The Change Proposal Mechanism

- 執行 `/opsx:propose` 指令，在 [Day 1](./openspec-labs_day1.md) 最後有實際跑過。

### 2.2 Drafting Verifiable Scenarios (Gherkin Implementation)

- 這段還是很偏描述性，而且著重於介紹「Gherkin-style scenarios (Given/When/Then)」。

### 2.3 Context Hygiene and Verification Logic

看樣子 Gemini Deep Research 生成的實作步驟不可靠。也可能因為 OpenSpec Skill 對應的文章比較少，所以生成的步驟混雜了單純使用 `openspec` CLI 指令的結果。

> 開發人員應在第二天結束時執行 `openspec validate <change-id> --strict` 命令。