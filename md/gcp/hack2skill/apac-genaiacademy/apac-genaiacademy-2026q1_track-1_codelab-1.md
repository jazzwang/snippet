- ( 2026-03-16 08:59:29 )
```bash
Welcome to Cloud Shell! Type "help" to get started, or type "gemini" to try prompting with Gemini CLI.
Your Cloud Platform project in this session is set to jazz-adk-labs.
Use `gcloud config set project [PROJECT_ID]` to change to a different project.
jazzwang@cloudshell:~ (jazz-adk-labs)$ gcloud config set project jazz-adk-labs
Updated property [core/project].
jazzwang@cloudshell:~ (jazz-adk-labs)$ gcloud services enable \
  run.googleapis.com \
  artifactregistry.googleapis.com \
  cloudbuild.googleapis.com \
  aiplatform.googleapis.com \
  compute.googleapis.com
Operation "operations/acf.p2-10xxx953xxx55-64f406e8-065f-49b0-ae18-c4394c066843" finished successfully.
jazzwang@cloudshell:~ (jazz-adk-labs)$ cd && mkdir zoo_guide_agent && cd zoo_guide_agent
jazzwang@cloudshell:~/zoo_guide_agent (jazz-adk-labs)$ cloudshell open-workspace ~/zoo_guide_agent
jazzwang@cloudshell:~/zoo_guide_agent (jazz-adk-labs)$ cloudshell edit requirements.txt
jazzwang@cloudshell:~/zoo_guide_agent (jazz-adk-labs)$ uv venv
source .venv/bin/activate
Using CPython 3.12.3 interpreter at: /usr/bin/python
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate
(zoo_guide_agent) jazzwang@cloudshell:~/zoo_guide_agent (jazz-adk-labs)$ uv pip install -r requirements.txt
Resolved 130 packages in 2.07s
      Built wikipedia==1.4.0
Prepared 130 packages in 2.69s
Installed 130 packages in 115ms
 + absolufy-imports==0.3.1
 + aiohappyeyeballs==2.6.1
 + aiohttp==3.13.3
 + aiosignal==1.4.0
 + alembic==1.18.4
 + annotated-doc==0.0.4
 + annotated-types==0.7.0
 + anyio==4.12.1
 + attrs==25.4.0
 + authlib==1.6.9
 + beautifulsoup4==4.14.3
 + certifi==2026.2.25
 + cffi==2.0.0
 + charset-normalizer==3.4.6
 + click==8.3.1
 + cloudpickle==3.1.2
 + cryptography==46.0.5
 + dataclasses-json==0.6.7
 + distro==1.9.0
 + docstring-parser==0.17.0
 + fastapi==0.135.1
 + frozenlist==1.8.0
 + google-adk==1.14.0
 + google-api-core==2.30.0
 + google-api-python-client==2.192.0
 + google-auth==2.49.1
 + google-auth-httplib2==0.3.0
 + google-cloud-aiplatform==1.141.0
 + google-cloud-appengine-logging==1.8.0
 + google-cloud-audit-log==0.4.0
 + google-cloud-bigquery==3.40.1
 + google-cloud-bigtable==2.35.0
 + google-cloud-core==2.5.0
 + google-cloud-iam==2.21.0
 + google-cloud-logging==3.14.0
 + google-cloud-monitoring==2.29.1
 + google-cloud-resource-manager==1.16.0
 + google-cloud-secret-manager==2.26.0
 + google-cloud-spanner==3.63.0
 + google-cloud-speech==2.37.0
 + google-cloud-storage==2.19.0
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
 + jsonpatch==1.33
 + jsonpointer==3.0.0
 + jsonschema==4.26.0
 + jsonschema-specifications==2025.9.1
 + langchain==0.3.28
 + langchain-community==0.3.27
 + langchain-core==0.3.83
 + langchain-text-splitters==0.3.11
 + langsmith==0.7.17
 + mako==1.3.10
 + markupsafe==3.0.3
 + marshmallow==3.26.2
 + mcp==1.26.0
 + mmh3==5.2.1
 + multidict==6.7.1
 + mypy-extensions==1.1.0
 + numpy==2.4.3
 + opentelemetry-api==1.38.0
 + opentelemetry-exporter-gcp-logging==1.11.0a0
 + opentelemetry-exporter-gcp-trace==1.11.0
 + opentelemetry-exporter-otlp-proto-common==1.38.0
 + opentelemetry-exporter-otlp-proto-http==1.38.0
 + opentelemetry-proto==1.38.0
 + opentelemetry-resourcedetector-gcp==1.11.0a0
 + opentelemetry-sdk==1.38.0
 + opentelemetry-semantic-conventions==0.59b0
 + orjson==3.11.7
 + packaging==25.0
 + propcache==0.4.1
 + proto-plus==1.27.1
 + protobuf==6.33.5
 + pyasn1==0.6.2
 + pyasn1-modules==0.4.2
 + pycparser==3.0
 + pydantic==2.12.5
 + pydantic-core==2.41.5
 + pydantic-settings==2.13.1
 + pyjwt==2.12.1
 + pyparsing==3.3.2
 + python-dateutil==2.9.0.post0
 + python-dotenv==1.2.2
 + python-multipart==0.0.22
 + pyyaml==6.0.3
 + referencing==0.37.0
 + requests==2.32.5
 + requests-toolbelt==1.0.0
 + rpds-py==0.30.0
 + six==1.17.0
 + sniffio==1.3.1
 + soupsieve==2.8.3
 + sqlalchemy==2.0.48
 + sqlalchemy-spanner==1.17.2
 + sqlparse==0.5.5
 + sse-starlette==3.3.2
 + starlette==0.52.1
 + tenacity==8.5.0
 + typing-extensions==4.15.0
 + typing-inspect==0.9.0
 + typing-inspection==0.4.2
 + tzlocal==5.3.1
 + uritemplate==4.2.0
 + urllib3==2.6.3
 + uuid-utils==0.14.1
 + uvicorn==0.41.0
 + watchdog==6.0.0
 + websockets==15.0.1
 + wikipedia==1.4.0
 + xxhash==3.6.0
 + yarl==1.23.0
 + zipp==3.23.0
 + zstandard==0.25.0
(zoo_guide_agent) jazzwang@cloudshell:~/zoo_guide_agent (jazz-adk-labs)$ 
(zoo_guide_agent) jazzwang@cloudshell:~/zoo_guide_agent (jazz-adk-labs)$ cloudshell edit .env
(zoo_guide_agent) jazzwang@cloudshell:~/zoo_guide_agent (jazz-adk-labs)$ # 1. Set the variables in your terminal first
PROJECT_ID=$(gcloud config get-value project)
PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format="value(projectNumber)")
SA_NAME=lab2-cr-service

# 2. Create the .env file using those variables
cat <<EOF > .env
PROJECT_ID=$PROJECT_ID
PROJECT_NUMBER=$PROJECT_NUMBER
SA_NAME=$SA_NAME
SERVICE_ACCOUNT=${SA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com
MODEL="gemini-2.5-flash"
EOF
Your active configuration is: [cloudshell-23482]
(zoo_guide_agent) jazzwang@cloudshell:~/zoo_guide_agent (jazz-adk-labs)$ cloudshell edit __init__.py
(zoo_guide_agent) jazzwang@cloudshell:~/zoo_guide_agent (jazz-adk-labs)$ cloudshell edit agent.py
(zoo_guide_agent) jazzwang@cloudshell:~/zoo_guide_agent (jazz-adk-labs)$ tree
.
├── agent.py
├── __init__.py
└── requirements.txt

0 directories, 3 files
(zoo_guide_agent) jazzwang@cloudshell:~/zoo_guide_agent (jazz-adk-labs)$ ls
agent.py  __init__.py  requirements.txt
(zoo_guide_agent) jazzwang@cloudshell:~/zoo_guide_agent (jazz-adk-labs)$ ls -al
total 28
drwxrwxr-x  3 jazzwang jazzwang 4096 Mar 16 00:29 .
drwxr-xr-x 15 jazzwang jazzwang 4096 Mar 16 00:24 ..
-rw-rw-r--  1 jazzwang jazzwang 3689 Mar 16 00:31 agent.py
-rw-rw-r--  1 jazzwang jazzwang  173 Mar 16 00:27 .env
-rw-rw-r--  1 jazzwang jazzwang   19 Mar 16 00:28 __init__.py
-rw-rw-r--  1 jazzwang jazzwang   63 Mar 16 00:26 requirements.txt
drwxrwxr-x  5 jazzwang jazzwang 4096 Mar 16 00:26 .venv
(zoo_guide_agent) jazzwang@cloudshell:~/zoo_guide_agent (jazz-adk-labs)$ cd ..
(zoo_guide_agent) jazzwang@cloudshell:~ (jazz-adk-labs)$ tree zoo_guide_agent/
zoo_guide_agent/
├── agent.py
├── __init__.py
└── requirements.txt

0 directories, 3 files
(zoo_guide_agent) jazzwang@cloudshell:~ (jazz-adk-labs)$ cd zoo_guide_agent/
(zoo_guide_agent) jazzwang@cloudshell:~/zoo_guide_agent (jazz-adk-labs)$ source .env
(zoo_guide_agent) jazzwang@cloudshell:~/zoo_guide_agent (jazz-adk-labs)$ gcloud iam service-accounts create ${SA_NAME} \
    --display-name="Service Account for lab 2 "
Created service account [lab2-cr-service].
(zoo_guide_agent) jazzwang@cloudshell:~/zoo_guide_agent (jazz-adk-labs)$ # Grant the "Vertex AI User" role to your service account
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$SERVICE_ACCOUNT" \
  --role="roles/aiplatform.user"
Updated IAM policy for project [jazz-adk-labs].
bindings:
- members:
  - serviceAccount:lab2-cr-service@jazz-adk-labs.iam.gserviceaccount.com
  role: roles/aiplatform.user
- members:
  - serviceAccount:10xxx953xxx55@cloudbuild.gserviceaccount.com
  role: roles/cloudbuild.builds.builder
- members:
  - serviceAccount:service-10xxx953xxx55@gcp-sa-cloudbuild.iam.gserviceaccount.com
  role: roles/cloudbuild.serviceAgent
- members:
  - serviceAccount:10xxx953xxx55@cloudservices.gserviceaccount.com
  role: roles/compute.instanceGroupManagerServiceAgent
- members:
  - serviceAccount:service-10xxx953xxx55@compute-system.iam.gserviceaccount.com
  role: roles/compute.serviceAgent
- members:
  - serviceAccount:service-10xxx953xxx55@containerregistry.iam.gserviceaccount.com
  role: roles/containerregistry.ServiceAgent
- members:
  - serviceAccount:10xxx953xxx55-compute@developer.gserviceaccount.com
  role: roles/editor
- members:
  - user:xxxxxxxxxx@gmail.com
  role: roles/owner
- members:
  - serviceAccount:service-10xxx953xxx55@gcp-sa-pubsub.iam.gserviceaccount.com
  role: roles/pubsub.serviceAgent
- members:
  - serviceAccount:service-10xxx953xxx55@serverless-robot-prod.iam.gserviceaccount.com
  role: roles/run.serviceAgent
etag: BwZNGVvfSzQ=
version: 1
(zoo_guide_agent) jazzwang@cloudshell:~/zoo_guide_agent (jazz-adk-labs)$ # Run the deployment command
uvx --from google-adk==1.14.0 \
adk deploy cloud_run \
  --project=$PROJECT_ID \
  --region=europe-west1 \
  --service_name=zoo-tour-guide \
  --with_ui \
  . \
  -- \
  --labels=dev-tutorial=codelab-adk \
  --service-account=$SERVICE_ACCOUNT
Installed 103 packages in 95ms
/home/jazzwang/.cache/uv/archive-v0/hwKfwa4Gry6K7cwO5Hq1D/lib/python3.12/site-packages/google/cloud/aiplatform/models.py:52: FutureWarning: Support for google-cloud-storage < 3.0.0 will be removed in a future version of google-cloud-aiplatform. Please upgrade to google-cloud-storage >= 3.0.0.
  from google.cloud.aiplatform.utils import gcs_utils
Start generating Cloud Run source files in /tmp/cloud_run_deploy_src/20260316_003347
Copying agent source code...
Copying agent source code completed.
Creating Dockerfile...
Creating Dockerfile complete: /tmp/cloud_run_deploy_src/20260316_003347/Dockerfile
Deploying to Cloud Run...
Deploying from source requires an Artifact Registry Docker repository to store built containers. A repository named [cloud-run-source-deploy] in region 
[europe-west1] will be created.

Do you want to continue (Y/n)?  Y

Allow unauthenticated invocations to [zoo-tour-guide] (y/N)?  y

Building using Dockerfile and deploying container to Cloud Run service [zoo-tour-guide] in project [jazz-adk-labs] region [europe-west1]
Building and deploying new service...                                                                                                                     
  Validating configuration...done                                                                                                                         
  Creating Container Repository...done                                                                                                                    
  Uploading sources.../INFO: Not using ignore file.                                                                                                       
  Uploading sources.../INFO: Uploading [/tmp/tmpb94s2yjz/file.zip] to [run-sources-jazz-adk-labs-europe-west1/services/zoo-tour-guide/1773621309.749087-f44af1ce61ca4a35b704ca1ff75482d4.zip]
  Uploading sources...done                                                                                                                                
  Building Container... Logs are available at [https://console.cloud.google.com/cloud-build/builds;region=europe-west1/5d4bbdef-832e-4223-83b6-a308a80ffda
  9?project=10xxx953xxx55]....done                                                                                                                        
  Setting IAM Policy...done                                                                                                                               
  Creating Revision...done                                                                                                                                
  Routing traffic...done                                                                                                                                  
Done.                                                                                                                                                     
Service [zoo-tour-guide] revision [zoo-tour-guide-00001-h64] has been deployed and is serving 100 percent of traffic.
Service URL: https://zoo-tour-guide-10xxx953xxx55.europe-west1.run.app
INFO: Display format: "none"
Cleaning up the temp folder: /tmp/cloud_run_deploy_src/20260316_003347
(zoo_guide_agent) jazzwang@cloudshell:~/zoo_guide_agent (jazz-adk-labs)$ 
```