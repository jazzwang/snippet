# minikube

> Run Kubernetes locally

- Git Repo
  - https://github.com/kubernetes/minikube
- Website
  - https://minikube.sigs.k8s.io/

## 2025-08-24

- 緣起：
  - [AWS OpenSearch Workshop](https://catalog.workshops.aws/workshops/c87214bf-11ea-46b7-82d9-4d934c2a7f53/en-US/setup/cfn-setup) 的 [CloudFormation Template](https://static.us-east-1.prod.workshops.aws/public/1db5425d-516a-4a44-98b8-97457a074f85/static/cfns/ops-workshop.yml) 用到 kubectl 來安裝 OpenSearch 與 OpenSearch Dashboard

### 在 WSL 安裝 `minikube`

- Google Gemini 2.5 Flash 建議的安裝步驟比較複雜。實際上[看 minikube 的 Linux 安裝步驟](https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fdebian+package)簡單很多。

> **# aider chat started at 2025-08-24 18:51:03**
> C:\Users\jazzw\.local\bin\aider --no-auto-commits --no-gitignore --model gemini/gemini-2.5-flash-preview-05-20 --chat-history-file minikube.md -m /ask could you create a bash script to install minikube within Ubuntu WSL?  
> Aider v0.86.1  
> Model: gemini/gemini-2.5-flash-preview-05-20 with whole edit format  
> Git repo: .git with 0 files  
> Repo-map: using 4096 tokens, auto refresh  

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
could you create a bash script to install minikube within Ubuntu WSL?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Here's a bash script to install Minikube on Ubuntu WSL, using Docker as its driver.

```bash
#!/bin/bash

# --- Minikube Installation Script for Ubuntu WSL ---
# This script installs Docker, kubectl, and Minikube.
# It uses Docker as the Minikube driver, which is generally
# the most straightforward option for WSL2.

echo "Starting Minikube installation on Ubuntu WSL..."

# 1. Update package lists
echo "1. Updating package lists..."
sudo apt update -y || { echo "Failed to update apt. Exiting."; exit 1; }

# 2. Install necessary dependencies for Docker and kubectl
echo "2. Installing essential dependencies..."
sudo apt install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    wget || { echo "Failed to install dependencies. Exiting."; exit 1; }

# 3. Install Docker Engine
echo "3. Installing Docker Engine..."

# Add Docker's official GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg || { echo "Failed to add Docker GPG key. Exiting."; exit 1; }

# Add Docker APT repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null || { echo "Failed to add Docker repository. Exiting."; exit 1; }

# Update apt package index again with Docker repo
sudo apt update -y || { echo "Failed to update apt after adding Docker repo. Exiting."; exit 1; }

# Install Docker Engine, containerd, and Docker Compose
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin || { echo "Failed to install Docker components. Exiting."; exit 1; }

# Add current user to the docker group to run Docker commands without sudo
echo "Adding current user ($USER) to the 'docker' group..."
sudo usermod -aG docker $USER || { echo "Failed to add user to docker group. Exiting."; exit 1; }

# 4. Install kubectl
echo "4. Installing kubectl..."
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" || { echo "Failed to download kubectl. Exiting."; exit 1; }
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl || { echo "Failed to install kubectl. Exiting."; exit 1; }
rm kubectl # Clean up downloaded binary
echo "kubectl installed successfully."

# 5. Install Minikube
echo "5. Installing Minikube..."
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 || { echo "Failed to download Minikube. Exiting."; exit 1; }
sudo install minikube-linux-amd64 /usr/local/bin/minikube || { echo "Failed to install Minikube. Exiting."; exit 1; }
rm minikube-linux-amd64 # Clean up downloaded binary
echo "Minikube installed successfully."

echo "--- Installation Complete ---"
echo "You may need to restart your WSL terminal or run 'newgrp docker' for the Docker group changes to take effect."
echo "After that, you can start Minikube with: minikube start --driver=docker"
echo "Verify installation with: minikube status"
echo "And kubectl with: kubectl version --client"
```

**How to use the script:**

1.  Save the content above into a file, for example, `install_minikube.sh`.
2.  Make the script executable: `chmod +x install_minikube.sh`
3.  Run the script: `./install_minikube.sh`

**Important Notes:**

*   **Restart or `newgrp docker`**: After the script finishes, you'll need to either close and reopen your WSL terminal or run `newgrp docker` for the changes to your user's group membership to take effect. This allows you to run Docker commands without `sudo`.
*   **WSL2 Requirement**: Minikube with the Docker driver works best on WSL2. If you are on WSL1, you might encounter issues or need to switch to a different driver (like `none`, which requires Docker Desktop running on Windows).
*   **Windows Docker Desktop**: While this script installs Docker *within* your WSL instance, if you prefer to use Docker Desktop running on Windows, you would typically configure your WSL instance to connect to that. However, for a self-contained WSL environment, installing Docker directly in WSL is often simpler.
</td></tr></table>

### 在 Github Codespace 安裝 `minikube`

- [根據 minikube 的 Linux 安裝步驟](https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fdebian+package)，直接下載 deb 安裝檔，就搞定了！
```bash
@jazzwang ➜ /workspaces/codespaces-blank (main) $ cd /tmp/
@jazzwang ➜ /tmp $ curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb
@jazzwang ➜ /tmp $ sudo dpkg -i minikube_latest_amd64.deb
```
- 這樣裝好就有 `minikube` 跟 `kubectl` 指令了
```bash
@jazzwang ➜ /tmp $ which kubectl
/usr/local/bin/kubectl
```