# DevContainer

## 2025-01-08

- Q: 如何讓 Github Codespace 的 devcontainer.json 讀取 Github Secret 當環境變數（例如：各種 API KEY 總不好寫在 Git Repo 裡吧？）
- A:
  - https://stackoverflow.com/a/73248022

The GitHub Codespaces secrets are available via `localEnv` which is a special variable used by `devcontainer.json` which provides access to environment variables on the host machine.

> [!TIP]
> GitHub Codespaces 機密可透過 `localEnv` 取得，這是 `devcontainer.json` 使用的特殊變數，提供對主機上環境變數的存取。

Furthermore, if you want to set an environment variable pointing to a path inside your repo you can use ${containerWorkspaceFolder}/path/inside/your/repo.

> [!TIP]
> 此外，如果您想要設定指向儲存庫內路徑的環境變量，您可以使用 ${containerWorkspaceFolder}/path/inside/your/repo 。

```json
"remoteEnv": {
    // Use a GitHub Codespaces secret:
    "QXToken": "${localEnv:QXTOKEN}",
    // Point to a path inside your repo:
    "QISKIT_SETTINGS": "${containerWorkspaceFolder}/.qiskit/settings.conf"
}
```

- 有關 `devcontainer.json` 中可用變數的更多詳細信息，請參閱文件。
  - https://containers.dev/implementors/json_reference/#variables-in-devcontainerjson
- <span style='background-color: lightgreen; padding: 5px;'>[ Github CodeSpaces 文件 ]</span> Specifying recommended secrets for a repository

  - https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/configuring-dev-containers/specifying-recommended-secrets-for-a-repository
  ![](https://docs.github.com/assets/cb-146520/mw-1440/images/help/codespaces/recommended-secrets.webp)
  - 然後在 `devcontainer.json` 最上層加上 `secrets` 的描述： 
  ```json
  "secrets": {
    "NAME_OF_SECRET_1": {
      "description": "This is the description of the secret.",
      "documentationUrl": "https://example.com/link/to/info"
    },
    "NAME_OF_SECRET_2": { }
  }
  ```