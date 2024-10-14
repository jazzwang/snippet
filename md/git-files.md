# Common Files in Git Repository

| Name | Type | Usage |
|------|------|-------|
| CITATION.cff | file | plain text files with human- and machine-readable citation information for software (and datasets). |
| `.devcontainer/devcontainer.json` | file | 

## 2024-10-07

- Learned from https://github.com/gabrielchua/RAGxplorer
- https://citation-file-format.github.io/#/create-a-citationcff-file-now
- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files

## 2024-10-14

- ( 2024-10-14 08:33:30 )
- 需求：因為有習慣性在 Markdown 文件中加入 Timestamp，在使用 Github CodeSpace 時，預設時區 Time Zone 是 UTC。所以想要改成 `Asia/Taipei`
- 限制：Github CodeSpace 預設身份是 `codespace` 而不是 Github 帳號，因此也沒辦法在 `.bashrc` 加入想要的環境變數。
- 參考：https://www.eliostruyf.com/set-timezone-github-codespaces/
    - 這裡提到四種作法 (A) 加 `.devcontainer/devcontainer.json` (B) 直接改 Github CodeSpace 設定 (C) 使用客製化 Dockerfile (D) 使用  [dotfiles repository](https://docs.github.com/en/codespaces/setting-your-user-preferences/personalizing-github-codespaces-for-your-account#dotfiles)。當然第一種作法可以通用其他像是 [gitpod](https://gitpod.io/) （很可能 Gitlab 也可以)，所以優先使用這種方式。
- 操作：若使用 `gh cs code` 開啟 Github CodeSpace 的話，可以按 `Ctrl-Shift-P` 選 `Codespaces: Add Dev Container Configuration Files...` ，然後選 `Create a new configuration ...` ，就能在目前的 Git Repo 產生一個預設的 `.devcontainer/devcontainer.json` (當然是針對 Github CodeSpace)。修改 JSON 內容，就可以加入 `TZ` 環境變數：
```json
{
    "image":"mcr.microsoft.com/devcontainers/universal:2",     ### 這個是預設的 CodeSpace Container Image
    "remoteEnv": {                                             ### 要求遠端環境應該要加入以下環境變數 Env
        "TZ": "Asia/Taipei"                                    ### 自訂 TZ 環境變數
    }
}
```