# jira-select

- PyPI
  - https://pypi.org/project/jira-select/
- Git Repo
  - https://github.com/coddingtonbear/jira-select
- Document
  - https://jira-select.readthedocs.io

## 2025-12-04

- 先前測試 `jirafs` 在 Windows 11 失敗（因為太久沒維護），卻發現作者改寫了 `jira-select`
- 最近因為每週都被要求要報告一些團隊的 KPI Metrics，想看看有沒有辦法簡化流程。
- 先來實測安裝與設定：
  - 安裝：
    - 用 `uv tool install` 試試看
    ```bash
    ~$ uv tool install jira-select
    Resolved 42 packages in 11.17s
        Built queryablelist==3.1.0
    Prepared 42 packages in 6.86s
    Installed 42 packages in 263ms
    + annotated-types==0.7.0
    + appdirs==1.4.4
    + certifi==2025.11.12
    + charset-normalizer==3.4.4
    + defusedxml==0.7.1
    + diskcache==4.1.0
    + dotmap==1.3.30
    + idna==3.11
    + importlib-metadata==8.7.0
    + jira==3.10.5
    + jira-select==3.4.2
    + keyring==22.4.0
    + markdown-it-py==4.0.0
    + mdurl==0.1.2
    + oauthlib==3.3.1
    + packaging==25.0
    + portion==2.6.1
    + prompt-toolkit==3.0.52
    + pydantic==2.12.5
    + pydantic-core==2.41.5
    + pygments==2.19.2
    + python-dateutil==2.9.0.post0
    + pytz==2025.2
    + pywin32-ctypes==0.2.3
    + pyyaml==6.0.3
    + queryablelist==3.1.0
    + requests==2.32.5
    + requests-oauthlib==2.0.0
    + requests-toolbelt==1.0.0
    + rich==13.9.4
    + safdie==2.0.4
    + simpleeval==0.9.13
    + six==1.17.0
    + sortedcontainers==2.4.0
    + standard-mailcap==3.13.0
    + typing-extensions==4.15.0
    + typing-inspection==0.4.2
    + urllib3==2.5.0
    + visidata==3.3
    + wcwidth==0.2.14
    + windows-curses==2.4.1
    + zipp==3.23.0
    Installed 1 executable: jira-select.exe
    ~$ which jira-select
    /c/Users/jazzw/.local/bin/jira-select
    ```
    - 設定：照文件說明，先用 `jira-select configure`
    ```bash
    ~$ jira-select.exe configure
    ```
    - 輸入 Jira Server 網址，使用者名稱，密碼，然後同意存到系統 keychain
    - 實測查詢：照文件，使用 `jira-select shell`
    ```bash
    ~$ jira-select shell
    Jira-select Shell v3.4.2
    | Run:         ESC->ENTER
    | Clear:       CTRL+C
    | Exit:        CTRL+D
    >>> select:
        Issue Key: key
        Issue Summary: summary
        from: issues
        where:
        - assignee = "jazz@example.com"
        - resolution is null
    jira   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 19/19 0:00:00
    select ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 19/19 0:00:00
    ```
- 問題一：可以把查詢結果存起來嗎？
  - 看到文件 https://jira-select.readthedocs.io/en/latest/parameters.html
    使用了這樣的指令：
    ```bash
    ~$ jira-select run-query --param="project=MYPROJECT" my-query.yaml
    ```
    看樣子可以用 `jira-select run-query` 來把常用的查詢定下來，然後用參數的方式去改每週有異動的部份
- 備註：那有哪些「子命令」可以用呢？目前用到 `configure`, `shell` 跟 `run-query`
  - 看起來 `build-query` 可以拿來互動式寫 YAML 查詢範例
```bash
~$ jira-select -h
usage: jira-select [-h] [--config CONFIG] [--instance-name INSTANCE_NAME]
                   [--instance-url INSTANCE_URL] [--username USERNAME]
                   [--password PASSWORD] [--certificate CERTIFICATE]
                   [--disable-certificate-verification] [--debugger]
                   [--log-level LOG_LEVEL]
                   {batch,build-query,configure,functions,install-user-script,remove-instance,run-query,run-script,schema,setup-instance,shell,show-instances,store-password} ...

positional arguments:
  {batch,build-query,configure,functions,install-user-script,remove-instance,run-query,run-script,schema,setup-instance,shell,show-instances,store-password}
    batch               Runs a specified Jira-select query multiple times with params and
                        values specified by a CSV file.
    build-query         Interactively generates a query definition (in yaml format).
    configure           Interactively allows you to configure jira-select to connect to
                        your Jira instance.
    functions           Lists all available functions, their signatures, and description.
    install-user-script
                        Installs a user script (i.e. a python script having functions
                        decorated with `jira_select.plugin.register_function`) into your
                        user configuration directory at
                        C:\Users\jazzw\AppData\Local\coddingtonbear\jira-
                        select\functions.
    remove-instance     Removes configuration for a particular Jira instance. Specify the
                        instance to remove via `--instance-name`.
    run-query           Runs a query definition specified in yaml format.
    run-script          Runs the 'main(**kwargs)' function in the specified file; see
                        documentation for details.
    schema              Describes the fields available in data returned from a particular
                        data source.
    setup-instance      Set up a Jira instance using command-line arguments. Note: if you
                        are a human, you probably want to use `configure` instead. If
                        `--password` is not specified as an argument, password will be
                        read from stdin.
    shell               Opens an interactive shell (a.k.a. repl) allowing you to interact
                        with Jira and see results immediately (like the sqlite3,
                        postgres, or mysql shells).
    show-instances      Displays Jira instances that you have configured jira-select to
                        be able to use.
    store-password      Stores the password for a given user account in your system
                        keychain.

options:
  -h, --help            show this help message and exit
  --config, -c CONFIG   Path to configuration file to load; by default configuration will
                        be loaded from C:\Users\jazzw\AppData\Local\coddingtonbear\jira-
                        select\config.yaml.
  --instance-name, -n INSTANCE_NAME
                        Named instance to connect to. You can define new instances by
                        running `jira-select configure --instance-name="my-instance"` to
                        set the instance URL, username, and password for later use in
                        other commands via providing the `--instance-name="my-instance"
                        command-line argument. By default the 'default' instance name
                        will be used.
  --instance-url, -i INSTANCE_URL
                        URL of the Jira instance to connect to (if you cannot use
                        'configure')
  --username, -u USERNAME
                        Username to use for connecting to Jira (if you cannot use
                        'configure')
  --password, -p PASSWORD
                        Password to use for connecting to Jira. NOT RECOMMENDED: use the
                        'store-password' or 'configure' command instead.
  --certificate CERTIFICATE
                        Path to a certificate to self-signed certificate use for
                        connecting to your instance.
  --disable-certificate-verification
                        Do not verify server certificate. Generally not recommended.
  --debugger            Wait for debugger connection before processing command (requires
                        debugpy).
  --log-level LOG_LEVEL
                        Print logging messages of the specified level and above to the
                        console.
~$
```
- 備註：`jira-select schema` 學到分成不同的範圍 `boards`, `issues`, `sprints`
```bash
~$ jira-select schema -h
usage: jira-select schema [-h] [--json] [--having HAVING]
                          {boards,issues,sprints} [search_terms ...]

positional arguments:
  {boards,issues,sprints}
  search_terms          Case-insensitive search term for limiting displayed results.

options:
  -h, --help            show this help message and exit
  --json, -j            Export schema as JSON format instead of printing a table.
  --having HAVING       A 'having' expression to use for limiting the displayed results.
                        Searchable fields are 'key', 'type', and 'description' and 'raw'.
                        E.g.--having="'estimate' in description.lower()".
```
- 根據目前的使用心得，這三個階層關係為：
```
boards/
└── sprints
    └── issues
```
- 實測 `jira-select build-query` 發現可以查到所有 `customfield` 的名字。輸出結果看起來可以 pipe 給 YAML 檔作為後續查詢的範本。
```bash
┌───────────────────────────────────────────────────────────────────────| Select |────────────────────────────────────────────────────────────────────────┐
│                                                                                                                                                         │
│ Which fields would you like to select in your query?                                                                                                    │
│                                                                                                                                                         │
│ [ ] ASSIGNEE (customfield_13602)                                                                                                                      ^ │
│ [ ] Acceptance Criteria (customfield_10313)                                                                                                             │
| ....................................................                                                                                                    |
│ [ ] Assumptions (customfield_13914)                                                                                                                   v │
│                                                                                                                                                         │
│                                                                <    Ok    > <  Cancel  >                                                                │
│                                                                                                                                                         │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
```bash
~$ jira-select build-query
from: issues
select:
- customfield_16000 as "gitBranch"
```
- 待查文件：關於 `jira-select run-script` 目前有點不太能理解用途。感覺跟 `jira-select run-query` 不同。
```bash
~$ jira-select run-script -h
usage: jira-select run-script [-h] file_path ...

positional arguments:
  file_path     Path to the file containg the `main(**kwargs)` functionto execute.
  command_args

options:
  -h, --help    show this help message and exit
```
- 備忘：`jira-select run-query` 看起來可以指定輸出格式(CSV, JSON, TSV, HTML)
```bash
~$ jira-select run-query -h
usage: jira-select run-query [-h] [--format {csv,html,json,raw,table,tsv}]
                             [--output OUTPUT] [--launch-default-viewer] [--view]
                             [--param PARAMETERS] [--no-cache] [--disable-progressbars]
                             [query_file]

positional arguments:
  query_file            Query definition file to run

options:
  -h, --help            show this help message and exit
  --format, -f {csv,html,json,raw,table,tsv}
                        Data format in which to write record data; default: 'csv'.
  --output, -o OUTPUT   Path to file where records will be written; default: stdout.
  --launch-default-viewer, -l
                        Display the output using the default viewer for the filetype used
                        by the selected formatter instead of displaying the results
                        inline.
  --view, -v            Launch viewer immediately after completing query.
  --param, -p PARAMETERS
  --no-cache, -c        Do not use cached data.
  --disable-progressbars, -b
```
- 整體來說，`jira-select` 用起來比用 golang 寫的 `jira-cli` (https://github.com/ankitpokhrel/jira-cli) 更有彈性。可以繼續花時間研究怎麼用。

## 2026-01-21

- 範例：使用 `jira-select run-query` 輸出 JSON 結果存到檔案
- here is the query_file:
```bash
~$ cat BA_Tickets.jql
from: issues
select:
- key
- summary
- description
- comment
where:
- labels in (BATickets, BAReview) AND project = HADOOP
```
- here is the example command:
```bash
~$ jira-select run-query -f json -o BA_Tickets.json BA_Tickets.jql
```

## 2026-01-28

- 範例：利用 `jira-select run-query` 輸出 CSV 結果，將所有 Jira Board 查詢結果存到檔案
- query_file:
```bash
~/Downloads/CY26_PI1_QBR_7_KPI$ cat list-boards.jql
from: boards
select:
- id
- name
- type
```
- 查詢方法
```
~$ jira-select run-query -f csv -o jira-boards.csv list-boards.jql
```

### schema (boards)

- 一般 boards 跟 sprints 的 schema 不會變，而 issues 的 schema 可以取得完整 custom_fields 列表
```bash
~$ jira-select schema boards
           boards
┏━━━━━━┳━━━━━━┳━━━━━━━━━━━━━┓
┃ id   ┃ type ┃ description ┃
┡━━━━━━╇━━━━━━╇━━━━━━━━━━━━━┩
│ id   │ int  │             │
│ name │ str  │             │
│ type │ str  │             │
└──────┴──────┴─────────────┘
```

### schema (sprints)

```bash
~$ jira-select schema sprints
                 sprints
┏━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━┓
┃ id            ┃ type    ┃ description ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━┩
│ id            │ int     │             │
│ state         │ str     │             │
│ name          │ str     │             │
│ startDate     │ datestr │             │
│ endDate       │ datestr │             │
│ completeDate  │ datestr │             │
│ originBoardId │ int     │             │
└───────────────┴─────────┴─────────────┘
```

### 取得指定 board 底下的 sprints

- 嘗試限制查詢條件，但還是沒成功
```bash
>>> from: sprints
    select:
    - id
    - state
    - name
    where:
    - board_name is "HADOOP"


Query Error: Sprint query 'where' expressions should be a dictionary having any of the following keys: 'board_type', 'board_name', or 'state'.
>>> from: sprints
    select:
    - id
    - state
    - name
    where:
    - state: 'active'

Parse Error: Your query could not be parsed: 2 validation errors for QueryDefinition
where.list.0
  Input should be a valid string
    For further information visit https://errors.pydantic.dev/2.12/v/string_type
where.dict
  Input should be a valid dictionary [type=dict_type, input_value=[{'state': 'active'}], input_type=list]
    For further information visit https://errors.pydantic.dev/2.12/v/dict_type
>>> from: sprints
    select:
    - id
    - state
    - name
    where:
    - state = 'active'


Query Error: Sprint query 'where' expressions should be a dictionary having any of the following keys: 'board_type', 'board_name', or 'state'.
```
