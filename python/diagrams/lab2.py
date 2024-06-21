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