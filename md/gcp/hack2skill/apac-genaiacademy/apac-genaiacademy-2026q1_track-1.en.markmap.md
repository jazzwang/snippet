# Agentic AI from Design to Deployment
## I. Google Cloud GenAI Academy 2026
### A. Program Overview
*   Challenge-based learning
*   Upscale technical professionals in GenAI on Google Cloud
### B. Track 1 Focus
*   Build and deploy AI agents
*   Using Gemini ADK and Cloud Run
*   Design, build, deploy agentic AI applications
*   Scalable, production-ready services
## II. Evolution of AI Agents
### A. Large Language Models (LLMs) with Prompts
*   Initial use cases: reports, specific questions
*   Limitations: plausible but not always accurate answers
### B. Retrieval Augmented Generation (RAG)
*   Purpose: Ground results, reduce hallucination
*   Mechanism: Incorporate external data for correct outputs
### C. Tooling/Extensions
*   Purpose: Enable LLMs to perform tasks
*   Examples: API extraction, database retrieval, file reading, invoking other agents
### D. Single Agents
*   Combination of LLMs, RAG, and multiple tools
*   Includes a reasoning loop for tool selection
### E. Multi-Agent Systems
*   Multiple agents working collaboratively
*   Achieve common, complex tasks (e.g., booking calendar, appointments)
## III. AI Agent Formula (3 Components)
### A. Model (Brain)
*   Examples: Gemini (2.5 flash, 3.0 pro, 3.0 zero flash), Gemma 3
*   Capability: Reasoning
### B. Tooling
*   Capabilities: Access APIs, databases, delegate to other agents
### C. Orchestration
*   Elements: Persona, instructions, guardrails, memory (track tasks)
## IV. ADK (Agent Development Kit)
### A. Definition
*   Flexible, modular, open-source framework
*   Develop and deploy AI agents
### B. Optimization
*   Optimized for Gemini models
*   Model and deployment agnostic (supports `litellm` compatible models)
### C. Features
*   Bidirectional streaming
*   Evaluation
*   Callback planning
*   Orchestration
*   Artifact management
*   Code execution tools
### D. Types of Agents in ADK
*   **1. LLM-Based Agents**
    *   LLM as core processing unit
    *   Handles tool calling and delegation
*   **2. Workflow Agents**
    *   Manage execution flow of other agents
    *   a. **Sequential Agent**
        *   Runs agents one after another in order
    *   b. **Parallel Agent**
        *   Executes multiple sub-agents simultaneously (e.g., multi-source research)
    *   c. **Loop Agent**
        *   Repeats steps for refinement or error correction
        *   Continues until condition met or max iterations reached
        *   Example: Coding agent passing test cases
*   **3. Custom Agents**
    *   Implement unique business logic
    *   Specialized controls for niche use cases
## V. Google Cloud Run
### A. Purpose
*   Deploy agents from local to scalable production environment
### B. Benefits
*   **1. Serverless**
    *   No infrastructure management
    *   Fully managed service
*   **2. Scalability**
    *   Scale to zero (no cost when idle)
    *   Automatic scaling up to defined maximums
*   **3. Availability**
    *   Agents available 24/7
*   **4. Integration**
    *   Logging, access control
    *   Low-latency access to other Google Cloud services (databases, Gemini APIs)
## VI. Hands-on Lab Walkthrough (Zoo Agent)
### A. Goal
*   Create, implement, and deploy a Zoo Tour Guide agent
*   Uses Wikipedia to extract animal info
*   Deploys to Cloud Run
### B. Key Steps
*   **1. Project Setup**
    *   Create new Google Cloud project
*   **2. Cloud Shell Editor & API Enablement**
    *   Open Cloud Shell
    *   Enable Cloud Run, Artifact Registry, Cloud Build, AI Platform, Compute APIs
*   **3. Environment & Requirements Setup**
    *   Create project directory
    *   Python virtual environment
    *   `requirements.txt` (ADK, Langchain, Wikipedia)
    *   `.env` file (PROJECT_ID, PROJECT_NUMBER, SERVICE_ACCOUNT_NAME, MODEL_NAME)
*   **4. Agent Implementation (Key Files)**
    *   `__init__.py`: Import `agent` object
    *   `agent.py`:
        *   Imports (ADK, Langchain, Wikipedia, Logging)
        *   Cloud Logging, environment loading
        *   `add_prompt_to_state` function
        *   `wikipedia_tool` setup
        *   **Comprehensive Researcher Agent:** LLM-based, uses tools, `research_data` output key. Prioritizes LLM, then Wikipedia.
        *   **Respond Formatter Agent:** Formats output using `research_data`.
        *   **Tour Guide Workflow (Sequential Agent):** Orchestrates Researcher -> Formatter.
        *   **Root Agent (Greeter Agent):** Entry point, greets, delegates control to Tour Guide Workflow.
*   **5. Preparation & Deployment**
    *   Source `.env`
    *   Create service account, grant "Vertex AI User" role
    *   `adk deploy cloud-run` command (project, region, service name, UI, labels, service account)
    *   Artifact Registry for Docker images
*   **6. Testing**
    *   Access deployed agent via URL
    *   Example query: "where can I find polar bear and zoo what's their diet"
*   **7. Security Considerations**
    *   Warning: Do not share unauthenticated invocation links (credit consumption risk)
    *   Production: Use VPN, proper authentication (firewall)
*   **8. Clean Up**
    *   Delete Cloud Run service
    *   Delete artifact registry
    *   Optionally delete entire Google Cloud project (irreversible, verify ID)
## VII. Program Logistics & Next Steps (for Participants)
### A. Dashboard
*   Single source of truth
*   Workshop recordings, learning modules, code labs, updates
### B. Code Lab
*   Key for applying learned knowledge
*   Credits received via email
*   Strongly encouraged to complete
### C. Google Skills Deep Dive
*   Specialized tracks for in-depth exploration
*   Strengthen expertise beyond core curriculum
### D. MCQ Assessment
*   Attempt after workshop and code lab for Track 1
### E. Project Submission
*   Submit a track-aligned project individually
*   Build practical, real-world applications
### F. GenAI Master Certificate
*   Received for completing all required actions in at least one track
### G. Graduation Ceremony
*   Invitation for successful participants
*   Top 10 performers recognized, projects showcased
### H. Cohort Hackathon
*   Work in teams (2-4 members)
*   Solve problem statement, build AI solutions
### I. GenAI Elite Club
*   Exclusive alumni network
*   Top 100 performers (Academy + Hackathon)
*   Space for collaboration and innovation
### J. Support
*   Reach out via Discord or email for questions (technical, program, credit issues)