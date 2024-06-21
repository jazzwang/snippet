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