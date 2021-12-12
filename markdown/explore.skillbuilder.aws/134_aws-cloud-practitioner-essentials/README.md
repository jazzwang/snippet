[TOC]
----------------------------------------------------------------
- https://www.aws.training/Details/eLearning?id=60697 (English)
- https://www.aws.training/Details/eLearning?id=66364 (繁體中文)

# AWS Cloud Practitioner Essentials

## Module 1: Introduction to Amazon Web Services

- pay-as-you-go pricing model

### Cloud computing

- 五大特徵
  - On-demand delivery
    - Q: Why Amazon has so many products?
    - A: Because companies need those products.
  - Pay-as-you-go

- 三種部署模型
- Deployment models for cloud computing
  - Cloud-based deployment
    - run applications on the cloud
    - migrate application to the cloud
    - new application on the cloud
  - On-premises deployment
    - private cloud deployment
    - application management and virtualization
  - Hybrid deployment
    - cloud-based + On-premises

- Benefits of cloud computing
  - upfront expense -> variable expense
  - reduce cost of data center maintenance
  - no more capacity planning
  - massive economies of scale 規模經濟
  - speed and agility 敏捷
  - go global

## Module 2: Compute in the cloud

- ( 2021-10-05 16:20:59 )
- EC2
  - benefits
  - instance type
  - billing options
  - Auto Scaling
- ELB
  - benefits
  - example use case
- SNS vs SQS

### EC2 = Elastic Compute Cloud

- **Benefits**
  - reduce upfrant to purchase hardward -> launch in minutes
  - pay-as-you-go
  - pay only for the capacity that you need
- How Amazon EC2 works
  - Launch -> Connect -> Use
- **Instance Type**
  - General purpose instances
  - Compute optimized instances
  - Memory optimized instances
  - Accelerated Computing instances (e.g. GPU)
  - Storage optimized instances
- **Billing options**
  - On-Demand 動態
  - Saving Plans 承諾用量 (1-year or 3-year term)
    - reduce <mark>72%</mark> of On-Demand costs
  - Reserved instances 保留
    - Reserved Instances are a <mark>billing discount</mark> applied to the use of <mark>On-Demand Instances</mark> in your account.
  - Spot instances 競標
    - 適用於可以中斷的服務
    - reduce <mark>90%</mark> of On-Demand costs
  - Dedicated Hosts 專用
- **EC2 Auto Scaling**
  - ![](https://content.aws.training/wbt/cecpeb/en/x1/1.0.1/assets/Elskydb_-JIuRgfX_f8VZ-ZFC2TOC7k5B.png)
- ( 2021-10-05 16:39:24 )

### ELB = Elastic Load Balancing

- ELB acts as a single point of contact for all incoming web traffic to your auto scaling group.

### SQS and SNS

- ( 2021-10-09 22:06:46 )
- tightly coupled components -> monolithic application => 單點失效造成整個系統失效
- loosely coupled components -> microservices => 單點失效不會造成整個系統失效
- Amazon Simple Notification Service (Amazon SNS)
  - a publish/subscribe service.
  - In Amazon SNS, subscribers can be `web servers`, `email addresses`, `AWS Lambda functions`, or several other options.
  - 概念類似 newsletter (電子報)，一個 topic 等同於一個電子報。
- ( 2021-10-09 22:21:51 )
- Amazon Simple Queue Service (Amazon SQS)
  - a message queuing service.
  - In Amazon SQS, an application sends messages into a queue.
  - A user or service retrieves a message from the queue, processes it, and then deletes it from the queue.

### Additional Compute services

- ( 2021-10-09 22:23:37 )
- Serverless computing
  - “serverless” means that your code runs on servers, but you do not need to provision or manage these servers.
  - e.g. AWS Lambda

#### Lambda

- ( 2021-10-09 22:29:51 )
- AWS Lambda is a service that lets you run code <mark>without needing to provision or manage servers</mark>.

- ( 2021-10-13 10:55:55 )
- How AWS Lambda works
  - <mark>upload your code</mark> to Lambda
  - trigger from an <mark>event source</mark>
  - run when triggered
  - You pay only for the compute time that you use.

#### Amazon Elastic Container Service (Amazon ECS)

- <mark>Container orchestration services</mark> help you to deploy, manage, and scale your containerized applications.
- AWS supports the use of open-source Docker Community Edition and subscription-based Docker Enterprise Edition.
- With Amazon ECS, you can use **API calls** to launch and stop Docker-enabled applications.

#### Amazon Elastic Kubernetes Service (Amazon EKS)

- a fully **managed service** that you can use to run **Kubernetes** on AWS.

#### AWS Fargate

- AWS Fargate is a **serverless** compute engine for containers.
- It works with **both Amazon ECS and Amazon EKS.**
- AWS Fargate manages your server infrastructure for you.

### Additional resources

- [Hands-On Tutorials: Compute](https://aws.amazon.com/getting-started/hands-on/?awsf.getting-started-category=category%23compute&awsf.getting-started-content-type=content-type%23hands-on)
- [Category Deep Dive: Serverless](https://aws.amazon.com/getting-started/deep-dive-serverless/)