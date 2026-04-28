# OneDrive on Windows

## 2026-04-27

- 緣起：能否用 command line 指令把 OneDrive 的特定檔案設成 Online Only??
- 參考：
  - https://www.reddit.com/r/macsysadmin/comments/rvts8a/does_any_one_know_the_free_up_space_onedrive/
  - Query and set Files On-Demand states in Windows
    - https://learn.microsoft.com/en-us/sharepoint/files-on-demand-windows
  - （相關，但針對 macOS）Query and set Files On-Demand states on Mac
    - https://learn.microsoft.com/en-us/sharepoint/files-on-demand-mac
  - Reclaim Space from OneDrive Offline Files.
    - https://msendpointsecurity.com/2024/04/25/reclaim-space-from-onedrive-offline-files/
- 參考指令：
  ```powershell
  attrib +U -P <file>
  ```
- [Reclaim Space from OneDrive Offline Files](https://msendpointsecurity.com/2024/04/25/reclaim-space-from-onedrive-offline-files/)一文提供了一個 Powershell 腳本，但需要了解每一行在做什麼，不敢貿然嘗試。
    ```powershell
    # Set root path
    $rootFolderPath = 'C:\users'

    # Get profiles with OneDrive folder
    $subFolders = Get-ChildItem -Path $rootFolderPath -Directory | Where-Object {$_.GetDirectories() -match "OneDrive" }
    foreach ($subfolder in $subfolders) {
        $folderPath = "$($subfolder.FullName)"
        $currentDate = Get-Date

        # Threshold
        $threshHoldDate = $currentDate.AddDays(-90)

        # Get all files in the folder and its subfolders
        $files = Get-ChildItem -Path $folderPath -Recurse -File

        # Iterate through each file and retrieve the last accessed date
        foreach ($file in $files) {
            $lastAccessedDate = $file.LastAccessTime
            If ($lastAccessedDate -le $threshHoldDate) {
                attrib +U -P $file.FullName
            }
        }
    }
    ```