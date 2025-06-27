# Github Local Runner

## 2025-06-05

- 緣起：
  - 先前用 Gitlab 可以自己註冊 Gitlab CI 的 runner，不管是 Windows 或 Linux 都可以。
    那 Github Actions 呢？可以註冊有內網連線權限的 Runner 嗎？
  - 其次，有辦法在 Local 先測試 Github Actions 嗎？
- 搜尋結果：
  - Github Enterprise 要靠 `Self-Hosted Runner` 來解決
    - 官方文件：
      - About self-hosted runners
        https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners
      - Limiting the use of self-hosted runners
        https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#limiting-the-use-of-self-hosted-runners
    - 其他參考：
      - 2024-08-28: [Step-by-Step Guide to Configuring a Self-Hosted Runner in GitHub Actions [2024]](https://dev.to/s3cloudhub/step-by-step-guide-to-configuring-a-self-hosted-runner-in-github-actions-2024-2b7j)
      - 2024-10-21: [Github Self-Hosted Runners: How to Setup & Use a Self-Hosted Github Runner for Your Actions & Workflows](https://gist.github.com/devinschumacher/c503cead206d4992d1a3cbb03c95e4c9)
      - 2025-05-24: [Github Self-Hosted Runners: How to Setup & Use a Self-Hosted Github Runner for Your Actions & Workflows](https://gist.github.com/devinschumacher/c503cead206d4992d1a3cbb03c95e4c9)
  - 要在 Local 測試 Github Actions，目前查到兩個解法：
    - nektos 的 `act`
      - https://github.com/nektos/act
      - 官方文件：https://nektosact.com/
      - 其他參考：
        - 2023-04-06: [Running GitHub Actions Locally: A Complete Guide for Windows, Mac, and Linux Users](https://medium.com/@debasishkumardas5/running-github-actions-locally-a-complete-guide-for-windows-mac-and-linux-users-34c45999c7cd)
    - Github 的 `local-action`
      - https://github.com/github/local-action

以下針對 `Local Runner` 進行測試。

## 2025-06-26

### Github Local Action

- 今天先測試 Github 的 `local-action`
  - https://github.com/github/local-action
- 安裝：
```bash
~$ npm i -g @github/local-action
added 230 packages in 37s
```
- 檢查：
```bash
~$ which local-action
/c/Users/jazzw/scoop/apps/nvm/current/nodejs/nodejs/local-action
~$ local-action -h
'tsx' is not recognized as an internal or external command,
operable program or batch file.
~$ local-action -v
~$
```
- 怪怪的，有無法識別 `tsx` 的錯誤訊息。
- 反安裝：
```bash
~$ npm uninstall -g @github/local-action

removed 230 packages in 1s
```

## 2025-06-27

- 測試一下 Github Codespace 上能不能用
```bash
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 6.8.0-1027-azure x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro
Last login: Wed Jun 25 16:33:23 2025 from ::1
@jazzwang ➜ /workspaces/codespaces-blank (main) $ npm i -g @github/local-action

added 230 packages in 29s

30 packages are looking for funding
  run `npm fund` for details
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.4.2
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.4.2
npm notice To update run: npm install -g npm@11.4.2
npm notice
@jazzwang ➜ /workspaces/codespaces-blank (main) $ which local-action
/home/codespace/nvm/current/bin/local-action
@jazzwang ➜ /workspaces/codespaces-blank (main) $ local-action -v
@jazzwang ➜ /workspaces/codespaces-blank (main) $ local-action -h
/bin/sh: 1: tsx: not found
```
- 一樣的錯誤，應該就是要找 TypeScript 的 `tsx` 該怎麼安裝。
  - https://www.npmjs.com/package/tsx
  - https://github.com/privatenumber/tsx
  - https://tsx.is/getting-started#global-installation
```bash
@jazzwang ➜ /workspaces/codespaces-blank (main) $ npm install -g tsx

added 5 packages in 2s

2 packages are looking for funding
  run `npm fund` for details
@jazzwang ➜ /workspaces/codespaces-blank (main) $ local-action
     _        _   _               ____       _
    / \   ___| |_(_) ___  _ __   |  _ \  ___| |__  _   _  __ _  __ _  ___ _ __
   / _ \ / __| __| |/ _ \| '_ \  | | | |/ _ \ '_ \| | | |/ _` |/ _` |/ _ \ '__|
  / ___ \ (__| |_| | (_) | | | | | |_| |  __/ |_) | |_| | (_| | (_| |  __/ |
 /_/   \_\___|\__|_|\___/|_| |_| |____/ \___|_.__/ \__,_|\__, |\__, |\___|_|
                                                         |___/ |___/
Usage: local-action [options] [command]

Test a GitHub Action locally

Options:
  -V, --version                          output the version number
  -h, --help                             display help for command

Commands:
  run <path> <entrypoint> <dotenv file>  Run a local action
  help [command]                         display help for command
@jazzwang ➜ /workspaces/codespaces-blank (main) $ local-action -v
@jazzwang ➜ /workspaces/codespaces-blank (main) $ local-action -V
@jazzwang ➜ /workspaces/codespaces-blank (main) $ local-action --version
@jazzwang ➜ /workspaces/codespaces-blank (main) $ 
```