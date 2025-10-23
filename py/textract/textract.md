# textract

- Git Repo
  - https://github.com/deanmalmgren/textract
- Document
  - https://textract.readthedocs.io/en/stable/

## 2025-10-14

- 緣起：
  - 從 [markitdown](../markitdown/markitdown.md) 的 `README.md` 看到的專案

## 2025-10-23

- 測試用 `uv` 安裝
  ```
  ~$ uname -a
  MINGW64_NT-10.0-26200 JazzBook 3.6.4-b9f03e96.x86_64 2025-07-16 18:17 UTC x86_64 Msys
  ~$ uv tool install textract
  ~$ which textract
  /c/Users/jazzw/.local/bin/textract
  ```
- 需求：把很長的 mailthread 轉成純文字或 Markdown
- 實驗 CLI 界面：
  ```bash
  ~$ textract
  Traceback (most recent call last):
    File "C:\Users\jazzw\.local\bin\textract", line 33, in <module>
      main()
      ~~~~^^
    File "C:\Users\jazzw\.local\bin\textract", line 22, in main
      parser = get_parser()
    File "C:\Users\jazzw\AppData\Roaming\uv\tools\textract\Lib\site-packages\textract\cli.py", line 67, in get_parser
      choices=_get_available_extensions(),
              ~~~~~~~~~~~~~~~~~~~~~~~~~^^
    File "C:\Users\jazzw\AppData\Roaming\uv\tools\textract\Lib\site-packages\textract\parsers\__init__.py", line 93, in _get_available_extensions
      ext_re = re.compile(glob_filename.replace('*', r"(?P<ext>\w+)"))
    File "C:\Users\jazzw\AppData\Roaming\uv\python\cpython-3.13.2-windows-x86_64-none\Lib\re\__init__.py", line 289, in compile
      return _compile(pattern, flags)
    File "C:\Users\jazzw\AppData\Roaming\uv\python\cpython-3.13.2-windows-x86_64-none\Lib\re\__init__.py", line 350, in _compile
      p = _compiler.compile(pattern, flags)
    File "C:\Users\jazzw\AppData\Roaming\uv\python\cpython-3.13.2-windows-x86_64-none\Lib\re\_compiler.py", line 748, in compile
      p = _parser.parse(p, flags)
    File "C:\Users\jazzw\AppData\Roaming\uv\python\cpython-3.13.2-windows-x86_64-none\Lib\re\_parser.py", line 980, in parse
      p = _parse_sub(source, state, flags & SRE_FLAG_VERBOSE, 0)
    File "C:\Users\jazzw\AppData\Roaming\uv\python\cpython-3.13.2-windows-x86_64-none\Lib\re\_parser.py", line 459, in _parse_sub
      itemsappend(_parse(source, state, verbose, nested + 1,
                  ~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                        not nested and not items))
                        ^^^^^^^^^^^^^^^^^^^^^^^^^
    File "C:\Users\jazzw\AppData\Roaming\uv\python\cpython-3.13.2-windows-x86_64-none\Lib\re\_parser.py", line 543, in _parse
      code = _escape(source, this, state)
    File "C:\Users\jazzw\AppData\Roaming\uv\python\cpython-3.13.2-windows-x86_64-none\Lib\re\_parser.py", line 397, in _escape
      raise source.error("incomplete escape %s" % escape, len(escape))
  re.PatternError: incomplete escape \U at position 2
  ```
  - 想改用 pip 安裝，似乎也有版本相容問題。
  ```bash
  $ pip3 install textract
  Collecting textract
    Using cached textract-1.6.5-py3-none-any.whl.metadata (2.5 kB)
  WARNING: Ignoring version 1.6.5 of textract since it has invalid metadata:
  Requested textract from https://files.pythonhosted.org/packages/6b/3e/ac16b6bf28edf78296aea7d0cb416b49ed30282ac8c711662541015ee6f3/textract-1.6.5-py3-none-any.whl has invalid metadata: .* suffix can only be used with `==` or `!=` operators
      extract-msg (<=0.29.*)
                  ~~~~~~~^
  Please use pip<24.1 if you need to use this version.
    Using cached textract-1.6.4.tar.gz (17 kB)
    Installing build dependencies ... done
    Getting requirements to build wheel ... error
    error: subprocess-exited-with-error

    × Getting requirements to build wheel did not run successfully.
    │ exit code: 1
    ╰─> [3 lines of output]
        error in textract setup command: 'install_requires' must be a string or iterable of strings containing valid project/version requirement specifiers; .* suffix can only be used with `==` or `!=` operators
            extract-msg<=0.29.*
                      ~~~~~~~^
        [end of output]

    note: This error originates from a subprocess, and is likely not a problem with pip.
  error: subprocess-exited-with-error

  × Getting requirements to build wheel did not run successfully.
  │ exit code: 1
  ╰─> See above for output.

  note: This error originates from a subprocess, and is likely not a problem with pip.
  ```