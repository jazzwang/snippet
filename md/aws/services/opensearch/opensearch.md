# OpenSearch

- Git Repo:
  - https://github.com/opensearch-project/OpenSearch
- Website:
  - https://opensearch.org/
- Document:
  - https://docs.opensearch.org/latest

## 2025-08-24

- 緣起：
  - 工作上要用到 OpenSearch 跟 OpenSearch Dashboard，紀錄一下怎麼用 Docker 在本地端建立實驗環境。
- Installation:
  - https://docs.opensearch.org/latest/install-and-configure/install-opensearch/docker/
- 參考：
  - 在 AWS Workshop ["When Life Hands You Data, Grab OpenSearch"](https://catalog.workshops.aws/workshops/c87214bf-11ea-46b7-82d9-4d934c2a7f53/en-US) 中，提供了一個 [CloudFormation Template](https://static.us-east-1.prod.workshops.aws/public/1db5425d-516a-4a44-98b8-97457a074f85/static/cfns/ops-workshop.yml)。這個 [CloudFormation Template](https://static.us-east-1.prod.workshops.aws/public/1db5425d-516a-4a44-98b8-97457a074f85/static/cfns/ops-workshop.yml) 中有一段是設定 EC2 instance，有一段 Shell Script 如 [opensearch-workshop.sh](opensearch-workshop.sh)。
- 請 Google Gemini 幫忙解釋（詳 [opensearch-workshop.md](opensearch-workshop.md) 中的流程圖跟說明），應該這個 AWS Workshop [CloudFormation Template](https://static.us-east-1.prod.workshops.aws/public/1db5425d-516a-4a44-98b8-97457a074f85/static/cfns/ops-workshop.yml) 只是先建立 EKS 叢集。後續還是用 `helm` 指令來佈署 OpenSearch 跟 OpenSearch Dashboard。
  - https://catalog.workshops.aws/workshops/c87214bf-11ea-46b7-82d9-4d934c2a7f53/en-US/setup/opensearch
  ```bash
  helm repo add opensearch https://opensearch-project.github.io/helm-charts/
  helm repo update
  helm search repo opensearch
  helm install my-opensearch opensearch/opensearch --version 2.25.0 --values=/home/ssm-user/k8s/helm/cluster-values.yaml
  ```
  - 從指令看起來重點還是 `/home/ssm-user/k8s/helm/cluster-values.yaml` 這些檔案，感覺應該放在 EC2 的範本裡。
  - 我想知道的設定檔還有 Moviegeek 的一些設定應該都在 EC2 的範本裡。