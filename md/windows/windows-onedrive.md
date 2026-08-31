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

## 2026-08-31

- 需求：
  - 工作上因為有大量單檔 2GB 左右的純文字檔案，為了協作需求，上傳到 OneDrive 上。
  - 但久而久之已經佔用太多 OneDrive 容量，想要針對歷史純文字檔進行壓縮（通常可以從 2 GB 壓到 800 MB 左右）。
  - 由於一段時間會把 local 硬碟空間釋出，只保留在雲上。所以本地縱使下指令，也會先把每一個 2GB 下載下來，然後執行 gzip 壓縮，再同步回去 OneDrive 雲儲存上。
- 問題：
  - 像這類型 Cloud Storage，特別又是 Object Storage，有什麼比較好的方法可以直接在雲儲存上做壓縮呢？
<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI Mode
</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
are there cli command to compress OneDrive file directly without sync to local disk?
</td></tr><tr><td>A:</td><td>

No, there is no native CLI command to compress OneDrive files directly on the cloud server without syncing them to a local disk first. [1] 
OneDrive does not expose server-side compression utilities (like zip or tar) via its native API or command-line interface. Any tool that creates a compressed archive must read the file data to compress it.
However, you can achieve this without cluttering or filling up your local storage by using alternative tools and workflows that stream the data directly into memory or temporary cloud environments.

### Workaround 1: Stream and Compress in Memory using Rclone (Recommended)

You can use [Rclone](https://rclone.org/onedrive/) (an open-source cloud CLI tool) combined with standard terminal piping. This downloads the file stream directly into your computer's RAM, compresses it on the fly, and streams it back to OneDrive—never writing the uncompressed file to your physical hard drive. [2, 3] 

* Linux / macOS:

rclone cat remote:path/to/large_file.txt | gzip | rclone rcat remote:path/to/large_file.txt.gz

* Windows (PowerShell):

rclone cat remote:path/to/large_file.txt | Compress-Archive -DestinationPath C:\Windows\Temp\temp.zip; rclone copy C:\Windows\Temp\temp.zip remote:path/to/; Remove-Item C:\Windows\Temp\temp.zip

(Note: Windows requires a temporary file in the Temp folder for Compress-Archive, but it avoids syncing via the native OneDrive client.)

### Workaround 2: Use the OneDrive Web Interface (Automatic Zip)

If your primary goal is to compress multiple files into a single .zip file on your local machine without using local disk space for the initial files:

   1. Log into OneDrive on the web.
   2. Select multiple files or a whole folder.
   3. Click Download.
   4. OneDrive's servers will automatically bundle and compress those files into a single .zip file before sending it to your machine. [4, 5] 

### Workaround 3: Use a Free Cloud Shell (True Server-Side)

If you want to completely avoid using your own internet bandwidth or local machine resources:

   1. Open a cloud environment like GitHub Codespaces, Google Cloud Shell, or a free Azure Cloud Shell.
   2. Install rclone and configure it with your OneDrive account.
   3. Download, zip, and re-upload the files within that cloud virtual machine. This executes at data-center speeds (often gigabits per second) and costs you zero local disk space. [2, 3] 

If you want to set up one of these workarounds, let me know:

* What operating system (Windows, macOS, Linux) you are running.
* If you prefer a pure script solution or a no-code web method.

I can give you the exact step-by-step commands to get it configured!

[1] [https://techcommunity.microsoft.com](https://techcommunity.microsoft.com/discussions/onedriveforbusiness/feature-request-onedrive-cli/4534796)
[2] [https://www.youtube.com](https://www.youtube.com/watch?v=uPCpxMcUW7E)
[3] [https://rclone.org](https://rclone.org/onedrive/)
[4] [https://superuser.com](https://superuser.com/questions/981039/can-you-force-a-single-folder-file-to-sync-with-onedrive)
[5] [https://www.stetson.edu](https://www.stetson.edu/law/offices/it/backup-onedrive-files.php)

</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
</td></tr><tr><td>A:</td><td>
</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
</td></tr><tr><td>A:</td><td>
</td></tr>
</table>