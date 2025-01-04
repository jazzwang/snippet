# Git for Windows & MSYS2

## 2024-01-04

- Git for Windows (Git Bash) 是基於 MSYS2 (內含 MINGWIN64, MSYS, Cygwin) 精簡後的版本。沒有包括 MSYS2 的套件管理 `pacman` (從 Arch Linux 移植到 MSYS2)。
- 原本想要找 `tree` 這個指令的套件，可是 Windows 上 Scoop 並沒有，所以念頭一轉，來試試看幫 Git Bash 加上 `pacman` 好了。
- ( 2025-01-04 16:31:39 )
- 做了兩次實驗，因為會把用 scoop 安裝的 Git Bash 環境弄亂，所以反安裝 scoop 的 git 套件，再測試一次流程。
```powershell
PS C:\Users\jazzw> scoop uninstall git
PS C:\Users\jazzw> scoop install git

Scoop uses Git to update itself. Run 'scoop install git' and try again.
Installing 'git' (2.47.1) [64bit] from 'main' bucket
'git' (2.47.1) was installed successfully!
Notes
-----
Set Git Credential Manager Core by running: "git config --global credential.helper manager"

To add context menu entries, run 'C:\Users\jazzw\scoop\apps\git\current\install-context.reg'

To create file-associations for .git* and .sh files, run 'C:\Users\jazzw\scoop\apps\git\current\install-file-associations.reg'
```
- 重新安裝以後，我先下載 MSYS2 `pacman` 套件的相依套件
  - https://packages.msys2.org/packages/pacman?variant=x86_64
    > Dependencies:
    > * bash >=4.2.045 ### Git Bash 自己就有包含 Bash
    > * bzip2          ### Git Bash 有包含 bzip2
    > * curl           ### Git Bash 有包含 curl
    > * gettext        ### 需要下載
    > * gnupg          ### Git Bash 有包含 gnupg
    > * msys2-keyring  ### 需要下載
    > * pacman-mirrors ### 需要下載
    > * which          ### Git Bash 有包含 which
    > * xz             ### Git Bash 有包含 xz
    > * zstd           ### 需要下載
   - https://packages.msys2.org/packages/gettext?variant=x86_64
   - https://packages.msys2.org/packages/zstd?variant=x86_64
   - https://packages.msys2.org/packages/msys2-keyring?variant=x86_64
   - https://packages.msys2.org/packages/pacman-mirrors?variant=x86_64
```bash
PS C:\Users\jazzw> bash
jazzw@JazzBook:~$ cd /tmp/
jazzw@JazzBook:/tmp$ mkdir -p pacman
jazzw@JazzBook:/tmp/pacman$ wget https://mirror.msys2.org/msys/x86_64/pacman-6.1.0-10-x86_64.pkg.tar.zst
jazzw@JazzBook:/tmp/pacman$ wget https://mirror.msys2.org/msys/x86_64/msys2-keyring-1~20241007-1-any.pkg.tar.zst
jazzw@JazzBook:/tmp/pacman$ wget https://mirror.msys2.org/msys/x86_64/pacman-mirrors-20241217-1-any.pkg.tar.zst
jazzw@JazzBook:/tmp/pacman$ wget https://mirror.msys2.org/msys/x86_64/gettext-0.22.4-1-x86_64.pkg.tar.zst
jazzw@JazzBook:/tmp/pacman$ wget https://mirror.msys2.org/msys/x86_64/zstd-1.5.6-1-x86_64.pkg.tar.zst
```
- 手動把缺的套件檔案下載完畢，接著手動解開：
```bash
jazzw@JazzBook:/tmp/pacman$ cd /
jazzw@JazzBook:/$ tar -xv --zstd -f /tmp/pacman/gettext-0.22.4-1-x86_64.pkg.tar.zst
tar (child): zstd: Cannot exec: No such file or directory
tar (child): Error is not recoverable: exiting now
tar: Child returned status 2
tar: Error is not recoverable: exiting now
```
- 好吧，因為 `zstd` 套件自己也是 zstd 壓縮檔，只好先用 scoop 安裝 zstd
```bash
jazzw@JazzBook:/$ scoop install zstd
jazzw@JazzBook:/$ tar -xv --zstd -f /tmp/pacman/gettext-0.22.4-1-x86_64.pkg.tar.zst
jazzw@JazzBook:/$ tar -xv --zstd -f /tmp/pacman/zstd-1.5.6-1-x86_64.pkg.tar.zst
jazzw@JazzBook:/$ tar -xv --zstd -f /tmp/pacman/msys2-keyring-1~20241007-1-any.pkg.tar.zst
jazzw@JazzBook:/$ tar -xv --zstd -f /tmp/pacman/pacman-mirrors-20241217-1-any.pkg.tar.zst
jazzw@JazzBook:/$ tar -xv --zstd -f /tmp/pacman/pacman-6.1.0-10-x86_64.pkg.tar.zst
```
- 清掉一些手動解壓縮造成的垃圾：
```
jazzw@JazzBook:/$ rm .BUILDINFO .INSTALL .MTREE .PKGINFO
```
- 先前會遇到套件庫金鑰錯誤的問題，所以手動匯入 msys2-keyring
```bash
jazzw@JazzBook:/$ pacman-key --add /usr/share/pacman/keyrings/msys2.gpg
==> 錯誤： 您的權限不足以讀取 pacman 鑰匙圈。
==> 使用「pacman-key --init」修正鑰匙圈權限。
jazzw@JazzBook:/$ pacman-key --init
gpg: /etc/pacman.d/gnupg/trustdb.gpg: trustdb created
gpg: no ultimately trusted keys found
gpg: starting migration from earlier GnuPG versions
gpg: porting secret keys from '/etc/pacman.d/gnupg/secring.gpg' to gpg-agent
gpg: migration succeeded
==> 正在生成 pacman 主控金鑰。這可能需要一點時間。
gpg: Generating pacman keyring master key...
gpg: directory '/etc/pacman.d/gnupg/openpgp-revocs.d' created
gpg: revocation certificate stored as '/etc/pacman.d/gnupg/openpgp-revocs.d/19D7142353439E8CD82DCD89A7A2CB53A67EF270.rev'
gpg: Done
==> 正在更新信任資料庫...
gpg: marginals needed: 3  completes needed: 1  trust model: pgp
gpg: depth: 0  valid:   1  signed:   0  trust: 0-, 0q, 0n, 0m, 0f, 1u
jazzw@JazzBook:/$ pacman-key --add /usr/share/pacman/keyrings/msys2.gpg
==> 正在更新信任資料庫...
gpg: no need for a trustdb check
jazzw@JazzBook:/$ pacman-key --refresh-keys
gpg: error retrieving 'alexey.pawlow@gmail.com' via WKD: No data
gpg: error reading key: No data
gpg: refreshing 1 key from hkps://keyserver.ubuntu.com
gpg: key F40D263ECA25678A: "Alexey Pavlov (Alexpux) <alexey.pawlow@gmail.com>" not changed
gpg: Total number processed: 1
gpg:              unchanged: 1
gpg: error retrieving 'david.macek.0@gmail.com' via WKD: No data
gpg: error reading key: No data
gpg: refreshing 1 key from hkps://keyserver.ubuntu.com
gpg: key 790AE56A1D3CFDDC: "David Macek (MSYS2 master key) <david.macek.0@gmail.com>" not changed
gpg: Total number processed: 1
gpg:              unchanged: 1
gpg: error retrieving 'martellmalone@gmail.com' via WKD: No data
gpg: error reading key: No data
gpg: refreshing 1 key from hkps://keyserver.ubuntu.com
gpg: key DA7EF2ABAEEA755C: "Martell Malone (martell) <martellmalone@gmail.com>" not changed
gpg: Total number processed: 1
gpg:              unchanged: 1
gpg: error retrieving 'reiter.christoph@gmail.com' via WKD: No data
gpg: error reading key: No data
gpg: refreshing 1 key from hkps://keyserver.ubuntu.com
gpg: key 755B8182ACD22879: "Christoph Reiter (MSYS2 master key) <reiter.christoph@gmail.com>" not changed
gpg: Total number processed: 1
gpg:              unchanged: 1
gpg: error retrieving 'icquinteiro@gmail.com' via WKD: No data
gpg: error reading key: No data
gpg: refreshing 1 key from hkps://keyserver.ubuntu.com
gpg: key 9F418C233E652008: "Ignacio Casal Quinteiro <icquinteiro@gmail.com>" not changed
gpg: Total number processed: 1
gpg:              unchanged: 1
gpg: error retrieving 'mingw.android@gmail.com' via WKD: No data
gpg: error reading key: No data
gpg: refreshing 1 key from hkps://keyserver.ubuntu.com
gpg: key BBE514E53E0D0813: "Ray Donnelly (MSYS2 Developer - master key) <mingw.android@gmail.com>" not changed
gpg: Total number processed: 1
gpg:              unchanged: 1
gpg: error retrieving 'alexpux@gmail.com' via WKD: No data
gpg: error reading key: No data
gpg: refreshing 1 key from hkps://keyserver.ubuntu.com
gpg: key 5F92EFC1A47D45A1: "Alexey Pavlov (Alexpux) <alexpux@gmail.com>" not changed
gpg: Total number processed: 1
gpg:              unchanged: 1
gpg: error retrieving 'david.macek.0@gmail.com' via WKD: No data
gpg: error reading key: No data
gpg: refreshing 1 key from hkps://keyserver.ubuntu.com
gpg: key 974C8BE49078F532: "David Macek <david.macek.0@gmail.com>" not changed
gpg: Total number processed: 1
gpg:              unchanged: 1
gpg: error retrieving 'reiter.christoph@gmail.com' via WKD: No data
gpg: error reading key: No data
gpg: refreshing 1 key from hkps://keyserver.ubuntu.com
gpg: key FA11531AA0AA7F57: "Christoph Reiter (MSYS2 development key) <reiter.christoph@gmail.com>" not changed
gpg: Total number processed: 1
gpg:              unchanged: 1
gpg: error retrieving 'me@martellmalone.com' via WKD: General error
gpg: error reading key: General error
gpg: refreshing 1 key from hkps://keyserver.ubuntu.com
gpg: key 794DCF97F93FC717: "Martell Malone (martell) <me@martellmalone.com>" not changed
gpg: Total number processed: 1
gpg:              unchanged: 1
gpg: error retrieving 'martellmalone@gmail.com' via WKD: No data
gpg: error reading key: No data
gpg: refreshing 1 key from hkps://keyserver.ubuntu.com
gpg: key D595C9AB2C51581E: "Martell Malone (MSYS2 Developer) <martellmalone@gmail.com>" not changed
gpg: Total number processed: 1
gpg:              unchanged: 1
gpg: error retrieving 'mingw.android@gmail.com' via WKD: No data
gpg: error reading key: No data
gpg: refreshing 1 key from hkps://keyserver.ubuntu.com
gpg: key 4DF3B7664CA56930: "Ray Donnelly (MSYS2 Developer) <mingw.android@gmail.com>" not changed
gpg: Total number processed: 1
gpg:              unchanged: 1
jazzw@JazzBook:/$ pacman -Syvv
Root      : /
Conf File : /etc/pacman.conf
DB Path   : /var/lib/pacman/
Cache Dirs: /var/cache/pacman/pkg/
Hook Dirs : /usr/share/libalpm/hooks/  /etc/pacman.d/hooks/
Lock File : /var/lib/pacman/db.lck
Log File  : /var/log/pacman.log
GPG Dir   : /etc/pacman.d/gnupg/
Targets   : 無
:: 正在同步軟體包資料庫…
 clangarm64                                                       430.1 KiB  66.0 KiB/s 00:07 [######################################################] 100%
 mingw32                                                          203.2 KiB  39.1 KiB/s 00:05 [######################################################] 100%
 mingw64                                                          452.0 KiB  58.1 KiB/s 00:08 [######################################################] 100%
 ucrt64                                                           482.5 KiB  59.8 KiB/s 00:08 [######################################################] 100%
 clang64                                                          470.8 KiB  67.2 KiB/s 00:07 [######################################################] 100%
 msys                                                             323.3 KiB  92.9 KiB/s 00:03 [######################################################] 100%
錯誤：clangarm64：來自 Christoph Reiter (MSYS2 development key) <reiter.christoph@gmail.com> 的簽章信任等級不明
錯誤：mingw32：來自 Christoph Reiter (MSYS2 development key) <reiter.christoph@gmail.com> 的簽章信任等級不明
錯誤：mingw64：來自 Christoph Reiter (MSYS2 development key) <reiter.christoph@gmail.com> 的簽章信任等級不明
錯誤：ucrt64：來自 Christoph Reiter (MSYS2 development key) <reiter.christoph@gmail.com> 的簽章信任等級不明
錯誤：clang64：來自 Christoph Reiter (MSYS2 development key) <reiter.christoph@gmail.com> 的簽章信任等級不明
錯誤：msys：來自 Christoph Reiter (MSYS2 development key) <reiter.christoph@gmail.com> 的簽章信任等級不明
錯誤：同步所有資料庫失敗 (資料庫不正確或損毀 (PGP 簽章))
jazzw@JazzBook:/$ pacman-key --populate
==> 正從 msys2.gpg 附加金鑰...
==> 正於本地端簽署鑰匙圈中信任的金鑰...
  -> 本機已簽署 5 個金鑰。
==> 正在匯入擁有者的信任值...
gpg: inserting ownertrust of 4
gpg: setting ownertrust to 4
gpg: setting ownertrust to 4
gpg: setting ownertrust to 4
gpg: setting ownertrust to 4
==> 正在停用鑰匙圈中被撤銷的金鑰...
  ->  4 個金鑰已停用。
==> 正在更新信任資料庫...
gpg: Note: third-party key signatures using the SHA1 algorithm are rejected
gpg: (use option "--allow-weak-key-signatures" to override)
gpg: marginals needed: 3  completes needed: 1  trust model: pgp
gpg: depth: 0  valid:   1  signed:   5  trust: 0-, 0q, 0n, 0m, 0f, 1u
gpg: depth: 1  valid:   5  signed:   3  trust: 0-, 0q, 0n, 5m, 0f, 0u
gpg: depth: 2  valid:   2  signed:   0  trust: 2-, 0q, 0n, 0m, 0f, 0u
gpg: next trustdb check due at 2025-04-05
jazzw@JazzBook:/$ pacman -Sy
:: 正在同步軟體包資料庫…
 clangarm64 已經是最新版本
 mingw32 已經是最新版本
 mingw64 已經是最新版本
 ucrt64 已經是最新版本
 clang64 已經是最新版本
 msys 已經是最新版本
```
- 看起來需要的金鑰認證與套件庫都準備好了，那來下載所需要的套件吧！！
```bash
jazzw@JazzBook:/$ pacman -S tree
正在解決依賴關係…
正在檢查衝突的軟體包…

軟體包 (1) tree-2.1.3-1

總計下載大小：  0.04 MiB
總計安裝大小：  0.07 MiB

:: 進行安裝嗎？ [Y/n]
:: 正在接收軟體包…
 tree-2.1.3-1-x86_64                                               38.4 KiB  9.04 KiB/s 00:04 [######################################################] 100%
(1/1) 正在檢查鑰匙圈中的鑰匙                                                                  [######################################################] 100%
(1/1) 正在檢查軟體包完整性                                                                    [######################################################] 100%
(1/1) 正在載入軟體包檔案                                                                      [######################################################] 100%
(1/1) 正在檢查檔案衝突                                                                        [######################################################] 100%
(1/1) 正在檢查可用磁碟空間                                                                    [######################################################] 100%
:: 正在處理軟體包變更…
(1/1) 正在安裝 tree
```
- 這樣就有 `tree` 這個指令了。
```bash
jazzw@JazzBook:/$ which tree
/usr/bin/tree
```
- 從 `ldd` 查到的結果，會相依 `msys-2.0.dll`。意思就只能在 Git Bash (MSYS2） 環境裡面用。
```
jazzw@JazzBook:~$ ldd /usr/bin/tree.exe
        ntdll.dll => /c/WINDOWS/SYSTEM32/ntdll.dll (0x7ff861560000)
        KERNEL32.DLL => /c/WINDOWS/System32/KERNEL32.DLL (0x7ff860650000)
        KERNELBASE.dll => /c/WINDOWS/System32/KERNELBASE.dll (0x7ff85edd0000)
        msys-2.0.dll => /usr/bin/msys-2.0.dll (0x210040000)
```
- 如果要讓 PowerShell 或 CMD 也能用，需要把 `msys-2.0.dll` 複製到 `C:/WINDOWS/System32` 且要改 PATH 的優先順序。Windows 11 已經有帶 `C:\Windows\System32\tree.com`
```cmd
Microsoft Windows [Version 10.0.26100.2605]
(c) Microsoft Corporation. All rights reserved.

C:\Users\jazzw>where tree
C:\Windows\System32\tree.com
```