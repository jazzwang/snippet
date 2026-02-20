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

<div style="background-color:lightgreen;">

## 實測

</div>

### Phase 1: Setup the "Vulnerable Patient"

```bash
~/git/snippet/js/opencode/opencode-labs$ cd /tmp/
/tmp$ mkdir day7-lab && cd day7-lab
/tmp/day7-lab$ code vulnerable_app.py
/tmp/day7-lab$ opencode .
```
- 貼上範例

### Phase 2: The Security Audit (Plan Mode)

- 切到 "Plan Mode"
- 輸入提示詞：
> Perform a security and performance audit of `@vulnerable_app.py`. Identify at least three major issues and explain the risks associated with each.

### Phase 3: The Surgical Patch (Build Mode)

- 切到 "Build Mode"
- 輸入提示詞：
> Fix the SQL injection vulnerability using parameterized queries. Then, move the `API_KEY` to an environment variable lookup using the `os` module. Finally, optimize the `calculate_data` function to run in O(n) time instead of O(n^2).

### Phase 4: Verification

### 結果

- session `/copy` 的結果：

**Session ID:** ses_38edd59f1ffeLvIf0kGoZVTqF5
**Created:** 2/18/2026, 10:23:42 PM
**Updated:** 2/18/2026, 10:27:05 PM


#### User

Perform a security and performance audit of `@vulnerable_app.py`. Identify at least three major issues and explain the risks associated with each.


#### Assistant (Plan · minimax-m2.5-free · 3.7s)

_Thinking:_

The user wants me to perform a security and performance audit of `@vulnerable_app.py`. This appears to be a file that exists in the working directory. However, I'm in "Plan Mode" which means I can only read and analyze - I cannot make any edits or modifications.

Let me first read the file to understand what it contains, then identify security and performance issues.

**Tool: glob**

**Input:**
```json
{
  "pattern": "**/*vulnerable_app.py"
}
```

**Output:**
```
C:\Users\jazzw\AppData\Local\Temp\day7-lab\vulnerable_app.py
```


#### Assistant (Plan · minimax-m2.5-free · 2.6s)

_Thinking:_

Found the file. Let me read its contents to analyze the security and performance issues.

**Tool: read**

**Input:**
```json
{
  "filePath": "C:\\Users\\jazzw\\AppData\\Local\\Temp\\day7-lab\\vulnerable_app.py"
}
```

**Output:**
```
<path>C:\Users\jazzw\AppData\Local\Temp\day7-lab\vulnerable_app.py</path>
<type>file</type>
<content>1: import sqlite3
2: 
3: # VULNERABILITY 1: Hardcoded Secret
4: API_KEY = "sk-12345-secret-key-do-not-share"
5: 
6: def get_user_data(username):
7:     db = sqlite3.connect("users.db")
8:     cursor = db.cursor()
9: 
10:     # VULNERABILITY 2: SQL Injection (Direct string formatting)
11:     query = f"SELECT * FROM users WHERE username = '{username}'"
12:     cursor.execute(query)
13:     return cursor.fetchone()
14: 
15: def calculate_data(numbers):
16:     # VULNERABILITY 3: Performance Bottleneck (O(n^2) for no reason)
17:     result = []
18:     for i in numbers:
19:         for j in numbers:
20:             if i == j:
21:                 result.append(i)
22:     return list(set(result))
23: 
24: print("App is running...")

(End of file - total 24 lines)
</content>
```


#### Assistant (Plan · minimax-m2.5-free · 9.7s)

_Thinking:_

I've now read the file. Let me analyze the security and performance issues:

1. **Hardcoded Secret (Line 4)**: API_KEY is hardcoded in plain text. This is a critical security vulnerability - secrets should never be hardcoded and should be loaded from environment variables or a secure vault.

2. **SQL Injection (Line 11)**: The username parameter is directly interpolated into the SQL query using f-string formatting. This allows an attacker to inject malicious SQL code. This is a critical security vulnerability.

3. **Performance Bottleneck (Lines 17-22)**: The `calculate_data` function has O(n²) complexity for what appears to be finding unique values. This can be replaced with a simple O(n) set operation. Additionally, there's a bug - it returns `list(set(result))` at the end but the nested loop with `if i == j` would add duplicates, so the set() call is there to fix that, but it's inefficient.

Let me provide a comprehensive audit report to the user.

## Security & Performance Audit Report for `vulnerable_app.py`

### Issue 1: Hardcoded Secret (Critical - Line 4)
```python
API_KEY = "sk-12345-secret-key-do-not-share"
```
**Risk**: Anyone with code access can read this API key. If committed to version control, it's exposed publicly. Attackers can use this key to authenticate as your application.


### Issue 2: SQL Injection (Critical - Line 11)
```python
query = f"SELECT * FROM users WHERE username = '{username}'"
```
**Risk**: An attacker can input `' OR '1'='1` as username to bypass authentication, extract all user data, or potentially execute arbitrary SQL commands (depending on DB permissions).


### Issue 3: Performance Bottleneck - O(n²) Algorithm (Medium - Lines 17-22)
```python
for i in numbers:
    for j in numbers:
        if i == j:
            result.append(i)
```
**Risk**: This is O(n²) complexity for a simple deduplication task. For 10,000 items, this performs 100,000,000 iterations. Should be `list(set(numbers))` which is O(n).


### Issue 4: Missing DB Connection Cleanup (Medium - Lines 7-13)
The database connection is opened but never closed, causing resource leaks.


Would you like me to create a plan showing how to fix these issues?


#### User

Fix the SQL injection vulnerability using parameterized queries. Then, move the `API_KEY` to an environment variable lookup using the `os` module.Finally, optimize the `calculate_data` function to run in O(n) time instead of O(n^2).


#### Assistant (Build · minimax-m2.5-free · 3.7s)

_Thinking:_

The user wants me to fix the three issues:
1. Fix SQL injection with parameterized queries
2. Move API_KEY to environment variable using os module
3. Optimize calculate_data from O(n²) to O(n)

Let me make these edits to the file.

**Tool: edit**

**Input:**
```json
{
  "filePath": "C:\\Users\\jazzw\\AppData\\Local\\Temp\\day7-lab\\vulnerable_app.py",
  "newString": "import os\nimport sqlite3\n\nAPI_KEY = os.environ.get(\"API_KEY\", \"\")",
  "oldString": "import sqlite3\n\nAPI_KEY = \"sk-12345-secret-key-do-not-share\""
}
```

**Error:**
```
Error: You must read file C:\Users\jazzw\AppData\Local\Temp\day7-lab\vulnerable_app.py before overwriting it. Use the Read tool first
```


#### Assistant (Build · minimax-m2.5-free · 3.4s)

_Thinking:_

I need to re-read the file first since it's a new conversation turn.

**Tool: read**

**Input:**
```json
{
  "filePath": "C:\\Users\\jazzw\\AppData\\Local\\Temp\\day7-lab\\vulnerable_app.py"
}
```

**Output:**
```
<path>C:\Users\jazzw\AppData\Local\Temp\day7-lab\vulnerable_app.py</path>
<type>file</type>
<content>1: import sqlite3
2: 
3: # VULNERABILITY 1: Hardcoded Secret
4: API_KEY = "sk-12345-secret-key-do-not-share"
5: 
6: def get_user_data(username):
7:     db = sqlite3.connect("users.db")
8:     cursor = db.cursor()
9: 
10:     # VULNERABILITY 2: SQL Injection (Direct string formatting)
11:     query = f"SELECT * FROM users WHERE username = '{username}'"
12:     cursor.execute(query)
13:     return cursor.fetchone()
14: 
15: def calculate_data(numbers):
16:     # VULNERABILITY 3: Performance Bottleneck (O(n^2) for no reason)
17:     result = []
18:     for i in numbers:
19:         for j in numbers:
20:             if i == j:
21:                 result.append(i)
22:     return list(set(result))
23: 
24: print("App is running...")

(End of file - total 24 lines)
</content>
```


#### Assistant (Build · minimax-m2.5-free · 3.4s)

_Thinking:_

Now I can make the edits. I'll do all three fixes.

**Tool: edit**

**Input:**
```json
{
  "filePath": "C:\\Users\\jazzw\\AppData\\Local\\Temp\\day7-lab\\vulnerable_app.py",
  "newString": "import os\nimport sqlite3\n\nAPI_KEY = os.environ.get(\"API_KEY\", \"\")",
  "oldString": "import sqlite3\n\n# VULNERABILITY 1: Hardcoded Secret\nAPI_KEY = \"sk-12345-secret-key-do-not-share\""
}
```

**Output:**
```
Edit applied successfully.
```


#### Assistant (Build · minimax-m2.5-free · 15.4s)

_Thinking:_

Now fix the SQL injection with parameterized query.

**Tool: edit**

**Input:**
```json
{
  "filePath": "C:\\Users\\jazzw\\AppData\\Local\\Temp\\day7-lab\\vulnerable_app.py",
  "newString": "def get_user_data(username):\n    db = sqlite3.connect(\"users.db\")\n    cursor = db.cursor()\n\n    query = \"SELECT * FROM users WHERE username = ?\"\n    cursor.execute(query, (username,))\n    return cursor.fetchone()",
  "oldString": "def get_user_data(username):\n    db = sqlite3.connect(\"users.db\")\n    cursor = db.cursor()\n\n    # VULNERABILITY 2: SQL Injection (Direct string formatting)\n    query = f\"SELECT * FROM users WHERE username = '{username}'\"\n    cursor.execute(query)\n    return cursor.fetchone()"
}
```

**Output:**
```
Edit applied successfully.
```


#### Assistant (Build · minimax-m2.5-free · 3.2s)

_Thinking:_

Now optimize the calculate_data function.

**Tool: edit**

**Input:**
```json
{
  "filePath": "C:\\Users\\jazzw\\AppData\\Local\\Temp\\day7-lab\\vulnerable_app.py",
  "newString": "def calculate_data(numbers):\n    return list(set(numbers))",
  "oldString": "def calculate_data(numbers):\n    # VULNERABILITY 3: Performance Bottleneck (O(n^2) for no reason)\n    result = []\n    for i in numbers:\n        for j in numbers:\n            if i == j:\n                result.append(i)\n    return list(set(result))"
}
```

**Output:**
```
Edit applied successfully.
```


#### Assistant (Build · minimax-m2.5-free · 1.8s)

_Thinking:_

All three fixes are done. Let me show the user the final result.

**Tool: read**

**Input:**
```json
{
  "filePath": "C:\\Users\\jazzw\\AppData\\Local\\Temp\\day7-lab\\vulnerable_app.py"
}
```

**Output:**
```
<path>C:\Users\jazzw\AppData\Local\Temp\day7-lab\vulnerable_app.py</path>
<type>file</type>
<content>1: import os
2: import sqlite3
3: 
4: API_KEY = os.environ.get("API_KEY", "")
5: 
6: def get_user_data(username):
7:     db = sqlite3.connect("users.db")
8:     cursor = db.cursor()
9: 
10:     query = "SELECT * FROM users WHERE username = ?"
11:     cursor.execute(query, (username,))
12:     return cursor.fetchone()
13: 
14: def calculate_data(numbers):
15:     return list(set(numbers))
16: 
17: print("App is running...")

(End of file - total 17 lines)
</content>
```


#### Assistant (Build · minimax-m2.5-free · 2.4s)

_Thinking:_

All fixes are complete. Let me summarize what was done.

Done. All three fixes applied:

1. **SQL Injection** - Now uses parameterized query with `?` placeholder (line 10-11)
2. **API_KEY** - Now reads from `os.environ.get("API_KEY", "")` (line 4)
3. **Performance** - Replaced O(n²) nested loop with O(n) `list(set(numbers))` (line 15)

To use the app, set the `API_KEY` environment variable before running.


## 反思

- 整個 Lab 並沒有提到 `/review` 的用法
- 重新貼上範例，然後用 `/review` 試試看
- 結論：`/review` 根據 help 的說明，是用來檢驗 commit/pr 的。不過這裡縱使不是一個 git repo，仍舊有檢驗到 security 問題。應該跟 LLM 的能力有關。參考 prompt 內容，是對 code changes 進行 code review 的動作使用。這段與 Gemini 3 生成的 Lab 說明有些出入。某種程度上也說明了大語言模型縱使參考了 Search 結果(Grounding) ，仍舊參考相對「直觀」的語意來進行生成的動作。

**Session ID:** ses_387052d2effeU704LSEc4mGcN6
**Created:** 2/20/2026, 10:57:09 AM
**Updated:** 2/20/2026, 10:57:41 AM

#### User

#### Assistant (Build · minimax-m2.5-free · 24.0s)

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
task_id: ses_387052cf0ffeqj9sxiYOYgSvi4 (for resuming to continue this task if needed)

<task_result>
## Code Review: `vulnerable_app.py`

### Issues Found

**1. SQL Injection (High Severity)** - Line 11
```python
query = f"SELECT * FROM users WHERE username = '{username}'"
```
User input is directly interpolated into SQL. An attacker could supply `username = "' OR '1'='1"` to bypass authentication or exfiltrate data.

**Fix**: Use parameterized queries:
```python
cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
```

**2. Hardcoded Secret (High Severity)** - Line 4
```python
API_KEY = "sk-12345-secret-key-do-not-share"
```
Secrets hardcoded in source control leak when code is committed, shared, or stored insecurely.

**Fix**: Use environment variables:
```python
import os
API_KEY = os.environ.get("API_KEY")
```

**3. Performance Issue (Low Severity)** - Lines 17-22
```python
for i in numbers:
    for j in numbers:
        if i == j:
            result.append(i)
return list(set(result))
```
This O(n²) algorithm is equivalent to `list(set(numbers))`, which is O(n).

**Fix**:
```python
return list(set(numbers))
```

### Summary
- 2 high-severity security issues (SQL injection, hardcoded secret)
- 1 performance issue

These appear to be intentionally vulnerable examples given the "VULNERABILITY" comments. If this is for learning purposes, the issues are clearly labeled. If this is production code, these must be fixed before deployment.
</task_result>
```

#### User

#### Assistant (Build · minimax-m2.5-free · 8.0s)

_Thinking:_

The user wants me to summarize the task tool output and continue with the task. Let me look at what was returned:

The task was a code review of `vulnerable_app.py` that found:

1. **SQL Injection (High Severity)** - Line 11 - User input directly interpolated into SQL query
2. **Hardcoded Secret (High Severity)** - Line 4 - API key hardcoded in source
3. **Performance Issue (Low Severity)** - Lines 17-22 - O(n²) algorithm that could be simplified to O(n)

The user wants me to summarize and continue. The task was already completed by the subagent - it provided a complete code review with findings. There's nothing more to "continue" since the review is done.

Let me provide a brief summary to the user.

The code review found 3 issues in `vulnerable_app.py`:

1. **SQL Injection (High)** - Line 11: User input directly interpolated into SQL query
2. **Hardcoded Secret (High)** - Line 4: API key hardcoded in source code
3. **Performance (Low)** - Lines 17-22: O(n²) loop that can be simplified to `list(set(numbers))`

The code appears to be intentionally vulnerable (has "VULNERABILITY" comments) - likely a learning example.

