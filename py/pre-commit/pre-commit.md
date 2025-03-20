# pre-commit

> A framework for managing and maintaining multi-language pre-commit hooks.

- https://pre-commit.com/
- Git Repo: https://github.com/pre-commit/pre-commit

## 2024-11-08

- 緣起：
  - 先前美國團隊那邊是靠 pre-commit 來觸發 [golint](https://pkg.go.dev/golang.org/x/lint/golint) 讓 local commit 發生前，確保一些軟體開發的團隊規則。
  - 今天想要幫自己的 snippet repo 加上 [Conventional Commits](https://www.conventionalcommits.org/) 想說靠 [commitlint](https://github.com/opensource-nepal/commitlint) 來讓自己的 commit message 照一些規範（還在學習理解 conventional commit 的建議）
  - 因為習慣上本機比較沒有裝 node.js (npm/npx) 但會裝 Python ，所以會想靠 python 的 `pre-commit` + `commitlint` 來完成這個目標。
