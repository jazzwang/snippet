# Github Flavored Markdown (GFM)

- https://github.github.com/gfm/

## Admonitions 示警

- 緣起：
  - 原本在 VS Code `Markdown Preview Enhanced` 裡發現一個新語法，會產生像電子書裡常見的「注意」框。英文說明寫著 Admonitions
    - https://shd101wyy.github.io/markdown-preview-enhanced/#/markdown-basics?id=admonition
  - 想查一下 Github 是否有支援對應的語法
- 結果：2024-12-14 已經有官方支援了。但對應的語法 VS Code `Markdown Preview Enhanced` 沒有支援。
  - 2023-12-14: [New Markdown extension: Alerts provide distinctive styling for significant content](https://github.blog/changelog/2023-12-14-new-markdown-extension-alerts-provide-distinctive-styling-for-significant-content/)
  - 文件說明：[Alerts Syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#alerts)
  - 2024-06-07: [How to Create Admonitions in GitHub Markdown](https://blog.solichain.com/how-to-create-admonitions-in-github-markdown-ab580debcfdc)

> [!NOTE]
> Make sure to check the compatibility of this library with your project's dependencies.

> [!TIP]
> To improve performance, enable caching in your configuration settings.

> [!IMPORTANT]
> Ensure you have administrator privileges before running the installation script.

> [!WARNING]
> Deleting system files can cause your operating system to become unstable or unbootable.

> [!CAUTION]
> Using this function with incorrect parameters may result in data loss.

- 其他參考：
  - https://stackoverflow.com/questions/50544499/github-flavored-markdown-how-to-make-a-styled-admonition-box-in-a-gist
    - 這種用 Emoji + Quote 語法是比較通用。

> **⚠️ Warning**
>
> You shouldn't. This is irreversible!

> **❌ Error**
>
> Don't do that. This is irreversible!

> **ℹ️ Information**
>
> You can do that without problem.

> **✅ Success**
>
> Don't hesitate to do that.

> **🦄 New line support**
>
> It supports new lines:
>
> .. simply use an empty `>` line

或者

> <picture>
>   <source media="(prefers-color-scheme: light)" srcset="https://github.com/Mqxx/GitHub-Markdown/blob/main/blockquotes/badge/light-theme/warning.svg">
>   <img alt="Warning" src="https://github.com/Mqxx/GitHub-Markdown/blob/main/blockquotes/badge/dark-theme/warning.svg">
> </picture><br>
>
> Warning

- TODO: 研究怎麼讓 `Markdown Preview Enhanced` 也支援 Github Flavored Markdown 的 Alerts (Admonitions) 語法。
- PS. `Markdown Preview Enhanced` 看起來是用 `Material for MkDocs` （因為文件裡有連結到 https://squidfunk.github.io/mkdocs-material/reference/admonitions
- 看了一下程式碼，只有相依 [marked.js](https://github.com/markedjs/marked)