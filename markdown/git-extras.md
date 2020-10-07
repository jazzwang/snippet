[git] 學習 git-extras 使用
    
[TOC]

# [git] 學習 git-extras 使用

- [X] learn this project from [https://libraries.io/homebrew/gitextras](https://libraries.io/homebrew/gitextras)
- [X] homepage: [https://github.com/tj/git-extras](https://github.com/tj/git-extras)

# 2020-10-07

## Test on Windows 10

### installation

- ( 2020-10-07 15:08:54 ) test with `scoop`, `cmder` and `git` installed

```
C:\Users\yawang\git
λ where git.exe
E:\writable\scoop\apps\git\current\cmd\git.exe
E:\writable\scoop\shims\git.exe
E:\writable\scoop\apps\git\current\mingw64\bin\git.exe
```
```
C:\Users\yawang\git\git-extras (master -> origin)
λ which column.exe
/usr/bin/column.exe
```

- install `git-extras` with `install.cmd`

```
C:\Users\yawang\git
λ git clone https://github.com/tj/git-extras.git
Cloning into 'git-extras'...
remote: Enumerating objects: 6446, done.
Receiving objects: 100% (6446/ reused 0 (delta 0), pack-reused 6446
Receiving objects: 100% (6446/6446), 1.55 MiB | 10.77 MiB/s, done.
Resolving deltas: 100% (4198/4198), done.
Updating files: 100% (296/296), done.

C:\Users\yawang\git
λ cd git-extras\

C:\Users\yawang\git\git-extras (master -> origin)
λ .\install.cmd
Installing to E:\writable\scoop\apps\git\current\mingw64
Installing binaries...
Installing man pages...
done
```

- ( 2020-10-07 15:11:33 ) test with `git-extras` repo

```
C:\Users\yawang\git\git-extras (master -> origin)
λ git summary
 project  : git-extras
 repo age : 10 years
 active   : 675 days
 commits  : 1497
 files    : 296
 authors  :
   229  hemanth.hm                15.3%
   179  spacewander               12.0%
   133  TJ Holowaychuk            8.9%
   128  罗泽轩                    8.6%
   115  Tj Holowaychuk            7.7%
    57  Nicolai Skogheim          3.8%

    (... skipped ... )

```