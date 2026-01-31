# git filter-branch

- 緣起：
  - 有時後會忘記改工作 Git Repo 裡的 `user.email`，因為 global 設定成個人的 Gmail。所以需要大量修改已經 push 出去的 commit
- 解法：
  - 一次性用 `git commit -amend`
  - 少量用 `git rebase`
  - 大量用 `git filter-branch`
- 參考：https://www.git-tower.com/learn/git/faq/change-author-name-email/
```bash
git filter-branch --env-filter '
WRONG_EMAIL="wrong@example.com"
NEW_NAME="New Name Value"
NEW_EMAIL="correct@example.com"

if [ "$GIT_COMMITTER_EMAIL" = "$WRONG_EMAIL" ]
then
    export GIT_COMMITTER_NAME="$NEW_NAME"
    export GIT_COMMITTER_EMAIL="$NEW_EMAIL"
fi
if [ "$GIT_AUTHOR_EMAIL" = "$WRONG_EMAIL" ]
then
    export GIT_AUTHOR_NAME="$NEW_NAME"
    export GIT_AUTHOR_EMAIL="$NEW_EMAIL"
fi
' --tag-name-filter cat -- --branches --tags
```
- 執行時，會出現這個 WARNING
```bash
WARNING: git-filter-branch has a glut of gotchas generating mangled history
         rewrites.  Hit Ctrl-C before proceeding to abort, then use an
         alternative filtering tool such as 'git filter-repo'
         (https://github.com/newren/git-filter-repo/) instead.  See the
         filter-branch manual page for more details; to squelch this warning,
         set FILTER_BRANCH_SQUELCH_WARNING=1.
```
- 2026-01-31 備註：
  - 後來為了合併別人 repo 某個檔案時，確實用到 `git filter-repo` 這個指令
  - 詳見 [git-filter-repo.md](git-filter-repo.md)
