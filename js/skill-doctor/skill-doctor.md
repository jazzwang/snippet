# Skill Doctor

- Git Repo
  - https://github.com/marian2js/skill-doctor

> [!NOTE]
> Help your agents create better skills

## 2026-09-04

- 緣起：
  在 LinkedIn 上看到 skill-doctor 的文章，想確認一下有沒有相關實作
- 搜尋：找到兩個
  - https://github.com/marian2js/skill-doctor - 看起來是 npx 可以直接驗證 skills
  - https://github.com/tcarac/skill-doctor - 這個比較像是 Github Action 的整合
- 實測：直接到 `~/.agents` 驗證
```bash
~/.agents$ npx -y skill-doctor@latest .
  skill doctor
  static diagnostics for agent skills
  metadata • bundle integrity • trigger quality • eval hygiene

  scan summary
  ────────────────────────
 ┌────────────────────────────────────┐
 │  score:    93 / 100 Strong         │
 │  coverage: 9 skills • 6 healthy    │
 │  findings: 0 errors • 15 warnings  │
 │  time:     54ms                    │
 └────────────────────────────────────┘
  ██████████████████████░░

  workspace overview
  ────────────────────────────
  name            score   findings
  ────────────────────────────────
  speak-human-tw   70   10 warn
  grill-me         76   4 warn
  context7         94   1 warn
  docx            100   clean
  find-skills     100   clean
  pdf             100   clean
  pptx            100   clean
  skill-creator   100   clean
  xlsx            100   clean

  finding details
  ─────────────────────────

context7 (94/100)
  ⚠ The description does not clearly say when the skill should be used.
    Add phrases like `use when`, `trigger when`, `if the user asks`, or equivalent trigger language.
    SKILL.md:1

grill-me (76/100)
  ⚠ The description does not clearly say when the skill should be used.
    Add phrases like `use when`, `trigger when`, `if the user asks`, or equivalent trigger language.
    SKILL.md:1

  ⚠ The body does not obviously explain how the skill should be used once triggered.
    Add a quick start, workflow, process, or usage section in the body.
    SKILL.md:6

  ⚠ The body is so short that the skill may not be actionable.
    Add a bit more procedural guidance, not just metadata.
    SKILL.md:6

  ⚠ Unexpected frontmatter key `disable-model-invocation`.
    Keep frontmatter focused on supported keys like `name`, `description`, `compatibility`, `allowed-tools`, `license`, and `metadata`.
    SKILL.md:1

speak-human-tw (70/100)
  ⚠ The description does not clearly say when the skill should be used.
    Add phrases like `use when`, `trigger when`, `if the user asks`, or equivalent trigger language.
    SKILL.md:1

  ⚠ The body does not obviously explain how the skill should be used once triggered.
    Add a quick start, workflow, process, or usage section in the body.
    SKILL.md:22

  ⚠ Unexpected frontmatter key `version`. (8)
    Keep frontmatter focused on supported keys like `name`, `description`, `compatibility`, `allowed-tools`, `license`, and `metadata`.
    SKILL.md:1 (+7 more)
```
```json
~/.agents$ npx -y skill-doctor@latest . --format json
{
  "rootDirectory": "C:\\Users\\jazzw\\.agents",
  "skills": [
    {
      "skill": {
        "name": "context7",
        "rootDirectory": "C:\\Users\\jazzw\\.agents\\skills\\context7",
        "skillFilePath": "C:\\Users\\jazzw\\.agents\\skills\\context7\\SKILL.md",
        "inventory": {
          "resourceDirectories": [],
          "hasEvals": false,
          "evalsPath": null,
          "fileCount": 1
        }
      },
      "diagnostics": [
        {
          "skillName": "context7",
          "skillPath": "C:\\Users\\jazzw\\.agents\\skills\\context7",
          "filePath": "SKILL.md",
          "ruleId": "skill.description-missing-trigger-guidance",
          "severity": "warning",
          "message": "The description does not clearly say when the skill should be used.",
          "help": "Add phrases like `use when`, `trigger when`, `if the user asks`, or equivalent trigger language.",
          "category": "trigger-quality",
          "line": 1
        }
      ],
      "score": {
        "score": 94,
        "label": "Strong"
      }
    },
    {
      "skill": {
        "name": "docx",
        "rootDirectory": "C:\\Users\\jazzw\\.agents\\skills\\docx",
        "skillFilePath": "C:\\Users\\jazzw\\.agents\\skills\\docx\\SKILL.md",
        "inventory": {
          "resourceDirectories": [
            "scripts"
          ],
          "hasEvals": false,
          "evalsPath": null,
          "fileCount": 69
        }
      },
      "diagnostics": [],
      "score": {
        "score": 100,
        "label": "Excellent"
      }
    },
    {
      "skill": {
        "name": "find-skills",
        "rootDirectory": "C:\\Users\\jazzw\\.agents\\skills\\find-skills",
        "skillFilePath": "C:\\Users\\jazzw\\.agents\\skills\\find-skills\\SKILL.md",
        "inventory": {
          "resourceDirectories": [],
          "hasEvals": false,
          "evalsPath": null,
          "fileCount": 1
        }
      },
      "diagnostics": [],
      "score": {
        "score": 100,
        "label": "Excellent"
      }
    },
    {
      "skill": {
        "name": "grill-me",
        "rootDirectory": "C:\\Users\\jazzw\\.agents\\skills\\grill-me",
        "skillFilePath": "C:\\Users\\jazzw\\.agents\\skills\\grill-me\\SKILL.md",
        "inventory": {
          "resourceDirectories": [
            "agents"
          ],
          "hasEvals": false,
          "evalsPath": null,
          "fileCount": 2
        }
      },
      "diagnostics": [
        {
          "skillName": "grill-me",
          "skillPath": "C:\\Users\\jazzw\\.agents\\skills\\grill-me",
          "filePath": "SKILL.md",
          "ruleId": "skill.unexpected-frontmatter-key",
          "severity": "warning",
          "message": "Unexpected frontmatter key `disable-model-invocation`.",
          "help": "Keep frontmatter focused on supported keys like `name`, `description`, `compatibility`, `allowed-tools`, `license`, and `metadata`.",
          "category": "metadata",
          "line": 1
        },
        {
          "skillName": "grill-me",
          "skillPath": "C:\\Users\\jazzw\\.agents\\skills\\grill-me",
          "filePath": "SKILL.md",
          "ruleId": "skill.description-missing-trigger-guidance",
          "severity": "warning",
          "message": "The description does not clearly say when the skill should be used.",
          "help": "Add phrases like `use when`, `trigger when`, `if the user asks`, or equivalent trigger language.",
          "category": "trigger-quality",
          "line": 1
        },
        {
          "skillName": "grill-me",
          "skillPath": "C:\\Users\\jazzw\\.agents\\skills\\grill-me",
          "filePath": "SKILL.md",
          "ruleId": "skill.short-content",
          "severity": "warning",
          "message": "The body is so short that the skill may not be actionable.",
          "help": "Add a bit more procedural guidance, not just metadata.",
          "category": "content",
          "line": 6
        },
        {
          "skillName": "grill-me",
          "skillPath": "C:\\Users\\jazzw\\.agents\\skills\\grill-me",
          "filePath": "SKILL.md",
          "ruleId": "skill.missing-usage-guidance",
          "severity": "warning",
          "message": "The body does not obviously explain how the skill should be used once triggered.",
          "help": "Add a quick start, workflow, process, or usage section in the body.",
          "category": "content",
          "line": 6
        }
      ],
      "score": {
        "score": 76,
        "label": "Healthy"
      }
    },
    {
      "skill": {
        "name": "pdf",
        "rootDirectory": "C:\\Users\\jazzw\\.agents\\skills\\pdf",
        "skillFilePath": "C:\\Users\\jazzw\\.agents\\skills\\pdf\\SKILL.md",
        "inventory": {
          "resourceDirectories": [
            "scripts"
          ],
          "hasEvals": false,
          "evalsPath": null,
          "fileCount": 12
        }
      },
      "diagnostics": [],
      "score": {
        "score": 100,
        "label": "Excellent"
      }
    },
    {
      "skill": {
        "name": "pptx",
        "rootDirectory": "C:\\Users\\jazzw\\.agents\\skills\\pptx",
        "skillFilePath": "C:\\Users\\jazzw\\.agents\\skills\\pptx\\SKILL.md",
        "inventory": {
          "resourceDirectories": [
            "scripts"
          ],
          "hasEvals": false,
          "evalsPath": null,
          "fileCount": 59
        }
      },
      "diagnostics": [],
      "score": {
        "score": 100,
        "label": "Excellent"
      }
    },
    {
      "skill": {
        "name": "skill-creator",
        "rootDirectory": "C:\\Users\\jazzw\\.agents\\skills\\skill-creator",
        "skillFilePath": "C:\\Users\\jazzw\\.agents\\skills\\skill-creator\\SKILL.md",
        "inventory": {
          "resourceDirectories": [
            "agents",
            "assets",
            "references",
            "scripts"
          ],
          "hasEvals": false,
          "evalsPath": null,
          "fileCount": 18
        }
      },
      "diagnostics": [],
      "score": {
        "score": 100,
        "label": "Excellent"
      }
    },
    {
      "skill": {
        "name": "speak-human-tw",
        "rootDirectory": "C:\\Users\\jazzw\\.agents\\skills\\speak-human-tw",
        "skillFilePath": "C:\\Users\\jazzw\\.agents\\skills\\speak-human-tw\\SKILL.md",
        "inventory": {
          "resourceDirectories": [
            "assets",
            "evals",
            "references",
            "scripts"
          ],
          "hasEvals": false,
          "evalsPath": null,
          "fileCount": 29
        }
      },
      "diagnostics": [
        {
          "skillName": "speak-human-tw",
          "skillPath": "C:\\Users\\jazzw\\.agents\\skills\\speak-human-tw",
          "filePath": "SKILL.md",
          "ruleId": "skill.unexpected-frontmatter-key",
          "severity": "warning",
          "message": "Unexpected frontmatter key `version`.",
          "help": "Keep frontmatter focused on supported keys like `name`, `description`, `compatibility`, `allowed-tools`, `license`, and `metadata`.",
          "category": "metadata",
          "line": 1
        },
        {
          "skillName": "speak-human-tw",
          "skillPath": "C:\\Users\\jazzw\\.agents\\skills\\speak-human-tw",
          "filePath": "SKILL.md",
          "ruleId": "skill.unexpected-frontmatter-key",
          "severity": "warning",
          "message": "Unexpected frontmatter key `user-invocable`.",
          "help": "Keep frontmatter focused on supported keys like `name`, `description`, `compatibility`, `allowed-tools`, `license`, and `metadata`.",
          "category": "metadata",
          "line": 1
        },
        {
          "skillName": "speak-human-tw",
          "skillPath": "C:\\Users\\jazzw\\.agents\\skills\\speak-human-tw",
          "filePath": "SKILL.md",
          "ruleId": "skill.unexpected-frontmatter-key",
          "severity": "warning",
          "message": "Unexpected frontmatter key `maturity`.",
          "help": "Keep frontmatter focused on supported keys like `name`, `description`, `compatibility`, `allowed-tools`, `license`, and `metadata`.",
          "category": "metadata",
          "line": 1
        },
        {
          "skillName": "speak-human-tw",
          "skillPath": "C:\\Users\\jazzw\\.agents\\skills\\speak-human-tw",
          "filePath": "SKILL.md",
          "ruleId": "skill.unexpected-frontmatter-key",
          "severity": "warning",
          "message": "Unexpected frontmatter key `review_cadence`.",
          "help": "Keep frontmatter focused on supported keys like `name`, `description`, `compatibility`, `allowed-tools`, `license`, and `metadata`.",
          "category": "metadata",
          "line": 1
        },
        {
          "skillName": "speak-human-tw",
          "skillPath": "C:\\Users\\jazzw\\.agents\\skills\\speak-human-tw",
          "filePath": "SKILL.md",
          "ruleId": "skill.unexpected-frontmatter-key",
          "severity": "warning",
          "message": "Unexpected frontmatter key `last-updated`.",
          "help": "Keep frontmatter focused on supported keys like `name`, `description`, `compatibility`, `allowed-tools`, `license`, and `metadata`.",
          "category": "metadata",
          "line": 1
        },
        {
          "skillName": "speak-human-tw",
          "skillPath": "C:\\Users\\jazzw\\.agents\\skills\\speak-human-tw",
          "filePath": "SKILL.md",
          "ruleId": "skill.unexpected-frontmatter-key",
          "severity": "warning",
          "message": "Unexpected frontmatter key `author`.",
          "help": "Keep frontmatter focused on supported keys like `name`, `description`, `compatibility`, `allowed-tools`, `license`, and `metadata`.",
          "category": "metadata",
          "line": 1
        },
        {
          "skillName": "speak-human-tw",
          "skillPath": "C:\\Users\\jazzw\\.agents\\skills\\speak-human-tw",
          "filePath": "SKILL.md",
          "ruleId": "skill.unexpected-frontmatter-key",
          "severity": "warning",
          "message": "Unexpected frontmatter key `tags`.",
          "help": "Keep frontmatter focused on supported keys like `name`, `description`, `compatibility`, `allowed-tools`, `license`, and `metadata`.",
          "category": "metadata",
          "line": 1
        },
        {
          "skillName": "speak-human-tw",
          "skillPath": "C:\\Users\\jazzw\\.agents\\skills\\speak-human-tw",
          "filePath": "SKILL.md",
          "ruleId": "skill.unexpected-frontmatter-key",
          "severity": "warning",
          "message": "Unexpected frontmatter key `changelog`.",
          "help": "Keep frontmatter focused on supported keys like `name`, `description`, `compatibility`, `allowed-tools`, `license`, and `metadata`.",
          "category": "metadata",
          "line": 1
        },
        {
          "skillName": "speak-human-tw",
          "skillPath": "C:\\Users\\jazzw\\.agents\\skills\\speak-human-tw",
          "filePath": "SKILL.md",
          "ruleId": "skill.description-missing-trigger-guidance",
          "severity": "warning",
          "message": "The description does not clearly say when the skill should be used.",
          "help": "Add phrases like `use when`, `trigger when`, `if the user asks`, or equivalent trigger language.",
          "category": "trigger-quality",
          "line": 1
        },
        {
          "skillName": "speak-human-tw",
          "skillPath": "C:\\Users\\jazzw\\.agents\\skills\\speak-human-tw",
          "filePath": "SKILL.md",
          "ruleId": "skill.missing-usage-guidance",
          "severity": "warning",
          "message": "The body does not obviously explain how the skill should be used once triggered.",
          "help": "Add a quick start, workflow, process, or usage section in the body.",
          "category": "content",
          "line": 22
        }
      ],
      "score": {
        "score": 70,
        "label": "Needs polish"
      }
    },
    {
      "skill": {
        "name": "xlsx",
        "rootDirectory": "C:\\Users\\jazzw\\.agents\\skills\\xlsx",
        "skillFilePath": "C:\\Users\\jazzw\\.agents\\skills\\xlsx\\SKILL.md",
        "inventory": {
          "resourceDirectories": [
            "scripts"
          ],
          "hasEvals": false,
          "evalsPath": null,
          "fileCount": 54
        }
      },
      "diagnostics": [],
      "score": {
        "score": 100,
        "label": "Excellent"
      }
    }
  ],
  "diagnostics": [
    {
      "skillName": "context7",
      "skillPath": "C:\\Users\\jazzw\\.agents\\skills\\context7",
      "filePath": "SKILL.md",
      "ruleId": "skill.description-missing-trigger-guidance",
      "severity": "warning",
      "message": "The description does not clearly say when the skill should be used.",
      "help": "Add phrases like `use when`, `trigger when`, `if the user asks`, or equivalent trigger language.",
      "category": "trigger-quality",
      "line": 1
    },
    {
      "skillName": "grill-me",
      "skillPath": "C:\\Users\\jazzw\\.agents\\skills\\grill-me",
      "filePath": "SKILL.md",
      "ruleId": "skill.unexpected-frontmatter-key",
      "severity": "warning",
      "message": "Unexpected frontmatter key `disable-model-invocation`.",
      "help": "Keep frontmatter focused on supported keys like `name`, `description`, `compatibility`, `allowed-tools`, `license`, and `metadata`.",
      "category": "metadata",
      "line": 1
    },
    {
      "skillName": "grill-me",
      "skillPath": "C:\\Users\\jazzw\\.agents\\skills\\grill-me",
      "filePath": "SKILL.md",
      "ruleId": "skill.description-missing-trigger-guidance",
      "severity": "warning",
      "message": "The description does not clearly say when the skill should be used.",
      "help": "Add phrases like `use when`, `trigger when`, `if the user asks`, or equivalent trigger language.",
      "category": "trigger-quality",
      "line": 1
    },
    {
      "skillName": "grill-me",
      "skillPath": "C:\\Users\\jazzw\\.agents\\skills\\grill-me",
      "filePath": "SKILL.md",
      "ruleId": "skill.short-content",
      "severity": "warning",
      "message": "The body is so short that the skill may not be actionable.",
      "help": "Add a bit more procedural guidance, not just metadata.",
      "category": "content",
      "line": 6
    },
    {
      "skillName": "grill-me",
      "skillPath": "C:\\Users\\jazzw\\.agents\\skills\\grill-me",
      "filePath": "SKILL.md",
      "ruleId": "skill.missing-usage-guidance",
      "severity": "warning",
      "message": "The body does not obviously explain how the skill should be used once triggered.",
      "help": "Add a quick start, workflow, process, or usage section in the body.",
      "category": "content",
      "line": 6
    },
    {
      "skillName": "speak-human-tw",
      "skillPath": "C:\\Users\\jazzw\\.agents\\skills\\speak-human-tw",
      "filePath": "SKILL.md",
      "ruleId": "skill.unexpected-frontmatter-key",
      "severity": "warning",
      "message": "Unexpected frontmatter key `version`.",
      "help": "Keep frontmatter focused on supported keys like `name`, `description`, `compatibility`, `allowed-tools`, `license`, and `metadata`.",
      "category": "metadata",
      "line": 1
    },
    {
      "skillName": "speak-human-tw",
      "skillPath": "C:\\Users\\jazzw\\.agents\\skills\\speak-human-tw",
      "filePath": "SKILL.md",
      "ruleId": "skill.unexpected-frontmatter-key",
      "severity": "warning",
      "message": "Unexpected frontmatter key `user-invocable`.",
      "help": "Keep frontmatter focused on supported keys like `name`, `description`, `compatibility`, `allowed-tools`, `license`, and `metadata`.",
      "category": "metadata",
      "line": 1
    },
    {
      "skillName": "speak-human-tw",
      "skillPath": "C:\\Users\\jazzw\\.agents\\skills\\speak-human-tw",
      "filePath": "SKILL.md",
      "ruleId": "skill.unexpected-frontmatter-key",
      "severity": "warning",
      "message": "Unexpected frontmatter key `maturity`.",
      "help": "Keep frontmatter focused on supported keys like `name`, `description`, `compatibility`, `allowed-tools`, `license`, and `metadata`.",
      "category": "metadata",
      "line": 1
    },
    {
      "skillName": "speak-human-tw",
      "skillPath": "C:\\Users\\jazzw\\.agents\\skills\\speak-human-tw",
      "filePath": "SKILL.md",
      "ruleId": "skill.unexpected-frontmatter-key",
      "severity": "warning",
      "message": "Unexpected frontmatter key `review_cadence`.",
      "help": "Keep frontmatter focused on supported keys like `name`, `description`, `compatibility`, `allowed-tools`, `license`, and `metadata`.",
      "category": "metadata",
      "line": 1
    },
    {
      "skillName": "speak-human-tw",
      "skillPath": "C:\\Users\\jazzw\\.agents\\skills\\speak-human-tw",
      "filePath": "SKILL.md",
      "ruleId": "skill.unexpected-frontmatter-key",
      "severity": "warning",
      "message": "Unexpected frontmatter key `last-updated`.",
      "help": "Keep frontmatter focused on supported keys like `name`, `description`, `compatibility`, `allowed-tools`, `license`, and `metadata`.",
      "category": "metadata",
      "line": 1
    },
    {
      "skillName": "speak-human-tw",
      "skillPath": "C:\\Users\\jazzw\\.agents\\skills\\speak-human-tw",
      "filePath": "SKILL.md",
      "ruleId": "skill.unexpected-frontmatter-key",
      "severity": "warning",
      "message": "Unexpected frontmatter key `author`.",
      "help": "Keep frontmatter focused on supported keys like `name`, `description`, `compatibility`, `allowed-tools`, `license`, and `metadata`.",
      "category": "metadata",
      "line": 1
    },
    {
      "skillName": "speak-human-tw",
      "skillPath": "C:\\Users\\jazzw\\.agents\\skills\\speak-human-tw",
      "filePath": "SKILL.md",
      "ruleId": "skill.unexpected-frontmatter-key",
      "severity": "warning",
      "message": "Unexpected frontmatter key `tags`.",
      "help": "Keep frontmatter focused on supported keys like `name`, `description`, `compatibility`, `allowed-tools`, `license`, and `metadata`.",
      "category": "metadata",
      "line": 1
    },
    {
      "skillName": "speak-human-tw",
      "skillPath": "C:\\Users\\jazzw\\.agents\\skills\\speak-human-tw",
      "filePath": "SKILL.md",
      "ruleId": "skill.unexpected-frontmatter-key",
      "severity": "warning",
      "message": "Unexpected frontmatter key `changelog`.",
      "help": "Keep frontmatter focused on supported keys like `name`, `description`, `compatibility`, `allowed-tools`, `license`, and `metadata`.",
      "category": "metadata",
      "line": 1
    },
    {
      "skillName": "speak-human-tw",
      "skillPath": "C:\\Users\\jazzw\\.agents\\skills\\speak-human-tw",
      "filePath": "SKILL.md",
      "ruleId": "skill.description-missing-trigger-guidance",
      "severity": "warning",
      "message": "The description does not clearly say when the skill should be used.",
      "help": "Add phrases like `use when`, `trigger when`, `if the user asks`, or equivalent trigger language.",
      "category": "trigger-quality",
      "line": 1
    },
    {
      "skillName": "speak-human-tw",
      "skillPath": "C:\\Users\\jazzw\\.agents\\skills\\speak-human-tw",
      "filePath": "SKILL.md",
      "ruleId": "skill.missing-usage-guidance",
      "severity": "warning",
      "message": "The body does not obviously explain how the skill should be used once triggered.",
      "help": "Add a quick start, workflow, process, or usage section in the body.",
      "category": "content",
      "line": 22
    }
  ],
  "score": {
    "score": 93,
    "label": "Strong"
  },
  "elapsedMilliseconds": 55.5257,
  "skippedPaths": []
}
```
- 感想：
  - skill-doctor 有點類似 `eslint` 之類的工具，修正還是要靠自己。
  - [待測試] 如果餵這些警告給 `skill-creator` 能夠增加分數嗎？