# git filter-repo

## 2026-01-30

- 緣起：
  - 想把 A repo 的單一檔案 git histroy 複製到 B repo 的新路徑
- 參考：
  - https://www.reddit.com/r/git/comments/1bq5mv6/how_to_move_file_with_commit_history_to_another/
    
    Here's a one-liner to extract your file with history using `filter-repo` (assuming the file you want is src/README.md):
    
    ```
    git filter-repo --path src/README.md
    ```
    
  - https://stackoverflow.com/a/69643404

    There is a new command `git filter-repo` nowadays. It has more possibilities and better performance.

    See [man page](https://htmlpreview.github.io/?https://github.com/newren/git-filter-repo/blob/docs/html/git-filter-repo.html) for details and [project page](https://github.com/newren/git-filter-repo) for installation.

    Remove everything except src/README.md and move it to the root:

    ```bash
    git filter-repo --path src/README.md
    git filter-repo --subdirectory-filter src/
    ```

    `--path` selects the single file and `--subdirectory-filter` moves the contents of that directory to root.
- 實測：
  - 發現 git 並沒有這個指令
    ```bash
    $ git filter-repo
    git: 'filter-repo' is not a git command. See 'git --help'.
    $ git -v
    git version 2.47.1
    ```
  - 在 https://ithelp.ithome.com.tw/articles/10257482 看到實際示範，並且知道要透過 `pip install git-filter-repo` 進行安裝
- 心得：
  - 當要抽取出來的檔案是在某個 branch 時，會警告
    ```bash
    @jazzwang ➜ /tmp/snippet (win11-bin) $ git filter-repo --path meeting-summary
    Aborting: Refusing to destructively overwrite repo history since
    this does not look like a fresh clone.
    (expected at most one entry in the reflog for HEAD)
    Please operate on a fresh clone instead.  If you want to proceed
    anyway, use --force.
    ```
  - 原本想說不是乾淨的 clone，但測試兩次以後，發現只要是獨立的 branch （root 跟 main/master 不同）就不行，一定要指定 `--force`。
  - 其次，照 [reddit 討論的作法](https://www.reddit.com/r/git/comments/1bq5mv6/how_to_move_file_with_commit_history_to_another/)，用 merge 的話，git history 會比較醜（有分支）。所以我後來改用 `git cherry-pick` 把 commit history 拉進來（算是一點小潔癖：保留別人的 commit，又不至於把 history 弄得很難追）。