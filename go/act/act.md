# Github Local Runner

> Run your GitHub Actions locally 🚀

- Git Repo
  - https://github.com/nektos/act
- Website
  - https://nektosact.com/

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

以下針對 `act` 進行測試。

## 2025-07-28

