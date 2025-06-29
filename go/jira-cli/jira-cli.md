# jira-cli

> 🔥 Feature-rich interactive Jira command line.

- Git repo
  - https://github.com/ankitpokhrel/jira-cli
- Blog Post
  - 2021-09-06: [Introducing Jira CLI: The Missing Command-line Tool for Atlassian Jira](https://medium.com/@ankitpokhrel/introducing-jira-cli-the-missing-command-line-tool-for-atlassian-jira-fe44982cc1de)

## 2025-03-27

- 緣起：
  - 這幾天想要備份一些 Jira Ticket，原本想要用 [jirafs](../jirafs/jirafs.md) 來備份，不過遇到一些 pip 安裝的問題。
- 行動：
  - 看了一下 Github `jira` topic 的專案
- 結果：
  - https://github.com/toabctl/jiracli - Python 實作的 Jira CLI
  - https://github.com/rhevm-qe-automation/pytest_jira - 讓 Pytest 跟 Jira 整合的 pytest plugin
  - https://github.com/ankitpokhrel/jira-cli - 用 Go 實作的 Jira CLI (這個看起來似乎社群成熟度比較高，還拿到 Attlassian 的贊助)
    - 2021-09-06: [Introducing Jira CLI: The Missing Command-line Tool for Atlassian Jira](https://medium.com/@ankitpokhrel/introducing-jira-cli-the-missing-command-line-tool-for-atlassian-jira-fe44982cc1de)
  - https://github.com/andygrunwald/go-jira - 用 Go 實作的 Jira 函式庫 （看起來有點久沒更新了，但可以看一下上面的 `jira-cli` 是否相依 `go-jira`）

## 2025-06-29

- 實測安裝：
  - Linux:
    ```bash
    @jazzwang ➜ /workspaces/snippet/go/jira-cli (master) $ cd /tmp
    @jazzwang ➜ /tmp $ wget https://github.com/ankitpokhrel/jira-cli/releases/download/v1.6.0/jira_1.6.0_linux_x86_64.tar.gz
    @jazzwang ➜ /tmp $ tar zxvf jira_1.6.0_linux_x86_64.tar.gz 
    jira_1.6.0_linux_x86_64/LICENSE
    jira_1.6.0_linux_x86_64/bin/jira
    @jazzwang ➜ /tmp $ cd jira_1.6.0_linux_x86_64/
    @jazzwang ➜ /tmp/jira_1.6.0_linux_x86_64 $ bin/jira
    Interactive Jira command line.

    USAGE
    jira <command> <subcommand> [flags]

    MAIN COMMANDS
    board       Board manages Jira boards in a project
    epic        Epic manage epics in a project
    issue       Issue manage issues in a project
    open        Open issue in a browser
    project     Project manages Jira projects
    sprint      Sprint manage sprints in a project board

    OTHER COMMANDS
    completion  Output shell completion code for the specified shell (bash or zsh)
    help        Help about any command
    init        Init initializes jira config
    man         Help generate man(7) pages for Jira CLI
    me          Displays configured jira user
    serverinfo  Displays information about the Jira instance
    version     Print the app version information

    FLAGS
    -c, --config string    Config file (default is /home/codespace/.config/.jira/.config.yml)
        --debug            Turn on debug output
    -h, --help             help for jira
    -p, --project string   Jira project to look into (defaults to /home/codespace/.config/.jira/.config.yml)

    LEARN MORE
    Use 'jira <command> <subcommand> --help' for more information about a command.
    Read the doc or get help at https://github.com/ankitpokhrel/jira-cli
    ```