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
<tr style="background-color:lightyellow;"><td>Q:</td><td>
NixOS 最開始的起源是為了什麼目的？跟容器技術有關嗎？
</td></tr><tr><td>A:</td><td>
NixOS 最開始的起源完全是為了解決學術研究上的「軟體部署（Software Deployment）」與「環境可重現性（Reproducible）」問題。 [1, 2] 
它在 2003 年誕生時，跟當時的容器技術沒有任何關係。事實上，Nix（2003年）比 Docker（2013年）早誕生了整整 10 年。 [2, 3] 
不過，NixOS 的底層邏輯與現代容器技術在「為了解決的問題」上殊途同歸，且現在 Nix 已經成為建構「最完美、最輕量 Docker 鏡像」的地表最強工具之一。 [4, 5] 

## 1. NixOS 的起源與最初目的

Nix 誕生於荷蘭烏特勒支大學（Utrecht University），最初是 Eelco Dolstra 的博士論文研究項目（2006年發表論文：《純函數式軟體部署模型》）。 [1, 2] 
當時 Eelco 及其團隊在開發軟體時，深受傳統 Linux「相依性地獄（Dependency Hell）」所苦。每當更新一個系統套件，其他軟體就可能因為共用函式庫版本改變而崩潰。他的研究目的非常純粹： [1] 

* 數學般的封閉性：將軟體安裝視為純函數（Pure Function），相同的輸入（原始碼、編譯參數）必須永遠得到相同的輸出（二進位檔案）。 [6] 
* 絕對的環境重現：讓科學研究、軟體開發的環境可以 100% 複製到另一台電腦上，不會因為「我的電腦上會動，你的不會」而導致研究無法被驗證。 [1, 3] 

後來在 2006 年，另一位學者 Armijn Hemel 的碩士論文將這個 Nix 套件管理器擴展到了整個 Linux 系統，正式寫出了 NixOS 的原型。 [2] 

## 2. Nix 與容器技術（Docker）的恩怨情仇

雖然 Nix 不是為了容器而生，但當 2013 年 Docker 大封神之後，兩者的哲學產生了非常有趣的對比。

### 💡 兩者解決問題的手段不同：

* Docker 的邏輯（破壞後重建）：「既然各系統的 準標準環境 (FHS) 這麼髒亂，那我就用 Linux 核心的 Namespace/Cgroups 隔出一個虛擬的小世界（貨櫃），在裡面把所需的髒亂環境包起來，假裝它是乾淨的。」 [7, 8] 
* Nix 的邏輯（從根本消除髒亂）：「我們不要大費周章去隔絕世界。我們直接打破傳統 Linux 目錄架構，改用加密雜湊值（Cryptographic Hash）把所有套件徹底孤立存放。這樣同一個系統內本來就可以並存幾百種不同版本的軟體，根本不需要容器來做硬隔離。」 [3, 6, 9, 10] 

### ⚠️ Docker 容器的致命缺點，正是 Nix 的強項：

在傳統的 Docker（使用 Dockerfile 搭配 apt-get update && apt-get install）中，建構出來的鏡像是不可重現的。如果你今天跑一次 docker build，半年後再跑一次，因為 Ubuntu 遠端伺服器的套件庫更新了，你兩次編譯出來的鏡像內容會完全不同，這在嚴謹的科學研究或高安全要求的企業中是個隱患。 [4] 

## 3. 現今 NixOS 與容器技術的完美結合

在現代雲原生（Cloud Native）架構中，NixOS 和 Nix 已經跟容器技術產生了深度的融合：

   1. 地表最安全的「無基底鏡像」（Distroless Images）：
   工程師現在極度喜歡用 Nix 來建構 Docker 鏡像（利用 pkgs.dockerTools）。傳統 Docker 鏡像必須塞入一個輕量的作業系統（如 Alpine 或 Ubuntu），但 Nix 可以精準計算出你的軟體「只」需要哪幾個 /.nix/store 裡面的檔案，並且只把這些檔案打包進 Docker。建構出來的 Docker 鏡像既沒有 /bin/sh，也沒有 apt，體積小到只有幾 MB，且完全沒有多餘套件的漏洞風險。 [11, 12] 
   2. NixOS 內建的宣告式容器（NixOS Containers）：
   NixOS 系統本身自帶一種類似 Docker 的輕量化虛擬化技術（基於 systemd-nspawn）。你甚至可以直接在 configuration.nix 設定檔裡直接宣告好幾個內嵌的容器：
   
   containers.my-web-server = {
     autoStart = true;
     config = { pkgs, ... }: {
       services.httpd.enable = true;
     };
   };
   
   執行一個指令，作業系統跟它裡面的所有微服務容器就會同時同步建構完成。 [7, 8] 

## 總結

NixOS 誕生自解決軟體學術部署與相依性問題的博士論文。它不因容器技術而生，但因為其極致的「可重現性」與「函數式架構」，在當今容器滿天飛的雲端時代，反而成為了精準控制、優化容器環境的頂級開發神兵。 [1, 2, 3, 4, 5, 6] 
您會想了解 NixOS 是如何用來建構 Docker 鏡像，還是對它如何取代您現有的 Docker 開發流程比較有興趣呢？

[1] [https://www.youtube.com](https://www.youtube.com/watch?v=Caao69qWK0A)
[2] [https://en.wikipedia.org](https://en.wikipedia.org/wiki/NixOS)
[3] [https://medium.com](https://medium.com/@Tom1212121/why-nix-when-docker-exists-e6367a0b9afe)
[4] [https://www.facebook.com](https://www.facebook.com/groups/linux.fans.group/posts/9545683282140035/)
[5] [https://thenewstack.io](https://thenewstack.io/nixos-a-combination-linux-os-and-package-manager/)
[6] [https://edolstra.github.io](https://edolstra.github.io/pubs/nixos-jfp-final.pdf)
[7] [https://www.xda-developers.com](https://www.xda-developers.com/nixos-containers-are-pretty-exciting/)
[8] [https://www.xda-developers.com](https://www.xda-developers.com/nixos-containers-are-pretty-exciting/)
[9] [https://news.ycombinator.com](https://news.ycombinator.com/item?id=23251895)
[10] [https://www.youtube.com](https://www.youtube.com/watch?v=9l-U2NwbKOc&t=136)
[11] [https://www.youtube.com](https://www.youtube.com/watch?v=t6goF1dM3ag&t=112)
[12] [https://nixos.wiki](https://nixos.wiki/wiki/NixOS_modules)

</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
NixOS 與 microkernel 的關聯
</td></tr><tr><td>A:</td><td>
NixOS 與 微核心（Microkernel）（例如 L4 微核心系列、seL4 或 GNU Hurd）之間沒有直接的作業系統架構血緣關係。
NixOS 本質上使用的是一個標準的、龐大的 Linux 單體核心（Monolithic Kernel）。然而，它們在「設計哲學」與「系統隔離邏輯」上，有著極高程度的靈魂共鳴。
簡單來說，微核心是在「執行時期（Runtime）的硬體與處理器層級」實施隔離；而 NixOS 則是透過 Nix 在「編譯與軟體相依性層級（Build/Dependency level）」實施相同的隔離哲學。
以下是它們深層的關聯與哲學對比：

## 1. 核心哲學的共鳴：最小權限與徹底隔離

微核心與 NixOS 的誕生，都是為了一改傳統作業系統「牽一髮而動全身」的巨大缺點（這常導致系統崩潰或安全漏洞）。

* 微核心的哲學（特權最小化）：
在傳統單體核心（如 Linux）中，檔案系統、網路驅動、顯示驅動全部以最高權限（Kernel Space / Ring 0）跑在同一個空間。任何一個驅動程式寫錯（例如記憶體溢位），整個作業系統就會藍畫面或當機。
* 微核心的解法：把核心縮到最小（只負責行程間通訊 IPC 和基本記憶體分配），把檔案系統、驅動程式全部趕到使用者空間（User Space）。如果網路驅動崩潰了，它就像普通 App 一樣重啟就好，核心完全不受影響。
* NixOS 的哲學（環境最小化）：
在傳統 Linux 中，所有軟體共用 /usr/lib。只要一個全域函式庫（例如 glibc 或 openssl）升級，所有依賴它的軟體都可能一起崩潰（即相依性地獄）。
* NixOS 的解法：消除全域共享空間。每個軟體都擁有獨立、唯讀、由雜湊值說明的 /nix/store/[hash]-software 目錄。如果軟體 A 升級了，它絕不會影響到需要舊版本函式庫的軟體 B。


## 2. 架構層級的本質差異

雖然兩者都追求「模組化」與「故障隔離」，但落實的層級完全不同：

| 特性 | 微核心 (Microkernel) | NixOS |
|---|---|---|
| 運作層級 | 運行時（Runtime）的 CPU 特權級別與記憶體硬體隔離。 | 編譯與部署時（Compile/Deployment）的檔案路徑與命名空間隔離。 |
| 故障範圍 | 驅動程式當機不影響核心（系統不崩潰）。 | 軟體升級失敗不影響其他軟體（系統可隨時還原）。 |
| 底層核心 | 精簡的核心（如 seL4、Mach）。 | 龐大的 Linux 單體核心。 |
| 主要代價 | 行程間通訊（IPC）帶來的效能損耗。 | 儲存空間（/nix/store 可能會並存多個重複檔案）。 |


## 3. 現實中的交集：用 NixOS 來開發微核心

在現代系統工程中，NixOS 成了開發和編譯微核心系統的最強工具鏈。
微核心（例如專注於極致安全的 seL4）的編譯過程極其複雜。它需要特定版本的交叉編譯器（Cross-compilers）、特定版本的 QEMU 模擬器，以及精準的 C 語言工具鏈。如果開發者的 Ubuntu 系統自動更新了某個套件，編譯出來的微核心鏡像可能就會出錯。
因此，許多尖端微核心研究員會使用 Nix 來定義他們的開發環境（使用 shell.nix 或 [Nix Flakes](https://wiki.nixos.org/wiki/NixOS)）。

* 研究員可以用 30 行 Nix 程式碼，精準鎖定 5 年前的某個特定 GCC 編譯器版本與相依函式庫。
* 不論是在哪台電腦上，只要輸入 nix-shell，就能瞬間變出一個 100% 相同且乾淨的微核心開發環境。

## 總結

NixOS 不是微核心，它是一個披著單體核心外衣，卻實踐了微核心「極致隔離、互不干擾、組件模組化」精神的作業系統。它用軟體工程和純函數的方式，在 Linux 龐大的架構上蓋出了一座結構嚴謹、如同微核心般精準運行的摩天大樓。
您之所以會聯想到微核心，是因為在關注系統的安全性、高可靠度，還是單純對作業系統的底層架構感興趣呢？如果您想進一步了解，我們可以聊聊 NixOS 如何在 Linux 核心之上建立起這種高可靠性的機制。

</td></tr>
</table>
