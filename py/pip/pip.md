# pip

- https://pip.pypa.io/en/stable/installation/

## 2025-04-08

- 緣起：
  - 自從改用 `uv` 管理套件以後，因為會有多個不同版本的 Python 環境，所以很容易錯亂到底某個指令是放在 venv 裡？還是 `uv tool` 對應的路徑？還是系統 (scoop) 安裝路徑。
  - 當然，一直有點困擾的是 `uv` 建立的系統 (`scoop`) 環境會沒有 pip 指令，只能靠 `uv pip` 或者 `python -m pip` 方式執行，很不習慣。
- 解法：
  - 最後測試成功的解法是下載 `get-pip.py`，然後用系統  python 執行 `python get-pip.py`。這樣就會有 `pip` 指令可以直接管理系統的 PIP 套件。
```bash
jazzw@JazzBook:~$ wget https://bootstrap.pypa.io/get-pip.py
jazzw@JazzBook:~$ python get-pip.py
jazzw@JazzBook:~$ which pip
/c/Users/jazzw/scoop/apps/python/current/Scripts/pip
```
- 注意：
  - `uv tool install pip` 雖然會產生 `pip` 執行檔，但 runtime 會是 `uv tool` 指定的共用函式庫存放路徑。可能會跟 system default python library 路徑不同。
  - `uv pip install pip` 會在指定的 python 版本環境(預設是 system)安裝 `pip` 套件。但有點古怪的是沒有產生 `pip` 執行擋在 PATH 裡。
  - `python -m ensurepip --upgrade` 會在系統 python 版本環境中升級 `pip` 套件，但不會產生 `pip` 執行檔在 PATH 路徑中。