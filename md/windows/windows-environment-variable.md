在 Windows 中，如果你使用 `setx` 建立了環境變數，想要將它**刪除**（移除），有幾種不同的方法。

最推薦的是使用 **方法一（PowerShell）** 或 **方法二（登錄檔指令）**，因為 Windows 內建的 `setx` 本身**沒有**提供刪除變數的參數。

### 方法一：使用 PowerShell（最快、最現代）

這是目前最乾淨、最不傷大腦的作法。

1.  打開 **PowerShell**。
2.  輸入以下指令並按 Enter：

    ```powershell
    [Environment]::SetEnvironmentVariable("COUNTER", $null, "User")
    ```

    *這行指令的意思是：將「使用者（User）」環境中的 `COUNTER` 變數設為空值（`$null`），Windows 就會自動把它整條刪除。*

### 方法二：使用命令提示字元 (CMD) / Git Bash 刪除

如果你習慣使用 CMD 或 Git Bash，可以透過修改 Windows 登錄檔（Registry）來刪除它，因為 `setx` 建立的使用者變數其實都存在登錄檔的 `HKCU\Environment` 路徑下。

在 CMD 或 Git Bash 中輸入以下指令：

```Bash
reg delete "HKCU\Environment" /v COUNTER /f
```

-   `/v COUNTER`：指定要刪除的名值對（Value）。
-   `/f`：強制刪除，不需要再跳出提示詢問 `(Y/N)`。

### 方法三：圖形介面手動刪除（視覺化）

如果你想眼見為憑，確認它真的消失了，可以用 GUI 介面：

1.  按下 `Win + R` 鍵，輸入 `sysdm.cpl` 並按 Enter（這會打開「系統內容」）。
2.  切換到 **「進階」** 頁籤，點選最下方的 **「環境變數」**。
3.  在上方視窗的 **「<你的用戶名> 的使用者變數」** 清單中，找到 `COUNTER`。
4.  點選它，然後按下 **「刪除」** 按鈕。
5.  一路點擊「確定」送出即可。

### ⚠️ 重要提醒

不論你用上述哪一種方法刪除：

1.  **當前已經打開的終端機視窗**（CMD、PowerShell 或 Git Bash）依然會殘留舊的變數記憶。
2.  你必須**關閉並重新打開**一個新的終端機視窗，輸入 `echo $COUNTER`（Git Bash）或 `echo %COUNTER%`（CMD），就會發現它已經徹底消失了！