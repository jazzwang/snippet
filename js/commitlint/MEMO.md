# commitlint.js | cz-commitlint | commitizen

> Lint commit messages

- https://commitlint.js.org/
- Git Repo: https://github.com/conventional-changelog/commitlint

## 2024-11-08

- 緣起：
  - 先前美國團隊那邊是靠 pre-commit 來觸發 [golint](https://pkg.go.dev/golang.org/x/lint/golint) 讓 local commit 發生前，確保一些軟體開發的團隊規則。
  - 今天想要幫自己的 snippet repo 加上 [Conventional Commits](https://www.conventionalcommits.org/) 想說靠 [commitlint](https://github.com/opensource-nepal/commitlint) 來讓自己的 commit message 照一些規範（還在學習理解 conventional commit 的建議）
  - 因為習慣上本機比較沒有裝 node.js (npm/npx) 但會裝 Python ，所以會想靠 python 的 `pre-commit` + `commitlint` 來完成這個目標。
  - 這裡只是紀錄一下 javascript 生態圈會怎麼處理 commitlint。簡單的結論如下對照表：

| Language | Python | JavaScript |
|----------|--------|------------|
| git hooks manager | [pre-commit]() | husky |
| commit linter | [commitlint](https://github.com/opensource-nepal/commitlint) | [commitlint.js](https://commitlint.js.org/) <br/> [cz-commitlint](https://www.npmjs.com/package/@commitlint/cz-commitlint) <br/> [commitizen](https://github.com/commitizen/cz-cli) |

- 參考：
  - https://www.freecodecamp.org/news/how-to-use-commitlint-to-write-good-commit-messages/
  - https://dev.to/thecharacterv/git-better-with-commitlint-and-conventional-commits-21pp (這篇文章有提到下方的 "Additional Links" 可以參考)
  - https://ithelp.ithome.com.tw/articles/10278664
    - 主要講到 commitlint 跟 husky
    - 提到另一個好處：可以搭配 [conventional-changelog](https://github.com/conventional-changelog/conventional-changelog) 來產生 Changelog
  - https://rexhung0302.github.io/2022/03/30/20220330/ 講到
    - Commitizen (互動式提交 interactive commit `git cz`) 
    - Commitlint-cli (工具 linter tool) 
    - config-conventional (規則 rule)
    - conventional-changelog (產生 changelog): 紀錄所有 commit 的詳細記錄
    - [standard-version](https://www.npmjs.com/package/standard-version): 產生版號紀錄，這些紀錄皆會記錄在 `CHANGELOG.md`。
    - lint-staged (ESlint 整合 husky)

- vscode-commitlint: 當然 javascript 實作的優點是可以整合進 VS Code
  - https://marketplace.visualstudio.com/items?itemName=joshbolduc.commitlint

### Additional Links

[Commitlint Local Setup Documentation](https://commitlint.js.org/#/guides-local-setup)
[Commitlint Rules Documentation](https://commitlint.js.org/#/reference-rules)
[Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
[Commitizen Repositories](https://github.com/orgs/commitizen/repositories)
[Commitlint Respositories](https://github.com/conventional-changelog/commitlint)