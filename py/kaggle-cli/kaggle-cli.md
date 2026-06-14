# kaggle-cli

- Git Repo
  - https://github.com/Kaggle/kaggle-cli

## 2026-06-14

- Learned from Kaggle Discord
  - 2026-05-28
  - Kaggle CLI Update: Forums, Competition Topics, Benchmarks, and OAuth! (v2.2.0)
  - https://www.kaggle.com/discussions/product-announcements/702989
- 安裝 - 文件是寫 `pip install kaggle` 我先試試看用 `uv` 安裝看看
```bash
~/git/snippet$ uv tool install kaggle
```
- 驗證
```bash
~/git/snippet$ which kaggle
/c/Users/jazzw/scoop/persist/uv/tools/shims/kaggle
~/git/snippet$ kaggle -h
usage: python.exe C:\Users\jazzw\scoop\persist\uv\tools\shims\kaggle [-h] [-v] [-W]
                                                                     {competitions,c,datasets,d,kernels,k,models,m,files,forums,f,benchmarks,b,config,auth,quota} ...

options:
  -h, --help            show this help message and exit
  -v, --version         Print the Kaggle CLI version
  -W, --no-warn         Disable out-of-date API version warning

commands:
  {competitions,c,datasets,d,kernels,k,models,m,files,forums,f,benchmarks,b,config,auth,quota}
                        Use one of:
                        competitions {list, files, download, submit, submissions, leaderboard, team-submissions, episodes, replay, logs, pages, topics, topic-messages}
                        competitions topics {list, show}
                        datasets {list, files, download, create, version, init, metadata, status, delete, topics}
                        datasets topics {list, show}
                        kernels {list, files, get, init, push, pull, output, status, logs, update, delete}
                        models {instances, i, variations, v, get, list, init, create, delete, update, topics}
                        models topics {list, show}
                        models variations {versions, v, get, files, list, init, create, delete, update}
                        models variations versions {init, create, download, delete, files, list}
                        forums {list, topics}
                        forums topics {list, show}
                        benchmarks {tasks, t, auth, init, topics}
                        benchmarks topics {list, show}
                        config {view, set, unset}
                        auth {login, print-access-token, revoke}
                        quota
    competitions (c)    Commands related to Kaggle competitions
    datasets (d)        Commands related to Kaggle datasets
    kernels (k)         Commands related to Kaggle kernels
    models (m)          Commands related to Kaggle models
    files               Commands related files
    forums (f)          Commands related to Kaggle discussion forums
    benchmarks (b)      Commands related to Kaggle benchmarks
    config              Configuration settings
    auth                Commands related to authentication
    quota               Show the current user's weekly GPU and TPU accelerator quota
```
- 登入
```bash
~/git/snippet$ kaggle auth
Authentication required to call the Kaggle API.

First, you will need a Kaggle account. You can sign up at
  https://www.kaggle.com/account/login

Recommended: log in with OAuth via a web-based authorization flow.
No token to manage; credentials are cached locally for you.
    kaggle auth login

If you'd rather not use OAuth, generate an API token at
  https://www.kaggle.com/settings/api  (click "Generate New Token" under "API")
and supply it to the CLI in one of these ways:

  Option A: Environment variable
    export KAGGLE_API_TOKEN=xxxxxxxxxxxxxx  # token copied from the settings UI

  Option B: API token file
    Save the token to ~/.kaggle/access_token
~/git/snippet$ kaggle auth login
Your browser has been opened to visit: ...
You are now logged in as [jazzwang]
```
- 論壇
```bash
~/git/snippet$ kaggle forums list
     id  name                   subtitle
-------  ---------------------  -----------------------------------------------------
     15  General                Announcements, resources, and interesting discussions
    208  Getting Started        The first stop for new Kagglers
    809  Product Feedback       Tell us what you love, hate, and wish for
    978  Product Announcements  New product features & updates from the Kaggle Team
   2239  Questions & Answers    Technical advice from other data scientists
2605300  Competition Hosting    Advice and support on running your own competitions
3831795  Accomplishments        Celebrate success, share achievements!
~/git/snippet$ kaggle forums topics list
    id  title                                                                                      authorName               commentCount  votes  postDate   
------  -----------------------------------------------------------------------------------------  -----------------------  ------------  -----  --------------------------
708114  [Welcome + Setup Instructions] 5-Day AI Agents: Intensive Vibe Coding Course With Google   Kinjal Parekh                       0    206  2026-06-13 16:43:49.614000
708107  Codelabs FAQs                                                                              Kinjal Parekh                       0     95  2026-06-13 15:36:54.249000
```
- 論壇：應景一下 2026-06-13 的 5-Day AI Agents 開課公告
```bash
~/git/snippet$ kaggle forums topics show 708114
Topic #708114: [Welcome + Setup Instructions] 5-Day AI Agents: Intensive Vibe Coding Course With Google
  Author: Kinjal Parekh
  Posted: 2026-06-13 16:43:49.614000
  Votes: 206  Comments: 0

Welcome to our 5-Day AI Agents: Intensive Vibe Coding Course With Google!

Here’s a brief summary of how the course works and detailed instructions on how to get set up. You’ll receive your first assignment on Sunday, June 14, 2026.

How the Course Works

The course is designed to be flexible and interactive, allowing you to learn at your own pace while benefiting from live sessions and community engagement.
```
- Benchmark
  - 2026-06-04
  - Build AI Evals Locally with Kaggle Benchmarks
  - https://www.youtube.com/watch?v=c7B8vyehyUA
```bash
~/git/snippet$ kaggle benchmarks -h
usage: python.exe C:\Users\jazzw\scoop\persist\uv\tools\shims\kaggle benchmarks [-h] {tasks,t,auth,init,topics} ...

options:
  -h, --help            show this help message and exit

commands:
  {tasks,t,auth,init,topics}
    tasks (t)           Commands related to benchmark tasks
    auth                Fetch and persist Model Proxy credential information
    init                Fetch and persist  Model Proxy credentials and other Kaggle Benchmarks environment variables
    topics              List discussion topics for a benchmark
```