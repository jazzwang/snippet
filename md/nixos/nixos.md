# NixOS

- Website
  - https://nixos.org/
- Wiki
  - https://wiki.nixos.org/wiki/NixOS

## 2026-06-02

<table><tr style="background-color:lightyellow;"><td>Q:</td><td>
what is Nix? NixOS?
</td></tr><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI Mode
</td></tr><tr><td>A:</td><td>

Nix is a functional package manager, while NixOS is an entire Linux operating system built on top of that package manager. Together, they represent a radically different approach to computing that focuses on being declarative, reproducible, and immutable. [1, 2, 3] 
Instead of installing software imperatively (e.g., running sudo apt install or brew install), you write a text file that lists exactly what your environment or system should look like, and the software builds it cleanly from that blueprint. [4, 5] 

## 📦 1. What is Nix?

[Nix](https://nixos.org/) is an open-source tool that handles package management and build configurations. You can install it on top of normal operating systems like Ubuntu, Fedora, or macOS. [1, 2, 6, 7, 8] 

* The Nix Store (/nix/store): Nix does not install binaries into global, shared folders like /usr/bin or /lib. Instead, every package lives in its own isolated directory inside /nix/store, named with a unique cryptographic hash. This hash represents every single dependency and compiler configuration used to build that program. [6, 9, 10] 
* No More "Dependency Hell": Because packages are strictly isolated, you can simultaneously install and run multiple versions of the exact same software (e.g., Python 3.8 and Python 3.12) without them breaking each other. [1, 6, 11, 12, 13] 
* The Nix Language: Packages are defined using a custom, pure functional programming language also called Nix. [2, 14] 

## 🖥️ 2. What is NixOS?
[NixOS](https://wiki.nixos.org/wiki/NixOS) is an entire Linux distribution where the operating system itself—including the kernel, drivers, system services, system users, and desktop environments—is built entirely by the Nix package manager. [15] 

* The Single Source of Truth: Your complete OS layout is defined in a text file (usually called configuration.nix). If you want to enable an SSH server, configure a firewall, or install a desktop setup, you simply type a few lines into this file and run nixos-rebuild switch. [3, 16, 17, 18, 19] 
* Atomic Upgrades: When you update the configuration, NixOS does not overwrite your existing system files. It builds a brand new, isolated layer (called a generation) and seamlessly swaps the system pointer to it. If the power cuts mid-update, your system remains perfectly intact. [3] 
* Flawless Bootloader Rollbacks: If a software update completely breaks your desktop environment or breaks a graphics driver, you don't need to reinstall the OS. You can just reboot your machine and select an older, working system "generation" straight from the boot menu to undo the changes instantly. [3, 20] 

## 📊 Key Differences at a Glance

| Feature [1, 2, 3, 4, 6, 7, 8, 14, 15, 16, 21] | Nix (The Package Manager) | NixOS (The Operating System) |
|---|---|---|
| What is it? | A command-line package manager and build environment tool. | A standalone Linux distribution built around Nix. |
| Where does it run? | Linux distros (Ubuntu, Arch, Debian) and macOS. | Runs directly on your bare metal computer hardware or a VM. |
| What does it manage? | Individual project environments, compiler chains, and software packages. | The complete operating system kernel, system services, users, and disks. |
| Primary Use Case | Sharing predictable dev environments with teammates so everyone has the exact same software toolchain. | Building immutable, stable servers or bulletproof personal desktop setups. |

## 🛠️ Why Researchers and Developers Use It
For an advanced user, Nix solves the "it works on my machine" problem. You can write a tiny configuration file for a data science experiment or an AI agent repository, check it into GitHub, and any colleague anywhere can spin up the exact same operating environment down to the exact library sub-dependencies. [1, 4, 22] 
If you are interested in exploring further, would you like to see a simple Nix development shell layout to see how it can isolate software tools for a specific research project?

[1] https://nixos.org
[2] [https://en.wikipedia.org](https://en.wikipedia.org/wiki/NixOS)
[3] [https://www.youtube.com](https://www.youtube.com/watch?v=9OMDnZWXjn4)
[4] [https://www.reddit.com](https://www.reddit.com/r/linux4noobs/comments/1cktkfc/can_someone_explain_nixos_to_me/)
[5] [https://www.youtube.com](https://www.youtube.com/watch?v=Ee0TWdR5kGE&t=79)
[6] [https://nixos.wiki](https://nixos.wiki/wiki/Nix_package_manager)
[7] [https://github.com](https://github.com/NixOS/nix)
[8] [https://nixos.org](https://nixos.org/nixpkgs/manual/)
[9] [https://nix.dev](https://nix.dev/manual/nix/prev-stable/)
[10] [https://en.wikipedia.org](https://en.wikipedia.org/wiki/Nix_%28package_manager%29)
[11] [https://distrowatch.com](https://distrowatch.com/weekly.php?issue=20240401)
[12] [https://ostechnix.com](https://ostechnix.com/getting-started-nix-package-manager/)
[13] [https://lazamar.co.uk](https://lazamar.co.uk/nix-versions/?package=python3.8-numpy&version=1.17.3&fullName=python3.8-numpy-1.17.3&keyName=python38Packages.numpy&revision=bca9437d1eae9519b61a58f2593f25f65494f8e9&channel=nixpkgs-unstable)
[14] [https://nixos.org](https://nixos.org/learn/)
[15] [https://wiki.nixos.org](https://wiki.nixos.org/wiki/NixOS)
[16] [https://medium.com](https://medium.com/@Erik_Krieg/what-is-nix-nixos-aab5610f0d7f)
[17] [https://zero-to-nix.com](https://zero-to-nix.com/concepts/nixos/)
[18] [https://mtlynch.io](https://mtlynch.io/notes/simple-go-web-service-nixos/)
[19] [https://medium.com](https://medium.com/thenixos/how-to-configure-zsh-and-oh-my-zsh-in-nixos-6ddfbc3f0da3)
[20] [https://www.youtube.com](https://www.youtube.com/watch?v=CwfKlX3rA6E&t=25)
[21] https://nixos.org
[22] [https://numtide.com](https://numtide.com/blog/nix-docker-or-both/)

</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
NixOS 跟 Debian / CentOS 的關聯性
</td></tr><tr><td>A:</td><td>
NixOS 與 Debian 或 CentOS（現主要為 Stream 體系）之間沒有任何直接的血緣關係。它們代表了 Linux 世界中截軟不同的設計哲學 [1, 2]。
簡單來說，Debian 與 CentOS 是「傳統命令式（Imperative）」作業系統的代表 [1, 3]；而 NixOS 則是「現代宣告式（Declarative）」與「不可變（Immutable）」作業系統的革命者 [1, 2]。
以下為您拆解它們之間的本質關聯與核心差異：

## 1. 沒有血緣關係，全部獨立開發

Linux 發行版通常有家族譜系（例如：Ubuntu 衍生自 Debian [4]；Rocky Linux/AlmaLinux 衍生自 RHEL/CentOS [5]）。

* Debian/CentOS：歷史悠久，擁有各自獨立的原生套件管理器（Debian 使用 apt/.deb [6, 7]；CentOS 使用 dnf/.rpm [3, 8]）。
* NixOS：完全從零開始獨立開發，不依賴任何現有的 Linux 家族 [1, 2]。它唯一的基礎就是 Nix 套件管理器 [1, 2]。

## 2. 核心哲學的「降維打擊」：命令式 vs. 宣告式

這三者最大的關聯，在於它們處理「系統管理」與「軟體安裝」的邏輯完全相反：

### 傳統陣營（Debian / CentOS）：狀態是累積出來的

在 Debian 或 CentOS 中，系統的狀態是由你執行指令的先後順序決定的 [1, 3]。

* 作法：你手動輸入 sudo apt install python3 或 sudo dnf install nginx [6, 8]。
* 缺點（狀態漂移）：時間久了，你根本不記得自己修改了 /etc/底下的哪些設定檔 [1]。兩台同時安裝的 Debian 伺服器，會因為維運人員的操作順序不同，最後變成完全不同的環境（俗稱「雪花伺服器」）。
* 移除殘留：移除軟體時，經常會留下孤立的依賴檔案或髒亂的設定檔 [1]。

### 革命陣營（NixOS）：狀態是描述出來的

在 NixOS 中，你不被允許（也無法）透過輸入指令來安裝全域軟體 [1, 2]。

* 作法：你必須在一個文字檔（configuration.nix）中寫下你「期望」的系統長相 [1, 2]。

### NixOS 設定檔片段範例

```
environment.systemPackages = [ pkgs.python3 pkgs.nginx ];
services.nginx.enable = true;
```

寫完後執行 nixos-rebuild switch，系統就會自動變成你描述的樣子 [1, 2]。
* 優點（絕對一致）：只要這份文字檔不變，在 100 台電腦上安裝 NixOS，編譯出來的系統不論是核心、驅動還是軟體，都會百分之百完全相同 [1, 2]。

## 3. 目錄結構的根本重組

| 特性 | Debian / CentOS (傳統架構) | NixOS (新世代架構) |
|---|---|---|
| 檔案配置標準 | 遵循 FHS 標準（有 /usr/bin, /lib） [1, 9] | 完全打破 FHS（沒有全域的 /bin 或 /lib） [1, 2] |
| 軟體存放位置 | 軟體散落在全域目錄，容易發生版本衝突 [1] | 集中在 /nix/store/，以加密雜湊值隔離 [1, 2] |
| 多版本共存 | 極難（例如同時裝兩版 Node.js 需要額外工具） | 極易（同一系統可同時執行十個不同版本的軟體） [1, 2] |
| 設定檔管理 | 維運人員手動修改 /etc/ 底下的各個檔案 [1] | 全由 Nix 根據主設定檔統一生成，/etc 大多是唯讀符號連結 [1, 2] |

## 4. 容錯與復原能力（Rollback）

* Debian / CentOS：如果升級過程中斷、或新版驅動導致黑畫面，你必須進入 Rescue 模式手動修復，或者依賴外部的虛擬機快照（Snapshot） [1]。
* NixOS：每次修改設定檔，系統就會生成一個獨立的「世代（Generation）」 [1, 2]。如果系統改爛了開不了機，只要在開機選單（Grub）直接選取前一個世代，就能 100% 毫秒級還原到正常狀態 [1, 2]。

## 總結：您該如何選擇？

這三者在當今的開發與研究環境中各有定位：

   1. CentOS (Stream/Rocky/Alma)：適合企業傳統架構、需要極度維穩的舊型資料庫、或與 RHEL 生態系高度綁定的企業環境 [3, 5]。
   2. Debian：Linux 界穩定的基石 [4]。如果你追求開箱即用、龐大的社群資源、遇到問題隨手都能 Google 到解答，或者要建立極輕量化的 Docker 容器，Debian 仍是首選 [4, 7]。
   3. NixOS：適合追求「環境絕對可重現」的研究員與開發者 [1, 2]。如果你常常因為「在我的電腦上會動，在別人的電腦上就不動」而崩潰，或者需要頻繁切換複雜的實驗環境（如跨領域的 Linked Data 處理工具鏈），NixOS（或單獨在 Debian 上安裝 Nix 核心）能提供地表最強的環境控制力 [1, 2]。

如果您打算將研究環境轉移到這種「可重現」的體系，您會希望將它部署在個人工作站（筆電/桌機）還是遠端的學術伺服器上呢？這會影響到設定的複雜度。
</td></tr>
</table>