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
- ( 2024-11-18 16:57:40 )
- 抓取 `jazzwang` 所有給星星的專案，輸出到 STDOUT 並寫到 `jazzwang_starred.json` 檔案。
```bash
jazzw@JazzBook:~$ gh api --paginate users/jazzwang/starred | tee jazzwang_starred.json
```
- 由於給的星星數太多，所以一定要加 `--paginate` 才有辦法列出全部的專案。
- 驗證輸出的 JSON 檔案是否為合格的 JSON 格式。用 `jq .` 確認格式正確。因為只有一行，所以是 NDJSON 格式，可以用 PySpark 或 Spark Shell 做後續分析。