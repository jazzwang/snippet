# MEMO

## 2022-12-26

### 緣起

- ( 2022-12-26 21:53:36 )
- 原本在找怎麼整合 Python, Jira 跟 [mermaid.js](https://github.com/mermaid-js/mermaid) 的繪圖來畫 in-sprint dependency
- 看到 https://github.com/coddingtonbear/jirafs 的 demo 覺得蠻有趣的。用 Apache Software Foundation 的 Jira 來測試一下。

### 安裝

- ( 2022-12-26 21:56:34 )
```bash
jazzwang:~$ source ~/venv/bin/activate
(venv) jazzwang:~$ pip install jirafs
(venv) jazzwang:~$ which jirafs
/Users/jazzwang/venv/bin/jirafs
```
- ( 2022-12-26 21:57:51 )
```bash
(venv) jazzwang:~$ jirafs clone https://issues.apache.org/jira/browse/BIGTOP-1889
Attempted to load entrypoint preview = jirafs.commands.preview:Command, but an ImportError occurred.
[INFO] {BIGTOP-1889} Ticket folder for issue BIGTOP-1889 created at /Users/jazzwang/BIGTOP-1889
Jira Username (https://issues.apache.org/jira): jazzwang
Jira Password (https://issues.apache.org/jira):
Save Jira Password (Y/N)? y
[WARNING] Attempted to load entrypoint preview = jirafs.commands.preview:Command, but an ImportError occurred.
[WARNING] Attempted to load entrypoint preview = jirafs.commands.preview:Command, but an ImportError occurred.
[INFO] {BIGTOP-1889} Updated 'jira' to 3828ab1920061685919b01ab1e9fd5eef84d4e38
[WARNING] Attempted to load entrypoint preview = jirafs.commands.preview:Command, but an ImportError occurred.
[INFO] {BIGTOP-1889} New comment(s) have been posted.
[INFO] {BIGTOP-1889} Field description changed: "" -> "Hi BigTop Team,…"
[INFO] {BIGTOP-1889} Merged 'jira' into 'master'; merge-base is now 3828ab1920061685919b01ab1e9fd5eef84d4e38
[INFO] {BIGTOP-1889} Issue https://issues.apache.org/jira/browse/BIGTOP-1889 cloned successfully to /Users/jazzwang/BIGTOP-1889
(venv) jazzwang:~$ cd BIGTOP-1889/
(venv) jazzwang:~/BIGTOP-1889$ ls -al
total 48
drwxr-xr-x    8 jazzwang  staff    256 Dec 26 22:01 .
drwxr-xr-x  269 jazzwang  staff   8608 Dec 26 22:01 ..
drwxr-xr-x   13 jazzwang  staff    416 Dec 26 22:01 .jirafs
-rw-r--r--    1 jazzwang  staff    672 Dec 26 22:01 comments.read_only.jira
-rw-r--r--    1 jazzwang  staff    439 Dec 26 22:01 description.jira
-rw-r--r--    1 jazzwang  staff  12977 Dec 26 22:01 fields.jira
-rw-r--r--    1 jazzwang  staff      0 Dec 26 22:01 links.jira
-rw-r--r--    1 jazzwang  staff      0 Dec 26 22:01 new_comment.jira
```

## 2025-03-27

### 改用 `uv tool` 安裝

```
jazzw@JazzBook:~/git/snippet/py/jira$ uv tool install jirafs
  × Failed to build `pathtools==0.1.2`
  ├─▶ The build backend returned an error
  ╰─▶ Call to `setuptools.build_meta:__legacy__.build_wheel` failed (exit code: 1)

      [stderr]
      Traceback (most recent call last):
        File "<string>", line 14, in <module>
        File "C:\Users\jazzw\AppData\Local\uv\cache\builds-v0\.tmpXTDwFI\Lib\site-packages\setuptools\build_meta.py", line 334, in get_requires_for_build_wheel
          return self._get_build_requires(config_settings, requirements=[])
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "C:\Users\jazzw\AppData\Local\uv\cache\builds-v0\.tmpXTDwFI\Lib\site-packages\setuptools\build_meta.py", line 304, in _get_build_requires
          self.run_setup()
        File "C:\Users\jazzw\AppData\Local\uv\cache\builds-v0\.tmpXTDwFI\Lib\site-packages\setuptools\build_meta.py", line 522, in run_setup
          super().run_setup(setup_script=setup_script)
        File "C:\Users\jazzw\AppData\Local\uv\cache\builds-v0\.tmpXTDwFI\Lib\site-packages\setuptools\build_meta.py", line 320, in run_setup
          exec(code, locals())
        File "<string>", line 25, in <module>
      ModuleNotFoundError: No module named 'imp'

      hint: This usually indicates a problem with the package or the build environment.
  help: `pathtools` (v0.1.2) was included because `jirafs` (v2.3.1) depends on `watchdog>=0.9.0, <1.0.0` (v0.10.7) which depends on `pathtools>=0.1.1`
jazzw@JazzBook:~/git/snippet/py/jira$
```
- 既然 PyPI 套件庫因為太久沒更新，所以遇到相容性問題，那直接改 checkout 原始碼，微調一下吧～
```
jazzw@JazzBook:~/git$ git clone https://github.com/coddingtonbear/jirafs.git
jazzw@JazzBook:~/git$ cd jirafs/
jazzw@JazzBook:~/git/jirafs$ code requirements.txt
jazzw@JazzBook:~/git/jirafs$ git diff
diff --git a/requirements.txt b/requirements.txt
index 6287525..b254d2d 100644
--- a/requirements.txt
+++ b/requirements.txt
@@ -4,4 +4,5 @@ blessings>=1.5.1,<2.0
 prettytable>=0.7.2,<1.0
 environmental-override>=0.1.2,<1.0.0
 jinja2>=2.10.3,<3.0
-watchdog>=0.9.0,<1.0.0
+watchdog>=0.9.0
```
- 因為問題出在 `watchdog` 那把條件放寬一點。然後用 `uv tool` 進行 local package 安裝
```bash
jazzw@JazzBook:~/git/jirafs$ cd ..
jazzw@JazzBook:~/git$ uv tool install ./jirafs
Resolved 22 packages in 30ms
Installed 22 packages in 114ms
 + blessings==1.7
 + certifi==2025.1.31
 + charset-normalizer==3.4.1
 + defusedxml==0.7.1
 + environmental-override==0.1.2
 + idna==3.10
 + jinja2==2.11.3
 + jira==3.8.0
 + jirafs==2.3.0 (from file:///C:/Users/jazzw/git/jirafs)
 + markupsafe==3.0.2
 + oauthlib==3.2.2
 + packaging==24.2
 + pillow==11.1.0
 + prettytable==0.7.2
 + python-dateutil==2.9.0.post0
 + requests==2.32.3
 + requests-oauthlib==2.0.0
 + requests-toolbelt==1.0.0
 + six==1.17.0
 + typing-extensions==4.13.0
 + urllib3==2.3.0
 + watchdog==6.0.0
Installed 1 executable: jirafs.exe
```
- ( 2025-03-27 21:05:49 )
- 裝好了，可是執行下去卻有 Python 原生 `curses` 函式庫相容性的問題。看樣子要改好，一時半刻有其困難度。
```bash
jazzw@JazzBook:~$ jirafs -h
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\jazzw\.local\bin\jirafs.exe\__main__.py", line 4, in <module>
  File "C:\Users\jazzw\AppData\Roaming\uv\tools\jirafs\Lib\site-packages\jirafs\cmdline.py", line 13, in <module>
    from blessings import Terminal
  File "C:\Users\jazzw\AppData\Roaming\uv\tools\jirafs\Lib\site-packages\blessings\__init__.py", line 5, in <module>
    import curses
  File "C:\Users\jazzw\scoop\apps\python\current\Lib\curses\__init__.py", line 13, in <module>
    from _curses import *
ModuleNotFoundError: No module named '_curses'
```
- 先刪除再說
```bash
jazzw@JazzBook:~/git$ uv tool uninstall jirafs
Uninstalled 1 executable: jirafs.exe
```

## 2025-03-30

- 看起來主要牽涉到 `blessings` 這個年代久遠的套件
  - https://pypi.org/project/blessings/
- https://github.com/erikrose/blessings/issues/166 提到 `blessings` 不支援 Windows (確實只看到支援 POSIX 系統)
  > jquast - on Dec 17, 2023
  > blessings doesn't work on windows.
  > The fork, https://github.com/jquast/blessed does.
- 備註：作者有寫了新的 https://github.com/coddingtonbear/jira-select 來跟 Jira 互動。