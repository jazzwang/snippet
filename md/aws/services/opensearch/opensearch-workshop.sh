#!/bin/bash
sudo yum install -y git
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && unzip awscliv2.zip
sudo ./aws/install && mv /usr/bin/aws /usr/bin/aws-old
curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.32.0/2024-12-20/bin/linux/amd64/kubectl
curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.32.0/2024-12-20/bin/linux/amd64/kubectl.sha256
sha256sum -c kubectl.sha256
chmod +x ./kubectl
mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$PATH:$HOME/bin
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
sudo yum install -y jq
sudo wget https://github.com/mikefarah/yq/releases/download/v4.40.5/yq_linux_amd64 -O /usr/bin/yq && chmod +x /usr/bin/yq
echo "export PATH=$PATH:$HOME/bin" >> ~/.bashrc
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
sudo mv /tmp/eksctl /usr/local/bin
/usr/local/bin/eksctl create cluster --version=1.32 --name ops-workshop  --region ${AWS_DEFAULT_REGION} --zones=${AWS_DEFAULT_REGION}a,${AWS_DEFAULT_REGION}b,${AWS_DEFAULT_REGION}c --nodegroup-name linux-nodes --node-type r6i.2xlarge --nodes 2
aws eks update-kubeconfig --region $AWS_DEFAULT_REGION --name ops-workshop
curl -O https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.11.0/docs/install/iam_policy.json
export uu=`uuidgen`
export LB_POLICY_NAME=AWSLoadBalancerControllerPolicy${uu:0:8}
aws iam create-policy --policy-name $LB_POLICY_NAME --policy-document file://iam_policy.json --output text > LBPolicy.out
export LB_POLICY_ARN=`head LBPolicy.out -n 1 | cut -f 2`
eksctl utils associate-iam-oidc-provider --region=$AWS_DEFAULT_REGION --cluster=ops-workshop --approve
eksctl create iamserviceaccount --cluster=ops-workshop --namespace=kube-system --name=aws-load-balancer-controller --attach-policy-arn=$LB_POLICY_ARN --override-existing-serviceaccounts --approve --region=$AWS_DEFAULT_REGION
export ACCOUNT_ID=`aws sts get-caller-identity --query "Account" --output text`
eksctl create iamserviceaccount --name ebs-csi-controller-sa --namespace kube-system --region ${AWS_DEFAULT_REGION} --cluster ops-workshop --attach-policy-arn arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy --approve --role-only --role-name AmazonEKS_EBS_CSI_DriverRole
eksctl create addon --name aws-ebs-csi-driver --cluster ops-workshop --region ${AWS_DEFAULT_REGION} --service-account-role-arn arn:aws:iam::${ACCOUNT_ID}:role/AmazonEKS_EBS_CSI_DriverRole --force
cat << 'EOF' > gp3-storage-class.yaml 
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: gp3
  annotations:
    storageclass.kubernetes.io/is-default-class: 'true'
provisioner: ebs.csi.aws.com
parameters:
  type: gp3
  encrypted: 'true'
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
EOF
kubectl annotate storageclass gp2 storageclass.kubernetes.io/is-default-class="false" --overwrite
kubectl apply -f gp3-storage-class.yaml
kubectl set env daemonset aws-node -n kube-system POD_SECURITY_GROUP_ENFORCING_MODE=standard
kubectl patch daemonset aws-node -n kube-system -p '{"spec": {"template": {"spec": {"initContainers": [{"env":[{"name":"DISABLE_TCP_EARLY_DEMUX","value":"true"}],"name":"aws-vpc-cni-init"}]}}}}'
helm repo add eks https://aws.github.io/eks-charts
export VPC_ID=aws eks describe-cluster --name ops-workshop | grep vpc | sed 's/\s*"vpcId"\s*: "//' | sed 's/"\,//'
helm install aws-load-balancer-controller eks/aws-load-balancer-controller --set clusterName=ops-workshop --set serviceAccount.create=false --set region=$AWS_DEFAULT_REGION --set vpcId=$VPC_ID --set serviceAccount.name=aws-load-balancer-controller -n kube-system
kubectl apply --validate=false -f https://github.com/cert-manager/cert-manager/releases/download/v1.12.3/cert-manager.yaml