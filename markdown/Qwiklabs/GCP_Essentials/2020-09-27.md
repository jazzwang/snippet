# 2020-09-27 - Google Cloud Essentials

- [Google Cloud Essentials](https://google.qwiklabs.com/quests/23)
    - `2020-09-27 14:42:44`
    - **qwiklabs**: [Creating a Virtual Machine](https://google.qwiklabs.com/focuses/3563?parent=catalog)
    - `2020-09-27 15:19:55`
    - **qwiklabs**: [Compute Engine: Qwik Start - Windows](https://google.qwiklabs.com/focuses/560?parent=catalog)
    - `2020-09-27 15:37:15`
    - **qwiklabs**: [Getting Started with Cloud Shell & gcloud](https://google.qwiklabs.com/focuses/563?parent=catalog)
    - `2020-09-27 15:52:59`
    - **qwiklabs**: [Kubernetes Engine: Qwik Start](https://google.qwiklabs.com/focuses/878?parent=catalog)
    - `2020-09-27 16:16:20`
    - **qwiklabs**: [Set Up Network and HTTP Load Balancers](https://google.qwiklabs.com/focuses/12007?parent=catalog)
        - https://cloud.google.com/load-balancing/docs/load-balancing-overview#a_closer_look_at_cloud_load_balancers
        - L4 - https://cloud.google.com/compute/docs/load-balancing/network/
        - L7 - https://cloud.google.com/compute/docs/load-balancing/http/
```bash
gcloud config set compute/zone us-central1-a
gcloud config set compute/region us-central1
cat << EOF > startup.sh
#! /bin/bash
apt-get update
apt-get install -y nginx
service nginx start
sed -i -- 's/nginx/Google Cloud Platform - '"\$HOSTNAME"'/' /var/www/html/index.nginx-debian.html
EOF
gcloud compute instance-templates create nginx-template \
         --metadata-from-file startup-script=startup.sh
gcloud compute target-pools create nginx-pool
gcloud compute instance-groups managed create nginx-group \
         --base-instance-name nginx \
         --size 2 \
         --template nginx-template \
         --target-pool nginx-pool
gcloud compute instances list
gcloud compute firewall-rules create www-firewall --allow tcp:80
gcloud compute forwarding-rules create nginx-lb \
         --region us-central1 \
         --ports=80 \
         --target-pool nginx-pool
gcloud compute forwarding-rules list
gcloud compute http-health-checks create http-basic-check
gcloud compute instance-groups managed \
       set-named-ports nginx-group \
       --named-ports http:80
gcloud compute backend-services create nginx-backend \
      --protocol HTTP --http-health-checks http-basic-check --global
gcloud compute backend-services add-backend nginx-backend \
    --instance-group nginx-group \
    --instance-group-zone us-central1-a \
    --global
gcloud compute url-maps create web-map \
    --default-service nginx-backend
gcloud compute target-http-proxies create http-lb-proxy \
    --url-map web-map
gcloud compute forwarding-rules create http-content-rule \
        --global \
        --target-http-proxy http-lb-proxy \
        --ports 80
```

-----

## `gcloud` command

### Environment Variable

- `PROJECT_ID`
- `ZONE`

```
export PROJECT_ID=<your_project_ID>
export ZONE=<your_zone>
```

### `gcloud auth`

```
gcloud auth list
```

### `gcloud components`

```
gcloud components list
```

### `gcloud config`

```
gcloud config --help    =   gcloud help config
gcloud config list
gcloud config list --all
gcloud config list project
gcloud config set compute/zone ...
gcloud config set compute/region ...
```

### `gcloud compute`

```
gcloud compute instances create --help
gcloud compute instances describe <your_vm>
gcloud compute instances list
```
```
gcloud compute ssh gcelab2 --zone $ZONE
```
```
gcloud compute instance-templates create nginx-template \
         --metadata-from-file startup-script=startup.sh
```
```
gcloud compute target-pools create nginx-pool
```
```
gcloud compute instance-groups managed create nginx-group \
         --base-instance-name nginx \
         --size 2 \
         --template nginx-template \
         --target-pool nginx-pool
```
```
gcloud compute firewall-rules create www-firewall --allow tcp:80
```
```
gcloud compute forwarding-rules create nginx-lb \
         --region us-central1 \
         --ports=80 \
         --target-pool nginx-pool
gcloud compute forwarding-rules list
gcloud compute forwarding-rules create http-content-rule \
        --global \
        --target-http-proxy http-lb-proxy \
        --ports 80
```
```
gcloud compute http-health-checks create http-basic-check
```
```
gcloud compute instance-groups managed \
       set-named-ports nginx-group \
       --named-ports http:80
```
```
gcloud compute backend-services create nginx-backend \
      --protocol HTTP --http-health-checks http-basic-check --global
gcloud compute backend-services add-backend nginx-backend \
    --instance-group nginx-group \
    --instance-group-zone us-central1-a \
    --global
```
```
gcloud compute url-maps create web-map \
    --default-service nginx-backend
```
```
gcloud compute target-http-proxies create http-lb-proxy \
    --url-map web-map
```

### `gcloud container`

```
gcloud container clusters create [CLUSTER-NAME]
gcloud container clusters get-credentials [CLUSTER-NAME]
gcloud container clusters delete [CLUSTER-NAME]
```
```
kubectl create deployment hello-server --image=gcr.io/google-samples/hello-app:1.0
kubectl expose deployment hello-server --type=LoadBalancer --port 8080
kubectl get service
```