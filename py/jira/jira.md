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