# Terraform - Getting Started

- by Ned Bellavance

> Terraform is an amazing tool for automating infrastructure in the public and private cloud. This course will teach you the fundamentals of Terraform to deploy infrastructure in a consistent, repeatable manner across multiple services.

- https://app.pluralsight.com/library/courses/terraform-getting-started-2021/table-of-contents

## 2022-10-16

### Infrastructure as Code

- ( 2022-10-16 22:09:44 )
- Define Infrastructure as Code
  > Provisioning infrastructure through **Software** to achieve **consistent** and **predictable** deployments
  - format: JSON or YAML
- Core concepts
  - Defined in Code
  - Store in source control
  - **Declarative** or **Imperative**
    - Terraform is `Declarative`
  - **Idempotent** and **consistent**
    - idempotent - 記住 state - 沒有改 code 就不用再做一次
  - **Push** or **Pull**
    - Terraform is `push-type` model
- Benefits
  - Automated deployment
  - Repeatable process
  - Consistent environment
  - Reusable components
  - Documented architecture

### First Terraform Confiration

- ( 2022-10-16 22:47:22 )
- What is Terraform?
  - **Infrastructure Automation Tool**
  - **Open Source** and Vendor agnorstic
  - Single binary compiled from **Go**
  - Declarative Syntax
  - HashiCorp Configuration Language (**HCL**) or **JSON**
  - Push based deployment
- Core Components
  - Executable
  - Configuration files
  - Provider plugins
    - registry.terraform.io
  - State data
- Install Terraform
  - ( 2022-10-16 23:37:18 )
  - https://github.com/ned1313/Getting-Started-Terraform
