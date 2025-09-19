# HTTrack

> HTTrack Website Copier, copy websites to your computer

- Git Repo
  - https://github.com/xroche/httrack
- Website
  - https://www.httrack.com
- User Guide
  - https://www.httrack.com/html/fcguide.html

## 2025-09-19

- 緣起：
  - 最近想要爬一些網站來測試 HTML 建 RAG 當 Knowledge Bot 的練習
  - 想起以前用過 httrack 來爬 HadoopCon 的歷史網頁

### Installation 安裝

- 測試環境 #1： WSL (Windows Subsystem Linux)
```
~/git/snippet$ neofetch
                                     jazzw@JazzBook
################  ################   --------------
################  ################   OS: Windows 11 Home x86_64
################  ################   Host: ASUSTeK COMPUTER INC. ASUS TUF Gaming A15 FA507NV_FA507NV
################  ################   Kernel: 10.0.26100
################  ################   Uptime: 2 days, 9 hours, 31 mins
################  ################   Packages: 22 (scoop)
################  ################   Shell: bash 5.2.37
                                     Resolution: 1920x1080
################  ################   DE: Aero
################  ################   WM: DWM.exe
################  ################   Terminal: Windows Terminal
################  ################   CPU: AMD Ryzen 7 7735HS with Radeon Graphics (16) @ 3.200GHz
################  ################   GPU: AMD Radeon(TM) Graphics
################  ################   GPU: NVIDIA GeForce RTX 4060 Laptop GPU
################  ################   Memory: 17349MiB / 31994MiB
```
```bash
[09/19 14:14:46] sudo apt-get update
[09/19 14:17:09] apt-cache search httrack
[09/19 14:17:30] apt-cache show httrack
[09/19 14:19:10] sudo apt-get -y install httrack
[09/19 14:19:22] httrack --help
```