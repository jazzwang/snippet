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

### more about `Development Containers`

- https://containers.dev/overview - 簡介
- https://containers.dev/supporting - 支援平台
- https://github.com/devcontainers/cli - CLI 工具

- 問題：能否在本地端模擬 `Development Containers` ？
- 看起來是可行的
  - [Reproducible Local Development with Dev Containers](https://medium.com/cwan-engineering/reproducible-local-development-with-dev-containers-0ed5fa850b36)
  - ![](https://miro.medium.com/v2/resize:fit:828/format:webp/1*p7fItlFwMp1VbKN2KgiVAw.png)
- 從文章中學到可以有多個不同「環境」的設定方法：
  - 參考：https://github.com/clearwater-analytics/devcontainer-java-example/tree/main/.devcontainer
  - 每個設定檔都是參考 https://github.com/devcontainers/templates/blob/main/src/java/.devcontainer/devcontainer.json
    ```json
    // For format details, see https://aka.ms/devcontainer.json. For config options, see the
    // README at: https://github.com/devcontainers/templates/tree/main/src/java
    {
        "name": "Java",
        // Or use a Dockerfile or Docker Compose file. More info: https://containers.dev/guide/dockerfile
        "image": "mcr.microsoft.com/devcontainers/java:1-${templateOption:imageVariant}",
        //... 以下省略 ..
    }
    ```
- [文章] [DevContainer and Makefile: A Duo for Simplified GCP Workflows](https://dev.to/tanvirrahman/devcontainer-and-makefile-a-duo-for-simplified-gcp-workflows-ii9)
  - 講述善用 DevContainer 跟 Makefile 來管理 GCP 的工作流程 (e.g. 產生 GCE VM)