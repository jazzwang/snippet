# Cloudformation 2 Terraform

- Git Repo
  - https://github.com/DontShaveTheYak/cf2tf
- PyPI
  - https://pypi.org/project/cf2tf/

## 2025-08-22

- 緣起：
  - AWS Workshop 有提供 CloudFormation 的 YAML 檔案，想轉成 Terraform
    - https://catalog.workshops.aws/workshops/c87214bf-11ea-46b7-82d9-4d934c2a7f53/en-US/setup/cfn-setup
- 搜尋：
  - https://discuss.hashicorp.com/t/tool-to-convert-cloudformation-to-terraform/46704
- 解法：
  - https://github.com/DontShaveTheYak/cf2tf
- 測試步驟：
```bash
pip install cf2tf
cd /tmp
wget https://static.us-east-1.prod.workshops.aws/public/1db5425d-516a-4a44-98b8-97457a074f85/static/cfns/ops-workshop.yml
```
- 測試紀錄：
```bash
@jazzwang ➜ /workspaces/snippet (master) $ pip install cf2tf
@jazzwang ➜ /workspaces/snippet (master) $ cd /tmp/
@jazzwang ➜ /tmp $ cf2tf  --help
Usage: cf2tf [OPTIONS] TEMPLATE_PATH

  Convert Cloudformation template into Terraform.

  Args:     template_path (str): The path to the cloudformation template

Options:
  --version            Show the version and exit.
  -o, --output PATH
  -v, --verbosity LVL  Either CRITICAL, ERROR, WARNING, INFO or DEBUG
  --help               Show this message and exit.
@jazzwang ➜ /tmp $ wget https://static.us-east-1.prod.workshops.aws/public/1db5425d-516a-4a44-98b8-97457a074f85/static/cfns/ops-workshop.yml
@jazzwang ➜ /tmp $ cf2tf -o tf ops-workshop.yml 
@jazzwang ➜ /tmp $ tree tf/
tf/
├── data.tf
├── locals.tf
├── output.tf
├── resource.tf
└── variable.tf

0 directories, 5 files
```