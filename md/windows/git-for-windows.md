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
- ( 2025-01-05 20:51:12 )
- 補充：
  - https://www.msys2.org/docs/pacman/
  - Updating MSYS2 https://www.msys2.org/docs/updating/#potential-issues
  - https://wiki.archlinux.org/title/Pacman/Tips_and_tricks
  - https://gist.github.com/adojos/0abab00dd7e6bd84db39a760fb40a340
- zstd
  - https://facebook.github.io/zstd/
  - Zstandard is a fast compression algorithm, providing high compression ratios.
- 其他參考資料：
  - https://www.pascallandau.com/blog/setting-up-git-bash-mingw-msys2-on-windows/

## 2025-03-06

- 其實後來發現我不需要把 pacman 裝起來，就可以有 git for bash msys 版本的 `tree` 可以用
- https://packages.msys2.org/packages/tree?variant=x86_64
- https://mirror.msys2.org/msys/x86_64/tree-2.2.1-1-x86_64.pkg.tar.zst
```bash
jazzw@JazzBook:/tmp$ mkdir tree
jazzw@JazzBook:/tmp$ cd tree/
jazzw@JazzBook:/tmp/tree$ wget "https://mirror.msys2.org/msys/x86_64/tree-2.2.1-1-x86_64.pkg.tar.zst"
jazzw@JazzBook:/tmp/tree$ tar -xv --zstd -f tree-2.2.1-1-x86_64.pkg.tar.zst
.BUILDINFO
.MTREE
.PKGINFO
usr/
usr/bin/
usr/bin/tree.exe
usr/share/
usr/share/man/
usr/share/man/man1/
usr/share/man/man1/tree.1.gz
jazzw@JazzBook:/tmp/tree$ cp usr/bin/tree.exe ~/scoop/shims/
jazzw@JazzBook:/tmp/tree$ which tree
/c/Users/jazzw/scoop/shims/tree
```

## 2025-09-01

- 緣起：需要 `cpio` 指令來解壓縮 `*.cpz`
- https://packages.msys2.org/packages/cpio?variant=x86_64
- https://mirror.msys2.org/msys/x86_64/cpio-2.15-1-x86_64.pkg.tar.zst
```bash
/tmp$ wget https://mirror.msys2.org/msys/x86_64/cpio-2.15-1-x86_64.pkg.tar.zst
/tmp$ tar -xv --zstd -f cpio-2.15-1-x86_64.pkg.tar.zst
/tmp$ cp usr/bin/cpio.exe ~/scoop/shims/
/tmp$ which cpio
/c/Users/jazzw/scoop/shims/cpio
```

## 2026-01-27

- 緣起：需要 `rsync` 指令來支援 `sftp` 或 `scp` 的續傳
- 套件：
  - https://packages.msys2.org/packages/rsync?variant=x86_64
  - https://packages.msys2.org/packages/libxxhash?variant=x86_64
```bash
~$ cd /tmp/
/tmp$ wget https://mirror.msys2.org/msys/x86_64/rsync-3.4.1-1-x86_64.pkg.tar.zst
/tmp$ tar -xv --zstd -f rsync-3.4.1-1-x86_64.pkg.tar.zst
/tmp$ ./usr/bin/rsync.exe
C:/Users/jazzw/AppData/Local/Temp/usr/bin/rsync.exe: error while loading shared libraries: msys-xxhash-0.dll: cannot open shared object file: No such file or directory
/tmp$ ldd usr/bin/rsync.exe
        ntdll.dll => /c/WINDOWS/SYSTEM32/ntdll.dll (0x7ffdcf120000)
        KERNEL32.DLL => /c/WINDOWS/System32/KERNEL32.DLL (0x7ffdce8b0000)
        KERNELBASE.dll => /c/WINDOWS/System32/KERNELBASE.dll (0x7ffdcc490000)
        msys-crypto-3.dll => /usr/bin/msys-crypto-3.dll (0x4356f0000)
        msys-lz4-1.dll => /usr/bin/msys-lz4-1.dll (0x541680000)
        msys-2.0.dll => /usr/bin/msys-2.0.dll (0x210040000)
        msys-iconv-2.dll => /usr/bin/msys-iconv-2.dll (0x5603f0000)
        msys-zstd-1.dll => /usr/bin/msys-zstd-1.dll (0x48b870000)
        msys-xxhash-0.dll => not found
```
- 解開之後發現缺 `msys-xxhash-0.dll`
- 根據 MSYS2 的 rsync 套件資訊，相依 `libxxhash` 套件，所以抓這個套件來用
```bash
/tmp$ wget https://mirror.msys2.org/msys/x86_64/libxxhash-0.8.3-1-x86_64.pkg.tar.zst
/tmp$ tar -xv --zstd -f libxxhash-0.8.3-1-x86_64.pkg.tar.zst
/tmp$ cp usr/bin/msys-xxhash-0.dll /usr/bin/
/tmp$ cp usr/bin/rsync.exe ~/scoop/shims/
/tmp$ ldd $(which rsync)
        ntdll.dll => /c/WINDOWS/SYSTEM32/ntdll.dll (0x7ffdcf120000)
        KERNEL32.DLL => /c/WINDOWS/System32/KERNEL32.DLL (0x7ffdce8b0000)
        KERNELBASE.dll => /c/WINDOWS/System32/KERNELBASE.dll (0x7ffdcc490000)
        msys-crypto-3.dll => /usr/bin/msys-crypto-3.dll (0x4356f0000)
        msys-lz4-1.dll => /usr/bin/msys-lz4-1.dll (0x541680000)
        msys-iconv-2.dll => /usr/bin/msys-iconv-2.dll (0x5603f0000)
        msys-2.0.dll => /usr/bin/msys-2.0.dll (0x210040000)
        msys-zstd-1.dll => /usr/bin/msys-zstd-1.dll (0x48b870000)
        msys-xxhash-0.dll => /usr/bin/msys-xxhash-0.dll (0x458540000)
/tmp$ rsync
rsync  version 3.4.1  protocol version 32
Copyright (C) 1996-2025 by Andrew Tridgell, Wayne Davison, and others.
Web site: https://rsync.samba.org/
Capabilities:
    64-bit files, 64-bit inums, 64-bit timestamps, 64-bit long ints,
    socketpairs, symlinks, symtimes, hardlinks, no hardlink-specials,
    no hardlink-symlinks, IPv6, atimes, batchfiles, inplace, append, ACLs,
    xattrs, optional secluded-args, iconv, prealloc, stop-at, crtimes
Optimizations:
    no SIMD-roll, no asm-roll, openssl-crypto, no asm-MD5
Checksum list:
    xxh128 xxh3 xxh64 (xxhash) md5 md4 sha1 none
Compress list:
    zstd lz4 zlibx zlib none
Daemon auth list:
    sha512 sha256 sha1 md5 md4

rsync comes with ABSOLUTELY NO WARRANTY.  This is free software, and you
are welcome to redistribute it under certain conditions.  See the GNU
General Public Licence for details.

rsync is a file transfer program capable of efficient remote update
via a fast differencing algorithm.

Usage: rsync [OPTION]... SRC [SRC]... DEST
  or   rsync [OPTION]... SRC [SRC]... [USER@]HOST:DEST
  or   rsync [OPTION]... SRC [SRC]... [USER@]HOST::DEST
  or   rsync [OPTION]... SRC [SRC]... rsync://[USER@]HOST[:PORT]/DEST
  or   rsync [OPTION]... [USER@]HOST:SRC [DEST]
  or   rsync [OPTION]... [USER@]HOST::SRC [DEST]
  or   rsync [OPTION]... rsync://[USER@]HOST[:PORT]/SRC [DEST]
The ':' usages connect via remote shell, while '::' & 'rsync://' usages connect
to an rsync daemon, and require SRC or DEST to start with a module name.

Options
--verbose, -v            increase verbosity
--info=FLAGS             fine-grained informational verbosity
--debug=FLAGS            fine-grained debug verbosity
--stderr=e|a|c           change stderr output mode (default: errors)
--quiet, -q              suppress non-error messages
--no-motd                suppress daemon-mode MOTD
--checksum, -c           skip based on checksum, not mod-time & size
--archive, -a            archive mode is -rlptgoD (no -A,-X,-U,-N,-H)
--no-OPTION              turn off an implied OPTION (e.g. --no-D)
--recursive, -r          recurse into directories
--relative, -R           use relative path names
--no-implied-dirs        don't send implied dirs with --relative
--backup, -b             make backups (see --suffix & --backup-dir)
--backup-dir=DIR         make backups into hierarchy based in DIR
--suffix=SUFFIX          backup suffix (default ~ w/o --backup-dir)
--update, -u             skip files that are newer on the receiver
--inplace                update destination files in-place
--append                 append data onto shorter files
--append-verify          --append w/old data in file checksum
--dirs, -d               transfer directories without recursing
--old-dirs, --old-d      works like --dirs when talking to old rsync
--mkpath                 create destination's missing path components
--links, -l              copy symlinks as symlinks
--copy-links, -L         transform symlink into referent file/dir
--copy-unsafe-links      only "unsafe" symlinks are transformed
--safe-links             ignore symlinks that point outside the tree
--munge-links            munge symlinks to make them safe & unusable
--copy-dirlinks, -k      transform symlink to dir into referent dir
--keep-dirlinks, -K      treat symlinked dir on receiver as dir
--hard-links, -H         preserve hard links
--perms, -p              preserve permissions
--executability, -E      preserve executability
--chmod=CHMOD            affect file and/or directory permissions
--acls, -A               preserve ACLs (implies --perms)
--xattrs, -X             preserve extended attributes
--owner, -o              preserve owner (super-user only)
--group, -g              preserve group
--devices                preserve device files (super-user only)
--copy-devices           copy device contents as a regular file
--write-devices          write to devices as files (implies --inplace)
--specials               preserve special files
-D                       same as --devices --specials
--times, -t              preserve modification times
--atimes, -U             preserve access (use) times
--open-noatime           avoid changing the atime on opened files
--crtimes, -N            preserve create times (newness)
--omit-dir-times, -O     omit directories from --times
--omit-link-times, -J    omit symlinks from --times
--super                  receiver attempts super-user activities
--fake-super             store/recover privileged attrs using xattrs
--sparse, -S             turn sequences of nulls into sparse blocks
--preallocate            allocate dest files before writing them
--dry-run, -n            perform a trial run with no changes made
--whole-file, -W         copy files whole (w/o delta-xfer algorithm)
--checksum-choice=STR    choose the checksum algorithm (aka --cc)
--one-file-system, -x    don't cross filesystem boundaries
--block-size=SIZE, -B    force a fixed checksum block-size
--rsh=COMMAND, -e        specify the remote shell to use
--rsync-path=PROGRAM     specify the rsync to run on remote machine
--existing               skip creating new files on receiver
--ignore-existing        skip updating files that exist on receiver
--remove-source-files    sender removes synchronized files (non-dir)
--del                    an alias for --delete-during
--delete                 delete extraneous files from dest dirs
--delete-before          receiver deletes before xfer, not during
--delete-during          receiver deletes during the transfer
--delete-delay           find deletions during, delete after
--delete-after           receiver deletes after transfer, not during
--delete-excluded        also delete excluded files from dest dirs
--ignore-missing-args    ignore missing source args without error
--delete-missing-args    delete missing source args from destination
--ignore-errors          delete even if there are I/O errors
--force                  force deletion of dirs even if not empty
--max-delete=NUM         don't delete more than NUM files
--max-size=SIZE          don't transfer any file larger than SIZE
--min-size=SIZE          don't transfer any file smaller than SIZE
--max-alloc=SIZE         change a limit relating to memory alloc
--partial                keep partially transferred files
--partial-dir=DIR        put a partially transferred file into DIR
--delay-updates          put all updated files into place at end
--prune-empty-dirs, -m   prune empty directory chains from file-list
--numeric-ids            don't map uid/gid values by user/group name
--usermap=STRING         custom username mapping
--groupmap=STRING        custom groupname mapping
--chown=USER:GROUP       simple username/groupname mapping
--timeout=SECONDS        set I/O timeout in seconds
--contimeout=SECONDS     set daemon connection timeout in seconds
--ignore-times, -I       don't skip files that match size and time
--size-only              skip files that match in size
--modify-window=NUM, -@  set the accuracy for mod-time comparisons
--temp-dir=DIR, -T       create temporary files in directory DIR
--fuzzy, -y              find similar file for basis if no dest file
--compare-dest=DIR       also compare destination files relative to DIR
--copy-dest=DIR          ... and include copies of unchanged files
--link-dest=DIR          hardlink to files in DIR when unchanged
--compress, -z           compress file data during the transfer
--compress-choice=STR    choose the compression algorithm (aka --zc)
--compress-level=NUM     explicitly set compression level (aka --zl)
--skip-compress=LIST     skip compressing files with suffix in LIST
--cvs-exclude, -C        auto-ignore files in the same way CVS does
--filter=RULE, -f        add a file-filtering RULE
-F                       same as --filter='dir-merge /.rsync-filter'
                         repeated: --filter='- .rsync-filter'
--exclude=PATTERN        exclude files matching PATTERN
--exclude-from=FILE      read exclude patterns from FILE
--include=PATTERN        don't exclude files matching PATTERN
--include-from=FILE      read include patterns from FILE
--files-from=FILE        read list of source-file names from FILE
--from0, -0              all *-from/filter files are delimited by 0s
--old-args               disable the modern arg-protection idiom
--secluded-args, -s      use the protocol to safely send the args
--trust-sender           trust the remote sender's file list
--copy-as=USER[:GROUP]   specify user & optional group for the copy
--address=ADDRESS        bind address for outgoing socket to daemon
--port=PORT              specify double-colon alternate port number
--sockopts=OPTIONS       specify custom TCP options
--blocking-io            use blocking I/O for the remote shell
--outbuf=N|L|B           set out buffering to None, Line, or Block
--stats                  give some file-transfer stats
--8-bit-output, -8       leave high-bit chars unescaped in output
--human-readable, -h     output numbers in a human-readable format
--progress               show progress during transfer
-P                       same as --partial --progress
--itemize-changes, -i    output a change-summary for all updates
--remote-option=OPT, -M  send OPTION to the remote side only
--out-format=FORMAT      output updates using the specified FORMAT
--log-file=FILE          log what we're doing to the specified FILE
--log-file-format=FMT    log updates using the specified FMT
--password-file=FILE     read daemon-access password from FILE
--early-input=FILE       use FILE for daemon's early exec input
--list-only              list the files instead of copying them
--bwlimit=RATE           limit socket I/O bandwidth
--stop-after=MINS        Stop rsync after MINS minutes have elapsed
--stop-at=y-m-dTh:m      Stop rsync at the specified point in time
--fsync                  fsync every written file
--write-batch=FILE       write a batched update to FILE
--only-write-batch=FILE  like --write-batch but w/o updating dest
--read-batch=FILE        read a batched update from FILE
--protocol=NUM           force an older protocol version to be used
--iconv=CONVERT_SPEC     request charset conversion of filenames
--checksum-seed=NUM      set block/file checksum seed (advanced)
--ipv4, -4               prefer IPv4
--ipv6, -6               prefer IPv6
--version, -V            print the version + other info and exit
--help, -h (*)           show this help (* -h is help only on its own)

Use "rsync --daemon --help" to see the daemon-mode command-line options.
Please see the rsync(1) and rsyncd.conf(5) manpages for full documentation.
See https://rsync.samba.org/ for updates, bug reports, and answers
rsync error: syntax or usage error (code 1) at main.c(1767) [client=3.4.1]
```
- 應該可以動了～再試試看 `rsync --avzr --progress` 指令是否可以正常運作

## 

- 狀況：因為 `cpio` 不能解壓縮到 git-for-windows 的根目錄（在 Cloud PC 裡面沒有 admin 權限，不能下 sudo 指令建目錄）
- Gemini 3 建議改用 `pax`
- 套件路徑
  - https://packages.msys2.org/packages/pax?variant=x86_64
  - https://mirror.msys2.org/msys/x86_64/pax-20201030-2-x86_64.pkg.tar.zst
- 實測：
```bash
/tmp$ wget https://mirror.msys2.org/msys/x86_64/pax-20201030-2-x86_64.pkg.tar.zst
/tmp$ tar -xv --zstd -f pax-20201030-2-x86_64.pkg.tar.zst
.BUILDINFO
.MTREE
.PKGINFO
usr/
usr/bin/
usr/bin/pax.exe
usr/bin/paxcpio.exe
usr/bin/paxtar.exe
usr/share/
usr/share/licenses/
usr/share/licenses/pax/
usr/share/licenses/pax/LICENSE
usr/share/man/
usr/share/man/man1/
usr/share/man/man1/pax.1.gz
usr/share/man/man1/paxcpio.1.gz
usr/share/man/man1/paxtar.1.gz
/tmp$ cp usr/bin/pax* ~/scoop/shims/
/tmp$ cd ~/scoop/shims/
~/scoop/shims$ ldd pax.exe
        ntdll.dll => /c/WINDOWS/SYSTEM32/ntdll.dll (0x7ff853de0000)
        KERNEL32.DLL => /c/WINDOWS/System32/KERNEL32.DLL (0x7ff852810000)
        KERNELBASE.dll => /c/WINDOWS/System32/KERNELBASE.dll (0x7ff8516d0000)
        msys-2.0.dll => /usr/bin/msys-2.0.dll (0x210040000)
~/scoop/shims$ ldd paxcpio.exe
        ntdll.dll => /c/WINDOWS/SYSTEM32/ntdll.dll (0x7ff853de0000)
        KERNEL32.DLL => /c/WINDOWS/System32/KERNEL32.DLL (0x7ff852810000)
        KERNELBASE.dll => /c/WINDOWS/System32/KERNELBASE.dll (0x7ff8516d0000)
        msys-2.0.dll => /usr/bin/msys-2.0.dll (0x210040000)
~/scoop/shims$ ldd paxtar.exe
        ntdll.dll => /c/WINDOWS/SYSTEM32/ntdll.dll (0x7ff853de0000)
        KERNEL32.DLL => /c/WINDOWS/System32/KERNEL32.DLL (0x7ff852810000)
        KERNELBASE.dll => /c/WINDOWS/System32/KERNELBASE.dll (0x7ff8516d0000)
        msys-2.0.dll => /usr/bin/msys-2.0.dll (0x210040000)
```
