# VS Code Tips

## 2026-09-04

- Tool: VS Code - Github Copilot Chat

### VS Code - Terminal

> [!QUESTION]
> VS Code 有辦法讓 Terminal 視窗跟其他檔案一樣開成一個分頁嗎？遇到的問題是當開啟 Markdown Preview 時，Terminal 會被強迫壓縮回下方

可以 — 把 Terminal 移到「編輯器區域（editor area）」就會像其他檔案一樣以分頁/分割視窗存在，開啟 Markdown Preview 就不會把它強制壓到下方面板了。

做法（幾種選擇）：

- 用 Command Palette（Ctrl+Shift+P）
  - 輸入並執行：Terminal: Create New Terminal in Editor Area（建立新的 Terminal 並放在編輯器）
  - 或：Terminal: Move Terminal into Editor Area（把現有的 Terminal 移到編輯器）

- 用 UI 快速操作
  - 在 Terminal 的標籤上（或右上角的下拉/三點選單）右鍵，選「Move to Editor Area / Open in Editor」（視語系顯示）
  - Terminal 就會變成一個 editor tab，你可以像一般檔案一樣分割、移動或關閉。
- 預設新 Terminal 都放在編輯器（不想每次都移）
  - 打開設定（Ctrl+,），搜尋「terminal default location」，把 Terminal > Integrated: Default Location 設為 Editor
  - 或在 settings.json 加入：
    ```
    "terminal.integrated.defaultLocation": "editor"
    ```

把 Terminal 放到 editor area 後，Markdown Preview（或其他檔案）在開啟/切換時不會再去壓縮下方的 panel；Terminal 會以 tab 的形式存在於某個編輯器分割頁中，行為就跟其他編輯器檔案一致。

如果要把它移回下面的 panel，右鍵該 Terminal 的編輯器分頁，選「Move Terminal to Panel」或用 Command Palette 對應的命令即可。

> [!QUESTION]
> 怎麼設定 VS Code 預設 Trim Trailing Whitespace?

可以，VS Code 的設定名稱是：

- `files.trimTrailingWhitespace`

你可以直接在 Settings 裡搜尋「Trim Trailing Whitespace」，打開後勾選，或直接加到 settings.json：

```json
"files.trimTrailingWhitespace": true
```

如果你想搭配「存檔時自動格式化」也可以一起加：

```json
"files.trimTrailingWhitespace": true,
"editor.formatOnSave": true
```

如果你只想關掉某些語言的尾端空白清理（例如 Markdown），可補一個覆寫：

```json
"files.trimTrailingWhitespace": true,
"markdown.trimTrailingWhitespace": false
```

- 方法 1：透過 UI
    - 按 `Ctrl + ,`
    - 搜尋：`Trim Trailing Whitespace`
    - 啟用即可

- 方法 2：直接改 settings.json
    - 按 `Ctrl + Shift + P`
    - 輸入 `Open Settings (JSON)`
    - 加入上面的設定

- 提醒：
    - 這個設定通常是「存檔時」生效，不是即時即刻改動。
    - 若你想保留 Markdown 內的尾端空白（有時會用來強制換行），建議保留 `markdown.trimTrailingWhitespace: false`。