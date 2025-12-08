# Git Clone

- https://git-scm.com/docs/git-clone

## 2025-12-08

- 情境：
  - 只複製遠端的特定 remote tag 或 remote branch
- 緣起：
  - 在處理 WSL2 編譯 HFS+ 客製化核心時，看到 `git clone -b <branch_name> -depth 1` 的寫法
  - 看起來指定 `-b` 應該也可以用在 remote `tag` 或 `branch`
  - 至於 `-depth 1` 是指定只下載一筆 commit history
- 參考：
  - https://graphite.com/guides/git-clone-specific-tag
  - https://medium.com/@thriving_chiffon_gnu_714/exploring-git-clone-depth-828eb4bac6c4
