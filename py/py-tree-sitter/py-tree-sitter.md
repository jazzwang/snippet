# py-tree-sitter

> Python bindings to the Tree-sitter parsing library

- PyPI
  - https://pypi.org/project/tree-sitter/
- Git Repo
  - https://github.com/tree-sitter/py-tree-sitter
- Document
  - https://tree-sitter.github.io/py-tree-sitter/

## 2025-04-24

- 緣起：
  - 在思考用 LLM 幫忙理解 Legacy Perl/Bash Git Repository ，並且萃取出必要的 Business Rules，想起 Aider 用到 tree-sitter 來分析 git repo
- 已完成：
  - 可以用 LLM 產生 high-level overview 甚至生成 sequence diagram 跟 package diagram。也可以把 long array definition 轉成 Markdown Table。
- 目的：
  - 有什麼工具可以方便抽取特定片段的 function definition 或 long array definition
  - 想要把這些資訊轉成 pandas DataFrame 以方便做 join 運作。
- 參考：
  - 2023-10-22: [Building a better repository map with tree sitter](https://aider.chat/2023/10/22/repomap.html)
  - Aider 作者介紹怎麼用 tree-sitter-language-pack 來增加不同程式語言的支援 - [Add language support via tree-sitter-language-pack](https://aider.chat/docs/recordings/tree-sitter-language-pack.html)

## 2025-07-06

- https://pypi.org/project/tree-sitter-languages/
- https://github.com/grantjenks/py-tree-sitter-languages