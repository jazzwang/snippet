# fzf

- Git Repo
  - https://github.com/junegunn/fzf
- Website
  - https://junegunn.github.io/fzf/

## 2026-09-04

- 緣起：
  - 裝了 `fzf` 好一段時間了，但是還沒有很順手。
  - 特別是遇到『想查檔案，然後直接用預設工具開啟這個檔案』這種場景
- 解法：

> [!QUESTION]
> 怎麼把 fzf 找到的檔案路徑餵給另一個指令

要把 [fzf](https://github.com/junegunn/fzf) 找到的檔案路徑餵給另一個指令，最常見的方法有以下 4 種，你可以根據「要不要同時處理多個檔案」或「操作習慣」來選擇：

### 1\. 使用 Command Substitution（命令替換）- 最直覺

這是最常見的做法，用 `$()` 把 `fzf` 包起來。Shell 會先執行 `fzf`，等你選好檔案後，再把路徑放進前面的指令中。

```bash
# 用 vim 開啟選中的檔案
vim $(fzf)

# 複製選中的檔案到 /tmp
cp $(fzf) /tmp/

```

### 2\. 使用 `xargs` - 適合接在 Pipe（管線）後面

如果你習慣用管線 `|` 將前面的輸出丟給後面，`xargs` 是最好的選擇。它會把 `fzf` 的輸出轉成後面指令的參數。
```bash
# 用 cat 讀取檔案內容
fzf | xargs cat

# 如果檔案名稱包含空白字元，建議加上 -d '\n'（指定換行符號分隔）
fzf | xargs -d '\n' nano

```

### 3\. 使用內建快捷鍵 `CTRL-T` - 最有彈性

如果你已經在命令列輸入到一半，這招最快。`fzf` 預設的快捷鍵 `CTRL-T` 會把選中的檔案路徑直接插入到目前游標的位置。 [1, 2]

1.  在終端機輸入：`ls -l `（後面留一個空格）
2.  按下 `CTRL-T`
3.  模糊搜尋並選好檔案，按下 `Enter`
4.  路徑會直接填入原指令中，變成 `ls -l ./your/file.txt`，這時再按一次 `Enter` 就會執行。 [1, 3, 4]

### 4\. 進階：支援「多選」多個檔案

如果你希望一次選很多個檔案餵給另一個指令，可以在 `fzf` 後面加上 `-m`（或 `--multi`），在選單中按 `Tab` 鍵可以勾選多個檔案，選完後按 `Enter` 輸出。 [5]

```bash
# 多選檔案並一起用 vim 開啟
fzf -m | xargs vim

# 或是使用命令替換（一樣要在 fzf 後面加 -m）
rm $(fzf -m)
```

你想把路徑餵給哪一個特定的指令呢？如果是比較複雜的指令（例如需要指定參數位置），我可以幫你寫成更精準的 `xargs` 或 Shell 函式！

[1] [https://www.itnotetk.com](https://www.itnotetk.com/2026/05/05/fzf-fuzzy-finder-shell-toolkit/)
[2] [https://blog.csdn.net](https://blog.csdn.net/u013318019/article/details/143962565)
[3] [https://forum.archlinuxcn.org](https://forum.archlinuxcn.org/t/topic/11681)
[4] [https://hackmd.io](https://hackmd.io/@steepinglogic/fzf)
[5] [https://op8867555.github.io](https://op8867555.github.io/posts/2017-11-27-cli-tools-ag-rg-fzf-fd.html)