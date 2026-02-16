Welcome to **Day 5: Single-File Surgery**.

Today, we transition from being an observer to being an operator. In "Build Mode," OpenCode doesn't just suggest ideas—it picks up the scalpel and modifies your source code. The goal today is to master **surgical precision**: making the smallest possible change to achieve a specific result while minimizing "code drift."

---

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

---

## Day 4 Recap vs. Day 5 Goal

While Day 4 was about **mapping 50 files**, Day 5 is about **perfecting one**.

---

## Day 5 Lab: "The Bug Hunter"

In this lab, you will intentionally create a broken script and use OpenCode to perform "surgery" to fix it.

### Phase 1: Create the "Patient"

1. **Open Ubuntu WSL.**
2. **Create a new file:**

```bash
mkdir ~/day5-lab && cd ~/day5-lab
touch validator.py
```

3. **Paste this "broken" code into `validator.py`** (it has a regex bug and a logic flaw):

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

---

### Phase 4: The Terminal Feedback Loop

1. **The Execution Prompt:**

    > "Run this script in the terminal and tell me if the output matches what we expect (False, False)."


2. **The Self-Correction:** If the output is still wrong, don't fix it yourself. Tell the agent:

    > "The terminal output was `True`. Re-examine the `check_password_strength` logic and try again."

---

## Day 5 Summary Checklist

| Task | Completed |
| --- | --- |
| Successfully toggled into **Build Mode** | ☐ |
| Reviewed a **Diff** and identified a specific change | ☐ |
| Applied a fix to a single function without touching the rest of the file | ☐ |
| Used the agent to execute the file and verify the fix | ☐ |

---

### Pro-Tip: Avoid "The Rewrite"

Sometimes AI agents get lazy and try to delete a 100-line file and replace it with 100 new lines just to change one variable. If you see a massive diff for a small change, **Cancel** it and say: *"Do not rewrite the whole file. Only modify the specific line where the error occurs."*

**How did the "Bug Hunter" lab go? Did the agent make a clean cut, or did it try to rewrite your whole script?** When you're ready, **Day 6** is the "level up" where we perform **Multi-File Refactoring**—making changes that span across different files at once!

<div style="background-color:lightgreen;">

## 實測

</div>

### Phase 1: Create the "Patient"

```bash
~$ cd /tmp/
/tmp$ mkdir day5-lab && cd day5-lab
/tmp/day5-lab$ touch validator.py
/tmp/day5-lab$ code validator.py
```

### Phase 2: Surgical Fixes

- 備註：原本文件使用 `opencode validator.py` 是不正確的

```bash
/tmp/day5-lab$ opencode .
```

- 輸入提示詞：

  > Look at the `validate_email` function in `@validator.py`. The regex is failing because it doesn't require a dot in the domain. Fix ONLY the regex string.

- 備註：其實不需要按 `Apply`

> 3. **Review the Diff:** Ensure it didn't rewrite the whole file—just the one line. Click **Apply**.

### Phase 3: Logical Surgery

- 輸入提示詞：

    > The `check_password_strength` function always returns True. Fix the logic so it returns True only if the password is longer than 8 characters and contains at least one number.



### Phase 4: The Terminal Feedback Loop

- 輸入提示詞：

    > Run this script in the terminal and tell me if the output matches what we expect (False, False).

### 結果

- session `/copy` 結果：

**Session ID:** ses_3994084c6ffegoauCSpdyDaYpQ
**Created:** 2/16/2026, 9:59:10 PM
**Updated:** 2/16/2026, 10:03:42 PM

---

#### User

Look at the `validate_email` function in `@validator.py`. The regex is failing because it doesn't require a dot in the domain. Fix ONLY the regex string.

---

#### Assistant (Build · minimax-m2.5-free · 5.2s)

_Thinking:_

The user wants me to look at a file called `@validator.py` (which seems like an unusual filename with the @ symbol), find the `validate_email` function, and fix the regex to require a dot in the domain. Let me first read this file.

**Tool: glob**

**Input:**
```json
{
  "pattern": "**/*validator*.py"
}
```

**Output:**
```
C:\Users\jazzw\AppData\Local\Temp\day5-lab\validator.py
```

---

#### Assistant (Build · minimax-m2.5-free · 5.6s)

_Thinking:_

Let me read the validator.py file to find the validate_email function.

**Tool: read**

**Input:**
```json
{
  "filePath": "C:\\Users\\jazzw\\AppData\\Local\\Temp\\day5-lab\\validator.py"
}
```

**Output:**
```
<path>C:\Users\jazzw\AppData\Local\Temp\day5-lab\validator.py</path>
<type>file</type>
<content>1: import re
2: 
3: def validate_email(email):
4:     # Bug: This regex is way too simple and misses the domain dot
5:     regex = r'^[a-z0-9]+@[a-z0-9]+$'
6:     if re.match(regex, email):
7:         return True
8:     return False
9: 
10: def check_password_strength(password):
11:     # Bug: This returns True even if the password is empty
12:     if len(password) > 8:
13:         return True
14:     else:
15:         return True
16: 
17: print(validate_email("test@example")) # Should be False
18: print(check_password_strength(""))    # Should be False

(End of file - total 18 lines)
</content>
```

---

#### Assistant (Build · minimax-m2.5-free · 3.2s)

_Thinking:_

I can see the issue. The regex `r'^[a-z0-9]+@[a-z0-9]+$'` doesn't include a dot in the domain part. I need to add a dot to the domain portion of the regex. The domain part should be something like `[a-z0-9]+\.[a-z0-9]+` to require at least one dot.

Let me fix just the regex string.

**Tool: edit**

**Input:**
```json
{
  "filePath": "C:\\Users\\jazzw\\AppData\\Local\\Temp\\day5-lab\\validator.py",
  "newString": "    regex = r'^[a-z0-9]+@[a-z0-9]+\\.[a-z0-9]+$'",
  "oldString": "    regex = r'^[a-z0-9]+@[a-z0-9]+$'"
}
```

**Output:**
```
Edit applied successfully.
```

---

#### Assistant (Build · minimax-m2.5-free · 2.1s)

_Thinking:_

I've added the dot requirement to the domain part of the regex. The pattern `[a-z0-9]+\.[a-z0-9]+` now requires at least one dot in the domain.

Fixed. The regex now requires a dot in the domain: `r'^[a-z0-9]+@[a-z0-9]+\.[a-z0-9]+$'`

---

#### User

The `check_password_strength` function always returns True. Fix the logic so it returns True only if the password is longer than 8 characters and contains at least one number.

---

#### Assistant (Build · minimax-m2.5-free · 4.0s)

_Thinking:_

The user wants me to fix the check_password_strength function. Looking at the current code:

```python
def check_password_strength(password):
    # Bug: This returns True even if the password is empty
    if len(password) > 8:
        return True
    else:
        return True
```

It always returns True. I need to:
1. Return False if password is 8 characters or less
2. Return False if password doesn't contain at least one number
3. Return True only if both conditions are met

Let me edit this function.

**Tool: edit**

**Input:**
```json
{
  "filePath": "C:\\Users\\jazzw\\AppData\\Local\\Temp\\day5-lab\\validator.py",
  "newString": "def check_password_strength(password):\n    if len(password) > 8 and any(c.isdigit() for c in password):\n        return True\n    return False",
  "oldString": "def check_password_strength(password):\n    # Bug: This returns True even if the password is empty\n    if len(password) > 8:\n        return True\n    else:\n        return True"
}
```

**Output:**
```
Edit applied successfully.
```

---

#### Assistant (Build · minimax-m2.5-free · 2.0s)

_Thinking:_

Done. The function now returns True only if the password is longer than 8 characters AND contains at least one digit.

Fixed. The function now returns True only when the password is longer than 8 characters **and** contains at least one digit.

---

#### User

Run this script in the terminal and tell me if the output matches what we expect (False, False).

---

#### Assistant (Build · minimax-m2.5-free · 2.6s)

_Thinking:_

The user wants me to run the validator.py script to check if the output is False, False.

**Tool: bash**

**Input:**
```json
{
  "command": "python validator.py",
  "description": "Run validator.py script"
}
```

**Output:**
```
False
False
```

---

#### Assistant (Build · minimax-m2.5-free · 1.6s)

_Thinking:_

The output is False, False which matches what the user expected. Let me confirm this to them.

Yes, the output is `False, False` - matching the expected result.

---

