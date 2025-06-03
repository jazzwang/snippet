# Mistral


## Mistral Small 3

- https://mistral.ai/news/mistral-small-3/
  - Apache 2.0
  - 81% MMLU
  - 150 tokens/s
![](https://mistral.ai/images/news/mistral-small-3/up-and-to-the-left.png)

### 2025-02-01

- Try the new Mistral AI `mistral-small` model w/ `Ollama` + `Google Cloud Cloud Run` GPUs today!
  - https://www.linkedin.com/feed/update/urn:li:activity:7290778625769979908/
  - ![](https://media.licdn.com/dms/image/v2/D5622AQE0UOog65bfRA/feedshare-shrink_800/B56ZS4MhmhHsAo-/0/1738257079231?e=1741219200&v=beta&t=hqs0XDCEo3DH85aRSJ0i1ZwR4nXKNVYg39_afUlIVlc)
```bash
# Deploy
gcloud beta run deploy --gpu 1 --image ollama/ollama --port 11434
# Enjoy
OLLAMA_HOST=https://ollama-[PROJECT].us-central1.run.app \
ollama run mistral-small
#Try g.co/cloudrun/gpu TODAY!!!
```
- 實測：
```bash
Welcome to Cloud Shell! Type "help" to get started.
To set your Cloud Platform project in this session use `gcloud config set project [PROJECT_ID]`.
You can view your projects by running `gcloud projects list`.
jazzwang_tw@cloudshell:~ $ gcloud config set project hadoop-labs
Updated property [core/project].
jazzwang_tw@cloudshell:~ (hadoop-labs)$ gcloud beta run deploy --gpu 1 --image ollama/ollama --port 11434
Service name (ollama):  ollama
Please specify a region:
 [1] africa-south1
 [2] asia-east1
 [3] asia-east2
 [4] asia-northeast1
 [5] asia-northeast2
 [6] asia-northeast3
 [7] asia-south1
 [8] asia-south2
 [9] asia-southeast1
 [10] asia-southeast2
 [11] australia-southeast1
 [12] australia-southeast2
 [13] europe-central2
 [14] europe-north1
 [15] europe-southwest1
 [16] europe-west1
 [17] europe-west10
 [18] europe-west12
 [19] europe-west2
 [20] europe-west3
 [21] europe-west4
 [22] europe-west6
 [23] europe-west8
 [24] europe-west9
 [25] me-central1
 [26] me-central2
 [27] me-west1
 [28] northamerica-northeast1
 [29] northamerica-northeast2
 [30] southamerica-east1
 [31] southamerica-west1
 [32] us-central1
 [33] us-east1
 [34] us-east4
 [35] us-east5
 [36] us-south1
 [37] us-west1
 [38] us-west2
 [39] us-west3
 [40] us-west4
 [41] cancel
Please enter numeric choice or text value (must exactly match list item):  2

To make this the default region, run `gcloud config set run/region asia-east1`.

Allow unauthenticated invocations to [ollama] (y/N)?  y

Deploying container to Cloud Run service [ollama] in project [hadoop-labs] region [asia-east1]
X  Deploying new service...                                                                                                                                 
  .  Creating Revision...                                                                                                                                   
  .  Routing traffic...                                                                                                                                     
  .  Setting IAM Policy...                                                                                                                                  
Deployment failed                                                                                                                                           
ERROR: (gcloud.beta.run.deploy) spec.template.spec.node_selector: GPU configuration is only supported in regions: us-central1, asia-southeast1, europe-west4
jazzwang_tw@cloudshell:~ (hadoop-labs)$ 
```

> [!INFO]
> 
> 目前只有 `us-central1`, `asia-southeast1`, `europe-west4` 支援 GPU 的 Google Cloud Run

- 強迫指定佈署到 `us-central1`

```bash
jazzwang_tw@cloudshell:~ (hadoop-labs)$ gcloud beta run deploy --gpu 1 --image ollama/ollama --port 11434 --region us-central1
Service name (ollama):  ollama
Allow unauthenticated invocations to [ollama] (y/N)?  y

Deploying container to Cloud Run service [ollama] in project [hadoop-labs] region [us-central1]
X  Deploying new service...                                                                                                                                 
  .  Creating Revision...                                                                                                                                   
  .  Routing traffic...                                                                                                                                     
  .  Setting IAM Policy...                                                                                                                                  
Deployment failed                                                                                                                                           
ERROR: (gcloud.beta.run.deploy) spec.template.spec.node_selector: This project must be allowed to access instances with attached GPU. Please request the GPU access by requesting a quota via your cloud console. 

See: https://console.cloud.google.com/iam-admin/quotas
```
- 試著申請增加 Cloud Run GPU 配額

> 編輯配額
> Cloud Run Admin API
> 配額： Total Nvidia L4 GPU allocation, per project per region
> 尺寸：
> region : us-central1
> 現值: 0
> 請輸入新配額。如果值超過 0，必須取得服務供應商許可。 
> 新值: 1
> 要求說明
>> trial request to test Cloud Run deploy with GPU
>
> 系統會將您輸入的說明內容傳送給服務供應商，以便對方評估您的要求。建議您在說明中提及配額使用目的、未來拓展計畫、區域或可用區的分布情況，以及任何其他要求或依附元件。

- 看起來因為地緣政治的關係，必須提出使用 GPU 配額的申請才能拿到 GPU 資源。
- ( 2025-02-01 14:29:44 )
- 在 Local 筆電下載看看
```bash
jazzw@JazzBook:~$ ollama pull mistral-small
pulling manifest
pulling manifest
pulling 102a747c1376...   0% ▕                                                        ▏  42 MB/ 14 GB  2.4 MB/s   1h39m 
```
- 預估要 14GB 的大小，那很可能單靠 8GB VRAM GPU 應該是跑不動。
- 來找一下有沒有 HuggingFace 的 GGUF 載點。
  - https://huggingface.co/bartowski/Mistral-Small-24B-Instruct-2501-GGUF
  - 看起來 Q2 的 Model 大約 8GB

### 2025-06-04

```bash
jazzwang_tw@cloudshell:~ (hadoop-labs)$ gcloud beta run deploy --gpu 1 --image ollama/ollama --port 11434
Service name (ollama):  
Please specify a region:
 [1] africa-south1
 [2] asia-east1
 [3] asia-east2
 [4] asia-northeast1
 [5] asia-northeast2
 [6] asia-northeast3
 [7] asia-south1
 [8] asia-south2
 [9] asia-southeast1
 [10] asia-southeast2
 [11] australia-southeast1
 [12] australia-southeast2
 [13] europe-central2
 [14] europe-north1
 [15] europe-north2
 [16] europe-southwest1
 [17] europe-west1
 [18] europe-west10
 [19] europe-west12
 [20] europe-west2
 [21] europe-west3
 [22] europe-west4
 [23] europe-west6
 [24] europe-west8
 [25] europe-west9
 [26] me-central1
 [27] me-central2
 [28] me-west1
 [29] northamerica-northeast1
 [30] northamerica-northeast2
 [31] northamerica-south1
 [32] southamerica-east1
 [33] southamerica-west1
 [34] us-central1
 [35] us-east1
 [36] us-east4
 [37] us-east5
 [38] us-south1
 [39] us-west1
 [40] us-west2
 [41] us-west3
 [42] us-west4
 [43] cancel
Please enter numeric choice or text value (must exactly match list item):  34

To make this the default region, run `gcloud config set run/region us-central1`.

Allow unauthenticated invocations to [ollama] (y/N)?  

Deploying container to Cloud Run service [ollama] in project [hadoop-labs] region [us-central1]
X  Deploying new service...                                                                                                                                 
  -  Creating Revision...                                                                                                                                   
  .  Routing traffic...                                                                                                                                     
Deployment failed                                                                                                                                           
ERROR: (gcloud.beta.run.deploy) Revision 'ollama-00001-ck5' is not ready and cannot serve traffic. Quota exceeded for total allowable count of GPUs per project per region.

Logs URL: https://console.cloud.google.com/logs/viewer?project=hadoop-labs&resource=cloud_run_revision/service_name/ollama/revision_name/ollama-00001-ck5&advancedFilter=resource.type%3D%22cloud_run_revision%22%0Aresource.labels.service_name%3D%22ollama%22%0Aresource.labels.revision_name%3D%22ollama-00001-ck5%22 
For more troubleshooting guidance, see https://cloud.google.com/run/docs/troubleshooting#container-failed-to-start
```
- 用命令列啟動失敗。用 Cloud Console 找不到 `ollama/ollama` image。不過 `gcloud` command 不會報錯。
- 跟
```bash
jazzwang_tw@cloudshell:~ (hadoop-labs)$ gcloud run deploy jazz-llm --image=ollama/ollama:latest --platform managed --region us-central1 --cpu 8 --memory 32Gi --gpu 1 --gpu-type nvidia-l4 --no-cpu-throttling --port 11434
Allow unauthenticated invocations to [jazz-llm] (y/N)?  y

Deploying container to Cloud Run service [jazz-llm] in project [hadoop-labs] region [us-central1]
X  Deploying new service...                                                                                      
  -  Creating Revision...                                                                                        
  .  Routing traffic...                                                                                          
  OK Setting IAM Policy...                                                                                       
Deployment failed                                                                                                
ERROR: (gcloud.run.deploy) Revision 'jazz-llm-00001-qlk' is not ready and cannot serve traffic. Quota exceeded for total allowable count of GPUs per project per region.

Logs URL: https://console.cloud.google.com/logs/viewer?project=hadoop-labs&resource=cloud_run_revision/service_name/jazz-llm/revision_name/jazz-llm-00001-qlk&advancedFilter=resource.type%3D%22cloud_run_revision%22%0Aresource.labels.service_name%3D%22jazz-llm%22%0Aresource.labels.revision_name%3D%22jazz-llm-00001-qlk%22 
For more troubleshooting guidance, see https://cloud.google.com/run/docs/troubleshooting#container-failed-to-start
jazzwang_tw@cloudshell:~ (hadoop-labs)$ 
```
