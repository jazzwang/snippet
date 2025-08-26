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
  - https://github.com/ankitpokhrel/jira-cli - 用 Go 實作的 Jira CLI (這個看起來似乎社群成熟度比較高，還拿到 Atlassian 的贊助)
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

## 2025-08-26

- Windows 11 實測：
  - 安裝：
    - 從 Github 下載
      - 
    - 解壓縮，把 `jira.exe` 複製到 `~/bin`
  - 設定：
    - 一開始下 `jira init` 時，會出現 `401`
    - 改用 `jira init --debug` 雖然出現比較多除錯用的訊息，但仍舊無法正常認證。
    - 仔細看[文件 "On-premise Installation" 段落](https://github.com/ankitpokhrel/jira-cli?tab=readme-ov-file#on-premise-installation)以後，發現要設定兩個環境變數：
      - `JIRA_API_TOKEN`
      - `JIRA_AUTH_TYPE`
    - 設定好以後，就可以正常跑完 `jira init` 了！
      ```bash
      ~/git/snippet$ env | grep -i JIRA
      JIRA_API_TOKEN="xxxxxxxxxxxxxxxxxxxxxxxxxxx"
      JIRA_AUTH_TYPE="bearer"
      ```
  - 操作：
    ```bash
    916  [08/26 17:02:54] jira board list
    919  [08/26 17:03:23] jira epic list
    922  [08/26 17:04:41] jira project list
    925  [08/26 17:05:18] jira sprint list
    927  [08/26 17:05:50] jira serverinfo
    928  [08/26 17:06:00] jira me
    930  [08/26 17:06:13] jira man -h
    931  [08/26 17:06:15] jira man -g
    936  [08/26 17:07:07] jira board list
    939  [08/26 17:07:36] jira board -p MDSMIG list
    940  [08/26 17:07:53] jira sprint -h
    943  [08/26 17:08:20] jira sprints -p MDSMIG list
    953  [08/26 17:09:59] cat ~/.config/.jira/.config.yml
    957  [08/26 17:13:59] jira issue -h
    958  [08/26 17:15:48] jira issue view AAP-274
    959  [08/26 17:11:24] jira issue list
    960  [08/26 17:16:05] jira issue list -h
    962  [08/26 17:18:34] jira issue list -q 'sprint=50458 ORDER BY key ASC'
    986  [08/26 21:03:22] jira sprint list --next
    988  [08/26 21:05:01] jira sprint list --next --plan
    989  [08/26 21:05:41] jira sprint list --next --order-by KEY --plain
    ```