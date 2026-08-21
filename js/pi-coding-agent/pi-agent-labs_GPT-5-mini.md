Pi Agent Labs — 15×1-hour hands-on curriculum

Purpose

This lab series gets you productive with pi (pi-coding-agent) in 15 one-hour sessions. Each day has a clear goal, step-by-step instructions, commands to run, and a deliverable you can save to your session or repo.

Prerequisites

- Terminal (bash / PowerShell)
- Node.js + npm installed
- Network access (for installs and provider auth)
- Optional: API keys for model providers (OPENAI_API_KEY, ANTHROPIC_API_KEY, etc.)

How to use this lab file

- Work one day at a time. Each day is ~1 hour.
- Create a project directory for labs and run pi there, or run in your existing repo.
- Save artifacts (skills, extensions, prompts) under .pi/ or ~/.pi/agent as indicated so pi can auto-discover them.

Directory & file hints used in the labs

- Project-local pi assets: .pi/extensions/, .pi/skills/, .pi/prompts/, .pi/themes/
- Global config: ~/.pi/agent/

Curriculum overview (high level)

Day 1 — Install & explore UI
Day 2 — Editor, slash commands, thinking levels
Day 3 — Built-in tools (bash, read, write, edit)
Day 4 — Sessions & session files
Day 5 — Compaction & context management
Day 6 — Providers & switching models
Day 7 — Custom providers & model overrides
Day 8 — Skills: create and invoke a SKILL.md
Day 9 — Prompt templates and templating workflows
Day 10 — Extensions: minimal TypeScript extension
Day 11 — Extensions: event hooks and tool integration
Day 12 — Packages: install and inspect a pi package
Day 13 — RPC mode and get_session_stats
Day 14 — SDK: createAgentSession programmatic usage
Day 15 — End-to-end mini project (extension + skill)

Detailed day-by-day step-by-step instructions

Day 1 — Install & explore UI (Goal: run pi and learn the interface)

Time: 60 minutes

Steps:
1. Install pi (global):
   npm install -g @earendil-works/pi-coding-agent

2. Start pi in an empty or sample repo:
   pi

3. Explore the TUI:
   - Read the startup header listing loaded prompt templates, skills, and extensions.
   - Note footer information: working dir, session name, token/cache usage, cost, context usage, current model.

4. Try simple interactions:
   - Type a simple question: "List files in the current directory" and press Enter.
   - Run a shell command inline: !ls (or !dir on Windows).
   - Run a hidden shell command: !!echo hidden (this runs but is excluded from context).

5. Save results: use /export to write a session to HTML (optional):
   /export session.html

Deliverable: a short interactive session with a few messages and a saved export (optional). Note one or two observations about the UI.

Day 2 — Editor, slash commands, and thinking levels (Goal: editor productivity)

Time: 60 minutes

Steps:
1. In pi, open /hotkeys and study keyboard shortcuts (Ctrl+L model selector, Ctrl+P cycle scoped models, Shift+Enter multiline input).

2. Practice editor features:
   - Type @ to fuzzy-search files in the project.
   - Use Tab to complete paths.
   - Use Shift+Enter to insert a newline and Enter to submit.
   - Paste an image (Ctrl+V) if supported and ask the model to describe it.

3. Switch thinking levels:
   - Use /settings or type /thinking and set to minimal, medium, high. Observe response length and style differences.

4. Use /model to view available models, then switch to a different model.

Deliverable: a short note written in the session that records which thinking level you prefer for code tasks and a comparison of two model responses.

Day 3 — Tools: bash, read, write, edit (Goal: let the model use built-in tools)

Time: 60 minutes

Steps:
1. In a repo with some files (or create a sample file):
   echo "console.log(\"hello\")" > sample.js

2. Ask the model to run a shell command (visible to model):
   "Run ls and summarize files" (the model will call the bash tool).

3. Use !! to run a hidden command (excluded from context):
   !!ls -la

4. Ask the model to read a file via the read tool: "Read sample.js and explain what it does."

5. Ask the model to modify a file; when it emits an edit tool call, review and accept.

6. Manually use edit/write tools if available to create or patch files via assistant tool calls.

Deliverable: the model modifies sample.js (or you apply a suggested edit) and you verify the file content.

Day 4 — Sessions & session management (Goal: understand JSONL session storage and branching)

Time: 60 minutes

Steps:
1. Run /session in pi and note session file path and ID. Example path: ~/.pi/agent/sessions/--<cwd>--/<timestamp>_<uuid>.jsonl

2. Open a separate terminal and inspect the session file:
   less ~/.pi/agent/sessions/<that-file>.jsonl

3. Use /tree to view the session tree. Create a branch by selecting an earlier user message and continuing from there.

4. Use /fork to create a new session from a previous message.

Deliverable: a forked session saved to ~/.pi/agent/sessions and a short note in your session explaining why you forked.

Day 5 — Compaction & context window management (Goal: learn /compact and automatic compaction)

Time: 60 minutes

Steps:
1. Create a long conversation (ask the assistant to summarize or repeat content until the session is long).

2. Run /compact and observe the compaction summary and replacement of older messages with a CompactionSummaryMessage.

3. Examine the footer: contextUsage.tokens and percent should reflect compaction.

4. Experiment with /compact "Summarize older messages focusing on TODOs" to supply custom compaction instructions.

Deliverable: a session where compaction was performed and the compaction summary message is present in the JSONL file.

Day 6 — Providers & switching models (Goal: work with different providers and models)

Time: 60 minutes

Steps:
1. If you have provider API keys, set them in the environment (example):
   export OPENAI_API_KEY=sk-...
   export ANTHROPIC_API_KEY=sk-ant-...

2. Start pi and run /model. Inspect provider lists (openai, anthropic, etc.).

3. Switch between two models and run the same prompt on both (for example, "Refactor this code to be more readable:") and compare outputs.

4. Note differences in costs and response styles.

Deliverable: a saved session containing the comparison and your notes about differences.

Day 7 — Custom providers & model overrides (Goal: register a simple provider or override model properties)

Time: 60 minutes

Steps:
1. Edit ~/.pi/agent/models.json or .pi/settings.json to add a model override snippet. Example (add under providers.openai.modelOverrides):

{
  "providers": {
    "openai": {
      "modelOverrides": {
        "gpt-4o": { "name": "gpt-4o (local-override)", "contextWindow": 200000 }
      }
    }
  }
}

2. Restart pi (or reload resources) and confirm the override appears in /model.

3. (Optional) Register a local Ollama provider by adding a provider entry per docs or using an extension.

Deliverable: a visible model override in /model and a short test run using the overridden model settings.

Day 8 — Skills: create and invoke a SKILL.md (Goal: author a simple skill)

Time: 60 minutes

Steps:
1. Create a directory .pi/skills/my-skill in your project:

mkdir -p .pi/skills/my-skill
cat > .pi/skills/my-skill/SKILL.md <<'SK'
# My Skill

This skill demonstrates a simple on-demand helper.

## Steps
1. The user runs /skill:my-skill
2. The skill prints a checklist for code review.

SK

2. Start pi and invoke the skill:
   /skill:my-skill

3. If the skill supports arguments (add a section in SKILL.md), test passing arguments: /skill:my-skill arg1 arg2

Deliverable: a skill that appears in the startup list and prints output when invoked.

Day 9 — Prompt templates and templating workflows (Goal: reusable prompt templates)

Time: 60 minutes

Steps:
1. Create .pi/prompts/code-review.md with contents:

cat > .pi/prompts/code-review.md <<'PR'
<!-- code-review.md -->
Review this code for bugs, security issues, and performance problems. Focus on: {{focus}}
PR

2. Start pi and expand the prompt by typing /code-review and supplying a value for {{focus}} (pi will prompt for variables).

3. Use the template on a code file: @src/index.js and ask for a review.

Deliverable: a prompt template used during a session and a saved review response.

Day 10 — Extensions: write a minimal TypeScript extension (Goal: add a simple tool/command)

Time: 60 minutes

Steps:
1. Create .pi/extensions/my-ext.ts with a minimal factory. Example:

mkdir -p .pi/extensions
cat > .pi/extensions/my-ext.ts <<'TS'
export default function (pi) {
  pi.registerCommand("hello", {
    description: "Say hello",
    handler: async () => {
      pi.notify("Hello from my-ext!");
    }
  });
}
TS

2. Start pi with the extension (either let resource loader auto-discover or run with explicit flag):
   pi --no-extensions -e ./.pi/extensions/my-ext.ts

3. Run /hello command.

Deliverable: a working extension that adds /hello and shows a notification.

Day 11 — Extensions: event hooks and tool integration (Goal: react to tool calls)

Time: 60 minutes

Steps:
1. Extend your extension to listen to events like "tool_call" or "assistant_message":

- Add pi.on("tool_call", (event) => { ... }) to log tool usage.

2. Modify the extension to write a short log file when a tool is invoked:
   - Append event info to .pi/logs/tool-calls.log

3. Test by asking assistant to run a tool (e.g., read or bash) and confirm the log entry is written.

Deliverable: extension logs a tool call to a local file and prints confirmation.

Day 12 — Packages & installing community packages (Goal: install a pi package)

Time: 60 minutes

Steps:
1. Search for packages on npm or GitHub (example: pi-ds4 or other community packages).

2. Install a package locally in project mode (recommended) or globally:
   pi install npm:@some/package -l

3. Run pi list to see installed packages and pi config to enable resources the package provides.

4. Use a skill or extension installed by the package and observe behavior.

Deliverable: one installed pi package contributing at least one usable resource (skill/extension/prompt).

Day 13 — RPC mode and get_session_stats (Goal: query session stats programmatically)

Time: 60 minutes

Steps:
1. Start pi in RPC mode in the project directory:
   pi --mode rpc

2. From another terminal, send a JSON line request to pi's stdin or simulate via a wrapper. Example request:
   echo '{"type":"get_session_stats"}' | nc -U /path/to/pi-rpc-socket  # platform-dependent

3. Observe response JSON with tokens and contextUsage. If you can't use unix sockets, run pi --mode rpc and paste the JSON request into stdin where pi reads it.

4. Parse the response to extract tokens and cost.

Deliverable: a JSON response showing tokens and cost, saved to a file for reference.

Day 14 — SDK: createAgentSession programmatic usage (Goal: use Node SDK to run prompts)

Time: 60 minutes

Steps:
1. Create a small Node project and install pi SDK (local dev may already have it in node_modules):

mkdir -p lab-sdk
cd lab-sdk
npm init -y
npm install @earendil-works/pi-coding-agent

2. Create script run.js with code similar to:

const { createAgentSession, AuthStorage, ModelRegistry, SessionManager } = require('@earendil-works/pi-coding-agent');
(async () => {
  const auth = AuthStorage.create();
  const registry = ModelRegistry.create(auth);
  const { session } = await createAgentSession({ sessionManager: SessionManager.inMemory(), authStorage: auth, modelRegistry: registry });
  const resp = await session.prompt('Summarize the files in the current directory');
  console.log('Assistant:', resp);
})();

3. Run node run.js and inspect output. Capture usage via session APIs if available.

Deliverable: script that prompts the agent and prints assistant response.

Day 15 — End-to-end mini project: extension + skill + CI checklist (Goal: combine what you learned)

Time: 60 minutes

Steps:
1. Create an extension .pi/extensions/ci-ext.ts that registers a tool "run-ci" which runs a simple lint/test command (eslint or npm test) and returns results as tool result.

2. Create a skill .pi/skills/ci-check/SKILL.md that instructs pi to run /skill:ci-check which invokes the run-ci tool and asks the assistant to summarize issues and produce a short fix list.

3. Run the skill in pi: /skill:ci-check and follow the workflow — the extension runs tests, the model summarizes, and the session stores the results.

4. Export the session or save the summary to a file via the write tool.

Deliverable: a working CI-check flow that runs a command, returns results, and gets summarized by the assistant.

Features not fully covered in these 15 labs

- Team deployments, credential governance, and enterprise-scale telemetry/ops
- Very large or complex provider compatibility tuning (advanced model compat flags)
- Rich custom TUI components beyond notifications and commands
- Full sub-agent workflows and integrated MCP systems (third-party packages exist)
- Publishing and testing pipelines for pi packages (packaging, CI for extensions)

References & resources

- Official docs: https://pi.dev/
- GitHub: https://github.com/earendil-works/pi
- Local installed docs: node_modules/@earendil-works/pi-coding-agent/README.md and docs/
- Context7 references used while authoring these labs: Context7 pi pages

Next steps

If you want, I can scaffold the project files for each lab (SKILL.md, example extension TS files, prompt templates, Node SDK script) so you can jump into each day's exercises quickly. Tell me whether you prefer project-local (.pi/) assets or global (~/.pi/agent/) placement.