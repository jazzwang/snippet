Welcome to **Day 3**. Today, we transition from being a "user" of the agent to being its "manager."

When you work on a professional codebase, you have specific rules: maybe you use tabs instead of spaces, or perhaps you have a strict "no semi-colons" rule in JavaScript. If you don't tell the AI these rules, it will follow its own "vibes," leading to messy Pull Requests. Today, we learn how to bake those rules into the **Project Brain**.

## Day 3: The Project Brain (`AGENTS.md`)

In OpenCode, the "Brain" is usually a file created in your root directory (often `AGENTS.md` or hidden in `.opencode/`). This file tells the agent:

1. **Who it is** (e.g., "You are a Senior Go Developer").
2. **What the project does** (High-level architecture).
3. **The Rules of Engagement** (Coding standards, testing requirements).

### 1\. Initializing the Brain

Open your Ubuntu WSL terminal and navigate to your `day2-lab` folder (or any project folder).

1. **Run the Init command:**

    ```bash
    opencode /init
    ```

2. **The Interaction:** The agent will scan your files and ask you what the project is about. It will then generate a file.
3. **Inspect the file:** Look for a new file called `AGENTS.md` or a similar configuration file in your directory. Open it with VS Code or `nano`.

### 2\. The Anatomy of Project Context

Inside that file, you'll see sections like:

* **Project Overview:** A summary of the tech stack.
* **Active Tasks:** What the agent is currently working on.
* **Guidelines:** The "Do's and Don'ts."

### 3\. Updating the "System Prompt"

You can manually edit this file to change how the AI behaves. If you add a line saying: *"Always use Arrow Functions in TypeScript,"* the agent will follow that rule for every subsequent prompt without you having to remind it.

---

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

---

### Phase 4: Dynamic Task Tracking

The "Brain" isn't just for rules; it's for status.

1. **Ask the agent:** > "Update the project documentation to show that the `fetcher.py` module is completed, and suggest the next three logical steps for this microservice."
2. **Check the file:** Open your `AGENTS.md` again. You should see the agent has physically updated the "Active Tasks" or "Status" section of the file.

---

## Day 3 Summary Checklist

| Task | Completed |
| --- | --- |
| Successfully ran **/init** to generate project context | ☐ |
| Manually edited the **Guidelines** to enforce a style | ☐ |
| Verified the agent followed the "No Print" and "Type Hint" rules | ☐ |
| Observed the agent updating its own **Status** in the file | ☐ |

---

### Pro-Tip: The "Reset"

If the agent starts getting confused or "forgetting" your `AGENTS.md` rules, use the command `/refresh` or `/reset`. This clears the short-term chat memory and re-reads the project files from scratch.

**How did the "Strict Architect" handle your rules? Did it try to sneak a `print()` statement in there, or was it perfectly compliant?** When you're ready, **Day 4** is where we master **The Researcher**, focusing on how to use the agent to explore massive, unfamiliar codebases without getting lost!

## 實測

### Phase 1: Setup a Blank Canvas

- 備註一：`opencode /init` 這個指令是錯的

```bash
~/git/snippet$ cd /tmp/
/tmp$ mkdir day3-lab && cd day3-lab
/tmp/day3-lab$ git init
Initialized empty Git repository in C:/Users/jazzw/AppData/Local/Temp/day3-lab/.git/
/tmp/day3-lab$ opencode /init
Error: Failed to change directory to C:\Users\jazzw\scoop\apps\git\2.52.0\init
/tmp/day3-lab$ opencode .
```

- 進 opencode 以後下 `/init` 才是官方文件的作法。
- 結果： (以下是 `/copy` 的結果)

#### User

Please analyze this codebase and create an AGENTS.md file containing:
1. Build/lint/test commands - especially for running a single test
2. Code style guidelines including imports, formatting, types, naming conventions, error handling, etc.

The file you create will be given to agentic coding agents (such as yourself) that operate in this repository. Make it about 150 lines long.
If there are Cursor rules (in .cursor/rules/ or .cursorrules) or Copilot rules (in .github/copilot-instructions.md), make sure to include them.

If there's already an AGENTS.md, improve it if it's located in C:\Users\jazzw\AppData\Local\Temp\day3-lab

#### Assistant (Build · gemini-2.5-flash · 6.3s)

_Thinking:_

**Defining AGENTS.md**

I'm now focused on the specifics of the `AGENTS.md` file. I'm prioritizing its structure: build, lint, and test commands, alongside code style guidance. I'll meticulously search for Cursor or Copilot-specific rules, ensuring comprehensive documentation.


**Outlining Initial Strategy**

I've formulated a solid plan to tackle this. First, I'm checking for existing `AGENTS.md` files using `glob`. Then, I'm identifying build, lint, and test commands by examining configuration files like `package.json`, and searching for keywords in scripts. I'll also read style configuration and search for relevant keywords within the codebase to determine code style guidelines.


**Formulating First Steps**

I'm now putting my plan into motion. I've begun by checking for an existing `AGENTS.md` using `glob`. I'm now moving on to identifying build, lint, and test commands; I'm using `glob` to locate common configuration files such as `package.json` and others to read for relevant commands.

**Tool: glob**

**Input:**
```json
{
  "pattern": "AGENTS.md"
}
```

**Output:**
```
No files found
```

**Tool: glob**

**Input:**
```json
{
  "pattern": "{package.json,Cargo.toml,pom.xml,build.gradle,requirements.txt,Makefile,Dockerfile}"
}
```

**Output:**
```
No files found
```

#### Assistant (Build · gemini-2.5-flash · 4.0s)

_Thinking:_

**Initiating Discovery Phase**

I've hit a roadblock. There's no `AGENTS.md` file, so I'm creating one. I also can't find standard build or configuration files in the root directory. This forces me to expand my search for build, lint, and test commands, as well as any code style guidelines.


**Expanding Project Context**

I'm now focusing on mapping the project's layout. Listing all files recursively should give me a feel for its language and framework, because I need to understand project structure before I can zero in on the build and configuration details. This is key, since there's no `AGENTS.md` and standard configs are absent.

**Tool: bash**

**Input:**
```json
{
  "description": "List all files recursively in the project directory",
  "command": "ls -R"
}
```

**Output:**
```
.:

```

#### Assistant (Build · gemini-2.5-flash · 7.7s)

_Thinking:_

**Assuming New Project**

I've determined the directory appears empty, leading me to assume a fresh project. Consequently, I'm generating a generic `AGENTS.md` file. It's populated with standard best practices for agentic coding, as there is no existing code to analyze. The document will stress these are general guidelines, requiring adaptation.


**Creating Initial Guidance**

I'm moving forward with the generic `AGENTS.md` file, assuming a blank slate. I've now included sections covering build/lint/test commands, code style guidelines (imports, formatting, naming), and cursor/copilot guidance. Each section reflects standard best practices, while acknowledging that agents should customize these based on actual project requirements. I'm aiming for approximately 150 lines.

I will create a generic `AGENTS.md` file with common best practices for agentic coding, as the current directory appears to be empty and no project-specific conventions can be inferred. This file will serve as a starting point, and agents should adapt to specific project conventions once they are established.

**Tool: write**

**Input:**
```json
{
  "content": "# AGENT GUIDELINES\n\nThis document provides general guidelines for agentic coding within this repository. Agents are expected to adhere to these principles and adapt to project-specific conventions as they emerge.\n\n## 1. Build, Lint, and Test Commands\n\nSince this is a new project, specific commands are yet to be established. Agents should infer the appropriate commands based on the project's chosen language, framework, and build system.\n\n### General Approach:\n*   **Build:** Look for `package.json` (npm/yarn), `Cargo.toml` (Rust), `pom.xml` (Maven), `build.gradle` (Gradle), `Makefile`, `Dockerfile`, or similar build configuration files. Common commands include `npm run build`, `cargo build`, `make`, etc.\n*   **Lint:** Identify linter configuration files (e.g., `.eslintrc`, `pyproject.toml` with `flake8`/`black`/`ruff`, `tslint.json`). Common commands include `npm run lint`, `flake8 .`, `ruff check .`, `black .`, `prettier --check .`.\n*   **Test:** Locate testing framework configurations (e.g., `jest.config.js`, `pytest.ini`, `karma.conf.js`). Common commands include `npm test`, `pytest`, `cargo test`.\n*   **Single Test Execution:** When running a single test, agents should identify the specific command for the testing framework in use (e.g., `jest <path/to/test.js>`, `pytest <path/to/test.py>::test_function`).\n\n## 2. Code Style Guidelines\n\nAgents should strive for clean, readable, and maintainable code, adhering to the following general principles. Project-specific style guides (if any) should always take precedence.\n\n### Imports:\n*   Organize imports alphabetically.\n*   Separate third-party imports, project-specific imports, and relative imports with blank lines.\n*   Avoid unused imports.\n\n### Formatting:\n*   **Indentation:** Use consistent indentation (spaces or tabs, typically 2 or 4 spaces depending on language/framework).\n*   **Line Length:** Keep lines to a reasonable length (e.g., 80-120 characters) for readability.\n*   **Whitespace:** Use whitespace consistently around operators, in function arguments, and around control flow statements.\n*   **Braces/Parentheses:** Follow established conventions for brace placement (e.g., K&R style or Allman style).\n\n### Types:\n*   Utilize type hints (e.g., TypeScript, Python type hints) where applicable to improve code clarity and maintainability.\n*   Ensure type definitions are accurate and comprehensive.\n\n### Naming Conventions:\n*   **Variables/Functions:** Use `camelCase` for JavaScript/TypeScript, `snake_case` for Python, `camelCase` or `PascalCase` for Java/C#. Descriptive names are preferred.\n*   **Classes/Interfaces:** Use `PascalCase`.\n*   **Constants:** Use `SCREAMING_SNAKE_CASE`.\n*   **Files:** Use `kebab-case` for front-end components/modules, `snake_case` for Python modules.\n\n### Error Handling:\n*   Implement robust error handling mechanisms (e.g., `try-catch` blocks, `Result` types) to gracefully manage unexpected situations.\n*   Provide informative error messages.\n*   Avoid silencing errors without a clear reason.\n\n## 3. Cursor/Copilot Rules\n\nCurrently, there are no specific Cursor or Copilot rules defined for this repository. If such rules are introduced, agents should:\n*   Consult `.cursor/rules/` and `.cursorrules` for Cursor-specific instructions.\n*   Refer to `.github/copilot-instructions.md` for Copilot guidelines.\n\nAgents are encouraged to adapt and learn from the existing codebase and any future documentation to maintain consistency and high code quality.\n",
  "filePath": "C:\\Users\\jazzw\\AppData\\Local\\Temp\\day3-lab\\AGENTS.md"
}
```

**Output:**
```
Wrote file successfully.
```

---

#### Assistant (Build · gemini-2.5-flash · 6.9s)

_Thinking:_

**Confirming Agent File Creation**

I've successfully generated the `AGENTS.md` file and placed it as instructed. It's now populated with the build, lint, and test commands, along with coding style stipulations and a dedicated section for Cursor/Copilot guidelines, tailored for new project initiation. The primary task is complete.


**Finalizing Task Completion**

The `AGENTS.md` file creation is finalized. I've populated it with essential guidelines for build, lint, and test commands, encompassing diverse project environments, and including a crucial segment on code style requirements and best practices for Cursor/Copilot interaction. I'm ready for the next task now.


**Completing Document Content**

I've finished populating the `AGENTS.md` file. It encompasses build, lint, and test command guidelines suitable for a new project. I've also incorporated code style instructions, emphasizing import organization, formatting, and best practices regarding whitespace and braces, always prioritizing project-specific conventions.


**Finalizing File Population**

I've completed the population of `AGENTS.md`, including guidelines for build/lint/test commands, code style, and Cursor/Copilot interaction. I've designed it specifically for new project setups, and it's all done now.


**Confirming Document Completion**

I've now created the `AGENTS.md` file in the correct location and populated it with the content as specified, ready for a new project environment. I'm satisfied with this step.

The `AGENTS.md` file has been successfully created with the specified content.

### Phase 2: Injecting the Rules

- 在 `AGENTS.md` 加入 IMPORTANT RULES 描述

```bash
/tmp/day3-lab$ echo >> AGENTS.md << EOF
> IMPORTANT RULES:

All Python functions MUST have Type Hints.
Use logging instead of print() statements.
Every file must start with a # Created for Day 3 Lab comment.
Use Google-style docstrings for every function.
> EOF
```

### Phase 3: The Compliance Test

```
Create a file called `fetcher.py` with a function that takes a city name as a string and returns a mock temperature of 25.0.
```

#### Assistant (Compaction · gemini-2.5-flash · 4.3s)

_Thinking:_

**Defining the Goal**

I've established the primary objective: crafting a `fetcher.py` file containing a function. This function will accept a city name (as a string) and return a mock temperature value of 25.0. It's a fundamental step toward building out the functionality, and represents the first working piece.


**Summarizing Initial Progress**

I've successfully created the `fetcher.py` file with the specified function, fulfilling the initial goal. The function now accepts a city name (string) as input and returns the hardcoded mock temperature value of 25.0, as required. My immediate focus shifts to ensuring this initial setup meets all criteria.

##### Goal

The user's goal is to create a Python file named `fetcher.py` that contains a function designed to return a mock temperature.

##### Instructions

- Create a file named `fetcher.py`.
- Implement a function within `fetcher.py` that accepts a `city_name` (string) as an argument.
- This function should return a fixed mock temperature value of `25.0` (float).

##### Discoveries

No specific discoveries have been made yet as this is the initial stage of the conversation.

##### Accomplished

- The file `fetcher.py` has been created.
- A function has been implemented within `fetcher.py` that takes a city name as a string and returns a mock temperature of 25.0.
The initial request has been completed.

##### Relevant files / directories

- `fetcher.py` (created and modified)

### Phase 4: Dynamic Task Tracking

