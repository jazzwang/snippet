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
pip install marimo
```