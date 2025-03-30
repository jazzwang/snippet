# pyinstaller

* 先前會用 py2exe 把 python 程式變成 Windows 執行檔，可以把一些不想揭露原始碼的小工具變成方便散播的格式。
* 查了一下在 macOS 或 Linux 上可以改用 pyinstaller
    * 參考 https://stackoverflow.com/a/9035527
* 官網：https://pyinstaller.org/en/stable/
* Github: https://github.com/pyinstaller/pyinstaller

## 2024-05-31

( 2024-05-31 16:39:52 )
* 安裝：`pip3 install pyinstaller`
* 以 hcml 新竹市圖書館的 requests 為例：
```
jazzwang:~/git/snippet/python/requests/hcml$ pyinstaller check-books.py
3293 INFO: PyInstaller: 6.7.0, contrib hooks: 2024.6
3293 INFO: Python: 3.9.6
3439 INFO: Platform: macOS-12.7.5-x86_64-i386-64bit
3442 INFO: wrote /Users/jazzwang/git/snippet/python/requests/hcml/check-books.spec
3487 INFO: Extending PYTHONPATH with paths
['/Users/jazzwang/git/snippet/python/requests/hcml']
7145 INFO: checking Analysis
7146 INFO: Building Analysis because Analysis-00.toc is non existent
7146 INFO: Running Analysis Analysis-00.toc
7147 INFO: Target bytecode optimization level: 0
7147 INFO: Initializing module dependency graph...
7158 INFO: Caching module graph hooks...
7249 INFO: Analyzing base_library.zip ...
8886 INFO: Loading module hook 'hook-encodings.py' from '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/PyInstaller/hooks'...
10890 INFO: Loading module hook 'hook-pickle.py' from '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/PyInstaller/hooks'...
12196 INFO: Loading module hook 'hook-heapq.py' from '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/PyInstaller/hooks'...
13728 INFO: Caching module dependency graph...
13861 INFO: Looking for Python shared library...
13936 INFO: Using Python shared library: /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Python3
13937 INFO: Analyzing /Users/jazzwang/git/snippet/python/requests/hcml/check-books.py
16115 INFO: Loading module hook 'hook-charset_normalizer.py' from '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/_pyinstaller_hooks_contrib/hooks/stdhooks'...
16428 INFO: Loading module hook 'hook-certifi.py' from '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/_pyinstaller_hooks_contrib/hooks/stdhooks'...
16681 INFO: Loading module hook 'hook-pandas.py' from '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/PyInstaller/hooks'...
25697 INFO: Loading module hook 'hook-platform.py' from '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/PyInstaller/hooks'...
25770 INFO: Loading module hook 'hook-xml.py' from '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/PyInstaller/hooks'...
25818 INFO: Loading module hook 'hook-sysconfig.py' from '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/PyInstaller/hooks'...
25851 INFO: Processing pre-safe import module hook distutils from '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/PyInstaller/hooks/pre_safe_import_module/hook-distutils.py'.
25856 INFO: Processing pre-find module path hook distutils from '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/PyInstaller/hooks/pre_find_module_path/hook-distutils.py'.
25869 INFO: Loading module hook 'hook-distutils.py' from '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/PyInstaller/hooks'...
25997 INFO: Loading module hook 'hook-numpy.py' from '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/numpy/_pyinstaller'...
27485 INFO: Loading module hook 'hook-difflib.py' from '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/PyInstaller/hooks'...
27863 INFO: Loading module hook 'hook-multiprocessing.util.py' from '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/PyInstaller/hooks'...
32003 INFO: Loading module hook 'hook-pytz.py' from '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/PyInstaller/hooks'...
32341 INFO: Loading module hook 'hook-pkg_resources.py' from '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/PyInstaller/hooks'...
37073 INFO: Loading module hook 'hook-pandas.io.formats.style.py' from '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/PyInstaller/hooks'...
40718 INFO: Loading module hook 'hook-pandas.plotting.py' from '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/PyInstaller/hooks'...
42948 INFO: Loading module hook 'hook-sqlite3.py' from '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/PyInstaller/hooks'...
43555 INFO: Loading module hook 'hook-pandas.io.clipboard.py' from '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/PyInstaller/hooks'...
44672 INFO: Processing pre-safe import module hook six.moves from '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/PyInstaller/hooks/pre_safe_import_module/hook-six.moves.py'.
45314 INFO: Loading module hook 'hook-xml.etree.cElementTree.py' from '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/PyInstaller/hooks'...
45327 INFO: Loading module hook 'hook-lxml.py' from '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/_pyinstaller_hooks_contrib/hooks/stdhooks'...
46269 INFO: Loading module hook 'hook-lxml.etree.py' from '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/_pyinstaller_hooks_contrib/hooks/stdhooks'...
46302 INFO: Loading module hook 'hook-xml.dom.domreg.py' from '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/PyInstaller/hooks'...
48310 INFO: Processing module hooks...
48568 INFO: Loading module hook 'hook-lxml.isoschematron.py' from '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/_pyinstaller_hooks_contrib/hooks/stdhooks'...
48643 INFO: Processing pre-safe import module hook win32com from '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/_pyinstaller_hooks_contrib/hooks/pre_safe_import_module/hook-win32com.py'.
48847 INFO: Loading module hook 'hook-distutils.util.py' from '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/PyInstaller/hooks'...
49187 INFO: Loading module hook 'hook-packaging.py' from '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/PyInstaller/hooks'...
49438 WARNING: Hidden import "jinja2" not found!
49459 INFO: Loading module hook 'hook-lxml.objectify.py' from '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/_pyinstaller_hooks_contrib/hooks/stdhooks'...
49487 INFO: Performing binary vs. data reclassification (628 entries)
52541 INFO: Looking for ctypes DLLs
52554 WARNING: Library msvcrt required via ctypes not found
52557 WARNING: Library user32 required via ctypes not found
52568 INFO: Analyzing run-time hooks ...
52576 INFO: Including run-time hook '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/PyInstaller/hooks/rthooks/pyi_rth_inspect.py'
52586 INFO: Including run-time hook '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/PyInstaller/hooks/rthooks/pyi_rth_pkgutil.py'
52601 INFO: Processing pre-find module path hook _pyi_rth_utils from '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/PyInstaller/hooks/pre_find_module_path/hook-_pyi_rth_utils.py'.
52615 INFO: Loading module hook 'hook-_pyi_rth_utils.py' from '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/PyInstaller/hooks'...
52621 INFO: Including run-time hook '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/PyInstaller/hooks/rthooks/pyi_rth_multiprocessing.py'
52632 INFO: Including run-time hook '/Users/jazzwang/Library/Python/3.9/lib/python/site-packages/PyInstaller/hooks/rthooks/pyi_rth_pkgres.py'
52701 INFO: Looking for dynamic libraries
54442 INFO: Warnings written to /Users/jazzwang/git/snippet/python/requests/hcml/build/check-books/warn-check-books.txt
54557 INFO: Graph cross-reference written to /Users/jazzwang/git/snippet/python/requests/hcml/build/check-books/xref-check-books.html
55143 INFO: checking PYZ
55143 INFO: Building PYZ because PYZ-00.toc is non existent
55143 INFO: Building PYZ (ZlibArchive) /Users/jazzwang/git/snippet/python/requests/hcml/build/check-books/PYZ-00.pyz
56487 INFO: Building PYZ (ZlibArchive) /Users/jazzwang/git/snippet/python/requests/hcml/build/check-books/PYZ-00.pyz completed successfully.
56514 INFO: EXE target arch: x86_64
56514 INFO: Code signing identity: None
56518 INFO: checking PKG
56519 INFO: Building PKG because PKG-00.toc is non existent
56519 INFO: Building PKG (CArchive) check-books.pkg
56558 INFO: Building PKG (CArchive) check-books.pkg completed successfully.
56559 INFO: Bootloader /Users/jazzwang/Library/Python/3.9/lib/python/site-packages/PyInstaller/bootloader/Darwin-64bit/run
56559 INFO: checking EXE
56560 INFO: Building EXE because EXE-00.toc is non existent
56560 INFO: Building EXE from EXE-00.toc
56560 INFO: Copying bootloader EXE to /Users/jazzwang/git/snippet/python/requests/hcml/build/check-books/check-books
56635 INFO: Converting EXE to target arch (x86_64)
56746 INFO: Removing signature(s) from EXE
56848 INFO: Appending PKG archive to EXE
56860 INFO: Fixing EXE headers for code signing
56879 INFO: Re-signing the EXE
56958 INFO: Building EXE from EXE-00.toc completed successfully.
56977 INFO: checking COLLECT
56977 INFO: Building COLLECT because COLLECT-00.toc is non existent
56978 INFO: Building COLLECT COLLECT-00.toc
66987 INFO: Building COLLECT COLLECT-00.toc completed successfully.
```
* 產生的執行檔會在 `dist` 目錄底下
```
jazzwang:~/git/snippet/python/requests/hcml$ ls dist/check-books/
_internal	check-books
jazzwang:~/git/snippet/python/requests/hcml$ file dist/check-books/check-books
dist/check-books/check-books: Mach-O 64-bit executable x86_64
```
( 2024-05-31 17:01:51 )
* 在 Github CodeSpace 上測試。
* Linux 環境遇到一些錯誤訊息：
```
@jazzwang ➜ .../snippet/python/requests/hcml (master) $ pyinstaller check-books.py
147 INFO: PyInstaller: 6.7.0, contrib hooks: 2024.6
147 INFO: Python: 3.10.13
149 INFO: Platform: Linux-6.5.0-1021-azure-x86_64-with-glibc2.31
150 INFO: wrote /workspaces/snippet/python/requests/hcml/check-books.spec
152 INFO: Extending PYTHONPATH with paths
['/workspaces/snippet/python/requests/hcml']
328 INFO: checking Analysis
328 INFO: Building Analysis because Analysis-00.toc is non existent
328 INFO: Running Analysis Analysis-00.toc
328 INFO: Target bytecode optimization level: 0
329 INFO: Initializing module dependency graph...
329 INFO: Caching module graph hooks...
337 INFO: Analyzing base_library.zip ...
793 INFO: Loading module hook 'hook-heapq.py' from '/usr/local/python/3.10.13/lib/python3.10/site-packages/PyInstaller/hooks'...
854 INFO: Loading module hook 'hook-encodings.py' from '/usr/local/python/3.10.13/lib/python3.10/site-packages/PyInstaller/hooks'...
2134 INFO: Loading module hook 'hook-pickle.py' from '/usr/local/python/3.10.13/lib/python3.10/site-packages/PyInstaller/hooks'...
3029 INFO: Caching module dependency graph...
3104 INFO: Looking for Python shared library...
Traceback (most recent call last):
  File "/home/codespace/.python/current/bin/pyinstaller", line 8, in <module>
    sys.exit(_console_script_run())
  File "/usr/local/python/3.10.13/lib/python3.10/site-packages/PyInstaller/__main__.py", line 228, in _console_script_run
    run()
  File "/usr/local/python/3.10.13/lib/python3.10/site-packages/PyInstaller/__main__.py", line 212, in run
    run_build(pyi_config, spec_file, **vars(args))
  File "/usr/local/python/3.10.13/lib/python3.10/site-packages/PyInstaller/__main__.py", line 69, in run_build
    PyInstaller.building.build_main.main(pyi_config, spec_file, **kwargs)
  File "/usr/local/python/3.10.13/lib/python3.10/site-packages/PyInstaller/building/build_main.py", line 1189, in main
    build(specfile, distpath, workpath, clean_build)
  File "/usr/local/python/3.10.13/lib/python3.10/site-packages/PyInstaller/building/build_main.py", line 1129, in build
    exec(code, spec_namespace)
  File "/workspaces/snippet/python/requests/hcml/check-books.spec", line 4, in <module>
    a = Analysis(
  File "/usr/local/python/3.10.13/lib/python3.10/site-packages/PyInstaller/building/build_main.py", line 529, in __init__
    self.__postinit__()
  File "/usr/local/python/3.10.13/lib/python3.10/site-packages/PyInstaller/building/datastruct.py", line 184, in __postinit__
    self.assemble()
  File "/usr/local/python/3.10.13/lib/python3.10/site-packages/PyInstaller/building/build_main.py", line 642, in assemble
    raise PythonLibraryNotFoundError()
PyInstaller.exceptions.PythonLibraryNotFoundError: Python library not found: libpython3.10.so, libpython3.10.so.1.0
    This means your Python installation does not come with proper shared library files.
    This usually happens due to missing development package, or unsuitable build parameters of the Python installation.

    * On Debian/Ubuntu, you need to install Python development packages:
      * apt-get install python3-dev
      * apt-get install python-dev
    * If you are building Python by yourself, rebuild with `--enable-shared` (or, `--enable-framework` on macOS).
```
* 試過 `apt-get install python3-dev` 跟 `apt-get install python-dev` 還是沒效。
* 根據錯誤訊息
```
PyInstaller.exceptions.PythonLibraryNotFoundError: Python library not found: libpython3.10.so, libpython3.10.so.1.0
```
* 應該是找不到 share library `libpython3.10.so` 跟 `libpython3.10.so.1.0`
* 用 `apt-file` 找找看
```
@jazzwang ➜ .../snippet/python/requests/hcml (master) $ apt-file search libpython3.10.so
conda: /opt/conda/lib/libpython3.10.so
conda: /opt/conda/lib/libpython3.10.so.1.0
```
* 安裝 `conda` 套件，重裝一次 pyinstaller，再跑一次。Yeah!! 成功！！
```
@jazzwang ➜ .../snippet/python/requests/hcml (master) $ sudo apt-get -y install conda
@jazzwang ➜ .../snippet/python/requests/hcml (master) $ source /opt/conda/bin/activate
(base) @jazzwang ➜ .../snippet/python/requests/hcml (master) $ pip3 install pyinstaller
(base) @jazzwang ➜ .../snippet/python/requests/hcml (master) $ pyinstaller check-books.py
217 INFO: PyInstaller: 6.7.0, contrib hooks: 2024.6
217 INFO: Python: 3.12.3 (conda)
219 INFO: Platform: Linux-6.5.0-1021-azure-x86_64-with-glibc2.31
219 INFO: wrote /workspaces/snippet/python/requests/hcml/check-books.spec
221 INFO: Extending PYTHONPATH with paths
['/workspaces/snippet/python/requests/hcml']
305 INFO: checking Analysis
305 INFO: Building Analysis because Analysis-00.toc is non existent
305 INFO: Running Analysis Analysis-00.toc
305 INFO: Target bytecode optimization level: 0
305 INFO: Initializing module dependency graph...
306 INFO: Caching module graph hooks...
311 INFO: Analyzing base_library.zip ...
1286 INFO: Loading module hook 'hook-encodings.py' from '/opt/conda/lib/python3.12/site-packages/PyInstaller/hooks'...
1881 INFO: Loading module hook 'hook-heapq.py' from '/opt/conda/lib/python3.12/site-packages/PyInstaller/hooks'...
2567 INFO: Loading module hook 'hook-pickle.py' from '/opt/conda/lib/python3.12/site-packages/PyInstaller/hooks'...
3459 INFO: Caching module dependency graph...
3527 INFO: Looking for Python shared library...
3535 INFO: Using Python shared library: /opt/conda/lib/libpython3.12.so.1.0
3535 INFO: Analyzing /workspaces/snippet/python/requests/hcml/check-books.py
3704 INFO: Loading module hook 'hook-platform.py' from '/opt/conda/lib/python3.12/site-packages/PyInstaller/hooks'...
4095 INFO: Loading module hook 'hook-charset_normalizer.py' from '/opt/conda/lib/python3.12/site-packages/_pyinstaller_hooks_contrib/hooks/stdhooks'...
4350 INFO: Loading module hook 'hook-cryptography.py' from '/opt/conda/lib/python3.12/site-packages/_pyinstaller_hooks_contrib/hooks/stdhooks'...
5512 INFO: Loading module hook 'hook-certifi.py' from '/opt/conda/lib/python3.12/site-packages/_pyinstaller_hooks_contrib/hooks/stdhooks'...
5626 INFO: Processing module hooks...
5657 INFO: Performing binary vs. data reclassification (13 entries)
5755 INFO: Looking for ctypes DLLs
5760 INFO: Analyzing run-time hooks ...
5763 INFO: Including run-time hook '/opt/conda/lib/python3.12/site-packages/PyInstaller/hooks/rthooks/pyi_rth_inspect.py'
5765 INFO: Including run-time hook '/opt/conda/lib/python3.12/site-packages/_pyinstaller_hooks_contrib/hooks/rthooks/pyi_rth_cryptography_openssl.py'
5771 INFO: Looking for dynamic libraries
6148 INFO: Warnings written to /workspaces/snippet/python/requests/hcml/build/check-books/warn-check-books.txt
6162 INFO: Graph cross-reference written to /workspaces/snippet/python/requests/hcml/build/check-books/xref-check-books.html
6171 INFO: checking PYZ
6171 INFO: Building PYZ because PYZ-00.toc is non existent
6171 INFO: Building PYZ (ZlibArchive) /workspaces/snippet/python/requests/hcml/build/check-books/PYZ-00.pyz
6457 INFO: Building PYZ (ZlibArchive) /workspaces/snippet/python/requests/hcml/build/check-books/PYZ-00.pyz completed successfully.
6467 INFO: checking PKG
6467 INFO: Building PKG because PKG-00.toc is non existent
6467 INFO: Building PKG (CArchive) check-books.pkg
6475 INFO: Building PKG (CArchive) check-books.pkg completed successfully.
6475 INFO: Bootloader /opt/conda/lib/python3.12/site-packages/PyInstaller/bootloader/Linux-64bit-intel/run
6475 INFO: checking EXE
6475 INFO: Building EXE because EXE-00.toc is non existent
6475 INFO: Building EXE from EXE-00.toc
6476 INFO: Copying bootloader EXE to /workspaces/snippet/python/requests/hcml/build/check-books/check-books
6476 INFO: Appending PKG archive to custom ELF section in EXE
6497 INFO: Building EXE from EXE-00.toc completed successfully.
6499 INFO: checking COLLECT
6499 INFO: Building COLLECT because COLLECT-00.toc is non existent
6499 INFO: Building COLLECT COLLECT-00.toc
6599 INFO: Building COLLECT COLLECT-00.toc completed successfully.
```
( 2024-05-31 17:11:10 )
* 看起來在 Linux 上就會是 ELF 64-bit LSB executable
```
(base) @jazzwang ➜ .../snippet/python/requests/hcml (master) $ file dist/check-books/check-books
dist/check-books/check-books: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=979c889cc9ca56a33ed67aeb4d2d05cb8db2df1b, for GNU/Linux 2.6.32, stripped
```
* 看起來還是有相依動態連結擋。
```
(base) @jazzwang ➜ .../snippet/python/requests/hcml (master) $ ldd dist/check-books/check-books
        linux-vdso.so.1 (0x00007ffe643d8000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x0000795bffcb1000)
        libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x0000795bffc95000)
        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x0000795bffc72000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x0000795bffa80000)
        /lib64/ld-linux-x86-64.so.2 (0x0000795bffcc3000)
```
( 2024-05-31 17:13:48 )
* 不錯～這樣以後可以靠 Github Action 來把編好的 Linux Binary 變成 DEB 或 RPM 檔。

## 2024-06-26

* 2024-06-26 21:47:29
- 後來經過一些實驗，發現產生出來的 macOS executable 會相依 `_internal` 目錄底下的內容。
```bash
jazzwang:/tmp$ ./export_fieldglass
[16974] Error loading Python lib '/private/tmp/_internal/Python3': dlopen: dlopen(/private/tmp/_internal/Python3, 0x000A): tried: '/private/tmp/_internal/Python3' (no such file)
```
- 2024-06-26 21:56:50
- 看了一下[官方文件 Using PyInstaller](https://pyinstaller.org/en/stable/usage.html)，有幾個參數可以試試看：
```
--clean

    Clean PyInstaller cache and remove temporary files before building.

-F, --onefile

    Create a one-file bundled executable.
```
- 2024-06-26 22:01:36
- 加上 `--onefile` 這樣跑的話，會產生單一個檔案比較大，但不相依其他目錄的執行檔。
```bash
jazzwang:/tmp$ pyinstaller --clean --onefile ~/git/snippet/python/requests/hcml/check-books.py
jazzwang:/tmp$ tree dist/
dist/
└── check-books

1 directory, 1 file

jazzwang:/tmp$ file dist/check-books
dist/check-books: Mach-O 64-bit executable x86_64

jazzwang:/tmp$ du -sh dist/check-books
 42M	dist/check-books
```
- 2024-06-26 22:06:01
- 遇到奇怪的錯誤
```bash
jazzwang:/tmp$ ./check-books
urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
ID: **********
Password:
Traceback (most recent call last):
  File "pandas/compat/_optional.py", line 135, in import_optional_dependency
  File "importlib/__init__.py", line 127, in import_module
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 984, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'html5lib'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "check-books.py", line 35, in <module>
  File "pandas/io/html.py", line 1240, in read_html
  File "pandas/io/html.py", line 971, in _parse
  File "pandas/io/html.py", line 915, in _parser_dispatch
  File "pandas/compat/_optional.py", line 138, in import_optional_dependency
ImportError: Missing optional dependency 'html5lib'.  Use pip or conda to install html5lib.
[17842] Failed to execute script 'check-books' due to unhandled exception!
```
- 2024-06-26 22:35:01
- 安裝 html5lib 套件，再重跑一次。
```bash
jazzwang:/tmp$ pip install html5lib
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: html5lib in /Users/jazzwang/Library/Python/3.9/lib/python/site-packages (1.1)
Requirement already satisfied: six>=1.9 in /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/site-packages (from html5lib) (1.15.0)
Requirement already satisfied: webencodings in /Users/jazzwang/Library/Python/3.9/lib/python/site-packages (from html5lib) (0.5.1)
jazzwang:/tmp$ pyinstaller -F ~/git/snippet/python/requests/hcml/check-books.py
jazzwang:/tmp$ cd dist/
jazzwang:/tmp/dist$ ./check-books
urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
ID: **********
Password:
-----------  待還書 -----------------
    到期日      題名                                            索書號               借書日期
 0  2024-07-14  簡單老師和想飛的企鵝                            C 861.59 8444 (4)    2024-06-16
 1  2024-07-14  管家貓                                          C 861 8736 (7)       2024-06-16
 6  2024-07-14  這是(便所專用)的腦筋急轉彎                      book 997 8564        2024-06-16
 9  2024-07-14  孩子精 媽媽驚 : 運動員兒子給校長媽媽的震撼教育  book 528.2 8457 (4)  2024-06-16
10  2024-07-14  戒掉孩子的拖延症                                book 528.2 8426 (4)  2024-06-16
 2  2024-07-20  跳箱要午休                                      C 861.596 8352 (3)   2024-06-22
 3  2024-07-20  腳踏車扛神轎                                    C 861.59 8352 (3)    2024-06-22
 4  2024-07-20  超白目爆笑腦筋急轉彎                            book 997 8564 (5)    2024-06-22
 5  2024-07-20  野兔甜點師傅的祕密                              C 861.59 8473 (4)    2024-06-22
 7  2024-07-20  深夜的放屁大賽                                  C 861.59 8633 (6)    2024-06-22
 8  2024-07-20  深夜的打呼大賽                                  C 861.596 8633 (6)   2024-06-22
11  nan         nan                                             nan                  nan
-----------  預約書 -----------------
      保留日期  題名
 0         nan  就是要爆笑啊!不然要幹嘛? : 最經典的腦筋急轉彎
 1         nan  全民大笑話 : 笑到凍未條!
 2         nan  我可以不去上學嗎?
 3         nan  Llama drama : it's showtime!
 4         nan  Llama llama sand & sun
 5         nan  暖爐放寒假
 6         nan  最棒的調味料
 7         nan  小獅子向前走!
 8         nan  nan
```