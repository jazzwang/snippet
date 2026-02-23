Welcome to **Day 11: Building Custom Skills**.

Today, we go "Meta." Yesterday, you used built-in skills like the web browser. Today, you will actually **program the agent's brain** to use a tool that doesn't exist yet.

In OpenCode (and many similar agent frameworks), a **Custom Skill** is a script paired with a "Manifest" that tells the AI: *"Here is a new superpower you have, here is how to call it, and here is what to expect back."*

## Day 11: The Architecture of a Custom Skill

### 1\. The Skill Payload

A skill consists of two parts:

* **The Logic:** A script (usually Python or Bash) that performs an action (e.g., querying a Jira ticket, checking GPU temperature, or interacting with a proprietary API).
* **The JSON Schema:** A description the LLM reads. It defines the **parameters** the agent needs to provide to use the tool.

### 2\. Why "Skills" over "Commands"?

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

<div style="background-color:lightgreen;">

## 實測

</div>

- 有前車之鑑，從 Day 9 以後，「幻覺」很嚴重。所以還是直接查官方文件，看怎麼新增一個 Skill
- 根據官方文件 https://opencode.ai/docs/skills/，這裡採用 project setting 新增一個 `.opencode/skills/check_system_resources/SKILL.md`
- 從文件的內容看起來，Skill 算是 Tools 底下的一部分

### Phase 1: Create the Skill Logic

```bash
~/git/snippet/js/opencode/opencode-labs$ cd /tmp/
/tmp$ mkdir day11-lab && cd day11-lab
/tmp/day11-lab$ mkdir -p .opencode/skills/check_system_resources/
/tmp/day11-lab$ cat > .opencode/skills/check_system_resources/SKILL.md << EOF
------
name: check_system_resources
description: Checks the current CPU and RAM usage.
------
!\`python3 .opencode/skills/check_system_resources/monitor.py\`
EOF
/tmp/day11-lab$ cat > .opencode/skills/check_system_resources/monitor.py << EOF
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
EOF
/tmp/day11-lab$ pip3 install psutil
/tmp/day11-lab$ opencode .
```
- 使用 opencode 的 `/skills` 指令，可是查不到 `check_system_resources` 這個 skill。