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