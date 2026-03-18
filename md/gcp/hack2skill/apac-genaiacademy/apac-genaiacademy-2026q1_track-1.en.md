**(A) Overall Summary, Takeaways, and Chapters**

**Overall Summary:**

This workshop, part of the Google Cloud GenAI Academy 2026 Track 1, focuses on the design, development, and deployment of agentic AI applications leveraging Google's Gemini ADK (Agent Development Kit) and Cloud Run. Mr. Tuya, a Developer Relations Engineer at Google, leads the session, commencing with an overview of the academy's objectives and the specific focus of Track 1. He thoroughly explains the evolution of AI agents, from simple Large Language Models (LLMs) with prompts to more sophisticated RAG (Retrieval Augmented Generation) systems, tool-enabled LLMs, standalone agents, and ultimately, complex multi-agent systems. A core component of the workshop is the introduction to ADK, an open-source framework that facilitates agent creation through various agent types (LLM-based, Workflow, Custom) and orchestration patterns (sequential, parallel, looping). Mr. Tuya then outlines the benefits of deploying these agents on Google Cloud Run, emphasizing its serverless nature, scalability (including scale-to-zero), high availability, and integrated security features. The practical segment involves a detailed hands-on lab demonstrating how to build a "Zoo Agent" that uses Wikipedia for information retrieval and deploy it onto Cloud Run. The session concludes with a recap and a rundown of the academy's next steps, including assessments, project submissions, certification, a hackathon, and an exclusive "GenAI Elite Club," along with crucial reminders about cloud credits and security best practices.

**Takeaways:**
*   AI agents represent the next technological frontier, evolving from basic LLMs to sophisticated multi-agent systems incorporating RAG and tools for more accurate and actionable responses.
*   The ADK (Agent Development Kit) is a flexible, modular, and open-source framework designed to simplify the development and deployment of AI agents, compatible with Gemini and other LLMs, and deployment platforms.
*   ADK offers different agent types (LLM-based, Workflow, Custom) and orchestration capabilities (Sequential, Parallel, Looping) to manage complex agent interactions.
*   Google Cloud Run provides an ideal serverless and fully managed environment for deploying production-ready AI agents, offering benefits like automatic scaling, cost efficiency (scale-to-zero), high availability, and seamless integration with other Google Cloud services.
*   Security must be a primary consideration throughout the agent development and deployment lifecycle, especially when dealing with service accounts, access control, and public-facing endpoints.
*   The Google Cloud GenAI Academy offers a comprehensive program with structured learning, practical labs, assessments, project opportunities, and a pathway to professional recognition and community engagement.

**Chapters:**
*   **00:02:52 - 00:03:31:** Welcome and Introduction of Mr. Tuya (Host, Manita Huja)
*   **00:03:31 - 00:05:08:** Introduction to Google Cloud GenAI Academy 2026 & Track 1 Overview (Mr. Tuya)
*   **00:05:08 - 00:08:44:** The Evolution of AI Agents (LLMs, RAG, Tools, Agents, Multi-Agent Systems) (Mr. Tuya)
*   **00:08:44 - 00:11:22:** AI Agent Formation Formula & Introduction to ADK (Agent Development Kit) (Mr. Tuya)
*   **00:11:22 - 00:15:43:** Types of Agents in ADK & Workflow Agent Patterns (Sequential, Parallel, Looping) (Mr. Tuya)
*   **00:15:43 - 00:18:46:** Benefits of Deploying AI Agents on Google Cloud Run (Serverless, Scalability, Availability, Security) (Mr. Tuya)
*   **00:18:46 - 00:20:16:** Overview of the Hands-on Lab: Building and Deploying a Zoo Agent (Mr. Tuya)
*   **00:20:16 - 00:25:57:** Lab Walkthrough: Google Cloud Project Setup & API Enablement (Mr. Tuya)
*   **00:25:57 - 00:29:34:** Lab Walkthrough: Setting Up the Development Environment (Virtual Env, `requirements.txt`, `.env` file for credentials) (Mr. Tuya)
*   **00:29:34 - 00:36:40:** Lab Walkthrough: Creating the Agent Workflow (`agent.py` - Researcher, Formatter, Tour Guide Workflow, Root Agent) (Mr. Tuya)
*   **00:36:40 - 00:41:13:** Lab Walkthrough: Application Preparation & Deployment to Cloud Run (Service Account, IAM Roles, ADK Deploy Command) (Mr. Tuya)
*   **00:41:13 - 00:45:14:** Lab Walkthrough: Testing the Deployed Agent & Cleaning Up Resources (Mr. Tuya)
*   **00:45:14 - 00:46:53:** Session Recap and Final Reminders (Mr. Tuya)
*   **00:46:53 - 00:50:08:** Program Next Steps and Benefits (Host, Manita Huja)

**(B) Detailed summary based on different attendees**

*   **Manita Huja (Host):**
    *   **Welcome and Introduction (00:02:52 - 00:03:31):**
        *   Welcomed attendees to the "Agentic AI from design to deployment" workshop, part of the Google Cloud GenAI Academy 2026 Track 1, powered by actskll.
        *   Introduced Mr. Tuya as a Developer Relations Engineer at Google with over seven years of experience in designing, developing, testing, and maintaining software solutions across various domains.
    *   **Program Next Steps and Benefits (00:46:53 - 00:50:08):**
        *   Thanked Mr. Tuya for the insightful session and all attendees for their active participation.
        *   Highlighted the importance of the **dashboard** as the "single source of truth" for workshop recordings, learning modules, code labs, and program updates.
        *   Stressed the importance of completing the **code lab** (credits and access details to be received via email) to apply theoretical knowledge to real-world scenarios.
        *   Encouraged exploring **specialized deep dive tracks** through Google Skills to enhance expertise beyond the core curriculum (credits provided).
        *   Explained the next mandatory step is attempting the **MCQ assessment** after completing the workshop and code lab for Track 1.
        *   Described the **project submission** phase, where participants can submit a track-aligned project individually.
        *   Outlined the **GenAI Master Certificate** awarded to participants who complete all required action items in at least one track.
        *   Mentioned invitations to a **graduation ceremony** where top 10 performers will be recognized and their projects showcased.
        *   Introduced the **cohort hackathon**, a team-based event (2-4 members) to solve a given problem statement with innovative AI solutions.
        *   Announced the **GenAI Elite Club**, an exclusive alumni network for top 100 performers from the academy and hackathon, fostering collaboration and innovation.
        *   Provided channels for support: Discord channel or email for technical or program-related questions.

*   **Mr. Tuya (Developer Relations Engineer, Google):**
    *   **Program Context and Vision (00:03:31 - 00:05:08):**
        *   Expressed gratitude and officially commenced the workshop as part of the Google Cloud GenAI Academy 2026 APAC edition, a premier challenge-based learning program.
        *   Stated that the program aims to upscale technical professionals and developers in GenAI technologies on Google Cloud, structured into three tracks.
        *   Specified today's workshop focuses on Track 1: "Build and deploy AI agent using Gemini ADK and Cloud Run," emphasizing designing, building, and deploying agentic AI applications as scalable, production-ready services.
    *   **Evolution of AI Agents (00:05:08 - 00:08:44):**
        *   **LLMs with Prompts:** The starting point, useful for generating reports or answering questions, but often providing "plausible but not accurate" answers.
        *   **Retrieval Augmented Generation (RAG):** Introduced to "ground" LLM results with correct information, reducing hallucination by providing context.
        *   **Extensions/Tooling:** Enabled LLMs to perform actionable tasks by calling external APIs, retrieving database information, reading files, or invoking other agents.
        *   **Agents:** Formed by combining LLMs with tools and a reasoning loop, capable of completing specific tasks.
        *   **Multi-Agent Systems:** Multiple agents collaborate to achieve complex common tasks, such as booking calendars or extracting relevant information.
    *   **AI Agent Formation & ADK (00:08:44 - 00:11:22):**
        *   Defined the three core components of an AI agent:
            *   **Model:** The reasoning core (e.g., Gemini 2.5 Flash, 3.0 Pro, Gemma).
            *   **Tooling:** Enables interaction with external systems (APIs, databases) or delegation to other agents.
            *   **Orchestration:** Provides persona, instructions, guardrails, and memory to manage agent behavior and track tasks.
        *   Introduced **ADK (Agent Development Kit)** as a flexible, modular, open-source framework for developing and deploying AI agents.
        *   Stated ADK is optimized for Gemini models but is model-agnostic (supporting `liteLLM` library) and deployment-agnostic.
        *   Highlighted ADK features: bidirectional streaming, evaluation, callbacks, planning, orchestration, artifact management, and code execution.
    *   **Agent Types in ADK & Workflows (00:11:22 - 00:15:43):**
        *   **LLM-based Agent:** Uses an LLM as its processing unit for direct task execution, tool calling, and delegation.
        *   **Workflow Agents:** Manages the execution flow of multiple agents.
            *   **Sequential:** Agents run strictly one after another (e.g., A -> B -> C).
            *   **Parallel:** Multiple sub-agents execute concurrently (e.g., for faster research across sources).
            *   **Looping:** Agents repeat steps for refinement or error correction until a condition is met or a maximum iteration count is reached (e.g., a coding agent passing all test cases).
        *   **Custom Agent:** Allows implementation of unique business logic or specialized controls for niche use cases not covered by other types.
    *   **Why Cloud Run for Deployment (00:15:43 - 00:18:46):**
        *   **Serverless and Fully Managed:** Eliminates infrastructure management concerns.
        *   **Scale to Zero:** Automatically de-provisions resources when not in use, reducing costs.
        *   **Automatic Scaling:** Scales up efficiently to handle increased demand.
        *   **High Availability:** Ensures agents are accessible 24/7.
        *   **Integrated Services:** Provides built-in logging, access control, and low-latency access to other Google Cloud services (like Gemini APIs) within the same ecosystem.
    *   **Hands-on Lab Introduction (00:18:46 - 00:20:16):**
        *   Introduced the lab: building and deploying a "Zoo Agent" that uses Wikipedia to provide animal information.
        *   Emphasized deployment to Cloud Run for public accessibility, not just local execution.
        *   Provided instructions for accessing the code lab and redeeming cloud credits.
    *   **Lab Walkthrough: Google Cloud Project Setup (00:20:16 - 00:25:57):**
        *   Demonstrated navigating to `console.cloud.google.com` and creating a new project (e.g., "AI agent zoo"), distinguishing between project name and project ID.
        *   Showed how to open the Cloud Shell Editor (`shell.cloud.google.com`) and authorize it.
        *   Provided the `gcloud services enable` command to activate necessary APIs: Cloud Run, Artifact Registry, Cloud Build, AI Platform (Vertex AI), and Compute Engine.
    *   **Lab Walkthrough: Environment Setup (00:25:57 - 00:29:34):**
        *   Instructed on creating a working directory (e.g., `zoo-guide-agent`) and opening it in the Cloud Shell Editor.
        *   Guided creation of `requirements.txt` listing `google-generative-ai-python[vertexai]==1.14`, `langchain-community`, and `wikipedia`.
        *   Steps for creating and activating a Python virtual environment and installing dependencies.
        *   Demonstrated setting environment variables (`PROJECT_ID`, `PROJECT_NUMBER`, `SERVICE_ACCOUNT_NAME`, `MODEL_NAME` like `gemini-2.5-flash`) via `gcloud` commands.
        *   Crucially warned against uploading `.env` files (especially those containing API keys) to public GitHub repositories due to security risks.
    *   **Lab Walkthrough: Agent Workflow Creation (00:29:34 - 00:36:40):**
        *   Created an `__init__.py` file to make the directory a Python package.
        *   Explained the `agent.py` content:
            *   Imports: `Agent`, `SequentialAgent`, `ToolContext`, `wikipedia.tool`.
            *   Cloud Logging setup for tracking application events.
            *   Model initialization using `VertexAI(model_name=MODEL_NAME)`.
            *   `add_prompt_to_state` function to log user prompts.
            *   `run_wikipedia_tool` function to perform Wikipedia searches.
            *   **Researcher Agent:** An LLM-based agent (`greeter`) instructed to access internal zoo data (hypothetical) and external knowledge from Wikipedia. It leverages LLM knowledge first, then Wikipedia. Output is stored under the `research_data` key.
            *   **Respond Formatter Agent:** An LLM-based agent designed to synthesize and format the `research_data` from the previous agent.
            *   **Tour Guide Workflow:** A `SequentialAgent` orchestrating the `researcher_agent` followed by the `respond_formatter_agent`.
            *   **Root Agent (Greeter):** The main entry point, greeting users and delegating animal-related questions to the `tour_guide_workflow` using "transfer control."
    *   **Lab Walkthrough: Application Preparation & Deployment (00:36:40 - 00:41:13):**
        *   Sourced the `.env` variables into the current terminal session.
        *   Created a dedicated service account (`gcloud iam service-accounts create`) to ensure the agent operates with minimal necessary permissions.
        *   Granted the "Vertex AI User" IAM role to the service account to allow model interaction.
        *   Executed the `adk deploy cloud-run` command to deploy the agent, specifying `PROJECT_ID`, `REGION`, `SERVICE_NAME` (`zoo-tour-guide`), enabling a UI, adding `LABELS`, and attaching the `SERVICE_ACCOUNT`.
        *   The deployment process involves packaging code, creating an Artifact Registry Docker repository (prompting user confirmation), and deploying the container to Cloud Run.
        *   Advised against allowing unauthenticated invocations in production and emphasized implementing proper security measures like VPNs, robust authentication, and firewalls for sensitive agents.
    *   **Lab Walkthrough: Testing & Cleanup (00:41:13 - 00:45:14):**
        *   Described accessing the deployed agent via the provided Cloud Run URL.
        *   Illustrated an interaction where the agent uses Wikipedia to answer questions about polar bear diets, demonstrating the sequential workflow.
        *   Mentioned that internal zoo information (like specific locations) would require integrating additional tools.
        *   Provided commands for cleaning up resources: `gcloud run services delete` (Cloud Run service), `gcloud artifacts repositories delete` (Artifact Registry), and `gcloud projects delete` (entire project).
        *   Strongly cautioned that project deletion is irreversible and requires careful verification of the `PROJECT_ID`.
    *   **Session Recap & Final Reminders (00:45:14 - 00:46:53):**
        *   Recapitulated the session's key topics: history and evolution of AI agents, ADK framework, different agent types and workflow orchestrations, and the hands-on lab on deploying a Zoo Agent to Cloud Run.
        *   Re-emphasized the critical importance of incorporating security concepts from the outset to protect against vulnerabilities.
        *   Reminded attendees to contact the program team if they had not received Google Cloud credits.

**(C) Action items**

*   **For Academy Participants:**
    - [ ] Log in to your participant dashboard and review all available resources (workshop recordings, learning modules, code labs).
    - [ ] Complete the "Build and Deploy AI Agent Lab" as demonstrated by Mr. Tuya.
    - [ ] Redeem the Google Cloud credits provided via email to complete the lab activities. If not received, contact the program team.
    - [ ] Explore the specialized deep dive tracks available through Google Skills to enhance your learning.
    - [ ] Complete the MCQ assessment for Track 1 after finishing the workshop and code lab.
    - [ ] Prepare and submit your track-aligned project through the dashboard when the submission window opens.
    - [ ] Plan to participate in the cohort hackathon with a team of 2-4 members.
    - [ ] Join the program's Discord channel or reach out via email for any technical or program-related questions.
*   **For Hands-on Lab Completion:**
    - [ ] Create a new Google Cloud project on `console.cloud.google.com`.
    - [ ] Open the Cloud Shell Editor at `shell.cloud.google.com`.
    - [ ] Authorize Cloud Shell when prompted.
    - [ ] Enable the following Google Cloud APIs in your project: `cloudrun.googleapis.com`, `artifactregistry.googleapis.com`, `cloudbuild.googleapis.com`, `aiplatform.googleapis.com`, `compute.googleapis.com`.
    - [ ] Create a dedicated working directory for the lab (e.g., `mkdir zoo-guide-agent && cd zoo-guide-agent`).
    - [ ] Create a `requirements.txt` file in your working directory with the specified dependencies.
    - [ ] Set up and activate a Python virtual environment, then install the dependencies using `pip install -r requirements.txt`.
    - [ ] Retrieve and set your `PROJECT_ID`, `PROJECT_NUMBER`, and define `SERVICE_ACCOUNT_NAME` and `MODEL_NAME` as environment variables.
    - [ ] Create a new service account with `gcloud iam service-accounts create <SERVICE_ACCOUNT_NAME>`.
    - [ ] Grant the "Vertex AI User" role to your newly created service account.
    - [ ] Create an empty `__init__.py` file in your working directory.
    - [ ] Create an `agent.py` file and copy the provided agent workflow code into it.
    - [ ] Deploy your AI agent to Google Cloud Run using the `adk deploy cloud-run` command, including all necessary parameters (project ID, region, service name, UI flag, service account).
    - [ ] (Optional for testing) Access your deployed agent's UI via the provided URL and test its functionality.
    - [ ] **Crucial for cost management:** After completing the lab, clean up your Google Cloud resources by deleting the Cloud Run service, the Artifact Registry repository, or the entire Google Cloud project (ensuring you use the correct project ID, as this action is irreversible).
    - [ ] Adhere to security best practices: avoid sharing unauthenticated agent URLs publicly and never commit sensitive files like `.env` to version control.

> # aider chat started at 2026-03-15 23:24:42

Here is a report based on the provided transcript, formatted in Markdown syntax as requested:

---

# Workshop Report: Agentic AI from Design to Deployment

## (A) Overview and Chapters

This workshop, part of the Google Cloud GenAI Academy APAC 2026 Track 1, focuses on designing, building, and deploying agentic AI applications using Gemini ADK (Agent Development Kit) and Google Cloud Run. The session covers the evolution of AI agents, key components of agent design, the functionalities of ADK, the benefits of deploying on Cloud Run, and a hands-on lab walkthrough for building and deploying a "Zoo Tour Guide" agent. It also outlines the overall program structure, participant responsibilities, and benefits.

**Chapters:**

*   **00:02:52 - 00:03:26**: Workshop Welcome and Speaker Introduction (Manita Huja)
*   **00:03:26 - 00:04:51**: Google Cloud GenAI Academy 2026 Overview and Track 1 Focus
*   **00:04:51 - 00:05:08**: Importance of AI Agents as the Next Frontier in Technology
*   **00:05:08 - 00:08:33**: Evolution of AI Agents (LLMs with Prompts, RAG, Tooling, Single Agents, Multi-Agent Systems)
*   **00:08:33 - 00:10:01**: The AI Agent Formula: Model, Tooling, and Orchestration
*   **00:10:01 - 00:11:22**: Introduction to ADK (Agent Development Kit) - Definition, Features, and Optimization
*   **00:11:22 - 00:13:15**: Types of Agents in ADK: LLM-Based, Workflow (Sequential, Parallel, Loop), and Custom Agents
*   **00:13:15 - 00:15:32**: Deep Dive into Workflow Agents: Sequential, Parallel, and Loop Examples
*   **00:15:32 - 00:18:44**: Understanding Google Cloud Run: Benefits for AI Agent Deployment (Serverless, Scalability, Availability, Integration)
*   **00:18:44 - 00:19:13**: Hands-on Lab Introduction: Building and Deploying a Zoo Agent
*   **00:19:13 - 00:22:50**: Lab Step 1: Google Cloud Project Creation
*   **00:22:50 - 00:25:50**: Lab Step 2: Cloud Shell Editor Setup and API Enablement
*   **00:25:50 - 00:29:33**: Lab Step 3: Environment and Requirements Setup (`requirements.txt`, virtual env, `.env`)
*   **00:29:33 - 00:35:59**: Lab Step 4: Agent Workflow Implementation (`__init__.py`, `agent.py` - Researcher, Formatter, Tour Guide Workflow, Root Agent)
*   **00:35:59 - 00:41:50**: Lab Step 5: Preparing and Deploying the Application to Cloud Run (Service Account, Roles, `adk deploy` command)
*   **00:41:50 - 00:44:12**: Lab Step 6: Testing and Important Security Considerations for Deployment
*   **00:44:12 - 00:45:10**: Lab Step 7: Environment Cleanup (Deleting Cloud Run, Repository, Project)
*   **00:45:10 - 00:46:49**: Workshop Recap
*   **00:46:49 - 00:50:08**: Program Next Steps for Participants (Dashboard, Code Lab, MCQ, Project, Hackathon, Certificates, Elite Club) (Manita Huja)

## (B) Mindmap (in markmap.js syntax)

```markmap
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
```

## (C) Detailed Summary Based on Different Attendees

Here's a detailed summary based on the contributions and key information provided by the different presenters and the expectations for program participants:

**Manita Huja (Host)**

*   **Welcome and Introductions:** Welcomed everyone to the workshop on agentic AI, expressing gratitude for their participation. She introduced herself as Manita Huja, the host for the day, and then proceeded to introduce Mr. Tuya, a Developer Relations Engineer at Google, as the main speaker.
*   **Closing Remarks and Program Next Steps:** Concluded Mr. Tuya's session by thanking him for an insightful presentation. She then transitioned into outlining the critical next steps for all program participants to ensure their success in the GenAI Academy program.
    *   **Dashboard:** Emphasized the participant dashboard as the "single source of truth" for all program resources, including workshop recordings, learning modules, code labs, and updates.
    *   **Code Lab:** Highlighted the importance of completing the code lab, which applies learned concepts through guided hands-on exercises based on real-world scenarios. Participants should have received credits and access details via email.
    *   **Google Skills Deep Dive:** Explained the availability of specialized deep-dive tracks through Google Skills to explore topics in more depth and practice beyond the core curriculum.
    *   **MCQ Assessment:** Instructed participants to attempt the MCQ assessment after completing the workshop and code lab for Track 1.
    *   **Project Submission:** Detailed the individual project submission phase, where participants can apply their learning to build practical, real-world AI applications.
    *   **GenAI Master Certificate:** Announced that a GenAI Master Certificate would be awarded to participants who complete all required action items in at least one track.
    *   **Graduation Ceremony:** Mentioned an invitation to a graduation ceremony for successful participants, where top 10 performers would be recognized and their projects showcased.
    *   **Cohort Hackathon:** Introduced the cohort hackathon where teams of 2-4 members would solve a problem statement and build innovative AI solutions.
    *   **GenAI Elite Club:** Highlighted the exclusive alumni network for the top 100 performers (from both the academy and hackathon) for ongoing collaboration and innovation.
    *   **Support:** Directed participants to the Discord channel or email for any questions.

**Mr. Tuya (Developer Relations Engineer at Google)**

*   **Program Context (03:30):**
    *   Confirmed the workshop is part of the expanded APAC edition of Google Cloud GenAI Academy 2026.
    *   Described it as a premier, challenge-based learning program designed to significantly upskill technical professionals and developers in GenAI technologies on Google Cloud.
    *   Stated that Track 1 focuses on "build and deploy AI agent using Gemini ADK and Cloud Run," enabling developers to design, build, and deploy agentic AI applications as scalable, production-ready services.
*   **Evolution of AI Agents (05:08):**
    *   **LLMs with Prompts:** Started with basic LLMs for tasks like report creation or specific questions.
    *   **Retrieval Augmented Generation (RAG):** Introduced to "ground" LLM results, reduce hallucinations, and provide more accurate outputs by using external context.
    *   **Tooling/Extensions:** Enabled LLMs to perform actionable tasks such as extracting information from APIs, retrieving from databases, reading files, or invoking other agents.
    *   **AI Agents:** Formed from LLMs, RAG, and tools, incorporating a "reasoning loop" to decide which tools to use.
    *   **Multi-Agent Systems:** Multiple agents working collaboratively to achieve complex common tasks (e.g., booking calendars, making appointments).
*   **AI Agent Formula (08:33):**
    *   **Model:** The "brain" (e.g., Gemini model versions, Gemma model versions) capable of reasoning.
    *   **Tooling:** Accesses APIs, databases, or delegates to other agents.
    *   **Orchestration:** Provides persona, instructions, guardrails, and memory to keep track of tasks.
*   **ADK (Agent Development Kit) (10:01):**
    *   **Definition:** A flexible, modular, open-source framework for developing and deploying AI agents.
    *   **Optimization:** Optimized for Gemini models but is model and deployment agnostic, supporting any model compatible with the `litellm` library.
    *   **Features:** Includes bidirectional streaming, evaluation, callback planning, orchestration, artifact management, and code execution tools.
*   **Agents in ADK (11:22):**
    *   **Large Language Model Based Agent:** Uses an LLM as the primary processing unit for user inputs, capable of tool calling and delegation.
    *   **Workflow Agents:** Manages the execution flow of other agents.
        *   **Sequential Agent:** Runs agents one after another in a predefined order.
        *   **Parallel Agent:** Executes multiple sub-agents concurrently to speed up tasks (e.g., researching multiple sources).
        *   **Loop Agent:** Repeats steps for refinement or error correction until a condition is met or a maximum number of iterations is reached (e.g., a coding agent passing all test cases).
    *   **Custom Agent:** Allows developers to implement unique business logic and specialized controls for niche use cases.
*   **Google Cloud Run (15:32):**
    *   **Purpose:** To deploy AI agents as publicly accessible, scalable production-ready services beyond a local laptop.
    *   **Benefits:**
        *   **Serverless:** Eliminates infrastructure management.
        *   **Fully Managed:** Google Cloud handles all platform operations.
        *   **Scalability:** Supports "scale to zero" (no cost when idle) and automatic scaling up to a defined maximum number of instances.
        *   **Availability:** Ensures agents are available 24/7 across different time zones.
        *   **Integration:** Provides built-in logging, access control, and low-latency access to other Google Cloud services (e.g., databases, Gemini APIs) within the same ecosystem.
*   **Hands-on Lab Walkthrough (Zoo Agent) (18:44):**
    *   **Objective:** To build and deploy a "Zoo Agent" that uses Wikipedia for information extraction and runs on Cloud Run.
    *   **Project Setup:** Guided through creating a new Google Cloud project via `console.cloud.google.com`.
    *   **Cloud Shell Editor & API Enablement:** Showed how to open the Cloud Shell editor (`shell.cloud.google.com`) and enable necessary Google Cloud APIs (`Cloud Run`, `Artifact Registry`, `Cloud Build`, `AI Platform`, `Compute`).
    *   **Environment Setup:** Covered creating a project directory, setting up a Python virtual environment, installing dependencies (`google-generative-ai-adk`, `langchain-community`, `wikipedia`), and configuring the `.env` file with `PROJECT_ID`, `PROJECT_NUMBER`, `SERVICE_ACCOUNT_NAME`, and `MODEL_NAME` (e.g., `gemini-1.5-flash`). Emphasized *not* uploading `.env` files to GitHub, especially if containing API keys.
    *   **Agent Implementation:** Walked through the code structure:
        *   `__init__.py`: For package initialization.
        *   `agent.py`:
            *   Initialized Cloud Logging and loaded environment variables.
            *   Defined a `add_prompt_to_state` function for logging prompts.
            *   Configured a `wikipedia_tool` using `LangchainTool` and `WikipediaAPIWrapper`.
            *   **Comprehensive Researcher Agent:** An LLM-based agent designed to research animal information, prioritizing internal zoo data (if available) then Wikipedia. It uses the `wikipedia_tool` and has `research_data` as its output key.
            *   **Respond Formatter Agent:** An agent responsible for formatting the final response using the `research_data` passed from the researcher.
            *   **Tour Guide Workflow (Sequential Agent):** An orchestration agent that runs the Comprehensive Researcher and Respond Formatter agents sequentially.
            *   **Root Agent (Greeter Agent):** The main entry point, designed to greet users and delegate control to the `tour_guide_workflow` for animal-related queries.
    *   **Deployment:** Explained sourcing the `.env` file, creating a dedicated service account, granting it the "Vertex AI User" role, and using the `adk deploy cloud-run` command with specified project, region, service name (e.g., `zoo-tour-guide`), UI, labels, and service account. This command handles Docker image creation, upload to Artifact Registry, and Cloud Run service deployment.
    *   **Security (41:50):** Strongly advised against sharing unauthenticated invocation links for deployed agents to prevent unintended credit consumption. Stressed the importance of VPNs and proper authentication for production systems.
    *   **Clean Up (44:12):** Provided commands to delete the Cloud Run service, the artifact registry repository, and, as a final option, the entire Google Cloud project (with a severe warning about its irreversibility and the need to verify the `PROJECT_ID`).
*   **Recap (45:10):** Summarized the workshop's key takeaways, reinforcing the evolution of AI agents, the capabilities of ADK, and the benefits of Cloud Run deployment for production-ready AI agents, along with security best practices.

**Program Participants (General Responsibilities & Benefits)**

*   **Responsibilities:**
    *   Redeem provided cloud credits for hands-on labs.
    *   Actively use the program dashboard for all resources and updates.
    *   Complete the code labs to apply practical knowledge.
    *   Engage with Google Skills for specialized deep-dive learning.
    *   Attempt MCQ assessments.
    *   Submit individual track-aligned projects.
    *   Participate in the cohort hackathon (optional but highly recommended).
    *   Adhere to security best practices when deploying solutions.
    *   Manage and clean up cloud resources to control costs.
    *   Reach out for support via Discord or email for any program or technical issues.
*   **Benefits:**
    *   Access to comprehensive learning modules, workshops, and code labs.
    *   Opportunity to build practical, real-world AI applications.
    *   Earn a GenAI Master Certificate for completing required actions.
    *   Invitation to a graduation ceremony with recognition for top performers.
    *   Opportunity to participate in a cohort hackathon and develop team-based AI solutions.
    *   Potential invitation to the exclusive GenAI Elite Club (for top 100 performers) for networking, collaboration, and staying at the forefront of innovation.
    *   Direct access to support channels for assistance.

## (D) Action Items

*   [x] Redeem Google Cloud credits as per instructions received via email or within the provided lab content comments.
*   [x] Familiarize yourself with and regularly check the participant dashboard for all workshop recordings, learning modules, code labs, and program updates.
*   [x] Complete the hands-on code lab, which involves building and deploying an AI agent using Gemini ADK and Cloud Run, to apply theoretical knowledge.
*   [x] Explore and engage with the specialized deep dive tracks available through Google Skills to further strengthen expertise and practice beyond the core curriculum.
*   [x] Attempt the MCQ assessment for Track 1 after completing the workshop and associated code lab.
*   [x] Individually prepare and submit a track-aligned project through the participant dashboard, focusing on building a practical, real-world AI application.
*   [x] Participate in the cohort hackathon, working in teams of two to four, to solve a given problem statement and build innovative AI solutions.
*   [x] Implement security best practices when deploying AI agents, particularly ensuring proper authentication and avoiding sharing unauthenticated invocation links to prevent unauthorized usage and credit consumption.
*   [x] Clean up Google Cloud resources (Cloud Run services, Artifact Registry repositories, or the entire project) after completing the lab to prevent incurring unnecessary costs.
*   [x] Reach out to the program team via the Discord channel or email for any technical, program-related, or credit-access questions.

## (E) 50 Single Select Quiz Questions

1.  **Which program is this workshop a part of?**
    a) Google Cloud AI Summit
    b) Google Cloud GenAI Academy APAC 2026 Track 1
    c) Google Cloud Developer Days
    d) Google AI Masterclass
    **Correct Answer:** b) Google Cloud GenAI Academy APAC 2026 Track 1

2.  **What is the primary focus of Track 1 in the academy?**
    a) Machine Learning Operations (MLOps)
    b) Data Engineering with BigQuery
    c) Build and deploy AI agent using Gemini ADK and Cloud Run
    d) Web Development with App Engine
    **Correct Answer:** c) Build and deploy AI agent using Gemini ADK and Cloud Run

3.  **What was the initial stage in the evolution of AI agents mentioned?**
    a) Multi-agent systems
    b) Tooling and extensions
    c) Large Language Models (LLMs) with prompts
    d) Retrieval Augmented Generation (RAG)
    **Correct Answer:** c) Large Language Models (LLMs) with prompts

4.  **What was the primary limitation of early LLMs that RAG aimed to address?**
    a) Slow processing speed
    b) High computational cost
    c) Providing plausible but not always accurate answers (hallucination)
    d) Inability to understand complex queries
    **Correct Answer:** c) Providing plausible but not always accurate answers (hallucination)

5.  **What is the purpose of "Tooling/Extensions" in the evolution of AI agents?**
    a) To enhance user interface design
    b) To enable LLMs to perform actionable tasks
    c) To optimize model training
    d) To improve data storage
    **Correct Answer:** b) To enable LLMs to perform actionable tasks

6.  **What three core components make up the "AI Agent Formula"?**
    a) Data, Algorithms, Cloud
    b) Model, Tooling, Orchestration
    c) Prompt, Response, Feedback
    d) Input, Process, Output
    **Correct Answer:** b) Model, Tooling, Orchestration

7.  **Which component of the AI Agent Formula provides persona, instructions, and memory?**
    a) Model
    b) Tooling
    c) Orchestration
    d) Data Source
    **Correct Answer:** c) Orchestration

8.  **What does ADK stand for?**
    a) AI Development Kit
    b) Agent Deployment Kernel
    c) Agent Development Kit
    d) Automated Deployment System
    **Correct Answer:** c) Agent Development Kit

9.  **ADK is optimized for which specific model family?**
    a) BERT
    b) GPT
    c) Gemini
    d) LLaMA
    **Correct Answer:** c) Gemini

10. **Is ADK specific to a particular deployment platform?**
    a) Yes, only Google Cloud
    b) Yes, only Kubernetes
    c) No, it's model and deployment agnostic
    d) Yes, only local machines
    **Correct Answer:** c) No, it's model and deployment agnostic

11. **Which ADK feature helps in testing the output of an agent?**
    a) Bidirectional streaming
    b) Evaluation
    c) Artifact management
    d) Code execution
    **Correct Answer:** b) Evaluation

12. **Which type of agent in ADK runs agents one after another in a predefined order?**
    a) Parallel Agent
    b) Loop Agent
    c) Custom Agent
    d) Sequential Agent
    **Correct Answer:** d) Sequential Agent

13. **Which type of workflow agent would be suitable for researching multiple different sources simultaneously?**
    a) Sequential Agent
    b) Parallel Agent
    c) Loop Agent
    d) Custom Agent
    **Correct Answer:** b) Parallel Agent

14. **A Loop Agent in ADK continues to execute until what two conditions are met?**
    a) User approval or system timeout
    b) Condition is met or maximum number of loops
    c) All tools are used or memory is full
    d) Internet connection is stable or deployment is complete
    **Correct Answer:** b) Condition is met or maximum number of loops

15. **What type of agent in ADK allows implementing unique business logic and specialized controls?**
    a) LLM-Based Agent
    b) Sequential Agent
    c) Parallel Agent
    d) Custom Agent
    **Correct Answer:** d) Custom Agent

16. **What is a key benefit of using Google Cloud Run for deploying AI agents?**
    a) Requires manual infrastructure provisioning
    b) Is a fully managed, serverless platform
    c) Only supports fixed scaling
    d) Limited to specific programming languages
    **Correct Answer:** b) Is a fully managed, serverless platform

17. **Cloud Run supports "scale to zero" functionality. What does this mean?**
    a) It can only handle zero requests.
    b) It scales down to zero instances when not in use, incurring no cost.
    c) It takes zero time to deploy.
    d) It has zero performance overhead.
    **Correct Answer:** b) It scales down to zero instances when not in use, incurring no cost.

18. **Why is availability a crucial factor for production AI agents, as discussed?**
    a) To minimize development time.
    b) To ensure agents are accessible to users across different time zones.
    c) To reduce the amount of code.
    d) To simplify logging.
    **Correct Answer:** b) To ensure agents are accessible to users across different time zones.

19. **What is the name of the AI agent built in the hands-on lab?**
    a) Weather Bot
    b) Shopping Assistant
    c) Zoo Tour Guide Agent
    d) Code Debugger
    **Correct Answer:** c) Zoo Tour Guide Agent

20. **Which external knowledge source does the lab's AI agent primarily use?**
    a) Google Search
    b) Proprietary Zoo Database
    c) Wikipedia
    d) Internal documentation
    **Correct Answer:** c) Wikipedia

21. **What command is used to enable Google Cloud APIs from the Cloud Shell?**
    a) `gcloud init`
    b) `gcloud services enable`
    c) `gcloud deploy`
    d) `gcloud config`
    **Correct Answer:** b) `gcloud services enable`

22. **Which Google Cloud service is NOT mentioned as needing to be enabled for the lab's deployment?**
    a) Cloud Run
    b) Artifact Registry
    c) BigQuery
    d) AI Platform (Vertex AI)
    **Correct Answer:** c) BigQuery

23. **What is the purpose of the `.env` file in the lab setup?**
    a) To store application logs.
    b) To define environment variables like project ID and model name.
    c) To list project dependencies.
    d) To configure network settings.
    **Correct Answer:** b) To define environment variables like project ID and model name.

24. **Which file contains the main agent workflow implementation in the lab?**
    a) `main.go`
    b) `agent.py`
    c) `requirements.txt`
    d) `init.py`
    **Correct Answer:** b) `agent.py`

25. **What is the role of the "Comprehensive Researcher Agent" in the Zoo Tour Guide workflow?**
    a) To greet users
    b) To format the final response
    c) To research animal information, prioritizing LLM knowledge then Wikipedia
    d) To manage deployment to Cloud Run
    **Correct Answer:** c) To research animal information, prioritizing LLM knowledge then Wikipedia

26. **What is the `output_key` defined for the "Comprehensive Researcher Agent"?**
    a) `final_answer`
    b) `research_data`
    c) `animal_facts`
    d) `wikipedia_result`
    **Correct Answer:** b) `research_data`

27. **The "Respond Formatter Agent" uses which keyword to retrieve data from the previous agent?**
    a) `input_data`
    b) `formatted_output`
    c) `research_data`
    d) `raw_output`
    **Correct Answer:** c) `research_data`

28. **What type of workflow agent is the "Tour Guide Workflow" implemented as?**
    a) Parallel Agent
    b) Loop Agent
    c) Sequential Agent
    d) Custom Agent
    **Correct Answer:** c) Sequential Agent

29. **What is the primary function of the "Root Agent" (Greeter) in the lab?**
    a) To perform all research tasks directly.
    b) To greet users and delegate to the tour guide workflow.
    c) To deploy the application.
    d) To clean up resources.
    **Correct Answer:** b) To greet users and delegate to the tour guide workflow.

30. **What mechanism is used by the Root Agent to pass control to the Tour Guide Workflow?**
    a) Direct function call
    b) Transfer control (sub-agent delegation)
    c) Shared global variable
    d) API endpoint
    **Correct Answer:** b) Transfer control (sub-agent delegation)

31. **Why is a dedicated service account created for deploying the agent to Cloud Run?**
    a) To make the deployment faster.
    b) To ensure the agent has only necessary permissions, not the user's full permissions.
    c) To enable advanced logging.
    d) To reduce billing costs.
    **Correct Answer:** b) To ensure the agent has only necessary permissions, not the user's full permissions.

32. **What Google Cloud IAM role is granted to the service account for the agent?**
    a) Owner
    b) Editor
    c) Vertex AI User
    d) Cloud Run Admin
    **Correct Answer:** c) Vertex AI User

33. **What is the command used to deploy the ADK agent to Cloud Run?**
    a) `gcloud run deploy`
    b) `adk deploy cloud-run`
    c) `docker push`
    d) `kubectl apply`
    **Correct Answer:** b) `adk deploy cloud-run`

34. **What is a critical security warning related to sharing deployed agent links?**
    a) It might expose your source code.
    b) It might lead to unauthorized credit consumption.
    c) It could reveal your personal identity.
    d) It might slow down the agent.
    **Correct Answer:** b) It might lead to unauthorized credit consumption.

35. **For production systems, what is recommended for securing agent access beyond unauthenticated invocation?**
    a) Public IP addresses
    b) Virtual Private Network (VPN) and proper authentication
    c) Open ports to the internet
    d) Disabling all logging
    **Correct Answer:** b) Virtual Private Network (VPN) and proper authentication

36. **Which command is used to delete the Cloud Run service created during the lab?**
    a) `adk delete service`
    b) `gcloud run services delete`
    c) `rm -rf cloud-run`
    d) `adk cleanup`
    **Correct Answer:** b) `gcloud run services delete`

37. **Deleting a Google Cloud project is reversible.**
    a) True
    b) False
    **Correct Answer:** b) False

38. **What is the "single source of truth" for program participants to find resources and updates?**
    a) Email inbox
    b) Discord channel
    c) Participant dashboard
    d) Google Drive
    **Correct Answer:** c) Participant dashboard

39. **Why is completing the code lab considered a "key part" of the program?**
    a) It's required for attendance tracking.
    b) It helps apply learned knowledge through hands-on exercises.
    c) It contributes to social networking.
    d) It's an alternative to attending workshops.
    **Correct Answer:** b) It helps apply learned knowledge through hands-on exercises.

40. **What is the benefit of exploring "specialized deep dive tracks" on Google Skills?**
    a) To quickly finish the program.
    b) To explore topics in more depth and strengthen expertise.
    c) To get extra credits without learning.
    d) To compete with other participants.
    **Correct Answer:** b) To explore topics in more depth and strengthen expertise.

41. **When should participants attempt the MCQ assessment for Track 1?**
    a) Before attending the workshop.
    b) After completing the workshop and code lab.
    c) At any time during the program.
    d) Only if they opt out of the project submission.
    **Correct Answer:** b) After completing the workshop and code lab.

42. **What is the final deliverable for individuals in the program journey before hackathon/elite club?**
    a) Attending all workshops
    b) Completing all MCQs
    c) Submitting a track-aligned project
    d) Redeeming all credits
    **Correct Answer:** c) Submitting a track-aligned project

43. **Who receives a GenAI Master Certificate?**
    a) All participants who enroll in the program.
    b) Participants who complete all required action items in at least one track.
    c) Only the top 10 performers.
    d) Participants who only attend workshops.
    **Correct Answer:** b) Participants who complete all required action items in at least one track.

44. **What is the team size for the cohort hackathon?**
    a) Individuals only
    b) Teams of 2 to 4
    c) Teams of 5 to 6
    d) Flexible, any size
    **Correct Answer:** b) Teams of 2 to 4

45. **Who is invited to join the "GenAI Elite Club"?**
    a) All participants who complete the program.
    b) Only those who submit a project.
    c) The top 100 performers from the cohort academy and hackathon.
    d) Workshop presenters and organizers.
    **Correct Answer:** c) The top 100 performers from the cohort academy and hackathon.

46. **What is the main advantage of the GenAI Elite Club?**
    a) Free Google Cloud credits for life.
    b) Exclusive alumni network for collaboration and innovation.
    c) Direct employment opportunities at Google.
    d) Access to beta features of Gemini.
    **Correct Answer:** b) Exclusive alumni network for collaboration and innovation.

47. **Where should participants reach out for questions (technical or program related)?**
    a) Through comments on the workshop video.
    b) Via Discord channel or email.
    c) Directly to Mr. Tuya's personal email.
    d) On public forums.
    **Correct Answer:** b) Via Discord channel or email.

48. **In the context of the lab, what does it mean to "source the env"?**
    a) To copy the .env file to a different location.
    b) To load the environment variables defined in the .env file into the current shell session.
    c) To delete the .env file.
    d) To encrypt the .env file.
    **Correct Answer:** b) To load the environment variables defined in the .env file into the current shell session.

49. **What is the primary purpose of an Artifact Registry in the deployment process?**
    a) To store source code files.
    b) To store Docker images for deployment.
    c) To manage virtual environments.
    d) To log agent interactions.
    **Correct Answer:** b) To store Docker images for deployment.

50. **The speaker emphasizes having what concept in mind when building and deploying solutions in a production system?**
    a) Cost optimization
    b) User interface design
    c) Security
    d) Performance
    **Correct Answer:** c) Security

## (F) FAQ

*   **What is the Google Cloud GenAI Academy 2026?**
    It is a premier, challenge-based learning program designed to significantly upskill technical professionals and developers across the APAC region in Generative AI (GenAI) technologies on Google Cloud.

*   **What is the focus of Track 1 in the GenAI Academy?**
    Track 1, titled "Build and deploy AI agent using Gemini ADK and Cloud Run," focuses on enabling developers to design, build, and deploy agentic AI applications as scalable, production-ready services.

*   **How have AI agents evolved according to the workshop?**
    The evolution began with Large Language Models (LLMs) and prompts, progressed to Retrieval Augmented Generation (RAG) for grounding results, then incorporated Tooling/Extensions for actionable tasks, leading to the creation of individual Agents with reasoning loops, and finally, Multi-Agent Systems where multiple agents collaborate.

*   **What are the three core components of an AI agent?**
    The three core components are:
    1.  **Model:** The "brain" (e.g., Gemini, Gemma) capable of reasoning.
    2.  **Tooling:** Enables access to APIs, databases, or delegation to other agents.
    3.  **Orchestration:** Provides persona, instructions, guardrails, and memory to manage tasks.

*   **What is ADK and what are its key features?**
    ADK stands for Agent Development Kit. It's a flexible, modular, and open-source framework for developing and deploying AI agents. Key features include bidirectional streaming, evaluation, callback planning, orchestration, artifact management, and code execution tools. It's optimized for Gemini but is model and deployment agnostic.

*   **What types of agents can be built with ADK?**
    ADK supports three distinct types of agents:
    1.  **Large Language Model Based Agents:** Use LLMs as the core processing unit.
    2.  **Workflow Agents:** Manage the execution flow of other agents, including Sequential, Parallel, and Loop types.
    3.  **Custom Agents:** Allow for implementing unique business logic and specialized controls.

*   **What is Google Cloud Run and why is it used for AI agents?**
    Google Cloud Run is a serverless, fully managed platform from Google Cloud. It is used for AI agents to deploy them from local development to a publicly accessible, scalable production environment. Benefits include scale-to-zero functionality (no cost when idle), automatic scaling, 24/7 availability, and seamless integration with other Google Cloud services.

*   **What critical security consideration should be kept in mind when deploying agents to Cloud Run, especially regarding access links?**
    It is crucial to avoid sharing unauthenticated invocation links for deployed agents, as this could lead to unauthorized individuals consuming your cloud credits. For production systems, Virtual Private Networks (VPNs) and proper authentication mechanisms are highly recommended.

*   **Where can participants find all the program resources and updates?**
    The participant dashboard is the "single source of truth" for workshop recordings, learning modules, code labs, and all program updates.

*   **How do participants get credits for the hands-on lab?**
    Participants should receive instructions and links via email to redeem cloud credits required to complete the labs. If not received, they should reach out to the program team.

*   **What are the final deliverables and recognitions for program participants?**
    Participants are expected to complete code labs, MCQ assessments, and submit an individual track-aligned project. Successful completion leads to a GenAI Master Certificate. Top performers are invited to a graduation ceremony and the GenAI Elite Club (for the top 100 performers after the hackathon).

> Tokens: 42k sent, 9.1k received. Cost: $0.04 message, $0.04 session.  
> js\n8n\lab0\.env  
> Add file to the chat? (Y)es/(N)o/(D)on't ask again [Yes]: n  
