# ripgrep

- Git Repo
  - https://github.com/burntsushi/ripgrep

## 2026-10-01

- 緣起：
  - 近期在使用 OpenCode 跟 Pi 的時候，都會看到 `rg` 這個指令，所以好奇查了一下這是什麼新的指令。

- Tool: Google Search - AI Mode

> [!NOTE]
> rg 是什麼指令

`rg` 是 `ripgrep` 的指令縮寫，它是一款在 Linux、macOS 和 Windows 上非常熱門的現代化高速文字搜尋工具。其主要功能是用於在專案目錄、程式碼庫或大量文字檔案中，快速搜尋特定的關鍵字或字串。 [1, 2, 3]

許多開發者會使用 `rg` 來取代傳統的 `grep` 指令，其主要特色包含： [2, 4]

* 速度極快： 使用 Rust 語言編寫，針對搜尋效能與 I/O 操作進行了深度優化，速度通常比傳統的 grep 快上數倍。
* 智慧過濾： 預設會自動忽略 .gitignore 檔案中指定的目錄（如 node_modules）、隱藏檔案以及二進位檔案，讓搜尋結果更乾淨、更精準。
* 自動遞迴： 預設就會自動搜尋當前目錄下的所有子資料夾，不需額外加上 -r 參數。 [1, 2, 4, 5, 6, 7]

### 常用基礎指令範例

如果你剛開始使用 rg，可以參考以下最常見的幾種用法： [5, 8]

* 基本關鍵字搜尋： 在當前目錄下的所有檔案中，搜尋包含 error 的行。

```
rg "error"
```

* 搜尋特定路徑： 在 src 資料夾中搜尋關鍵字。

```
rg "login" ./src
```

* 忽略大小寫搜尋 (-i)： 同時搜尋 Error、error 或 ERROR。

```
rg -i "error"
```

* 搜尋被忽略的隱藏檔案 (--hidden)： 包含預設被跳過的隱藏檔案與目錄一起搜尋。 [5, 8]

```
rg --hidden "secret_key"
```

不論你是要查找程式碼、翻閱設定檔還是分析 log 紀錄，rg 都是現代開發者與 AI agent 工具（如 Cursor、LLM 執行環境）不可或缺的文字檢索利器。 [1, 3]
您目前是在 Linux、macOS 還是 Windows 環境下打算使用 rg 呢？我可以為您提供對應的安裝方法或更進階的正規表示式（Regex）搜尋範例！

[1] [https://hackmd.io](https://hackmd.io/@tsungjung411/B1EHY7wgze)
[2] [https://blog.csdn.net](https://blog.csdn.net/qq_41483419/article/details/133179489)
[3] [https://hackmd.io](https://hackmd.io/@tsungjung411/H1UZ8M4gMg)
[4] [https://clay-atlas.com](https://clay-atlas.com/blog/2024/09/24/cn-linux-ripgrep-rg-search/)
[5] [https://ithelp.ithome.com.tw](https://ithelp.ithome.com.tw/m/articles/10271828)
[6] [https://peterpowerfullife.com](https://peterpowerfullife.com/blog/tool-command-line-ripgrep/)
[7] [https://www.51cto.com](https://www.51cto.com/article/722190.html)
[8] [https://tinghao.com.tw](https://tinghao.com.tw/news-toolx-grep-ripgrep-search)
