# Github CLI

- 2024-06-28 23:46:25
- https://github.com/cli/cli
- https://cli.github.com/

## 2024-06-28 

- Installation
```bash
jazzwang:~$ brew install gh
```
- Authentication
```bash
jazzwang:~$ gh auth login
```
- need to enable Codespace Authentication
```bash
jazzwang:~$ gh auth refresh -h github.com -s codespace
```
- fetch codespace list
```bash
jazzwang:~$ gh codespace 
Connect to and manage codespaces

USAGE
  gh codespace [flags]

ALIASES
  gh cs

AVAILABLE COMMANDS
  code:        Open a codespace in Visual Studio Code
  cp:          Copy files between local and remote file systems
  create:      Create a codespace
  delete:      Delete codespaces
  edit:        Edit a codespace
  jupyter:     Open a codespace in JupyterLab
  list:        List codespaces
  logs:        Access codespace logs
  ports:       List ports in a codespace
  rebuild:     Rebuild a codespace
  ssh:         SSH into a codespace
  stop:        Stop a running codespace
  view:        View details about a codespace

INHERITED FLAGS
  --help   Show help for command

LEARN MORE
  Use `gh <command> <subcommand> --help` for more information about a command.
  Read the manual at https://cli.github.com/manual

jazzwang:~$ gh codespace list
NAME                       DISPLAY NAME  REPOSITORY        BRANCH  STATE     CREATED AT        
shiny-zebra-jjrxjgp652gqw  snippet       jazzwang/snippet  master  Shutdown  about 2 months ago
```
- ssh codespace
```bash
jazzwang:~$ gh cs ssh 
? Choose codespace: jazzwang/snippet (master): snippet
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 6.5.0-1022-azure x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro
Last login: Fri Jun 28 13:32:06 2024 from ::1
manpath: can't set the locale; make sure $LC_* and $LANG are correct
@jazzwang ➜ /workspaces/snippet (master) $ 
```
- generate ssh config
```bash
jazzwang:~$ gh cs ssh --config
Host cs.shiny-zebra-jjrxjgp652gqw.master
	User codespace
	ProxyCommand /usr/local/bin/gh cs ssh -c shiny-zebra-jjrxjgp652gqw --stdio -- -i /Users/jazzwang/.ssh/codespaces.auto
	UserKnownHostsFile=/dev/null
	StrictHostKeyChecking no
	LogLevel quiet
	ControlMaster auto
	IdentityFile /Users/jazzwang/.ssh/codespaces.auto
```
```bash
jazzwang:~$ gh cs ssh --help
The `ssh` command is used to SSH into a codespace. In its simplest form, you can
run `gh cs ssh`, select a codespace interactively, and connect.

The `ssh` command will automatically create a public/private ssh key pair in the
`~/.ssh` directory if you do not have an existing valid key pair. When selecting the
key pair to use, the preferred order is:
  
1. Key specified by `-i` in `<ssh-flags>`
2. Automatic key, if it already exists
3. First valid key pair in ssh config (according to `ssh -G`)
4. Automatic key, newly created

The `ssh` command also supports deeper integration with OpenSSH using a `--config`
option that generates per-codespace ssh configuration in OpenSSH format.
Including this configuration in your `~/.ssh/config` improves the user experience
of tools that integrate with OpenSSH, such as Bash/Zsh completion of ssh hostnames,
remote path completion for `scp/rsync/sshfs`, `git` ssh remotes, and so on.

Once that is set up (see the second example below), you can ssh to codespaces as
if they were ordinary remote hosts (using `ssh`, not `gh cs ssh`).

Note that the codespace you are connecting to must have an SSH server pre-installed.
If the docker image being used for the codespace does not have an SSH server,
install it in your `Dockerfile` or, for codespaces that use Debian-based images,
you can add the following to your `devcontainer.json`:

	"features": {
		"ghcr.io/devcontainers/features/sshd:1": {
			"version": "latest"
		}
	}


USAGE
  gh codespace ssh [<flags>...] [-- <ssh-flags>...] [<command>]

FLAGS
  -c, --codespace string    Name of the codespace
      --config              Write OpenSSH configuration to stdout
  -d, --debug               Log debug data to a file
      --debug-file string   Path of the file log to
      --profile string      Name of the SSH profile to use
  -R, --repo string         Filter codespace selection by repository name (user/repo)
      --repo-owner string   Filter codespace selection by repository owner (username or org)
      --server-port int     SSH server port number (0 => pick unused)

INHERITED FLAGS
  --help   Show help for command

EXAMPLES
  $ gh codespace ssh
  
  $ gh codespace ssh --config > ~/.ssh/codespaces
  $ printf 'Match all\nInclude ~/.ssh/codespaces\n' >> ~/.ssh/config

LEARN MORE
  Use `gh <command> <subcommand> --help` for more information about a command.
  Read the manual at https://cli.github.com/manual
```

## 2024-11-18

- ( 2024-11-18 16:13:18 )
- 參考: https://docs.github.com/en/rest/activity/starring?apiVersion=2022-11-28#list-repositories-starred-by-a-user
- 從參考文件可以知道取得某個使用者所有 Starred 專案列表的 Github CLI 指令為
```bash
# GitHub CLI api
# https://cli.github.com/manual/gh_api

gh api \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  /users/USERNAME/starred
```
- 實測， URI 開頭不能加 `/`
- 參考：https://cli.github.com/manual/gh_api
- ( 2024-11-18 16:57:40 )
- 抓取 `jazzwang` 所有給星星的專案，輸出到 STDOUT 並寫到 `jazzwang_starred.json` 檔案。
```bash
jazzw@JazzBook:~$ gh api --paginate users/jazzwang/starred | tee jazzwang_starred.json
```
- 由於給的星星數太多，所以一定要加 `--paginate` 才有辦法列出全部的專案。
- 驗證輸出的 JSON 檔案是否為合格的 JSON 格式。用 `jq .` 確認格式正確。因為只有一行，所以是 NDJSON 格式，可以用 PySpark 或 Spark Shell 做後續分析。

## 2024-11-21

- ( 2024-11-21 11:46:44 )
- 問題：如何備份 Github Repo 的 Issues?
- 緣起：
  - 有人用 Github Repo 的 Issue 當作留言板（討論區）
  - 過去曾經用 Github Repo 的 Issue 當作議程投票機制
- 作法：
  - 參考：https://rewind.com/blog/three-ways-to-backup-your-github-issues/
    - 法一：用 Github API - 這也是為何我把紀錄放在 Github CLI 這邊
    - 法二：Github Migration API 服務 - https://docs.github.com/en/rest/migrations
  - 參考：https://docs.github.com/en/repositories/archiving-a-github-repository/backing-up-a-repository
    - 這裡也提到備份 Github Repo 的 Wiki - 當然好佳在 Wiki 跟 Gist 都是 Git repo，相對好備份。
    - 或許該思考的是 Release Binary 跟 workflow (Github Actions) 是否需要備份
- 實驗：
  - 目標：備份 https://github.com/datacontw/DataCon.TW_2020/issues 成 JSON 檔
```bash
jazzw@JazzBook:~$ gh api repos/datacontw/DataCon.TW_2020/issues | tee issues_backup.json
```
  - 結果：把備份檔也 commit 回 https://github.com/datacontw/DataCon.TW_2020/
```bash
jazzw@JazzBook:~/git$ gh repo clone datacontw/DataCon.TW_2020
Cloning into 'DataCon.TW_2020'...
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (4/4), 4.54 KiB | 4.54 MiB/s, done.
jazzw@JazzBook:~/git$ cd DataCon.TW_2020/
jazzw@JazzBook:~/git/DataCon.TW_2020$ gh api repos/datacontw/DataCon.TW_2020/issues | tee issues_backup.json
jazzw@JazzBook:~/git/DataCon.TW_2020$ git add issues_backup.json
jazzw@JazzBook:~/git/DataCon.TW_2020$ git commit -a -m "chore: backup issue history (in JSON format)"
jazzw@JazzBook:~/git/DataCon.TW_2020$ git push
jazzw@JazzBook:~/git/DataCon.TW_2020$ cd ..
```
  - 備份 https://github.com/datacontw/DataCon.TW_2022/issues 成 JSON 檔
  - 結果：原來 Github Repo 的 Project Issue 跟 Repo Issue 是分開的！！
```bash
jazzw@JazzBook:~/git$ gh repo clone datacontw/DataCon.TW_2022
jazzw@JazzBook:~/git$ cd DataCon.TW_2022/
jazzw@JazzBook:~/git/DataCon.TW_2022$ gh api repos/datacontw/DataCon.TW_2022/issues | tee issues_backup.json
[]
jazzw@JazzBook:~/git/DataCon.TW_2022$ cd ..
jazzw@JazzBook:~/git$ rm -rf DataCon.TW_2022/
```
- ( 2024-11-21 12:50:28 )
- 來研究一下怎麼用 Github CLI 查詢 Project
```bash
jazzw@JazzBook:~/git$ gh project list
error: your authentication token is missing required scopes [read:project]
To request it, run:  gh auth refresh -s read:project

jazzw@JazzBook:~/git$ gh auth refresh -s read:project

! First copy your one-time code: 4E51-E1E1
Press Enter to open https://github.com/login/device in your browser...
✓ Authentication complete.
```
- 重新取得 authentication token 後，再來列舉看看
```bash
jazzw@JazzBook:~/git$ gh project list --owner datacontw
NUMBER  TITLE                         STATE  ID
4       @jazzwang's untitled project  open   PVT_kwDOA-Wp984Ap8R0
3       DataCon.TW 2026               open   PVT_kwDOA-Wp984Ap8Ry
2       DataCon.TW 2025               open   PVT_kwDOA-Wp984Ap8Rx
1       DataCon.TW 2022               open   PVT_kwDOA-Wp984AHyfU
```
- 實際上 Project `DataCon.TW 2022` 應該連結到 https://github.com/datacontw/DataCon.TW_2022/issues
  - 我後來在 https://github.com/datacontw/DataCon.TW_2022/issues?q=is%3Aissue+is%3Aclosed 找到已經完成的 issues
```bash
jazzw@JazzBook:~/git/snippet$ gh project item-list
? Which owner would you like to use? datacontw
? Which project would you like to use? DataCon.TW 2022 (#1)
TYPE   TITLE                                         NUMBER  REPOSITORY                 ID
Issue  [金][稅] 11-12 月營業稅(發票)繳納             38      datacontw/DataCon.TW_2022  PVTI_lADOA-Wp984AHyfUzgDknCU
Issue  [金] 活動通收入結算                           33      datacontw/DataCon.TW_2022  PVTI_lADOA-Wp984AHyfUzgDknDk
Issue  [金][志工][講者] 準備活動現場所需現金         32      datacontw/DataCon.TW_2022  PVTI_lADOA-Wp984AHyfUzgDknHk
Issue  [金][地][食] 支付尾款 場地便當茶點            34      datacontw/DataCon.TW_2022  PVTI_lADOA-Wp984AHyfUzgDknL8
Issue  [金][稅][法] 開立電子發票                     37      datacontw/DataCon.TW_2022  PVTI_lADOA-Wp984AHyfUzgDkm_I
Issue  [人][志工] 活動通 -- 志工出票                 35      datacontw/DataCon.TW_2022  PVTI_lADOA-Wp984AHyfUzgDoHH8
Issue  [人][志工] 志工分工與行前須知                 36      datacontw/DataCon.TW_2022  PVTI_lADOA-Wp984AHyfUzgDoHKs
Issue  通知線上與會方式與預演時段                    31      datacontw/DataCon.TW_2022  PVTI_lADOA-Wp984AHyfUzgDkm7Q
Issue  [技][視訊平台] 測試 Teams Live 播放預錄影片   27      datacontw/DataCon.TW_2022  PVTI_lADOA-Wp984AHyfUzgDZmi0
Issue  [人][講者] 活動通 -- 講者出票                 28      datacontw/DataCon.TW_2022  PVTI_lADOA-Wp984AHyfUzgDknbA
Issue  [人][講者] 講者溝通與追蹤事項                 24      datacontw/DataCon.TW_2022  PVTI_lADOA-Wp984AHyfUzgDZRJ8
Issue  [物][設備] 分軌議程公用筆電                   26      datacontw/DataCon.TW_2022  PVTI_lADOA-Wp984AHyfUzgDZRR8
Issue  [地][物][場地] 回覆 NTHCC 活動事項確認        25      datacontw/DataCon.TW_2022  PVTI_lADOA-Wp984AHyfUzgDdu6s
Issue  [金][地][場地] 支付訂金                       21      datacontw/DataCon.TW_2022  PVTI_lADOA-Wp984AHyfUzgDZRHI
Issue  [人][志工] 徵求活動志工                       20      datacontw/DataCon.TW_2022  PVTI_lADOA-Wp984AHyfUzgDZ54Y
Issue  [銷][網站] 設定 https://2022.datacon.tw 後台  19      datacontw/DataCon.TW_2022  PVTI_lADOA-Wp984AHyfUzgDZmkM
Issue  [銷][臉書] 粉絲頁圖檔                         17      datacontw/DataCon.TW_2022  PVTI_lADOA-Wp984AHyfUzgDZ6zk
Issue  [人][聽眾] 設定活動通售票                     16      datacontw/DataCon.TW_2022  PVTI_lADOA-Wp984AHyfUzgDZRIM
Issue  [時][地][場地] 回覆報價並確認使用時段         15      datacontw/DataCon.TW_2022  PVTI_lADOA-Wp984AHyfUzgDZRF8
Issue  [技][視訊平台] 訂閱 Office 365 E1             18      datacontw/DataCon.TW_2022  PVTI_lADOA-Wp984AHyfUzgDZmiA
Issue  [時][議程] 根據投稿意願時段，安排下午議程     14      datacontw/DataCon.TW_2022  PVTI_lADOA-Wp984AHyfUzgDZRO0
Issue  [金][預算] 預估收支，決定票種與票價           13      datacontw/DataCon.TW_2022  PVTI_lADOA-Wp984AHyfUzgDZRQk
```
- 看起來被標成 closed 的 issue 預設不會顯示出來
```bash
jazzw@JazzBook:~/git/snippet$ gh issue list -R datacontw/DataCon.TW_2022
no open issues in datacontw/DataCon.TW_2022
```
- 加上 `-s all` 就會顯示全部了
```bash
jazzw@JazzBook:~/git/snippet$ gh issue list -R datacontw/DataCon.TW_2022 -s all

Showing 30 of 37 issues in datacontw/DataCon.TW_2022 that match your search

ID   TITLE                                                              LABELS                                                            UPDATED
#38  [金][稅] 11-12 月營業稅(發票)繳納                                  Logistics                                                         about 4 months ago
#37  [金][稅][法] 開立電子發票                                          Logistics                                                         about 1 year ago
#36  [人][志工] 志工分工與行前須知                                                                                                        about 1 year ago
#35  [人][志工] 活動通 -- 志工出票                                      Logistics                                                         about 1 year ago
#34  [金][地][食] 支付尾款 場地便當茶點                                 Logistics                                                         about 1 year ago
#33  [金] 活動通收入結算                                                Logistics                                                         about 1 year ago
#32  [金][志工][講者] 準備活動現場所需現金                              Logistics                                                         about 1 year ago
#31  通知線上與會方式與預演時段                                         Logistics                                                         about 1 year ago
#30  [K3] Kafka 優化的最後一哩路                                                                                                          about 4 months ago
#29  [K2] 快速落地 Big Data 資料應用: 在 Trino / Presto 上從頭打造 ...                                                                    about 4 months ago
#28  [人][講者] 活動通 -- 講者出票                                      Logistics                                                         about 1 year ago
#27  [技][視訊平台] 測試 Teams Live 播放預錄影片                        Logistics                                                         about 1 year ago
#26  [物][設備] 分軌議程公用筆電                                        Logistics                                                         about 1 year ago
#25  [地][物][場地] 回覆 NTHCC 活動事項確認                             Logistics                                                         about 1 year ago
#24  [人][講者] 講者溝通與追蹤事項                                      Logistics                                                         about 1 year ago
#23  [物][印刷品] 識別證與海報設計稿                                    Logistics                                                         about 4 months ago
#22  [物][設備] 領夾式無線麥克風 -- 視訊收音用                          Logistics                                                         about 4 months ago
#21  [金][地][場地] 支付訂金                                            Logistics                                                         about 2 years ago
#20  [人][志工] 徵求活動志工                                            Logistics                                                         about 2 years ago
#19  [銷][網站] 設定 https://2022.datacon.tw 後台                       Logistics                                                         about 2 years ago
#18  [技][視訊平台] 訂閱 Office 365 E1                                  Logistics                                                         about 2 years ago
#17  [銷][臉書] 粉絲頁圖檔                                              Logistics                                                         about 2 years ago
#16  [人][聽眾] 設定活動通售票                                          Logistics                                                         about 2 years ago
#15  [時][地][場地] 回覆報價並確認使用時段                              Logistics                                                         about 2 years ago
#14  [時][議程] 根據投稿意願時段，安排下午議程                          Logistics                                                         about 2 years ago
#13  [金][預算] 預估收支，決定票種與票價                                Logistics                                                         about 2 years ago
#12  Overview of Synthetic Patient Data Generators 淺談病患資料產生器   Developer, Architecture, Data Generator, Agenda                   about 1 year ago
#11  MLOps 入門與實踐: 讓資料科學家高效且無後顧之憂地開發               Developer, Machine Learning, Data Science, MLOps, Agenda          about 4 months ago
#10  建立連接全世界資料的橋樑：特徵工程模組化工具                       Developer, Machine Learning, Data Science, Agenda                 about 4 months ago
#9   知識圖譜建置與投資應用                                             Application, Machine Learning, Data Science, Knowledge Graph,...  about 4 months ago
```
- 根據 https://docs.github.com/en/rest/issues/issues#list-repository-issues 的描述，Query parameters 中 `state` 預設為 `open`，可以選 `open`, `closed`, `all`
- ( 2024-11-21 14:15:28 )
- 再做一次
```bash
jazzw@JazzBook:~/git$ gh repo clone datacontw/DataCon.TW_2022
jazzw@JazzBook:~/git$ cd DataCon.TW_2022/
jazzw@JazzBook:~/git/DataCon.TW_2022$ gh api repos/datacontw/DataCon.TW_2022/issues?state=all > issues_backup.json
jazzw@JazzBook:~/git/DataCon.TW_2022$ git commit -a -m "chore: backup issue history (in JSON format)"
jazzw@JazzBook:~/git/DataCon.TW_2022$ git push
```
- ( 2024-11-21 14:31:40 )
- 練習直接用 Github CLI 對 repo 做 Archive 的動作（不能再發 issues / Pull Request 等）
```bash
jazzw@JazzBook:~$ gh repo archive  -h
Archive a GitHub repository.

With no argument, archives the current repository.

USAGE
  gh repo archive [<repository>] [flags]

FLAGS
  -y, --yes   Skip the confirmation prompt

INHERITED FLAGS
  --help   Show help for command

LEARN MORE
  Use `gh <command> <subcommand> --help` for more information about a command.
  Read the manual at https://cli.github.com/manual
  Learn about exit codes using `gh help exit-codes`
```
```
jazzw@JazzBook:~$ gh repo archive datacontw/DataCon.TW_2022
? Archive datacontw/DataCon.TW_2022? Yes
✓ Archived repository datacontw/DataCon.TW_2022
```
- 練習直接用 Github CLI 對 project 做 close 的動作。
```bash
jazzw@JazzBook:~$ gh project close
? Which owner would you like to use? datacontw
? Which project would you like to use? DataCon.TW 2022 (#1)
error: your authentication token is missing required scopes [project]
To request it, run:  gh auth refresh -s project
```
- 重新授權 `project` scope 的權限
```bash
jazzw@JazzBook:~$ gh auth refresh -s project

! First copy your one-time code: B2E1-5ACA
Press Enter to open https://github.com/login/device in your browser...
✓ Authentication complete.
```
- CLI 手動關閉成功
```bash
jazzw@JazzBook:~$ gh project close --owner datacontw
? Which project would you like to use? DataCon.TW 2022 (#1)
https://github.com/orgs/datacontw/projects/1
```

## 2025-07-06

- https://g.co/gemini/share/0313b8116d7b
<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
is it possible to use github cli (gh) to create a codespace template?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
While the GitHub CLI (`gh`) can be used to **create a codespace from an existing repository or template**, it doesn't have a direct command like `gh codespace create-template` to *create* a new codespace template from scratch in the same way you might create a new repository.

Here's how codespace templates work and how you can manage them, leveraging the GitHub CLI where applicable:

**How Codespace Templates Work:**

A GitHub Codespace template is essentially a regular GitHub repository that you've designated as a template. This repository typically contains:

1.  **Your project's starter files:** Boilerplate code, basic application structure, etc.
2.  **A `.devcontainer` folder:** This is crucial. It contains the `devcontainer.json` file and any other necessary configuration for your codespace environment (e.g., specifying the base image, pre-installed tools, extensions, port forwarding, post-creation commands).

**Steps to Create a Codespace Template (and where `gh` fits in):**

1.  **Create a new GitHub Repository:**

      * You can do this directly on GitHub.com.
      * You can also use the GitHub CLI:
        ```bash
        gh repo create my-codespace-template --template --public
        ```
        The `--template` flag is important here as it marks the repository as a template.

2.  **Clone the Repository Locally:**

    ```bash
    gh repo clone my-codespace-template
    cd my-codespace-template
    ```

3.  **Add Your Project Files and `.devcontainer` Configuration:**

      * Place your starter code, project structure, etc., into this repository.
      * **Crucially, create a `.devcontainer` folder at the root of your repository and add a `devcontainer.json` file.** This file defines your codespace environment. You can find many examples and documentation on `devcontainer.json` on the GitHub Docs and devcontainers.json schema.

4.  **Commit and Push Your Changes:**

    ```bash
    git add .
    git commit -m "Initial codespace template setup"
    git push
    ```

5.  **(Optional but Recommended) Make it a Template Repository (if you didn't in step 1):**

      * Navigate to your repository on GitHub.com.
      * Go to **Settings**.
      * Under "General" settings, check the "Template repository" option.

**Using the GitHub CLI with Codespace Templates:**

Once you have a repository set up as a codespace template, you can use `gh codespace create` to launch a new codespace from it:

```bash
gh codespace create -r <owner>/<repository-name> -b main
```

For example, if your template repository is `my-username/my-codespace-template`, you'd use:

```bash
gh codespace create -r my-username/my-codespace-template -b main
```

This will create a new codespace based on the `devcontainer.json` configuration and the files in your `my-codespace-template` repository. When a user creates a codespace from a template, the template repository's contents are cloned into their new codespace, and the link to the original template is severed. Users can then publish their work to a *new* repository under their own account.

**In summary:** The `gh` CLI is excellent for interacting with existing codespaces and creating new ones from repositories (including template repositories), but the "template creation" itself involves setting up a standard GitHub repository with a `.devcontainer` configuration and marking it as a template through GitHub's web interface or the `gh repo create --template` command.
</td></tr></table>
<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
could you give me a step-by-step command line instruction to create a github page?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Sure, here are step-by-step command-line instructions to create a GitHub Page. These instructions assume you already have Git and the GitHub CLI (`gh`) installed and authenticated on your system.

### Step-by-Step Command Line Instructions to Create a GitHub Page

**Goal:** Create a GitHub Page for a new or existing repository. We'll cover both user/organization pages (hosted at `username.github.io`) and project pages (hosted at `username.github.io/repository-name`).

-----

#### Option 1: User/Organization Page (e.g., `username.github.io`)

This type of page uses a special repository name.

1.  **Create a new repository with the specific name:**
    Your repository must be named exactly `YOUR_USERNAME.github.io` (replace `YOUR_USERNAME` with your actual GitHub username or organization name).

    ```bash
    gh repo create YOUR_USERNAME.github.io --public --description "My personal GitHub Page"
    ```

      * `gh repo create`: Command to create a new GitHub repository.
      * `YOUR_USERNAME.github.io`: The required repository name for a user/organization page.
      * `--public`: Makes the repository publicly accessible (required for GitHub Pages).
      * `--description`: An optional description for your repository.

2.  **Clone the newly created repository to your local machine:**

    ```bash
    gh repo clone YOUR_USERNAME.github.io
    cd YOUR_USERNAME.github.io
    ```

3.  **Create your `index.html` file (or other web content):**
    This is the main file that will be served. You can use a text editor directly in your terminal, or your preferred IDE.

    ```bash
    # Create the file using a simple echo command (for a basic test)
    echo '<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My GitHub Page</title>
    </head>
    <body>
        <h1>Hello from My GitHub Page!</h1>
        <p>This is a test page created via the command line.</p>
    </body>
    </html>' > index.html
    ```

    Or, if you prefer to open an editor:

    ```bash
    # For nano
    nano index.html
    # For vim
    vim index.html
    # For VS Code (if installed and added to PATH)
    code index.html
    ```

4.  **Add, commit, and push your changes to GitHub:**

    ```bash
    git add .
    git commit -m "Initial commit for GitHub Page"
    git push origin HEAD
    ```

5.  **Verify your GitHub Page:**
    It might take a few minutes for GitHub Pages to deploy. Once deployed, your page will be live at:

    `https://YOUR_USERNAME.github.io`

-----

#### Option 2: Project Page (e.g., `username.github.io/repository-name`)

This type of page uses an existing or new repository and typically serves content from the `gh-pages` branch or the `docs/` folder in the `main` branch.

**Scenario A: Starting with a New Repository**

1.  **Create a new repository for your project:**

    ```bash
    gh repo create my-project-page --public --description "My awesome project GitHub Page"
    ```

      * `my-project-page`: Replace with your desired project repository name.

2.  **Clone the repository:**

    ```bash
    gh repo clone my-project-page
    cd my-project-page
    ```

3.  **Choose your publishing source:**
    You have two common options: the `gh-pages` branch or the `docs/` folder on the `main` branch. The `gh-pages` branch is historically common, while the `docs/` folder is often simpler for single-page sites or documentation.

    **Option 2.A.1: Publish from `gh-pages` branch**

    a.  **Create and switch to the `gh-pages` branch:**

    ```bash
    git checkout --orphan gh-pages
    git rm -rf . # Remove all files from the previous branch (if any)
    ```
    * `git checkout --orphan gh-pages`: Creates a new branch named `gh-pages` without any commit history from the current branch.
    * `git rm -rf .`: Removes any files inherited from the previous branch, ensuring a clean slate for your web content.

    b.  **Create your `index.html` file:**

    ```bash
    echo '<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My Project Page</title>
    </head>
    <body>
        <h1>Welcome to My Project Page!</h1>
        <p>This page is hosted from the gh-pages branch.</p>
    </body>
    </html>' > index.html
    ```

    c.  **Add, commit, and push the `gh-pages` branch:**

    ```bash
    git add .
    git commit -m "Initial gh-pages content"
    git push origin gh-pages
    ```

    d.  **Configure GitHub Pages to serve from `gh-pages`:**
    Unfortunately, configuring the *source branch* for GitHub Pages is not directly supported by `gh cli` as of now. You'll need to do this step on GitHub.com:
    \* Go to your repository on GitHub.com (`github.com/YOUR_USERNAME/my-project-page`).
    \* Click on **Settings**.
    \* In the left sidebar, click on **Pages**.
    \* Under "Build and deployment", for "Source", select **Deploy from a branch**.
    \* For "Branch", select `gh-pages` and `/ (root)`.
    \* Click **Save**.

    **Option 2.A.2: Publish from `main` branch's `docs/` folder**

    a.  **Ensure you are on the `main` branch:**

    ```bash
    git checkout main
    ```

    b.  **Create a `docs` directory:**

    ```bash
    mkdir docs
    cd docs
    ```

    c.  **Create your `index.html` file inside `docs/`:**

    ```bash
    echo '<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My Project Page</title>
    </head>
    <body>
        <h1>Welcome to My Project Page!</h1>
        <p>This page is hosted from the docs folder on the main branch.</p>
    </body>
    </html>' > index.html
    ```

    d.  **Navigate back to the repository root, add, commit, and push:**

    ```bash
    cd .. # Go back to the root of the repository
    git add .
    git commit -m "Add GitHub Pages content in docs/"
    git push origin main
    ```

    e.  **Configure GitHub Pages to serve from `main` branch's `docs/` folder:**
    Similar to the `gh-pages` option, this step currently requires the web interface:
    \* Go to your repository on GitHub.com (`github.com/YOUR_USERNAME/my-project-page`).
    \* Click on **Settings**.
    \* In the left sidebar, click on **Pages**.
    \* Under "Build and deployment", for "Source", select **Deploy from a branch**.
    \* For "Branch", select `main` and `/docs`.
    \* Click **Save**.

4.  **Verify your GitHub Project Page:**
    It might take a few minutes for GitHub Pages to deploy. Once deployed, your page will be live at:

    `https://YOUR_USERNAME.github.io/my-project-page` (replace `my-project-page` with your actual repository name)

-----

**Important Notes:**

  * **Custom Domains:** You can configure custom domains for your GitHub Pages. This process involves adding a `CNAME` file to your repository and setting up DNS records with your domain provider. This is typically done through the GitHub web interface under **Repository Settings \> Pages**.
  * **Jekyll:** GitHub Pages has built-in support for Jekyll, a static site generator. If you plan to use Jekyll, your workflow will involve building your Jekyll site and pushing the output (usually to the `_site` directory) to your GitHub Pages source.
  * **Deployment Time:** GitHub Pages deployment can take a few minutes. If your page doesn't appear immediately, give it some time. You can often see the deployment status in your repository's "Actions" tab.
  * **Troubleshooting:** If your page isn't showing up, check the "Pages" section in your repository settings on GitHub.com for any error messages or build logs. Also, ensure your `index.html` file (or other entry point) is correctly named and located according to your chosen publishing source.
</td></tr></table>

- ( 2025-07-06 08:07:26 )
- 實測：
```bash
~/git/aider-labs$ ls
LICENSE
~/git/aider-labs$ git checkout --orphan gh-pages
Switched to a new branch 'gh-pages'
~/git/aider-labs$ git rm -rf .
rm 'LICENSE'
~/git/aider-labs$ ls
~/git/aider-labs$ git br
  main                9a5d7da [origin/main] Initial commit
  remotes/origin/HEAD -> origin/main
  remotes/origin/main 9a5d7da Initial commit
~/git/aider-labs$ echo '<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Project Page</title>
</head>
<body>
    <h1>Welcome to My Project Page!</h1>
    <p>This page is hosted from the docs folder on the main branch.</p>
</body>
</html>' > index.html
~/git/aider-labs$ git add .
warning: in the working copy of 'index.html', LF will be replaced by CRLF the next time Git touches it
~/git/aider-labs$ git commit -m "Initial gh-pages content"
[gh-pages (root-commit) 194fee5] Initial gh-pages content
 1 file changed, 12 insertions(+)
 create mode 100644 index.html
~/git/aider-labs$ git remote set-url --push origin git@github.com:jazzwang/aider-labs.git
~/git/aider-labs$ git push origin gh-pages
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 16 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 435 bytes | 217.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote:
remote: Create a pull request for 'gh-pages' on GitHub by visiting:
remote:      https://github.com/jazzwang/aider-labs/pull/new/gh-pages
remote:
To github.com:jazzwang/aider-labs.git
 * [new branch]      gh-pages -> gh-pages
```
- 一開始如果沒有照上面的步驟加上 `--template` 參數，事後還是可以透過 `gh` 指令修改。
  - 在 git repo 底下，輸入 `gh repo edit` 勾選要用 `Template` 跟 `Topic`，就可以把該 Github Repo 改成 Template，並且可以指定要顯示在 `Topic` 的關鍵字。
```bash
~/git/aider-labs$ gh repo edit
? What do you want to edit? Template Repository, Topics
? Convert into a template repository? Yes
? Add topics?(csv format) tutorial
✓ Edited repository jazzwang/aider-labs
```

## 2025-12-10

- 緣起：想要查詢 Github Enterprise 上，特定使用者曾經貢獻過哪些 Git Repo
<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
are there github api or gh cli command to list of git repositories contributed by specific user?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Yes, there are methods using the **GitHub API** to list repositories a specific user has contributed to, though it's not a single, direct endpoint for "all contributed repositories." There is also a powerful way to do this using the **`gh cli`** by combining commands.

-----

## 💻 Using the GitHub REST API (Advanced Method)

The GitHub REST API doesn't have a direct endpoint like `/users/{username}/contributed_repos`. A common and effective workaround is to use the **Search API** to find all the user's **Pull Requests (`type:pr`)** and then extract the repository information from those results.

### 1\. API Endpoint

You will use the **Search Issues and Pull Requests** endpoint:

  * **Endpoint:** `GET /search/issues`
  * **Query Parameter (`q`):** You must construct a search query string. To find all Pull Requests authored by a specific user, the query is: `q=author:{username}+type:pr`
      * **Example for user `octocat`:** `q=author:octocat+type:pr`
  * **Pagination:** You'll need to paginate through the results to get a complete list, as the API limits results per page (max 100) and the total number of results returned (up to 1,000 for searches).

### 2\. Request Example (with `curl`)

This example uses `curl` and `jq` (a command-line JSON processor) to fetch the first page of results and list the unique repository names (`owner/repo`). You'd need a loop to handle multiple pages.

```bash
curl -sS -G \
  "https://api.github.com/search/issues" \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Authorization: token YOUR_GITHUB_TOKEN" \
  --data-urlencode "q=author:octocat+type:pr" \
  | jq -r '.items[] | .repository_url' \
  | grep -oP 'repos/\K.*' \
  | sort -u
```

## 🛠️ Using the GitHub CLI (`gh cli`)

The **GitHub CLI (`gh`)** provides the most convenient way to do this from the command line by leveraging the same Search API logic with a simpler syntax.

### 1\. `gh api` Command

You can use the `gh api` command to hit the same Search API endpoint and pipe the output to `jq`:

```bash
gh api search/issues \
  -X GET \
  -f q='author:octocat type:pr' \
  --paginate \
  --jq '.items[] | .repository_url' \
  | grep -oP 'repos/\K.*' \
  | sort -u
```

  * **`gh api search/issues`**: Calls the `/search/issues` endpoint.
  * **`-f q='...'`**: Sets the query parameter.
  * **`--paginate`**: **Crucially**, this handles the API pagination automatically, fetching all pages up to the 1000-result limit.
  * **`--jq '.items[] | .repository_url'`**: Extracts the URL of the repository for each Pull Request item.
  * **`grep -oP 'repos/\K.*'`**: A common way to strip the initial part of the URL (`https://api.github.com/repos/`) to get just the `owner/repo` name.
  * **`sort -u`**: Ensures you get a list of **unique** repository names.

Replace `octocat` with the desired username.

-----

Would you like me to generate a complete shell script that automatically iterates through all pages of the Search API to get the full list of repositories contributed by a specific user?
</td></tr></table>
- 上述結果看起來比較像是特定使用者曾經發過的 Pull Request 列表
- 實測：用 Github 個人帳號
```bash
~/git/snippet$ gh api search/issues \
  -X GET \
  -f q='author:octocat type:pr' \
  --paginate \
  --jq '.items[] | .repository_url' \
  | grep -oP 'repos/\K.*' \
  | sort -u
octocat/Hello-World
violet-org/boysenberry-repo
```
- 這個查詢代表 `octocat` 這個帳號曾經發過 PR 到 `octocat/Hello-World` 跟 `violet-org/boysenberry-repo`
- 改成查我自己
```bash
~/git/snippet$ gh api search/issues -X GET -f q='author:jazzwang type:pr' --paginate --jq '.items[] | .repository_url' | grep -oP 'repos/\K.*' | sort -u
awsdocs/amazon-cloudwatch-user-guide
cloudera/cm_api
Homebrew/homebrew-cask
hueitan/made-in-taiwan
jazzwang/hicloud-hadoop
mitaketw/sms-java
tenmax/azurekit
```
- 改問能否查詢曾經 commit 過的 git repo 列表
<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
are there github api or gh cli command to list of git repositories committed by specific user?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Yes, you can list the GitHub repositories a specific user has committed to using both the **GitHub API** (specifically the GraphQL API or Search REST API) and a powerful two-step method with the **GitHub CLI (`gh`)**.

There is no single, simple command for this, as a user's commits can be scattered across thousands of repositories they don't own. The most efficient methods involve leveraging GitHub's search capabilities.

-----

## 🛠️ Using the GitHub CLI (`gh`)

The GitHub CLI provides the most accessible command-line solution by using its built-in search functionality (`gh search commits`) and parsing the results.

### `gh cli` Command

You can use the `gh search commits` command to find all commits authored by a user, extract the repository names from those results, and then list the unique names.

```bash
gh search commits --author=USERNAME --json repository \
  --limit 1000 \
  | jq -r '.[] | .repository.nameWithOwner' \
  | sort -u
```

  * **`gh search commits`**: Searches across GitHub's commit history.
  * **`--author=USERNAME`**: Filters the search to include only commits authored by the specified GitHub `USERNAME`.
  * **`--json repository`**: Tells the command to output the result in JSON format and only include the `repository` object for each commit.
  * **`--limit 1000`**: Sets the maximum number of results to retrieve (the maximum for this search endpoint is generally 1,000 commits). For a more complete list, you'd need to paginate (see the API section).
  * **`| jq -r '.[] | .repository.nameWithOwner'`**: Uses the `jq` tool to extract the full repository name (e.g., `owner/repo-name`) from the JSON output.
  * **`| sort -u`**: Sorts the list alphabetically and filters out duplicate repository names, giving you a clean list of unique repositories.

-----

## 💻 Using the GitHub API (GraphQL is Recommended)

The GraphQL API is superior to the REST API for this task because it allows you to retrieve the repository information directly while fetching the commit contributions, making it far more efficient than the REST API's search endpoint.

### 1\. GraphQL Query

You can use the `repositoriesContributedTo` field on the `User` object. This specifically lists repositories where the user has made contributions (including commits, pull requests, and issues).

  * **Endpoint:** `POST https://api.github.com/graphql`
  * **Query Example:**

<!-- end list -->

```graphql
query CommitsBy($username: String!, $cursor: String) {
  user(login: $username) {
    repositoriesContributedTo(
      first: 100
      after: $cursor
      contributionTypes: [COMMIT]
      # Set to PUBLIC or ALL (requires auth with 'repo' scope)
      privacy: PUBLIC 
    ) {
      pageInfo {
        hasNextPage
        endCursor
      }
      nodes {
        nameWithOwner
      }
    }
  }
}
```

### 2\. Execution with `gh api` (The easiest way)

You can execute this GraphQL query directly using the `gh api` command, which simplifies authentication and pagination (if you remove the pagination logic and rely on the maximum `first: 100` results).

```bash
gh api graphql -f query='
  query($username: String!) {
    user(login: $username) {
      repositoriesContributedTo(
        first: 100
        contributionTypes: [COMMIT]
        privacy: PUBLIC
      ) {
        nodes {
          nameWithOwner
        }
      }
    }
  }
' -f username='octocat' | jq -r '.data.user.repositoriesContributedTo.nodes[] | .nameWithOwner'
```

  * **Note:** The GraphQL API also requires **pagination** (using the `after: $cursor` variables) to get a truly complete list of hundreds or thousands of contributed repositories. The script above only retrieves the first 100 results.

Would you like me to show you how to construct a more complex script that handles the necessary **pagination** using the GraphQL API or the REST API search command for a full, comprehensive list?
</td></tr></table>

- 實測：

  ```bash
  ~/git/snippet$ gh search commits --author=jazzwang --json repository \
    --limit 1000 \
    | jq -r '.[] | .repository.nameWithOwner' \
    | sort -u
  null
  ```

- 把 `nameWithOwner` 改成 `url` 就對了～應該是 JSON Schema 有變化造成 Gemini 誤判

  ```bash
  ~/git/snippet$ gh search commits --author=jazzwang --json repository   --limit 1000   | jq -r '.[] | .repository.url'   | sort -u
  https://github.com/aiham/cloudera-director
  https://github.com/alxdrl/homebrew-cask
  https://github.com/armenelruth/homebrew-cask
  https://github.com/astzweig/homebrew-cask
  https://github.com/awsdocs/amazon-cloudwatch-user-guide
  https://github.com/colinshr/homebrew-cask2
  https://github.com/colinshr/homebrew-cask3
  https://github.com/colinshr/homebrew-cask4
  https://github.com/crawlzilla/crawlzilla.github.com
  https://github.com/datacontw/DataCon.TW_2020
  https://github.com/datacontw/datacon.tw_2020_test_scripts
  https://github.com/edsolis/homebrew-cask-mirror
  https://github.com/etusolution/EHC_2014
  https://github.com/FluentdTW/fluentd-labs
  https://github.com/HadoopTW/communities-dashboard
  https://github.com/HadoopTW/CS100.1x
  https://github.com/HadoopTW/spark_labs
  https://github.com/Homebrew/homebrew-cask
  https://github.com/jazzwang/advent-of-code
  https://github.com/jazzwang/aider-labs
  https://github.com/jazzwang/cloud-interop
  https://github.com/jazzwang/confluence-insight
  https://github.com/jazzwang/data-pipeline-labs
  https://github.com/jazzwang/docker-pool
  https://github.com/jazzwang/dotfiles
  https://github.com/jazzwang/dotnet-codespace
  https://github.com/jazzwang/f-motif
  https://github.com/jazzwang/GenAI
  https://github.com/jazzwang/github-action-lab
  https://github.com/jazzwang/gitpod-labs
  https://github.com/jazzwang/hadoop_labs
  https://github.com/jazzwang/haduzilla
  https://github.com/jazzwang/hicloud-hadoop
  https://github.com/jazzwang/hive_labs
  https://github.com/jazzwang/homebrew-lab
  https://github.com/jazzwang/hpt-chat
  https://github.com/jazzwang/init-spark-sql
  https://github.com/jazzwang/init-spark-stream
  https://github.com/jazzwang/jazzwang.github.io
  https://github.com/jazzwang/katacoda-scenarios
  https://github.com/jazzwang/ms-teams-chatbot
  https://github.com/jazzwang/nyc-tlc
  https://github.com/jazzwang/preseed
  https://github.com/jazzwang/pytest-selenium-ci
  https://github.com/jazzwang/react-labs
  https://github.com/jazzwang/sbt-liquibase-sqlite
  https://github.com/jazzwang/scala-spark.g8
  https://github.com/jazzwang/scoop-bucket
  https://github.com/jazzwang/serverless-wordpress
  https://github.com/jazzwang/skills-copilot-codespaces-vscode
  https://github.com/jazzwang/snippet
  https://github.com/jazzwang/vagrant-gcp
  https://github.com/jazzwang/vagrant-hadoop
  https://github.com/jazzwang/vagrant-pool
  https://github.com/jazzwang/webex-recorder
  https://github.com/korczis/mahout-spark
  https://github.com/liling0509/tea-test
  https://github.com/MaksSlot/cask
  https://github.com/phstudy/vagrant-hadoop-etu
  https://github.com/pr14m1990/cask
  https://github.com/TDEA-Study/DDIA-2020-1
  https://github.com/TheCoolBlackCat/homebrew-cask-orbstack
  https://github.com/vikrampratap21/AmazonCloudWatchAgent-Configuration-file
  https://github.com/X-oss-byte/homebrewcask
  https://github.com/xreg2/schema
  ~/git/snippet$
  ```

- 那如果想要看是誰 merge 了 PR 呢？
<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
are there github api or gh cli command to list of git repositories whose PR were  resolved by specific user?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Yes, the most reliable way to find a list of repositories where a specific user **merged** a Pull Request is by using the **GitHub Search API** or the **GitHub CLI (`gh`)** which wraps that API.

The key is to search for Pull Requests that are `merged` and filter by the `merger` user.

-----

## 🛠️ Using the GitHub CLI (`gh`)

The `gh` CLI provides the most straightforward command-line method by combining the powerful Search API with JSON filtering (`jq`).

### 1\. The `gh` Command

You use the `gh api` command to access the GitHub Search API and construct a query that filters for merged PRs by the merger.

```bash
gh api search/issues \
  -X GET \
  -f q='is:pr is:merged merger:USERNAME' \
  --paginate \
  --jq '.items[] | .repository_url' \
  | grep -oP 'repos/\K.*' \
  | sort -u
```

| Component | Purpose |
| :--- | :--- |
| **`is:pr is:merged`** | Filters the results to only include Pull Requests that have been merged. |
| **`merger:USERNAME`** | Filters those merged PRs to include only the ones where the specified `USERNAME` was the one who clicked the merge button. |
| **`--paginate`** | Handles API pagination automatically to retrieve more than the default 30 results (up to the search API limit of 1000). |
| **`--jq '... | .repository_url'`** | Uses `jq` to extract the full repository API URL from each result item. |
| **`grep -oP 'repos/\K.*'`** | Strips the API prefix to give you the clean `owner/repo-name`. |
| **`sort -u`** | Sorts the repository names and lists only **unique** names. |

-----

## 💻 Using the GitHub REST API (Advanced Search)

You can achieve the same result directly using the **REST API's Search Issues and Pull Requests** endpoint. This requires manual handling of pagination in your script.

### 1\. API Endpoint and Query

  * **Endpoint:** `GET /search/issues`
  * **Query Parameter (`q`):**
      * `q=is:pr+is:merged+merger:USERNAME`

### 2\. Request Example (`curl` with Pagination Concept)

You would need a loop to increment the `&page=` parameter until `total_count` is reached or the array of `items` is empty.

A single-page request example (assuming you use a tool like `jq` to process the JSON):

```bash
curl -sS -G \
  "https://api.github.com/search/issues" \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Authorization: token YOUR_GITHUB_TOKEN" \
  --data-urlencode "q=is:pr is:merged merger:octocat" \
  --data-urlencode "per_page=100" \
  | jq -r '.items[] | .repository_url' \
  | grep -oP 'repos/\K.*' \
  | sort -u
```

-----

The user in this scenario would be looking for the fastest, most effective way to track merge activity, which the `gh cli` provides in a single command. The included video shows how to use the `gh cli` for general PR management.

You can learn more about managing pull requests from the command line by checking out [Create, View, and Merge GitHub PRs with the gh CLI](https://www.youtube.com/watch?v=EXlLKq4kuvQ).
</td></tr></table>
- 如果想查有參與過 PR Review 的呢？
<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
are there github api or gh cli command to list of git repositories whose PR were  reviewed by specific user?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Yes, the most effective way to list repositories where a specific user has **reviewed** a Pull Request is by using the **GitHub Search API** or the **GitHub CLI (`gh`)**, which utilizes the same search capabilities.

The key is to search for Pull Requests where the user is listed as a **reviewer** using the specific search qualifier.

-----

## 🛠️ Using the GitHub CLI (`gh`)

The `gh` CLI offers the most convenient command-line method by executing the API search and handling the output and pagination for you.

### 1\. The `gh` Command

You use the `gh api` command to access the GitHub Search API and construct a query that filters for Pull Requests reviewed by the specific user (`reviewed-by`).

```bash
gh api search/issues \
  -X GET \
  -f q='is:pr reviewed-by:USERNAME' \
  --paginate \
  --jq '.items[] | .repository_url' \
  | grep -oP 'repos/\K.*' \
  | sort -u
```

| Component | Purpose |
| :--- | :--- |
| **`is:pr`** | Filters the results to only include Pull Requests (excluding issues). |
| **`reviewed-by:USERNAME`** | Filters for PRs where the specified `USERNAME` has submitted a review (Approved, Commented, or Requested Changes). |
| **`--paginate`** | **Crucially**, this handles API pagination automatically, fetching all pages up to the search API limit (typically 1,000 results). |
| **`--jq '... | .repository_url'`** | Uses `jq` to extract the full API URL for the repository associated with each PR. |
| **`grep -oP 'repos/\K.*'`** | Strips the API prefix to yield the clean repository name, e.g., `owner/repo-name`. |
| **`sort -u`** | Sorts the list alphabetically and filters out duplicate repository names. |

### 2\. Filtering by Review Status (Optional)

You can refine this query if you only want to see repositories where the user **approved** the PR by changing the query:

  * **For Approved Reviews:** `q='is:pr review:approved reviewed-by:USERNAME'`
  * **For Reviews Requesting Changes:** `q='is:pr review:changes-requested reviewed-by:USERNAME'`

-----

## 💻 Using the GitHub API (GraphQL is Alternative)

While the REST API's Search endpoint is the most direct way, the **GraphQL API** also provides a dedicated way to list repositories a user has contributed reviews to.

You can use the `pullRequestReviewContributionsByRepository` field within a user's `contributionsCollection`. This is more powerful for getting a truly comprehensive list beyond the 1000-item limit of the Search API, but requires writing a slightly more complex, paginated GraphQL query.

### GraphQL Field Snippet:

```graphql
{
  user(login: "USERNAME") {
    contributionsCollection {
      pullRequestReviewContributionsByRepository {
        repository {
          nameWithOwner
        }
        # ... other details
      }
    }
  }
}
```

You would use the `gh api graphql` command to execute this, adding pagination logic to retrieve all results.
</td></tr></table>

- 後記：
  - 後來把 Github CLI 的 Authentication 切換成 Github Enterprise 確實也可以得到團隊成員曾經 commit 過的 Git Repo
  - 搭配 git-extras 的 `git summary --line` 就可以得到每個團隊成員貢獻的程式碼總行數
  - 當然也可以得到總 commit 次數跟 Merge 了多少 PR，Review 了多少 PR
  - 這有點像是 Github 開發者個人版上的雷達圖，可以生成一個「量化」的貢獻度視覺化圖表