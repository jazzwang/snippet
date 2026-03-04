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
   - Go to your repo on GitHub.com.
   - Navigate to **Settings > Secrets and variables > Actions**.
   - Add a **New repository secret**:
   - Name: `OPENCODE_API_KEY`
   - Value: (Your OpenAI or Anthropic key)

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

**How did it feel to see the agent comment on your code without you even being in the terminal? It's like having a 24/7 intern who never sleeps.**

When you're ready, **Day 14** is the **Real-World Lab**. We’ll find an actual "Good First Issue" on a public repo and use OpenCode to draft a professional contribution! Ready to go public?

<div style="background-color:lightgreen;">

## 實測

</div>

### Phase 1: Setup a GitHub Repo from WSL

- 建立測試用 Github Repo

```bash
~$ cd /tmp/
/tmp$ mkdir day13-ci && cd day13-ci
/tmp/day13-ci$ git init
Initialized empty Git repository in C:/Users/jazzw/AppData/Local/Temp/day13-ci/.git/
/tmp/day13-ci$ gh repo create day13-ci --public --source=. --remote=origin
✓ Created repository jazzwang/day13-ci on github.com
  https://github.com/jazzwang/day13-ci
✓ Added remote https://github.com/jazzwang/day13-ci.git
```

- **新增 API Key to GitHub Secrets:**
   - Go to your repo on GitHub.com.
   - Navigate to **Settings > Secrets and variables > Actions**.
   - Add a **New repository secret**:
   - Name: `OPENCODE_API_KEY`
   - Value: (Your OpenAI or Anthropic key)

### Phase 2: Create the Workflow

- 建立 Github Action 的 Workflow
```bash
/tmp/day13-ci$ mkdir -p .github/workflows
/tmp/day13-ci$ touch .github/workflows/opencode-ci.yml
```
- 使用以下設定
```bash
/tmp/day13-ci$ cat >> .github/workflows/opencode-ci.yml << EOF
name: OpenCode Reviewer
on: [pull_request]

jobs:
  ai_review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run OpenCode Headless
        env:
          OPENCODE_API_KEY: \${{ secrets.OPENCODE_API_KEY }}
        run: |
          curl -fsSL https://opencode.ai/install | bash
          opencode --headless --review "Check this PR for bugs and suggest fixes"
EOF
```

### Phase 3: The "Bait" (Triggering the Bot)

1. **Create a "broken" feature branch:**

```bash
/tmp/day13-ci$ git checkout -b feature/broken-logic
Switched to a new branch 'feature/broken-logic'
```

2. **Create `math_utils.py` with a bug:**

```bash
/tmp/day13-ci$ cat > math_utils.py << EOF
def divide_numbers(a, b):
    # Bug: This will crash on zero, and the agent should catch it.
    return a / b
EOF
```

3. **Commit and push:**

```bash
/tmp/day13-ci$ git add .
/tmp/day13-ci$ git commit -m "Add division feature"
/tmp/day13-ci$ git push origin feature/broken-logic
warning: in the working copy of '.github/workflows/opencode-ci.yml', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'math_utils.py', LF will be replaced by CRLF the next time Git touches it
[feature/broken-logic (root-commit) ff343af] Add division feature
 2 files changed, 17 insertions(+)
 create mode 100644 .github/workflows/opencode-ci.yml
 create mode 100644 math_utils.py
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 16 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (6/6), 709 bytes | 354.00 KiB/s, done.
Total 6 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/jazzwang/day13-ci.git
 * [new branch]      feature/broken-logic -> feature/broken-logic
```

### Phase 4: The PR Review

- 這裡漏了一步，應該先有一個 `main` branch。所以沒辦法到 Github Repo 建立 Pull Request
- 所以刪掉 github 上的 `day13-cli` repo，重新建立一個。