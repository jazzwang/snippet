# autoresearch

- Git Repo
  - https://github.com/karpathy/autoresearch

## 2026-03-10

- From AlphaSignal 2026-03-10 Newsletter

> Andrej Karpathy publishes Autoresearch, an open-source agent that runs continuous ML training experiments on one GPU

- 同事也提到這個專案
- 不過看了一下 README 感覺比較偏重於進行 Machine Learning 的訓練實驗

## 2026-03-17

- 參考 README 與 https://x.com/hooeem/status/2030720614752039185
```bash
~$ cd git/
~/git$ git clone https://github.com/karpathy/autoresearch
Cloning into 'autoresearch'...
remote: Enumerating objects: 185, done.
remote: Total 185 (delta 0), reused 0 (delta 0), pack-reused 185 (from 1)
Receiving objects: 100% (185/185), 524.25 KiB | 1.40 MiB/s, done.
Resolving deltas: 100% (102/102), done.
~/git$ cd autoresearch/
~/git/autoresearch$ uv sync
Using CPython 3.10.16
Creating virtual environment at: .venv
Resolved 74 packages in 1ms
Prepared 52 packages in 28m 59s
Installed 52 packages in 4.98s
```
- 跑 `uv run prepare.py` 時，下載了很久，按 CTRL+C 也中斷不了。只好開另一個終端機把 uv process 用 kill 砍掉。結果才看到下載了某些 parquet 檔案
```bash
~$ cd git/autoresearch/
~/git/autoresearch$ uv run prepare.py
Cache directory: C:\Users\jazzw\.cache\autoresearch

Data: downloading 11 shards (0 already exist)...
KeyboardInterrupt
  File "<frozen importlib._bootstrap_external>", line 975, in get_code
    addpackage(sitedir, name, known_paths)
  File "C:\Users\jazzw\AppData\Roaming\uv\python\cpython-3.10.16-windows-x86_64-none\lib\site.py", line 195, in addpackage
  File "<frozen importlib._bootstrap_external>", line 1074, in get_data
    exec(line)
KeyboardInterrupt
  File "<string>", line 1, in <module>
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 879, in exec_module
  File "<frozen importlib._bootstrap_external>", line 975, in get_code
  File "<frozen importlib._bootstrap_external>", line 1073, in get_data
KeyboardInterrupt
  Downloaded shard_06542.parquet
Killed
~/git/autoresearch$   Downloaded shard_00009.parquet
  Downloaded shard_00008.parquet
```
```bash
~$ ls -al ~/.cache/autoresearch/data/
total 560332
drwxr-xr-x 1 jazzw 197609        0 Mar 18 23:28 .
drwxr-xr-x 1 jazzw 197609        0 Mar 18 23:22 ..
-rw-r--r-- 1 jazzw 197609 39845888 Mar 18 23:25 shard_00000.parquet.tmp
-rw-r--r-- 1 jazzw 197609 37748736 Mar 18 23:25 shard_00001.parquet.tmp
-rw-r--r-- 1 jazzw 197609 35651584 Mar 18 23:25 shard_00002.parquet.tmp
-rw-r--r-- 1 jazzw 197609 35651584 Mar 18 23:25 shard_00003.parquet.tmp
-rw-r--r-- 1 jazzw 197609 36700160 Mar 18 23:25 shard_00004.parquet.tmp
-rw-r--r-- 1 jazzw 197609 38797312 Mar 18 23:25 shard_00005.parquet.tmp
-rw-r--r-- 1 jazzw 197609 35651584 Mar 18 23:25 shard_00006.parquet.tmp
-rw-r--r-- 1 jazzw 197609 38797312 Mar 18 23:25 shard_00007.parquet.tmp
-rw-r--r-- 1 jazzw 197609 91155507 Mar 18 23:28 shard_00008.parquet
-rw-r--r-- 1 jazzw 197609 92072356 Mar 18 23:28 shard_00009.parquet
-rw-r--r-- 1 jazzw 197609 91699537 Mar 18 23:28 shard_06542.parquet
```
