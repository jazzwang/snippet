# commitlint | commitizen

> commitlint is a tool designed to lint your commit messages according to the Conventional Commits standard for your pre-commit hook and GitHub Actions.

- Git Repo: https://github.com/opensource-nepal/commitlint
- PyPi: https://pypi.org/project/commitlint/

## 2024-11-08 commitlint

- 緣起：
  - 先前美國團隊那邊是靠 pre-commit 來觸發 [golint](https://pkg.go.dev/golang.org/x/lint/golint) 讓 local commit 發生前，確保一些軟體開發的團隊規則。
  - 今天想要幫自己的 snippet repo 加上 [Conventional Commits](https://www.conventionalcommits.org/) 想說靠 [commitlint](https://github.com/opensource-nepal/commitlint) 來讓自己的 commit message 照一些規範（還在學習理解 conventional commit 的建議）
  - 因為習慣上本機比較沒有裝 node.js (npm/npx) 但會裝 Python ，所以會想靠 python 的 `pre-commit` + `commitlint` 來完成這個目標。

## 2024-11-09 - commitizen

| Language | Python | JavaScript |
|----------|--------|------------|
| git hooks manager | [pre-commit](https://github.com/pre-commit/pre-commit) | [husky](https://typicode.github.io/husky/) |
| commit linter | [commitlint](https://github.com/opensource-nepal/commitlint) | [commitlint.js](https://commitlint.js.org/) <br/> [cz-commitlint](https://www.npmjs.com/package/@commitlint/cz-commitlint) <br/> [commitizen](https://github.com/commitizen/cz-cli) |

- 對照 [commitlint.js](../../js/commitlint/MEMO.md) 的相關介紹文章，少了一段 commitizen 互動式檢查的部份

- https://pypi.org/project/commitizen/
- https://github.com/commitizen-tools/commitizen

- 從 README 看起來，應該會產生一個命令列工具 `cz` (跟 javascript 版本會變成 `git cz` 指令類似)