# Kaggle

- https://github.com/Kaggle/kaggle-api

> Official Kaggle API

```
pip install kaggle
```

## 2024-12-28

- 在 https://www.kaggle.com/competitions/wsdm-cup-multilingual-chatbot-arena/data 看到這一行

```
kaggle competitions download -c wsdm-cup-multilingual-chatbot-arena
```

- 猜想應該是有 CLI 指令，所以查了一下。有兩個實作：
  - https://github.com/Kaggle/kaggle-api (Kaggle 官方的)
  - https://github.com/floydwch/kaggle-cli (An unofficial Kaggle command line tool - 已於 2024-01-28 設為 `Archived`)

### 安裝

```bash
@jazzwang ➜ /workspaces/snippet (master) $ pip install kaggle
@jazzwang ➜ /workspaces/snippet (master) $ which kaggle
/home/codespace/.python/current/bin/kaggle
```

### 下載資料集

```bash
@jazzwang ➜ /workspaces/snippet (master) $ kaggle competitions download -c wsdm-cup-multilingual-chatbot-arena
Traceback (most recent call last):
  File "/home/codespace/.python/current/bin/kaggle", line 5, in <module>
    from kaggle.cli import main
  File "/home/codespace/.python/current/lib/python3.10/site-packages/kaggle/__init__.py", line 7, in <module>
    api.authenticate()
  File "/home/codespace/.python/current/lib/python3.10/site-packages/kaggle/api/kaggle_api_extended.py", line 407, in authenticate
    raise IOError('Could not find {}. Make sure it\'s located in'
OSError: Could not find kaggle.json. Make sure it's located in /home/codespace/.config/kaggle. Or use the environment method. See setup instructions at https://github.com/Kaggle/kaggle-api/
```
- ( 2024-12-28 12:01:34 )
- 看樣子需要設定 `~/.config/kaggle/kaggle.json`