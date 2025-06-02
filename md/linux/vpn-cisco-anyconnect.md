# VPN: Cisco AnyConnect

## 2025-05-31

- 需求：
  - 有一些自動化流程需要內網 Intranet 才能完成，因此想先試試看 Cisco AnyConnect 在 Linux Container 中可否順利連上。
- 參考：
  - 安裝：
    - 2025-05-24: Install Cisco AnyConnect VPN on Ubuntu, Debian, and Fedora
      - https://computingforgeeks.com/install-cisco-anyconnect-on-ubuntu-debian-fedora/
    - 2024-01-22: Installing the Cisco AnyConnect VPN Client on Linux
      - https://www.baeldung.com/linux/cisco-anyconnect-vpn-client
  - 設定：
    - https://computingforgeeks.com/connect-to-vpn-server-with-cisco-anyconnect-from-linux-terminal/
  - 自動化：
    - https://superuser.com/questions/649614/connect-using-anyconnect-from-command-line
  - 其他：
    - Cisco AnyConnect client command line with KeePass support - 這個看起來是 Windows 版搭配 KeePass 的 CLI 工具
      - https://github.com/hacki11/cisco-anyconnect-cli
- 實測：
  - 讀了兩篇安裝文件[[1]](https://computingforgeeks.com/install-cisco-anyconnect-on-ubuntu-debian-fedora/)[[2]](https://www.baeldung.com/linux/cisco-anyconnect-vpn-client)，看起來有兩種安裝方式：
    - 套件安裝: 使用 OpenConnect 套件（直接 apt 就可以安裝）
    - 手動安裝: Cisco AnyConnect 的 tar.gz
  - 有一篇提到因為 OpenConnect 會遇到很多問題，所以才試試看 Cisco AnyConnect 安裝檔
  > I encountered so many issues with OpenConnect and decided to give AnyConnect a try.
  - https://software.cisco.com/download/home/286330811/type/282364313/release/5.1.9.113 看到有 DEB, RPM, TAR (Linux) 跟 DMG (macOS)
    ![](img/anyconnect-packages.png)
- 測試環境：WSL
```bash
jazz@JazzBook:~$ uname -a
Linux JazzBook 6.6.87.1-microsoft-standard-WSL2 #1 SMP PREEMPT_DYNAMIC Mon Apr 21 17:08:54 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux
jazz@JazzBook:~$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 24.04.2 LTS
Release:        24.04
Codename:       noble
```
- 下載 DEB 套件
  - 由於 Cisco 一些授權的限制，縱使完成帳號註冊，仍舊無法順利下載。所以只好退回其他的方案，測試一下 `OpenConnect` 來看看能否達成目標。

## 2025-06-01

- 2025-05-24: Connect to VPN Server on Linux Using **OpenConnect**
  - https://computingforgeeks.com/how-to-connect-to-vpn-server-with-openconnect-ssl-vpn-client-on-linux/
```bash
jazz@JazzBook:~$ sudo apt install openconnect
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
openconnect is already the newest version (9.12-1build5).
0 upgraded, 0 newly installed, 0 to remove and 30 not upgraded.
jazz@JazzBook:~$ dpkg -L openconnect | grep bin
/usr/sbin
/usr/sbin/openconnect
```
- 實測結果：
  - 一直卡在帳號密碼驗證。由於現在多數身份驗證都是靠 redirect 到 Azure AD 做 SAML 認證，所以查了一下 openconnect 對 Azure AD SAML 的支援。
