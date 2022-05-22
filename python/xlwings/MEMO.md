# MEMO

## 緣起

- 工作上有需求讀 Excel XLSX 檔案，做一些比對。想說拿這個來練練手，維持寫程式的手感。
- 查了 [Libraries.io 的 SourceRank](https://libraries.io/search?languages=python&q=excel&sort=rank) 第二筆是 [xlwings](https://libraries.io/pypi/xlwings)

  | | |
  |---|---|
  | SourceRank | 21 |
  | Total releases | 124 |
  | Stars | 2.3K |
  | Forks | 418 |
  | Watchers | 120 |
  | Contributors | 46 |

## 定位

- 照官方網站 https://www.xlwings.org/ 的說明：

  <div style="background-color: lightyellow;padding:5px;">
  xlwings is open source and free, comes preinstalled with Anaconda and WinPython, and works on Windows and macOS.

  <mark>Automate Excel via Python scripts or Jupyter notebooks, call Python from Excel via macros</mark>, and write user-defined functions (UDFs are Windows-only).
  </div>

- 定位：https://docs.xlwings.org/en/stable/
  - **Scripting**: Automate/interact with Excel from Python using a syntax close to VBA.
  - **Macros**: Replace VBA macros with clean and powerful Python code.
  - **UDFs**: Write User Defined Functions (UDFs) in Python (<mark>Windows only</mark>).

## 練習實作

- ( 2022-05-20 15:24:18 )
- https://docs.xlwings.org/en/stable/quickstart.html
- ( 2022-05-21 00:56:45 )
- 安裝 `xlwings` 跟 `matplotlib`
```bash
jazzwang:~/git/snippet/python/xlwings$ source ~/venv/bin/activate
(venv) jazzwang:~/git/snippet/python/xlwings$ pip3 install xlwings matplotlib
(venv) jazzwang:~/git/snippet/python/xlwings$ xlwings addin install

xlwings version: 0.27.7
Successfully installed the xlwings add-in! Please restart Excel.
Successfully enabled RunPython!
```
- 使用 ipython 來做互動式操作
```
(venv) jazzwang:~/git/snippet/python/xlwings$ ipython3
Python 3.8.9 (default, Oct 26 2021, 07:25:54)
Type 'copyright', 'credits' or 'license' for more information
IPython 8.3.0 -- An enhanced Interactive Python. Type '?' for help.
```
```python
import xlwings as xw
app = xw.App()
wb = app.books.add()
sheet = wb.sheets['Sheet1']
sheet.range('A1').value = [['Foo 1', 'Foo 2', 'Foo 3'], [10.0, 20.0, 30.0]]
import matplotlib.pyplot as plt
fig = plt.figure()
plt.plot([1, 2, 3, 4, 5])
sheet.pictures.add(fig, name='MyPlot', top=100, left=100, update=True)
wb.save("sample.xlsx")
```