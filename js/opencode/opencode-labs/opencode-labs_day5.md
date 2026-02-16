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

### Phase 2: Surgical Fixes

### Phase 3: Logical Surgery

### Phase 4: The Terminal Feedback Loop
