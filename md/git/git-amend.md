# git commit --amend

## 2025-11-10

- How can I change the commit author for a single commit?
- https://stackoverflow.com/questions/3042437/how-can-i-change-the-commit-author-for-a-single-commit
```bash
git commit --amend --reset-author
```
- Reference:
  - https://stackoverflow.com/a/3042512
  - can also use `git rebase -i <commit>`
