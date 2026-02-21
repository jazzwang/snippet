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

<div style="background-color:lightgreen">

## 實測

</div>

### Phase 1: Create the Command Script

```bash
~/git/snippet/js/opencode$ cd /tmp
/tmp$ mkdir -p ~/.config/opencode/commands
/tmp$ cat > ~/.config/opencode/commands/ui-checker.sh << EOF
#!/bin/bash
echo "--- RUNNING UI AUDIT ---"
# This simulates finding a problem in a file
grep -rn "inline-style" .
echo "--- AUDIT COMPLETE ---"
EOF
/tmp$ chmod a+x ~/.config/opencode/commands/ui-checker.sh
```

### Phase 2: Registering the Command with OpenCode

```bash
/tmp$ cat ~/.config/opencode/config.yaml
cat: /c/Users/jazzw/.config/opencode/config.yaml: No such file or directory
/tmp$ cat >> ~/.config/opencode/config.yaml << EOF
custom_commands:
  - name: "audit-ui"
    description: "Checks for forbidden inline styles in HTML/CSS"
    executable: "~/.config/opencode/commands/ui-checker.sh"
    system_prompt: "When this command runs, look for any 'inline-style' mentions in the output. Immediately propose a refactor to move those styles to a separate CSS file."
> EOF
```

### Phase 3: The Live Test

```bash
/tmp$ mkdir day9-lab && cd day9-lab
/tmp/day9-lab$ echo '<div style="color: red;">Hello World</div>' > index.html
/tmp/day9-lab$ opencode .
```
- 輸入指令 `/audit-ui`
- 觀察結果