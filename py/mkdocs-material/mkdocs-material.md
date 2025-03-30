# README

- 原始碼： https://github.com/squidfunk/mkdocs-material 
- 官方文件： https://squidfunk.github.io/mkdocs-material/getting-started/ 

## 2024-08-30

- 在 MLOps Community 看到一門課 [MLOps Coding Course](https://mlops-coding-course.fmind.dev/index.html)
    - 課程會用到的原始碼 https://github.com/MLOps-Courses/mlops-coding-course
- 從網站最下方看到 Made with [Material for MkDocs]()
- ( 2024-08-30 16:51:10 )
- 先從安裝開始
    - 測試環境：Github Codespace
```bash
@jazzwang ➜ /workspaces/snippet (master) $ pip install mkdocs-material
```
- 根據文件 https://squidfunk.github.io/mkdocs-material/creating-your-site/
- 要用指令產生範本 `mkdocs new .`
```bash
@jazzwang ➜ /workspaces/snippet/python/mkdocs-material (master) $ mkdocs new .

INFO    -  Writing config file: ./mkdocs.yml
INFO    -  Writing initial docs: ./docs/index.md

@jazzwang ➜ /workspaces/snippet/python/mkdocs-material (master) $ ls
README.md docs  mkdocs.yml
```
- 我沒做什麼修改，就執行 `mkdocs serve`
- 確實可以 Preview 結果
![Screen Shot 2024-08-30 at 5.33.54 PM](https://i.imgur.com/k19Huu8.png)