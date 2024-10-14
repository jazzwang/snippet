# Windows Subsystem for Linux (WSL)

- https://github.com/Microsoft/WSL
- https://learn.microsoft.com/en-us/windows/wsl/

## 原理介紹/環境設定

- [第一篇：Windows Subsystem for Linux (WSL) 原理介紹](https://hackmd.io/@billsun/Bkh8oAmGX?type=view)
- [第二篇：WSL 環境設定](https://hackmd.io/@billsun/BJByCIUHf?type=view)
- [第三篇：WSL 補充內容](https://hackmd.io/@billsun/SyL3pzzQm?type=view)
- [第四篇：WSL 搭配 Visual Studio Code](https://hackmd.io/@billsun/S1LFy-BzQ?type=view)
    - [補充參考：Visual Studio Code](https://hackmd.io/@sysprog/rJPKpohsx?type=view)

## 情境：掛載 USB 隨身碟 - `DrvFs`

- https://devblogs.microsoft.com/commandline/tag/drvfs/
- 參考：https://askubuntu.com/a/1116220
- 範例指令：
```bash
sudo mount -t drvfs G: /mnt/g
```
```bash
sudo mkdir /mnt/h
sudo mount -t drvfs h: /mnt/h -o uid=$(id -u $USER),gid=$(id -g $USER),metadata
```

### 互通性：Windows / Linux / MacOS

- [File format for both Windows and macOS](https://www.reddit.com/r/MacOS/comments/15qqvbj/file_format_for_both_windows_and_macos/)
  - 建議 `extFAT` 格式，但也說明有其缺點。
- 2023-11-30: [exFAT: Advantages and Disadvantages of Extensible FAT](https://www.profolus.com/topics/exfat-advantages-disadvantages-extensible-fat/)

