Yesterday was surgery; today is a full organ transplant. Welcome to **Day 6: Multi-File Refactoring**.

In professional software development, a single feature change rarely stays inside one file. If you change a database schema, you have to update the models, the API serializers, and the frontend types. Today, we’ll teach OpenCode how to coordinate these "ripples" across your codebase.

---

## Day 6: Coordinating Cross-File Changes

### 1\. The Multi-File Context Strategy

To refactor across files, the agent needs to see the **interconnections**. If you only point it at `file_a.py`, it won't know that `file_b.py` depends on it.

* **Pro Tip:** Use the `@` symbol for *all* involved files in your initial prompt so the agent builds a complete dependency graph in its "mind."

### 2\. The "Atomic" Transaction

When OpenCode refactors, it usually presents a sequence of diffs.

1. **File 1 (The Source):** It modifies the original logic.
2. **File 2 (The Consumer):** It updates the code that calls that logic.
3. **New Files:** It creates any necessary supporting modules.

---

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

---

### Phase 4: Validation & Testing

Now, verify the agent didn't break the imports (a common AI mistake in WSL).

1. **Run the entry point:**

```bash
python3 app.py
```

2. **The Error Hunt:** If you get an `ImportError`, don't fix it manually!
* **Prompt the agent:** 

    > "I got an `ImportError`. Look at `@terminal` and fix the import paths in `@app.py` or `@services.py`."

---

## Day 6 Summary Checklist

| Task | Completed |
| --- | --- |
| Split a single file into at least 3 distinct modules | ☐ |
| Successfully managed cross-file imports using the AI | ☐ |
| Verified that the logic remains identical after the split | ☐ |
| Used **`@`** to reference multiple files in one prompt | ☐ |

---

### Pro-Tip: The "Dry Run" Check

Before applying a multi-file refactor, I always ask: *"Before you edit, list the exact imports you plan to add to each file."* This forces the agent to think about the file paths (like `from .database import save_to_db`) which is where most AI-generated code fails.

**How did the "Great Decoupling" go? Did the agent remember to add the `import` statements, or did you have to nudge it?** When you're ready, **Day 7** is all about **The Auditor**, where we use the agent to find security holes and performance bottlenecks in the code we just wrote!

<div style="background-color:lightgreen;">

## 實測

</div>

### Phase 1: Create the Monolith

```bash
~/git/snippet$ cd /tmp/
/tmp$ mkdir day6-lab && cd day6-lab
/tmp$ code app.py
/tmp$ opencode .
```

- 貼上範例 `app.py` 的內容

### Phase 2: The Multi-File Refactor

- 貼上提示詞
    > I want to clean this up. Move the `save_to_db` function into a new file called `database.py`. Move the `process_user_data` logic into `services.py`. Update `app.py` to import these functions and keep the main execution logic there. Ensure all files are correctly linked.

### Phase 3: Reviewing the Chain

- 實際上並不需要按 `Apply` 就已經有完成對應的修改。
- 額外呼叫 `/review` 觀察 LLM 如何驗證更動

### Phase 4: Validation & Testing

- 可能新的 LLM 能力都夠強了，並沒有遇到 `import` 語法上的問題

### 結果：

- `/copy` 複製 session 的紀錄如下：

**Session ID:** ses_3942c54b1ffebrFFOB1h7cOvD0
**Created:** 2/17/2026, 9:39:20 PM
**Updated:** 2/17/2026, 9:42:03 PM

---

#### User

I want to clean this up. Move the `save_to_db` function into a new file called `database.py`.  Move the `process_user_data` logic into `services.py`. Update `app.py` to import these functions and keep the main execution logic there. Ensure all files are correctly linked.

---

#### Assistant (Build · minimax-m2.5-free · 4.9s)

_Thinking:_

The user wants to refactor their code by:
1. Moving `save_to_db` function to a new file called `database.py`
2. Moving `process_user_data` logic to `services.py`
3. Updating `app.py` to import these functions and keep main execution logic there

First, I need to see what files exist and understand the current structure. Let me explore the directory.

**Tool: glob**

**Input:**
```json
{
  "pattern": "**/*.py"
}
```

**Output:**
```
C:\Users\jazzw\AppData\Local\Temp\day6-lab\app.py
```

---

#### Assistant (Build · minimax-m2.5-free · 3.8s)

_Thinking:_

Let me read the app.py file to understand its structure.

**Tool: read**

**Input:**
```json
{
  "filePath": "C:\\Users\\jazzw\\AppData\\Local\\Temp\\day6-lab\\app.py"
}
```

**Output:**
```
<path>C:\Users\jazzw\AppData\Local\Temp\day6-lab\app.py</path>
<type>file</type>
<content>1: # A messy monolith that does everything
2: import json
3: 
4: def save_to_db(data):
5:     print(f"Connecting to database... Saving: {data}")
6: 
7: def process_user_data(name, age):
8:     if age < 18:
9:         status = "minor"
10:     else:
11:         status = "adult"
12: 
13:     user_record = {"name": name, "age": age, "status": status}
14:     save_to_db(user_record)
15:     return user_record
16: 
17: # Main execution
18: user = process_user_data("Alice", 30)
19: print(f"Processed: {user}")

(End of file - total 19 lines)
</content>
```

---

#### Assistant (Build · minimax-m2.5-free · 6.6s)

_Thinking:_

Now I understand the structure. I need to:
1. Create `database.py` with `save_to_db` function
2. Create `services.py` with `process_user_data` function (importing from database)
3. Update `app.py` to import both and keep main execution

Let me create the files:

**Tool: write**

**Input:**
```json
{
  "content": "def save_to_db(data):\n    print(f\"Connecting to database... Saving: {data}\")\n",
  "filePath": "C:\\Users\\jazzw\\AppData\\Local\\Temp\\day6-lab\\database.py"
}
```

**Output:**
```
Wrote file successfully.
```

**Tool: write**

**Input:**
```json
{
  "content": "from database import save_to_db\n\ndef process_user_data(name, age):\n    if age < 18:\n        status = \"minor\"\n    else:\n        status = \"adult\"\n\n    user_record = {\"name\": name, \"age\": age, \"status\": status}\n    save_to_db(user_record)\n    return user_record\n",
  "filePath": "C:\\Users\\jazzw\\AppData\\Local\\Temp\\day6-lab\\services.py"
}
```

**Output:**
```
Wrote file successfully.
```

**Tool: write**

**Input:**
```json
{
  "content": "from services import process_user_data\n\nuser = process_user_data(\"Alice\", 30)\nprint(f\"Processed: {user}\")\n",
  "filePath": "C:\\Users\\jazzw\\AppData\\Local\\Temp\\day6-lab\\app.py"
}
```

**Output:**
```
Wrote file successfully.
```

---

#### Assistant (Build · minimax-m2.5-free · 2.8s)

_Thinking:_

All files have been created/updated. Let me verify the refactored code works by running it.

**Tool: bash**

**Input:**
```json
{
  "command": "python app.py",
  "description": "Test the refactored code"
}
```

**Output:**
```
Connecting to database... Saving: {'name': 'Alice', 'age': 30, 'status': 'adult'}
Processed: {'name': 'Alice', 'age': 30, 'status': 'adult'}

```

---

#### Assistant (Build · minimax-m2.5-free · 2.5s)

_Thinking:_

The code runs successfully. Let me provide a quick summary of what was done.

Done. Created:
- `database.py` - contains `save_to_db`
- `services.py` - contains `process_user_data` (imports from database)
- `app.py` - imports from services and contains main execution

Verified it runs correctly.

---

#### User

---

#### Assistant (Build · minimax-m2.5-free · 49.6s)

**Tool: task**

**Input:**
```json
{
  "prompt": "You are a code reviewer. Your job is to review code changes and provide actionable feedback.\n\n---\n\nInput: \n\n---\n\n## Determining What to Review\n\nBased on the input provided, determine which type of review to perform:\n\n1. **No arguments (default)**: Review all uncommitted changes\n   - Run: `git diff` for unstaged changes\n   - Run: `git diff --cached` for staged changes\n   - Run: `git status --short` to identify untracked (net new) files\n\n2. **Commit hash** (40-char SHA or short hash): Review that specific commit\n   - Run: `git show `\n\n3. **Branch name**: Compare current branch to the specified branch\n   - Run: `git diff ...HEAD`\n\n4. **PR URL or number** (contains \"github.com\" or \"pull\" or looks like a PR number): Review the pull request\n   - Run: `gh pr view ` to get PR context\n   - Run: `gh pr diff ` to get the diff\n\nUse best judgement when processing input.\n\n---\n\n## Gathering Context\n\n**Diffs alone are not enough.** After getting the diff, read the entire file(s) being modified to understand the full context. Code that looks wrong in isolation may be correct given surrounding logic—and vice versa.\n\n- Use the diff to identify which files changed\n- Use `git status --short` to identify untracked files, then read their full contents\n- Read the full file to understand existing patterns, control flow, and error handling\n- Check for existing style guide or conventions files (CONVENTIONS.md, AGENTS.md, .editorconfig, etc.)\n\n---\n\n## What to Look For\n\n**Bugs** - Your primary focus.\n- Logic errors, off-by-one mistakes, incorrect conditionals\n- If-else guards: missing guards, incorrect branching, unreachable code paths\n- Edge cases: null/empty/undefined inputs, error conditions, race conditions\n- Security issues: injection, auth bypass, data exposure\n- Broken error handling that swallows failures, throws unexpectedly or returns error types that are not caught.\n\n**Structure** - Does the code fit the codebase?\n- Does it follow existing patterns and conventions?\n- Are there established abstractions it should use but doesn't?\n- Excessive nesting that could be flattened with early returns or extraction\n\n**Performance** - Only flag if obviously problematic.\n- O(n²) on unbounded data, N+1 queries, blocking I/O on hot paths\n\n**Behavior Changes** - If a behavioral change is introduced, raise it (especially if it's possibly unintentional).\n\n---\n\n## Before You Flag Something\n\n**Be certain.** If you're going to call something a bug, you need to be confident it actually is one.\n\n- Only review the changes - do not review pre-existing code that wasn't modified\n- Don't flag something as a bug if you're unsure - investigate first\n- Don't invent hypothetical problems - if an edge case matters, explain the realistic scenario where it breaks\n- If you need more context to be sure, use the tools below to get it\n\n**Don't be a zealot about style.** When checking code against conventions:\n\n- Verify the code is *actually* in violation. Don't complain about else statements if early returns are already being used correctly.\n- Some \"violations\" are acceptable when they're the simplest option. A `let` statement is fine if the alternative is convoluted.\n- Excessive nesting is a legitimate concern regardless of other style choices.\n- Don't flag style preferences as issues unless they clearly violate established project conventions.\n\n---\n\n## Tools\n\nUse these to inform your review:\n\n- **Explore agent** - Find how existing code handles similar problems. Check patterns, conventions, and prior art before claiming something doesn't fit.\n- **Exa Code Context** - Verify correct usage of libraries/APIs before flagging something as wrong.\n- **Exa Web Search** - Research best practices if you're unsure about a pattern.\n\nIf you're uncertain about something and can't verify it with these tools, say \"I'm not sure about X\" rather than flagging it as a definite issue.\n\n---\n\n## Output\n\n1. If there is a bug, be direct and clear about why it is a bug.\n2. Clearly communicate severity of issues. Do not overstate severity.\n3. Critiques should clearly and explicitly communicate the scenarios, environments, or inputs that are necessary for the bug to arise. The comment should immediately indicate that the issue's severity depends on these factors.\n4. Your tone should be matter-of-fact and not accusatory or overly positive. It should read as a helpful AI assistant suggestion without sounding too much like a human reviewer.\n5. Write so the reader can quickly understand the issue without reading too closely.\n6. AVOID flattery, do not give any comments that are not helpful to the reader. Avoid phrasing like \"Great job ...\", \"Thanks for ...\".",
  "description": "review changes [commit|branch|pr], defaults to uncommitted",
  "subagent_type": "build",
  "command": "review"
}
```

**Output:**
```
task_id: ses_3942ad205ffekxawVjZkI7uZTD (for resuming to continue this task if needed)

<task_result>
Since there's no git repository, I can't see a diff of changes. I'll review the current code:

## Code Review

### Issues Found

1. **services.py:4** - No input validation. If `age` is `None` or non-numeric, `age < 18` raises `TypeError`. If `name` is `None`, it gets stored directly in the dict.

2. **services.py:10** - No error handling around `save_to_db()`. If the database operation fails, the exception propagates uncaught, and the caller receives no indication of failure—yet the function still returns `user_record` as if successful.

3. **database.py:1-2** - `save_to_db` has no return value. Callers can't distinguish between success/failure without exception handling.

4. **services.py:4** - Negative ages are treated as "minor". Depending on requirements, ages < 0 may need validation.

### Severity

- Items 1 and 2 are **medium severity** — runtime crashes possible with bad input or DB failures.
- Items 3 and 4 are **low severity** — design/validation concerns rather than bugs.

Would you like me to suggest fixes for any of these?
</task_result>
```

---

#### User

---

#### Assistant (Build · minimax-m2.5-free · 14.4s)

_Thinking:_

The user wants me to summarize the code review output and continue with my task. The previous task was to refactor the code, which I already completed. The code review found some issues:

1. No input validation in services.py for age/name
2. No error handling around save_to_db()
3. save_to_db has no return value
4. Negative ages treated as "minor"

Since the user said "continue with your task", I think they want me to address the issues found in the review. Let me ask which issues they want me to fix, or I could just fix the most important ones.

Actually, re-reading the context - the original task was to refactor the code into separate files, which I completed. The code review was a separate tool execution. The user now wants me to summarize and continue. 

I should summarize the findings briefly and ask if they want me to fix these issues.

The code review found 4 issues:

1. **services.py:4** - No input validation (None/non-numeric `age` causes TypeError)
2. **services.py:10** - No error handling for `save_to_db()` failures
3. **database.py:1** - `save_to_db` has no return value to indicate success/failure
4. **services.py:4** - Negative ages treated as "minor"

Items 1 and 2 are medium severity (runtime crashes possible). Items 3 and 4 are low severity.

Would you like me to fix any of these issues?

---

