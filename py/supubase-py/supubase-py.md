# Supabase

- 在測試 https://www.chatbotui.com 的登入時，看到 Google OAuth 認證的網域名稱是 `ictjeriolkoxhduautym.supabase.co` 所以查了一下 `supabase` 是什麼。
- https://supabase.com/
> Supabase is an open source Firebase alternative.
> Start your project with a Postgres database, Authentication, instant APIs, Edge Functions, Realtime subscriptions, Storage, and Vector embeddings.

## 測試專案

- 看官方文件，有點找不太到合適的入口，所以找 Gemini 幫忙。
  - https://g.co/gemini/share/8bf8f2815d5a
- 試著照 Gemini 的步驟開始。第一步是安裝 Supabase CLI
  - 在 Google Cloud Shell 上測試，第一動的指令就出錯了。
```bash
jazzwang_tw@cloudshell:~/snippet/python/supubase-py$ npm install -g supabase
npm error code 1
npm error path /usr/local/nvm/versions/node/v20.17.0/lib/node_modules/supabase
npm error command failed
npm error command sh -c node scripts/postinstall.js
npm error node:internal/modules/run_main:129
npm error     triggerUncaughtException(
npm error     ^
npm error Installing Supabase CLI as a global module is not supported.
npm error Please use one of the supported package managers: https://github.com/supabase/cli#install-the-cli
npm error
npm error (Use `node --trace-uncaught ...` to show where the exception was thrown)
npm error
npm error Node.js v20.17.0
npm error A complete log of this run can be found in: /home/jazzwang_tw/.npm/_logs/2024-08-28T15_06_27_627Z-debug-0.log
jazzwang_tw@cloudshell:~/snippet/python/supubase-py$ 
```
- 參考 https://github.com/supabase/cli
- 修正指令
```bash
jazzwang_tw@cloudshell:~/snippet/python/supubase-py$ npm i supabase --save-dev
npm warn idealTree Removing dependencies.supabase in favor of devDependencies.supabase

up to date, audited 66 packages in 785ms

18 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities

jazzwang_tw@cloudshell:~/snippet/python/supubase-py$ ln -s ~/node_modules/supabase/bin/supabase ~/bin/supabase 
```
- 由於我有設定 `~/bin` 到 PATH 環境變數，所以就可以找到 `supabase` 指令
```bash
jazzwang_tw@cloudshell:~/snippet/python/supubase-py$ supabase 
Supabase CLI 1.191.3

Usage:
  supabase [command]

Quick Start:
  bootstrap            Bootstrap a Supabase project from a starter template

Local Development:
  db                   Manage Postgres databases
  gen                  Run code generation tools
  init                 Initialize a local project
  inspect              Tools to inspect your Supabase project
  link                 Link to a Supabase project
  login                Authenticate using an access token
  logout               Log out and delete access tokens locally
  migration            Manage database migration scripts
  seed                 Seed a Supabase project from supabase/config.toml
  start                Start containers for Supabase local development
  status               Show status of local Supabase containers
  stop                 Stop all local Supabase containers
  test                 Run tests on local Supabase containers
  unlink               Unlink a Supabase project

Management APIs:
  branches             Manage Supabase preview branches
  domains              Manage custom domain names for Supabase projects
  encryption           Manage encryption keys of Supabase projects
  functions            Manage Supabase Edge functions
  network-bans         Manage network bans
  network-restrictions Manage network restrictions
  orgs                 Manage Supabase organizations
  postgres-config      Manage Postgres database config
  projects             Manage Supabase projects
  secrets              Manage Supabase secrets
  services             Show versions of all Supabase services
  snippets             Manage Supabase SQL snippets
  ssl-enforcement      Manage SSL enforcement configuration
  sso                  Manage Single Sign-On (SSO) authentication for projects
  storage              Manage Supabase Storage objects
  vanity-subdomains    Manage vanity subdomains for Supabase projects

Additional Commands:
  completion           Generate the autocompletion script for the specified shell
  help                 Help about any command

Flags:
      --create-ticket                     create a support ticket for any CLI error
      --debug                             output debug logs to stderr
      --dns-resolver [ native | https ]   lookup domain names using the specified resolver (default native)
      --experimental                      enable experimental features
  -h, --help                              help for supabase
      --network-id string                 use the specified docker network instead of a generated one
  -v, --version                           version for supabase
      --workdir string                    path to a Supabase project directory

Use "supabase [command] --help" for more information about a command.
```
- 照第二步是跑 `supabase init`，不過從文件看起來，跑 `supabase bootstrap` 更好。
```
jazzwang_tw@cloudshell:~/snippet/python/supubase-py$ supabase bootstrap
Using workdir /home/jazzwang_tw
Enter a directory to bootstrap your project (or leave blank to use /home/jazzwang_tw/snippet/python/supubase-py): 

    Which starter template do you want to use?                                     
                                                                                   
    1. amazon-bedrock [Image Search with Amazon Bedrock and Supabase Vector.]      
    2. embeddings [AI Inference in Supabase Edge Functions.]                       
    3. pgvector-python [AI Inference Image Search with Supabase Vector in Python.]
    4. nextjs [A Next.js App Router template configured with cookie-based auth.]   
    5. expo [An Expo React Native User Management starter.]                        
    6. flutter [A Flutter User Management starter.]                                
    7. swift [A Swift User Management starter.]    
    8. rbac [A Next.js RBAC Slack clone starter.]
    9. @basejump/nextjs [A Next.js starter with personal accounts, teams, permissions and Stripe billing]
  >  10. scratch [An empty project from scratch.]          

Using workdir /home/jazzwang_tw
Enter a directory to bootstrap your project (or leave blank to use /home/jazzwang_tw/snippet/python/supubase-py): 
Do you want to overwrite existing files in /home/jazzwang_tw/snippet/python/supubase-py directory? [Y/n] 
Using workdir /home/jazzwang_tw
Generate VS Code settings for Deno? [y/N] 
Generate IntelliJ Settings for Deno? [y/N] 
Hello from Supabase! Press Enter to open browser and login automatically.

Here is your login link in case browser did not open https://supabase.com/dashboard/cli/login?session_id=0d05fb91-0eb3-4973-b1e5-06a7a53d6838&token_name=cli_jazzwang_tw@cs-216321250341-default_1724858616&public_key=04db51c57570d8808e727e1cf7bed91e1e5257d0b3e9c0d7c75d1e4ee061bd6369ac235074bc13684bc9c362498798e01d46d65351e985d730a07e74329f0ec214

exec: "xdg-open": executable file not found in $PATH
context canceled
```
- 好吧，看起來這個 `supabase bootstrap` 指令雖然提供了 10 種範本，但相依 X-Window 環境（在 Linux 上）。所以還是改跑 `supabase init` 吧！
```bash
jazzwang_tw@cloudshell:~/snippet/python/supubase-py$ supabase init
Generate VS Code settings for Deno? [y/N] y
Generated VS Code settings in .vscode/settings.json. Please install the recommended extension!
Finished supabase init.
jazzwang_tw@cloudshell:~/snippet/python/supubase-py$ tree . .vscode/
.
├── README.md
└── supabase
    ├── config.toml
    └── seed.sql
.vscode/
├── extensions.json
└── settings.json
```
- 接著跑 `supabase start` 就會啟動預設的 docker
```bash
jazzwang_tw@cloudshell:~/snippet/python/supubase-py$ supabase start

Started supabase local development setup.

         API URL: http://127.0.0.1:54321
     GraphQL URL: http://127.0.0.1:54321/graphql/v1
  S3 Storage URL: http://127.0.0.1:54321/storage/v1/s3
          DB URL: postgresql://postgres:postgres@127.0.0.1:54322/postgres
      Studio URL: http://127.0.0.1:54323
    Inbucket URL: http://127.0.0.1:54324
      JWT secret: super-secret-jwt-token-with-at-least-32-characters-long
        anon key: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZS1kZW1vIiwicm9sZSI6ImFub24iLCJleHAiOjE5ODM4MTI5OTZ9.CRXP1A7WOeoJeXxjNni43kdQwgnWNReilDMblYTn_I0
service_role key: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZS1kZW1vIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImV4cCI6MTk4MzgxMjk5Nn0.EGIM96RAZx35lJzdJsyH-qQwv8Hdp7fsn3W0YpN81IU
   S3 Access Key: 625729a08b95bf1b7ff351a663f3a23c
   S3 Secret Key: 850181e4652dd023b7a98c58ae0d2d34bd487ee0cc3254aed6eda37307425907
       S3 Region: local
```
- 取得 Google Cloud Shell 上跑 Supabase Studio Docker 的 URL
```
jazzwang_tw@cloudshell:~/snippet/python/supubase-py$ cloudshell get-web-preview-url -p54323
https://54323-cs-216321250341-default.cs-asia-east1-duck.cloudshell.dev
```
- 關閉範例 Supabase 範例容器
```bash
jazzwang_tw@cloudshell:~/snippet/python/supubase-py$ docker ps -a
CONTAINER ID   IMAGE                                             COMMAND                  CREATED          STATUS                    PORTS                                                        NAMES
929f5175375c   public.ecr.aws/supabase/studio:20240729-ce42139   "docker-entrypoint.s…"   27 seconds ago   Up 27 seconds (healthy)   0.0.0.0:54323->3000/tcp                                      supabase_studio_supubase-py
f16d7ba876b1   public.ecr.aws/supabase/postgres-meta:v0.83.2     "docker-entrypoint.s…"   27 seconds ago   Up 27 seconds (healthy)   8080/tcp                                                     supabase_pg_meta_supubase-py
9a877faba846   public.ecr.aws/supabase/edge-runtime:v1.56.1      "sh -c 'cat <<'EOF' …"   28 seconds ago   Up 27 seconds             8081/tcp                                                     supabase_edge_runtime_supubase-py
ce1edc9c7036   public.ecr.aws/supabase/imgproxy:v3.8.0           "imgproxy"               28 seconds ago   Up 28 seconds (healthy)   8080/tcp                                                     supabase_imgproxy_supubase-py
22af469602d0   public.ecr.aws/supabase/storage-api:v1.10.1       "docker-entrypoint.s…"   29 seconds ago   Up 28 seconds (healthy)   5000/tcp                                                     supabase_storage_supubase-py
05810d7a5c0c   public.ecr.aws/supabase/postgrest:v12.2.0         "/bin/postgrest"         29 seconds ago   Up 29 seconds             3000/tcp                                                     supabase_rest_supubase-py
1ec9f56af0e1   public.ecr.aws/supabase/realtime:v2.30.23         "/usr/bin/tini -s -g…"   30 seconds ago   Up 29 seconds (healthy)   4000/tcp                                                     supabase_realtime_supubase-py
238969f9e16a   public.ecr.aws/supabase/inbucket:3.0.3            "/start-inbucket.sh …"   30 seconds ago   Up 29 seconds (healthy)   1100/tcp, 2500/tcp, 0.0.0.0:54324->9000/tcp                  supabase_inbucket_supubase-py
01a9fdde27a9   public.ecr.aws/supabase/gotrue:v2.158.1           "auth"                   30 seconds ago   Up 30 seconds (healthy)   9999/tcp                                                     supabase_auth_supubase-py
817f84620f6b   public.ecr.aws/supabase/kong:2.8.1                "sh -c 'cat <<'EOF' …"   31 seconds ago   Up 30 seconds (healthy)   8001/tcp, 8088/tcp, 8443-8444/tcp, 0.0.0.0:54321->8000/tcp   supabase_kong_supubase-py
ec09641e341c   public.ecr.aws/supabase/vector:0.28.1-alpine      "sh -c 'cat <<'EOF' …"   31 seconds ago   Up 31 seconds (healthy)                                                                supabase_vector_supubase-py
3237f0a0c835   public.ecr.aws/supabase/logflare:1.4.0            "sh -c 'cat <<'EOF' …"   31 seconds ago   Up 31 seconds (healthy)   0.0.0.0:54327->4000/tcp                                      supabase_analytics_supubase-py
9a140a4db6c8   public.ecr.aws/supabase/postgres:15.1.1.78        "sh -c 'cat <<'EOF' …"   43 seconds ago   Up 42 seconds (healthy)   0.0.0.0:54322->5432/tcp                                      supabase_db_supubase-p
jazzwang_tw@cloudshell:~/snippet/python/supubase-py$ supabase stop
Stopped supabase local development setup.
Local data are backed up to docker volume. Use docker to show them: docker volume ls --filter label=com.supabase.cli.project=supubase-py
```