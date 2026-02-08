# OpenCode Labs - Day 1

## 2026-02-08

- 測試環境  #1：Github Codespace (隨時可以清掉的環境)
``
@jazzwang ➜ /workspaces/snippet (master) $ curl -fsSL https://opencode.ai/install | bash

Installing opencode version: 1.1.53
■■■■･･････････････････････････････････････････････   8%
■■■■■･････････････････････････････････････････････  10%
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 100%
Successfully added opencode to $PATH in /home/codespace/.bashrc

                                 ▄     
█▀▀█ █▀▀█ █▀▀█ █▀▀▄ █▀▀▀ █▀▀█ █▀▀█ █▀▀█
█░░█ █░░█ █▀▀▀ █░░█ █░░░ █░░█ █░░█ █▀▀▀
▀▀▀▀ █▀▀▀ ▀▀▀▀ ▀  ▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀▀


OpenCode includes free models, to start:

cd <project>  # Open directory
opencode      # Run command

For more information visit https://opencode.ai/docs
```
- 驗證：
```bash
@jazzwang ➜ /workspaces/snippet (master) $ source ~/.bashrc
@jazzwang ➜ /workspaces/snippet (master) $ opencode --version
1.1.53
```