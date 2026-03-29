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