# marimo

- Git Repo:
  - https://github.com/marimo-team/marimo
- Website:
  - https://marimo.io/

> A reactive notebook for Python — run reproducible experiments, execute as a script, deploy as an app, and version with git.

## 2024-12-27

- 在 Calmcode 的訂閱信看到的專案，他們甚至幫 Marimo 製作了系列課程。
  - https://calmcode.io/course/marimo/introduction
- 與 Jupyter 筆記本不同，Marimo 比較特別的地方：
  - <span class="green">互動性</span>：**UI 元素** - https://docs.marimo.io/guides/interactivity/
  - <span class="green">可維護性</span>：marimo 筆記本儲存為<mark>純 Python 程式（ `*.py` 檔）</mark>，並可以使用 Git 輕鬆進行<mark>版本控制</mark>。
  - <span class="green">可重複使用性</span>：marimo 筆記本可以從命令列作為 Python 腳本執行（因為 它們儲存為.py檔案）
  - <span class="green">可共享性</span>：可部署為互動式 Web 應用程序 deployed as interactive web apps - 您可以使用 `marimo run` 指令提供這些元素。

### 安裝

- https://docs.marimo.io/getting_started/installation/

```bash
@jazzwang ➜ /workspaces/snippet/py/marimo (master) $ pip install marimo
```

### Quick Start 快速入門

- https://docs.marimo.io/getting_started/quickstart/

```bash
@jazzwang ➜ /workspaces/snippet/py/marimo (master) $ marimo tutorial --help
Usage: marimo tutorial [OPTIONS] {intro|dataflow|ui|markdown|plots|sql|layout|
                       fileformat|markdown-format|for-jupyter-users}

  Open a tutorial.

  marimo is a powerful library for making reactive notebooks and apps. To get
  the most out of marimo, get started with a few tutorials, starting with the
  intro:

          marimo tutorial intro

  Recommended sequence:

          - intro
          - dataflow
          - ui
          - markdown
          - plots
          - sql
          - layout
          - fileformat
          - markdown-format
          - for-jupyter-users

Options:
  -p, --port INTEGER     Port to attach to.
  --host TEXT            Host to attach to.  [default: 127.0.0.1]
  --proxy TEXT           Address of reverse proxy.
  --headless             Don't launch a browser.
  --token / --no-token   Use a token for authentication. This enables session-
                         based authentication. A random token will be
                         generated if --token-password is not set. If --no-
                         token is set, session-based authentication will not
                         be used.   [default: token]
  --token-password TEXT  Use a specific token for authentication. This enables
                         session-based authentication. A random token will be
                         generated if not set.
  --help                 Show this message and exit.
  ```
  ```bash
  @jazzwang ➜ /workspaces/snippet/py/marimo (master) $ marimo tutorial intro

        Edit intro.py in your browser 📝

        ➜  URL: http://localhost:2718?access_token=cEE5gbyaXl_YLNbFIYhDuA
  ```
  - 測試使用 `marimo` 來編輯 `lab1.py`
  ```bash
  @jazzwang ➜ /workspaces/snippet/py/marimo (master) $ marimo edit lab1.py
  
        Edit lab1.py in your browser 📝

        ➜  URL: http://localhost:2718?access_token=ZPrgDpzatUh7lj_zmY-UNg


        Thanks for using marimo! 🌊🍃
  ```
  - 實驗了 (A) `mo.mermaid()` (B) 儲存檔案 (Ctrl+S) (C) App View - Grid
  - 來觀察一下生成的 `lab1.py`
  ```python
  import marimo

__generated_with = "0.10.7"
app = marimo.App(width="medium", layout_file="layouts/lab1.grid.json")


@app.cell
def _():
    import marimo as mo

    diagram = '''
    graph LR
        A[Square Rect] -- Link text --> B((Circle))
        A --> C(Round Rect)
        B --> D{Rhombus}
        C --> D
    '''
    mo.mermaid(diagram)
    return diagram, mo


if __name__ == "__main__":
    app.run()
```
- 所以 App View 的 Layout 會以 JSON 檔案方式儲存。
```bash
@jazzwang ➜ /workspaces/snippet/py/marimo (master) $ tree
.
├── MEMO.md
├── lab1.py
└── layouts
    └── lab1.grid.json

1 directory, 3 files
```
- 如果用 `marimo run` 的話，就只會用 read-only 方式執行。回到 marimo 一開始想作為可重複執行 command line 程式，目標很吻合。
```bash
@jazzwang ➜ /workspaces/snippet/py/marimo (master) $ marimo run lab1.py 

        Running lab1.py ⚡

        ➜  URL: http://localhost:2718

        Are you sure you want to quit? (y/n): y

        Thanks for using marimo! 🌊🍃
```
- 匯出功能：
```bash
@jazzwang ➜ /workspaces/snippet/py/marimo (master) $ marimo export --help
Usage: marimo export [OPTIONS] COMMAND [ARGS]...

  Export a notebook to various formats.

Options:
  --help  Show this message and exit.

Commands:
  html       Run a notebook and export it as an HTML file.
  html-wasm  Export a notebook as a WASM-powered standalone HTML file.
  ipynb      Export a marimo notebook as a Jupyter notebook in...
  md         Export a marimo notebook as a code fenced Markdown file.
  script     Export a marimo notebook as a flat script, in topological...
```
- 感覺蠻合適 Data Scientist 拿來放在 static website 當作品集使用，特別因為 WASM 的發展，提供了更多互動性 Dashboard 的可能。
```bash
@jazzwang ➜ /workspaces/snippet/py/marimo (master) $ marimo shell-completion
Run this command to enable completions:

    echo 'eval "$(_MARIMO_COMPLETE=bash_source marimo)"' >> ~/.bashrc


Then restart your shell or run 'source ~/.bashrc' to enable completions
@jazzwang ➜ /workspaces/snippet/py/marimo (master) $ eval "$(_MARIMO_COMPLETE=bash_source marimo)"
```
- 方便 Shell 自動補完指令，可以照 `marimo shell-completion` 的指引，修改 `~/.bashrc` (也許在 zsh 環境會產生不同結果)