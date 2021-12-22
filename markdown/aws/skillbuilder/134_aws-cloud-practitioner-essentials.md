[TOC]
----------------------------------------------------------------
- https://explore.skillbuilder.aws/learn/course/134/aws-cloud-practitioner-essentials
- (OLD, deprecated) https://www.aws.training/Details/eLearning?id=60697 (English)
- (OLD, deprecated) https://www.aws.training/Details/eLearning?id=66364 (繁體中文)

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

#### AWS Lambda

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

## Module 3: Global Infrastructure and Reliability

### AWS global infrastructure

- **AWS Region**
  - Regions are <mark>geographically isolated areas</mark>, where you can access services needed to run your enterprise.
  - 4 business factors that go into choosing a Region:
    - compliance
    - proximity
    - feature availability
    - pricing
- **Availability Zones (AZ)**
  - An Availability Zone is <mark>a single data center or a group of data centers</mark> within a Region.
  - Availability Zones are located **tens of miles apart from each other**.
  - Availability Zones help you solve **<mark>high availability</mark>** and **<mark>disaster recovery</mark>** scenarios, without any additional effort on your part

### Edge locations

- **AWS Edge locations** run **Amazon CloudFront** to help get content closer to your customers, no matter where they are in the world.
- Content Delivery Networks = **CDN**s -> <mark>**Amazon CloudFront**</mark>
- **DNS** -> <mark>**Amazon Route 53**</mark>
- An edge location is a site that <mark>Amazon CloudFront</mark> uses to store cached copies of your content closer to your customers for faster delivery.
- <mark>**AWS Outposts**</mark> - Extend AWS infrastructure and services to your on-premises data center.

### How to provision AWS resources

- In AWS, everything is a API.
- Ways to interact with AWS services
  - **AWS Management Console**
  - **AWS Command Line Interface (AWS CLI)**
  - **software development kits (SDKs)**
    - Supported programming languages include C++, Java, .NET, and more.
- Managed Tool
  - **AWS Elastic Beanstalk**
    - service that helps you provision **Amazon EC2-based environments**.
  - **AWS CloudFormation**
    - an **infrastructure as code** tool that allows you to define a wide variety of AWS resources in a declarative way using **JSON** or **YAML** text-based documents called CloudFormation templates.

### Additional resources

Review these resources to learn more about the concepts that were explored in Module 3.

- [Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)
- [Interactive map of the AWS Global Infrastructure](https://www.infrastructure.aws/)
- [Regions and Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az)
- [AWS Networking and Content Delivery Blog](https://aws.amazon.com/blogs/networking-and-content-delivery/)
- [Tools to Build on AWS](https://aws.amazon.com/tools/)
- [AWS Customer Stories: Content Delivery](https://aws.amazon.com/solutions/case-studies/?customer-references-cards.sort-by=item.additionalFields.publishedDate&customer-references-cards.sort-order=desc&awsf.customer-references-location=*all&awsf.customer-references-segment=*all&awsf.customer-references-product=product%23vpc%7Cproduct%23api-gateway%7Cproduct%23cloudfront%7Cproduct%23route53%7Cproduct%23directconnect%7Cproduct%23elb&awsf.customer-references-category=category%23content-delivery)

- ( 2021-12-12 17:31:29 )

## Module 4: Networking

- ( 2021-12-12 21:31:35 )
- Amazon Virtual Private Cloud, or VPCs

### Connectivity to AWS

- Amazon Virtual Private Cloud (**Amazon VPC**)
  - Amazon VPC enables you to provision an isolated section of the AWS Cloud.
- A **subnet** is a section of a VPC that can contain resources such as Amazon EC2 instances.
- To allow public traffic from the internet to access your VPC, you attach an **internet gateway** to the VPC.

![](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1639317600/QJdXiPoV4TGc9YByvpZSyw/tincan/31d9c0cca79c54bdceaf3e938fd424e97c98c7e8/assets/Q_HnMl_BAEsDZGxf_NEblbQjD0vn0-pPU.png)

- To access private resources in a VPC, you can use a **virtual private gateway**.

![](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1639317600/QJdXiPoV4TGc9YByvpZSyw/tincan/31d9c0cca79c54bdceaf3e938fd424e97c98c7e8/assets/tthacSS-FyYNWwE3_s8U3lQzEONXm1FMX.png)

- **AWS Direct Connect** is a service that enables you to establish a dedicated private connection between your data center and a VPC.

![](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1639317600/QJdXiPoV4TGc9YByvpZSyw/tincan/31d9c0cca79c54bdceaf3e938fd424e97c98c7e8/assets/p53HDtoqu2euSy0Y_YdzRvczPABE_j-yV.png)

### Subnets and network access control lists

#### Network access control lists (ACLs)

- A network access control list (ACL) is a **virtual firewall** that controls inbound and outbound traffic at the **subnet** level.
- **Stateless** packet filtering
  - Network ACLs perform stateless packet filtering.
- By default, your account’s default network ACL <mark>**allows** all inbound and outbound traffic</mark>, but you can modify it by adding your own rules.

#### Security groups

- A security group is a **virtual firewall** that controls inbound and outbound traffic for an **Amazon EC2** instance.
- **Stateful** packet filtering
  - Security groups perform stateful packet filtering.
- By default, security groups <mark>**deny** all inbound traffic</mark>, but you can add custom rules to fit your operational and security needs.

![](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1639317600/QJdXiPoV4TGc9YByvpZSyw/tincan/31d9c0cca79c54bdceaf3e938fd424e97c98c7e8/assets/QkcDe-SJB4lQAuyB_ha8um-1InZb0jryB.png)

### Global networking

#### Domain Name System (DNS) - Amazon Route 53
#### Example: How Amazon Route 53 and Amazon CloudFront deliver content

![](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1639317600/QJdXiPoV4TGc9YByvpZSyw/tincan/31d9c0cca79c54bdceaf3e938fd424e97c98c7e8/assets/mR1nvYoC4OSUVg9a_WE71CA369xcdceJ2.png)

#### Additional resources

To learn more about the concepts that were explored in Module 4, review these resources.

- [Networking and Content Delivery on AWS](https://aws.amazon.com/products/networking)
- [AWS Networking & Content Delivery Blog](https://aws.amazon.com/blogs/networking-and-content-delivery/)
- [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc)
- [What is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
- [How Amazon VPC works](https://docs.aws.amazon.com/vpc/latest/userguide/how-it-works.html)

( 2021-12-12 22:46:59 )

## Module 5: Storage and Databases

- ( 2021-12-12 22:51:46 )

In this module, you will learn how to:

- Summarize the basic concept of storage and databases.
- Describe the benefits of Amazon Elastic Block Store (Amazon EBS).
- Describe the benefits of Amazon Simple Storage Service (Amazon S3).
- Describe the benefits of Amazon Elastic File System (Amazon EFS).
- Summarize various storage solutions.
- Describe the benefits of Amazon Relational Database Service (Amazon RDS).
- Describe the benefits of Amazon DynamoDB.
- Summarize various database services.

### Instance stores and Amazon Elastic Block Store (Amazon EBS)

#### Instance stores

- An instance store provides **temporary** block-level storage for an Amazon EC2 instance.

#### Amazon EBS

- **Amazon Elastic Block Store (Amazon EBS)** is a service that provides **block-level storage volumes** that you can use with Amazon EC2 instances. If you stop or terminate an Amazon EC2 instance, all the data on the attached EBS volume remains available.

#### Amazon EBS snapshots

- An EBS snapshot is an **incremental** backup.

### Amazon Simple Storage Service (Amazon S3)

#### Object storage

- In object storage, each object consists of **data, metadata, and a key**.
  - The data might be an image, video, text document, or any other type of file.
  - Metadata contains information about what the data is, how it is used, the object size, and so on.
  - An object’s key is its **unique identifier**.

#### Amazon S3

- Amazon Simple Storage Service (Amazon S3) is a service that provides **object-level storage**. Amazon S3 stores data as objects in **buckets**.

- <mark>The maximum file size for an object in Amazon S3 is **5 TB**</mark>.

#### Amazon S3 storage classes

- S3 Standard
  - Designed for **frequently accessed** data
  - Stores data in a minimum of **three Availability Zones**
- S3 Standard-Infrequent Access (S3 Standard-IA)
  - Ideal for **infrequently accessed** data
  - Similar to S3 Standard but has a lower storage price and **higher retrieval price**
  - store data in a minimum of **three Availability Zones**.
- S3 One Zone-Infrequent Access (S3 One Zone-IA)
  - Stores data in a **single Availability Zone**
  - Has a lower storage price than S3 Standard-IA
- S3 Intelligent-Tiering
  - Ideal for data with **unknown or changing access patterns**
  - Requires a small monthly monitoring and automation fee per object
  - 30 consecutive days -> move to `S3 Standard-IA` or `S3 Standard`
- S3 Glacier
  - Low-cost storage designed for data archiving
  - Able to retrieve objects within a few minutes to hours
- S3 Glacier Deep Archive
  - Lowest-cost object storage class ideal for archiving
  - Able to retrieve objects within 12 hours

#### AWS EBS vs AWS S3

| AWS EBS | AWS S3 |
|-------------|------------|
| up to 16 TB | up to 5 TB |
| EC2 required | serverless |

### Amazon Elastic File System (Amazon EFS)

- ( 2021-12-12 23:23:42 )
- File storage
  - In file storage, multiple clients (such as users, applications, servers, and so on) can access data that is stored in shared file folders.
- Amazon Elastic File System (Amazon EFS) is a scalable file system used with AWS Cloud services and on-premises resources. As you add and remove files, Amazon EFS grows and shrinks automatically. It can scale on demand to **petabytes** without disrupting applications.
- ( 2021-12-19 23:48:05 )
- - [Amazon EFS: How it works](https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html)

#### AWS EBS vs AWS EFS

| AWS EBS | AWS EFS |
|-------------|------------|
| 1 AZ | multiple AZ |
| attach EC2 | managed service |

- NOTE: think about `NFS over WAN`

### Amazon Relational Database Service (Amazon RDS)

- ( 2021-12-12 23:29:53 )
- Amazon Relational Database Service (Amazon RDS) is a service that enables you to run relational databases in the AWS Cloud.
- Amazon RDS is a **managed service** that automates tasks such as hardware provisioning, database setup, patching, and backups.
- Amazon RDS is available on six database engines:
  - Amazon Aurora
  - PostgreSQL
  - MySQL
  - MariaDB
  - Oracle Database
  - Microsoft SQL Server

#### Amazon Aurora

- an enterprise-class relational database.
- It is compatible with MySQL and PostgreSQL relational databases.
- It is up to **five times faster** than standard MySQL databases and up to **three times faster** than standard PostgreSQL databases.
- Consider Amazon Aurora if your workloads require **high availability**. It replicates **six copies** of your data across **three Availability Zones** and continuously backs up your data to **Amazon S3**.

### Amazon DynamoDB

- Nonrelational databases are sometimes referred to as **“NoSQL databases”** because they use structures other than rows and columns to organize data. With key-value pairs, data is organized into items (keys), and items have attributes (values).

- Amazon DynamoDB is a key-value database service. It delivers single-digit millisecond performance at any scale.
  - Serverless
  - Auto Scaling
- Scaling up to 10 trillion requests per day

#### Amazon RDS vs Amazon DynamoDB

| AWS RDS | AWS DynamoDB |
|-------------|------------|
| Relational (SQL) | Non-Relational (NoSQL) - `key-value` |
| provision on EC2 | managed service |

- ( 2021-12-12 23:46:29 )

### Amazon Redshift

- ( 2021-12-19 22:31:59 )
- Amazon Redshift is a **data warehousing** service that you can use for big data analytics.
- In cooperation with Amazon Redshift Spectrum, you can directly run a single SQL query against **exabytes** of unstructured data running in data lakes.

### AWS Database Migration Service (DMS)

- ( 2021-12-19 23:37:21 )
- AWS Database Migration Service (AWS DMS) enables you to migrate relational databases, nonrelational databases, and other types of data stores.

### Additional database services

- ( 2021-12-19 23:39:42 )
- **Amazon DocumentDB** is a **document database** service that supports **MongoDB** workloads. (MongoDB is a document database program.)
- **Amazon Neptune** is a **graph database** service. You can use Amazon Neptune to build and run applications that work with highly connected datasets, such as <mark>recommendation engines, fraud detection, and knowledge graphs</mark>.
- **Amazon Quantum Ledger Database (Amazon QLDB)** is a ledger database service. You can use Amazon QLDB to review a complete history of all the changes that have been made to your application data.
- **Amazon Managed Blockchain** is a service that you can use to create and manage blockchain networks with **open-source frameworks**. Blockchain is a distributed ledger system that lets multiple parties run transactions and share data without a central authority.
- **Amazon ElastiCache** is a service that adds caching layers on top of your databases to help improve the read times of common requests. It supports two types of data stores: **Redis** and **Memcached**.
- **Amazon DynamoDB Accelerator (DAX)** is an <mark>in-memory cache for DynamoDB</mark>. It helps improve response times from single-digit milliseconds to microseconds.

### Additional resources

- [Cloud Storage on AWS](https://aws.amazon.com/products/storage)
- [AWS Storage Blog](https://aws.amazon.com/blogs/storage/)
- [Hands-On Tutorials: Storage](https://aws.amazon.com/getting-started/hands-on/?awsf.getting-started-category=category%23storage&awsf.getting-started-content-type=content-type%23hands-on)
- [AWS Customer Stories: Storage](https://aws.amazon.com/solutions/case-studies/?customer-references-cards.sort-by=item.additionalFields.publishedDate&customer-references-cards.sort-order=desc&awsf.customer-references-location=*all&awsf.customer-references-segment=*all&awsf.customer-references-product=product%23vpc%7Cproduct%23api-gateway%7Cproduct%23cloudfront%7Cproduct%23route53%7Cproduct%23directconnect%7Cproduct%23elb&awsf.customer-references-category=category%23storage)
- [AWS Database Migration Service](https://aws.amazon.com/dms/)
- [Databases on AWS](https://aws.amazon.com/products/databases)
- [Category Deep Dive: Databases](https://aws.amazon.com/getting-started/deep-dive-databases/)
- [AWS Database Blog](https://aws.amazon.com/blogs/database/)
- [AWS Customer Stories: Databases](https://aws.amazon.com/solutions/case-studies/?customer-references-cards.sort-by=item.additionalFields.publishedDate&customer-references-cards.sort-order=desc&awsf.customer-references-location=*all&awsf.customer-references-segment=*all&awsf.customer-references-product=product%23vpc%7Cproduct%23api-gateway%7Cproduct%23cloudfront%7Cproduct%23route53%7Cproduct%23directconnect%7Cproduct%23elb&awsf.customer-references-category=category%23databases)

## Module 6: Security

- Explain the benefits of the shared responsibility model.
- Describe multi-factor authentication (MFA).
- Differentiate between the AWS Identity and Access Management (IAM) security levels.
- Explain the main benefits of AWS Organizations.
- Describe security policies at a basic level.
- Summarize the benefits of compliance with AWS.
- Explain additional AWS security services at a basic level.

### Shared responsibility model

- customer responsibilities - “security in the cloud” - homeowner
- AWS responsibilities - “security of the cloud” - homebuilder

![](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1639933200/NNsIt-0m45WY040i2hOBFA/tincan/31d9c0cca79c54bdceaf3e938fd424e97c98c7e8/assets/sIlyltjk4kwKozZ1_eyqltDSWURM2V1xC.png)

### User permissions and access

#### AWS Identity and Access Management (IAM)

- **AWS Identity and Access Management (IAM)** enables you to manage access to AWS services and resources securely.

#### AWS account root user

- When you first create an AWS account, you begin with an identity known as the root user.

#### IAM users

- An IAM user is an **identity** that you create in AWS. It represents the **person** or **application** that interacts with AWS services and resources. It consists of a **name** and **credentials**.

#### IAM policies

- An **IAM policy** is a document that **allows or denies permissions** to AWS services and resources.
- Best practice: Follow the security principle of **least privilege** when granting permissions.

#### IAM groups

- An IAM group is a **collection of IAM users**.

#### IAM roles

- An IAM role is an identity that you can assume to gain **temporary** access to permissions.
- Best practice: IAM roles are ideal for situations in which access to services or resources needs to be granted **temporarily**, instead of long-term.

#### Multi-factor authentication (MFA)

- In IAM, multi-factor authentication (MFA) provides an extra layer of security for your AWS account.

### AWS Organizations

- You can use AWS Organizations to consolidate and manage **multiple AWS accounts** within a central location.
- In AWS Organizations, you can centrally control permissions for the accounts in your organization by using <mark>**[service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)**</mark>.
- **Consolidated billing** is another feature of AWS Organizations.

#### Organizational units (OUs)

- In AWS Organizations, you can group accounts into organizational units (OUs) to make it easier to manage accounts with similar business or security requirements.
- In AWS Organizations, you can apply service control policies (SCPs) to the **organization root**, an **individual member account**, or an **OU**.

### Compliance

#### AWS Artifact

- [AWS Artifact](https://aws.amazon.com/artifact) is a service that provides on-demand access to AWS security and compliance reports and select online agreements.
- AWS Artifact consists of two main sections:
  - AWS Artifact Agreements
    - Different types of agreements are offered to address the needs of customers who are subject to specific regulations, such as the **Health Insurance Portability and Accountability Act (HIPAA)**.
  - AWS Artifact Reports.
    - AWS Artifact Reports provide **compliance reports from third-party auditors**.

![](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1639933200/NNsIt-0m45WY040i2hOBFA/tincan/31d9c0cca79c54bdceaf3e938fd424e97c98c7e8/assets/MqGHDcunFO8FzCGV_qiguS0QgqBrh0ktF.jpg)

#### Customer Compliance Center

- The [Customer Compliance Center](https://aws.amazon.com/compliance/customer-center/) contains resources to help you learn more about AWS compliance.

### Denial-of-service attacks

- A **denial-of-service (DoS) attack** is a deliberate attempt to make a website or application unavailable to users.

#### Distributed denial-of-service attacks (DDoS)

To help minimize the effect of DoS and DDoS attacks on your applications, you can use [AWS Shield](https://aws.amazon.com/shield).

#### AWS Shield

- ( 2021-12-20 00:29:04 )
- AWS Shield is a service that protects applications against DDoS attacks.
- AWS Shield provides two levels of protection:
  - AWS Shield Standard
    - automatically protects all AWS customers at no cost. It protects your AWS resources from the most common, frequently occurring types of DDoS attacks.
  - AWS Shield Advanced
    - a paid service that provides detailed attack diagnostics and the ability to detect and mitigate sophisticated DDoS attacks.
    - It also integrates with other services:
      - Amazon CloudFront
      - Amazon Route 53
      - Amazon Elastic Load Balancing (ELB).
      - [AWS WAF(Web Application Firewall)](https://aws.amazon.com/waf/)

### Additional security services

#### AWS Key Management Service (AWS KMS)

- AWS Key Management Service (AWS KMS) enables you to perform encryption operations through the use of cryptographic keys.

#### AWS WAF (Web Application Firewall)

- AWS WAF is a web application firewall that lets you monitor network requests that come into your web applications.
- AWS WAF works together with **Amazon CloudFront** and an **Application Load Balancer**.
- using a <mark>**[web access control list (ACL)](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl.html)**</mark> to protect your AWS resources.

#### Amazon Inspector

- Amazon Inspector helps to improve the security and compliance of applications by running automated security assessments. It checks applications for **security vulnerabilities** and deviations from security best practices, such as open access to Amazon EC2 instances and installations of vulnerable software versions.
- 感覺類似**黑箱掃描**

#### Amazon GuardDuty

- https://aws.amazon.com/guardduty
- a service that provides **intelligent threat detection** for your AWS infrastructure and resources.
- GuardDuty then continuously analyzes data from multiple AWS sources, including **VPC Flow Logs** and **DNS logs**.

### Additional resources

- [Security, Identity, and Compliance on AWS](https://aws.amazon.com/products/security)
- [Whitepaper: Introduction to AWS Security](https://docs.aws.amazon.com/whitepapers/latest/introduction-aws-security/welcome.html)[](https://docs.aws.amazon.com/whitepapers/latest/aws-security-best-practices/know-the-aws-shared-responsibility-model.html)
- [Whitepaper: Amazon Web Services - Overview of Security Processes](https://docs.aws.amazon.com/whitepapers/latest/aws-overview-security-processes/aws-overview-security-processes.pdf)
- [AWS Security Blog](https://aws.amazon.com/blogs/security/)
- [AWS Compliance](https://aws.amazon.com/compliance)
- [AWS Customer Stories: Security, Identity, and Compliance](https://aws.amazon.com/solutions/case-studies/?customer-references-cards.sort-by=item.additionalFields.publishedDate&customer-references-cards.sort-order=desc&awsf.customer-references-location=*all&awsf.customer-references-segment=*all&awsf.customer-references-product=product%23vpc%7Cproduct%23api-gateway%7Cproduct%23cloudfront%7Cproduct%23route53%7Cproduct%23directconnect%7Cproduct%23elb&awsf.customer-references-category=category%23security-identity-compliance)

- ( 2021-12-20 00:38:42 )

## Module 7: Monitoring and Analytics

- Summarize approaches to monitoring your AWS environment.
- Describe the benefits of Amazon CloudWatch.
- Describe the benefits of AWS CloudTrail.
- Describe the benefits of AWS Trusted Advisor.

### Amazon CloudWatch

- Amazon CloudWatch is a web service that enables you to **monitor** and manage various **metrics** and configure **alarm** actions based on data from those metrics.

#### CloudWatch alarms

- With CloudWatch, you can create alarms that automatically **perform actions** if the value of your metric has gone above or below a predefined threshold.

#### CloudWatch dashboard

- The CloudWatch dashboard feature enables you to access all the metrics for your resources from a single location.

### AWS CloudTrail

- AWS CloudTrail records API calls for your account.
- The recorded information includes:
  -  the identity of the API caller
  - the time of the API call
  - the source IP address of the API caller
- Events are typically updated in CloudTrail **within 15 minutes after an API call**.

#### CloudTrail Insights

- ( 2021-12-21 21:56:03 )
-  CloudTrail Insights.
  - optional feature allows CloudTrail to automatically **detect unusual API activities** in your AWS account.

### AWS Trusted Advisor

- AWS Trusted Advisor is a web service that inspects your AWS environment and provides real-time recommendations in accordance with AWS best practices.
- Trusted Advisor compares its findings to AWS best practices in five categories:
  - cost optimization
  - performance
  - security
  - fault tolerance
  - service limits

### Additional resources

- [Management and Governance on AWS](https://aws.amazon.com/products/management-tools)
- [Monitoring and Observability](https://aws.amazon.com/products/management-tools/use-cases/monitoring-and-observability/)
- [Configuration, Compliance, and Auditing](https://aws.amazon.com/products/management-tools/use-cases/configuration-compliance-and-auditing/)
- [AWS Management & Governance Blog](https://aws.amazon.com/blogs/mt/)
- [Whitepaper: AWS Governance at Scale](https://docs.aws.amazon.com/whitepapers/latest/aws-governance-at-scale/introduction.html)

- ( 2021-12-21 21:56:07 )

## Module 8: Pricing and Support.

- ( 2021-12-21 21:58:32 )
- Describe AWS pricing and support models.
- Describe the AWS Free Tier.
- Describe key benefits of AWS Organizations and consolidated billing.
- Explain the benefits of AWS Budgets.
- Explain the benefits of AWS Cost Explorer.
- Explain the primary benefits of the AWS Pricing Calculator.
- Distinguish between the various AWS Support Plans.
- Describe the benefits of AWS Marketplace.

### AWS Free Tier

- The AWS Free Tier enables you to begin using certain services without having to worry about incurring costs for the specified period.
- Three types of offers are available:
  - Always Free
    - e.g. AWS Lambda allows 1 million free requests and up to 3.2 million seconds of compute time per month.
    - e.g. Amazon DynamoDB allows 25 GB of free storage per month.
  - 12 Months Free
    - These offers are free for 12 months following **your initial sign-up date** to AWS.
  - Trials
    - Short-term free trial offers start from the date you activate a particular service.
    - e.g. Amazon Inspector offers a **90-day** free trial.
    - e.g. Amazon Lightsail (a service that enables you to run virtual private servers) offers **750 free hours** of usage over a **30-day** period.

### AWS pricing concepts

- Pay for what you use.
- Pay less when you reserve.
- 