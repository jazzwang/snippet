<table width="100%"><tr style="background-color:lightyellow;"><td>Q:</td><td>
could you plan 15 days learning how to use opencode based on popular hands-on labs?
</td></tr></table>


OpenCode has exploded in popularity as the go-to **open-source AI coding agent** (currently sitting at over 95,000 GitHub stars). Think of it as a fully transparent, model-agnostic version of Claude Code or GitHub Copilot that you can run in your terminal, IDE, or as a standalone desktop app.

Here is a 15-day hands-on curriculum designed to take you from "What is this terminal wizardry?" to building complex features with custom sub-agents.

## Phase 1: The Launchpad (Days 1–4)

**Goal:** Master the environment and the "Plan vs. Build" mindset.

* **Day 1: Zero to Hero Installation.** Install OpenCode via CLI (`curl -fsSL https://opencode.ai/install | bash`). Connect your first provider—use **OpenCode Zen** for a free start, or hook up your OpenAI/Anthropic API keys using the `/connect` command.
* **Day 2: Navigating the TUI.** Learn the essential "dance" of the Text User Interface. Practice using `@` to reference files and `Tab` to switch between the **Plan** (Read-only) and **Build** (Write) agents.
* **Day 3: Project Contextualization.** Run `/init` in an existing project. Analyze the generated `AGENTS.md` file. This is the "brain" of your project—learn how to tweak it to tell the AI about your specific coding standards.
* **Day 4: The Researcher (Plan Mode).** Hands-on Lab: Open a legacy or complex open-source codebase. Use Plan mode to ask: *"How does the authentication flow work here?"* and *"Trace the data path from the API to the DB."*

## Phase 2: The Builder (Days 5–8)

**Goal:** Let the agent write code while you maintain the "Pilot" seat.

* **Day 5: Single-File Surgery.** Use Build mode to fix a specific bug or add a simple function. Observe how OpenCode handles file permissions and diffs.
* **Day 6: Multi-File Refactoring.** The "Great Cleanup" Lab. Ask OpenCode to take a messy 500-line file and split it into three clean, modular components.
* **Day 7: The Auditor.** Use the `/review` command. Challenge the AI to find security vulnerabilities or "code smells" in your recent work.
* **Day 8: Session Isolation.** Practice running two separate agents simultaneously—one designing a database schema while another builds the frontend components.

## Phase 3: Power User & Skills (Days 9–12)

**Goal:** Customize the agent to your specific workflow.

* **Day 9: Custom Commands.** Create your first custom command in `~/.config/opencode/commands/`. Example: A `/tailwind` command that ensures all UI suggestions strictly use specific design tokens.
* **Day 10: The Skill System.** Explore built-in skills (like terminal execution). Practice giving the agent permission to run tests automatically after every build.
* **Day 11: Building Custom Skills.** Write a small script (Python or Go) that OpenCode can call. For example, a skill that automatically fetches the latest Jira tickets related to the file you're editing.
* **Day 12: Privacy & Local Models.** Disconnect from the cloud. Set up **Ollama** and connect OpenCode to a local Llama 3 or Mistral model. Compare the "Vibe" and accuracy vs. cloud models.

## Phase 4: Integration & Mastery (Days 13–15)

**Goal:** Deploying OpenCode in professional pipelines.

* **Day 13: CI/CD & GitHub Actions.** Set up the OpenCode bot in a repo. Use `/opencode` in a Pull Request comment to have the agent automatically suggest a fix for a failing test.
* **Day 14: Real-World Lab: The "Good First Issue".** Find a beginner-friendly issue on a public GitHub repo. Use OpenCode to diagnose, fix, and draft the PR description.
* **Day 15: Vibe Coding Project.** Build a utility from scratch (e.g., a CLI weather app or a personal task tracker) purely through conversation. Focus on prompt chaining and high-level architectural guidance.

### Pro-Tips for the Journey

> **Watch the Context:** AI agents can "hallucinate" more when the context window is cluttered. Use `/init` regularly after major changes to keep the `AGENTS.md` file (and the agent's memory) fresh.

**Would you like me to provide a specific "Starter Project" idea to use for the Day 15 Vibe Coding lab?**
<table><tr style="background-color:lightyellow;"><td>Q:</td><td>
Let's plan step by step. Could you give me step-by-step instruction for Day 1? Target environment: Ubuntu WSL over Windows 11
</td></tr></table>


Setting up on **WSL (Windows Subsystem for Linux)** is a pro move. You get the power of a Linux kernel with the comfort of Windows UI. Since we are targeting a high-performance open-source agent setup, we’ll ensure your Ubuntu environment is primed for containerization and Python-based CLI tools.

Here is your **Day 1: The Foundation & The "Hello World"**.

## 1. Prepare your Ubuntu Environment

Before installing the agent, we need to ensure Ubuntu is up to date and has the necessary build tools.

1. **Open your Ubuntu Terminal** and run:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y build-essential curl git python3-pip
```


2. **Verify your WSL Version:** Ensure you are on **WSL 2**. In your Windows PowerShell (not Ubuntu), run `wsl -l -v`. If it says version 1, run:
```bash
wsl --set-version Ubuntu 2
```

## 2. The Engine: Install Docker (Crucial)

Most open-source agents (like OpenHands or OpenCode) use Docker to "sandbox" the code they write so they don't accidentally delete your Windows files.

1. **Install Docker Desktop for Windows** (if you haven't already).
2. **Crucial Step:** Go to Docker Desktop **Settings > Resources > WSL Integration**.
3. Toggle the switch for **Ubuntu** to "On."
4. Back in your Ubuntu terminal, type `docker ps`. If you don't see an error, you’re in business.

## 3. The Installation: OpenCode CLI

We will pull the latest stable build. Most modern agents use a simple curl-to-bash script.

1. **Run the Installer:**
```bash
curl -fsSL https://opencode.ai/install | bash
```


2. **Refresh your shell:**
```bash
source ~/.bashrc
```


3. **Test the command:** Type `opencode --version`.

## 4. Connecting the "Brain"

OpenCode is a body; it needs a model (LLM) to act as the brain. For Day 1, we’ll use an API key (easiest setup) or a local provider.

1. **Initialize Configuration:**
```bash
opencode config
```
> [!WARNING] 這個指令不正確，2026-02-08 測試時，並不存在。

2. **Choose your Provider:** * **Option A (Cloud):** Select `OpenAI` or `Anthropic`. It will ask for your API Key.
* **Option B (Local):** Select `Ollama` if you want to run things 100% locally on your PC (requires Ollama to be installed on Windows).


3. **Set the Workspace:** When asked for a workspace directory, point it to a new folder:
`~/opencode-lab`

## 5. The "Hello World" Lab

Let’s make sure the agent can actually "see" and "write" in your WSL environment.

1. **Create a test directory:**

```bash
mkdir ~/opencode-lab && cd ~/opencode-lab
```

2. **Start the Agent:**

```bash
opencode .
```

3. **The Prompt:** Inside the OpenCode interface, type:

> "Create a simple Python script named `sys_info.py` that prints the current OS version and the number of CPU cores. Then, execute it to prove it works."


4. **The Success Criteria:** You should see the agent create the file and then run it in the integrated terminal, outputting "Linux" (Ubuntu).

### Troubleshooting Tip

> **Permission Denied?** If you get a "Permission Denied" error when the agent tries to run a command, it’s usually because Docker needs `sudo`. You can fix this by adding your user to the docker group: `sudo usermod -aG docker $USER` (then restart WSL).

**How did the "sys_info.py" test go? If it worked, would you like to move on to Day 2 and learn how to navigate the interface like a power user?**
<table><tr style="background-color:lightyellow;"><td>Q:</td><td>
great! let's follow the same practice and create step-by-step instruction for Day 2.
</td></tr></table>


Since you’ve got the engine running, Day 2 is all about mastering the **User Interface (UI)** and the **Workflow Philosophy**.

In the world of AI agents, there is a massive difference between asking an AI to "write code" and "planning a solution." Today, you’ll learn how to switch between these modes to ensure the agent doesn't go off the rails.

## Day 2: Navigating the TUI & The "Plan-First" Workflow

### 1. Launching into "Project Mode"

Always launch OpenCode from the root of a project. This gives the agent the correct "context" of your file structure.

1. Open your Ubuntu terminal.
2. Navigate to your lab folder: `cd ~/opencode-lab`
3. Launch the interface: `opencode`

### 2. The Power of "Plan Mode" vs. "Build Mode"

In the TUI, you will see a toggle (usually at the top or switched via `Tab`).

* **Plan Mode (The Architect):** The agent can read files, search the web, and suggest logic, but it **cannot** write to your disk. It’s "Read-Only." Use this to brainstorm or explore.
* **Build Mode (The Engineer):** The agent has "Write" permissions. It can create files, delete code, and run terminal commands.

**The Golden Rule:** Never start in Build Mode. Always ask for a plan first to save your API tokens and prevent unwanted code changes.

### 3. Mastering the "@" Mentions

Just like on Discord or Slack, OpenCode uses the `@` symbol to focus the AI's "eyes" on specific things. Try these in the chat box:

* **`@file`**: Type `@` followed by a filename (e.g., `@sys_info.py`) to attach that specific file to your prompt.
* **`@folder`**: Attach an entire directory for context.
* **`@terminal`**: Sends the recent output of your terminal to the AI (great for debugging errors).
* **`@web`**: (If enabled) tells the agent to search the internet for documentation.

### 4. Hands-on Lab: The "Discovery" Exercise

Let’s practice navigating a small codebase without writing a single line of code yet.

1. **Step A (Setup):** In your terminal, quickly grab a tiny sample project:

```bash
git clone https://github.com/huggingface/chat-ui-template.git test-repo
cd test-repo
opencode .
```


2. **Step B (Plan Mode):** Switch to **Plan Mode**. Ask the agent:

> "I'm new here. Using `@test-repo`, can you explain the project structure and tell me where the main entry point for the API is?"


3. **Step C (Deep Dive):** Once it answers, use the `@` mention for the specific file it suggested:

> "Looking at `@src/lib/server/api.ts` (or whatever file it found), what environment variables do I need to set up to make this work?"

### 5. Essential Keyboard Shortcuts

To move fast in the OpenCode TUI, memorize these three:

| Shortcut | Action |
| --- | --- |
| `Tab` | Switch between Plan and Build modes |
| `Ctrl + C` | Cancel a running agent process (if it starts looping) |
| `Ctrl + L` | Clear the chat history to refresh the context window |
| `/` | Open the command menu (Connect, Settings, Clear) |

### Day 2 Success Checklist

* [ ] You successfully navigated between **Plan** and **Build** modes.
* [ ] You used the **`@`** symbol to reference a specific file.
* [ ] You understood why the agent recommended a specific file without it editing your code.

**How did the "Discovery" exercise go? Did the agent accurately find the entry point of that repo? If you're ready, Day 3 is where we start "Vibe Coding" our first multi-file feature!**
<table><tr style="background-color:lightyellow;"><td>Q:</td><td>
 create an exercise lab for Day 2
</td></tr></table>

For **Day 2**, we are moving from "Can I run this?" to "How do I control this?" This lab, titled **"Operation: Code Scout,"** focuses on using OpenCode as a high-level architect before you ever let it touch your source code.

## Day 2 Lab: Operation "Code Scout"

In this lab, you will explore a "mystery" codebase, map its dependencies, and simulate a debugging session using context mentions.

### Phase 1: The Setup

We need a project with enough files to be interesting but small enough to keep your head from spinning.

1. **Open Ubuntu WSL.**
2. **Clone this small FastAPI project** (a common web framework):

```bash
git clone https://github.com/tiangolo/full-stack-fastapi-template.git day2-lab
cd day2-lab/backend
```

3. **Launch OpenCode:**

```bash
opencode .
```
### Phase 2: The Architect's Walkthrough (Plan Mode)

Your goal is to understand the project without writing a single line of code.

1. **Switch to Plan Mode:** Press `Tab` until the UI indicates you are in **Plan** or **Architect** mode.
2. **The Scout Prompt:** Type the following:

> "Summarize the directory structure of this backend. What is the main entry point where the app starts, and which database is being used?"


3. **Verify the Context:** Note how OpenCode reads the `pyproject.toml` or `requirements.txt` to answer the database question.

### Phase 3: Surgical Context with `@`

Now, let’s test how well OpenCode can "see" specific files you point at.

1. **The Target:** Find a file related to "users" or "models" (likely in `app/models/`).
2. **The Context Prompt:** Use the `@` symbol to reference it:

> "Look at `@app/models/user.py`. Explain the relationship between the `User` model and any other models in this project. Does it have a one-to-many relationship with anything?"

3. **The Multi-File Prompt:** Ask it to compare two files:

> "Compare `@app/schemas/user.py` and `@app/models/user.py`. Why do we have two different files for the same 'User' entity?"

### Phase 4: The Detective (Terminal Integration)

The agent can see what's happening in your terminal. Let's simulate a "failed" environment check.

1. **Try to run the app (it will likely fail due to missing dependencies):**

```bash
python3 -m app.main
```

2. **Use `@terminal`:** In the OpenCode chat, type:

> "I just tried to run the app and got an error. Look at `@terminal` and tell me which library I am missing and how to install it in this WSL environment."

### Phase 5: The "Dry Run" Challenge

Before finishing, ask the agent to **plan** a change without **executing** it.

1. **The Challenge Prompt:**

> "I want to add a 'phone_number' field to the User model. In **Plan Mode**, give me a step-by-step list of every file I would need to modify to make this work, from the database model to the API schema."

2. **The Review:** Read the plan. Does it make sense? Did it miss the migration file? This is where you develop your "AI Oversight" skills.

## Day 2 Summary Checklist

| Task | Completed |
| --- | --- |
| Successfully toggled into **Plan Mode** | ☐ |
| Used **`@file`** to analyze a specific script | ☐ |
| Used **`@terminal`** to diagnose a shell error | ☐ |
| Received a multi-step plan without any files being edited | ☐ |

**How did OpenCode handle the "Phone Number" plan? Did it feel like it "understood" the full stack, or did it miss a spot?** When you're ready, we can move to **Day 3: The Project Brain**, where we learn how to configure `AGENTS.md` to make the AI follow your specific rules!

<table><tr style="background-color:lightyellow;"><td>Q:</td><td>
 Let's move on to Day 3. Could you give me step-by-step instruction for Day 3? Create an exercise lab for Day 3, too. Thanks
</td></tr></table>


Welcome to **Day 3**. Today, we transition from being a "user" of the agent to being its "manager."

When you work on a professional codebase, you have specific rules: maybe you use tabs instead of spaces, or perhaps you have a strict "no semi-colons" rule in JavaScript. If you don't tell the AI these rules, it will follow its own "vibes," leading to messy Pull Requests. Today, we learn how to bake those rules into the **Project Brain**.

## Day 3: The Project Brain (`AGENTS.md`)

In OpenCode, the "Brain" is usually a file created in your root directory (often `AGENTS.md` or hidden in `.opencode/`). This file tells the agent:

1. **Who it is** (e.g., "You are a Senior Go Developer").
2. **What the project does** (High-level architecture).
3. **The Rules of Engagement** (Coding standards, testing requirements).

### 1. Initializing the Brain

Open your Ubuntu WSL terminal and navigate to your `day2-lab` folder (or any project folder).

1. **Run the Init command:**

    ```bash
    opencode /init
    ```

2. **The Interaction:** The agent will scan your files and ask you what the project is about. It will then generate a file.
3. **Inspect the file:** Look for a new file called `AGENTS.md` or a similar configuration file in your directory. Open it with VS Code or `nano`.

### 2. The Anatomy of Project Context

Inside that file, you'll see sections like:

* **Project Overview:** A summary of the tech stack.
* **Active Tasks:** What the agent is currently working on.
* **Guidelines:** The "Do's and Don'ts."

### 3. Updating the "System Prompt"

You can manually edit this file to change how the AI behaves. If you add a line saying: *"Always use Arrow Functions in TypeScript,"* the agent will follow that rule for every subsequent prompt without you having to remind it.

## Day 3 Lab: "The Strict Architect"

In this lab, you will force OpenCode to adhere to a specific, strict set of rules for a new project.

### Phase 1: Setup a Blank Canvas

1. **Create a new directory:**
```bash
mkdir ~/day3-lab && cd ~/day3-lab
```

2. **Initialize OpenCode:**
```bash
opencode /init
```

*When it asks what the project is, tell it:* "This is a Python-based microservice for weather data."

### Phase 2: Injecting the Rules

Open the newly created `AGENTS.md` (or the config file it pointed you to) and add the following block under a section titled `# Coding Standards`:

> **IMPORTANT RULES:**
> * All Python functions MUST have Type Hints.
> * Use `logging` instead of `print()` statements.
> * Every file must start with a `# Created for Day 3 Lab` comment.
> * Use Google-style docstrings for every function.
>
>

### Phase 3: The Compliance Test

Now, let's see if the agent "remembers" its training.

1. **Launch OpenCode** in Build Mode: `opencode .`
2. **The Prompt:**

    > "Create a file called `fetcher.py` with a function that takes a city name as a string and returns a mock temperature of 25.0."

3. **The Audit:** Look at the code it generated.
* Did it use Type Hints? (`city: str -> float`)
* Did it add the `# Created for Day 3 Lab` comment?
* Did it avoid using `print()`?

### Phase 4: Dynamic Task Tracking

The "Brain" isn't just for rules; it's for status.

1. **Ask the agent:** > "Update the project documentation to show that the `fetcher.py` module is completed, and suggest the next three logical steps for this microservice."
2. **Check the file:** Open your `AGENTS.md` again. You should see the agent has physically updated the "Active Tasks" or "Status" section of the file.

## Day 3 Summary Checklist

| Task | Completed |
| --- | --- |
| Successfully ran **/init** to generate project context | ☐ |
| Manually edited the **Guidelines** to enforce a style | ☐ |
| Verified the agent followed the "No Print" and "Type Hint" rules | ☐ |
| Observed the agent updating its own **Status** in the file | ☐ |

### Pro-Tip: The "Reset"

If the agent starts getting confused or "forgetting" your `AGENTS.md` rules, use the command `/refresh` or `/reset`. This clears the short-term chat memory and re-reads the project files from scratch.

**How did the "Strict Architect" handle your rules? Did it try to sneak a `print()` statement in there, or was it perfectly compliant?** When you're ready, **Day 4** is where we master **The Researcher**, focusing on how to use the agent to explore massive, unfamiliar codebases without getting lost!

<table><tr style="background-color:lightyellow;"><td>Q:</td><td>
Let's move on to Day 4. Could you give me step-by-step instruction for Day 4? Create an exercise lab for Day 4, too. Thanks
</td></tr></table>

Welcome to **Day 4: The Researcher**.

Until now, you've been working with small files you mostly understood. Today, we shift gears. In a professional setting, you'll often be dropped into a "legacy" codebase with 50,000 lines of code written by someone who left the company three years ago.

Today is about using OpenCode as a **High-Resolution Intelligence Tool** to map out complex logic without getting overwhelmed.

## Day 4: Deep Tracing & Architecture Mapping

### 1. The Researcher's Mindset

In **Plan Mode**, OpenCode doesn't just "read" files; it can perform a "Deep Trace." This means following a single variable or function call across dozens of files to see how data actually moves.

### 2. Advanced Search Commands

Most agents have built-in "search" capabilities that are smarter than a simple `Ctrl+F`.

* **The Semantic Search:** Instead of searching for a word, you ask the agent: *"Find all files related to the user authentication lifecycle."*
* **The Logic Grep:** Ask: *"Where does the `User` object get mutated before being saved to the database?"*

## Day 3 Recap vs. Day 4 Goal

While Day 3 was about **setting the rules**, Day 4 is about **extracting the truth** from an existing system.

## Day 4 Lab: "The Code Archaeologist"

In this lab, you will download a real-world, complex library and use OpenCode to explain its "Black Box" logic.

### Phase 1: The Setup (The Target)

We'll use the **Flask** repository (a famous Python web framework) because it has deep, nested logic that is hard for humans to map quickly.

1. **Open Ubuntu WSL.**
2. **Clone the repo:**
```bash
git clone https://github.com/pallets/flask.git day4-archaeology
cd day4-archaeology
```

3. **Launch OpenCode in Plan Mode:**
```bash
opencode .
# Ensure you are in PLAN/ARCHITECT mode (Tab to switch)
```

### Phase 2: The Logic Trace

Your goal is to find out exactly what happens when a user visits a URL.

1. **The Entry Point Prompt:**

    > I want to understand how a Request is handled. Start at the very beginning—where does Flask first receive a WSGI request, and which file handles the initial parsing?

2. **The "Follow the Breadcrumbs" Prompt:** Once it gives you a file (likely `src/flask/app.py`), point to it:

    > In `@src/flask/app.py`, look at the `wsgi_app` method. Trace the execution from there to where the actual 'View Function' (the user's code) is called. List every file and function in that chain.

### Phase 3: Visualizing Dependencies

Let's ask the agent to create a "map" for us.

1. **The Mapping Prompt:**

    > Based on your analysis, create a Mermaid.js flowchart that shows the lifecycle of a Request in Flask, from `RequestContext` creation to the final `Response` being sent back.

2. **The Review:** Copy the Mermaid code it provides into the [Mermaid Live Editor](https://mermaid.live/) to see your visual map of the code.

### Phase 4: Finding the "Hidden" Logic

Large codebases often have "magic" (decorators, globals). Let's hunt them down.

1. **The Investigation Prompt:**

    > Flask uses a 'Global' called `request`. Since Python doesn't truly have global request objects in a multi-threaded environment, explain the 'magic' behind `LocalProxy` and `ContextVar` used here. Show me the specific code in this repo that makes this work.

## Day 4 Summary Checklist

| Task | Completed |
| --- | --- |
| Traced a function call across at least 3 different files | ☐ |
| Used the agent to explain a complex "magic" pattern (like LocalProxy) | ☐ |
| Generated a visual flowchart (Mermaid) of a logic path | ☐ |
| Identified the "Source of Truth" for a specific feature | ☐ |

### Pro-Tip: Context Budgeting

When researching large repos, the agent might try to read *too many* files and hit a "Context Limit." If you see a warning about "Context Window," tell the agent: *"Summarize the current file first, then tell me which ONE file I should open next to continue the trace."* This keeps the "memory" clean.

**How did the Flask trace go? Did the Mermaid flowchart help you visualize the "magic" of the framework?** If you're feeling like a code detective now, **Day 5** is where we finally put the "Researcher" cap away and start **Single-File Surgery**—learning how to make precise, surgical code edits in Build Mode! Would you like to proceed?

<table><tr style="background-color:lightyellow;"><td>Q:</td><td>
Let's move on to Day 5. Could you give me step-by-step instruction and create an exercise lab for Day 5?
</td></tr></table>

Welcome to **Day 5: Single-File Surgery**.

Today, we transition from being an observer to being an operator. In "Build Mode," OpenCode doesn't just suggest ideas—it picks up the scalpel and modifies your source code. The goal today is to master **surgical precision**: making the smallest possible change to achieve a specific result while minimizing "code drift."

## Day 5: The Build Mode & The Art of the Diff

### 1\. Entering Build Mode

In your WSL terminal, navigate to a project and launch OpenCode. Use `Tab` to switch from **Plan** to **Build**.

* **Visual Indicator:** The UI usually changes color (often to a "Caution" yellow or "Action" green) to let you know that the agent now has permission to write to your disk.

### 2\. Understanding the Diff View

When OpenCode proposes a change, it will show you a **Diff** (Differential).

* **Red/Minus (-):** Lines the AI wants to delete.
* **Green/Plus (+):** Lines the AI wants to add.
* **Gray/White:** Unchanged context code.

### 3\. The "Edit-Review-Apply" Loop

1. **Prompt:** You ask for a change.
2. **Draft:** The AI shows you the diff.
3. **Review:** You look for hallucinations or syntax errors.
4. **Action:** You choose to **Apply** (Save to disk), **Undo**, or **Iterate** (Ask for a fix to the fix).

## Day 4 Recap vs. Day 5 Goal

While Day 4 was about **mapping 50 files**, Day 5 is about **perfecting one**.

## Day 5 Lab: "The Bug Hunter"

In this lab, you will intentionally create a broken script and use OpenCode to perform "surgery" to fix it.

### Phase 1: Create the "Patient"

1. **Open Ubuntu WSL.**
2. **Create a new file:**

```bash
mkdir ~/day5-lab && cd ~/day5-lab
touch validator.py
```

3. **Paste this "broken" code into `validator.py**` (it has a regex bug and a logic flaw):

```python
import re

def validate_email(email):
    # Bug: This regex is way too simple and misses the domain dot
    regex = r'^[a-z0-9]+@[a-z0-9]+$'
    if re.match(regex, email):
        return True
    return False

def check_password_strength(password):
    # Bug: This returns True even if the password is empty
    if len(password) > 8:
        return True
    else:
        return True

print(validate_email("test@example")) # Should be False
print(check_password_strength(""))    # Should be False
```

### Phase 2: Surgical Fixes

1. **Launch OpenCode in Build Mode:**

```bash
opencode validator.py
```

2. **The Surgical Prompt:**

    > "Look at the `validate_email` function in `@validator.py`. The regex is failing because it doesn't require a dot in the domain. Fix ONLY the regex string."


3. **Review the Diff:** Ensure it didn't rewrite the whole file—just the one line. Click **Apply**.

### Phase 3: Logical Surgery

1. **The Logic Prompt:**

    > "The `check_password_strength` function always returns True. Fix the logic so it returns True only if the password is longer than 8 characters and contains at least one number."

2. **The Audit:** Did it import the `re` module if it needed it for the number check? Did it maintain your existing variable names?

### Phase 4: The Terminal Feedback Loop

1. **The Execution Prompt:**

    > "Run this script in the terminal and tell me if the output matches what we expect (False, False)."


2. **The Self-Correction:** If the output is still wrong, don't fix it yourself. Tell the agent:

    > "The terminal output was `True`. Re-examine the `check_password_strength` logic and try again."

## Day 5 Summary Checklist

| Task | Completed |
| --- | --- |
| Successfully toggled into **Build Mode** | ☐ |
| Reviewed a **Diff** and identified a specific change | ☐ |
| Applied a fix to a single function without touching the rest of the file | ☐ |
| Used the agent to execute the file and verify the fix | ☐ |

### Pro-Tip: Avoid "The Rewrite"

Sometimes AI agents get lazy and try to delete a 100-line file and replace it with 100 new lines just to change one variable. If you see a massive diff for a small change, **Cancel** it and say: *"Do not rewrite the whole file. Only modify the specific line where the error occurs."*

**How did the "Bug Hunter" lab go? Did the agent make a clean cut, or did it try to rewrite your whole script?** When you're ready, **Day 6** is the "level up" where we perform **Multi-File Refactoring**—making changes that span across different files at once!

<table><tr style="background-color:lightyellow;"><td>Q:</td><td>
Could you give me step-by-step instruction and create an exercise lab for Day 6?
</td></tr></table>

Yesterday was surgery; today is a full organ transplant. Welcome to **Day 6: Multi-File Refactoring**.

In professional software development, a single feature change rarely stays inside one file. If you change a database schema, you have to update the models, the API serializers, and the frontend types. Today, we’ll teach OpenCode how to coordinate these "ripples" across your codebase.

## Day 6: Coordinating Cross-File Changes

### 1\. The Multi-File Context Strategy

To refactor across files, the agent needs to see the **interconnections**. If you only point it at `file_a.py`, it won't know that `file_b.py` depends on it.

* **Pro Tip:** Use the `@` symbol for *all* involved files in your initial prompt so the agent builds a complete dependency graph in its "mind."

### 2\. The "Atomic" Transaction

When OpenCode refactors, it usually presents a sequence of diffs.

1. **File 1 (The Source):** It modifies the original logic.
2. **File 2 (The Consumer):** It updates the code that calls that logic.
3. **New Files:** It creates any necessary supporting modules.

## Day 6 Lab: "The Great Decoupling"

In this lab, you will take a "monolithic" script (one big messy file) and force OpenCode to break it into a clean, modular structure.

### Phase 1: Create the Monolith

1. **Open Ubuntu WSL.**
2. **Create a folder and a messy file:**

```bash
mkdir ~/day6-lab && cd ~/day6-lab
nano app.py
```

3. **Paste this code into `app.py`:**

```python
# A messy monolith that does everything
import json

def save_to_db(data):
    print(f"Connecting to database... Saving: {data}")

def process_user_data(name, age):
    if age < 18:
        status = "minor"
    else:
        status = "adult"

    user_record = {"name": name, "age": age, "status": status}
    save_to_db(user_record)
    return user_record

# Main execution
user = process_user_data("Alice", 30)
print(f"Processed: {user}")
```

### Phase 2: The Multi-File Refactor

1. **Launch OpenCode in Build Mode:**
```bash
opencode .
```


2. **The Refactor Prompt:**

    > "I want to clean this up. Move the `save_to_db` function into a new file called `database.py`. Move the `process_user_data` logic into `services.py`. Update `app.py` to import these functions and keep the main execution logic there. Ensure all files are correctly linked."

### Phase 3: Reviewing the Chain

1. **Watch the Diff Sequence:** OpenCode should show you:
* **Creation** of `database.py`.
* **Creation** of `services.py`.
* **Deletion/Modification** of `app.py`.

2. **Apply All:** Click "Apply" for each file.

### Phase 4: Validation & Testing

Now, verify the agent didn't break the imports (a common AI mistake in WSL).

1. **Run the entry point:**

```bash
python3 app.py
```

2. **The Error Hunt:** If you get an `ImportError`, don't fix it manually!
* **Prompt the agent:** > "I got an `ImportError`. Look at `@terminal` and fix the import paths in `@app.py` or `@services.py`."

## Day 6 Summary Checklist

| Task | Completed |
| --- | --- |
| Split a single file into at least 3 distinct modules | ☐ |
| Successfully managed cross-file imports using the AI | ☐ |
| Verified that the logic remains identical after the split | ☐ |
| Used **`@`** to reference multiple files in one prompt | ☐ |

### Pro-Tip: The "Dry Run" Check

Before applying a multi-file refactor, I always ask: *"Before you edit, list the exact imports you plan to add to each file."* This forces the agent to think about the file paths (like `from .database import save_to_db`) which is where most AI-generated code fails.

**How did the "Great Decoupling" go? Did the agent remember to add the `import` statements, or did you have to nudge it?** When you're ready, **Day 7** is all about **The Auditor**, where we use the agent to find security holes and performance bottlenecks in the code we just wrote!

<table><tr style="background-color:lightyellow;"><td>Q:</td><td>
Could you give me step-by-step instruction and create an exercise lab for Day 7?
</td></tr></table>

Welcome to **Day 7: The Auditor**.

By now, you’ve built code, moved code, and refactored code. But is the code *actually* good? Today, we stop playing the "Developer" and start playing the "Senior Security Engineer."

OpenCode shines when you ask it to find things you might have missed—like security holes, "code smells," or logic that will slow down your app as it scales.

## Day 7: Security, Performance, and the `/review` Command

### 1\. The Audit Mindset

When you audit code, you aren't looking for bugs that break the app (functional bugs); you are looking for **structural weaknesses**.

* **Security:** Are there hardcoded secrets? Is there a risk of SQL injection?
* **Performance:** Is there a "Big O" nightmare (like a loop inside a loop) that will crash if the data grows?
* **Maintainability:** Is the code so clever that a human won't understand it in six months?

### 2\. Using the `/review` Command

Most advanced agents have a dedicated review mode. In OpenCode, you can trigger this by using the `/review` command or by asking the agent specifically to "critique" a file.

## Day 7 Lab: "The Security Breach"

In this lab, you will create an intentionally "bad" application and use OpenCode to identify and patch the vulnerabilities.

### Phase 1: Setup the "Vulnerable Patient"

1. **Open Ubuntu WSL.**
2. **Create a new directory and file:**

```bash
mkdir ~/day7-lab && cd ~/day7-lab
nano vulnerable_app.py
```

3. **Paste this dangerously written code into `vulnerable_app.py`:**

```python
import sqlite3

# VULNERABILITY 1: Hardcoded Secret
API_KEY = "sk-12345-secret-key-do-not-share"

def get_user_data(username):
    db = sqlite3.connect("users.db")
    cursor = db.cursor()

    # VULNERABILITY 2: SQL Injection (Direct string formatting)
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchone()

def calculate_data(numbers):
    # VULNERABILITY 3: Performance Bottleneck (O(n^2) for no reason)
    result = []
    for i in numbers:
        for j in numbers:
            if i == j:
                result.append(i)
    return list(set(result))

print("App is running...")
```

### Phase 2: The Security Audit (Plan Mode)

1. **Launch OpenCode in Plan Mode:** `opencode .`
2. **The Auditor Prompt:**

    > "Perform a security and performance audit of `@vulnerable_app.py`. Identify at least three major issues and explain the risks associated with each."

3. **The Analysis:** Does the agent catch the SQL injection? Does it notice the hardcoded API key?

### Phase 3: The Surgical Patch (Build Mode)

1. **Switch to Build Mode** (`Tab`).
2. **The Patch Prompt:**

    > "Fix the SQL injection vulnerability using parameterized queries. Then, move the `API_KEY` to an environment variable lookup using the `os` module. Finally, optimize the `calculate_data` function to run in O(n) time instead of O(n^2)."

### Phase 4: Verification

1. **Review the Diff:** Look closely at how it handles the SQL query. It should change `'{username}'` to `?` and pass the variable as a tuple.
2. **Apply the changes.**

## Day 7 Summary Checklist

| Task | Completed |
| --- | --- |
| Identified a SQL injection vulnerability | ☐ |
| Replaced a hardcoded secret with an environment variable | ☐ |
| Optimized a nested loop into a more efficient algorithm | ☐ |
| Used **Plan Mode** to generate a written report of "code smells" | ☐ |

### Pro-Tip: The "Rubber Ducking" Technique

If the agent suggests a fix you don't understand, ask: *"Why is this fix safer than my original code?"* This turns the audit into a private tutoring session. Understanding the *why* is what makes you a better developer, not just a better AI user.

**How did your audit go? Did OpenCode find all three vulnerabilities, or did it miss the performance bottleneck?** When you're ready, we'll wrap up the week with **Day 8: Session Isolation**, where we learn how to run multiple "sub-agents" to handle different parts of a project at the same time! Would you like to proceed?

<table><tr style="background-color:lightyellow;"><td>Q:</td><td>
Could you give me step-by-step instruction and create an exercise lab for Day 8?
</td></tr></table>

Welcome to **Day 8: Session Isolation**.

Yesterday, you played the Auditor. Today, we learn the ultimate power move for scaling your productivity: **Parallel Workflows**.

In complex projects, you often have a "context pollution" problem. If you ask an agent to build a database and then ask it to design a CSS layout in the same session, the CSS logic might get "polluted" by database schemas, leading to hallucinations or irrelevant suggestions. Day 8 is about **Dividing and Conquering**.

## Day 8: Managing Sub-Agents and Parallel Tasks

### 1\. The Theory of Isolation

Session isolation allows you to run multiple instances of OpenCode on the same project but with different "missions."

* **Agent A (The Backend):** Focused only on Python/SQL.
* **Agent B (The Frontend):** Focused only on React/CSS.
* **The Bridge:** They both read a shared "Contract" file (like an API spec) to ensure they stay in sync without sharing every messy detail of their internal logic.

### 2\. How to "Double Up" in WSL

Since you are using Ubuntu WSL, you can easily open multiple terminal tabs (Ctrl+Shift+T in Windows Terminal).

1. **Tab 1:** Run `opencode` focused on the `/backend` folder.
2. **Tab 2:** Run `opencode` focused on the `/frontend` folder.

## Day 8 Lab: "The Full-Stack Split"

In this lab, you will act as the "Project Manager" coordinating two separate agents to build a feature simultaneously.

### Phase 1: Setup the Workspace

1. **Open Ubuntu WSL.**
2. **Create the structure:**

```bash
mkdir ~/day8-lab && cd ~/day8-lab
mkdir backend frontend shared
touch shared/api_spec.md
```

### Phase 2: Defining the Contract

Open `shared/api_spec.md` and paste this "Source of Truth":

> **Feature:** Task Logger
> **Endpoint:** `POST /tasks`
> **Input:** `{"title": string, "priority": int}`
> **Success Response:** `{"status": "success", "id": 1}`

### Phase 3: Launching the Backend Agent

1. **Open a New Terminal Tab** and navigate to `~/day8-lab/backend`.
2. **Launch OpenCode:** `opencode .`
3. **The Prompt:**

    > "Using the contract in `@../shared/api_spec.md`, build a FastAPI server with a POST endpoint that matches the spec. Don't worry about the UI."

### Phase 4: Launching the Frontend Agent (Simultaneously!)

1. **Switch back to your first Terminal Tab** (or open a 3rd) and go to `~/day8-lab/frontend`.
2. **Launch OpenCode:** `opencode .`
3. **The Prompt:**

    > "Using the contract in `@../shared/api_spec.md`, create a simple HTML/JavaScript file called `index.html`. It should have a form to submit a task title and priority. Assume the backend is running at `localhost:8000`."

### Phase 5: The Integration Test

Now, you bring them together.

1. In the **Backend Tab**, tell the agent: > "Run the server."
2. In the **Frontend Tab**, tell the agent: > "Open the `index.html` file in a way I can view it." (Usually, it will suggest a simple python server like `python3 -m http.server 3000`).
3. **Test the flow:** Submit a task from the UI and see the backend logs update in the other terminal.

## Day 8 Summary Checklist

| Task | Completed |
| --- | --- |
| Created a shared "Contract" file to sync agents | ☐ |
| Ran two separate OpenCode sessions in parallel | ☐ |
| Successfully prevented "Context Pollution" | ☐ |
| Verified that both agents adhered to the same API spec | ☐ |

### Pro-Tip: The "Context Wall"

If an agent starts asking about files in the other folder, remind it: *"You are the Frontend Agent. Stay within your directory. Only refer to the shared spec for external logic."* This keeps its "brain" lean and its responses fast.

**How did it feel to manage two "employees" at once? Did the UI and API connect on the first try, or was there a mismatch in the "Contract"?**

When you're ready, **Day 9** is where we get truly custom. We'll learn how to write **Custom Commands** so you can automate your own specific workflows with a single slash! Ready to move on?

<table><tr style="background-color:lightyellow;"><td>Q:</td><td>
Could you give me step-by-step instruction and create an exercise lab for Day 9?
</td></tr></table>

Welcome to **Day 9: Custom Commands**.

Yesterday, you mastered the "Project Manager" role by coordinating two agents. Today, we are going to give your agent a **Superpower**.

In OpenCode, you don't have to keep typing the same long instructions (e.g., *"Run my tests using pytest, format the output as a table, and then delete the cache"*). Instead, you can create a **Custom Command**. This allows you to trigger complex, multi-step workflows with a single slash like `/test` or `/deploy`.

## Day 9: Extending the Agent with Custom Commands

### 1\. The Configuration Directory

OpenCode stores its "DNA" in your home directory. In Ubuntu WSL, this is typically located at `~/.config/opencode/`. This is where the agent looks for global rules and custom scripts.

### 2\. Anatomy of a Custom Command

A custom command is essentially a "Shortcut" that combines:

* **The Trigger:** The name of the command (e.g., `lint`).
* **The Script:** A shell script or Python file that does the actual work.
* **The System Prompt:** Instructions telling the agent how to interpret the results of that script.

## Day 9 Lab: "Operation: Clean Slate"

In this lab, you will create a custom command called `/audit-ui`. This command will automatically run a "Linter" on your code and then tell the agent to fix only the errors that match your specific style guide.

### Phase 1: Create the Command Script

1. **Open Ubuntu WSL.**
2. **Create the commands directory** (if it doesn't exist):
```bash
mkdir -p ~/.config/opencode/commands
```

3. **Create the actual logic script:**
```bash
nano ~/.config/opencode/commands/ui-checker.sh
```

4. **Paste this simple "mock linter" code into the script:**
```bash
#!/bin/bash
echo "--- RUNNING UI AUDIT ---"
# This simulates finding a problem in a file
grep -rn "inline-style" .
echo "--- AUDIT COMPLETE ---"
```

5. **Make it executable:**
```bash
chmod +x ~/.config/opencode/commands/ui-checker.sh
```

### Phase 2: Registering the Command with OpenCode

Now we need to tell OpenCode that `/audit-ui` exists.

1. **Open the OpenCode config file:**
```bash
nano ~/.config/opencode/config.yaml
```

2. **Add a new section for commands** (The syntax may vary slightly by version, but it usually looks like this):
```yaml
custom_commands:
  - name: "audit-ui"
    description: "Checks for forbidden inline styles in HTML/CSS"
    executable: "~/.config/opencode/commands/ui-checker.sh"
    system_prompt: "When this command runs, look for any 'inline-style' mentions in the output. Immediately propose a refactor to move those styles to a separate CSS file."
```

### Phase 3: The Live Test

1. **Create a "messy" file in a new lab folder:**
```bash
mkdir ~/day9-lab && cd ~/day9-lab
echo '<div style="color: red;">Hello World</div>' > index.html
```
2. **Launch OpenCode:** `opencode .`
3. **The Magic Prompt:** 
   Simply type:
   > `/audit-ui`
4. **The Result:** You should see the agent trigger your bash script, see the "inline-style" output, and—without you saying another word—propose a diff to create `styles.css`.

## Day 9 Summary Checklist

| Task | Completed |
| --- | --- |
| Located the global OpenCode config directory | ☐ |
| Created an executable shell script in the `commands` folder | ☐ |
| Mapped a `/` command to a custom system prompt | ☐ |
| Successfully triggered a refactor using only a custom command | ☐ |

### Pro-Tip: The "Shell" Skill

If you don't want to create a permanent command, you can use the **Shell Skill**. You can tell OpenCode: *"I'm going to give you a new skill. Whenever I say 'Cleanup', run `rm -rf __pycache__` and then `git status`."* This is a "temporary command" valid for just that session.

**How did your `/audit-ui` command work? Did it feel like you just gave your agent a specialized tool?** When you're ready, **Day 10** is all about **The Skill System**, where we explore how to let the agent use external tools like web browsers or database clients! Would you like to proceed?

<table><tr style="background-color:lightyellow;"><td>Q:</td><td>
Could you give me step-by-step instruction and create an exercise lab for Day 10?
</td></tr></table>

Welcome to **Day 10: The Skill System**.

Yesterday, you built **Custom Commands**, which are like macros. Today, we dive into **Skills**, which are the agent's "senses" and "limbs." While a command is a script you tell the agent to run, a **Skill** is a capability the agent *knows* it can use whenever it needs to solve a problem.

Think of it this way: A Custom Command is a specific hammer you built. The Skill System is the agent’s ability to use any tool in the toolbox—browsers, terminal execution, and file system manipulation—without you explicitly telling it which one to pick.

## Day 10: Mastering Tool-Use and Permissions

### 1\. The Anatomy of a Skill

OpenCode agents typically have three core "Native Skills":

* **The Terminal Skill:** The ability to execute commands and read the output.
* **The File Skill:** The ability to read, write, and search the directory tree.
* **The Web Skill:** The ability to browse the internet to read documentation or search for solutions (often via a headless browser like Playwright).

### 2\. Managing "Agent Trust"

In Ubuntu WSL, security is key. You can set your skills to three levels of permission:

* **Manual:** Every time the agent wants to run a tool, it asks you for a "Yes/No."
* **Semi-Auto:** It asks for permission for "Write" or "Execute" actions, but "Read" actions are silent.
* **Auto-Pilot:** The agent runs everything freely (Only recommended for sandboxed Docker environments).

## Day 10 Lab: "The Documentation Scout"

In this lab, you will force the agent to use the **Web Skill** to learn about a library that is too new for its internal training data, and then use the **Terminal Skill** to verify its findings.

### Phase 1: Setup the Workspace

1. **Open Ubuntu WSL.**
2. **Create a clean folder:**
```bash
mkdir ~/day10-lab && cd ~/day10-lab
```

### Phase 2: Enabling the Web Skill

Before starting, ensure OpenCode has its "eyes" open.

1. **Launch OpenCode:** `opencode config`
2. Navigate to **Skills** or **Tools**.
3. Ensure **Search/Browser** is enabled (it may require a Search API key like Tavily or Serper, or it may use a built-in scraper).
4. Set **Terminal Permissions** to "Always Ask" (to practice the safety loop).

### Phase 3: The "Modern Tech" Challenge

We are going to ask the agent to use a very specific, modern library—let's use **`FastHTML`** (a relatively new Python web framework).

1. **The Research Prompt:**

    > "I want to build a simple Hello World app using the `FastHTML` library. I suspect your training data might be outdated for this. Use your **Web Search skill** to find the latest 'Getting Started' snippet from their official documentation."


2. **Watch the Skill in Action:** You should see the agent trigger a search, visit a URL, and summarize the findings.

### Phase 4: Verification via Terminal Skill

1. **The Execution Prompt:**

    > "Based on what you found, create `main.py`. Then, try to install the necessary library using `pip` and run the script. If it fails, search for the error message and fix it."

2. **The Safety Check:** When the agent tries to run `pip install`, you will see a prompt in your WSL terminal: **"Agent wants to run: pip install fasthtml. Allow? [y/N]"**.
3. **Approve it** and watch the agent complete the cycle.

## Day 10 Summary Checklist

| Task | Completed |
| --- | --- |
| Verified Web/Search skill is active in config | ☐ |
| Observed the agent performing a live web search | ☐ |
| Used the Terminal skill to install a real dependency | ☐ |
| Experienced the "Permission Prompt" security loop | ☐ |

### Pro-Tip: The "Context Refresh"

When the agent uses the Web Skill, it often brings back a *lot* of text. If the chat gets sluggish, use the command `/summarize-context`. This tells the agent to keep the important facts it found on the web but "forget" the raw HTML/Logs it processed, keeping your WSL performance high.

**How did the agent handle the FastHTML challenge? Did it find the right documentation, or did it try to guess the syntax?**

When you're ready, **Day 11** is where we go "Meta." We’ll learn how to build **Custom Skills**—actually writing Python scripts that the agent can call as if they were built-in features! Would you like me to prepare the Day 11 instructions?

<table><tr style="background-color:lightyellow;"><td>Q:</td><td>
Could you give me step-by-step instruction and create an exercise lab for Day 11?
</td></tr></table>

Welcome to **Day 11: Building Custom Skills**.

Today, we go "Meta." Yesterday, you used built-in skills like the web browser. Today, you will actually **program the agent's brain** to use a tool that doesn't exist yet.

In OpenCode (and many similar agent frameworks), a **Custom Skill** is a script paired with a "Manifest" that tells the AI: *"Here is a new superpower you have, here is how to call it, and here is what to expect back."*

## Day 11: The Architecture of a Custom Skill

### 1. The Skill Payload

A skill consists of two parts:

* **The Logic:** A script (usually Python or Bash) that performs an action (e.g., querying a Jira ticket, checking GPU temperature, or interacting with a proprietary API).
* **The JSON Schema:** A description the LLM reads. It defines the **parameters** the agent needs to provide to use the tool.

### 2. Why "Skills" over "Commands"?

* **Commands (/):** You have to trigger them manually.
* **Skills:** The agent **decides** to use them autonomously when it realizes it doesn't have the information it needs.

## Day 11 Lab: "The Hardware-Aware Agent"

In this lab, you will build a skill that allows OpenCode to check your WSL system resources (CPU/RAM). You will then give it a task that it should only perform if there is enough "headroom."

### Phase 1: Create the Skill Logic

1. **Open Ubuntu WSL.**
2. **Create a dedicated skills folder:**
```bash
mkdir -p ~/.config/opencode/skills/sys_monitor
cd ~/.config/opencode/skills/sys_monitor

```


3. **Create the Python script (`monitor.py`):**
```python
import psutil
import json

def get_stats():
    stats = {
        "cpu_usage": psutil.cpu_percent(interval=1),
        "ram_usage": psutil.virtual_memory().percent,
        "is_safe": psutil.cpu_percent() < 80
    }
    print(json.dumps(stats))

if __name__ == "__main__":
    get_stats()

```


*(Note: You might need to `pip install psutil` in your WSL environment).*

### Phase 2: Create the Manifest (`skill.json`)

This is the "instruction manual" for the AI.

1. **Create the file:** `nano skill.json`
2. **Paste the schema:**
```json
{
  "name": "check_system_resources",
  "description": "Checks the current CPU and RAM usage of the WSL environment.",
  "parameters": {
    "type": "object",
    "properties": {}
  },
  "command": "python3 ~/.config/opencode/skills/sys_monitor/monitor.py"
}

```



### Phase 3: Registering the Skill

1. Open your global config: `nano ~/.config/opencode/config.yaml`
2. Under the `skills:` section, add the path to your new `skill.json`.
3. **Restart OpenCode.**

### Phase 4: The Autonomous Test

1. **Navigate to a test folder:** `cd ~/day11-lab`
2. **Launch OpenCode.**
3. **The Challenge Prompt:**
> "I want to run a heavy data processing script that requires at least 20% free CPU capacity. Use your `check_system_resources` tool to see if it's safe to run. If it is, create a dummy 1GB file. If not, tell me why."


4. **Watch the Magic:** You should see a log entry: **"Agent called tool: check_system_resources"**. The agent will read the JSON output from your Python script and make a logical decision based on the `is_safe` boolean.

## Day 11 Summary Checklist

| Task | Completed |
| --- | --- |
| Wrote a Python script that outputs JSON | ☐ |
| Defined a JSON Schema (Manifest) for the tool | ☐ |
| Integrated the skill into the global agent config | ☐ |
| Observed the agent choosing to use the tool autonomously | ☐ |

### Pro-Tip: The "Bridge" Pattern

If you have a tool on your **Windows 11** side (like a specific `.exe`) that you want the agent to use, you can call it from WSL by using the `.exe` extension (e.g., `/mnt/c/Windows/System32/tasklist.exe`). This allows you to build "Cross-OS" skills!

**Did the agent correctly identify your CPU usage? It’s a bit of a rush the first time you see the AI "decide" to use a tool you just built.** When you're ready, **Day 12** is a major pivot: **Privacy & Local Models**. We’ll take the agent completely offline using Ollama! Ready to cut the cord?
<table><tr style="background-color:lightyellow;"><td>Q:</td><td>
Could you give me step-by-step instruction and create an exercise lab for Day 12?
</td></tr></table>

Welcome to **Day 12: Privacy & Local Models**.

Until now, your agent’s "brain" has likely lived in the cloud (OpenAI, Anthropic, etc.). While powerful, this means your code is being sent to third-party servers. Today, we "cut the cord." We will set up **Ollama** to run Large Language Models (LLMs) directly on your Windows 11 hardware, and we’ll point OpenCode to this local instance.

This is the "Privacy First" setup—perfect for working on sensitive corporate data or when you’re on a plane with no Wi-Fi.

## Day 12: Taking the Agent Offline

### 1. The Local LLM Architecture

In a local setup, the "Agent" (OpenCode) still runs in your WSL terminal, but instead of calling an API over the internet, it calls a local server (Ollama) running on your own machine.

### 2. Choosing Your Model

Since you are in a coding environment, you need a model optimized for logic.

* **Llama 3 (8B):** Great all-rounder.
* **Codestral (Mistral):** Specifically tuned for 80+ programming languages.
* **DeepSeek-Coder-V2:** Currently one of the highest-rated open-source coding models.

## Day 12 Lab: "The Air-Gapped Assistant"

In this lab, you will install a local model, configure OpenCode to use it, and test its ability to handle a "top secret" coding task without internet access.

### Phase 1: Install Ollama in WSL

While you can install Ollama on Windows, installing it natively in WSL often provides better performance for Linux-based agents.

1. **Open Ubuntu WSL.**
2. **Run the Ollama install script:**
```bash
curl -fsSL https://ollama.com/install.sh | sh

```


3. **Start the Ollama server:**
```bash
ollama serve

```


*(Note: Keep this terminal open, or run it in the background).*
4. **In a new WSL tab, pull a coding model:**
```bash
ollama run codestral

```


*(This may take a few minutes to download—it's about 5-8GB).*

### Phase 2: Point OpenCode to the Local Brain

1. **Open your OpenCode config:**
```bash
nano ~/.config/opencode/config.yaml

```


2. **Update the provider settings:**
Change your active provider to `ollama`:
```yaml
provider: ollama
base_url: "http://localhost:11434"
model: codestral

```


3. **Save and exit.**

### Phase 3: The "Offline" Coding Test

To prove we are private, let’s simulate an air-gapped environment.

1. **Create a "Sensitive" project:**
```bash
mkdir ~/day12-private && cd ~/day12-private
echo "SECRET_KEY=12345-ABCDE-PROPRIETARY" > .env

```


2. **Turn off your Wi-Fi** (optional but satisfying for this lab).
3. **Launch OpenCode:** `opencode .`
4. **The Prompt:**
> "Analyze `@.env`. Create a Python script that masks this SECRET_KEY and logs only the first and last three characters. Do this 100% locally."



### Phase 4: Performance Benchmarking

1. **Observe the speed:** Local models depend on your GPU (VRAM). If it feels slow, check if WSL is using your NVIDIA/AMD GPU.
2. **The Quality Check:** Ask a complex logic question:
> "Explain the Big O complexity of a recursive Fibonacci function and suggest an optimized iterative version."


3. Compare the answer to what you remember from the "Cloud" models.

## Day 12 Summary Checklist

| Task | Completed |
| --- | --- |
| Installed Ollama natively in WSL | ☐ |
| Downloaded a specialized coding model (e.g., Codestral) | ☐ |
| Configured OpenCode to use `localhost:11434` | ☐ |
| Successfully completed a coding task while offline | ☐ |

### Pro-Tip: The "VRAM" Wall

If your local model is extremely slow or "hallucinates" gibberish, your GPU might be out of memory (VRAM). In WSL, you can check your GPU usage by running `nvidia-smi`. If you're maxed out, try a smaller model like `phi3:mini` (Microsoft's lightweight model) which runs fast even on laptops without dedicated GPUs.

**How did the local model feel compared to the cloud? Was it a "snappy" experience, or did your PC fans start sounding like a jet engine?**

When you're ready, **Day 13** is where we move back to the "World" by integrating OpenCode into **CI/CD and GitHub Actions**. We’ll learn how to make the agent part of your team's automated workflow! Ready?
<table><tr style="background-color:lightyellow;"><td>Q:</td><td>
Could you give me step-by-step instruction and create an exercise lab for Day 13?
</td></tr></table>


Welcome to **Day 13: CI/CD & GitHub Actions**.

We are now in the **Mastery Phase**. Up until now, OpenCode has been a personal assistant living in your local terminal. Today, we turn it into a **Team Member**. We will integrate the agent into a GitHub repository so that it can automatically review code, fix failing tests, and suggest improvements every time you (or a teammate) push code.

## Day 13: The Automated Collaborator

### 1. Headless Mode (The Bot Mindset)

In your local WSL, you’ve been using the TUI (interactive interface). For CI/CD, we use **Headless Mode**. This allows OpenCode to:

* Run as a command-line script.
* Read a Pull Request (PR) description.
* Output its "diffs" directly into a GitHub comment.

### 2. GitHub Secrets & Security

Since the agent needs to call an LLM (OpenAI, Anthropic, or even your local Ollama if it's exposed), you must never hardcode your API keys in the `.yml` file. We will use **GitHub Secrets** to keep things secure.

## Day 13 Lab: "The Automated PR Doctor"

In this lab, you will set up a GitHub Action that triggers OpenCode to "diagnose" a failing test in a Pull Request.

### Phase 1: Setup a GitHub Repo from WSL

1. **Open Ubuntu WSL.**
2. **Create a new repo and push to GitHub:**
```bash
mkdir ~/day13-ci && cd ~/day13-ci
git init
# (Assuming you have the GitHub CLI 'gh' installed)
gh repo create day13-ci --public --source=. --remote=origin

```


3. **Add your API Key to GitHub Secrets:**
* Go to your repo on GitHub.com.
* Navigate to **Settings > Secrets and variables > Actions**.
* Add a **New repository secret**:
* Name: `OPENCODE_API_KEY`
* Value: (Your OpenAI or Anthropic key)





### Phase 2: Create the Workflow

1. **In your WSL terminal, create the workflow directory:**
```bash
mkdir -p .github/workflows
nano .github/workflows/opencode-ci.yml

```


2. **Paste this configuration:**
```yaml
name: OpenCode Reviewer
on: [pull_request]

jobs:
  ai_review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run OpenCode Headless
        env:
          OPENCODE_API_KEY: ${{ secrets.OPENCODE_API_KEY }}
        run: |
          curl -fsSL https://opencode.ai/install | bash
          opencode --headless --review "Check this PR for bugs and suggest fixes"

```



### Phase 3: The "Bait" (Triggering the Bot)

1. **Create a "broken" feature branch:**
```bash
git checkout -b feature/broken-logic

```


2. **Create `math_utils.py` with a bug:**
```python
def divide_numbers(a, b):
    # Bug: This will crash on zero, and the agent should catch it.
    return a / b

```


3. **Commit and push:**
```bash
git add .
git commit -m "Add division feature"
git push origin feature/broken-logic

```



### Phase 4: The PR Review

1. Open GitHub.com and create a **Pull Request** for your new branch.
2. Navigate to the **Actions** tab. You will see "OpenCode Reviewer" start running.
3. Wait 1–2 minutes. Check the "Conversation" tab of your PR. If set up correctly, OpenCode should leave a comment suggesting a `try/except` block or a zero-check for your function.

## Day 13 Summary Checklist

| Task | Completed |
| --- | --- |
| Configured GitHub Secrets for API safety | ☐ |
| Wrote a YAML workflow for GitHub Actions | ☐ |
| Triggered a "Headless" run of OpenCode via a PR | ☐ |
| Observed the AI agent interacting as a "Reviewer" bot | ☐ |

### Pro-Tip: The "Self-Healing" CI

Advanced users set the Action to **Auto-Commit**. If OpenCode finds a trivial bug (like a linting error), you can configure the YAML to let it push the fix directly to your branch. *Caution: Only do this if you have high trust in your test suite!*

**How did it feel to see the agent comment on your code without you even being in the terminal? It's like having a 24/7 intern who never sleeps.** When you're ready, **Day 14** is the **Real-World Lab**. We’ll find an actual "Good First Issue" on a public repo and use OpenCode to draft a professional contribution! Ready to go public?
<table><tr style="background-color:lightyellow;"><td>Q:</td><td>
Could you give me step-by-step instruction and create an exercise lab for Day 14?
</td></tr></table>


Welcome to **Day 14: The Real-World Contributor**.

Today is the "Capstone" of your technical training. You’ve mastered the agent locally, configured its brain, audited code, and even automated it in CI/CD. Now, we apply all of that to the world of **Open Source Software (OSS)**.

In a professional setting, you aren't just writing code for yourself; you're writing for a community. Today, you’ll learn how to use OpenCode to navigate a massive, unfamiliar repo, identify a "Good First Issue," and prepare a professional-grade Pull Request (PR) that maintainers will actually want to merge.

## Day 14: Navigating the Open Source Ecosystem

### 1. The OSS Workflow with an Agent

When contributing to a project you don't own, the workflow is slightly different:

1. **Fork & Clone:** You create your own copy of the repo.
2. **Context Injection:** You give the agent the **Issue Description** so it understands the "Why."
3. **The Fix:** Using Build Mode to solve the problem.
4. **The PR Draft:** Using the agent to write a clear, concise summary of the changes.

### 2. Identifying "Good First Issues"

GitHub has a specific label for beginners. You can find these by searching: `is:open is:issue label:"good first issue"`.

## Day 14 Lab: "Operation Open Source"

Since we are in a lab environment, we will simulate a real-world contribution to a popular (but manageable) repo. We’ll use the **`requests`** library (the gold standard for Python HTTP) or a similar sandbox.

### Phase 1: The Setup (The Fork)

1. **Open Ubuntu WSL.**
2. **Clone a "Sandbox" version of a repo** (for this lab, let's use a common tutorial repo to avoid "spamming" real maintainers):
```bash
git clone https://github.com/firstcontributions/first-contributions.git day14-oss
cd day14-oss

```


3. **Launch OpenCode:** `opencode .`

### Phase 2: Feeding the Issue Context

Instead of just saying "Fix this," we are going to copy a "Bug Report" into the agent's memory.

1. **Switch to Plan Mode.**
2. **The "Issue Injection" Prompt:**
> "I want to contribute to this repo. Here is an issue description: 'The current README is missing a section on how to run tests in a WSL environment. Users are getting confused about Docker integration.' Based on the files in `@.`, where should this information go, and what are the specific steps a WSL user needs to take?"



### Phase 3: The Surgical Fix (Build Mode)

1. **Switch to Build Mode.**
2. **The Fix Prompt:**
> "Update the `README.md` to include a 'WSL Setup' section. Use the instructions we verified on Day 1 of this course. Ensure the formatting matches the existing style of the document."


3. **Audit the Diff:** Make sure the agent didn't delete the original contributors' names or other vital info.

### Phase 4: The Professional PR Description

The secret to getting code merged isn't just the code—it's the **explanation**.

1. **The PR Prompt:**
> "I have completed the fix. Now, write a professional GitHub Pull Request description. Include:


> * A summary of the change.
> * Why this change is necessary (reference the 'WSL confusion' issue).
> * A checklist of what was tested."
>
>


2. **The Review:** Read what the agent wrote. Does it sound like a helpful human or a generic bot? (Hint: Use your **Day 3** rules to make it sound more like "you").

## Day 14 Summary Checklist

| Task | Completed |
| --- | --- |
| Navigated a repo you didn't create | ☐ |
| Injected an external "Issue Description" into the agent's context | ☐ |
| Performed a non-code contribution (Documentation/Markdown) | ☐ |
| Generated a high-quality PR description using the agent | ☐ |

### Pro-Tip: The "Linter" Check

Before you ever submit a PR in the real world, run your custom `/audit` command from **Day 7** or **Day 9**. Maintainers hate "nitpick" errors (like trailing spaces). Let the agent clean those up so the human maintainer only has to focus on your logic.

**How did the PR description turn out? Did the agent manage to capture the "vibe" of the repo?** Tomorrow is **Day 15: The Grand Finale**. We are going to do a **"Vibe Coding" session** where you build an entire application from scratch using only high-level conversation. Would you like to move to the final day?
<table><tr style="background-color:lightyellow;"><td>Q:</td><td>
Could you give me step-by-step instruction and create an exercise lab for Day 15?
</td></tr></table>


Welcome to **Day 15: The Grand Finale — Vibe Coding**.

You’ve spent 14 days learning the mechanics: the terminal, the config files, the security audits, and the custom skills. Today, we put the "Developer" in the passenger seat and the "Architect" in the driver’s chair.

**Vibe Coding** is a paradigm where you describe the *intent*, *feel*, and *logic* of an application in high-level language, and let OpenCode manage the boilerplate, the imports, and the syntax. Your job is to provide the "vibe" and course-correct.

## Day 15: Scaling Your Intent

### 1. The Multi-File "Vibe"

Vibe coding isn't about one-line snippets; it's about building a **system**. To do this effectively, you use **Plan Mode** to map out the architecture first, then **Build Mode** to execute.

### 2. The Feedback Loop

In this stage, you don't look at the code to find a missing semicolon. You look at the **functionality**.

* If the UI is ugly: *"Make it look more like a retro terminal."*
* If the logic is slow: *"Optimize the data fetching to be asynchronous."*

## Day 15 Lab: "The Smart Workspace Companion"

In this final lab, you will build a **CLI-based Productivity Dashboard** that tracks your tasks, shows the local time in multiple zones, and plays a notification sound when a timer ends.

### Phase 1: The Master Prompt (Plan Mode)

1. **Open Ubuntu WSL.**
2. **Create a clean directory:** `mkdir ~/day15-final && cd ~/day15-final`
3. **Launch OpenCode:** `opencode .`
4. **The "Vibe" Prompt:**
> "I want to build a productivity tool called 'VibeDash'. It should have a Pomodoro timer, a persistent to-do list saved to a JSON file, and a 'World Clock' section for London, Tokyo, and New York. Use a TUI library like `Rich` or `Textual` to make it look professional in the terminal. **Plan the architecture first.**"



### Phase 2: Initializing the Project

1. **Run the Init Command:** Inside the OpenCode TUI, type:
> `/init`
> *(This command in the 2026 version of OpenCode generates an `AGENTS.md` file that acts as the 'Memory' for your project's rules and structure.)*



### Phase 3: The Build (Iterative Refinement)

1. **Switch to Build Mode.**
2. **Step 1:** *"Implement the basic layout and the World Clock."*
3. **Step 2:** *"Add the JSON-backed To-Do list logic. Allow me to add and delete tasks via the terminal."*
4. **Step 3:** *"Add the Pomodoro timer. When it hits zero, use a system beep or a terminal notification to alert me."*

### Phase 4: The "Final Polish"

1. **The Visual Vibe:** *"The layout feels cramped. Move the World Clock to a sidebar and use neon-cyan colors for the timer."*
2. **The Audit:** Use your Day 7 skills:
> `/review`
> *"Check for any potential file-lock issues when saving the JSON task list."*



## Day 15 Summary Checklist

| Task | Completed |
| --- | --- |
| Built a multi-feature application from a single vision | ☐ |
| Used `/init` to create a project-specific instruction set | ☐ |
| Refined UI/UX using only natural language descriptions | ☐ |
| Successfully managed state (JSON) and time (Timer/Clock) | ☐ |

### Congratulations! You’ve Graduated.

You’ve gone from "How do I install this?" to "I am orchestrating an AI agent to build complex systems." You are no longer just a coder; you are an **AI-Augmented Engineer**.

**What was the most surprising thing your agent built today? Did it choose a UI style you didn't expect?**

Your training is complete, but the tech changes every week. I recommend keeping your `~/.config/opencode/` folder backed up—it now contains your unique "flavor" of AI assistance.

Would you like me to generate a **Graduation Summary** of all the skills you've mastered over the last 15 days?

[Advanced Vibe Coding workflow with OpenCode](https://www.youtube.com/watch?v=7XQdp3hItX4)

This video demonstrates a real-world "Vibe Coding" session using OpenCode to build an entire web project from scratch, mirroring the workflow you just completed in this lab.