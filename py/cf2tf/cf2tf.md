# Cloudformation to Terraform

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
cf2tf -o tf ops-workshop.yml
```

## 2025-08-24

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
- 在 GCP Cloud Shell 裡面驗證：看起來要裝 AWS Terraform Provider
```bash
~/tf$ terraform plan -out=plan.out
╷
│ Error: Missing argument separator
│ 
│   on resource.tf line 13, in resource "aws_subnet" "opensearchvpc_public_subnet1_subnet6_b259228":
│   12:   availability_zone = element(// Unable to resolve Fn::GetAZs with value: "" because cannot access local variable 'az_data' where it is not associated with a value, 0)
│   13:   cidr_block = "10.0.0.0/18"
│ 
│ A comma is required to separate each function argument from the next.
╵
╷
│ Error: Invalid multi-line string
│ 
│   on resource.tf line 222, in resource "aws_subnet" "opensearchvpc_public_subnet1_subnet6_b259228":
│  222:   user_data = base64encode(join("", ["#!/bin/bash
│  223: !/bin/bash
│ 
│ Quoted strings may not be split over multiple lines. To produce a multi-line string, either use the \n escape to represent a newline character or use the "heredoc" multi-line template
│ syntax.
╵
╷
│ Error: Invalid multi-line string
│ 
│   on resource.tf line 223, in resource "aws_subnet" "opensearchvpc_public_subnet1_subnet6_b259228":
│  223: !/bin/bash
│  224: export AWS_DEFAULT_REGION=", data.aws_region.current.name, "
│ 
│ Quoted strings may not be split over multiple lines. To produce a multi-line string, either use the \n escape to represent a newline character or use the "heredoc" multi-line template
│ syntax.
╵
╷
│ Error: Invalid multi-line string
│ 
│   on resource.tf line 224, in resource "aws_subnet" "opensearchvpc_public_subnet1_subnet6_b259228":
│  224: export AWS_DEFAULT_REGION=", data.aws_region.current.name, "
│  225: sudo yum install -y git
│ 
│ Quoted strings may not be split over multiple lines. To produce a multi-line string, either use the \n escape to represent a newline character or use the "heredoc" multi-line template
│ syntax.
╵
╷
│ Error: Invalid multi-line string
│ 
│   on resource.tf line 225, in resource "aws_subnet" "opensearchvpc_public_subnet1_subnet6_b259228":
│  225: sudo yum install -y git
│  226: curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && unzip awscliv2.zip
│ 
│ Quoted strings may not be split over multiple lines. To produce a multi-line string, either use the \n escape to represent a newline character or use the "heredoc" multi-line template
│ syntax.
╵
╷
│ Error: Invalid character
│ 
│   on resource.tf line 232, in resource "aws_subnet" "opensearchvpc_public_subnet1_subnet6_b259228":
│  232: mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$PATH:$HOME/bin
│ 
│ This character is not used within the language.
╵
╷
│ Error: Invalid character
│ 
│   on resource.tf line 232, in resource "aws_subnet" "opensearchvpc_public_subnet1_subnet6_b259228":
│  232: mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$PATH:$HOME/bin
│ 
│ This character is not used within the language.
╵
╷
│ Error: Invalid character
│ 
│   on resource.tf line 232, in resource "aws_subnet" "opensearchvpc_public_subnet1_subnet6_b259228":
│  232: mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$PATH:$HOME/bin
│ 
│ This character is not used within the language.
╵
╷
│ Error: Invalid character
│ 
│   on resource.tf line 232, in resource "aws_subnet" "opensearchvpc_public_subnet1_subnet6_b259228":
│  232: mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$PATH:$HOME/bin
│ 
│ This character is not used within the language.
╵
╷
│ Error: Unsupported operator
│ 
│   on resource.tf line 238, in resource "aws_subnet" "opensearchvpc_public_subnet1_subnet6_b259228":
│  238: echo "export PATH=$PATH:$HOME/bin" >> ~/.bashrc
│ 
│ Bitwise operators are not supported. Did you mean boolean NOT ("!")?
╵
╷
│ Error: Unsupported operator
│ 
│   on resource.tf line 239, in resource "aws_subnet" "opensearchvpc_public_subnet1_subnet6_b259228":
│  239: curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
│ 
│ Bitwise operators are not supported. Did you mean boolean OR ("||")?
╵
╷
│ Error: Invalid character
│ 
│   on resource.tf line 241, in resource "aws_subnet" "opensearchvpc_public_subnet1_subnet6_b259228":
│  241: /usr/local/bin/eksctl create cluster --version=1.32 --name ops-workshop  --region ${AWS_DEFAULT_REGION} --zones=${AWS_DEFAULT_REGION}a,${AWS_DEFAULT_REGION}b,${AWS_DEFAULT_REGION}c --nodegroup-name linux-nodes --node-type r6i.2xlarge --nodes 2
│ 
│ This character is not used within the language.
╵
╷
│ Error: Invalid character
│ 
│   on resource.tf line 241, in resource "aws_subnet" "opensearchvpc_public_subnet1_subnet6_b259228":
│  241: /usr/local/bin/eksctl create cluster --version=1.32 --name ops-workshop  --region ${AWS_DEFAULT_REGION} --zones=${AWS_DEFAULT_REGION}a,${AWS_DEFAULT_REGION}b,${AWS_DEFAULT_REGION}c --nodegroup-name linux-nodes --node-type r6i.2xlarge --nodes 2
│ 
│ This character is not used within the language.
╵
╷
│ Error: Invalid character
│ 
│   on resource.tf line 241, in resource "aws_subnet" "opensearchvpc_public_subnet1_subnet6_b259228":
│  241: /usr/local/bin/eksctl create cluster --version=1.32 --name ops-workshop  --region ${AWS_DEFAULT_REGION} --zones=${AWS_DEFAULT_REGION}a,${AWS_DEFAULT_REGION}b,${AWS_DEFAULT_REGION}c --nodegroup-name linux-nodes --node-type r6i.2xlarge --nodes 2
│ 
│ This character is not used within the language.
╵
╷
│ Error: Invalid character
│ 
│   on resource.tf line 241, in resource "aws_subnet" "opensearchvpc_public_subnet1_subnet6_b259228":
│  241: /usr/local/bin/eksctl create cluster --version=1.32 --name ops-workshop  --region ${AWS_DEFAULT_REGION} --zones=${AWS_DEFAULT_REGION}a,${AWS_DEFAULT_REGION}b,${AWS_DEFAULT_REGION}c --nodegroup-name linux-nodes --node-type r6i.2xlarge --nodes 2
│ 
│ This character is not used within the language.
╵
╷
│ Error: Invalid character
│ 
│   on resource.tf line 242, in resource "aws_subnet" "opensearchvpc_public_subnet1_subnet6_b259228":
│  242: aws eks update-kubeconfig --region $AWS_DEFAULT_REGION --name ops-workshop
│ 
│ This character is not used within the language.
╵
╷
│ Error: Invalid character
│ 
│   on resource.tf line 244, in resource "aws_subnet" "opensearchvpc_public_subnet1_subnet6_b259228":
│  244: export uu=`uuidgen`
│ 
│ The "`" character is not valid. To create a multi-line string, use the "heredoc" syntax, like "<<EOT".
╵
╷
│ Error: Invalid character
│ 
│   on resource.tf line 245, in resource "aws_subnet" "opensearchvpc_public_subnet1_subnet6_b259228":
│  245: export LB_POLICY_NAME=AWSLoadBalancerControllerPolicy${uu:0:8}
│ 
│ This character is not used within the language.
╵
╷
│ Error: Invalid character
│ 
│   on resource.tf line 246, in resource "aws_subnet" "opensearchvpc_public_subnet1_subnet6_b259228":
│  246: aws iam create-policy --policy-name $LB_POLICY_NAME --policy-document file://iam_policy.json --output text > LBPolicy.out
│ 
│ This character is not used within the language.
╵
╷
│ Error: Invalid character
│ 
│   on resource.tf line 247, in resource "aws_subnet" "opensearchvpc_public_subnet1_subnet6_b259228":
│  247: export LB_POLICY_ARN=`head LBPolicy.out -n 1 | cut -f 2`
│ 
│ The "`" character is not valid. To create a multi-line string, use the "heredoc" syntax, like "<<EOT".
╵
╷
│ Error: Unsupported operator
│ 
│   on resource.tf line 247, in resource "aws_subnet" "opensearchvpc_public_subnet1_subnet6_b259228":
│  247: export LB_POLICY_ARN=`head LBPolicy.out -n 1 | cut -f 2`
│ 
│ Bitwise operators are not supported. Did you mean boolean OR ("||")?
╵
╷
│ Error: Invalid character
│ 
│   on resource.tf line 248, in resource "aws_subnet" "opensearchvpc_public_subnet1_subnet6_b259228":
│  248: eksctl utils associate-iam-oidc-provider --region=$AWS_DEFAULT_REGION --cluster=ops-workshop --approve
│ 
│ This character is not used within the language.
╵
╷
│ Error: Invalid character
│ 
│   on resource.tf line 249, in resource "aws_subnet" "opensearchvpc_public_subnet1_subnet6_b259228":
│  249: eksctl create iamserviceaccount --cluster=ops-workshop --namespace=kube-system --name=aws-load-balancer-controller --attach-policy-arn=$LB_POLICY_ARN --override-existing-serviceaccounts --approve --region=$AWS_DEFAULT_REGION
│ 
│ This character is not used within the language.
╵
╷
│ Error: Invalid character
│ 
│   on resource.tf line 249, in resource "aws_subnet" "opensearchvpc_public_subnet1_subnet6_b259228":
│  249: eksctl create iamserviceaccount --cluster=ops-workshop --namespace=kube-system --name=aws-load-balancer-controller --attach-policy-arn=$LB_POLICY_ARN --override-existing-serviceaccounts --approve --region=$AWS_DEFAULT_REGION
│ 
│ This character is not used within the language.
╵
╷
│ Error: Invalid character
│ 
│   on resource.tf line 251, in resource "aws_subnet" "opensearchvpc_public_subnet1_subnet6_b259228":
│  251: eksctl create iamserviceaccount --name ebs-csi-controller-sa --namespace kube-system --region ${AWS_DEFAULT_REGION} --cluster ops-workshop --attach-policy-arn arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy --approve --role-only --role-name AmazonEKS_EBS_CSI_DriverRole
│ 
│ This character is not used within the language.
╵
╷
│ Error: Invalid character
│ 
│   on resource.tf line 252, in resource "aws_subnet" "opensearchvpc_public_subnet1_subnet6_b259228":
│  252: eksctl create addon --name aws-ebs-csi-driver --cluster ops-workshop --region ${AWS_DEFAULT_REGION} --service-account-role-arn arn:aws:iam::${ACCOUNT_ID}:role/AmazonEKS_EBS_CSI_DriverRole --force
│ 
│ This character is not used within the language.
╵
╷
│ Error: Invalid character
│ 
│   on resource.tf line 252, in resource "aws_subnet" "opensearchvpc_public_subnet1_subnet6_b259228":
│  252: eksctl create addon --name aws-ebs-csi-driver --cluster ops-workshop --region ${AWS_DEFAULT_REGION} --service-account-role-arn arn:aws:iam::${ACCOUNT_ID}:role/AmazonEKS_EBS_CSI_DriverRole --force
│ 
│ This character is not used within the language.
╵
╷
│ Error: Invalid character
│ 
│   on resource.tf line 253, in resource "aws_subnet" "opensearchvpc_public_subnet1_subnet6_b259228":
│  253: cat << 'EOF' > gp3-storage-class.yaml 
│ 
│ Single quotes are not valid. Use double quotes (") to enclose strings.
╵
╷
│ Error: Invalid character
│ 
│   on resource.tf line 259, in resource "aws_subnet" "opensearchvpc_public_subnet1_subnet6_b259228":
│  259:     storageclass.kubernetes.io/is-default-class: 'true'
│ 
│ Single quotes are not valid. Use double quotes (") to enclose strings.
╵
╷
│ Error: Unsupported operator
│ 
│   on resource.tf line 272, in resource "aws_subnet" "opensearchvpc_public_subnet1_subnet6_b259228":
│  272: export VPC_ID=aws eks describe-cluster --name ops-workshop | grep vpc | sed 's/\s*"vpcId"\s*: "//' | sed 's/"\,//'
│ 
│ Bitwise operators are not supported. Did you mean boolean OR ("||")?
╵
╷
│ Error: Invalid character
│ 
│   on resource.tf line 272, in resource "aws_subnet" "opensearchvpc_public_subnet1_subnet6_b259228":
│  272: export VPC_ID=aws eks describe-cluster --name ops-workshop | grep vpc | sed 's/\s*"vpcId"\s*: "//' | sed 's/"\,//'
│ 
│ This character is not used within the language.
╵
╷
│ Error: Invalid character
│ 
│   on resource.tf line 272, in resource "aws_subnet" "opensearchvpc_public_subnet1_subnet6_b259228":
│  272: export VPC_ID=aws eks describe-cluster --name ops-workshop | grep vpc | sed 's/\s*"vpcId"\s*: "//' | sed 's/"\,//'
│ 
│ This character is not used within the language.
╵
╷
│ Error: Invalid character
│ 
│   on resource.tf line 272, in resource "aws_subnet" "opensearchvpc_public_subnet1_subnet6_b259228":
│  272: export VPC_ID=aws eks describe-cluster --name ops-workshop | grep vpc | sed 's/\s*"vpcId"\s*: "//' | sed 's/"\,//'
│ 
│ This character is not used within the language.
╵
╷
│ Error: Invalid character
│ 
│   on resource.tf line 273, in resource "aws_subnet" "opensearchvpc_public_subnet1_subnet6_b259228":
│  273: helm install aws-load-balancer-controller eks/aws-load-balancer-controller --set clusterName=ops-workshop --set serviceAccount.create=false --set region=$AWS_DEFAULT_REGION --set vpcId=$VPC_ID --set serviceAccount.name=aws-load-balancer-controller -n kube-system
│ 
│ This character is not used within the language.
╵
╷
│ Error: Invalid character
│ 
│   on resource.tf line 273, in resource "aws_subnet" "opensearchvpc_public_subnet1_subnet6_b259228":
│  273: helm install aws-load-balancer-controller eks/aws-load-balancer-controller --set clusterName=ops-workshop --set serviceAccount.create=false --set region=$AWS_DEFAULT_REGION --set vpcId=$VPC_ID --set serviceAccount.name=aws-load-balancer-controller -n kube-system
│ 
│ This character is not used within the language.
```