<div style="background-color:lightyellow;">

## Day 2: Navigating the TUI & The "Plan-First" Workflow

### 1. Launching into "Project Mode"

Always launch OpenCode from the root of a project. This gives the agent the correct "context" of your file structure.

1. Open your Ubuntu terminal.
2. Navigate to your lab folder: `cd ~/opencode-lab`
3. Launch the interface: `opencode`

---

### 2. The Power of "Plan Mode" vs. "Build Mode"

In the TUI, you will see a toggle (usually at the top or switched via `Tab`).

* **Plan Mode (The Architect):** The agent can read files, search the web, and suggest logic, but it **cannot** write to your disk. It’s "Read-Only." Use this to brainstorm or explore.
* **Build Mode (The Engineer):** The agent has "Write" permissions. It can create files, delete code, and run terminal commands.

**The Golden Rule:** Never start in Build Mode. Always ask for a plan first to save your API tokens and prevent unwanted code changes.

---

### 3. Mastering the "@" Mentions

Just like on Discord or Slack, OpenCode uses the `@` symbol to focus the AI's "eyes" on specific things. Try these in the chat box:

* **`@file`**: Type `@` followed by a filename (e.g., `@sys_info.py`) to attach that specific file to your prompt.
* **`@folder`**: Attach an entire directory for context.
* **`@terminal`**: Sends the recent output of your terminal to the AI (great for debugging errors).
* **`@web`**: (If enabled) tells the agent to search the internet for documentation.

---

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

---

### 5. Essential Keyboard Shortcuts

To move fast in the OpenCode TUI, memorize these three:

| Shortcut | Action |
| --- | --- |
| `Tab` | Switch between Plan and Build modes |
| `Ctrl + C` | Cancel a running agent process (if it starts looping) |
| `Ctrl + L` | Clear the chat history to refresh the context window |
| `/` | Open the command menu (Connect, Settings, Clear) |

---

## Day 2 Success Checklist

* [ ] You successfully navigated between **Plan** and **Build** modes.
* [ ] You used the **`@`** symbol to reference a specific file.
* [ ] You understood why the agent recommended a specific file without it editing your code.

</div>

-----

<div style="background-color:lightgreen;">

## 實測

</div>

- 步驟中的 HuggingFace 測試 git repo 已經不存在
```bash
@jazzwang ➜ .../snippet/js/opencode/opencode-labs (master) $ git clone https://github.com/huggingface/chat-ui-template.git test-repo
Cloning into 'test-repo'...
remote: Repository not found.
fatal: repository 'https://github.com/huggingface/chat-ui-template.git/' not found
```
- 查了一下，可能已經更名為 https://github.com/huggingface/chat-ui
- 所以把步驟改成
```bash
@jazzwang ➜ .../snippet/js/opencode/opencode-labs (master) $ git clone https://github.com/huggingface/chat-ui test-repo
Cloning into 'test-repo'...
remote: Enumerating objects: 28881, done.
remote: Counting objects: 100% (1379/1379), done.
remote: Compressing objects: 100% (492/492), done.
remote: Total 28881 (delta 1143), reused 904 (delta 885), pack-reused 27502 (from 2)
Receiving objects: 100% (28881/28881), 10.40 MiB | 19.02 MiB/s, done.
Resolving deltas: 100% (19739/19739), done.
@jazzwang ➜ .../snippet/js/opencode/opencode-labs (master) $ cd test-repo/
@jazzwang ➜ .../js/opencode/opencode-labs/test-repo (main) $ opencode .
```
- 原本這一段 prompt 也不太合理，如果已經進到 `test-erpo` 子目錄底下才啟動 opencode，那就沒辦法用 `@test-repo` 來指定 `test-erpo` 子目錄
```
> "I'm new here. Using `@test-repo`, can you explain the project structure and tell me where the main entry point for the API is?"
```
- 因為 test-repo 內容可能不一樣，所以把 prompt 改成
```
Looking at @src/lib/server/apiToken.ts , what environment variables do I need to set up to make this work?
```
- 結果：
<div  style="background-color:lightgray;">

Based on `apiToken.ts`, you need these environment variables:

**If using user authentication:**
- `USE_USER_TOKEN=true` - Uses the authenticated user's token

**Otherwise (for API access):**
- `OPENAI_API_KEY` - Primary API key (used if `USE_USER_TOKEN` is not "true")
- `HF_TOKEN` - Fallback token (used if `OPENAI_API_KEY` is not set)

The priority order is:
1. User token (if `USE_USER_TOKEN=true` and user is authenticated)
2. `OPENAI_API_KEY`
3. `HF_TOKEN`

</div>