# Track 2 - Codelabs 2
## MCP Toolbox for Databases: Making BigQuery datasets available to MCP clients

- MCP Toolbox for Databases: Making BigQuery datasets available to MCP clients
- https://codelabs.developers.google.com/mcp-toolbox-bigquery-dataset?hl=zh-tw#1
- ( 2026-03-29 18:58:31 )
- 打開 http://shell.cloud.google.com/?show=terminal
```bash
Welcome to Cloud Shell! Type "help" to get started, or type "gemini" to try prompting with Gemini CLI.
To set your Cloud Platform project in this session use `gcloud config set project [PROJECT_ID]`.
You can view your projects by running `gcloud projects list`.
jazzwang_tw@cloudshell:~$ #### --------------
jazzwang_tw@cloudshell:~$ #### --------------
jazzwang_tw@cloudshell:~$ gcloud config list project
[core]
project (unset)

Your active configuration is: [cloudshell-18156]
jazzwang_tw@cloudshell:~$ #### --------------
jazzwang_tw@cloudshell:~$ #### --------------
jazzwang_tw@cloudshell:~$ gcloud config set project jazz-adk-labs
Updated property [core/project].
jazzwang_tw@cloudshell:~$ #### --------------
jazzwang_tw@cloudshell:~$ #### --------------
jazzwang_tw@cloudshell:~ (jazz-adk-labs)$ gcloud services enable cloudresourcemanager.googleapis.com \
                       servicenetworking.googleapis.com \
                       run.googleapis.com \
                       cloudbuild.googleapis.com \
                       cloudfunctions.googleapis.com \
                       aiplatform.googleapis.com \
                       sqladmin.googleapis.com \
                       compute.googleapis.com 
Operation "operations/acf.p2-1078995358955-2184f752-0b10-4536-82de-cc73382e2082" finished successfully.
jazzwang_tw@cloudshell:~ (jazz-adk-labs)$ #### --------------
jazzwang_tw@cloudshell:~ (jazz-adk-labs)$ #### --------------
jazzwang_tw@cloudshell:~ (jazz-adk-labs)$ mkdir mcp-toolbox
jazzwang_tw@cloudshell:~ (jazz-adk-labs)$ cd mcp-toolbox
jazzwang_tw@cloudshell:~/mcp-toolbox (jazz-adk-labs)$ export VERSION=0.23.0
jazzwang_tw@cloudshell:~/mcp-toolbox (jazz-adk-labs)$ curl -O https://storage.googleapis.com/genai-toolbox/v$VERSION/linux/amd64/toolbox
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  159M  100  159M    0     0  23.4M      0  0:00:06  0:00:06 --:--:-- 31.2M
jazzwang_tw@cloudshell:~/mcp-toolbox (jazz-adk-labs)$ chmod +x toolbox
jazzwang_tw@cloudshell:~/mcp-toolbox (jazz-adk-labs)$ #### --------------
jazzwang_tw@cloudshell:~/mcp-toolbox (jazz-adk-labs)$ #### --------------
jazzwang_tw@cloudshell:~/mcp-toolbox (jazz-adk-labs)$ cloudshell edit tools.yaml
jazzwang_tw@cloudshell:~/mcp-toolbox (jazz-adk-labs)$ cat tools.yaml 
sources:
 my-bq-source:
   kind: bigquery
   project: YOUR_PROJECT_ID

tools:
 search_release_notes_bq:
   kind: bigquery-sql
   source: my-bq-source
   statement: |
    SELECT
     product_name,description,published_at
    FROM
      `bigquery-public-data`.`google_cloud_release_notes`.`release_notes`
    WHERE
     DATE(published_at) >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
    GROUP BY product_name,description,published_at
    ORDER BY published_at DESC
   description: |
    Use this tool to get information on Google Cloud Release Notes.

toolsets:
 my_bq_toolset:
jazzwang_tw@cloudshell:~/mcp-toolbox (jazz-adk-labs)$ #### --------------
jazzwang_tw@cloudshell:~/mcp-toolbox (jazz-adk-labs)$ #### --------------
jazzwang_tw@cloudshell:~/mcp-toolbox (jazz-adk-labs)$ ./toolbox --tools-file="tools.yaml"
2026-03-29T11:10:35.476004835Z INFO "Initialized 1 sources: my-bq-source" 
2026-03-29T11:10:35.476119935Z INFO "Initialized 0 authServices: " 
2026-03-29T11:10:35.476172384Z INFO "Initialized 1 tools: search_release_notes_bq" 
2026-03-29T11:10:35.476213384Z INFO "Initialized 2 toolsets: my_bq_toolset, default" 
2026-03-29T11:10:35.476225355Z INFO "Initialized 0 prompts: " 
2026-03-29T11:10:35.476239124Z INFO "Initialized 1 promptsets: default" 
2026-03-29T11:10:35.476273555Z WARN "wildcard (`*`) allows all origin to access the resource and is not secure. Use it with cautious for public, non-sensitive data, or during local development. Recommended to use `--allowed-origins` flag to prevent DNS rebinding attacks" 
2026-03-29T11:10:35.480521953Z INFO "Server ready to serve!" 
```
- 使用Cloud Shell 的「網頁預覽」，
  - https://5000-cs-216321250341-default.cs-asia-east1-cats.cloudshell.dev
  - 顯示
  ```
  🧰 Hello, World! 🧰
  ```
- 在網址後面加上 `/api/toolset`
  - https://5000-cs-216321250341-default.cs-asia-east1-cats.cloudshell.dev/api/toolset
  - 看到結果是
  ```json
  {
    "serverVersion": "0.23.0+binary.linux.amd64.466aef0",
    "tools": {
        "search_release_notes_bq": {
        "description": "Use this tool to get information on Google Cloud Release Notes.\n",
        "parameters": [],
        "authRequired": []
        }
    }
  }
  ```
- 按 CTRL+C 終止
- 測試 MCP Toolbox 的 UI 界面
```bash
^C2026-03-29T11:18:02.638016251Z WARN "Shutting down gracefully..." 
jazzwang_tw@cloudshell:~/mcp-toolbox (jazz-adk-labs)$ 
jazzwang_tw@cloudshell:~/mcp-toolbox (jazz-adk-labs)$ 
jazzwang_tw@cloudshell:~/mcp-toolbox (jazz-adk-labs)$ ./toolbox --tools-file "tools.yaml" --ui
2026-03-29T11:18:21.456598071Z INFO "Initialized 1 sources: my-bq-source" 
2026-03-29T11:18:21.456667081Z INFO "Initialized 0 authServices: " 
2026-03-29T11:18:21.456693341Z INFO "Initialized 1 tools: search_release_notes_bq" 
2026-03-29T11:18:21.456732021Z INFO "Initialized 2 toolsets: my_bq_toolset, default" 
2026-03-29T11:18:21.456754791Z INFO "Initialized 0 prompts: " 
2026-03-29T11:18:21.456768631Z INFO "Initialized 1 promptsets: default" 
2026-03-29T11:18:21.456802611Z WARN "wildcard (`*`) allows all origin to access the resource and is not secure. Use it with cautious for public, non-sensitive data, or during local development. Recommended to use `--allowed-origins` flag to prevent DNS rebinding attacks" 
2026-03-29T11:18:21.460929899Z INFO "Server ready to serve!" 
2026-03-29T11:18:21.460960799Z INFO "Toolbox UI is up and running at: http://127.0.0.1:5000/ui" 
2026-03-29T11:18:34.899517422Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/?authuser=0" method: "GET" path: "/" remoteIP: "127.0.0.1:43632" proto: "HTTP/1.1" requestID: "cs-216321250341-default/pIiGepQbp2-000001"} httpResponse: {status: 200 bytes: 23 elapsed: 0.017560} 
2026-03-29T11:18:41.717695847Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui" method: "GET" path: "/ui" remoteIP: "127.0.0.1:43632" proto: "HTTP/1.1" requestID: "cs-216321250341-default/pIiGepQbp2-000002"} httpResponse: {status: 200 bytes: 1742 elapsed: 2.633189} 
2026-03-29T11:18:41.830942029Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/css/style.css" method: "GET" path: "/ui/css/style.css" remoteIP: "127.0.0.1:43632" proto: "HTTP/1.1" requestID: "cs-216321250341-default/pIiGepQbp2-000003"} httpResponse: {status: 200 bytes: 29184 elapsed: 0.230199} 
2026-03-29T11:18:41.900302002Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/js/navbar.js" method: "GET" path: "/ui/js/navbar.js" remoteIP: "127.0.0.1:43632" proto: "HTTP/1.1" requestID: "cs-216321250341-default/pIiGepQbp2-000004"} httpResponse: {status: 200 bytes: 4426 elapsed: 0.068649} 
2026-03-29T11:18:41.914997976Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/js/mainContent.js" method: "GET" path: "/ui/js/mainContent.js" remoteIP: "127.0.0.1:43632" proto: "HTTP/1.1" requestID: "cs-216321250341-default/pIiGepQbp2-000005"} httpResponse: {status: 200 bytes: 7712 elapsed: 0.070690} 
2026-03-29T11:18:41.950816548Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/assets/mcptoolboxlogo.png" method: "GET" path: "/ui/assets/mcptoolboxlogo.png" remoteIP: "127.0.0.1:43632" proto: "HTTP/1.1" requestID: "cs-216321250341-default/pIiGepQbp2-000006"} httpResponse: {status: 200 bytes: 117020 elapsed: 0.251089} 
```
- 在 https://5000-cs-216321250341-default.cs-asia-east1-cats.cloudshell.dev/ui/tools 按下「Run Tools」，結果顯示：
```json
Error: HTTP error 400: {"status":"Bad Request","error":"error while invoking tool: query validation failed: failed to insert dry run job: googleapi: Error 400: ProjectId must be non-empty, badRequest"}
```
- 改按「Edit Headers」，下方有「How to extract Google OAuth ID Token manually」
- Go to the Google OAuth Playground site: 
  - https://developers.google.com/oauthplayground/
- 以下這段說明，暫時還沒搞懂該按哪裡：

To obtain a Google OAuth ID token using a standard account:

1.  Make sure you are on your intended standard account. Verify by running the command below.
    ```
    gcloud auth list
    ```

2.  Within your Cloud Console, add the following link to the "Authorized Redirect URIs".
```
https://developers.google.com/oauthplayground
```
4.  Go to the Google OAuth Playground site: <https://developers.google.com/oauthplayground/>
5.  In the top right settings menu, select "Use your own OAuth Credentials".
6.  Input your clientID (from tools file), along with the client secret from Cloud Console.
7.  Inside the Google OAuth Playground, select "Google OAuth2 API v2.

    -   Select "Authorize APIs".
    -   Select "Exchange Authorization codes for tokens"
    -   Copy the id\_token field provided in the response.

9.  Paste this token into the header in JSON editor. The key should be the name of your auth service followed by `_token`
    ```
    {
      "Content-Type": "application/json",
      "my-google-auth_token": "YOUR_ID_TOKEN_HERE"
    }
    ```

This token is typically short-lived.

- 按 CTRL+C 終止 MCP Toolbox
- 繼續實作 ADK 的部份
```
^C2026-03-29T11:24:05.841965727Z WARN "Shutting down gracefully..." 
jazzwang_tw@cloudshell:~/mcp-toolbox (jazz-adk-labs)$ cd
jazzwang_tw@cloudshell:~ (jazz-adk-labs)$ mkdir my-agents && cd my-agents
jazzwang_tw@cloudshell:~/my-agents (jazz-adk-labs)$ uv venv
Using CPython 3.12.3 interpreter at: /usr/bin/python
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate
jazzwang_tw@cloudshell:~/my-agents (jazz-adk-labs)$ source .venv/bin/activate
(my-agents) jazzwang_tw@cloudshell:~/my-agents (jazz-adk-labs)$ uv pip install google-adk toolbox-core
Resolved 120 packages in 2.12s
Prepared 5 packages in 14.04s
Installed 120 packages in 2.73s
 + aiohappyeyeballs==2.6.1
 + aiohttp==3.13.4
 + aiosignal==1.4.0
 + aiosqlite==0.22.1
 + alembic==1.18.4
 + annotated-doc==0.0.4
 + annotated-types==0.7.0
 + anyio==4.13.0
 + attrs==26.1.0
 + authlib==1.6.9
 + certifi==2026.2.25
 + cffi==2.0.0
 + charset-normalizer==3.4.6
 + click==8.3.1
 + cloudpickle==3.1.2
 + cryptography==46.0.6
 + deprecated==1.3.1
 + distro==1.9.0
 + docstring-parser==0.17.0
 + fastapi==0.135.2
 + frozenlist==1.8.0
 + google-adk==1.28.0
 + google-api-core==2.30.0
 + google-api-python-client==2.193.0
 + google-auth==2.49.1
 + google-auth-httplib2==0.3.0
 + google-cloud-aiplatform==1.143.0
 + google-cloud-appengine-logging==1.8.0
 + google-cloud-audit-log==0.4.0
 + google-cloud-bigquery==3.40.1
 + google-cloud-bigquery-storage==2.36.2
 + google-cloud-bigtable==2.35.0
 + google-cloud-core==2.5.0
 + google-cloud-dataplex==2.17.0
 + google-cloud-discoveryengine==0.13.12
 + google-cloud-iam==2.21.0
 + google-cloud-logging==3.15.0
 + google-cloud-monitoring==2.30.0
 + google-cloud-pubsub==2.36.0
 + google-cloud-resource-manager==1.17.0
 + google-cloud-secret-manager==2.27.0
 + google-cloud-spanner==3.63.0
 + google-cloud-speech==2.38.0
 + google-cloud-storage==3.10.1
 + google-cloud-trace==1.19.0
 + google-crc32c==1.8.0
 + google-genai==1.69.0
 + google-resumable-media==2.8.0
 + googleapis-common-protos==1.73.1
 + graphviz==0.21
 + greenlet==3.3.2
 + grpc-google-iam-v1==0.14.3
 + grpc-interceptor==0.15.4
 + grpcio==1.78.0
 + grpcio-status==1.78.0
 + h11==0.16.0
 + httpcore==1.0.9
 + httplib2==0.31.2
 + httpx==0.28.1
 + httpx-sse==0.4.3
 + idna==3.11
 + importlib-metadata==8.7.1
 + jsonschema==4.26.0
 + jsonschema-specifications==2025.9.1
 + mako==1.3.10
 + markupsafe==3.0.3
 + mcp==1.26.0
 + mmh3==5.2.1
 + multidict==6.7.1
 + opentelemetry-api==1.38.0
 + opentelemetry-exporter-gcp-logging==1.11.0a0
 + opentelemetry-exporter-gcp-monitoring==1.11.0a0
 + opentelemetry-exporter-gcp-trace==1.11.0
 + opentelemetry-exporter-otlp-proto-common==1.38.0
 + opentelemetry-exporter-otlp-proto-http==1.38.0
 + opentelemetry-proto==1.38.0
 + opentelemetry-resourcedetector-gcp==1.11.0a0
 + opentelemetry-sdk==1.38.0
 + opentelemetry-semantic-conventions==0.59b0
 + packaging==26.0
 + propcache==0.4.1
 + proto-plus==1.27.2
 + protobuf==6.33.6
 + pyarrow==23.0.1
 + pyasn1==0.6.3
 + pyasn1-modules==0.4.2
 + pycparser==3.0
 + pydantic==2.12.5
 + pydantic-core==2.41.5
 + pydantic-settings==2.13.1
 + pyjwt==2.12.1
 + pyopenssl==26.0.0
 + pyparsing==3.3.2
 + python-dateutil==2.9.0.post0
 + python-dotenv==1.2.2
 + python-multipart==0.0.22
 + pyyaml==6.0.3
 + referencing==0.37.0
 + requests==2.33.0
 + rpds-py==0.30.0
 + six==1.17.0
 + sniffio==1.3.1
 + sqlalchemy==2.0.48
 + sqlalchemy-spanner==1.17.3
 + sqlparse==0.5.5
 + sse-starlette==3.3.4
 + starlette==0.52.1
 + tenacity==9.1.4
 + toolbox-core==1.0.0
 + typing-extensions==4.15.0
 + typing-inspection==0.4.2
 + tzlocal==5.3.1
 + uritemplate==4.2.0
 + urllib3==2.6.3
 + uvicorn==0.42.0
 + watchdog==6.0.0
 + websockets==15.0.1
 + wrapt==2.1.2
 + yarl==1.23.0
 + zipp==3.23.0
(my-agents) jazzwang_tw@cloudshell:~/my-agents (jazz-adk-labs)$ #### --------------
(my-agents) jazzwang_tw@cloudshell:~/my-agents (jazz-adk-labs)$ #### --------------
(my-agents) jazzwang_tw@cloudshell:~/my-agents (jazz-adk-labs)$ adk
Usage: adk [OPTIONS] COMMAND [ARGS]...

  Agent Development Kit CLI tools.

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  api_server   Starts a FastAPI server for agents.
  conformance  Conformance testing tools for ADK.
  create       Creates a new app in the current folder with prepopulated agent template.
  deploy       Deploys agent to hosted environments.
  eval         Evaluates an agent given the eval sets.
  eval_set     Manage Eval Sets.
  migrate      ADK migration commands.
  optimize     Optimizes the root agent instructions using the GEPA optimizer.
  run          Runs an interactive CLI for a certain agent.
  web          Starts a FastAPI server with Web UI for agents.

(my-agents) jazzwang_tw@cloudshell:~/my-agents (jazz-adk-labs)$ #### --------------
(my-agents) jazzwang_tw@cloudshell:~/my-agents (jazz-adk-labs)$ #### --------------
(my-agents) jazzwang_tw@cloudshell:~/my-agents (jazz-adk-labs)$ adk create gcp_releasenotes_agent_app
Choose a model for the root agent:
1. gemini-2.5-flash
2. Other models (fill later)
Choose model (1, 2): 1
1. Google AI
2. Vertex AI
Choose a backend (1, 2): 2

You need an existing Google Cloud account and project, check out this link for details:
https://google.github.io/adk-docs/get-started/quickstart/#gemini---google-cloud-vertex-ai

Enter Google Cloud project ID [jazz-adk-labs]: 
Enter Google Cloud region [us-central1]: 

Agent created in /home/jazzwang_tw/my-agents/gcp_releasenotes_agent_app:
- .env
- __init__.py
- agent.py

(my-agents) jazzwang_tw@cloudshell:~/my-agents (jazz-adk-labs)$ #### --------------
(my-agents) jazzwang_tw@cloudshell:~/my-agents (jazz-adk-labs)$ #### --------------
(my-agents) jazzwang_tw@cloudshell:~/my-agents (jazz-adk-labs)$ cloudshell edit gcp_releasenotes_agent_app/agent.py 
```
- 貼上範例程式碼
```bash
(my-agents) jazzwang_tw@cloudshell:~/my-agents (jazz-adk-labs)$ cat gcp_releasenotes_agent_app/agent.py 
from google.adk.agents import Agent
from toolbox_core import ToolboxSyncClient

toolbox = ToolboxSyncClient("http://127.0.0.1:5000")

# Load all the tools
tools = toolbox.load_toolset('my_bq_toolset')

root_agent = Agent(
    name="gcp_releasenotes_agent",
    model="gemini-2.5-flash",
    description=(
        "Agent to answer questions about Google Cloud Release notes."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the Google Cloud Release notes. Use the tools to answer the question"
    ),
    tools=tools,
)

(my-agents) jazzwang_tw@cloudshell:~/my-agents (jazz-adk-labs)$ 
```
- 開另一個終端機視窗：
```bash
Welcome to Cloud Shell! Type "help" to get started, or type "gemini" to try prompting with Gemini CLI.
To set your Cloud Platform project in this session use `gcloud config set project [PROJECT_ID]`.
You can view your projects by running `gcloud projects list`.
jazzwang_tw@cloudshell:~$ 
jazzwang_tw@cloudshell:~$ 
jazzwang_tw@cloudshell:~$ gcloud config set project jazz-adk-labs
Updated property [core/project].
jazzwang_tw@cloudshell:~ (jazz-adk-labs)$ cd mcp-toolbox/
jazzwang_tw@cloudshell:~$ 
jazzwang_tw@cloudshell:~$ 
jazzwang_tw@cloudshell:~/mcp-toolbox (jazz-adk-labs)$ cat tools.yaml 
sources:
 my-bq-source:
   kind: bigquery
   project: jazz-adk-labs

tools:
 search_release_notes_bq:
   kind: bigquery-sql
   source: my-bq-source
   statement: |
    SELECT
     product_name,description,published_at
    FROM
      `bigquery-public-data`.`google_cloud_release_notes`.`release_notes`
    WHERE
     DATE(published_at) >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
    GROUP BY product_name,description,published_at
    ORDER BY published_at DESC
   description: |
    Use this tool to get information on Google Cloud Release Notes.

toolsets:
 my_bq_toolset:
   - search_release_notes_bq


jazzwang_tw@cloudshell:~/mcp-toolbox (jazz-adk-labs)$ 
```
- 把 `YOUR_PROJECT_ID` 換成 `jazz-adk-labs` (設定的 Google Cloud Project ID)
- 執行 `./toolbox --tools-file="tools.yaml"`
```bash
jazzwang_tw@cloudshell:~/mcp-toolbox (jazz-adk-labs)$ cat tools.yaml 
sources:
 my-bq-source:
   kind: bigquery
   project: jazz-adk-labs

tools:
 search_release_notes_bq:
   kind: bigquery-sql
   source: my-bq-source
   statement: |
    SELECT
     product_name,description,published_at
    FROM
      `bigquery-public-data`.`google_cloud_release_notes`.`release_notes`
    WHERE
     DATE(published_at) >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
    GROUP BY product_name,description,published_at
    ORDER BY published_at DESC
   description: |
    Use this tool to get information on Google Cloud Release Notes.

toolsets:
 my_bq_toolset:
   - search_release_notes_bq


jazzwang_tw@cloudshell:~/mcp-toolbox (jazz-adk-labs)$ ./toolbox --tools-file="tools.yaml"
2026-03-29T12:37:17.571177877Z INFO "Initialized 1 sources: my-bq-source" 
2026-03-29T12:37:17.571238207Z INFO "Initialized 0 authServices: " 
2026-03-29T12:37:17.571256847Z INFO "Initialized 1 tools: search_release_notes_bq" 
2026-03-29T12:37:17.571302687Z INFO "Initialized 2 toolsets: my_bq_toolset, default" 
2026-03-29T12:37:17.571325177Z INFO "Initialized 0 prompts: " 
2026-03-29T12:37:17.571339837Z INFO "Initialized 1 promptsets: default" 
2026-03-29T12:37:17.571362467Z WARN "wildcard (`*`) allows all origin to access the resource and is not secure. Use it with cautious for public, non-sensitive data, or during local development. Recommended to use `--allowed-origins` flag to prevent DNS rebinding attacks" 
2026-03-29T12:37:17.575386435Z INFO "Server ready to serve!"
```
- 開啟 https://5000-cs-216321250341-default.cs-asia-east1-cats.cloudshell.dev/ui/tools 按下 「Run Tools」，還是顯示不同的錯誤訊息
```json
Error: HTTP error 400: {"status":"Bad Request","error":"error while invoking tool: query validation failed: failed to insert dry run job: Post \"https://bigquery.googleapis.com/bigquery/v2/projects/jazz-adk-labs/jobs?alt=json\u0026prettyPrint=false\": oauth2/google: invalid token JSON from metadata: EOF"}
```
- 另一個終端機視窗執行 `adk run gcp_releasenotes_agent_app/`
```bash
(my-agents) jazzwang_tw@cloudshell:~/my-agents (jazz-adk-labs)$ adk run gcp_releasenotes_agent_app/
Log setup complete: /tmp/agents_log/agent.20260329_124840.log
To access latest log: tail -F /tmp/agents_log/agent.latest.log
/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/google/adk/cli/cli.py:204: UserWarning: [EXPERIMENTAL] InMemoryCredentialService: This feature is experimental and may change or be removed in future versions without notice. It may introduce breaking changes at any time.
  credential_service = InMemoryCredentialService()
/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/google/adk/auth/credential_service/in_memory_credential_service.py:33: UserWarning: [EXPERIMENTAL] BaseCredentialService: This feature is experimental and may change or be removed in future versions without notice. It may introduce breaking changes at any time.
  super().__init__()
Running agent gcp_releasenotes_agent, type exit to exit.
[user]: get me the google cloud release notes
Traceback (most recent call last):
  File "/home/jazzwang_tw/my-agents/.venv/bin/adk", line 10, in <module>
    sys.exit(main())
             ^^^^^^
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/click/core.py", line 1485, in __call__
    return self.main(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/click/core.py", line 1406, in main
    rv = self.invoke(ctx)
         ^^^^^^^^^^^^^^^^
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/click/core.py", line 1873, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/click/core.py", line 1269, in invoke
    return ctx.invoke(self.callback, **ctx.params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/click/core.py", line 824, in invoke
    return callback(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/google/adk/cli/cli_tools_click.py", line 127, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/google/adk/cli/cli_tools_click.py", line 598, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/google/adk/cli/cli_tools_click.py", line 680, in cli_run
    asyncio.run(
  File "/usr/lib/python3.12/asyncio/runners.py", line 194, in run
    return runner.run(main)
           ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/asyncio/runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/asyncio/base_events.py", line 687, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/google/adk/cli/cli.py", line 259, in run_cli
    await run_interactively(
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/google/adk/cli/cli.py", line 129, in run_interactively
    async for event in agen:
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/google/adk/runners.py", line 632, in run_async
    async for event in agen:
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/google/adk/runners.py", line 617, in _run_with_trace
    async for event in agen:
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/google/adk/runners.py", line 853, in _exec_with_plugin
    async for event in agen:
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/google/adk/runners.py", line 606, in execute
    async for event in agen:
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/google/adk/agents/base_agent.py", line 297, in run_async
    async for event in agen:
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/google/adk/agents/llm_agent.py", line 479, in _run_async_impl
    async for event in agen:
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/google/adk/flows/llm_flows/base_llm_flow.py", line 754, in run_async
    async for event in agen:
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/google/adk/flows/llm_flows/base_llm_flow.py", line 831, in _run_one_step_async
    async for llm_response in agen:
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/google/adk/flows/llm_flows/base_llm_flow.py", line 1188, in _call_llm_async
    async for event in agen:
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/google/adk/flows/llm_flows/base_llm_flow.py", line 1171, in _call_llm_with_tracing
    async for llm_response in agen:
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/google/adk/flows/llm_flows/base_llm_flow.py", line 1247, in _run_and_handle_error
    async for response in agen:
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/google/adk/flows/llm_flows/base_llm_flow.py", line 391, in _run_and_handle_error
    raise model_error
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/google/adk/flows/llm_flows/base_llm_flow.py", line 372, in _run_and_handle_error
    async for llm_response in agen:
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/google/adk/models/google_llm.py", line 245, in generate_content_async
    response = await self.api_client.aio.models.generate_content(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/google/genai/models.py", line 7875, in generate_content
    return await self._generate_content(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/google/genai/models.py", line 6642, in _generate_content
    response = await self._api_client.async_request(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/google/genai/_api_client.py", line 1578, in async_request
    result = await self._async_request(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/google/genai/_api_client.py", line 1511, in _async_request
    return await self._async_retry(  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/tenacity/asyncio/__init__.py", line 112, in __call__
    do = await self.iter(retry_state=retry_state)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/tenacity/asyncio/__init__.py", line 157, in iter
    result = await action(retry_state)
             ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/tenacity/_utils.py", line 111, in inner
    return call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/tenacity/__init__.py", line 413, in exc_check
    raise retry_exc.reraise()
          ^^^^^^^^^^^^^^^^^^^
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/tenacity/__init__.py", line 184, in reraise
    raise self.last_attempt.result()
          ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/concurrent/futures/_base.py", line 449, in result
    return self.__get_result()
           ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/concurrent/futures/_base.py", line 401, in __get_result
    raise self._exception
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/tenacity/asyncio/__init__.py", line 116, in __call__
    result = await fn(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/google/genai/_api_client.py", line 1337, in _async_request_once
    f'Bearer {await self._async_access_token()}'
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/google/genai/_api_client.py", line 1134, in _async_access_token
    return await async_get_token_from_credentials(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/google/genai/_api_client.py", line 2147, in async_get_token_from_credentials
    await asyncio.to_thread(refresh_auth, credentials)
  File "/usr/lib/python3.12/asyncio/threads.py", line 25, in to_thread
    return await loop.run_in_executor(None, func_call)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/concurrent/futures/thread.py", line 58, in run
    result = self.fn(*self.args, **self.kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/google/genai/_api_client.py", line 207, in refresh_auth
    credentials.refresh(Request())  # type: ignore[no-untyped-call]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/google/auth/credentials.py", line 367, in refresh
    self._perform_refresh_token(request)
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/google/auth/compute_engine/credentials.py", line 139, in _perform_refresh_token
    self._retrieve_info(request)
  File "/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/google/auth/compute_engine/credentials.py", line 112, in _retrieve_info
    raise exceptions.RefreshError(
google.auth.exceptions.RefreshError: Unexpected response from metadata server: service account info is missing 'email' field.
```
- 看起來應該是 IAM 權限設定造成的問題。
- ( 2026-03-29 23:02:20 )
- 後來在查 https://googleapis.github.io/genai-toolbox/resources/sources/bigquery/ 時，發現 `tools.yaml` 寫錯，稍微重新做過 YAML 縮排以後，並且修正 `project: jazz-adk-labsps ax` 應該是 `project: jazz-adk-labs` ，可以正確執行 `Run Tools` 並取得 BigQuery 裡的 Release Note
```json
[
  {
    "description": "<p>The following issues were fixed in 1.33.600-gke.40:</p>\n\n<ul>\n<li>Fixed an issue where if updates or upgrades to advanced admin clusters failed and the external bootstrap cluster was deleted, you could lose critical data.</li>\n</ul>",
    "product_name": "Google Distributed Cloud (software only) for VMware",
    "published_at": "2026-03-27"
  },
  {
    "description": "<p>Google Distributed Cloud (software only) for bare metal 1.32.1000-gke.57 is now available for\ndownload. To upgrade, see <a href=\"how-to/upgrade\">Upgrade clusters</a>.\nGoogle Distributed Cloud for bare metal\n1.32.1000-gke.57 runs on Kubernetes v1.32.13-gke.1000.</p>\n\n<p>After a release, it takes approximately 7 to 14 days for the version to become\navailable for installations or upgrades with the GKE On-Prem API clients: the\nGoogle Cloud console, the gcloud CLI, and Terraform.</p>\n\n<p>If you use a third-party storage vendor, check the Google Distributed Cloud-ready\nstorage partners document to make sure the storage vendor has already passed the\nqualification for this release of Google Distributed Cloud for bare metal.",
    "product_name": "Google Distributed Cloud (software only) for bare metal",
    "published_at": "2026-03-27"
  },
  {
    "description": "<p>Google Distributed Cloud (software only) for VMware 1.33.600-gke.40 is now available\nfor download. To upgrade, see <a href=\"https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading.md\">Upgrade clusters</a>.\nGoogle Distributed Cloud 1.33.600-gke.40 runs on Kubernetes 1.33.5-gke.2200.</p>\n\n<p>If you are using a third-party storage vendor, check the Google Distributed Cloud-ready\nstorage partners document to make sure the storage vendor has already passed the\nqualification for this release.</p>\n\n<p>After a release, it takes approximately 7 to 14 days for the version to become\navailable for use with GKE On-Prem API clients: the Google Cloud console, the\ngcloud CLI, and Terraform.</p>",
    "product_name": "Google Distributed Cloud (software only) for VMware",
    "published_at": "2026-03-27"
  },
  {
    "description": "<p>Google Distributed Cloud (software only) for VMware 1.32.1000-gke.57 is now available\nfor download. To upgrade, see <a href=\"https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading.md\">Upgrade clusters</a>.\nGoogle Distributed Cloud 1.32.1000-gke.57 runs on Kubernetes v1.32.13-gke.1000.</p>\n\n<p>If you are using a third-party storage vendor, check the Google Distributed Cloud-ready\nstorage partners document to make sure the storage vendor has already passed the\nqualification for this release.</p>\n\n<p>After a release, it takes approximately 7 to 14 days for the version to become\navailable for use with GKE On-Prem API clients: the Google Cloud console, the\ngcloud CLI, and Terraform.</p>",
    "product_name": "Google Distributed Cloud (software only) for VMware",
    "published_at": "2026-03-27"
  },
  {
    "description": "<p>Risk Engine has launched enhanced heuristics to help identify default\nhigh-value resources.</p>\n\n<p>If you are using the default high-value resource set, you might observe changes in the\nexposure scores of their findings, resources, and issues. For information about\nthese changes, see <a href=\"https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#default-high-value-resource-set\">Default high-value resource set</a>.</p>",
    "product_name": "Security Command Center",
    "published_at": "2026-03-27"
  },
  {
    "description": "<p>Cloud Composer 2 environments can no longer be created in\nMelbourne (australia-southeast2). We&#39;re switching this region to\nsupporting only Cloud Composer 3 environments. Existing Cloud Composer 2\nenvironments in this region aren&#39;t affected by this change.</p>",
    "product_name": "Cloud Composer",
    "published_at": "2026-03-27"
  },
  {
    "description": "<p>A vulnerability (CVE-2026-23268) about CrackArmor was discovered and has been addressed.\nFor more information, see the <a href=\"https://docs.cloud.google.com/compute/docs/security-bulletins#gcp-2026-015\">GCP-2026-015 security bulletin</a>.",
    "product_name": "Compute Engine",
    "published_at": "2026-03-27"
  },
  {
    "description": "<p>The following issues were fixed in 1.32.1000-gke.57:</p>\n\n<ul>\n<li>Fixed an issue where the node-problem-detector was incorrectly deployed onto\nnon-Advanced (V1) VMware clusters, causing the containerd runtime to\ncontinuously restart on affected nodes, leading to ETCD/CRI failures and\nunsuccessful cluster upgrades.\n</li>\n<li>Fixed an issue where setting the deprecated stackdriver.enableVPC field to\ntrue in a cluster configuration file would block upgrades to an Advanced\nCluster. The stackdriver.enableVPC field has been deprecated and its setting is\nnow ignored during the upgrade validation process.\n</li>\n<li>Fixes an issue where Advanced Clusters incorrectly deployed the node problem\ndetector onto non-Advanced clusters, which caused containerd to continuously\nrestart and led to cluster upgrade failures.\n</li>\n<li>Fixed an issue where the system certificate pool was ignored when a custom CA\ncertificate was configured for a registry mirror.\n</li>\n<li>Fixed an issue where retrying the <code>gkectl upgrade admin</code> command after a\nprevious failure could fail with &quot;AlreadyExists&quot; errors in the bootstrap cluster.\n</li>\n<li>Fixed an issue where cluster creation or upgrade failed if the proxy or\nnoProxy configuration fields contained extraneous whitespaces. These spaces\ninterfered with internal command-line argument parsing, causing the control\nplane load balancer initialization to fail.\n</li>\n<li>Fixed an issue where if updates or upgrades to advanced admin clusters failed\nand the external bootstrap cluster was deleted, you could lose critical data.</li>\n</ul>",
    "product_name": "Google Distributed Cloud (software only) for VMware",
    "published_at": "2026-03-27"
  },
  {
    "description": "<p><a href=\"https://docs.cloud.google.com/document-ai/docs/custom-splitter\">Custom splitter</a> model\n<code>pretrained-splitter-v1.5-2025-07-14</code> is available in\n<a href=\"https://cloud.google.com/products/#product-launch-stages\">General Availability (GA)</a>.</p>",
    "product_name": "Document AI",
    "published_at": "2026-03-27"
  },
  {
    "description": "<p>The following issues were fixed in 1.32.1000-gke.57:</p>\n\n<ul>\n<li>Fixed vulnerabilities listed in <a href=\"https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history\">Vulnerability fixes</a>.</li>\n<li>Cluster and\nnode pool failures are now surfaced in the <code>RecentFailures</code> field\nin the cluster status. This change provides a centralized location for viewing\nerrors from both worker node pools and control plane nodes, improving the\ntroubleshooting and debugging experience.\n</li>\n<li>Fixed an issue where Metrics API operations—including\n<code>kubectl top</code>, Horizontal Pod Autoscaling (HPA), and Vertical Pod Autoscaling\n(VPA)—could fail with TLS verification errors during CA rotation.\n</li>\n<li>Resolved an issue where Certificate Authority (CA) rotation became stuck\non self-managed clusters (admin, hybrid, or standalone). This fix resolves an\ninternal resource synchronization error that previously prevented the rotation\nprocess from completing successfully.\n</li>\n</ul>",
    "product_name": "Google Distributed Cloud (software only) for bare metal",
    "published_at": "2026-03-27"
  },
  {
    "description": "<p><strong>Vertex AI Search: Gemini 3 Pro (Preview) for answer generation discontinued</strong></p>\n\n<p>The Gemini 3 Pro (Preview) model has been discontinued and is no longer\navailable for answer generation. If you have been using that model, upgrade to\nthe Gemini 3.1 Pro (Preview) model.</p>\n\n<p>For information about available models, see <a href=\"https://docs.cloud.google.com/generative-ai-app-builder/docs/answer-generation-models\">Answer generation model versions\nand lifecycle</a>.</p>",
    "product_name": "Vertex AI Search",
    "published_at": "2026-03-26"
  },
  {
    "description": "<p>On March 26th, 2026, we released an updated version of Apigee (1-17-0-apigee-6).</p>\n<aside class=\"note\"><strong>Note:</strong><span> Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.",
    "product_name": "Apigee X",
    "published_at": "2026-03-26"
  },
  {
    "description": "<p>Upgraded bundled Helm version from v3.18.6 to <a href=\"https://github.com/helm/helm/releases/tag/v3.20.0\">v3.20.0</a> to pick up vulnerability fixes. To understand the changes in each release, review the <a href=\"https://github.com/helm/helm/releases\">changelogs</a>.</p>",
    "product_name": "Anthos Config Management",
    "published_at": "2026-03-26"
  },
  {
    "description": "<p>Addressed multiple Common Vulnerabilities and Exposures (CVEs) by updating dependencies.</p>",
    "product_name": "Anthos Config Management",
    "published_at": "2026-03-26"
  },
  {
    "description": "<table>\n<thead>\n<tr>\n<th>Bug ID</th>\n<th>Description</th>\n</tr>\n</thead>\n\n<tbody>\n<tr>\n<td><strong>495897297, 495909767</strong></td>\n<td><strong>Security fix for Apigee infrastructure.</strong> <p>This addresses the following vulnerabilities: <ul> <li><a href=\"https://nvd.nist.gov/vuln/detail/CVE-2026-33210\">CVE-2026-33210</a></li><li><a href=\"https://nvd.nist.gov/vuln/detail/CVE-2026-25679\">CVE-2026-25679</a></li><li><a href=\"https://nvd.nist.gov/vuln/detail/CVE-2026-27139\">CVE-2026-27139</a></li><li><a href=\"https://nvd.nist.gov/vuln/detail/CVE-2026-27142\">CVE-2026-27142</a></li><li><a href=\"https://nvd.nist.gov/vuln/detail/CVE-2026-33186\">2026-33186</a></li></ul></p></td>\n</tr>\n</tbody>\n</table>",
    "product_name": "Apigee X",
    "published_at": "2026-03-26"
  },
  {
    "description": "<table>\n<thead>\n<tr>\n<th>Bug ID</th>\n<th>Description</th>\n</tr>\n</thead>\n\n<tbody>\n<tr>\n<td><strong>N/A</strong></td>\n<td><strong>Updates to infrastructure and libraries.</strong></td>\n</tr>\n</tbody>\n</table>",
    "product_name": "Apigee X",
    "published_at": "2026-03-26"
  },
  {
    "description": "<p>Memorystore for Valkey supports version 1.0 of <a href=\"https://docs.cloud.google.com/memorystore/docs/valkey/about-bloom-filters\">Bloom filters</a> and <a href=\"https://docs.cloud.google.com/memorystore/docs/valkey/about-json\">JSON documents</a>. This feature is available in <a href=\"https://docs.cloud.google.com/products#product-launch-stages\">Preview</a>.</p>",
    "product_name": "Memorystore for Valkey",
    "published_at": "2026-03-26"
  },
  {
    "description": "<p>In addition to the <a href=\"https://docs.cloud.google.com/memorystore/docs/valkey/manage-in-transit-encryption\">per-instance CA mode</a>, Memorystore for Valkey offers the following new CA modes:</p>\n\n<ul>\n<li><a href=\"https://docs.cloud.google.com/memorystore/docs/valkey/use-shared-ca\"><strong>Shared CA</strong></a>: a managed,\nregionalized CA infrastructure. For each region, you can download a single CA\ncertificate bundle. This bundle is valid for all instances located in a region\nthat you configure to use the shared CA. Using a shared CA reduces the number of\ncertificates that clients need to manage. This CA mode is available in <a href=\"https://docs.cloud.google.com/products#product-launch-stages\">Preview</a>.</li>\n<li><a href=\"https://docs.cloud.google.com/memorystore/docs/valkey/use-customer-managed-ca\"><strong>Customer-managed CA</strong></a>:\nuse your own CA pool that&#39;s hosted on <a href=\"https://docs.cloud.google.com/certificate-authority-service/docs\">Certificate Authority Service</a>. If your client applications are configured to trust this CA, then your\napplications can connect to an instance without you having to download and\ninstall additional CA certificates. This gives you greater control and helps you\nmeet compliance requirements. This CA mode is available in <a href=\"https://docs.cloud.google.com/products#product-launch-stages\">Preview</a>.</li>\n</ul>",
    "product_name": "Memorystore for Valkey",
    "published_at": "2026-03-26"
  },
  {
    "description": "<p><a href=\"https://cloud.google.com/products#product-launch-stages\">General availability</a> support\nfor the following integration:</p>\n\n<ul>\n<li><a href=\"https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_oracle_database\">Oracle Database@Google Cloud</a></li>\n</ul>",
    "product_name": "VPC Service Controls",
    "published_at": "2026-03-26"
  },
  {
    "description": "<p>MySQL 8.0.44 is now the <a href=\"https://docs.cloud.google.com/sql/docs/mysql/db-versions#database-version-support\">default minor version</a> for Cloud SQL for MySQL 8.0.</p>\n\n<p>For more information about minor version support in Cloud SQL for MySQL, see\n<a href=\"https://docs.cloud.google.com/sql/docs/mysql/db-versions#mysql-8.0\">MySQL 8.0</a>.</p>",
    "product_name": "Cloud SQL for MySQL",
    "published_at": "2026-03-26"
  },
  {
    "description": "<p><strong>Gemini Enterprise: Chat with files in the Google Drive connector</strong></p>\n\n<p>Gemini Enterprise can analyze content and generate answers from CSV, PDF, PPTX,\nand XLSX files in the Google Drive connector, eliminating the need to upload\nthese files to the assistant.</p>\n\n<p>This feature is generally available (GA). For more information, see <a href=\"https://docs.cloud.google.com/gemini/enterprise/docs/assistant-chat#chat_with_files_in_connectors\">Chat with\nfiles in connectors</a>.</p>",
    "product_name": "Gemini Enterprise",
    "published_at": "2026-03-26"
  },
  {
    "description": "<p><strong>Vertex AI Search: Gemini 3.1 Pro and Gemini 3 Flash for answer generation (Preview)</strong></p>\n\n<p>You can generate answers with the Gemini 3.1 Pro (Preview) and Gemini 3 Flash (Preview)\nmodels.</p>\n\n<p>For more information, see <a href=\"https://docs.cloud.google.com/generative-ai-app-builder/docs/answer-generation-models\">Answer generation model versions and\nlifecycle</a>, <a href=\"https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/3-1-pro\">Gemini\n3.1 Pro</a>, and <a href=\"https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/3-flash\">Gemini 3\nFlash</a>.</p>",
    "product_name": "Vertex AI Search",
    "published_at": "2026-03-26"
  },
  {
    "description": "<p>You can use the\n<a href=\"https://docs.cloud.google.com/error-reporting/reference_mcp/mcp\">Error Reporting API MCP server</a>\nto let agents and AI applications interact with your error data.\nThis feature is in <a href=\"https://docs.cloud.google.com/products#product-launch-stages\">Preview</a>.",
    "product_name": "Error Reporting",
    "published_at": "2026-03-26"
  },
  {
    "description": "<p>You can now use\n<a href=\"https://docs.cloud.google.com/bigquery/docs/export-to-spanner#export_using_a_cloud_resource_connection\">Cloud resource connections with <code>EXPORT DATA</code> statements</a>\nto reverse ETL BigQuery data to Spanner. This\nfeature is\n<a href=\"https://cloud.google.com/products/#product-launch-stages\">generally available</a> (GA).</p>",
    "product_name": "BigQuery",
    "published_at": "2026-03-26"
  },
  {
    "description": "<p>As part of Looker 26.6, Conversational Analytics now offers <a href=\"https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data#ca-question-mode\">new modes for asking questions</a>. Fast mode allows you to get answers more quickly. Thinking mode allows you to ask more complex questions and test your agent&#39;s capabilities.</p>",
    "product_name": "Looker",
    "published_at": "2026-03-26"
  },
  {
    "description": "<p>As part of Looker 26.6, <a href=\"https://docs.cloud.google.com/looker/docs/conversational-analytics-overview\">Conversational Analytics</a> will now ask you questions to clarify any ambiguities in your original query.</p>",
    "product_name": "Looker",
    "published_at": "2026-03-26"
  },
  {
    "description": "<p>Upgraded the Open Telemetry image from v0.127.0 to v0.133.0 to pick up vulnerability fixes. This change promotes the <code>pkg.translator.prometheus.NormalizeName</code> feature gate to stable.\nTo understand the changes in each release, review the full changelog for <a href=\"https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/CHANGELOG.md\">opentelemetry-collector-contrib</a>.</p>",
    "product_name": "Anthos Config Management",
    "published_at": "2026-03-26"
  },
  {
    "description": "<p><strong>Google Cloud Compute</strong>: Version 16.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Add IP To Firewall Rule</strong></p></li>\n<li><p><strong>Add Network Tags</strong></p></li>\n<li><p><strong>Delete Instance</strong></p></li>\n<li><p><strong>Execute VM Patch Job</strong></p></li>\n<li><p><strong>Remove IP From Firewall Rule</strong></p></li>\n<li><p><strong>Remove Network Tags</strong></p></li>\n<li><p><strong>Start Instance</strong></p></li>\n<li><p><strong>Stop Instance</strong></p></li>\n<li><p><strong>Update Firewall Rule</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Mandiant ASM</strong>: Version 12.0</p>\n\n<ul>\n<li><p>IIntroduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Update Issue</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>Fixed an ek-cpu-balloon bug which would result in CPUs being underreported on ek machines with SMT enabled.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>BitSight</strong>: Version 12.0</p>\n\n<ul>\n<li><p>IIntroduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Get Company Details</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>Added CPU balloon support for Arm CPUs.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-25"
  },
  {
    "description": "<h4 id=\"2026-r12-version-updates\">(2026-R12) Version updates</h4>\n\n\n<aside class=\"note\"><strong>Note</strong>: Your clusters might not have these versions available.\nRollouts are already in progress when we publish the release notes, and can take\nmultiple days to complete across all Google Cloud zones.</aside>\n\n\n<ul>\n<li>Version <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1351\">1.35.1-gke.1396002</a> is now the default version for cluster creation.</li>\n<li>The following versions are now available:\n<ul>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213\">1.32.13-gke.1147000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339\">1.33.9-gke.1166000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1345\">1.34.5-gke.1208000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352\">1.35.2-gke.1842000</a></li>\n</ul></li>\n<li>The following node versions are now available:\n<ul>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014\">1.30.14-gke.2250000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114\">1.31.14-gke.1634000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213\">1.32.13-gke.1147000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339\">1.33.9-gke.1166000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1345\">1.34.5-gke.1208000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352\">1.35.2-gke.1842000</a></li>\n</ul></li>\n<li>The following versions are no longer available:\n<ul>\n<li>1.32.11-gke.1264000 is <a href=\"https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support\">deprecated</a>. This version will be removed in 90 days, or at the end of support, if sooner.</li>\n<li>1.33.5-gke.2392000 is <a href=\"https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support\">deprecated</a>. This version will be removed in 90 days, or at the end of support, if sooner.</li>\n<li>1.34.3-gke.1444000 is <a href=\"https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support\">deprecated</a>. This version will be removed in 90 days, or at the end of support, if sooner.</li>\n<li>1.35.1-gke.1396001 is <a href=\"https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support\">deprecated</a>. This version will be removed in 90 days, or at the end of support, if sooner.</li>\n</ul></li>\n<li>Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:\n<ul>\n<li>GKE upgrades clusters to the following new minor versions if there are no factors, such as <a href=\"https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions\">maintenance exclusions</a> or deprecated APIs, preventing upgrades:\n<ul>\n<li>1.31 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212\">1.32.12-gke.1127000</a></li>\n<li>1.32 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338\">1.33.8-gke.1026000</a></li>\n</ul></li>\n<li>GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has <a href=\"https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions\">maintenance exclusions</a> or other factors preventing minor version upgrades:\n<ul>\n<li>1.32 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212\">1.32.12-gke.1127000</a></li>\n<li>1.33 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338\">1.33.8-gke.1026000</a></li>\n<li>1.34 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344\">1.34.4-gke.1193000</a></li>\n</ul></li>\n</ul></li>\n</ul>",
    "product_name": "Google Kubernetes Engine",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>Upgraded dev-db/sqlite to v3.51.3.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>An issue has been fixed where creating or updating database connections that use OAuth (such as Snowflake or BigQuery) could fail with the error <code>JDBC Parameter Validation Failed</code>. This feature now performs as expected.</p>",
    "product_name": "Looker",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>The following AlloyDB AI features are available in <a href=\"https://cloud.google.com/products#product-launch-stages\">Preview</a>:</p>\n\n<ul>\n<li><p>You can now use the <code>ai.hybrid_search()</code> function, which fuses results from\neach search type into a single list using the Reciprocal Rank Fusion (RRF)\nalgorithm. For more information, see <a href=\"https://docs.cloud.google.com/alloydb/docs/ai/run-hybrid-vector-similarity-search\">Run hybrid vector similarity search</a>.</p></li>\n<li><p>AlloyDB supports the <code>rum</code> extension for complex full-text search\noperations. The <code>rum</code> extension extends standard GIN indexes by storing\npositional information directly in the index. This enables faster phrase\nsearches and relevance ranking without needing to access the table data. For\nmore information, see <a href=\"https://docs.cloud.google.com/alloydb/docs/ai/create-rum-index\">Create and manage a RUM index</a>.</p></li>\n</ul>",
    "product_name": "AlloyDB",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>Database server compatibility with PostgreSQL version 18 is now generally\navailable (<a href=\"https://cloud.google.com/products#product-launch-stages\">GA</a>):</p>\n\n<ul>\n<li>You can <a href=\"https://docs.cloud.google.com/alloydb/docs/cluster-create#procedure\">create AlloyDB clusters</a>\nwith PostgreSQL 18 compatibility.</li>\n<li>You can <a href=\"https://docs.cloud.google.com/alloydb/docs/upgrade-db-inplace-major-version\">upgrade</a> existing\nAlloyDB clusters running PostgreSQL major versions 14, 15, 16, or 17 to\nPostgreSQL major version 18 with one click.</li>\n<li>You can use Database Migration Service to\n<a href=\"https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest\">migrate databases to AlloyDB</a>.</li>\n</ul>",
    "product_name": "AlloyDB",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>The Spark Spanner connector supports writing a Spark Dataframe to a Spanner\ntable using the Spark data source API. For more information, see\n<a href=\"https://docs.cloud.google.com/dataproc/docs/tutorials/spanner-connector-spark-example#write-spanner-tables\">Use the Spark Spanner connector</a>.</p>",
    "product_name": "Spanner",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Web SDK version 2 will be shut down on June 26, 2026</strong></p>\n\n<p>On June 26, 2025, we announced the launch of <a href=\"https://docs.cloud.google.com/contact-center/ccai-platform/docs/release-notes#June_26_2025\">Web SDK version\n3</a>. Starting on\n<strong>June 26, 2026</strong>, the web SDK v2 will no longer function. Be sure to <a href=\"https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-upgrade\">update\nyour website</a> to use the\nweb SDK v3 before that date to avoid breaking your integration with the web SDK.\nWe are no longer adding new features to the web SDK v2.</p>",
    "product_name": "Google Cloud Contact Center as a Service",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>You can use the <a href=\"https://docs.cloud.google.com/bigquery/docs/migration-assessment\">BigQuery migration assessment for\nSnowflake</a> to assess the complexity of\nmigrating from Snowflake to BigQuery. This feature is\n<a href=\"https://cloud.google.com/products#product-launch-stages\">generally available</a>\n(GA).</p>",
    "product_name": "BigQuery",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>In BigQuery Data Transfer Service, you can\n<a href=\"https://docs.cloud.google.com/bigquery/docs/hdfs-data-lake-transfer#monitor-transfer-status\">monitor resource-level status reporting for Hive managed tables</a>\nto track progress and view granular error details for individual tables.\nThis feature is in\n<a href=\"https://cloud.google.com/products#product-launch-stages\">preview</a>.</p>",
    "product_name": "BigQuery",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>Upgraded virtual/logger to v0-r3.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>You can now use the <a href=\"https://docs.cloud.google.com/bigquery/docs/use-bigquery-migration-mcp\">BigQuery Migration Service MCP server</a>\nto perform SQL translation tasks, including translating SQL queries into\nGoogleSQL syntax, generating DDL statements from SQL input queries, and getting\nexplanations of SQL translations.</p>\n\n<p>This feature is in\n<a href=\"https://cloud.google.com/products/#product-launch-stages\">preview</a>.",
    "product_name": "BigQuery",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>An issue has been fixed where dashboard themes were not applying color collections correctly. This feature now performs as expected.</p>",
    "product_name": "Looker",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>Cloud Location Finder checks service activation and quota for the project that\nyou&#39;re using to run Cloud Location Finder API queries (the client project), not\nthe projects that queries target (the resource project). As a result, you only\nneed to enable the Cloud Location Finder API in your client project.</p>",
    "product_name": "Cloud Location Finder",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>When no theme is selected, the Theme picker will now display &quot;Default&quot; rather than &quot;None&quot;.</p>",
    "product_name": "Looker",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>An issue has been fixed where searching for content could return a 500 error. This feature now performs as expected.</p>",
    "product_name": "Looker",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>BASE quality data generally available in limited APAC regions</strong></p>\n\n<p><code>BASE</code>-quality data coverage (defined as API requests made with\n<code>requiredQuality=BASE</code> where corresponding responses with\n<code>imagery_quality: BASE</code>) is available for residential building areas in the\nfollowing regions: Indonesia, Thailand, Philippines, Malaysia, and Taiwan. Solar\nAPI calls requesting <code>BASE</code> quality data for locations in these regions are\nbilled at the standard rate.</p>\n\n<p>For more details, see the\n<a href=\"https://developers.google.com/maps/documentation/solar/coverage\">Solar API coverage map</a>.</p>",
    "product_name": "Solar API",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>Bigtable client for Java has modernized its Admin API. For detailed migration\nsteps and code examples, see\n<a href=\"https://docs.cloud.google.com/bigtable/docs/upgrading-clients#java\">Upgrading client libraries</a>.</p>",
    "product_name": "Bigtable",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>The <a href=\"https://docs.cloud.google.com/gemini/docs/overview\">Gemini for Google Cloud API</a>\n(cloudaicompanion.googleapis.com) is now enabled for existing\nBigQuery projects in the European jurisdiction.</p>",
    "product_name": "BigQuery",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>An issue has been fixed where the font and background color picker was not accessible when you edited visualizations on merge queries. This feature now performs as expected.</p>",
    "product_name": "Looker",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Looker 26.6</strong> is expected to include the following changes, features, and fixes:</p>\n\n<ul>\n<li><p>Expected Looker (original) deployment start: <strong>Sunday, March 22, 2026</strong></p></li>\n<li><p>Expected Looker (original) final deployment and download available: <strong>Sunday, April 5, 2026</strong></p></li>\n<li><p>Expected Looker (Google Cloud core) deployment start: <strong>Monday, March 23, 2026</strong></p></li>\n<li><p>Expected Looker (Google Cloud core) final deployment: <strong>Friday, April 3, 2026</strong></p></li>\n</ul>",
    "product_name": "Looker",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>Upgraded app-admin/google-osconfig-agent to v20260119.00.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>ArcSight</strong>: Version 45.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>List Resources</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>RSA Archer</strong>: Version 14.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Add Incident Journal Entry</strong></p></li>\n<li><p><strong>Create Incident</strong></p></li>\n<li><p><strong>Get Incident Details</strong></p></li>\n<li><p><strong>Update Incident</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>IronPort</strong>: Version 15.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Get All Recipients By Sender</strong></p></li>\n<li><p><strong>Get All Recipients By Subject</strong></p></li>\n<li><p><strong>Get Report</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Ivanti Endpoint Manager</strong>: Version 9.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Execute Query</strong></p></li>\n<li><p><strong>List Column Set Fields</strong></p></li>\n<li><p><strong>List Column Sets</strong></p></li>\n<li><p><strong>List Delivery Methods</strong></p></li>\n<li><p><strong>List Packages</strong></p></li>\n<li><p><strong>List Queries</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Carbon Black Response</strong>: Version 38.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Get FileMod Data For Process</strong></p></li>\n<li><p><strong>Get Process Tree Data</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Credential validation for third-party API connectors</strong></p>\n\n<p>Credential validation is now available for all 49 third-party API connectors.</p>\n\n<p>When you create a feed using a third-party API connector, Google SecOps now automatically validates the provided credentials. This ensures that if credentials are incorrect:</p>\n\n<ul>\n<li><strong>Immediate feedback</strong>: The web interface displays an error message explaining the configuration failure.</li>\n<li><strong>Prevention of broken feeds</strong>: The system blocks the creation of the feed until valid credentials are provided, preventing the creation of broken feeds that fail to ingest data later.</li>\n</ul>",
    "product_name": "Google SecOps",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Okta</strong>: Version 16.0</p>\n\n<ul>\n<li><strong>Integration</strong>: Added support for OAuth authentication.</li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Remote Agent Utilities</strong>: Version 7.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Serialize A File</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Microsoft Azure Sentinel</strong>: Version 62.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Add Comment to Incident</strong></p></li>\n<li><p><strong>Create Alert Rule</strong></p></li>\n<li><p><strong>Create Custom Hunting Rule</strong></p></li>\n<li><p><strong>Get Alert Rule Details</strong></p></li>\n<li><p><strong>Get Custom Hunting Rule Details</strong></p></li>\n<li><p><strong>Get Incident Statistic</strong></p></li>\n<li><p><strong>Update Alert Rule</strong></p></li>\n<li><p><strong>Update Custom Hunting Rule</strong></p></li>\n<li><p><strong>Update Incident Details</strong></p></li>\n<li><p><strong>Update Incident Details v2</strong></p></li>\n<li><p><strong>Update Incident Labels</strong></p></li>\n<li><p><strong>Update Incident Labels v2</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Microsoft Graph Security</strong>: Version 26.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Get Alert</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Splunk</strong>: Version 64.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Submit Event</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Qualys VM</strong>: Version 24.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Download Report</strong></p></li>\n<li><p><strong>List Ips</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Check Point Firewall</strong>: Version 15.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Add a SAM Rule</strong></p></li>\n<li><p><strong>Remove SAM Rule</strong></p></li>\n<li><p><strong>Run Script</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>IntSights</strong>: Version 26.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Download Alert CSV</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Trend Micro Cloud App Security</strong>: Version 11.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Enrich Entities</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Credential validation for third-party API connectors</strong></p>\n\n<p>Credential validation is now available for all 49 third-party API connectors.</p>\n\n<p>When you create a feed using a third-party API connector, Google SecOps now automatically validates the provided credentials. This ensures that if credentials are incorrect:</p>\n\n<ul>\n<li><strong>Immediate feedback</strong>: The web interface displays an error message explaining the configuration failure.</li>\n<li><strong>Prevention of broken feeds</strong>: The system blocks the creation of the feed until valid credentials are provided, preventing the creation of broken feeds that fail to ingest data later.</li>\n</ul>",
    "product_name": "Google SecOps SIEM",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>AWS GuardDuty</strong>: Version 11.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Create a Detector</strong></p></li>\n<li><p><strong>Create a Trusted IP List</strong></p></li>\n<li><p><strong>Create Threat Intelligence Set</strong></p></li>\n<li><p><strong>Get all Trusted IP lists</strong></p></li>\n<li><p><strong>Get Finding Details</strong></p></li>\n<li><p><strong>List Detectors</strong></p></li>\n<li><p><strong>List Findings for a Detector</strong></p></li>\n<li><p><strong>List Threat Intelligence Sets</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>Upgraded dev-libs/expat to v2.7.5.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Reversinglabs A1000</strong>: Version 9.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Upload File</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>Added support for loading the ublk kernel module.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Anomali</strong>: Version 14.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Get Related Associations</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Cloudflare</strong>: Version 7.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Create Firewall Rule</strong></p></li>\n<li><p><strong>Create Rule List</strong></p></li>\n<li><p><strong>Update Firewall Rule</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>Upgraded sys-apps/file to v5.47-r1.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>To provide more controls over the control plane version upgrade, you can now do\nthe following:</p>\n\n<ul>\n<li>Configure a frequency of disruption from auto-upgrades by using the cluster\ndisruption budget. For more information, see\n<a href=\"https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-disruption-budget\">Control the frequency of disruption from auto-upgrades</a>.</li>\n<li>Continue using an existing control plane patch for a longer period, which\nfacilitates large-scale upgrade and downgrade operations. For more\ninformation, see\n<a href=\"https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support\">Patch version support</a>.</li>\n</ul>",
    "product_name": "Google Kubernetes Engine",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Office 365 CloudApp Security</strong>: Version 25.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Add IP To IP Address Range</strong></p></li>\n<li><p><strong>Create IP Address Range</strong></p></li>\n<li><p><strong>Remove IP From IP Address Range</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Azure API</strong>: Version 3.0</p>\n\n<ul>\n<li><p>Added predefined widget to the following action:</p>\n\n<ul>\n<li><strong>Ping</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Microsoft Defender ATP</strong>: Version 30.0</p>\n\n<ul>\n<li><p>The following new actions have been added:</p>\n\n<ul>\n<li><p><strong>Get Machine Recommendations</strong></p></li>\n<li><p><strong>Get Machine Vulnerabilities</strong></p></li>\n<li><p><strong>Get User Related Alerts</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Microsoft Graph Security</strong>: Version 26.0</p>\n\n<ul>\n<li><p>Added predefined widget to the following action:</p>\n\n<ul>\n<li><strong>Get Incident</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Google Cloud IAM</strong>: Version 20.0</p>\n\n<ul>\n<li><p>The following new action has been added:</p>\n\n<ul>\n<li><strong>Rotate Service Account Keys</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Siemplify</strong>: Version 106.0</p>\n\n<ul>\n<li><p>The following new action has been added:</p>\n\n<ul>\n<li><strong>Search Cases</strong></li>\n</ul></li>\n<li><p>Added predefined widget to the following action:</p>\n\n<ul>\n<li><strong>Search Cases</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Lyria 3</strong></p>\n\n<p>Lyria is available in <a href=\"https://cloud.google.com/products#product-launch-stages\">public\npreview</a>. You can use\n<code>lyria-3-pro-preview</code> to generate 184 seconds of audio, or\n<code>lyria-3-clip-preview</code> to generate 30 seconds of audio.</p>\n\n<p>For more information, see the following:</p>\n\n<ul>\n<li><p><a href=\"https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/lyria/lyria-3#lyria-3-pro-preview\">Lyria 3 Pro\nPreview</a></p></li>\n<li><p><a href=\"https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/lyria/lyria-3#lyria-3-clip-preview\">Lyria 3 Clip Preview</a></p></li>\n</ul>",
    "product_name": "Generative AI on Vertex AI",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Symantec Endpoint Security Complete Cloud</strong>: Version 8.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Symantec Endpoint Security Complete Cloud</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>ThreatQ</strong>: Version 18.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Add Attribute</strong></p></li>\n<li><p><strong>Add Source</strong></p></li>\n<li><p><strong>Create Adversary</strong></p></li>\n<li><p><strong>Create Event</strong></p></li>\n<li><p><strong>Create Indicator</strong></p></li>\n<li><p><strong>Create Object</strong></p></li>\n<li><p><strong>Link Objects</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Google Threat Intelligence</strong>: Version 13.0</p>\n\n<ul>\n<li><p>Improved loading for predefined widgets of the following actions:</p>\n\n<ul>\n<li><p><strong>Enrich Entities</strong></p></li>\n<li><p><strong>Enrich IOC</strong></p></li>\n</ul></li>\n<li><p>Removed the usage of a deprecated API endpoint and the <code>Retrieve AI Summary</code>\nparameter from the following action:</p>\n\n<ul>\n<li><strong>Submit File</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>AWS CloudWatch</strong>: Version 9.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Create Log Group</strong></p></li>\n<li><p><strong>Create Log Stream</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Microsoft Teams</strong>: Version 35.0</p>\n\n<ul>\n<li><p><strong>Integration</strong>: Updated dependencies.</p></li>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Create Channel</strong></p></li>\n<li><p><strong>Create Channel</strong></p></li>\n<li><p><strong>Send Chat Message</strong></p></li>\n<li><p><strong>Send Message Reply</strong></p></li>\n<li><p><strong>Wait For Reply</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Illusive Networks</strong>: Version 6.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>List Deceptive Items</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>F5 BIG-IP iControl API</strong>: Version 7.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Add IP To Address List</strong></p></li>\n<li><p><strong>Add IP To Data Group</strong></p></li>\n<li><p><strong>Add Port To Port List</strong></p></li>\n<li><p><strong>Create Address List</strong></p></li>\n<li><p><strong>Create Data Group</strong></p></li>\n<li><p><strong>Create iRule</strong></p></li>\n<li><p><strong>Create Port List</strong></p></li>\n<li><p><strong>Remove IP From Address List</strong></p></li>\n<li><p><strong>Remove IP From Data Group</strong></p></li>\n<li><p><strong>Remove Port From Port List</strong></p></li>\n<li><p><strong>Update iRule</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Site24x7</strong>: Version 6.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Generate Refresh Token</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>FortiAnalyzer</strong>: Version 11.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Add Comment To Alert</strong></p></li>\n<li><p><strong>Update Alert</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>Tabbed dashboards with unsupported layouts will now display a warning message prompting users to <a href=\"https://docs.cloud.google.com/looker/docs/best-practices/troubleshooting-unsupported-dashboard-layout\">update to a new layout</a>.</p>",
    "product_name": "Looker",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>LogRhythm</strong>: Version 22.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Add Note To Case</strong></p></li>\n<li><p><strong>Create Cas</strong></p></li>\n<li><p><strong>Download Case Files</strong></p></li>\n<li><p><strong>Update Case</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>An issue has been fixed where pressing Enter to confirm IME composition when writing a message in Conversational Analytics would prematurely submit the message. This feature now performs as expected.</p>",
    "product_name": "Looker",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>An issue has been fixed where buttons on dashboards that used the extension framework could unnecessarily add <code>/embed/</code> to link URLs. This feature now performs as expected.</p>",
    "product_name": "Looker",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>Updated sys-libs/binutils-libs to 2.46.0. This resolves CVE-2025-69644.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Microsoft Defender ATP</strong>: Version 30.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Update Alert</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>Fixed CVE-2026-32597 with pyjwt package upgrade to v2.12.1.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>Fixed CVE-2026-32597 with pyjwt package upgrade to 2.12.1.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Cofense Triage</strong>: Version 20.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Add Tags To Report</strong></p></li>\n<li><p><strong>Categorize Report</strong></p></li>\n<li><p><strong>Download Report Email</strong></p></li>\n<li><p><strong>Download Report Preview</strong></p></li>\n<li><p><strong>Get Report Reporters</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Google Cloud Recommender</strong>: Version 10.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Apply IAM Recommendations</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Falcon Sandbox</strong>: Version 20.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Wait For Job and Fetch Report</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Freshworks Freshservice</strong>: Version 18.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Create Agent</strong></p></li>\n<li><p><strong>Deactivate Agent</strong></p></li>\n<li><p><strong>Update Agent</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Palo Alto Next Gen Firewall</strong>: Version 28.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Add Ips to group</strong></p></li>\n<li><p><strong>Block ips in policy</strong></p></li>\n<li><p><strong>Block Urls</strong></p></li>\n<li><p><strong>Edit Blocked Applications</strong></p></li>\n<li><p><strong>Get Blocked Applications</strong></p></li>\n<li><p><strong>Remove Ips from group</strong></p></li>\n<li><p><strong>Unblock ips in policy</strong></p></li>\n<li><p><strong>Unblock Urls</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Sophos</strong>: Version 20.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>List Alert Actions</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>Fixed CVE-2025-71268 in the Linux kernel.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Gmail</strong>: Version 8.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Forward Email</strong></p></li>\n<li><p><strong>Save Email To The Case</strong></p></li>\n<li><p><strong>Send Email</strong></p></li>\n<li><p><strong>Send Thread Reply</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>Fixed KCTF-c9bc175 in the Linux kernel.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Microsoft Graph Mail</strong>: Version 39.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Forward Email</strong></p></li>\n<li><p><strong>Save Email to the Case</strong></p></li>\n<li><p><strong>Send Email</strong></p></li>\n<li><p><strong>Send Email HTML</strong></p></li>\n<li><p><strong>Send Thread Reply</strong></p></li>\n<li><p><strong>Send Vote Email</strong></p></li>\n<li><p><strong>Wait For Email From User</strong></p></li>\n<li><p><strong>Wait For Vote Email Results</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Google Cloud Armor</strong>: Version 5.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Add a Rule to a Security Policy</strong></p></li>\n<li><p><strong>Create a Security Policy</strong></p></li>\n<li><p><strong>Update a Security Policy</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>Fixed CVE-2025-71266 in the Linux kernel.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>Fixed CVE-2026-23243 in the Linux kernel.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>FireEye Helix</strong>: Version 18.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Archive Search</strong></p></li>\n<li><p><strong>Get Alert Details</strong></p></li>\n<li><p><strong>Index Search</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Extrahop</strong>: Version 8.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Update Detection</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>MobileIron</strong>: Version 6.0</p>\n\n<ul>\n<li><strong>Integration</strong>: The integration&#39;s source code is now publicly available on\n<a href=\"https://github.com/chronicle/content-hub\">Github</a>.</li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Endgame</strong>: Version 14.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Get Investigation Details</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>Fixed KCTF-329f0b9 in the Linux kernel.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>Fixed CVE-2026-23262 in the Linux kernel.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Google Chat</strong>: Version 7.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Send Advanced Message</strong></p></li>\n<li><p><strong>Send Message</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>Fixed CVE-2025-71267 in the Linux kernel.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>Fixed CVE-2026-23254 in the Linux kernel.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>NessusScanner</strong>: Version 12.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Get Scan Templates</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>Updated net-misc/curl to v8.19.0. This resolves CVE-2026-1965 and CVE-2026-3783.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>Fixed CVE-2025-71265 in the Linux kernel.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-25"
  },
  {
    "description": "<h4 id=\"2026-r12-security-updates\">(2026-R12) Security updates</h4>\n\n<p>This release includes new GKE versions that use updated\nContainer-Optimized OS images. These updated images are cumulative,\nincorporating security fixes from all Container-Optimized OS\nversions released since the previous GKE release.</p>\n\n<p>To identify the specific vulnerabilities that were resolved in each updated\nContainer-Optimized OS image, see the <strong>Security</strong> release notes\nfor that image. The following table includes links to the release notes for\neach updated Container-Optimized OS image:</p>\n\n<p>\n\n<table>\n<tbody>\n<tr>\n<th>GKE version</th>\n<th>Container-Optimized OS version</th>\n<th>Details</th>\n</tr>\n<tr>\n<td>1.30.14-gke.2250000</td>\n<td>cos-117-18613-534-36</td>\n<td><a href=\"https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m117#cos-117-18613-534-36_\">cos-117-18613-534-36 release notes</a></td>\n</tr>\n<tr>\n<td>1.31.14-gke.1634000</td>\n<td>cos-117-18613-534-36</td>\n<td><a href=\"https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m117#cos-117-18613-534-36_\">cos-117-18613-534-36 release notes</a></td>\n</tr>\n<tr>\n<td>1.32.13-gke.1147000</td>\n<td>cos-117-18613-534-24</td>\n<td><a href=\"https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m117#cos-117-18613-534-24_\">cos-117-18613-534-24 release notes</a></td>\n</tr>\n<tr>\n<td>1.33.9-gke.1166000</td>\n<td>cos-121-18867-381-24</td>\n<td><a href=\"https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m121#cos-121-18867-381-24_\">cos-121-18867-381-24 release notes</a></td>\n</tr>\n</tbody>\n</table>\n\n</p>",
    "product_name": "Google Kubernetes Engine",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>When no major version is specified, AlloyDB for PostgreSQL now defaults to\n<a href=\"https://docs.cloud.google.com/alloydb/docs/db-version-policies#support-table\">PostgreSQL major version 17</a>\nfor new clusters.</p>",
    "product_name": "AlloyDB",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Recorded Future</strong>: Version 21.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Get Alert Details</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Palo Alto Cortex XDR</strong>: Version 26.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Get Incident Details</strong></p></li>\n<li><p><strong>Query</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>CA Service Desk Manager</strong>: Version 26.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Wait For Status Change</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<h3 id=\"cos-dev-133-19654-0-0_\">cos-dev-133-19654-0-0 <a id=&quot;cos-arm64-dev-133-19654-0-0&quot;/></h3>\n\n<table class=pkg>\n  <tr>\n    <td>Kernel</td>\n    <td>Docker</td>\n    <td>Containerd</td>\n    <td><a href=\"https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus\">GPU Drivers</a></td>\n  </tr>\n  <tr>\n    <td><a href=\"https://cos.googlesource.com/third_party/kernel/+/8ecb3fb8b4bed2db662e41f5991ae84debec7939\n\">COS-6.12.76</a></td>\n    <td>v27.5.1</td>\n    <td>v2.2.1</td>\n    <td><a href=\"https://storage.googleapis.com/cos-tools/19654.0.0/lakitu/gpu_driver_versions.textproto\">See List</a></td>\n  </tr>\n</table>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>Runtime sysctl changes:\n<ul>\n<li>Changed: net.ipv4.udp_mem: 188034   250714  376068 -&gt; 188034    250715  376068</li>\n</ul></p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>JoeSandbox</strong>: Version 10.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Detonate File</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Service Desk Plus V3</strong>: Version 8.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Add Note</strong></p></li>\n<li><p><strong>Add Note And Wait For Reply</strong></p></li>\n<li><p><strong>Close Request</strong></p></li>\n<li><p><strong>Create Alert Request</strong></p></li>\n<li><p><strong>Create Request</strong></p></li>\n<li><p><strong>Create Request - Dropdown Lists</strong></p></li>\n<li><p><strong>Get Request</strong></p></li>\n<li><p><strong>Update Request</strong></p></li>\n<li><p><strong>Wait For Field Update</strong></p></li>\n<li><p><strong>Wait For Status Update</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>Added support for the Lustre 2.14.0_p249 drivers.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>MISP</strong>: Version 37.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Create Event</strong></p></li>\n<li><p><strong>Create File Misp Object</strong></p></li>\n<li><p><strong>Create IP-Port Misp Object</strong></p></li>\n<li><p><strong>Create network-connection Misp Object</strong></p></li>\n<li><p><strong>Create Virustotal-Report Object</strong></p></li>\n<li><p><strong>Download File</strong></p></li>\n<li><p><strong>Publish Event</strong></p></li>\n<li><p><strong>Unpublish Event</strong></p></li>\n<li><p><strong>Upload File</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<h3 id=\"cos-125-19216-220-87_\">cos-125-19216-220-87 <a id=&quot;cos-arm64-125-19216-220-87&quot;/></h3>\n\n<table class=pkg>\n  <tr>\n    <td>Kernel</td>\n    <td>Docker</td>\n    <td>Containerd</td>\n    <td><a href=\"https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus\">GPU Drivers</a></td>\n  </tr>\n  <tr>\n    <td><a href=\"https://cos.googlesource.com/third_party/kernel/+/98c1b6ad6f970918e8fe029d2ee331c556111ae3\n\">COS-6.12.68</a></td>\n    <td>v27.5.1</td>\n    <td>v2.1.5</td>\n    <td><a href=\"https://storage.googleapis.com/cos-tools/19216.220.87/lakitu/gpu_driver_versions.textproto\">See List</a></td>\n  </tr>\n</table>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>AlienVault USM Appliance</strong>: Version 25.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Get PCAP Files For Events</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Symantec Endpoint Protection 12</strong>: Version 15.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>GetReport</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>An issue has been fixed where tabs could be automatically added to existing dashboards. This feature now performs as expected.</p>",
    "product_name": "Looker",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>An issue has been fixed where opening the <strong>Interaction Details</strong> dialog on the <strong>Historical Analytics Interactions Search</strong> dashboard in a new window could result in a 401 error. This feature now performs as expected.</p>",
    "product_name": "Looker",
    "published_at": "2026-03-25"
  },
  {
    "description": "<h4 id=\"2026-r12-version-updates\">(2026-R12) Version updates</h4>\n\n\n<aside class=\"note\"><strong>Note</strong>: Your clusters might not have these versions available.\nRollouts are already in progress when we publish the release notes, and can take\nmultiple days to complete across all Google Cloud zones.</aside>\n\n\n<ul>\n<li>Version <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338\">1.33.8-gke.1026000</a> is now the default version for cluster creation in the Stable channel.</li>\n<li>The following versions are now available in the Stable channel:\n<ul>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212\">1.32.12-gke.1076000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338\">1.33.8-gke.1112000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344\">1.34.4-gke.1130000</a></li>\n</ul></li>\n<li>The following versions are no longer available in the Stable channel:\n<ul>\n<li>1.32.11-gke.1264000 is <a href=\"https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support\">deprecated</a> in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.</li>\n<li>1.33.5-gke.2469000</li>\n<li>1.34.3-gke.1444000 is <a href=\"https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support\">deprecated</a> in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.</li>\n</ul></li>\n<li>Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:\n<ul>\n<li>GKE upgrades clusters to the following new minor versions if there are no factors, such as <a href=\"https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions\">maintenance exclusions</a> or deprecated APIs, preventing upgrades:\n<ul>\n<li>1.31 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212\">1.32.12-gke.1026000</a></li>\n<li>1.32 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338\">1.33.8-gke.1026000</a></li>\n</ul></li>\n<li>GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has <a href=\"https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions\">maintenance exclusions</a> or other factors preventing minor version upgrades:\n<ul>\n<li>1.32 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212\">1.32.12-gke.1026000</a></li>\n<li>1.33 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338\">1.33.8-gke.1026000</a></li>\n<li>1.34 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344\">1.34.4-gke.1047000</a></li>\n</ul></li>\n</ul></li>\n</ul>",
    "product_name": "Google Kubernetes Engine",
    "published_at": "2026-03-25"
  },
  {
    "description": "<h4 id=\"2026-r12-version-updates\">(2026-R12) Version updates</h4>\n\n\n<aside class=\"note\"><strong>Note</strong>: Your clusters might not have these versions available.\nRollouts are already in progress when we publish the release notes, and can take\nmultiple days to complete across all Google Cloud zones.</aside>\n\n\n<ul>\n<li>Version <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352\">1.35.2-gke.1485000</a> is now the default version for cluster creation in the Rapid channel.</li>\n<li>The following versions are now available in the Rapid channel:\n<ul>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213\">1.32.13-gke.1147000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339\">1.33.9-gke.1166000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1345\">1.34.5-gke.1208000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352\">1.35.2-gke.1842000</a></li>\n</ul></li>\n<li>The following versions are no longer available in the Rapid channel:\n<ul>\n<li>1.32.13-gke.1059000</li>\n<li>1.33.9-gke.1060000</li>\n<li>1.34.5-gke.1076000</li>\n<li>1.35.2-gke.1269001</li>\n</ul></li>\n<li>Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:\n<ul>\n<li>GKE upgrades clusters to the following new minor versions if there are no factors, such as <a href=\"https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions\">maintenance exclusions</a> or deprecated APIs, preventing upgrades:\n<ul>\n<li>1.31 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213\">1.32.13-gke.1090000</a></li>\n<li>1.32 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339\">1.33.9-gke.1117000</a></li>\n<li>1.33 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1345\">1.34.5-gke.1153000</a></li>\n<li>1.34 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352\">1.35.2-gke.1485000</a></li>\n</ul></li>\n<li>GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has <a href=\"https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions\">maintenance exclusions</a> or other factors preventing minor version upgrades:\n<ul>\n<li>1.32 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213\">1.32.13-gke.1090000</a></li>\n<li>1.33 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339\">1.33.9-gke.1117000</a></li>\n<li>1.34 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1345\">1.34.5-gke.1153000</a></li>\n<li>1.35 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352\">1.35.2-gke.1485000</a></li>\n</ul></li>\n</ul></li>\n</ul>",
    "product_name": "Google Kubernetes Engine",
    "published_at": "2026-03-25"
  },
  {
    "description": "<h4 id=\"2026-r12-version-updates\">(2026-R12) Version updates</h4>\n\n\n<aside class=\"note\"><strong>Note</strong>: Your clusters might not have these versions available.\nRollouts are already in progress when we publish the release notes, and can take\nmultiple days to complete across all Google Cloud zones.</aside>\n\n\n<ul>\n<li>Version <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1351\">1.35.1-gke.1396002</a> is now the default version for cluster creation in the Extended channel.</li>\n<li>The following versions are now available in the Extended channel:\n<ul>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014\">1.30.14-gke.2192000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014\">1.30.14-gke.2250000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114\">1.31.14-gke.1576000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114\">1.31.14-gke.1634000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213\">1.32.13-gke.1059000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339\">1.33.9-gke.1060000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1345\">1.34.5-gke.1076000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352\">1.35.2-gke.1269001</a></li>\n</ul></li>\n<li>The following versions are no longer available in the Extended channel:\n<ul>\n<li>1.30.14-gke.2117000 is <a href=\"https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support\">deprecated</a> in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.</li>\n<li>1.30.14-gke.2215000 is <a href=\"https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support\">deprecated</a> in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.</li>\n<li>1.31.14-gke.1476000 is <a href=\"https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support\">deprecated</a> in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.</li>\n<li>1.31.14-gke.1599000 is <a href=\"https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support\">deprecated</a> in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.</li>\n<li>1.32.12-gke.1076000</li>\n<li>1.33.8-gke.1112000</li>\n<li>1.34.4-gke.1130000</li>\n</ul></li>\n<li>Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:\n<ul>\n<li>GKE upgrades clusters to the following new minor versions if there are no factors, such as <a href=\"https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions\">maintenance exclusions</a> or deprecated APIs, preventing upgrades:\n<ul>\n<li>1.29 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014\">1.30.14-gke.2154000</a></li>\n</ul></li>\n<li>GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has <a href=\"https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions\">maintenance exclusions</a> or other factors preventing minor version upgrades:\n<ul>\n<li>1.30 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014\">1.30.14-gke.2154000</a></li>\n<li>1.31 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114\">1.31.14-gke.1526000</a></li>\n<li>1.32 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212\">1.32.12-gke.1127000</a></li>\n<li>1.33 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338\">1.33.8-gke.1169000</a></li>\n<li>1.34 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344\">1.34.4-gke.1193000</a></li>\n</ul></li>\n</ul></li>\n</ul>",
    "product_name": "Google Kubernetes Engine",
    "published_at": "2026-03-25"
  },
  {
    "description": "<h4 id=\"2026-r12-version-updates\">(2026-R12) Version updates</h4>\n\n\n<aside class=\"note\"><strong>Note</strong>: Your clusters might not have these versions available.\nRollouts are already in progress when we publish the release notes, and can take\nmultiple days to complete across all Google Cloud zones.</aside>\n\n\n<ul>\n<li>Version <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1351\">1.35.1-gke.1396002</a> is now the default version for cluster creation in the Regular channel.</li>\n<li>The following versions are now available in the Regular channel:\n<ul>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213\">1.32.13-gke.1059000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339\">1.33.9-gke.1060000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1345\">1.34.5-gke.1076000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352\">1.35.2-gke.1269001</a></li>\n</ul></li>\n<li>The following versions are no longer available in the Regular channel:\n<ul>\n<li>1.32.12-gke.1076000</li>\n<li>1.33.8-gke.1112000</li>\n<li>1.34.4-gke.1130000</li>\n</ul></li>\n<li>Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:\n<ul>\n<li>GKE upgrades clusters to the following new minor versions if there are no factors, such as <a href=\"https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions\">maintenance exclusions</a> or deprecated APIs, preventing upgrades:\n<ul>\n<li>1.31 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212\">1.32.12-gke.1127000</a></li>\n<li>1.32 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338\">1.33.8-gke.1169000</a></li>\n<li>1.33 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344\">1.34.4-gke.1193000</a></li>\n</ul></li>\n<li>GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has <a href=\"https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions\">maintenance exclusions</a> or other factors preventing minor version upgrades:\n<ul>\n<li>1.32 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212\">1.32.12-gke.1127000</a></li>\n<li>1.33 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338\">1.33.8-gke.1169000</a></li>\n<li>1.34 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344\">1.34.4-gke.1193000</a></li>\n</ul></li>\n</ul></li>\n</ul>",
    "product_name": "Google Kubernetes Engine",
    "published_at": "2026-03-25"
  },
  {
    "description": "<h4 id=\"2026-r12-version-updates\">(2026-R12) Version updates</h4>\n\n\n\n<p>GKE cluster versions have been updated.</p>\n\n<p><strong>New versions available for upgrades and new clusters.</strong></p>\n\n<p>The following versions are now available for new GKE clusters, and for\nmanual control plane upgrades and node upgrades for existing clusters. For more\ninformation about versioning and upgrades, see <a href=\"https://cloud.google.com/kubernetes-engine/versioning\">GKE versioning and\nsupport</a> and <a href=\"https://cloud.google.com/kubernetes-engine/upgrades\">About GKE\ncluster upgrades</a>.</p>\n\n<div>\n<devsite-selector>\n<section>\n  <h3>Rapid channel</h3>\n  <aside class=\"note\"><strong>Note</strong>: Your clusters might not have these versions available.\nRollouts are already in progress when we publish the release notes, and can take\nmultiple days to complete across all Google Cloud zones.</aside>\n  \n\n<ul>\n<li>Version <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352\">1.35.2-gke.1485000</a> is now the default version for cluster creation in the Rapid channel.</li>\n<li>The following versions are now available in the Rapid channel:\n<ul>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213\">1.32.13-gke.1147000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339\">1.33.9-gke.1166000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1345\">1.34.5-gke.1208000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352\">1.35.2-gke.1842000</a></li>\n</ul></li>\n<li>The following versions are no longer available in the Rapid channel:\n<ul>\n<li>1.32.13-gke.1059000</li>\n<li>1.33.9-gke.1060000</li>\n<li>1.34.5-gke.1076000</li>\n<li>1.35.2-gke.1269001</li>\n</ul></li>\n<li>Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:\n<ul>\n<li>GKE upgrades clusters to the following new minor versions if there are no factors, such as <a href=\"https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions\">maintenance exclusions</a> or deprecated APIs, preventing upgrades:\n<ul>\n<li>1.31 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213\">1.32.13-gke.1090000</a></li>\n<li>1.32 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339\">1.33.9-gke.1117000</a></li>\n<li>1.33 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1345\">1.34.5-gke.1153000</a></li>\n<li>1.34 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352\">1.35.2-gke.1485000</a></li>\n</ul></li>\n<li>GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has <a href=\"https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions\">maintenance exclusions</a> or other factors preventing minor version upgrades:\n<ul>\n<li>1.32 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213\">1.32.13-gke.1090000</a></li>\n<li>1.33 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339\">1.33.9-gke.1117000</a></li>\n<li>1.34 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1345\">1.34.5-gke.1153000</a></li>\n<li>1.35 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352\">1.35.2-gke.1485000</a></li>\n</ul></li>\n</ul></li>\n</ul>\n\n\n</section>\n<section>\n  <h3>Regular channel</h3>\n  <aside class=\"note\"><strong>Note</strong>: Your clusters might not have these versions available.\nRollouts are already in progress when we publish the release notes, and can take\nmultiple days to complete across all Google Cloud zones.</aside>\n  \n\n<ul>\n<li>Version <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1351\">1.35.1-gke.1396002</a> is now the default version for cluster creation in the Regular channel.</li>\n<li>The following versions are now available in the Regular channel:\n<ul>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213\">1.32.13-gke.1059000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339\">1.33.9-gke.1060000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1345\">1.34.5-gke.1076000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352\">1.35.2-gke.1269001</a></li>\n</ul></li>\n<li>The following versions are no longer available in the Regular channel:\n<ul>\n<li>1.32.12-gke.1076000</li>\n<li>1.33.8-gke.1112000</li>\n<li>1.34.4-gke.1130000</li>\n</ul></li>\n<li>Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:\n<ul>\n<li>GKE upgrades clusters to the following new minor versions if there are no factors, such as <a href=\"https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions\">maintenance exclusions</a> or deprecated APIs, preventing upgrades:\n<ul>\n<li>1.31 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212\">1.32.12-gke.1127000</a></li>\n<li>1.32 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338\">1.33.8-gke.1169000</a></li>\n<li>1.33 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344\">1.34.4-gke.1193000</a></li>\n</ul></li>\n<li>GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has <a href=\"https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions\">maintenance exclusions</a> or other factors preventing minor version upgrades:\n<ul>\n<li>1.32 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212\">1.32.12-gke.1127000</a></li>\n<li>1.33 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338\">1.33.8-gke.1169000</a></li>\n<li>1.34 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344\">1.34.4-gke.1193000</a></li>\n</ul></li>\n</ul></li>\n</ul>\n\n\n</section>\n<section>\n  <h3>Stable channel</h3>\n  <aside class=\"note\"><strong>Note</strong>: Your clusters might not have these versions available.\nRollouts are already in progress when we publish the release notes, and can take\nmultiple days to complete across all Google Cloud zones.</aside>\n  \n\n<ul>\n<li>Version <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338\">1.33.8-gke.1026000</a> is now the default version for cluster creation in the Stable channel.</li>\n<li>The following versions are now available in the Stable channel:\n<ul>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212\">1.32.12-gke.1076000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338\">1.33.8-gke.1112000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344\">1.34.4-gke.1130000</a></li>\n</ul></li>\n<li>The following versions are no longer available in the Stable channel:\n<ul>\n<li>1.32.11-gke.1264000 is <a href=\"https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support\">deprecated</a> in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.</li>\n<li>1.33.5-gke.2469000</li>\n<li>1.34.3-gke.1444000 is <a href=\"https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support\">deprecated</a> in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.</li>\n</ul></li>\n<li>Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:\n<ul>\n<li>GKE upgrades clusters to the following new minor versions if there are no factors, such as <a href=\"https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions\">maintenance exclusions</a> or deprecated APIs, preventing upgrades:\n<ul>\n<li>1.31 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212\">1.32.12-gke.1026000</a></li>\n<li>1.32 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338\">1.33.8-gke.1026000</a></li>\n</ul></li>\n<li>GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has <a href=\"https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions\">maintenance exclusions</a> or other factors preventing minor version upgrades:\n<ul>\n<li>1.32 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212\">1.32.12-gke.1026000</a></li>\n<li>1.33 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338\">1.33.8-gke.1026000</a></li>\n<li>1.34 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344\">1.34.4-gke.1047000</a></li>\n</ul></li>\n</ul></li>\n</ul>\n\n\n</section>\n<section>\n  <h3>Extended channel</h3>\n  <aside class=\"note\"><strong>Note</strong>: Your clusters might not have these versions available.\nRollouts are already in progress when we publish the release notes, and can take\nmultiple days to complete across all Google Cloud zones.</aside>\n  \n\n<ul>\n<li>Version <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1351\">1.35.1-gke.1396002</a> is now the default version for cluster creation in the Extended channel.</li>\n<li>The following versions are now available in the Extended channel:\n<ul>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014\">1.30.14-gke.2192000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014\">1.30.14-gke.2250000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114\">1.31.14-gke.1576000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114\">1.31.14-gke.1634000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213\">1.32.13-gke.1059000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339\">1.33.9-gke.1060000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1345\">1.34.5-gke.1076000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352\">1.35.2-gke.1269001</a></li>\n</ul></li>\n<li>The following versions are no longer available in the Extended channel:\n<ul>\n<li>1.30.14-gke.2117000 is <a href=\"https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support\">deprecated</a> in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.</li>\n<li>1.30.14-gke.2215000 is <a href=\"https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support\">deprecated</a> in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.</li>\n<li>1.31.14-gke.1476000 is <a href=\"https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support\">deprecated</a> in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.</li>\n<li>1.31.14-gke.1599000 is <a href=\"https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support\">deprecated</a> in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.</li>\n<li>1.32.12-gke.1076000</li>\n<li>1.33.8-gke.1112000</li>\n<li>1.34.4-gke.1130000</li>\n</ul></li>\n<li>Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:\n<ul>\n<li>GKE upgrades clusters to the following new minor versions if there are no factors, such as <a href=\"https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions\">maintenance exclusions</a> or deprecated APIs, preventing upgrades:\n<ul>\n<li>1.29 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014\">1.30.14-gke.2154000</a></li>\n</ul></li>\n<li>GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has <a href=\"https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions\">maintenance exclusions</a> or other factors preventing minor version upgrades:\n<ul>\n<li>1.30 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014\">1.30.14-gke.2154000</a></li>\n<li>1.31 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114\">1.31.14-gke.1526000</a></li>\n<li>1.32 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212\">1.32.12-gke.1127000</a></li>\n<li>1.33 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338\">1.33.8-gke.1169000</a></li>\n<li>1.34 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344\">1.34.4-gke.1193000</a></li>\n</ul></li>\n</ul></li>\n</ul>\n\n\n</section>\n<section>\n  <h3>No channel</h3>\n  <aside class=\"note\"><strong>Note</strong>: Your clusters might not have these versions available.\nRollouts are already in progress when we publish the release notes, and can take\nmultiple days to complete across all Google Cloud zones.</aside>\n  \n\n<ul>\n<li>Version <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1351\">1.35.1-gke.1396002</a> is now the default version for cluster creation.</li>\n<li>The following versions are now available:\n<ul>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213\">1.32.13-gke.1147000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339\">1.33.9-gke.1166000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1345\">1.34.5-gke.1208000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352\">1.35.2-gke.1842000</a></li>\n</ul></li>\n<li>The following node versions are now available:\n<ul>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014\">1.30.14-gke.2250000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114\">1.31.14-gke.1634000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13213\">1.32.13-gke.1147000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1339\">1.33.9-gke.1166000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1345\">1.34.5-gke.1208000</a></li>\n<li><a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352\">1.35.2-gke.1842000</a></li>\n</ul></li>\n<li>The following versions are no longer available:\n<ul>\n<li>1.32.11-gke.1264000 is <a href=\"https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support\">deprecated</a>. This version will be removed in 90 days, or at the end of support, if sooner.</li>\n<li>1.33.5-gke.2392000 is <a href=\"https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support\">deprecated</a>. This version will be removed in 90 days, or at the end of support, if sooner.</li>\n<li>1.34.3-gke.1444000 is <a href=\"https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support\">deprecated</a>. This version will be removed in 90 days, or at the end of support, if sooner.</li>\n<li>1.35.1-gke.1396001 is <a href=\"https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support\">deprecated</a>. This version will be removed in 90 days, or at the end of support, if sooner.</li>\n</ul></li>\n<li>Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:\n<ul>\n<li>GKE upgrades clusters to the following new minor versions if there are no factors, such as <a href=\"https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions\">maintenance exclusions</a> or deprecated APIs, preventing upgrades:\n<ul>\n<li>1.31 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212\">1.32.12-gke.1127000</a></li>\n<li>1.32 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338\">1.33.8-gke.1026000</a></li>\n</ul></li>\n<li>GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has <a href=\"https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions\">maintenance exclusions</a> or other factors preventing minor version upgrades:\n<ul>\n<li>1.32 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v13212\">1.32.12-gke.1127000</a></li>\n<li>1.33 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1338\">1.33.8-gke.1026000</a></li>\n<li>1.34 to <a href=\"https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1344\">1.34.4-gke.1193000</a></li>\n</ul></li>\n</ul></li>\n</ul>\n\n\n</section>\n</devsite-selector>\n</div>",
    "product_name": "Google Kubernetes Engine",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>An issue has been fixed where the <strong>LookML dashboards</strong> folder could fail to display the complete list of LookML dashboards. This feature now performs as expected.</p>",
    "product_name": "Looker",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>An issue has been fixed where the LookML Assistant could return a 404 error. This feature now performs as expected.</p>",
    "product_name": "Looker",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p>An issue has been fixed where visualization tooltips on dashboards could use incorrect background or text colors. This feature now performs as expected.</p>",
    "product_name": "Looker",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Rapid7 InsightVm</strong>: Version 15.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Get Scan Results</strong></p></li>\n<li><p><strong>Launch Scan</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Tenable Security Center</strong>: Version 21.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Add IP To IP List Asset</strong></p></li>\n<li><p><strong>Create IP List Asset</strong></p></li>\n<li><p><strong>Get Report</strong></p></li>\n<li><p><strong>Get Scan Results</strong></p></li>\n<li><p><strong>Run Asset Scan</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Exchange</strong>: Version 122.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Save Mail Attachments To The Case</strong></p></li>\n<li><p><strong>Send Mail</strong></p></li>\n<li><p><strong>Send Thread Reply</strong></p></li>\n<li><p><strong>Send Vote Mail</strong></p></li>\n<li><p><strong>Wait for mail from user</strong></p></li>\n<li><p><strong>Wait for Vote Mail Results</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Azure API</strong>: Version 3.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Execute HTTP Request</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Cisco Threat Grid</strong>: Version 17.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Upload Sample</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Lastline</strong>: Version 8.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Search Analysis History</strong></p></li>\n<li><p><strong>Submit File</strong></p></li>\n<li><p><strong>Submit URL</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Cynet</strong>: Version 12.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Hash Query</strong></p></li>\n<li><p><strong>Remediation Status</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>AWS WAF</strong>: Version 11.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>List Rule Groups</strong></p></li>\n<li><p><strong>List Web ACLs</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Shodan</strong>: Version 16.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>DNS Resolve</strong></p></li>\n<li><p><strong>DNS Reverse</strong></p></li>\n<li><p><strong>Get Api Info</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Jira</strong>: Version 55.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Create Alert Issue</strong></p></li>\n<li><p><strong>Create Issue</strong></p></li>\n<li><p><strong>List Issues</strong></p></li>\n<li><p><strong>Update Issue</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Zoho Desk</strong>: Version 11.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Add Comment To Ticket</strong></p></li>\n<li><p><strong>Create Ticket</strong></p></li>\n<li><p><strong>Update Ticket</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Palo Alto Panorama</strong>: Version 35.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Add Ips to group</strong></p></li>\n<li><p><strong>Block ips in policy</strong></p></li>\n<li><p><strong>Block Urls</strong></p></li>\n<li><p><strong>Edit Blocked Applications</strong></p></li>\n<li><p><strong>Get Blocked Applications</strong></p></li>\n<li><p><strong>Remove Ips from group</strong></p></li>\n<li><p><strong>Unblock ips in policy</strong></p></li>\n<li><p><strong>Unblock Urls</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>FireEye NX</strong>: Version 11.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Download Alert Artifacts</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>FireEye AX</strong>: Version 8.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Get Appliance Details</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Microsoft Graph Mail Delegated</strong>: Version 16.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Forward Email</strong></p></li>\n<li><p><strong>Save Email to the Case</strong></p></li>\n<li><p><strong>Send Email</strong></p></li>\n<li><p><strong>Send Email HTML</strong></p></li>\n<li><p><strong>Send Thread Reply</strong></p></li>\n<li><p><strong>Send Vote Email</strong></p></li>\n<li><p><strong>Wait For Email From User</strong></p></li>\n<li><p><strong>Wait For Vote Email Results</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>VSphere</strong>: Version 11.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Get System Info</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>McAfee NSM</strong>: Version 10.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Get Alert Info Data</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>CyberArk PAM</strong>: Version 9.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Get Account Password Value</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Any.Run</strong>: Version 11.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>AnalyzeFile</strong></p></li>\n<li><p><strong>AnalyzeFileURL</strong></p></li>\n<li><p><strong>AnalyzeURL</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>BMC Remedy ITSM</strong>: Version 12.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Create Incident</strong></p></li>\n<li><p><strong>Create Record</strong></p></li>\n<li><p><strong>Wait For Incident Fields Update</strong></p></li>\n<li><p><strong>Wait For Record Fields Update</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Tanium</strong>: Version 18.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Create Question</strong></p></li>\n<li><p><strong>Download File</strong></p></li>\n<li><p><strong>Get Question Results</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Tor</strong>: Version 9.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Is Exit Node</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Salesforce</strong>: Version 17.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Get Case</strong></p></li>\n<li><p><strong>Search Records</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>QRadar</strong>: Version 66.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>QRadar AQL Search</strong></p></li>\n<li><p><strong>QRadar Simple AQL Search</strong></p></li>\n<li><p><strong>Update Offense</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Mimecast</strong>: Version 15.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Create Block Sender Policy</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>CrowdStrike Falcon</strong>: Version 75.0</p>\n\n<ul>\n<li><p>Added offline queueing support to the following actions:</p>\n\n<ul>\n<li><p><strong>Execute Command</strong></p></li>\n<li><p><strong>Run Script</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>EmailV2</strong>: Version 40.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Delete Email</strong></p></li>\n<li><p><strong>Forward Email</strong></p></li>\n<li><p><strong>Save Email Attachments To Case</strong></p></li>\n<li><p><strong>Send Email</strong></p></li>\n<li><p><strong>Send Thread Reply</strong></p></li>\n<li><p><strong>Wait for Email from User</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>SSH</strong>: Version 20.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>List Connections</strong></p></li>\n<li><p><strong>List iptables Rules</strong></p></li>\n<li><p><strong>List Processes</strong></p></li>\n<li><p><strong>Run Command</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Atlassian Confluence Server</strong>: Version 5.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Get Child Pages</strong></p></li>\n<li><p><strong>Get Page by ID</strong></p></li>\n<li><p><strong>Get Page Comments</strong></p></li>\n<li><p><strong>List Pages</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Symantec ICDX</strong>: Version 9.0</p>\n\n<ul>\n<li><strong>Integration</strong>: The integration&#39;s source code is now publicly available on\n<a href=\"https://github.com/chronicle/content-hub\">Github</a>.</li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>AWS Elastic Compute Cloud (EC2)</strong>: Version 10.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>List Instances</strong></p></li>\n<li><p><strong>List Security Groups</strong></p></li>\n<li><p><strong>Take Snapshot</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>CiscoUmbrella</strong>: Version 18.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Get Malicious Domains</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>SentinelOneV2</strong>: Version 47.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Create Device Control Rule</strong></p></li>\n<li><p><strong>Download Threat File</strong></p></li>\n<li><p><strong>Enrich Endpoint</strong></p></li>\n<li><p><strong>Get System Status</strong></p></li>\n<li><p><strong>Update Alert</strong></p></li>\n<li><p><strong>Update Device Control Rule</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Symantec ATP</strong>: Version 12.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Get Incident Comments</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Trend Vision One</strong>: Version 8.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Execute Email</strong></p></li>\n<li><p><strong>Update Workbench Alert</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Service Desk Plus</strong>: Version 8.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Create Request</strong></p></li>\n<li><p><strong>Get Request</strong></p></li>\n<li><p><strong>Update Request</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>HTTP Rest API</strong>: Version 14.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Get Data</strong></p></li>\n<li><p><strong>Post Data</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>FireEye HX</strong>: Version 22.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Acknowledge Alert Groups</strong></p></li>\n<li><p><strong>Get Indicator</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>FireEye CM</strong>: Version 14.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Add IOC Feed</strong></p></li>\n<li><p><strong>Download Alert Artifacts</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Rapid7 InsightIDR</strong>: Version 12.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Create Saved Query</strong></p></li>\n<li><p><strong>Set Investigation Assignee</strong></p></li>\n<li><p><strong>Set Investigation Status</strong></p></li>\n<li><p><strong>Update Investigation</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>SiemplifyUtilities</strong>: Version 28.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Delete File</strong></p></li>\n<li><p><strong>Filter JSON</strong></p></li>\n<li><p><strong>Get Deployment URL</strong></p></li>\n<li><p><strong>List Operations</strong></p></li>\n<li><p><strong>Parse EML to JSON</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Carbon Black Protection</strong>: Version 12.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><strong>Get System Info</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>AlienVault USM Anywhere</strong>: Version 35.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Get Alarm Details</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Intezer</strong>: Version 13.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Get Alert</strong></p></li>\n<li><p><strong>Submit Alert</strong></p></li>\n<li><p><strong>Submit File</strong></p></li>\n<li><p><strong>Submit Suspicious Email</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>AlgoSec</strong>: Version 7.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Allow IP</strong></p></li>\n<li><p><strong>Block IP</strong></p></li>\n<li><p><strong>Wait for Change Request Status Update</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Sumo Logic Cloud SIEM</strong>: Version 12.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Add Tags To Insight</strong></p></li>\n<li><p><strong>Add Comment To Insight</strong></p></li>\n<li><p><strong>Update Insight</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>RSA NetWitness Platform</strong>: Version 16.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Update Incident</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Akamai</strong>: Version 5.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Activate Client List</strong></p></li>\n<li><p><strong>Activate Network List</strong></p></li>\n<li><p><strong>Add Items To Network List</strong></p></li>\n<li><p><strong>Remove Items From Network List</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Palo Alto Prisma Cloud</strong>: Version 6.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Enrich Assets</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Google Kubernetes Engine</strong>: Version 9.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Get Operation Status</strong></p></li>\n<li><p><strong>List Clusters</strong></p></li>\n<li><p><strong>List Node Pools</strong></p></li>\n<li><p><strong>List Operations</strong></p></li>\n<li><p><strong>Set Cluster Addons</strong></p></li>\n<li><p><strong>Set Cluster Labels</strong></p></li>\n<li><p><strong>Set Node Autoscaling</strong></p></li>\n<li><p><strong>Set Node Count</strong></p></li>\n<li><p><strong>Set Node Pool Management</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Cybereason</strong>: Version 24.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Get Malop</strong></p></li>\n<li><p><strong>List Malop Processes</strong></p></li>\n<li><p><strong>List Reputation Items</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Cisco AMP</strong>: Version 22.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Create Group</strong></p></li>\n<li><p><strong>Get File Lists By Policy</strong></p></li>\n<li><p><strong>Get Groups</strong></p></li>\n<li><p><strong>Get Policies</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Solar Winds Orion</strong>: Version 7.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Enrich Endpoint</strong></p></li>\n<li><p><strong>Execute Entity Query</strong></p></li>\n<li><p><strong>Execute Query</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>WMI</strong>: Version 14.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>GetSystemInfo</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Cuckoo</strong>: Version 13.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Detonate File</strong></p></li>\n<li><p><strong>Get Report</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>MalShare</strong>: Version 10.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Upload File</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>CyberArk Credential Provider</strong>: Version 3.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Get Application Password Value</strong></p></li>\n<li><p><strong>Run CLI Application Password SDK Command</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>HashiCorp Vault</strong>: Version 6.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Generate AWS Credentials</strong></p></li>\n<li><p><strong>List AWS Roles</strong></p></li>\n<li><p><strong>List Key-Value Secret Keys</strong></p></li>\n<li><p><strong>Read Key-Value Secret</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Tenable.io</strong>: Version 16.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Scan Endpoints</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Redis</strong>: Version 8.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Add To List</strong></p></li>\n<li><p><strong>Get List</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>CSV</strong>: Version 40.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for the predefined widget of the following\naction:</p>\n\n<ul>\n<li><strong>Save Json To CSV</strong></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Google Translate</strong>: Version 6.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Translate Text</strong></p></li>\n<li><p><strong>List Languages</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>ConnectWise</strong>: Version 21.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Add Attachment To Ticket</strong></p></li>\n<li><p><strong>Get Ticket</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Zendesk</strong>: Version 12.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Get Ticket Details</strong></p></li>\n<li><p><strong>Search Tickets</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>ServiceNow</strong>: Version 62.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Add Comment To Record</strong></p></li>\n<li><p><strong>Add Parent Incident</strong></p></li>\n<li><p><strong>Create Alert Incident</strong></p></li>\n<li><p><strong>Create Incident</strong></p></li>\n<li><p><strong>Create Record</strong></p></li>\n<li><p><strong>Get Incident</strong></p></li>\n<li><p><strong>Get Oauth Token</strong></p></li>\n<li><p><strong>Get Record Details</strong></p></li>\n<li><p><strong>Update Incident</strong></p></li>\n<li><p><strong>Update Record</strong></p></li>\n<li><p><strong>Wait For Field Update</strong></p></li>\n<li><p><strong>Wait For Status Update</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>BMC Helix Remedyforce</strong>: Version 17.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Create Record</strong></p></li>\n<li><p><strong>Wait For Fields Update</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Anomali ThreatStream</strong>: Version 14.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Get Related Associations</strong></p></li>\n<li><p><strong>Get Related Entities</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Slack</strong>: Version 29.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Build Block</strong></p></li>\n<li><p><strong>Create Channel</strong></p></li>\n<li><p><strong>Get User Details</strong></p></li>\n<li><p><strong>Get User Details By Id</strong></p></li>\n<li><p><strong>Rename Channel</strong></p></li>\n<li><p><strong>Wait For Reply</strong></p></li>\n<li><p><strong>Wait For Reply With Webhook</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Exchange Extension Pack</strong>: Version 13.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Add Domains to Exchange-Siemplify Mail Flow Rules</strong></p></li>\n<li><p><strong>Add Senders to Exchange-Siemplify Mail Flow Rule</strong></p></li>\n<li><p><strong>Purge Compliance Search Results</strong></p></li>\n<li><p><strong>Remove Domains from Exchange-Siemplify Mail Flow Rules</strong></p></li>\n<li><p><strong>Remove Senders from Exchange-Siemplify Mail Flow Rules</strong></p></li>\n<li><p><strong>Run Compliance Search</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>McAfee ATD</strong>: Version 16.0</p>\n\n<ul>\n<li><p>Introduced Light Theme compatibility for predefined widgets of the following\nactions:</p>\n\n<ul>\n<li><p><strong>Get Report</strong></p></li>\n<li><p><strong>Submit File</strong></p></li>\n</ul></li>\n</ul>",
    "product_name": "Google SecOps Marketplace",
    "published_at": "2026-03-25"
  },
  {
    "description": "<p><strong>Imagen generation GA endpoints deprecation</strong></p>\n\n<p>The following table describes image generation endpoints that are deprecated and\ntheir replacements. We recommend updating your model endpoints before June 30,\n2026, to avoid service disruption.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Discontinued endpoints</th>\n      <th>Recommended endpoint migration</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td><code>imagegeneration@002</code></td>\n      <td><code>gemini-2.5-flash-image</code></td>\n    </tr>\n    <tr>\n      <td><code>imagegeneration@003</code></td>\n      <td><code>gemini-2.5-flash-image</code></td>\n    </tr>\n    <tr>\n      <td><code>imagegeneration@004</code></td>\n      <td><code>gemini-2.5-flash-image</code></td>\n    </tr>\n    <tr>\n      <td><code>imagegeneration@005</code></td>\n      <td><code>gemini-2.5-flash-image</code></td>\n    </tr>\n    <tr>\n      <td><code>imagegeneration@006</code></td>\n      <td><code>gemini-2.5-flash-image</code></td>\n    </tr>\n    <tr>\n      <td><code>imagetext@001</code></td>\n      <td><code>gemini-2.5-flash-image</code></td>\n    </tr>\n    <tr>\n      <td><code>imagen-3.0-capability-001</code></td>\n      <td><code>gemini-2.5-flash-image</code></td>\n    </tr>\n    <tr>\n      <td><code>imagen-3.0-capability-002</code></td>\n      <td><code>gemini-2.5-flash-image</code></td>\n    </tr>\n    <tr>\n      <td><code>imagen-3.0-fast-generate-001</code></td>\n      <td><code>gemini-2.5-flash-image</code></td>\n    </tr>\n    <tr>\n      <td><code>imagen-3.0-generate-001</code></td>\n      <td><code>gemini-2.5-flash-image</code></td>\n    </tr>\n    <tr>\n      <td><code>imagen-3.0-generate-002</code></td>\n      <td><code>gemini-2.5-flash-image</code></td>\n    </tr>\n    <tr>\n      <td><code>imagen-4.0-fast-generate-001</code></td>\n      <td><code>gemini-2.5-flash-image</code></td>\n    </tr>\n    <tr>\n      <td><code>imagen-4.0-generate-001</code></td>\n      <td><code>gemini-2.5-flash-image</code></td>\n    </tr>\n    <tr>\n      <td><code>imagen-4.0-ultra-generate-001</code></td>\n      <td><code>gemini-2.5-flash-image</code></td>\n    </tr>\n  </tbody>\n</table>",
    "product_name": "Generative AI on Vertex AI",
    "published_at": "2026-03-24"
  },
  {
    "description": "<p><strong>Google Cloud CCaaS 4.12</strong></p>\n\n<p>We&#39;ve released version 4.12 of Google Cloud CCaaS.</p>\n\n<p>The timing of the update to your instance depends on the deployment schedule\nthat you have chosen. For more information, see <a href=\"https://cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules\">Deployment\nschedules</a>.</p>",
    "product_name": "Google Cloud Contact Center as a Service",
    "published_at": "2026-03-24"
  },
  {
    "description": "<p>You can now use the <a href=\"https://docs.cloud.google.com/bigquery/docs/reference/datatransfer/mcp\">BigQuery Data Transfer Service remote MCP\nserver</a> to enable AI agents to\ncreate, manage, and run data transfers. This feature is in\n<a href=\"https://cloud.google.com/products/#product-launch-stages\">Preview</a>.</p>",
    "product_name": "BigQuery",
    "published_at": "2026-03-24"
  },
  {
    "description": "<p>A new Confidential Space image (260300) is available.</p>",
    "product_name": "Confidential Space",
    "published_at": "2026-03-24"
  },
  {
    "description": "<p>You can manage Bigtable <a href=\"https://docs.cloud.google.com/bigtable/docs/tiered-storage\">tiered storage</a>\nconfiguration in Google Cloud console and view tiered storage metrics in\n<a href=\"https://docs.cloud.google.com/bigtable/docs/monitoring-instance#console-monitoring-resources\">system insights</a>.\nFor more information, see <a href=\"https://docs.cloud.google.com/bigtable/docs/managing-tables\">Create and manage tables</a>.</p>",
    "product_name": "Bigtable",
    "published_at": "2026-03-24"
  },
  {
    "description": "<p>Anywhere Cache has been renamed to Rapid Cache.</p>",
    "product_name": "Cloud Storage",
    "published_at": "2026-03-24"
  },
  {
    "description": "<p>New <a href=\"https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-version-clusters#supported-dataproc-image-versions\">Dataproc on Compute Engine subminor image versions</a>:</p>\n\n<ul>\n<li>2.1.112-debian11, 2.1.112-rocky8, 2.1.112-ubuntu20, 2.1.112-ubuntu20-arm</li>\n<li>2.2.80-debian12, 2.2.80-rocky9, 2.2.80-ubuntu22, 2.2.80-ubuntu22-arm</li>\n<li>2.3.27-debian12, 2.3.27-ml-ubuntu22, 2.3.27-rocky9, 2.3.27-ubuntu22, 2.3.27-ubuntu22-arm</li>\n</ul>",
    "product_name": "Dataproc",
    "published_at": "2026-03-24"
  },
  {
    "description": "<p>You can use the URL filtering service to filter your workload traffic by using\ndomain and Server Name Indication (SNI) information available in the egress\nHTTP(S) messages. For more information, see\n<a href=\"https://docs.cloud.google.com/firewall/docs/about-url-filtering\">URL filtering service overview</a>. This\nfeature is available in <strong>General Availability</strong>.</p>",
    "product_name": "Cloud NGFW",
    "published_at": "2026-03-24"
  },
  {
    "description": "<p>The Telemetry API supports trace ingestion of up to 2.4GB per minute for the\nfollowing regions:</p>\n\n<ul>\n<li>asia-east1, asia-northeast1, asia-southeast1, and asia-south1</li>\n<li>europe-west1, europe-west2, europe-west3, and europe-west4</li>\n<li>us-central1, us-east4, and us-west1.</li>\n</ul>\n\n<p>For all other regions, the Telemetry API supports trace ingestion of up to\n300 MB per minute.</p>\n\n<p>These regional byte-based quotas replace a global quota which limited the\nnumber of requests per minute. To learn more, see\n<a href=\"https://docs.cloud.google.com/trace/docs/quotas#telemetry-api-limits\">Telemetry API limits and quotas</a>.</p>",
    "product_name": "Cloud Trace",
    "published_at": "2026-03-24"
  },
  {
    "description": "<p>Cloud Router supports named sets in <a href=\"https://cloud.google.com/products#product-launch-stages\">Preview</a>\nfor BGP route policies. Named sets are used to group together expressions of\neither communities or BGP prefixes, allowing them to be managed or\nreferenced as a single entity. For more information, see\n<a href=\"https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-route-policies-overview#what-are-bgp-route-policies\">BGP route policies overview</a>.</p>",
    "product_name": "Cloud Router",
    "published_at": "2026-03-24"
  },
  {
    "description": "<p><strong>Generally available</strong>: The maximum throughput for a Hyperdisk Balanced High\nAvailability disk is increased to 2,400 MiB/s from 1,200 MiB/s.\nHyperdisk Balanced High Availability provides high availability block storage for\nmission-critical workloads by synchronously replicating data between two zones\nwithin a region.</p>\n\n<p>For more information, see <a href=\"https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced-ha\">Hyperdisk Balanced High Availability overview</a>.",
    "product_name": "Compute Engine",
    "published_at": "2026-03-24"
  },
  {
    "description": "<p>The Telemetry API&#39;s supports up to 60,000 metric-ingestion requests per minute\nper region. The regional quota replaces the global quota. To learn more, see\n<a href=\"https://docs.cloud.google.com/monitoring/quotas#telemetry-api-metric-limits\">Telemetry API quotas and limits for metric ingestion</a>.</p>",
    "product_name": "Cloud Monitoring",
    "published_at": "2026-03-24"
  },
  {
    "description": "<p><strong>Gemini Enterprise: Get insights with the Data Insights agent (GA with allowlist)</strong></p>\n\n<p>The Data Insights agent is a Made by Google agent that provides insights from\nyour BigQuery data.\nThis feature is available as a GA with allowlist.\nContact your Google Cloud <a href=\"https://cloud.google.com/contact\">sales representative</a> to access this\nfeature.</p>\n\n<p>For more information, see\n<a href=\"https://docs.cloud.google.com/gemini/enterprise/docs/data-agent\">Get insights with the Data Insights agent</a>.</p>",
    "product_name": "Gemini Enterprise",
    "published_at": "2026-03-24"
  },
  {
    "description": "<p><strong>Gemini Enterprise: Enhanced filtering for Microsoft OneDrive data stores (Preview)</strong></p>\n\n<p>You can configure filters for your Microsoft OneDrive data stores using either the Google Cloud console or the API. These filters allow you to define exactly which content is accessible to the Assistant by including or excluding specific OneDrive paths.</p>\n\n<p>This feature is in Public Preview. For more information, see <a href=\"https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-onedrive/set-up-data-store\">Set up a Microsoft OneDrive data store</a> and <a href=\"https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-onedrive/add-filters-to-onedrive-data-store\">Add filters to a Microsoft OneDrive data store</a>.</p>",
    "product_name": "Gemini Enterprise",
    "published_at": "2026-03-24"
  },
  {
    "description": "<p>The following issues were addressed in this release:</p>\n\n<ul>\n<li><p>Fixed an issue for Zendesk users where using click-to-dial from a private\nnote failed to display existing tickets for outbound calls, forcing agents\nto create new tickets.</p></li>\n<li><p>Fixed an issue for Brightspeed users where the CRM link in the agent adapter\ndidn&#39;t open during calls or chats.</p></li>\n<li><p>Fixed an issue where call recordings between agents and end-users didn&#39;t\nupload to Salesforce promptly.</p></li>\n<li><p>Fixed an issue where agents placing an outbound call couldn&#39;t select queues\nfrom their parent team.</p></li>\n<li><p>Fixed an issue where agent status durations continued to accrue even after\nagents logged out or went offline.</p></li>\n<li><p>Fixed an issue where web queue redirects didn&#39;t work with domains ending in\n<code>.today</code>.</p></li>\n<li><p>Fixed an issue in the <strong>Agent</strong> dashboard where team names with a forward\nslash displayed the HTML character entity (<code>&amp;#x2F;</code>) instead of the forward\nslash.</p></li>\n<li><p>Fixed an issue where changing agent status after completing wrap-up\ndisplayed the wrap-up screen instead of the new status.</p></li>\n<li><p>Fixed an issue where the default global contact list was missing, despite\nbeing enabled, preventing end-users from accessing this directory.</p></li>\n<li><p>Fixed an issue where virtual agent calls weren&#39;t recorded and uploaded to\nexternal storage even when call recording was turned on.</p></li>\n<li><p>Fixed an issue where outbound calls were incorrectly prompting for customer\nsatisfaction (CSAT) feedback when a menu was assigned.</p></li>\n<li><p>Fixed an issue where the French Canadian translation for &quot;wrap-up&quot; was\ninconsistent between the chat adapter and notes panel.</p></li>\n<li><p>Fixed an issue where filtering agents by Team on the Agents tab resulted in\nsignificant delays.</p></li>\n<li><p>Fixed an issue where users were unable to download reports from the virtual\nagent dashboard and chat history if the requested date range exceeded the\nstorage retention period.</p></li>\n<li><p>Fixed an issue where SMS, WhatsApp, and AMB queues that were copied from Web\nor IVR channels incorrectly inherited transfer restrictions, preventing\nagents from transferring chats.</p></li>\n<li><p>Fixed an issue where users were unable to upload a key when adding or\nediting a redaction platform under developer settings.</p></li>\n<li><p>Fixed an issue where call recording links were not being pushed to HubSpot\ncases as expected.</p></li>\n<li><p>Fixed an issue where agents intermittently failed to connect to incoming\ncalls and were immediately disconnected, causing calls to requeue or drop\nunexpectedly.</p></li>\n<li><p>Fixed an issue where chat and call queues appeared unavailable for transfers\nwhen destination agents reached maximum capacity or were in an unavailable\nstatus.</p></li>\n<li><p>Fixed an issue where toggling the Whisper Announcement or Countdown settings\nin Automatic Redirection would unintentionally disable the Customize\nGreetings Announcement option.</p></li>\n<li><p>Fixed an issue where callback selections made after a virtual agent handover\nwere not accurately reflected in downloadable reports.</p></li>\n<li><p>Fixed an issue where the <strong>Available</strong> filter didn&#39;t display agents that\nwere available to receive a transfer.</p></li>\n<li><p>Fixed an issue with Alvaria Workforce integrations where files were rejected\ndue to a random suffix added to the RECORDKEY value.</p></li>\n<li><p>Fixed an issue where two end-users could be connected simultaneously to a\nsingle agent during campaign calls.</p></li>\n<li><p>Fixed an issue where the inactive chat dismissal timer did not reset after a\nconversation was escalated from a virtual agent to a live agent queue.</p></li>\n<li><p>Fixed an issue where transcript metadata files were sometimes stored in the\nfolder for the following day instead of matching the transcript file date,\nensuring all metadata and transcript files are now consistently organized by\nthe correct chat end date.</p></li>\n<li><p>Fixed an issue where agents appeared available but were unable to receive or\nbe re-offered calls due to repeated WebSocket presence updates and\nconnection expirations.</p></li>\n<li><p>Fixed an issue where Direct Access Points configured with SIP URIs\ncontaining spaces or non-standard formats failed to route calls correctly.</p></li>\n<li><p>Fixed an issue where the Agents tab filter in the UJET Portal displayed &quot;All\nundefined&quot; and was unclickable, preventing manual agent selection.</p></li>\n<li><p>Fixed an issue where managers could access queue reports requested by other\nmanagers, even if they were not involved in the relevant queues.</p></li>\n<li><p>Fixed an issue where searching by Location on the Users &amp; Teams page could\nreturn agents who no longer matched the search criteria. Search results now\naccurately reflect current agent locations.</p></li>\n<li><p>Fixed an issue where users did not see a message indicating that no time\nslots were available when selecting a queue with no available time slots.</p></li>\n<li><p>Fixed an issue where the fetch time slots endpoint incorrectly included\nnon-working days when calculating available future time slots.</p></li>\n<li><p>Fixed an issue where call recordings failed to convert from MP3 to WAV,\npreventing playback in Call Quality Assurance tools that require WAV format.</p></li>\n<li><p>Fixed an issue where, after a warm call transfer, if Agent 1 left the call\nand Agent 2 resumed the conversation, there was no audio between Agent 2 and\nthe end user.</p></li>\n<li><p>Fixed a 500 Internal Server Error that occurred when administrators tried to\nadd a new language (for example, Danish) under the &quot;Languages and Message&quot;\nsettings. This error prevented the language from being added to the list.</p></li>\n<li><p>Fixed an issue where the chat widget landmark was missing an accessible\nlabel. The chat widget now includes an aria-label matching the chat button\nlabel.</p></li>\n<li><p>We have updated the session metadata to provide a strict distinction between\nEscalations and Transfers. This ensures that reporting accurately reflects\nthe business context of how a session moves between resources. The session\nmetadata will now categorize these events as follows:</p>\n\n<ul>\n<li><p><strong>Escalation</strong>: Recorded only when a Virtual Agent transfers a session\nto a Human Agent.</p></li>\n<li><p><strong>Transfer</strong>: Recorded for all other routing scenarios, including:</p>\n\n<ul>\n<li><p>Human Agent &gt; Human Agent</p></li>\n<li><p>Virtual Agent &gt; Virtual Agent (Support or Task)</p></li>\n<li><p>Human Agent &gt; Virtual Agent</p></li>\n</ul></li>\n</ul></li>\n<li><p>Fixed an issue where updating a contact&#39;s mobile phone number during an\ninteraction would incorrectly overwrite the existing phone number field.</p></li>\n<li><p>Fixed an issue where chats that ended due to end user timeout or\ndisconnection were incorrectly shown as &quot;undefined&quot; in the Interaction\nOutcome column of platform reports.</p></li>\n<li><p>Fixed an issue in WFM data where the handle count was showing incorrect\ninformation if a chat spanned multiple intervals.</p></li>\n<li><p>Fixed a data discrepancy in NICE WFM interval reports where chat metrics\n(specifically ContactsReceived and HandledLong) were incorrectly showing\nactivity during time intervals where no chats actually occurred.</p></li>\n<li><p>Fixed an issue where calls transferred using warm transfer to another queue\nwere incorrectly deflected due to overcapacity, resulting in a cold transfer\ninstead.</p></li>\n<li><p>Fixed an issue where agents with multiple custom roles were incorrectly\nprevented from changing to certain statuses due to role restriction logic.</p></li>\n<li><p>Fixed an issue where changing the &quot;Custom After Hours Deflection&quot; setting in\nqueue configuration would incorrectly reset wrap up settings from &quot;Queue&quot; to\n&quot;Global.&quot;</p></li>\n<li><p>Fixed an issue where users with custom roles and correct permissions for\nQueues were unable to add teams.</p></li>\n<li><p>Fixed an issue where the right-side columns on the outbound phone numbers\npage were not visible and could not be accessed when the browser window was\ntoo small.</p></li>\n<li><p>Fixed a web SDK issue where the chat modal on Android Chrome was not\nrecognized by screen readers due to a missing dialog role.</p></li>\n<li><p>Fixed a web SDK issue where elements behind the Text size menu overlay were\nfocusable, ensuring that keyboard focus now remains on the Text size menu\nuntil it is dismissed by the user.</p></li>\n<li><p>Fixed a web SDK issue where the &quot;Request a call&quot; option in the chat widget\nwas not accessible to screen reader or keyboard-only users.</p></li>\n<li><p>Fixed an issue where agents were incorrectly presented with a manual\n&quot;Answer&quot; button and placed in &quot;Missed Call&quot; status after a single missed\nDeltacast, even when auto answer was enabled.</p></li>\n<li><p>Fixed an issue where transferring a direct outbound call to a queue could\nfail with a &quot;Not Found&quot; error, even when the target menu and agents were\navailable.</p></li>\n<li><p>Fixed an issue where the disposition list was not displaying in the\nconfigured custom order and instead appeared alphabetically in both Agent\nDesktop and standard Agent Adapter.</p></li>\n<li><p>Fixed an issue where the user inactivity timeout setting did not\nconsistently log out users as configured.</p></li>\n<li><p>Fixed an issue where queue channels and menu options would intermittently\ndisappear or fail to load correctly due to delays in feature flag\ninitialization.</p></li>\n<li><p>Fixed an issue where adding multiple agents to a team would fail if any\nselected user was already a member, resulting in a vague error and no agents\nbeing added.</p></li>\n<li><p>Fixed an issue in Progressive Campaigns where agents were intermittently\nconnected to two outbound call targets simultaneously. This occurred when a\ndial attempt terminated immediately but failed to detach from the conference\nbridge before the next attempt connected.</p></li>\n<li><p>Fixed an issue where deleting a queue that was the target of an automatic\nredirection could cause transfer options to fail to load for agents.</p></li>\n<li><p>Fixed an issue where adding multiple agents to a team would fail if any\nselected user was already a member, resulting in a vague error and no agents\nbeing added. </p></li>\n<li><p>Fixed the following issues that occurred with dual-channel and segmented\ncall recordings:</p>\n\n<ul>\n<li><p>Calls escalated from virtual agents weren&#39;t being recorded properly.</p></li>\n<li><p>Recordings of conversations with transferred agents were missing.</p></li>\n</ul></li>\n<li><p>Fixed an issue where chats escalated from a virtual agent to a human agent\nqueue were incorrectly set to auto answer.</p></li>\n<li><p>Fixed an issue where the call recording warning message didn&#39;t play for\ncallbacks initiated by virtual agent escalation when the destination queue\nexceeded capacity.</p></li>\n<li><p>Fixed an issue where search results in the <strong>Directory</strong> tab of the\n<strong>Transfer/Add party</strong> screen in the call adapter persisted after closing\nand reopening the screen.</p></li>\n<li><p>Fixed an issue where the call adapter displayed an error when the <strong>Call</strong>\nbutton was clicked.</p></li>\n<li><p>Fixed an issue where uploading an automatic-redirection audio recording in\none IVR queue caused the recording to incorrectly appear in a different IVR\nqueue.</p></li>\n<li><p>Fixed an issue where custom agent statuses restricted to specific roles\nweren&#39;t visible to users assigned those roles.</p></li>\n<li><p>Fixed an issue where contacts added to an outbound campaign using the\n<code>/outbound_dialer/campaigns/CAMPAIGN_ID/contacts</code> endpoint weren&#39;t dialed.</p></li>\n<li><p>Fixed an issue where users who authenticated with Single Sign-On (SSO)\ncouldn&#39;t update their profiles due to an invalid password error.</p></li>\n<li><p>Fixed an issue where the queue list on the <strong>Settings <span aria-label=\"and then\">></span> Queues</strong>\npage didn&#39;t load for instances with a large number of queues.</p></li>\n<li><p>Fixed an issue where the interaction history in the agent adapter\nincorrectly displayed as empty.</p></li>\n<li><p>Fixed an issue where Salesforce account lookup settings couldn&#39;t be saved\nwhen selecting the <code>Person Account</code> object and record types.</p></li>\n<li><p>Fixed an issue in the chat adapter where the <strong>Previous Interactions</strong>\nsummary displayed duplicate section headings (<strong>Customer Satisfaction</strong> and\n<strong>Action</strong>) and an incorrect section heading (<strong>Label</strong>).</p></li>\n<li><p>Fixed an issue where team managers couldn&#39;t download agent reports when\nselecting the <strong>All Agents</strong> filter.</p></li>\n<li><p>Fixed an issue where the system didn&#39;t record the failure reason when a\nvirtual agent tried to escalate a chat to a human agent outside of\noperating hours.</p></li>\n<li><p>Fixed an issue where using the <strong>Bulk User Management</strong> tool to deactivate\nusers failed.</p></li>\n<li><p>Fixed an issue where the <strong>Monitoring Chat</strong> screen displayed chats\nincorrectly, with misaligned chat bubbles, incorrectly formatted bullets,\nand missing sender names and timestamps.</p></li>\n<li><p>Fixed an issue where the <strong>Directory</strong> screen in the call adapter appeared\nempty when an agent tried to start an internal call transfer to another\nagent.</p></li>\n<li><p>Fixed an issue where agent prioritization for deltacast selection was\nincorrect.</p></li>\n<li><p>Fixed an issue that occurred when a human agent didn&#39;t respond to a\ntransferred or auto-answered session. The system incorrectly recorded the\ntermination reason as &quot;agent stopped responding&quot; instead of &quot;timeout waiting\nfor agent message&quot;.</p></li>\n<li><p>Fixed a web SDK issue where underscores in text (for example, in email\naddresses like user_name@example.com) were incorrectly removed in messages\nto end-users.</p></li>\n<li><p>Fixed a web SDK issue for iOS users where the <strong>Yes</strong> and <strong>No</strong> buttons in\nthe survey request at the end of a chat were hidden.</p></li>\n</ul>",
    "product_name": "Google Cloud Contact Center as a Service",
    "published_at": "2026-03-24"
  },
  {
    "description": "<ul>\n<li>Added <a href=\"https://developers.google.com/earth-engine/datasets/catalog/overture-maps_places_place\">overture-maps/places_place</a>: Overture Maps - Places: Place",
    "product_name": "Earth Engine Data Catalog",
    "published_at": "2026-03-24"
  },
  {
    "description": "<p><strong>Callback fulfillment hours</strong></p>\n\n<p>You can configure callback fulfillment hours, which are the hours when your\ncontact center fulfills callbacks. If you enable callback rollovers to the next\nday, callbacks that are scheduled outside of these hours are rolled over to the\nnext day. If you don&#39;t enable callback rollovers, callbacks that are scheduled\noutside of these hours are canceled. Callback fulfillment hours aren&#39;t available\nby default. To use this capability, ask your Google contact to turn it on for\nyour instance. For more information, see <a href=\"https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#callback-fulfillment-hours\">Callback fulfillment\nhours</a>.</p>",
    "product_name": "Google Cloud Contact Center as a Service",
    "published_at": "2026-03-24"
  },
  {
    "description": "<p><strong>HubSpot lookup against company profiles</strong></p>\n\n<p>HubSpot integrations now support lookups against Company profiles.\nAdministrators can configure primary and secondary lookup objects, allowing the\nsystem to search for end-users across both Contacts and Companies to ensure\naccurate identification during active sessions.</p>\n\n<p>For more information, see <a href=\"https://docs.cloud.google.com/contact-center/ccai-platform/docs/hubspot-lookups\">HubSpot lookup against company\nprofiles</a>.",
    "product_name": "Google Cloud Contact Center as a Service",
    "published_at": "2026-03-24"
  },
  {
    "description": "<p><strong>Improved support for multiple agent matches for agent extension searches</strong></p>\n\n<p>When an end-user inputs an agent extension number at the beginning of a call and\nthere are multiple agent matches, the system now reads agent matches in groups\nof eight. This gets the end-user to the correct agent faster. We&#39;ve added the\nfollowing new extension directory messages to help guide the end-user to the\ncorrect agent:</p>\n\n<ul>\n<li><p>Multiple agents found</p></li>\n<li><p>Search results next page</p></li>\n<li><p>End of search results</p></li>\n</ul>\n\n<p>For more information, see <a href=\"https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#extension-directory-messages\">Extension directory\nmessages</a>.</p>",
    "product_name": "Google Cloud Contact Center as a Service",
    "published_at": "2026-03-24"
  },
  {
    "description": "<p><strong>Improved controls for predictive campaigns</strong></p>\n\n<p>We&#39;ve added the following controls to predictive campaigns to reduce the risk of\ncall abandonment due to overdialing. These controls let you ramp up dialing\nrates more naturally and consistently.</p>\n\n<ul>\n<li><p><strong>Max Calls Per Agent</strong></p></li>\n<li><p><strong>Target Agent Occupancy</strong></p></li>\n</ul>\n\n<p>We&#39;ve also made the <strong>Max Abandonment %</strong> setting optional, for campaigns that\ndon&#39;t require maintaining a maximum abandonment percentage.</p>\n\n<p>Administrators: When you click <strong>Campaigns <span aria-label=\"and then\">></span> Add Campaign\n  <span aria-label=\"and then\">></span> Mode <span aria-label=\"and then\">></span> Predictive</strong>, the new controls appear in the\n  <strong>Add Campaign</strong> dialog.</p>\n\n<p>For more information, see <a href=\"https://docs.cloud.google.com/contact-center/ccai-platform/docs/campaign-predictive\">Predictive\ncampaigns</a>.</p>",
    "product_name": "Google Cloud Contact Center as a Service",
    "published_at": "2026-03-24"
  },
  {
    "description": "<p><strong>Resume chat endpoint</strong></p>\n\n<p>You can use the new <code>chats/CHAT_ID/resume</code> endpoint to resume chat sessions that\nare in <code>dismissed</code> or <code>va_dismissed</code> status. Resumed chat sessions display the\nchat history to both the end-user and the agent.</p>\n\n<p>For more information, see\n<a href=\"https://docs.cloud.google.com/contact-center/ccai-platform/docs/resume-a-chat\">Resume a chat</a>.</p>",
    "product_name": "Google Cloud Contact Center as a Service",
    "published_at": "2026-03-24"
  },
  {
    "description": "<p><strong>Support for creating chat virtual agents using CX Agent Studio</strong></p>\n\n<p>Contact Center AI Platform supports creating chat virtual agents using\n<a href=\"https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps\">Customer Experience Agent Studio</a>\n(CX Agent Studio). This expands on its existing support for creating voice virtual\nagents with CX Agent Studio.</p>\n\n<p>For more information, see <a href=\"https://docs.cloud.google.com/contact-center/ccai-platform/docs/create-a-cx-agent-studio-agent\">Create and integrate Customer Experience Agent Studio\nagents</a>.</p>",
    "product_name": "Google Cloud Contact Center as a Service",
    "published_at": "2026-03-24"
  },
  {
    "description": "<p><strong>HubSpot: Mobile Phone Number Lookup</strong></p>\n\n<p>Admins can now enable mobile phone number lookups for HubSpot integrations to\nensure callers are accurately matched with existing contacts. To activate this,\nnavigate to <strong>Settings &gt; Developer Settings &gt; CRM</strong> and check the <strong>Mobile phone\nnumber lookup</strong> box in the new <strong>Phone Number Lookup</strong> section. Once enabled,\nthe system will automatically search both the &quot;Phone number&quot; and &quot;Mobile phone\nnumber&quot; fields in HubSpot during incoming voice or chat sessions. For more\ninformation, see <a href=\"https://docs.cloud.google.com/contact-center/ccai-platform/docs/hubspot-mobile-phone-lookup\">HubSpot mobile phone number\nlookup</a>.</p>",
    "product_name": "Google Cloud Contact Center as a Service",
    "published_at": "2026-03-24"
  },
  {
    "description": "<p><strong>Video generation GA endpoints deprecation</strong></p>\n\n<p>The following table describes video generation endpoints that are deprecated and\ntheir replacements. We recommend updating your model endpoints before June 30,\n2026, to avoid service disruption.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Discontinued endpoints</th>\n      <th>Recommended endpoint migration</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td><code>veo-3.0-generate-001</code></td>\n      <td><code>veo-3.1-generate-001</code></td>\n    </tr>\n    <tr>\n      <td><code>veo-3.0-fast-generate-001</code></td>\n      <td><code>veo-3.1-fast-generate-001</code></td>\n    </tr>\n    <tr>\n      <td><code>veo-2.0-generate-001</code></td>\n      <td><code>veo-3.1-generate-001</code></td>\n    </tr>\n  </tbody>\n</table>",
    "product_name": "Generative AI on Vertex AI",
    "published_at": "2026-03-24"
  },
  {
    "description": "<p><a href=\"https://cloud.google.com/products#product-launch-stages\">Preview stage</a> support\nfor the following integration:</p>\n\n<ul>\n<li><a href=\"https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_oracle_database\">Oracle Database@Google Cloud</a></li>\n</ul>",
    "product_name": "VPC Service Controls",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>Google Distributed Cloud (software only) for bare metal 1.33.600-gke.39 is now available for\ndownload. To upgrade, see <a href=\"how-to/upgrade\">Upgrade clusters</a>.\nGoogle Distributed Cloud for bare metal\n1.33.600-gke.39 runs on Kubernetes v1.33.5-gke.2200.</p>\n\n<p>After a release, it takes approximately 7 to 14 days for the version to become\navailable for installations or upgrades with the GKE On-Prem API clients: the\nGoogle Cloud console, the gcloud CLI, and Terraform.</p>\n\n<p>If you use a third-party storage vendor, check the Google Distributed Cloud-ready\nstorage partners document to make sure the storage vendor has already passed the\nqualification for this release of Google Distributed Cloud for bare metal.",
    "product_name": "Google Distributed Cloud (software only) for bare metal",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>Fixed KCTF-c9bc175 in the Linux kernel.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>Updated sys-libs/binutils-libs to 2.46.0. This resolves CVE-2025-69644.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>Fixed CVE-2026-23262 in the Linux kernel.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>Fixed CVE-2025-71268 in the Linux kernel.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>Fixed CVE-2026-23254 in the Linux kernel.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>Fixed KCTF-71e99ee in the Linux kernel.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>Updated net-misc/curl to v8.19.0. This resolves CVE-2026-1965 and CVE-2026-3783.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>Fixed CVE-2025-71265 in the Linux kernel.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>Fixed CVE-2025-22026 in the Linux kernel.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>Fixed CVE-2025-71266 in the Linux kernel.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>Upgraded sys-apps/file to v5.47-r1.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>Added support for 8th generation TPU devices.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>Fixed CVE-2025-69647 in binutils-libs.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>Upgraded chromeos-base/google-breakpad to v2026.03.03.162944-r270.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>Fixed CVE-2025-69648 in binutils-libs.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>Fixed CVE-2026-23243 in the Linux kernel.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p><strong>Gemini Enterprise: Data connector for Docusign (Preview)</strong></p>\n\n<p>You can connect Docusign data stores to Gemini Enterprise. </p>\n\n<p>Support for Docusign data stores is in Public Preview. For more information, see <a href=\"https://docs.cloud.google.com/gemini/enterprise/docs/connectors/docusign\">Connect Docusign</a>.</p>",
    "product_name": "Gemini Enterprise",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>Added CPU balloon support for Arm CPUs.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>Upgraded dev-libs/expat to v2.7.4.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>Fixed CVE-2024-26822 in the Linux kernel.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>Updated cos-gpu-installer to v2.6.1.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>Fixed CVE-2025-71267 in the Linux kernel.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p><strong>Preview</strong>: The instance flexibility policy of a managed instance group (MIG)\nlets you override the minimum CPU platform and disk definition that is specified\nin the MIG&#39;s instance template. With these overrides, you can select machine\ntypes that run on different CPU platforms and that have different architectures.</p>\n\n<p>For more information, see <a href=\"https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility#overrides-for-instance-properties\">About instance flexibility in MIGs</a>.</p>",
    "product_name": "Compute Engine",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>Fixed CVE-2026-23231 in the Linux kernel.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>You can now provide user-defined actions using <a href=\"https://docs.cloud.google.com/deploy/docs/tasks\"><code>tasks</code></a>.\nThis includes <a href=\"https://docs.cloud.google.com/deploy/docs/hooks\">deploy hooks</a>,\n<a href=\"https://docs.cloud.google.com/deploy/docs/verify-deployment\">deployment verification</a>,\n<a href=\"https://docs.cloud.google.com/deploy/docs/analysis\">analysis</a>, and <a href=\"https://docs.cloud.google.com/deploy/docs/custom-targets\">custom target types</a>.\nThis feature is\n<a href=\"https://cloud.google.com/products#product-launch-stages\">generally available</a>.</p>",
    "product_name": "Cloud Deploy",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>You can now <a href=\"https://docs.cloud.google.com/deploy/docs/analysis\">analyze the performance of your deployed applications</a>\nusing the monitoring platform of your choice and\n<a href=\"https://docs.cloud.google.com/deploy/docs/automation-rules\">automatically trigger actions</a>\nsuch as rollbacks. This feature is\n<a href=\"https://cloud.google.com/products#product-launch-stages\">generally available</a>.</p>",
    "product_name": "Cloud Deploy",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>Agent Assist offers <a href=\"https://docs.cloud.google.com/agent-assist/docs/tool-integration-for-ai-coach\">Gemini Enterprise for Customer Experience tools for AI coach</a> in GA. These tools enable virtual agents to connect with external systems to retrieve, update, format, or analyze information.</p>",
    "product_name": "Agent Assist",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p><a href=\"https://docs.cloud.google.com/document-ai/docs/custom-splitter\">Custom splitter</a> models\n<code>pretrained-splitter-v1.6-2026-03-09</code> and <code>pretrained-splitter-v1.6-pro-2026-03-09</code>\nare available in <a href=\"https://cloud.google.com/products/#product-launch-stages\">Preview</a>.</p>",
    "product_name": "Document AI",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>To enhance security, the <a href=\"https://docs.cloud.google.com/looker/docs/api-sdk\">Looker language SDKs</a> and the Looker API <a href=\"https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/ApiAuth/login\"><code>/login</code> endpoint</a> are being modified. They will exclusively accept passing credentials in the HTTP request body and will no longer support using URL query parameters.</p>\n\n<p><strong>Release date</strong>: This update is expected to take effect with the Looker 26.18 release in October 2026.</p>\n\n<p><strong>Potential impact</strong>: Any scripts or applications currently passing credentials in the URL query parameters in the Looker SDK libraries, or directly calling the <code>/login</code> API endpoint, will fail after this update.</p>\n\n<p><strong>Who is affected</strong>: All customers using Looker SDKs, custom scripts, or applications that call the <code>/login</code> API endpoint directly.</p>\n\n<p><strong>Action required</strong>:</p>\n\n<p>We have sent a message to your affected customers. However, to help avoid service disruptions, please recommend that they evaluate their environment and take the following actions before October 2026:</p>\n\n<ul>\n<li><strong>Upgrade SDKs:</strong> Upgrade the Looker SDKs to version 26.4 or later as soon as possible.</li>\n<li><strong>Update custom scripts:</strong> Modify any scripts or applications that rely on passing Looker API credentials in URL query parameters so that they will pass credentials in the HTTP request body.</li>\n<li><strong>Test the environment:</strong> Validate these changes in an environment that can identify these potential misconfigurations.</li>\n</ul>",
    "product_name": "Looker",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p><a href=\"https://docs.cloud.google.com/document-ai/docs/custom-classifier\">Custom classifier</a> models\n<code>pretrained-classifier-v1.6-2026-03-09</code> and <code>pretrained-classifier-v1.6-pro-2026-03-09</code>\nare available in <a href=\"https://cloud.google.com/products/#product-launch-stages\">Preivew</a>.</p>",
    "product_name": "Document AI",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p><strong>Billing account permissions now streamline access to Google payments\n profiles and payments accounts</strong></p>\n\n<p>We&#39;ve launched a billing IAM permissions update that simplifies\nand streamlines Cloud Billing account access to the associated\n<a href=\"https://docs.cloud.google.com/billing/docs/concepts#billing_account\">Google payments profiles and accounts</a>, for users who have the <code>billing.accounts.updatePaymentInfo</code> permission on their\nCloud Billing account.</p>\n\n<p><strong>Prior to this update</strong>: <em>While working in the Cloud Billing console</em>,\nto access and edit the associated Google payments profile and account\ninformation, all Cloud Billing account users <strong>needed <em>two</em> sets of\npermissions</strong>:</p>\n\n<ul>\n<li>Identity and Access Management (IAM)\n<a href=\"https://docs.cloud.google.com/billing/docs/how-to/billing-access\">permissions on the Cloud Billing account</a>\nto access and manage the billing account.</li>\n<li>Edit or Admin\n<a href=\"https://docs.cloud.google.com/billing/docs/how-to/modify-contacts#permissions\">access permissions on the associated Google payments profile</a>\nin order to add and edit payment methods, make a manual payment, and update\npayments profile info such as the business name, address,\ntax info, and payments account settings.</li>\n</ul>\n\n<p><strong>After this permissions update</strong>: Cloud Billing account users with\nthe <code>billing.accounts.updatePaymentInfo</code> permission on the billing account\ncan access and edit Google payments profile and account information\ndirectly from the Cloud Billing console, without needing additional permissions on the payments profile itself.\nThis includes users with the\n<a href=\"https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.admin\">Billing Account Administrator role</a>\n(<code>roles/billing.admin</code>) and those granted this permission via a\n<a href=\"https://docs.cloud.google.com/billing/docs/how-to/custom-roles#payment_information\">custom role</a>.</p>\n\n<p>Note that this permissions update applies only to Cloud Billing\naccounts associated with an\n<a href=\"https://docs.cloud.google.com/billing/docs/concepts#payments_profile_types\">Organization (or Business)</a>\nGoogle payments profile type. You can verify your account type on the\n<a href=\"https://console.cloud.google.com/billing/profile\">Payment settings</a>\npage in the Cloud Billing console.</p>\n\n<p>With the <code>billing.accounts.updatePaymentInfo</code> permission on the billing account,\nusers can do the following:</p>\n\n<ul>\n<li><a href=\"https://docs.cloud.google.com/billing/docs/how-to/view-history\">View payments history</a> and\n<a href=\"https://docs.cloud.google.com/billing/docs/how-to/get-invoice\">documents</a> related to the associated\nGoogle payments profile.</li>\n<li><a href=\"https://docs.cloud.google.com/billing/docs/how-to/payment-methods\">Add and edit payment methods</a> on a\nself-serve (online) billing account.</li>\n<li><a href=\"https://docs.cloud.google.com/billing/docs/how-to/manual-payment\">Make a manual payment</a> to a\nself-serve (online) billing account.</li>\n<li><a href=\"https://docs.cloud.google.com/billing/docs/how-to/modify-billing-account\">Update payments profile info</a>\nsuch as the business name, address, tax info, and payments\naccount settings.</li>\n</ul>\n\n<p>Billing account users with the <code>billing.accounts.updatePaymentInfo</code> permission\nwon&#39;t have the <em>Manage users</em> or <em>Admin with all permissions</em> level of access\non the Google payments profile. To <em>fully manage</em> a payments\nprofile and gain\n<a href=\"https://docs.cloud.google.com/billing/docs/how-to/modify-contacts#permissions\"><em>Manage users</em> and <em>Admin</em> permissions</a>, billing account users still require additional\n<a href=\"https://docs.cloud.google.com/billing/docs/how-to/modify-contacts\"><em>Google payments user permissions</em></a>\ngranted on the associated payments profile.",
    "product_name": "Cloud Billing",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>Secure tags with a <code>purpose-data</code> attribute specifying a VPC network or an\norganization now support VPC networks that are connected using VPC Network\nPeering. For more information, see\n<a href=\"https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview\">Secure tags for firewalls</a>.\nThis feature is available in <strong>General Availability</strong>.",
    "product_name": "Cloud NGFW",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>Added support for the Lustre 2.14.0_p249 drivers.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>Runtime sysctl changes:\n<ul>\n<li>Changed: net.ipv4.udp_mem: 188034   250714  376068 -&gt; 188034    250715  376068</li>\n</ul></p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>Regional and Multi-Regional endpoints for the Firestore API\nare now Generally Available (<a href=\"https://cloud.google.com/products#product-launch-stages\">GA</a>).\nYou can use a Regional or a Multi-Regional endpoint to ensure that your\napplication&#39;s requests are transmitted, stored and processed in the same region\nor multi-region as your database&#39;s location.</p>\n\n<p>To learn more, see the\n<a href=\"https://docs.cloud.google.com/firestore/native/docs/regional-endpoints\">Firestore regional endpoints</a>\nguide.</p>\n\n<p>You can also use\n<a href=\"https://docs.cloud.google.com/vpc/docs/about-accessing-regional-google-apis-endpoints\">Private Service Connect regional endpoints</a>\nand <a href=\"https://docs.cloud.google.com/vpc/docs/private-service-connect-backends\">Private Service Connect backends</a>\nto connect to the regional and the multi-regional endpoints of the\nFirestore API.</p>",
    "product_name": "Firestore",
    "published_at": "2026-03-23"
  },
  {
    "description": "<h3 id=\"cos-117-18613-534-44_\">cos-117-18613-534-44 <a id=&quot;cos-arm64-117-18613-534-44&quot;/></h3>\n\n<table class=pkg>\n  <tr>\n    <td>Kernel</td>\n    <td>Docker</td>\n    <td>Containerd</td>\n    <td><a href=\"https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus\">GPU Drivers</a></td>\n  </tr>\n  <tr>\n    <td><a href=\"https://cos.googlesource.com/third_party/kernel/+/e91b457d7df4624c595f612f65f6a2f2bc973df4\n\">COS-6.6.123</a></td>\n    <td>v24.0.9</td>\n    <td>v1.7.29</td>\n    <td><a href=\"https://storage.googleapis.com/cos-tools/18613.534.44/lakitu/gpu_driver_versions.textproto\">See List</a></td>\n  </tr>\n</table>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p><strong>New parser documentation now available</strong></p>\n\n<p>New parser documentation is available to help you ingest and normalize logs from the following sources:</p>\n\n<ul>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/umbrella-firewall\">Collect Cisco Umbrella Cloud Firewall logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/umbrella-ip\">Collect Cisco Umbrella IP logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/medigate-iot\">Collect Claroty xDome for Healthcare logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudm\">Collect CloudM logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/digitalguardian-edr\">Collect Digital Guardian EDR logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dnsfilter\">Collect DNSFilter logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dope-swg\">Collect Dope Security SWG logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/druva-backup\">Collect Druva Backup logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/efficientip-ddi\">Collect EfficientIP DDI logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/elastic-defend\">Collect Elastic Defend logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/elastic-winlogbeat\">Collect Elastic Windows Event Log Beats logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ergon-informatik-airlock-iam\">Collect Ergon Informatik Airlock IAM logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/eset-ioc\">Collect ESET Threat Intelligence logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-dcs\">Collect F5 Distributed Cloud Services logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-shape\">Collect F5 Shape logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-silverline\">Collect F5 Silverline logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/falco-ids\">Collect Falco IDS logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fastly-cdn\">Collect Fastly CDN logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/file-scanning-framework\">Collect File Scanning Framework logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-etp\">Collect FireEye ETP logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-hx-audit\">Collect FireEye HX Audit logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-nx-audit\">Collect FireEye NX Audit logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fivetran\">Collect Fivetran logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forcepoint-mail-relay\">Collect Forcepoint Mail Relay logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gitguardian-enterprise\">Collect GitGuardian Enterprise logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/looker-audit\">Collect Google Cloud Looker audit logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/guardicore-centra\">Collect Guardicore Centra logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hcl-bigfix\">Collect HCL BigFix logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hid-digitalpersona\">Collect HID DigitalPersona logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-as400\">Collect IBM AS/400 logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/informix\">Collect IBM Informix logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-maas360\">Collect IBM MaaS360 logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-mainframe-storage\">Collect IBM Mainframe Storage logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-openpages\">Collect IBM OpenPages logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-sam\">Collect IBM Security Access Manager logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-sim\">Collect IBM Security Identity Manager logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/iboss-webproxy\">Collect iBoss Web Proxy logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/intel471-watcher-alerts\">Collect Intel 471 Watcher Alerts logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/intel-ema\">Collect Intel Endpoint Management Assistant logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ionix\">Collect IONIX Attack Surface Management logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/island-browser\">Collect Island Enterprise Browser logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jamf-telemetry-v2\">Collect Jamf Protect Telemetry V2 logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/keycloak\">Collect Keycloak logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/kong-gateway\">Collect Kong Gateway logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/lenel-onguard\">Collect LenelS2 OnGuard logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/lookout-mobile-endpoint-security\">Collect Lookout Mobile Endpoint Security logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/lucid\">Collect Lucid audit logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/manage-engine-reporter-plus\">Collect ManageEngine Exchange Reporter Plus logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mandiant-custom-ioc\">Collect Mandiant Threat Intelligence Custom IOC logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/menlo-security\">Collect Menlo Security Isolation Platform (MSIP) logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/metabase\">Collect Metabase logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-defender-endpoint-ios\">Collect Microsoft Defender for Endpoint on iOS logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-dynamics-365\">Collect Microsoft Dynamics 365 User Activity logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-ias\">Collect Microsoft IAS / Network Policy Server (NPS) logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-nps\">Collect Microsoft Network Policy Server (NPS) logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/kubernetes-auth-proxy\">Collect OAuth2 Proxy logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/office-365-messagetrace\">Collect Office 365 Message Trace logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ipswitch-moveit-transfer\">Collect Progress MOVEit Transfer logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/arbor-sightline\">Collect Netscout Arbor Sightline logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mcafee-web-protection\">Collect Skyhigh Secure Web Gateway (On-Premises) logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/malwarebytes-edr\">Collect ThreatDown EDR logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trellix-hx-alerts\">Collect Trellix Endpoint Security (HX) alert logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trellix-hx-audit\">Collect Trellix Endpoint Security (HX) audit event logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trellix-hx-hosts\">Collect Trellix Endpoint Security (HX) host inventory logs</a></li>\n</ul>",
    "product_name": "Google SecOps",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>Regional and Multi-Regional endpoints for the Datastore API\nare now Generally Available (<a href=\"https://cloud.google.com/products#product-launch-stages\">GA</a>).\nYou can use a Regional or a Multi-Regional endpoint to ensure that your\napplication&#39;s requests are transmitted, stored and processed in the same region\nor multi-region as your database&#39;s location.</p>\n\n<p>To learn more, see the\n<a href=\"https://docs.cloud.google.com/datastore/docs/regional-endpoints\">Datastore regional endpoints</a>\nguide.</p>\n\n<p>You can also use\n<a href=\"https://docs.cloud.google.com/vpc/docs/about-accessing-regional-google-apis-endpoints\">Private Service Connect regional endpoints</a>\nand <a href=\"https://docs.cloud.google.com/vpc/docs/private-service-connect-backends\">Private Service Connect backends</a>\nto connect to the regional and the multi-regional endpoints of the\nDatastore API.</p>",
    "product_name": "Datastore",
    "published_at": "2026-03-23"
  },
  {
    "description": "<h3 id=\"cos-113-18244-582-47_\">cos-113-18244-582-47 <a id=&quot;cos-arm64-113-18244-582-47&quot;/></h3>\n\n<table class=pkg>\n  <tr>\n    <td>Kernel</td>\n    <td>Docker</td>\n    <td>Containerd</td>\n    <td><a href=\"https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus\">GPU Drivers</a></td>\n  </tr>\n  <tr>\n    <td><a href=\"https://cos.googlesource.com/third_party/kernel/+/824daafa5f157963eea76b8fc10de1d2df43be70\n\">COS-6.1.161</a></td>\n    <td>v24.0.9</td>\n    <td>v1.7.27</td>\n    <td><a href=\"https://storage.googleapis.com/cos-tools/18244.582.47/lakitu/gpu_driver_versions.textproto\">See List</a></td>\n  </tr>\n</table>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-23"
  },
  {
    "description": "<h3 id=\"cos-121-18867-381-45_\">cos-121-18867-381-45 <a id=&quot;cos-arm64-121-18867-381-45&quot;/></h3>\n\n<table class=pkg>\n  <tr>\n    <td>Kernel</td>\n    <td>Docker</td>\n    <td>Containerd</td>\n    <td><a href=\"https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus\">GPU Drivers</a></td>\n  </tr>\n  <tr>\n    <td><a href=\"https://cos.googlesource.com/third_party/kernel/+/d8086709417b04f7a79c84710f6bf3db42e87814\n\">COS-6.6.122</a></td>\n    <td>v27.5.1</td>\n    <td>v2.0.7</td>\n    <td><a href=\"https://storage.googleapis.com/cos-tools/18867.381.45/lakitu/gpu_driver_versions.textproto\">See List</a></td>\n  </tr>\n</table>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p><strong>New parser documentation now available</strong></p>\n\n<p>New parser documentation is available to help you ingest and normalize logs from the following sources:</p>\n\n<ul>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/umbrella-firewall\">Collect Cisco Umbrella Cloud Firewall logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/umbrella-ip\">Collect Cisco Umbrella IP logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/medigate-iot\">Collect Claroty xDome for Healthcare logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudm\">Collect CloudM logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/digitalguardian-edr\">Collect Digital Guardian EDR logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dnsfilter\">Collect DNSFilter logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dope-swg\">Collect Dope Security SWG logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/druva-backup\">Collect Druva Backup logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/efficientip-ddi\">Collect EfficientIP DDI logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/elastic-defend\">Collect Elastic Defend logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/elastic-winlogbeat\">Collect Elastic Windows Event Log Beats logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ergon-informatik-airlock-iam\">Collect Ergon Informatik Airlock IAM logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/eset-ioc\">Collect ESET Threat Intelligence logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-dcs\">Collect F5 Distributed Cloud Services logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-shape\">Collect F5 Shape logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-silverline\">Collect F5 Silverline logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/falco-ids\">Collect Falco IDS logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fastly-cdn\">Collect Fastly CDN logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/file-scanning-framework\">Collect File Scanning Framework logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-etp\">Collect FireEye ETP logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-hx-audit\">Collect FireEye HX Audit logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-nx-audit\">Collect FireEye NX Audit logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fivetran\">Collect Fivetran logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forcepoint-mail-relay\">Collect Forcepoint Mail Relay logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gitguardian-enterprise\">Collect GitGuardian Enterprise logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/looker-audit\">Collect Google Cloud Looker audit logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/guardicore-centra\">Collect Guardicore Centra logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hcl-bigfix\">Collect HCL BigFix logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hid-digitalpersona\">Collect HID DigitalPersona logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-as400\">Collect IBM AS/400 logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/informix\">Collect IBM Informix logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-maas360\">Collect IBM MaaS360 logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-mainframe-storage\">Collect IBM Mainframe Storage logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-openpages\">Collect IBM OpenPages logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-sam\">Collect IBM Security Access Manager logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-sim\">Collect IBM Security Identity Manager logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/iboss-webproxy\">Collect iBoss Web Proxy logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/intel471-watcher-alerts\">Collect Intel 471 Watcher Alerts logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/intel-ema\">Collect Intel Endpoint Management Assistant logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ionix\">Collect IONIX Attack Surface Management logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/island-browser\">Collect Island Enterprise Browser logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jamf-telemetry-v2\">Collect Jamf Protect Telemetry V2 logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/keycloak\">Collect Keycloak logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/kong-gateway\">Collect Kong Gateway logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/lenel-onguard\">Collect LenelS2 OnGuard logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/lookout-mobile-endpoint-security\">Collect Lookout Mobile Endpoint Security logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/lucid\">Collect Lucid audit logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/manage-engine-reporter-plus\">Collect ManageEngine Exchange Reporter Plus logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mandiant-custom-ioc\">Collect Mandiant Threat Intelligence Custom IOC logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/menlo-security\">Collect Menlo Security Isolation Platform (MSIP) logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/metabase\">Collect Metabase logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-defender-endpoint-ios\">Collect Microsoft Defender for Endpoint on iOS logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-dynamics-365\">Collect Microsoft Dynamics 365 User Activity logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-ias\">Collect Microsoft IAS / Network Policy Server (NPS) logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-nps\">Collect Microsoft Network Policy Server (NPS) logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/kubernetes-auth-proxy\">Collect OAuth2 Proxy logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/office-365-messagetrace\">Collect Office 365 Message Trace logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ipswitch-moveit-transfer\">Collect Progress MOVEit Transfer logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/arbor-sightline\">Collect Netscout Arbor Sightline logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mcafee-web-protection\">Collect Skyhigh Secure Web Gateway (On-Premises) logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/malwarebytes-edr\">Collect ThreatDown EDR logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trellix-hx-alerts\">Collect Trellix Endpoint Security (HX) alert logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trellix-hx-audit\">Collect Trellix Endpoint Security (HX) audit event logs</a></li>\n<li><a href=\"https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trellix-hx-hosts\">Collect Trellix Endpoint Security (HX) host inventory logs</a></li>\n</ul>",
    "product_name": "Google SecOps SIEM",
    "published_at": "2026-03-23"
  },
  {
    "description": "<h3 id=\"cos-125-19216-220-72_\">cos-125-19216-220-72 <a id=&quot;cos-arm64-125-19216-220-72&quot;/></h3>\n\n<table class=pkg>\n  <tr>\n    <td>Kernel</td>\n    <td>Docker</td>\n    <td>Containerd</td>\n    <td><a href=\"https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus\">GPU Drivers</a></td>\n  </tr>\n  <tr>\n    <td><a href=\"https://cos.googlesource.com/third_party/kernel/+/6df21e3fc3957bf2dc7eeb7d8e703fc57b1e07ac\n\">COS-6.12.68</a></td>\n    <td>v27.5.1</td>\n    <td>v2.1.5</td>\n    <td><a href=\"https://storage.googleapis.com/cos-tools/19216.220.72/lakitu/gpu_driver_versions.textproto\">See List</a></td>\n  </tr>\n</table>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>The following functions are now\n<a href=\"https://cloud.google.com/products#product-launch-stages\">generally available</a>\n(GA):</p>\n\n<ul>\n<li><a href=\"https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-embed\"><code>AI.EMBED</code></a>:\ncreate embeddings from text or image data.</li>\n<li><a href=\"https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-similarity\"><code>AI.SIMILARITY</code></a>:\ncompute the semantic similarity between pairs of text, pairs of images, or\nacross text and images.",
    "product_name": "BigQuery",
    "published_at": "2026-03-23"
  },
  {
    "description": "<h3 id=\"cos-dev-133-19633-0-0_\">cos-dev-133-19633-0-0 <a id=&quot;cos-arm64-dev-133-19633-0-0&quot;/></h3>\n\n<table class=pkg>\n  <tr>\n    <td>Kernel</td>\n    <td>Docker</td>\n    <td>Containerd</td>\n    <td><a href=\"https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus\">GPU Drivers</a></td>\n  </tr>\n  <tr>\n    <td><a href=\"https://cos.googlesource.com/third_party/kernel/+/788077df45931035984615c9958e274d89bd7e1f\n\">COS-6.12.76</a></td>\n    <td>v27.5.1</td>\n    <td>v2.2.1</td>\n    <td><a href=\"https://storage.googleapis.com/cos-tools/19633.0.0/lakitu/gpu_driver_versions.textproto\">See List</a></td>\n  </tr>\n</table>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>You can clean, transform, and enrich data from files in Cloud Storage and Google\nDrive in your BigQuery data preparations. For more information, see\n<a href=\"https://docs.cloud.google.com/bigquery/docs/data-prep-get-suggestions#open-data-prep-editor\">Prepare data with Gemini</a>.\nThis feature is <a href=\"https://cloud.google.com/products#product-launch-stages\">generally available</a>\n(GA).",
    "product_name": "BigQuery",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>Upgraded app-admin/google-osconfig-agent to v20260119.00.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>Google Distributed Cloud (software only) for VMware 1.33.600-gke.39 is now available\nfor download. To upgrade, see <a href=\"https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading.md\">Upgrade clusters</a>.\nGoogle Distributed Cloud 1.33.600-gke.39 runs on Kubernetes v1.33.5-gke.2200.</p>\n\n<p>If you are using a third-party storage vendor, check the Google Distributed Cloud-ready\nstorage partners document to make sure the storage vendor has already passed the\nqualification for this release.</p>\n\n<p>After a release, it takes approximately 7 to 14 days for the version to become\navailable for use with GKE On-Prem API clients: the Google Cloud console, the\ngcloud CLI, and Terraform.</p>",
    "product_name": "Google Distributed Cloud (software only) for VMware",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>The following issues were fixed in 1.33.600-gke.39:</p>\n\n<ul>\n<li>Fixed an issue where the node-problem-detector was incorrectly deployed onto\nnon-Advanced (V1) VMware clusters, causing the containerd runtime to\ncontinuously restart on affected nodes, leading to ETCD/CRI failures and\nunsuccessful cluster upgrades.</li>\n<li>Fixed an issue where setting the deprecated stackdriver.enableVPC field to\ntrue in a cluster configuration file would block upgrades to an Advanced\nCluster. The stackdriver.enableVPC field has been deprecated and its setting is\nnow ignored during the upgrade validation process.</li>\n<li>Fixes an issue where Advanced Clusters incorrectly deployed the node problem\ndetector onto non-Advanced clusters, which caused containerd to continuously\nrestart and led to cluster upgrade failures.</li>\n<li>Fixed an issue where retrying the <code>gkectl upgrade admin</code> command after a\nprevious failure could fail with &quot;AlreadyExists&quot; errors in the bootstrap cluster.</li>\n<li>Fixed an issue where cluster creation or upgrade failed if the proxy or\nnoProxy configuration fields contained extraneous whitespaces. These spaces\ninterfered with internal command-line argument parsing, causing the control\nplane load balancer initialization to fail.</li>\n<li>Fixed an issue where the system certificate pool was ignored when a custom CA\ncertificate was configured for a registry mirror.</li>\n</ul>",
    "product_name": "Google Distributed Cloud (software only) for VMware",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>The following issues were fixed in 1.33.600-gke.39:</p>\n\n<ul>\n<li>Resolved an issue where Certificate Authority (CA) rotation became stuck\non self-managed clusters (admin, hybrid, or standalone). This fix resolves an\ninternal resource synchronization error that previously prevented the rotation\nprocess from completing successfully.\n</li>\n<li>Fixed vulnerabilities listed in <a href=\"https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history\">Vulnerability fixes</a>.</li>\n</ul>",
    "product_name": "Google Distributed Cloud (software only) for bare metal",
    "published_at": "2026-03-23"
  },
  {
    "description": "<p>Upgraded net-firewall/iptables to v1.8.13.</p>",
    "product_name": "Container Optimized OS",
    "published_at": "2026-03-23"
  }
]
```
- ( 2026-03-29 23:12:34 )
```bash
(my-agents) jazzwang_tw@cloudshell:~/my-agents (jazz-adk-labs)$ adk run gcp_releasenotes_agent_app/
Log setup complete: /tmp/agents_log/agent.20260329_150832.log
To access latest log: tail -F /tmp/agents_log/agent.latest.log
/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/google/adk/cli/cli.py:204: UserWarning: [EXPERIMENTAL] InMemoryCredentialService: This feature is experimental and may change or be removed in future versions without notice. It may introduce breaking changes at any time.
  credential_service = InMemoryCredentialService()
/home/jazzwang_tw/my-agents/.venv/lib/python3.12/site-packages/google/adk/auth/credential_service/in_memory_credential_service.py:33: UserWarning: [EXPERIMENTAL] BaseCredentialService: This feature is experimental and may change or be removed in future versions without notice. It may introduce breaking changes at any time.
  super().__init__()
Running agent gcp_releasenotes_agent, type exit to exit.
[user]: get me the lastest 3 google cloud release notes          
[gcp_releasenotes_agent]: Here are the latest 3 Google Cloud release notes:

1.  **Product Name:** Google Distributed Cloud (software only) for VMware
    **Description:** The following issues were fixed in 1.33.600-gke.40:
    *   Fixed an issue where if updates or upgrades to advanced admin clusters failed and the external bootstrap cluster was deleted, you could lose critical data.
    **Published At:** 2026-03-27

2.  **Product Name:** Google Distributed Cloud (software only) for bare metal
    **Description:** Google Distributed Cloud (software only) for bare metal 1.32.1000-gke.57 is now available for download. To upgrade, see Upgrade clusters. Google Distributed Cloud for bare metal 1.32.1000-gke.57 runs on Kubernetes v1.32.13-gke.1000.

    After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.

    If you use a third-party storage vendor, check the Google Distributed Cloud-ready storage partners document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.
    **Published At:** 2026-03-27

3.  **Product Name:** Google Distributed Cloud (software only) for VMware
    **Description:** Google Distributed Cloud (software only) for VMware 1.33.600-gke.40 is now available for download. To upgrade, see Upgrade clusters. Google Distributed Cloud 1.33.600-gke.40 runs on Kubernetes 1.33.5-gke.2200.

    If you are using a third-party storage vendor, check the Google Distributed Cloud-ready storage partners document to make sure the storage vendor has already passed the qualification for this release.

    After a release, it takes approximately 7 to 14 days for the version to become available for use with GKE On-Prem API clients: the Google Cloud console, the gcloud CLI, and Terraform.
    **Published At:** 2026-03-27
[user]: 
[user]: exit
(my-agents) jazzwang_tw@cloudshell:~/my-agents (jazz-adk-labs)$ 
```
```bash
jazzwang_tw@cloudshell:~$ tail -F /tmp/agents_log/agent.latest.log
2026-03-29 15:01:56,805 - INFO - agent_loader.py:131 - Found root_agent in gcp_releasenotes_agent_app.agent
2026-03-29 15:01:56,806 - INFO - envs.py:83 - Loaded .env file for gcp_releasenotes_agent_app at /home/jazzwang_tw/my-agents/gcp_releasenotes_agent_app/.env
2026-03-29 15:01:56,806 - INFO - local_storage.py:84 - Using per-agent session storage rooted at /home/jazzwang_tw/my-agents
2026-03-29 15:01:56,808 - INFO - local_storage.py:110 - Using file artifact service at /home/jazzwang_tw/my-agents/gcp_releasenotes_agent_app/.adk/artifacts
2026-03-29 15:01:56,809 - INFO - service_factory.py:266 - Using in-memory memory service
2026-03-29 15:01:56,886 - INFO - local_storage.py:60 - Creating local session service at /home/jazzwang_tw/my-agents/gcp_releasenotes_agent_app/.adk/session.db
2026-03-29 15:05:57,370 - INFO - google_llm.py:185 - Sending out request, model: gemini-2.5-flash, backend: GoogleLLMVariant.VERTEX_AI, stream: False
2026-03-29 15:05:59,141 - INFO - google_llm.py:250 - Response received from the model.
2026-03-29 15:05:59,141 - WARNING - types.py:7900 - Warning: there are non-text parts in the response: ['function_call'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.
2026-03-29 15:06:01,615 - INFO - google_llm.py:185 - Sending out request, model: gemini-2.5-flash, backend: GoogleLLMVariant.VERTEX_AI, stream: False
tail: '/tmp/agents_log/agent.latest.log' has been replaced;  following new file
2026-03-29 15:08:32,458 - INFO - envs.py:83 - Loaded .env file for gcp_releasenotes_agent_app at /home/jazzwang_tw/my-agents/gcp_releasenotes_agent_app/.env
2026-03-29 15:08:32,568 - WARNING - client.py:83 - A newer version of MCP (2025-11-25) is available. Please use Protocol.MCP_LATEST to use the latest features.
2026-03-29 15:08:32,574 - INFO - agent_loader.py:131 - Found root_agent in gcp_releasenotes_agent_app.agent
2026-03-29 15:08:32,576 - INFO - envs.py:83 - Loaded .env file for gcp_releasenotes_agent_app at /home/jazzwang_tw/my-agents/gcp_releasenotes_agent_app/.env
2026-03-29 15:08:32,576 - INFO - local_storage.py:84 - Using per-agent session storage rooted at /home/jazzwang_tw/my-agents
2026-03-29 15:08:32,577 - INFO - local_storage.py:110 - Using file artifact service at /home/jazzwang_tw/my-agents/gcp_releasenotes_agent_app/.adk/artifacts
2026-03-29 15:08:32,577 - INFO - service_factory.py:266 - Using in-memory memory service
2026-03-29 15:08:32,583 - INFO - local_storage.py:60 - Creating local session service at /home/jazzwang_tw/my-agents/gcp_releasenotes_agent_app/.adk/session.db
2026-03-29 15:09:13,183 - INFO - google_llm.py:185 - Sending out request, model: gemini-2.5-flash, backend: GoogleLLMVariant.VERTEX_AI, stream: False
2026-03-29 15:09:15,057 - INFO - google_llm.py:250 - Response received from the model.
2026-03-29 15:09:15,057 - WARNING - types.py:7900 - Warning: there are non-text parts in the response: ['function_call'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.
2026-03-29 15:09:17,211 - INFO - google_llm.py:185 - Sending out request, model: gemini-2.5-flash, backend: GoogleLLMVariant.VERTEX_AI, stream: False
2026-03-29 15:09:27,285 - INFO - google_llm.py:250 - Response received from the model.
2026-03-29 15:13:00,057 - INFO - runners.py:1571 - Closing runner...
2026-03-29 15:13:00,057 - INFO - runners.py:1579 - Runner closed.
```
```bash
jazzwang_tw@cloudshell:~/mcp-toolbox (jazz-adk-labs)$ ./toolbox --tools-file "tools.yaml" --ui
2026-03-29T15:00:06.546246577Z INFO "Initialized 1 sources: my-bq-source" 
2026-03-29T15:00:06.546394653Z INFO "Initialized 0 authServices: " 
2026-03-29T15:00:06.546431896Z INFO "Initialized 1 tools: search_release_notes_bq" 
2026-03-29T15:00:06.546480874Z INFO "Initialized 2 toolsets: my_bq_toolset, default" 
2026-03-29T15:00:06.546498525Z INFO "Initialized 0 prompts: " 
2026-03-29T15:00:06.546517152Z INFO "Initialized 1 promptsets: default" 
2026-03-29T15:00:06.546548996Z WARN "wildcard (`*`) allows all origin to access the resource and is not secure. Use it with cautious for public, non-sensitive data, or during local development. Recommended to use `--allowed-origins` flag to prevent DNS rebinding attacks" 
2026-03-29T15:00:06.55170671Z INFO "Server ready to serve!" 
2026-03-29T15:00:06.55174007Z INFO "Toolbox UI is up and running at: http://127.0.0.1:5000/ui" 
2026-03-29T15:00:13.727318717Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/?authuser=0" method: "GET" path: "/" remoteIP: "127.0.0.1:55148" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000001"} httpResponse: {status: 200 bytes: 23 elapsed: 0.015062} 
2026-03-29T15:00:17.304698274Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui" method: "GET" path: "/ui" remoteIP: "127.0.0.1:55148" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000002"} httpResponse: {status: 200 bytes: 1742 elapsed: 2.684313} 
2026-03-29T15:00:17.434450606Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/css/style.css" method: "GET" path: "/ui/css/style.css" remoteIP: "127.0.0.1:55148" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000003"} httpResponse: {status: 200 bytes: 29184 elapsed: 0.216900} 
2026-03-29T15:00:17.56194032Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/js/navbar.js" method: "GET" path: "/ui/js/navbar.js" remoteIP: "127.0.0.1:55148" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000004"} httpResponse: {status: 200 bytes: 4426 elapsed: 0.155372} 
2026-03-29T15:00:17.58977093Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/js/mainContent.js" method: "GET" path: "/ui/js/mainContent.js" remoteIP: "127.0.0.1:55148" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000005"} httpResponse: {status: 200 bytes: 7712 elapsed: 0.067139} 
2026-03-29T15:00:17.670012032Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/assets/mcptoolboxlogo.png" method: "GET" path: "/ui/assets/mcptoolboxlogo.png" remoteIP: "127.0.0.1:55148" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000006"} httpResponse: {status: 200 bytes: 117020 elapsed: 0.305607} 
2026-03-29T15:00:19.218144569Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/toolsets" method: "GET" path: "/ui/toolsets" remoteIP: "127.0.0.1:55148" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000007"} httpResponse: {status: 200 bytes: 3246 elapsed: 0.082117} 
2026-03-29T15:00:19.306198303Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/css/style.css" method: "GET" path: "/ui/css/style.css" remoteIP: "127.0.0.1:55148" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000008"} httpResponse: {status: 200 bytes: 29184 elapsed: 0.210155} 
2026-03-29T15:00:19.341869226Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/js/toolsets.js" method: "GET" path: "/ui/js/toolsets.js" remoteIP: "127.0.0.1:55148" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000009"} httpResponse: {status: 200 bytes: 4570 elapsed: 0.088582} 
2026-03-29T15:00:19.370137129Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/js/navbar.js" method: "GET" path: "/ui/js/navbar.js" remoteIP: "127.0.0.1:55148" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000010"} httpResponse: {status: 200 bytes: 4426 elapsed: 0.102240} 
2026-03-29T15:00:19.402143046Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/js/mainContent.js" method: "GET" path: "/ui/js/mainContent.js" remoteIP: "127.0.0.1:55148" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000011"} httpResponse: {status: 200 bytes: 7712 elapsed: 0.129607} 
2026-03-29T15:00:19.43846916Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/js/loadTools.js" method: "GET" path: "/ui/js/loadTools.js" remoteIP: "127.0.0.1:55148" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000012"} httpResponse: {status: 200 bytes: 15184 elapsed: 0.129390} 
2026-03-29T15:00:19.482357022Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/js/toolDisplay.js" method: "GET" path: "/ui/js/toolDisplay.js" remoteIP: "127.0.0.1:55148" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000013"} httpResponse: {status: 200 bytes: 42248 elapsed: 0.179359} 
2026-03-29T15:00:19.562788607Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/js/runTool.js" method: "GET" path: "/ui/js/runTool.js" remoteIP: "127.0.0.1:55148" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000014"} httpResponse: {status: 200 bytes: 12748 elapsed: 0.305360} 
2026-03-29T15:00:19.577738626Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/js/auth.js" method: "GET" path: "/ui/js/auth.js" remoteIP: "127.0.0.1:55148" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000015"} httpResponse: {status: 200 bytes: 15426 elapsed: 0.142096} 
2026-03-29T15:00:19.653833507Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/assets/mcptoolboxlogo.png" method: "GET" path: "/ui/assets/mcptoolboxlogo.png" remoteIP: "127.0.0.1:55148" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000016"} httpResponse: {status: 200 bytes: 117020 elapsed: 0.190885} 
2026-03-29T15:00:25.998303444Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/tools" method: "GET" path: "/ui/tools" remoteIP: "127.0.0.1:55148" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000017"} httpResponse: {status: 200 bytes: 2366 elapsed: 0.052756} 
2026-03-29T15:00:26.10580695Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/css/style.css" method: "GET" path: "/ui/css/style.css" remoteIP: "127.0.0.1:55148" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000018"} httpResponse: {status: 200 bytes: 29184 elapsed: 0.153648} 
2026-03-29T15:00:26.142435566Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/js/tools.js" method: "GET" path: "/ui/js/tools.js" remoteIP: "127.0.0.1:55148" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000019"} httpResponse: {status: 200 bytes: 2538 elapsed: 0.055952} 
2026-03-29T15:00:26.173680088Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/js/navbar.js" method: "GET" path: "/ui/js/navbar.js" remoteIP: "127.0.0.1:55148" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000020"} httpResponse: {status: 200 bytes: 4426 elapsed: 0.090620} 
2026-03-29T15:00:26.197905063Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/js/mainContent.js" method: "GET" path: "/ui/js/mainContent.js" remoteIP: "127.0.0.1:55148" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000021"} httpResponse: {status: 200 bytes: 7712 elapsed: 0.097398} 
2026-03-29T15:00:26.229873929Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/js/loadTools.js" method: "GET" path: "/ui/js/loadTools.js" remoteIP: "127.0.0.1:55148" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000022"} httpResponse: {status: 200 bytes: 15184 elapsed: 0.149366} 
2026-03-29T15:00:26.278195993Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/js/toolDisplay.js" method: "GET" path: "/ui/js/toolDisplay.js" remoteIP: "127.0.0.1:55148" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000023"} httpResponse: {status: 200 bytes: 42248 elapsed: 0.193693} 
2026-03-29T15:00:26.426606254Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/js/runTool.js" method: "GET" path: "/ui/js/runTool.js" remoteIP: "127.0.0.1:55148" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000024"} httpResponse: {status: 200 bytes: 12748 elapsed: 0.113106} 
2026-03-29T15:00:26.441905942Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/js/auth.js" method: "GET" path: "/ui/js/auth.js" remoteIP: "127.0.0.1:55148" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000025"} httpResponse: {status: 200 bytes: 15426 elapsed: 0.136326} 
2026-03-29T15:00:26.678561944Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/assets/mcptoolboxlogo.png" method: "GET" path: "/ui/assets/mcptoolboxlogo.png" remoteIP: "127.0.0.1:55148" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000026"} httpResponse: {status: 200 bytes: 117020 elapsed: 0.210060} 
2026-03-29T15:00:26.711139592Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/api/toolset/" method: "GET" path: "/api/toolset/" remoteIP: "127.0.0.1:55148" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000027"} httpResponse: {status: 200 bytes: 208 elapsed: 17.113845} 
2026-03-29T15:00:28.446040232Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/api/tool/search_release_notes_bq" method: "GET" path: "/api/tool/search_release_notes_bq" remoteIP: "127.0.0.1:55148" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000028"} httpResponse: {status: 200 bytes: 208 elapsed: 0.091008} 
2026-03-29T15:00:35.949763105Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/api/tool/search_release_notes_bq/invoke" method: "POST" path: "/api/tool/search_release_notes_bq/invoke" remoteIP: "127.0.0.1:55148" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000029"} httpResponse: {status: 200 bytes: 303462 elapsed: 2843.745586} 
2026-03-29T15:01:56.801437405Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/mcp/" method: "POST" path: "/mcp/" remoteIP: "127.0.0.1:51572" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000030"} httpResponse: {status: 200 bytes: 261 elapsed: 0.405225} 
2026-03-29T15:01:56.802893756Z INFO Response: 202 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/mcp/" method: "POST" path: "/mcp/" remoteIP: "127.0.0.1:51572" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000031"} httpResponse: {status: 202 bytes: 0 elapsed: 0.151791} 
2026-03-29T15:01:56.804088064Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/mcp/my_bq_toolset" method: "POST" path: "/mcp/my_bq_toolset" remoteIP: "127.0.0.1:51572" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000032"} httpResponse: {status: 200 bytes: 262 elapsed: 0.309648} 
2026-03-29T15:04:56.481386795Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/?authuser=0" method: "GET" path: "/" remoteIP: "127.0.0.1:50888" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000033"} httpResponse: {status: 200 bytes: 23 elapsed: 0.020289} 
2026-03-29T15:04:59.422705039Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui" method: "GET" path: "/ui" remoteIP: "127.0.0.1:50888" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000034"} httpResponse: {status: 200 bytes: 1742 elapsed: 0.076901} 
2026-03-29T15:04:59.526721982Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/css/style.css" method: "GET" path: "/ui/css/style.css" remoteIP: "127.0.0.1:50888" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000035"} httpResponse: {status: 200 bytes: 29184 elapsed: 0.244418} 
2026-03-29T15:04:59.554578122Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/js/navbar.js" method: "GET" path: "/ui/js/navbar.js" remoteIP: "127.0.0.1:50888" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000036"} httpResponse: {status: 200 bytes: 4426 elapsed: 0.073935} 
2026-03-29T15:04:59.585618354Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/js/mainContent.js" method: "GET" path: "/ui/js/mainContent.js" remoteIP: "127.0.0.1:50888" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000037"} httpResponse: {status: 200 bytes: 7712 elapsed: 0.064783} 
2026-03-29T15:04:59.890381629Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/assets/mcptoolboxlogo.png" method: "GET" path: "/ui/assets/mcptoolboxlogo.png" remoteIP: "127.0.0.1:50888" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000038"} httpResponse: {status: 200 bytes: 117020 elapsed: 0.310874} 
2026-03-29T15:05:01.28646963Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/tools" method: "GET" path: "/ui/tools" remoteIP: "127.0.0.1:50888" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000039"} httpResponse: {status: 200 bytes: 2366 elapsed: 0.063550} 
2026-03-29T15:05:01.398209373Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/css/style.css" method: "GET" path: "/ui/css/style.css" remoteIP: "127.0.0.1:50888" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000040"} httpResponse: {status: 200 bytes: 29184 elapsed: 0.202975} 
2026-03-29T15:05:01.435450606Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/js/tools.js" method: "GET" path: "/ui/js/tools.js" remoteIP: "127.0.0.1:50888" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000041"} httpResponse: {status: 200 bytes: 2538 elapsed: 0.051159} 
2026-03-29T15:05:01.465931198Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/js/navbar.js" method: "GET" path: "/ui/js/navbar.js" remoteIP: "127.0.0.1:50888" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000042"} httpResponse: {status: 200 bytes: 4426 elapsed: 0.075911} 
2026-03-29T15:05:01.489891585Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/js/mainContent.js" method: "GET" path: "/ui/js/mainContent.js" remoteIP: "127.0.0.1:50888" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000043"} httpResponse: {status: 200 bytes: 7712 elapsed: 0.077227} 
2026-03-29T15:05:01.505882171Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/js/loadTools.js" method: "GET" path: "/ui/js/loadTools.js" remoteIP: "127.0.0.1:50888" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000044"} httpResponse: {status: 200 bytes: 15184 elapsed: 0.126164} 
2026-03-29T15:05:01.538580354Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/js/toolDisplay.js" method: "GET" path: "/ui/js/toolDisplay.js" remoteIP: "127.0.0.1:50888" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000045"} httpResponse: {status: 200 bytes: 42248 elapsed: 0.153475} 
2026-03-29T15:05:01.577982078Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/js/runTool.js" method: "GET" path: "/ui/js/runTool.js" remoteIP: "127.0.0.1:50888" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000046"} httpResponse: {status: 200 bytes: 12748 elapsed: 0.140363} 
2026-03-29T15:05:01.594258334Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/js/auth.js" method: "GET" path: "/ui/js/auth.js" remoteIP: "127.0.0.1:50888" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000047"} httpResponse: {status: 200 bytes: 15426 elapsed: 0.258639} 
2026-03-29T15:05:01.639209522Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/ui/assets/mcptoolboxlogo.png" method: "GET" path: "/ui/assets/mcptoolboxlogo.png" remoteIP: "127.0.0.1:50888" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000048"} httpResponse: {status: 200 bytes: 117020 elapsed: 0.212729} 
2026-03-29T15:05:01.65477986Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/api/toolset/" method: "GET" path: "/api/toolset/" remoteIP: "127.0.0.1:50888" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000049"} httpResponse: {status: 200 bytes: 208 elapsed: 0.080928} 
2026-03-29T15:05:03.241861664Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/api/tool/search_release_notes_bq" method: "GET" path: "/api/tool/search_release_notes_bq" remoteIP: "127.0.0.1:50888" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000050"} httpResponse: {status: 200 bytes: 208 elapsed: 0.084583} 
2026-03-29T15:05:06.561551552Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/api/tool/search_release_notes_bq/invoke" method: "POST" path: "/api/tool/search_release_notes_bq/invoke" remoteIP: "127.0.0.1:50888" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000051"} httpResponse: {status: 200 bytes: 303462 elapsed: 2147.137158} 
2026-03-29T15:06:01.460349717Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/mcp/" method: "POST" path: "/mcp/" remoteIP: "127.0.0.1:51216" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000052"} httpResponse: {status: 200 bytes: 310932 elapsed: 2305.200411} 
2026-03-29T15:08:32.570888628Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/mcp/" method: "POST" path: "/mcp/" remoteIP: "127.0.0.1:46558" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000053"} httpResponse: {status: 200 bytes: 261 elapsed: 0.232309} 
2026-03-29T15:08:32.572136505Z INFO Response: 202 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/mcp/" method: "POST" path: "/mcp/" remoteIP: "127.0.0.1:46558" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000054"} httpResponse: {status: 202 bytes: 0 elapsed: 0.108352} 
2026-03-29T15:08:32.573205122Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/mcp/my_bq_toolset" method: "POST" path: "/mcp/my_bq_toolset" remoteIP: "127.0.0.1:46558" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000055"} httpResponse: {status: 200 bytes: 262 elapsed: 0.118384} 
2026-03-29T15:09:17.069472085Z INFO Response: 200 OK service: "httplog" httpRequest: {url: "http://127.0.0.1:5000/mcp/" method: "POST" path: "/mcp/" remoteIP: "127.0.0.1:46168" proto: "HTTP/1.1" requestID: "cs-216321250341-default/8t3PhE3Eev-000056"} httpResponse: {status: 200 bytes: 310932 elapsed: 1997.581936} 
```