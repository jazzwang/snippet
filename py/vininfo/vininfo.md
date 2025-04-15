# vininfo

- Git Repo
  - https://github.com/idlesign/vininfo
- PyPI
  - https://pypi.org/project/vininfo/1.8.0/
- SourceRank: 13
  - https://libraries.io/pypi/vininfo

## 其他相關套件

- https://pypi.org/project/vin/
  - https://libraries.io/pypi/vin
- https://pypi.org/project/pyvin
  - https://libraries.io/pypi/pyvin
- https://pypi.org/project/vinlib/
  - https://github.com/h3/python-libvin

## Install 安裝

- 因為 vininfo 有 CLI，所以用 `uv tool` 安裝
- ( 2025-04-15 19:16:39 )
```bash
~/git/snippet/py$ uv tool install vininfo
Resolved 1 package in 1.38s
Prepared 1 package in 402ms
Installed 1 package in 20ms
 + vininfo==1.8.0
Installed 1 executable: vininfo.exe
```
- ( 2025-04-15 19:22:47 )
```bash
jazzw@JazzBook:~$ vininfo show JN8BT3DDXPW300834
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\jazzw\.local\bin\vininfo.exe\__main__.py", line 4, in <module>
    from vininfo.cli import main
  File "C:\Users\jazzw\AppData\Roaming\uv\tools\vininfo\Lib\site-packages\vininfo\cli.py", line 4, in <module>
    import click
ModuleNotFoundError: No module named 'click'
```
- ( 2025-04-15 19:22:54 )
- 看起來缺少 `click` ，再仔細看一下 `uv tool --help` 補上 `--with` 試試看
```bash
jazzw@JazzBook:~/git/snippet$ uv tool install vininfo --with click
Resolved 3 packages in 675ms
Installed 3 packages in 35ms
 + click==8.1.8
 + colorama==0.4.6
 + vininfo==1.8.0
Installed 1 executable: vininfo.exe
```
- 再測試一次
```bash
jazzw@JazzBook:~/git/snippet$ vininfo show JN8BT3DDXPW300834
Basic:
Country: Japan
Manufacturer: Nissan
Region: Asia
Years: 2023, 1993

Details:
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\jazzw\.local\bin\vininfo.exe\__main__.py", line 10, in <module>
    sys.exit(main())
             ~~~~^^
  File "C:\Users\jazzw\AppData\Roaming\uv\tools\vininfo\Lib\site-packages\vininfo\cli.py", line 51, in main
    entry_point(obj={})
    ~~~~~~~~~~~^^^^^^^^
  File "C:\Users\jazzw\AppData\Roaming\uv\tools\vininfo\Lib\site-packages\click\core.py", line 1161, in __call__
    return self.main(*args, **kwargs)
           ~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "C:\Users\jazzw\AppData\Roaming\uv\tools\vininfo\Lib\site-packages\click\core.py", line 1082, in main
    rv = self.invoke(ctx)
  File "C:\Users\jazzw\AppData\Roaming\uv\tools\vininfo\Lib\site-packages\click\core.py", line 1697, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
                           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
  File "C:\Users\jazzw\AppData\Roaming\uv\tools\vininfo\Lib\site-packages\click\core.py", line 1443, in invoke
    return ctx.invoke(self.callback, **ctx.params)
           ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jazzw\AppData\Roaming\uv\tools\vininfo\Lib\site-packages\click\core.py", line 788, in invoke
    return __callback(*args, **kwargs)
  File "C:\Users\jazzw\AppData\Roaming\uv\tools\vininfo\Lib\site-packages\vininfo\cli.py", line 35, in show
    out(details)
    ~~~^^^^^^^^^
  File "C:\Users\jazzw\AppData\Roaming\uv\tools\vininfo\Lib\site-packages\vininfo\cli.py", line 24, in out
    for k, v in annotatable.annotate().items():
                ~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\jazzw\AppData\Roaming\uv\tools\vininfo\Lib\site-packages\vininfo\common.py", line 25, in annotate
    annotations[label] = f'{value}'
                           ^^^^^^^
TypeError: __str__ returned non-string (type list)
```
- 還是有一些錯誤訊息，改用 `pip` 安裝好了
```bash
jazzw@JazzBook:~/git/snippet$ uv tool uninstall vininfo
Uninstalled 1 executable: vininfo.exe
jazzw@JazzBook:~/git/snippet$ pip install vininfo
Collecting vininfo
  Downloading vininfo-1.8.0-py3-none-any.whl.metadata (3.5 kB)
Downloading vininfo-1.8.0-py3-none-any.whl (20 kB)
Installing collected packages: vininfo
Successfully installed vininfo-1.8.0
jazzw@JazzBook:~/git/snippet$ which vininfo
/c/Users/jazzw/scoop/apps/python/current/Scripts/vininfo
```
- 
```bash
jazzw@JazzBook:~$ vininfo
Usage: vininfo [OPTIONS] COMMAND [ARGS]...

  vininfo command line utilities.

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  check  Perform VIN checksum validation
  show   Show information for VIN
jazzw@JazzBook:~$ vininfo show JN8BT3DDXPW300834
Basic:
Country: Japan
Manufacturer: Nissan
Region: Asia
Years: 2023, 1993

Details:
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\jazzw\scoop\apps\python\current\Scripts\vininfo.exe\__main__.py", line 7, in <module>
  File "C:\Users\jazzw\scoop\apps\python\current\Lib\site-packages\vininfo\cli.py", line 51, in main
    entry_point(obj={})
  File "C:\Users\jazzw\scoop\apps\python\current\Lib\site-packages\click\core.py", line 1161, in __call__
    return self.main(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jazzw\scoop\apps\python\current\Lib\site-packages\click\core.py", line 1082, in main
    rv = self.invoke(ctx)
         ^^^^^^^^^^^^^^^^
  File "C:\Users\jazzw\scoop\apps\python\current\Lib\site-packages\click\core.py", line 1697, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jazzw\scoop\apps\python\current\Lib\site-packages\click\core.py", line 1443, in invoke
    return ctx.invoke(self.callback, **ctx.params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jazzw\scoop\apps\python\current\Lib\site-packages\click\core.py", line 788, in invoke
    return __callback(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jazzw\scoop\apps\python\current\Lib\site-packages\vininfo\cli.py", line 35, in show
    out(details)
  File "C:\Users\jazzw\scoop\apps\python\current\Lib\site-packages\vininfo\cli.py", line 24, in out
    for k, v in annotatable.annotate().items():
                ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jazzw\scoop\apps\python\current\Lib\site-packages\vininfo\common.py", line 25, in annotate
    annotations[label] = f'{value}'
                           ^^^^^^^
TypeError: __str__ returned non-string (type list)
jazzw@JazzBook:~$ vininfo check JN8BT3DDXPW300834
Checksum is valid
```
- 看起來可能是原生套件的問題了～
