# [Quest] Create and Manage Cloud Resources

- https://www.cloudskillsboost.google/quests/120

## 2022-02-04

- [GCP] 2022 TWHK Cloud Study Jam
- https://www.cloudskillsboost.google/focuses/10258?parent=catalog

- Create and Manage Cloud Resources quest
    - https://google.qwiklabs.com/quests/120
    - 內容類似 [Google Cloud Essentials](https://google.qwiklabs.com/quests/23) 但多了 [Create and Manage Cloud Resources](https://www.cloudskillsboost.google/focuses/10258)

----------------

[TOC]

----------------

## 2022-02-09

- 改用另一個沒註冊過的 Gmail 帳號申請一個月 subscription <mark>[DONE]</mark>

## GSP001 - Creating a Virtual Machine
- https://www.cloudskillsboost.google/focuses/3563

### Task 1: Create a new instance from the Cloud Console

```
gcloud compute instances create gcelab \
--zone=us-central1-f \
--machine-type=n1-standard-2 \
--network-interface=network-tier=PREMIUM,subnet=default \
--metadata=enable-oslogin=true \
--maintenance-policy=MIGRATE \
--tags=http-server
```

### Task 2: Install an NGINX web server

```
sudo su -
apt-get update; apt-get install nginx -y ; ps auwx | grep nginx
```

### Task 3: Create a new instance with gcloud

```
gcloud compute instances create gcelab2 --machine-type n1-standard-2 --zone us-central1-f
```

```
gcloud compute instances create --help
```

----------------

[TOC]

----------------

## GSP002 - Getting Started with Cloud Shell and gcloud
- https://www.cloudskillsboost.google/focuses/563

### Task 1: Configure your environment

```
gcloud config get-value compute/zone
gcloud config get-value compute/region
gcloud compute project-info describe --project <your_project_ID>
export PROJECT_ID=<your_project_ID>
export ZONE=<your_zone>
echo $PROJECT_ID
echo $ZONE
gcloud compute instances create gcelab2 --machine-type n1-standard-2 --zone $ZONE
```
- ( 2022-02-09 15:24:40 )
```
gcloud compute instances create --help
```
```
gcloud -h
gcloud config --help
gcloud help config
gcloud config list
gcloud config list --all
gcloud components list
```

### Task 2: Install a new component

```
sudo apt-get install google-cloud-sdk
gcloud beta interactive
gcloud compute instances describe <your_vm>
exit
```

### Task 3: Connect to your VM instance with SSH

```
gcloud compute ssh gcelab2 --zone $ZONE
exit
```

### Task 4: Use the Home directory

```
cd $HOME
vi ./.bashrc
```

----------------

[TOC]

----------------

## GSP100 - Kubernetes Engine: Qwik Start

- https://www.cloudskillsboost.google/focuses/878

### Task 1: Set a default compute zone

```
gcloud config set compute/zone us-central1-a
```

### Task 2: Create a GKE cluster

```
gcloud container clusters create my-cluster
```

### Task 3: Get authentication credentials for the cluster

```
gcloud container clusters get-credentials my-cluster
```

### Task 4: Deploy an application to the cluster

```
kubectl create deployment hello-server --image=gcr.io/google-samples/hello-app:1.0
kubectl expose deployment hello-server --type=LoadBalancer --port 8080
kubectl get service
```

### Task 5: Deleting the cluster

```
gcloud container clusters delete my-cluster
```

----------------

[TOC]

----------------

- ( 2022-02-09 15:55:10 )

## GSP007 - Set Up Network and HTTP Load Balancers

- https://www.cloudskillsboost.google/focuses/12007

### Task 1: Set the default region and zone for all resources

```
gcloud config set compute/zone us-central1-a
gcloud config set compute/region us-central1
```

### Task 2: Create multiple web server instances

```
gcloud compute instances create www1 \
  --image-family debian-9 \
  --image-project debian-cloud \
  --zone us-central1-a \
  --tags network-lb-tag \
  --metadata startup-script="#! /bin/bash
    sudo apt-get update
    sudo apt-get install apache2 -y
    sudo service apache2 restart
    echo '<!doctype html><html><body><h1>www1</h1></body></html>' | tee /var/www/html/index.html"
```
```
gcloud compute instances create www2 \
  --image-family debian-9 \
  --image-project debian-cloud \
  --zone us-central1-a \
  --tags network-lb-tag \
  --metadata startup-script="#! /bin/bash
    sudo apt-get update
    sudo apt-get install apache2 -y
    sudo service apache2 restart
    echo '<!doctype html><html><body><h1>www2</h1></body></html>' | tee /var/www/html/index.html"
```
```
gcloud compute instances create www3 \
  --image-family debian-9 \
  --image-project debian-cloud \
  --zone us-central1-a \
  --tags network-lb-tag \
  --metadata startup-script="#! /bin/bash
    sudo apt-get update
    sudo apt-get install apache2 -y
    sudo service apache2 restart
    echo '<!doctype html><html><body><h1>www3</h1></body></html>' | tee /var/www/html/index.html"
```

- Create a firewall rule to allow external traffic to the VM instances:

```
gcloud compute firewall-rules create www-firewall-network-lb \
    --target-tags network-lb-tag --allow tcp:80
```
- Run the following to list your instances. You'll see their IP addresses in the EXTERNAL_IP column:

```
gcloud compute instances list
```

### Task 3: Configure the load balancing service

- Create a static external IP address for your load balancer:

```
gcloud compute addresses create network-lb-ip-1 \
 --region us-central1
```

- Add a legacy HTTP health check resource:

```
gcloud compute http-health-checks create basic-check
```

- Add a target pool in the same region as your instances.

```
gcloud compute target-pools create www-pool \
    --region us-central1 --http-health-check basic-check
```

- Add the instances to the pool:

```
gcloud compute target-pools add-instances www-pool \
    --instances www1,www2,www3
```

- ( 2022-02-09 16:06:26 )
- Add a forwarding rule:

```
gcloud compute forwarding-rules create www-rule \
    --region us-central1 \
    --ports 80 \
    --address network-lb-ip-1 \
    --target-pool www-pool
```

### Task 4: Sending traffic to your instances

```
gcloud compute forwarding-rules describe www-rule --region us-central1
```

### Task 5: Create an HTTP load balancer

- First, create the load balancer template:

```
gcloud compute instance-templates create lb-backend-template \
   --region=us-central1 \
   --network=default \
   --subnet=default \
   --tags=allow-health-check \
   --image-family=debian-9 \
   --image-project=debian-cloud \
   --metadata=startup-script='#! /bin/bash
     apt-get update
     apt-get install apache2 -y
     a2ensite default-ssl
     a2enmod ssl
     vm_hostname="$(curl -H "Metadata-Flavor:Google" \
     http://169.254.169.254/computeMetadata/v1/instance/name)"
     echo "Page served from: $vm_hostname" | \
     tee /var/www/html/index.html
     systemctl restart apache2'
```

- Create a managed instance group based on the template:

```
gcloud compute instance-groups managed create lb-backend-group \
   --template=lb-backend-template --size=2 --zone=us-central1-a
```

- Create the fw-allow-health-check firewall rule.

```
gcloud compute firewall-rules create fw-allow-health-check \
    --network=default \
    --action=allow \
    --direction=ingress \
    --source-ranges=130.211.0.0/22,35.191.0.0/16 \
    --target-tags=allow-health-check \
    --rules=tcp:80
```

- set up a global static external IP address that your customers use to reach your load balancer.

```
gcloud compute addresses create lb-ipv4-1 \
    --ip-version=IPV4 \
    --global
gcloud compute addresses describe lb-ipv4-1 \
    --format="get(address)" \
    --global
```

- Create a health check for the load balancer:

```
gcloud compute health-checks create http http-basic-check \
    --port 80
```

- Create a backend service:

```
gcloud compute backend-services create web-backend-service \
    --protocol=HTTP \
    --port-name=http \
    --health-checks=http-basic-check \
    --global
```

- Add your instance group as the backend to the backend service:

```
gcloud compute backend-services add-backend web-backend-service \
    --instance-group=lb-backend-group \
    --instance-group-zone=us-central1-a \
    --global
```

- Create a URL map to route the incoming requests to the default backend service:

```
gcloud compute url-maps create web-map-http \
    --default-service web-backend-service
```

- Create a target HTTP proxy to route requests to your URL map:

```
gcloud compute target-http-proxies create http-lb-proxy \
    --url-map web-map-http
```

- Create a global forwarding rule to route incoming requests to the proxy:

```
gcloud compute forwarding-rules create http-content-rule \
    --address=lb-ipv4-1\
    --global \
    --target-http-proxy=http-lb-proxy \
    --ports=80
```

- VALIDATION CHECK

```
gcloud compute instance-templates list
gcloud compute instance-groups managed list
gcloud compute firewall-rules list
gcloud compute addresses list
gcloud compute health-checks list
gcloud compute backend-services list
gcloud compute url-maps list
gcloud compute target-http-proxies list
gcloud compute forwarding-rules list
```

### Task 6: Testing traffic sent to your instances

----------------

[TOC]

----------------

## GSP313 - Create and Manage Cloud Resources: Challenge Lab

- https://www.cloudskillsboost.google/focuses/10258

### Standards you should follow:

1.  Create all resources in the default region or zone, unless otherwise directed.

2.  Naming normally uses the format ==*team-resource*==; for example, an instance could be named **nucleus-webserver1**.

3.  Allocate cost-effective resource sizes. Projects are monitored, and excessive resource use will result in the containing project's termination (and possibly yours), so plan carefully. This is the guidance the monitoring team is willing to share: unless directed, use ==**f1-micro**== for small Linux VMs, and use ==**n1-standard-1**== for Windows or other applications, such as ==Kubernetes nodes==.

### Background

- you receive several requests from the ==Nucleus== team

### Task 1. Create a project jumphost instance

You will use this instance to perform maintenance for the project.

**Requirements:**

- ( 2022-02-04 22:32:58 )
- Name the instance . ==nucleus-jumphost==
- Use an ==*f1-micro*== machine type.
- Use the default image type (Debian Linux).


### Task 2. Create a Kubernetes service cluster

The team is building an application that will use a service running on Kubernetes. You need to:

- Create a cluster (in the `us-east1-b` zone) to host the service.
- Use the Docker container hello-app (`gcr.io/google-samples/hello-app:2.0`) as a place holder; the team will replace the container with their own work later.
- Expose the app on port .

### Task 3. Set up an HTTP load balancer

You will serve the site via nginx web servers, but you want to ensure that the environment is fault-tolerant. Create an HTTP load balancer with a managed instance group of **2 nginx web servers**. Use the following code to configure the web servers; the team will replace this with their own configuration later.

You need to:

- Create an instance template.
- Create a target pool.
- Create a managed instance group.
- Create a firewall rule named as to allow traffic (80/tcp).
- Create a health check.
- Create a backend service, and attach the managed instance group with named port (http:80).
- Create a URL map, and target the HTTP proxy to route requests to your URL map.
- Create a forwarding rule.