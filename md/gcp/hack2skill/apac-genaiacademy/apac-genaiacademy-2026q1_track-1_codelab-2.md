```bash
Welcome to Cloud Shell! Type "help" to get started, or type "gemini" to try prompting with Gemini CLI.
Your Cloud Platform project in this session is set to jazz-adk-labs.
Use `gcloud config set project [PROJECT_ID]` to change to a different project.
jazzwang@cloudshell:~ (jazz-adk-labs)$ gcloud services enable aiplatform.googleapis.com
jazzwang@cloudshell:~ (jazz-adk-labs)$ mkdir ai-agents-adk
cd ai-agents-adk
jazzwang@cloudshell:~/ai-agents-adk (jazz-adk-labs)$ uv venv --python 3.12
source .venv/bin/activate
Using CPython 3.12.3 interpreter at: /usr/bin/python3.12
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate
(ai-agents-adk) jazzwang@cloudshell:~/ai-agents-adk (jazz-adk-labs)$ uv pip install google-adk
Resolved 110 packages in 373ms
Prepared 11 packages in 1.07s
Installed 110 packages in 98ms
 + aiosqlite==0.22.1
 + alembic==1.18.4
 + annotated-doc==0.0.4
 + annotated-types==0.7.0
 + anyio==4.12.1
 + attrs==25.4.0
 + authlib==1.6.9
 + certifi==2026.2.25
 + cffi==2.0.0
 + charset-normalizer==3.4.6
 + click==8.3.1
 + cloudpickle==3.1.2
 + cryptography==46.0.5
 + distro==1.9.0
 + docstring-parser==0.17.0
 + fastapi==0.135.1
 + google-adk==1.27.1
 + google-api-core==2.30.0
 + google-api-python-client==2.192.0
 + google-auth==2.49.1
 + google-auth-httplib2==0.3.0
 + google-cloud-aiplatform==1.141.0
 + google-cloud-appengine-logging==1.8.0
 + google-cloud-audit-log==0.4.0
 + google-cloud-bigquery==3.40.1
 + google-cloud-bigquery-storage==2.36.2
 + google-cloud-bigtable==2.35.0
 + google-cloud-core==2.5.0
 + google-cloud-dataplex==2.16.0
 + google-cloud-discoveryengine==0.13.12
 + google-cloud-iam==2.21.0
 + google-cloud-logging==3.14.0
 + google-cloud-monitoring==2.29.1
 + google-cloud-pubsub==2.36.0
 + google-cloud-resource-manager==1.16.0
 + google-cloud-secret-manager==2.26.0
 + google-cloud-spanner==3.63.0
 + google-cloud-speech==2.37.0
 + google-cloud-storage==3.9.0
 + google-cloud-trace==1.18.0
 + google-crc32c==1.8.0
 + google-genai==1.67.0
 + google-resumable-media==2.8.0
 + googleapis-common-protos==1.73.0
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
 + proto-plus==1.27.1
 + protobuf==6.33.5
 + pyarrow==23.0.1
 + pyasn1==0.6.2
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
 + requests==2.32.5
 + rpds-py==0.30.0
 + six==1.17.0
 + sniffio==1.3.1
 + sqlalchemy==2.0.48
 + sqlalchemy-spanner==1.17.2
 + sqlparse==0.5.5
 + sse-starlette==3.3.2
 + starlette==0.52.1
 + tenacity==9.1.4
 + typing-extensions==4.15.0
 + typing-inspection==0.4.2
 + tzlocal==5.3.1
 + uritemplate==4.2.0
 + urllib3==2.6.3
 + uvicorn==0.41.0
 + watchdog==6.0.0
 + websockets==15.0.1
 + zipp==3.23.0
(ai-agents-adk) jazzwang@cloudshell:~/ai-agents-adk (jazz-adk-labs)$ adk create personal_assistant
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
Enter Google Cloud region [us-central1]: us-central1

Agent created in /home/jazzwang/ai-agents-adk/personal_assistant:
- .env
- __init__.py
- agent.py

(ai-agents-adk) jazzwang@cloudshell:~/ai-agents-adk (jazz-adk-labs)$ cloudshell 
personal_assistant/ .venv/              
(ai-agents-adk) jazzwang@cloudshell:~/ai-agents-adk (jazz-adk-labs)$ cloudshell -h
usage: cloudshell [-h]
                  {help,edit-files,edit-file,edit,open,open-workspace,workspace,ws,download-files,download-file,download,dl,launch-tutorial,env,aliases,get-web-preview-url}
                  ...

positional arguments:
  {help,edit-files,edit-file,edit,open,open-workspace,workspace,ws,download-files,download-file,download,dl,launch-tutorial,env,aliases,get-web-preview-url}
                        Commands
    help                shows this message.
    edit-files (edit-file, edit, open)
                        opens specified file in the Google Cloud Shell editor.
    open-workspace (workspace, ws)
                        opens specified directory as workspace in the Google Cloud Shell editor.
    download-files (download-file, download, dl)
                        initiates the download of the specified file.
    launch-tutorial     launches the specified tutorial.
    aliases             generates a sequence of shell "alias" commands to create short aliases for common subcommands. Example use: eval `cloudshell
                        aliases`
    get-web-preview-url
                        generates web preview URL.

options:
  -h, --help            show this help message and exit
(ai-agents-adk) jazzwang@cloudshell:~/ai-agents-adk (jazz-adk-labs)$ cloudshell ws .
(ai-agents-adk) jazzwang@cloudshell:~/ai-agents-adk (jazz-adk-labs)$ adk run personal_assistant
Log setup complete: /tmp/agents_log/agent.20260316_010355.log
To access latest log: tail -F /tmp/agents_log/agent.latest.log
/home/jazzwang/ai-agents-adk/.venv/lib/python3.12/site-packages/google/adk/cli/cli.py:204: UserWarning: [EXPERIMENTAL] InMemoryCredentialService: This feature is experimental and may change or be removed in future versions without notice. It may introduce breaking changes at any time.
  credential_service = InMemoryCredentialService()
/home/jazzwang/ai-agents-adk/.venv/lib/python3.12/site-packages/google/adk/auth/credential_service/in_memory_credential_service.py:33: UserWarning: [EXPERIMENTAL] BaseCredentialService: This feature is experimental and may change or be removed in future versions without notice. It may introduce breaking changes at any time.
  super().__init__()
Running agent root_agent, type exit to exit.
[user]: hello. What can you do for me?
[root_agent]: Hello! I'm an AI assistant, and I can help you with a wide variety of tasks. Here are some examples of what I can do:

*   **Answer questions:** I can provide information on nearly any topic, from general knowledge to specific facts.
*   **Generate text:** I can write emails, stories, poems, code, scripts, musical pieces, fan mail, or almost any kind of creative content you need.
*   **Summarize information:** I can take a long text and condense it into key points.
*   **Translate languages:** I can help you understand and communicate in different languages.
*   **Explain complex concepts:** If you're struggling with a difficult topic, I can break it down into simpler terms.
*   **Brainstorm ideas:** I can help you come up with new ideas for projects, stories, or anything else.
*   **Provide recommendations:** Looking for a book, movie, or recipe? I can offer suggestions.
*   **Help with writing tasks:** I can assist with grammar, spelling, and improving the clarity of your writing.

Just tell me what you need, and I'll do my best to assist you! How can I help you today?
[user]: ^C
[user]: exit

Aborted!
(ai-agents-adk) jazzwang@cloudshell:~/ai-agents-adk (jazz-adk-labs)$ adk web
2026-03-16 01:05:31,178 - INFO - service_factory.py:266 - Using in-memory memory service
2026-03-16 01:05:31,178 - INFO - local_storage.py:84 - Using per-agent session storage rooted at /home/jazzwang/ai-agents-adk
2026-03-16 01:05:31,179 - INFO - local_storage.py:110 - Using file artifact service at /home/jazzwang/ai-agents-adk/.adk/artifacts
/home/jazzwang/ai-agents-adk/.venv/lib/python3.12/site-packages/google/adk/cli/fast_api.py:192: UserWarning: [EXPERIMENTAL] InMemoryCredentialService: This feature is experimental and may change or be removed in future versions without notice. It may introduce breaking changes at any time.
  credential_service = InMemoryCredentialService()
/home/jazzwang/ai-agents-adk/.venv/lib/python3.12/site-packages/google/adk/auth/credential_service/in_memory_credential_service.py:33: UserWarning: [EXPERIMENTAL] BaseCredentialService: This feature is experimental and may change or be removed in future versions without notice. It may introduce breaking changes at any time.
  super().__init__()
INFO:     Started server process [5122]
INFO:     Waiting for application startup.

+-----------------------------------------------------------------------------+
| ADK Web Server started                                                      |
|                                                                             |
| For local testing, access at http://127.0.0.1:8000.                         |
+-----------------------------------------------------------------------------+

INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:33480 - "GET / HTTP/1.1" 307 Temporary Redirect
INFO:     127.0.0.1:33480 - "GET /dev-ui/ HTTP/1.1" 200 OK
INFO:     127.0.0.1:33480 - "GET /dev-ui/styles-YY6V3TJU.css HTTP/1.1" 200 OK
INFO:     127.0.0.1:33480 - "GET /dev-ui/chunk-RGCH6K7F.js HTTP/1.1" 200 OK
INFO:     127.0.0.1:33480 - "GET /dev-ui/chunk-W7GRJBO5.js HTTP/1.1" 200 OK
INFO:     127.0.0.1:33480 - "GET /dev-ui/polyfills-5CFQRCPP.js HTTP/1.1" 200 OK
INFO:     127.0.0.1:33480 - "GET /dev-ui/main-7SJG752M.js HTTP/1.1" 200 OK
INFO:     127.0.0.1:33480 - "GET /dev-ui/assets/config/runtime-config.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:33480 - "GET /dev-ui/adk_favicon.svg HTTP/1.1" 200 OK
INFO:     127.0.0.1:33480 - "GET /list-apps?relative_path=./ HTTP/1.1" 200 OK
INFO:     127.0.0.1:33480 - "GET /dev-ui/assets/ADK-512-color.svg HTTP/1.1" 200 OK
2026-03-16 01:06:22,776 - INFO - local_storage.py:60 - Creating local session service at /home/jazzwang/ai-agents-adk/personal_assistant/.adk/session.db
2026-03-16 01:06:22,786 - INFO - adk_web_server.py:669 - New session created: c2b49c04-cb34-4f8e-85d9-e0a47509badc
INFO:     127.0.0.1:33480 - "POST /apps/personal_assistant/users/user/sessions HTTP/1.1" 200 OK
INFO:     127.0.0.1:33480 - "GET /builder/app/personal_assistant?ts=1773623182902 HTTP/1.1" 200 OK
INFO:     127.0.0.1:33480 - "GET /apps/personal_assistant/users/user/sessions/c2b49c04-cb34-4f8e-85d9-e0a47509badc HTTP/1.1" 200 OK
INFO:     127.0.0.1:33480 - "GET /debug/trace/session/c2b49c04-cb34-4f8e-85d9-e0a47509badc HTTP/1.1" 200 OK
INFO:     127.0.0.1:33480 - "GET /debug/trace/session/c2b49c04-cb34-4f8e-85d9-e0a47509badc HTTP/1.1" 200 OK
INFO:     127.0.0.1:33480 - "GET /apps/personal_assistant/users/user/sessions HTTP/1.1" 200 OK
INFO:     127.0.0.1:33480 - "GET /apps/personal_assistant/users/user/sessions HTTP/1.1" 200 OK
INFO:     127.0.0.1:33480 - "GET /apps/personal_assistant/eval_results HTTP/1.1" 200 OK
INFO:     127.0.0.1:33480 - "GET /apps/personal_assistant/eval_sets HTTP/1.1" 200 OK
2026-03-16 01:07:09,150 - INFO - envs.py:83 - Loaded .env file for personal_assistant at /home/jazzwang/ai-agents-adk/personal_assistant/.env
2026-03-16 01:07:09,151 - INFO - envs.py:83 - Loaded .env file for personal_assistant at /home/jazzwang/ai-agents-adk/personal_assistant/.env
2026-03-16 01:07:09,152 - INFO - agent_loader.py:130 - Found root_agent in personal_assistant.agent
INFO:     127.0.0.1:44762 - "POST /run_sse HTTP/1.1" 200 OK
2026-03-16 01:07:09,252 - INFO - google_llm.py:185 - Sending out request, model: gemini-2.5-flash, backend: GoogleLLMVariant.VERTEX_AI, stream: False
2026-03-16 01:07:09,252 - INFO - models.py:7569 - AFC is enabled with max remote calls: 10.
2026-03-16 01:07:12,122 - INFO - _client.py:1740 - HTTP Request: POST https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jazz-adk-labs/locations/us-central1/publishers/google/models/gemini-2.5-flash:generateContent "HTTP/1.1 200 OK"
2026-03-16 01:07:12,125 - INFO - google_llm.py:250 - Response received from the model.
INFO:     127.0.0.1:44762 - "GET /debug/trace/session/c2b49c04-cb34-4f8e-85d9-e0a47509badc HTTP/1.1" 200 OK
^C
INFO:     Shutting down
INFO:     Waiting for application shutdown.

+-----------------------------------------------------------------------------+
| ADK Web Server shutting down...                                             |
+-----------------------------------------------------------------------------+

2026-03-16 01:10:16,861 - INFO - runners.py:1571 - Closing runner...
2026-03-16 01:10:16,862 - INFO - runners.py:1579 - Runner closed.
INFO:     Application shutdown complete.
INFO:     Finished server process [5122]

Aborted!
(ai-agents-adk) jazzwang@cloudshell:~/ai-agents-adk (jazz-adk-labs)$ 
```