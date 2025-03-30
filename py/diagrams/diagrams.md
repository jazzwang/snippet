# Diagrams - Diagram as Code

[TOC]

> .
> Diagrams lets you draw the cloud system architecture in Python code.
> .

- 平常用比較兇的文字繪圖工具主要是 [mermaid](https://mermaid.js.org/) (流程圖) 或 [PlantUML](https://plantuml.com/) (Sequence Diagram)
- 若是手畫的架構圖，比較常用 draw.io，雖然偶爾會有同仁用 [Excalidraw](https://excalidraw.com/) (手繪風)，但我個人還是比較喜歡可以做純文字版本控制。
- 第一次聽到 `Diagrams` 是有同仁用來畫 AWS 架構圖。最近有一些需求要畫複雜的網路連線架構（比較接近 Deployment Model），所以就來試試看用 Python 話架構圖吧！

## 2024-06-21

- 2024-06-21 10:39:19
- 環境建立：
```bash
$ brew install graphviz ## Diagrams 相依 graphviz，所以要先裝 graphviz。
$ pip3 install diagrams
```

- Graphviz 相依的 Homebrew 套件還挺多的。Linux 上相依套件更多。
- 看樣子還是 mermaid 比較輕量 (JavaScript)。
- PlantUML 是一個 JAR 檔，至少相依 JRE。
> 當然 PlantUML 也可以直接用官方的 Server，如果要繪製的圖不是太複雜的話。

### 實驗一：

```bash
jazzwang:~/git/snippet/python/diagrams$ cat >> quick-start.py << EOF
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("Web Service", show=False):
    ELB("lb") >> EC2("web") >> RDS("userdb")
EOF
jazzwang:~/git/snippet/python/diagrams$ python3 quick-start.py
```
- 結果：
![](web_service.png)

- 2024-06-21 11:47:25
- Graphviz 相依性太多，把實驗移到 Google Cloud Shell 做。

### 實驗二：

```
bash
$ cat >> clustered-web-services.py << EOF
from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS
from diagrams.aws.database import ElastiCache, RDS
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53

with Diagram("Clustered Web Services", show=False):
    dns = Route53("dns")
    lb = ELB("lb")

    with Cluster("Services"):
        svc_group = [ECS("web1"),
                     ECS("web2"),
                     ECS("web3")]

    with Cluster("DB Cluster"):
        db_primary = RDS("userdb")
        db_primary - [RDS("userdb ro")]

    memcached = ElastiCache("memcached")

    dns >> lb >> svc_group
    svc_group >> db_primary
    svc_group >> memcached
EOF
$ python3 clustered-web-services.py
```
- 結果
![](clustered_web_services.png)

### 實驗三：
- 預計用到
  - https://diagrams.mingrammer.com/docs/nodes/onprem
    - diagrams.onprem.client.Client - 筆電
  - https://diagrams.mingrammer.com/docs/nodes/generic
    - diagrams.generic.device.Mobile - 手機
    - diagrams.generic.os.Windows - Windows 作業系統
    - diagrams.generic.virtualization.Vmware - VMWare
  - 參考 https://diagrams.mingrammer.com/docs/nodes/saas
    - diagrams.saas.chat.Teams - Microsoft Teams
- 實作：[lab1.py](lab1.py)
```python
from diagrams import Cluster, Diagram
from diagrams.onprem.client import Client ## 筆電
from diagrams.generic.device import Mobile ## 手機
from diagrams.generic.os import Windows ## Windows 作業系統
from diagrams.generic.virtualization import Vmware ## VMWare
from diagrams.saas.chat import Teams ## Microsoft Teams

with Diagram("Access Summary", show=False):
    laptop = Client("Company-issued Laptop")
    mobile = Mobile("Personal Mobile")

    with Cluster("Internal Services (Intranet)"):
      vdi = Vmware("VMWare Server")
      vm = Windows("Windows VM")

    with Cluster("External Service (Internet)"):
      teams = Teams("Microsoft Teams")

    laptop >> vdi >> vm
    laptop >> teams
    mobile >> teams
```
- 結果:
![](access_summary.png)

### 實驗四：

- 從實驗三結果，看起來 Diagram 在微調一些「文字置中」的支援上沒有很細緻。Edge 線條也不是很方便調整位置。或許產生 dot 檔後，可以再用 Graphviz 語法微調。
- 實驗四來測試一下客製化的 icon
- 參考：https://diagrams.mingrammer.com/docs/nodes/custom
- 實作：[lab2.py](lab2.py)
```python
from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from diagrams.generic.device import Mobile ## 手機
from urllib.request import urlretrieve

with Diagram("Custom with remote icons", show=False, filename="custom_remote", direction="LR"):
    # download the icon image file
    onedrive_url = "https://github.com/sempostma/office365-icons/blob/master/png/256/onedrive.png?raw=true"
    onedrive_icon = "onedrive.png"
    urlretrieve(onedrive_url, onedrive_icon)
    
    onedrive = Custom("OneDrive", onedrive_icon)

    mobile = Mobile("Personal Mobile")

    mobile >> onedrive
```
- 結果：
![](custom_remote.png)

### 備忘：

- 從 Diagrams 原始碼 Github 看起來 icon 並沒有做過 size 正規化 (e.g. 固定為 `256px` )
- 除非想要把圖片弄得很好看，有很多 icon，不然 Diagrams 比較合適畫 AWS, Azure, GCP 架構簡圖。

### 資源：

- Office 365 的 256x256 icon png
  - https://github.com/sempostma/office365-icons/tree/master/png/256
- Microsoft Integration, Azure, Power Platform, Office 365 等 SVG 圖庫
  - https://github.com/sandroasp/Microsoft-Integration-and-Azure-Stencils-Pack-for-Visio
- Microsoft Power Platform icons
  - https://learn.microsoft.com/en-us/power-platform/guidance/icons
- Microsoft Dynamics 365 icons
  - https://learn.microsoft.com/en-us/dynamics365/get-started/icons
- Microsoft 365 architecture templates and icons
  - https://learn.microsoft.com/en-us/microsoft-365/solutions/architecture-icons-templates?view=o365-worldwide
- Azure architecture icons
  - https://learn.microsoft.com/en-us/azure/architecture/icons/
- Microsoft Entra architecture icons (Active Directory)
  - https://learn.microsoft.com/en-us/entra/architecture/architecture-icons
- Microsoft icons
  - https://janbakker.tech/microsoft-icons/
- Microsoft 365 Product Icons
  - https://developer.microsoft.com/en-us/fluentui#/styles/web/m365-product-icons
- 以前常用的兩個找 icon 圖示的線上服務 (Google Slides 有 extension 可以加)
  - https://www.flaticon.com
  - https://thenounproject.com/