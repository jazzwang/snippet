# deptree

> Display installed Python distributions as a tree of dependencies

- PyPI
  - https://pypi.org/project/deptree/
- Git Repo
  - https://github.com/sinoroc/deptree
  - https://gitlab.com/sinoroc/deptree

## 2025-04-17

- 緣起：
  - 想了解一下 LlamaIndex 跟 ChromaDB 的套件相依狀況
- 安裝：
  - 因為有 CLI 界面，所以用 `uv tool` 安裝
```bash
jazzw@JazzBook:~/git/snippet/py$ cd deptree/
jazzw@JazzBook:~/git/snippet/py/deptree$ uv tool install deptree
Resolved 4 packages in 1.87s
Prepared 3 packages in 430ms
Installed 4 packages in 374ms
 + deptree==0.0.12
 + importlib-metadata==8.6.1
 + setuptools==78.1.0
 + zipp==3.21.0
Installed 1 executable: deptree.exe
```
- 先前應該是用 `pipdeptree` 來產生 `graphviz` 的圖
  - https://github.com/tox-dev/pipdeptree?tab=readme-ov-file#visualizing-the-dependency-graph