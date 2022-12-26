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