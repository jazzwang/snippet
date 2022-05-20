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