# jira

> Python Jira library.

- Git Repo
  - https://github.com/pycontribs/jira
- Document
  - https://jira.readthedocs.io/

## 2025-03-27

### Jira 與 Attlassian Software 相關的有趣專案

- 緣起：
  - 這幾天想要備份一些 Jira Ticket，原本想要用 [jirafs](../jirafs/jirafs.md) 來備份，不過遇到一些 pip 安裝的問題。
- 行動：
  - 看了一下 Github `jira` topic 的專案
- 結果：
  - https://github.com/toabctl/jiracli - Python 實作的 Jira CLI
  - https://github.com/rhevm-qe-automation/pytest_jira - 讓 Pytest 跟 Jira 整合的 pytest plugin
  - https://github.com/ankitpokhrel/jira-cli - 用 Go 實作的 Jira CLI (這個看起來似乎社群成熟度比較高，還拿到 Attlassian 的贊助)
    - 2021-09-06: [Introducing Jira CLI: The Missing Command-line Tool for Atlassian Jira](https://medium.com/@ankitpokhrel/introducing-jira-cli-the-missing-command-line-tool-for-atlassian-jira-fe44982cc1de)
    - 2022-08-02: [JiraCLI, a Feature-rich Interactive Jira Command Line](https://www.mslinn.com/blog/2022/08/12/jiracli.html)
  - https://github.com/andygrunwald/go-jira - 用 Go 實作的 Jira 函式庫 （看起來有點久沒更新了，但可以看一下上面的 `jira-cli` 是否相依 `go-jira`）

## 2026-01-17

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
are there API or CLI tool that can fetch single Jira ticket including comments as JSON file?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Yes, there are two primary ways to do this: using the **Jira REST API** (via `curl`) or using a dedicated **CLI tool**.

### Method 1: The "Universal" Way (cURL)

This is the most reliable method because it interacts directly with Jira's API and saves the exact raw JSON response. You don't need to install 3rd-party tools, just `curl` (which is standard on Mac/Linux and available on Windows).

**Command:**

```bash
curl -u "email@example.com:YOUR_API_TOKEN" \
     -X GET "https://YOUR_DOMAIN.atlassian.net/rest/api/3/issue/ISSUE-123" \
     -H "Content-Type: application/json" \
     > ticket.json
```

**Key details to make this work:**

1. **API Token:** Do not use your password. Generate a token at [id.atlassian.com](https://id.atlassian.com/manage-profile/security/api-tokens).
2. **Domain:** Replace `YOUR_DOMAIN` with your actual instance name.
3. **Comments:** By default, this endpoint **includes** comments in the JSON under `fields.comment`.
4. **Rendered HTML:** If you want the comments as HTML instead of Jira's internal wiki-markup, add `?expand=renderedFields` to the URL.

---

### Method 2: Dedicated CLI Tools

If you prefer a binary tool over raw `curl` commands, there are two popular open-source CLI tools.

#### Option A: `go-jira` (Best for JSON Export)

This tool is older but excellent for scripting and automation because it has a specific flag for JSON output.

* **Tool:** [go-jira/jira](https://github.com/go-jira/jira)
* **Command:**
```bash
jira view ISSUE-123 --output json > issue.json
```

* **Why choose this:** It is specifically designed to pipe JSON output easily.

#### Option B: `jira-cli` (Modern Interactive Tool)

This is the modern, interactive CLI maintained by Ankit Pokhrel. While it focuses on a TUI (Text User Interface), it can also export data.

* **Tool:** [ankitpokhrel/jira-cli](https://github.com/ankitpokhrel/jira-cli)
* **Command:**
```bash
jira issue view ISSUE-123 --plain --comments > issue.txt
```

* **Note:** This tool often defaults to a human-readable format. For strict JSON file generation, **Method 1 (curl)** or **Option A (go-jira)** is usually better.

### Quick Comparison

| Tool | Best For | JSON Support |
| --- | --- | --- |
| **cURL** | No dependencies, exact API data | **Native** (Returns the raw API JSON) |
| **go-jira** | Scripting & Automation | **Excellent** (`--output json`) |
| **jira-cli** | Interactive/Day-to-day usage | Good (but focuses on readable text) |

**Recommendation:**
If you just need to fetch this once or for a script, use **Method 1 (cURL)**. It guarantees you get the full data structure including comments without installing extra software.

**Would you like me to generate a `jq` command to help you filter just the comments from that JSON file?**
</td></tr></table>