# Windows Troubleshoot 各種疑難雜症/狀況排除

## 2026-01-11

- 狀況：突然 Windows 的 Start Menu 沒辦法按，要開 Terminal 也顯示 explore.exe 無法開啟
- 參考：
  - https://learn.microsoft.com/en-us/answers/questions/5657217/after-windows-11-update-start-menu-does-not-work-r
- 解法：
  - 按 CTRL+R 然後輸入 powershell
  - 在 PowerShell 底下輸入
    ```powershell
    Windows PowerShell
    Copyright (C) Microsoft Corporation. All rights reserved.

    Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

    PS C:\Users\jazzw> reg delete HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\IrisService /f
    PS C:\Users\jazzw> shutdown -r -t 0
    ```
  - 重新開機以後，就恢復正常了。
- 追查：
  - Explore.exe 在 2025-12-11 有被更動過，看起來是 Security Patch/Update 造成的

## 2026-01-19

<table>
<tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
為何 windows 11 突然一直在讀取硬碟，根據 `Resource Monitor` 的查詢結果，判定主要是 `System (PID=4)` 跟 `SearchIndexer.exe` 兩個執行檔
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
這是一個在 Windows 11 非常常見且令人煩躁的問題。這通常不是病毒，而是 Windows 的**維護機制失控**或**卡在某個檔案上**。

簡單來說：

* **SearchIndexer.exe**：是「Windows 搜尋」，它正在建立檔案索引以便你搜尋。如果它一直跑，通常是因為**卡在某個損壞的檔案**或是**索引資料庫壞了**。
* **System (PID 4)**：是 Windows 核心。高讀取通常代表**記憶體不足（正在使用虛擬記憶體/硬碟）**，或者是**Windows Update 在背景運作**。

在你嘗試修復之前，建議先做這一步驟找出「元兇」，這比盲目關閉服務更有效。

---

### 第一步：找出「究竟在讀哪個檔案」？（最重要的一步）

不要猜測，直接用內建工具看它卡在哪裡：

1. 按下 **Ctrl + Shift + Esc** 開啟「工作管理員」。
2. 切換到 **[效能]** 分頁，點擊底部的 **[開啟資源監視器]** (Resource Monitor)。
3. 在資源監視器中，點擊 **[磁碟]** 分頁。
4. 在中間的 **[磁碟活動]** 列表中，點擊「檔案」欄位標題進行排序。
5. **觀察：** 看 `System` 或 `SearchIndexer` 正在瘋狂讀寫**哪個檔案路徑**？
* 如果是 `.ost` 或 `.pst`：這是 Outlook 電子郵件索引，通常是罪魁禍首。
* 如果是 `pagefile.sys`：代表你的 **RAM (實體記憶體) 不夠用了**，系統被迫一直讀寫硬碟當記憶體用。
* 如果是 `Windows\SoftwareDistribution`：代表 Windows 正在背景下載或安裝更新。
* 如果是某個特定的影片或 PDF 檔：代表該檔案可能損壞，導致索引器卡住。



---

### 第二步：針對 SearchIndexer 的解決方案

如果資源監視器顯示 `SearchIndexer.exe` 佔用最高，請嘗試以下順序：

#### 1. 執行搜尋與索引疑難排解

* **設定** > **系統** > **疑難排解** > **其他疑難排解**。
* 找到 **[搜尋與索引]**，點擊 **[執行]**。讓系統自動修復。

#### 2. 重建索引（徹底解決索引資料庫損壞）

這是最有效的解法，但需要一點時間執行。

* 按下 `Win + S`，搜尋「**索引選項**」(Indexing Options) 並開啟。
* 點擊 **[進階]** (Advanced)。
* 在「疑難排解」區塊下，點擊 **[重建]** (Rebuild)。
* *注意：這會花費數小時重新建立索引，期間電腦可能會慢一點，建議睡覺前做。*



#### 3. 暫時停用（如果硬碟聲真的很吵）

如果不急著修復，只想立刻安靜下來：

* 按下 `Win + R`，輸入 `services.msc`。
* 找到 **Windows Search**，右鍵選 **[停止]** (Stop)。
* *副作用：開始選單的搜尋功能會變得很慢。*



---

### 第三步：針對 System (PID 4) 的解決方案

如果 `System` 佔用最高，通常與系統資源管理有關：

#### 1. 檢查 Windows Update

* 去 **設定** > **Windows Update**。
* 如果有更新正在「安裝中」或「下載中」，請讓它跑完，這是正常的。跑完重開機就會恢復正常。

#### 2. 檢查記憶體與虛擬記憶體

如果你看到它一直在讀寫 `pagefile.sys`：

* 代表你的 Chrome 分頁開太多，或軟體吃光了 RAM。
* **解法：** 關閉多餘的應用程式。如果是長期問題，考慮增加實體 RAM。

#### 3. 關閉 SysMain (舊稱 Superfetch)

這個服務會預先將程式載入記憶體以加速啟動，但在某些硬碟（特別是傳統 HDD）上會造成反效果。

* 按下 `Win + R`，輸入 `services.msc`。
* 找到 **SysMain**，右鍵點擊 **[內容]**。
* 將啟動類型改為 **[已停用]**，並點擊 **[停止]**。

---

### 第四步：最後的大絕招 (系統健康檢查)

如果以上都沒用，可能是系統檔案受損。請以「系統管理員身分」開啟 CMD (命令提示字元)，依序執行以下兩行指令：

1. 修復磁碟錯誤：
`chkdsk /f /r`
*(它會問你是否下次重開機時執行，輸入 Y 然後重開機)*
2. 修復系統檔案：
`sfc /scannow`

---

### 下一步你能做什麼？

你剛剛在「資源監視器」裡，看到 `SearchIndexer` 或 `System` 具體是在讀取**哪個檔案名稱**嗎？

如果是某個特定的檔案（例如 `outlook.ost` 或某個影片檔），**請告訴我那個檔名**，我可以教你如何針對那個檔案將它「排除在索引之外」，這樣就不用重建整個資料庫了。
</td></tr>
<tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
看起來一直在讀取 `C:\ProgramData\Microsoft\Search\Data\Applications\Windows\Windows.db`
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->

這是一個非常經典的 Windows 11 效能問題。`Windows.db` 是 Windows 搜尋索引的**核心資料庫檔案**。

當你發現 `SearchIndexer` 與 `System` 一直在讀取它時，通常代表這幾種情況：

1. **資料庫受損 (Corruption)**：索引檔壞了，系統反覆嘗試修復或讀取失敗，導致硬碟狂跑。
2. **檔案變動太頻繁**：例如你正在下載大量檔案，或 Outlook 正在同步數千封郵件。
3. **索引目標太大**：你可能把整個 C 槽或大容量資料槽都納入索引了。

請按照以下順序操作，這能解決 90% 以上 `Windows.db` 造成的讀取問題：

---

### 方案一：重建索引資料庫 (最推薦)

這會刪除舊的 `Windows.db` 並讓系統重新生成一個乾淨的。

1. 按下 `Win + S`，搜尋「**索引選項**」(Indexing Options) 並開啟。
2. 點擊下方的 **[進階]** (Advanced) 按鈕（可能需要管理員權限）。
3. 在「疑難排解」區塊，點擊 **[重建]** (Rebuild)。
4. 系統會彈出警告，點擊「確定」。
* **注意：** 重建期間搜尋功能會暫時無法使用，且硬碟會持續讀取一段時間。建議在不使用電腦時（如午休或睡覺）放著讓它跑完。

---

### 方案二：排除「最吵」的索引位置

如果你有使用 **Outlook** 或是有一個放滿小檔案的資料夾，它們是 `Windows.db` 異常增長的元兇。

1. 同樣在「**索引選項**」視窗，點擊 **[修改]** (Modify)。
2. 在上方清單中，檢查是否有不必要的路徑被勾選。
3. **特別建議：** 如果你有用 Outlook 且郵件量極大，試著**取消勾選「Microsoft Outlook」**。這能極大程度減輕 `Windows.db` 的負擔（代價是 Outlook 內搜尋會變慢）。

---

### 方案三：使用指令強制「重設」搜尋服務

如果連「索引選項」都卡死打不開，可以用指令強行重設。

1. 搜尋 `CMD`，對它點右鍵選擇「**以系統管理員身分執行**」。
2. 依序輸入以下指令（每行結束按 Enter）：

```cmd
net stop wsearch
del "%ProgramData%\Microsoft\Search\Data\Applications\Windows\Windows.db"
net start wsearch
```

* 這會停止服務、強行刪除該檔案，然後重新啟動服務讓它自動生出一個新的資料庫。*

---

### 方案四：關閉「內容搜尋」 (針對 HDD 或慢速 SSD)

如果你的硬碟讀取壓力還是很大，可以限制它只索引「檔名」而不讀取「檔案內容」：

1. 在「索引選項」 > **[進階]** > **[檔案類型]**。
2. 將下方的選項改為「**僅針對內容索引屬性**」(Index Properties Only)。
3. 這樣系統就不會去「拆開」每個 Word 或 PDF 讀裡面的文字，能顯著降低 `System` 的負載。

---

### 補充建議：這台電腦有裝 Outlook 嗎？

如果你的 `Windows.db` 讀取量極高，且你有在使用 Outlook，通常是因為 Windows 11 在嘗試索引你的 `.ost` 或 `.pst` 郵件檔。

**你需要我幫你確認如何單獨優化 Outlook 的搜尋設定嗎？**
</td></tr>
</table>

- 參考：
  - https://zhuanlan.zhihu.com/p/507590692

## 2026-01-20

```bash
PS C:\ProgramData\Microsoft\Search\Data\Applications\Windows> bash
/c/ProgramData/Microsoft/Search/Data/Applications/Windows$ ls -al
total 1232488
drwxr-xr-x 1 jazzw 197609          0 Jan 19 08:31 .
drwxr-xr-x 1 jazzw 197609          0 Sep  9  2024 ..
drwxr-xr-x 1 jazzw 197609          0 Sep  9  2024 GatherLogs
drwxr-xr-x 1 jazzw 197609          0 Sep  9  2024 Projects
-rw-r--r-- 1 jazzw 197609 1206644736 Jan 19 15:35 Windows.db
-rw-r--r-- 1 jazzw 197609    2228224 Jan 19 12:08 Windows.db-shm
-rw-r--r-- 1 jazzw 197609    4165352 Jan 19 15:35 Windows.db-wal
-rw-r--r-- 1 jazzw 197609   42307584 Jan 19 15:35 Windows-gather.db
-rw-r--r-- 1 jazzw 197609      32768 Jan 19 08:31 Windows-gather.db-shm
-rw-r--r-- 1 jazzw 197609    4132392 Jan 19 15:35 Windows-gather.db-wal
-rw-r--r-- 1 jazzw 197609    2428928 Aug 29 11:51 Windows-usn.db
-rw-r--r-- 1 jazzw 197609      32768 Jan 19 08:31 Windows-usn.db-shm
-rw-r--r-- 1 jazzw 197609          0 Jan 19 08:31 Windows-usn.db-wal
/c/ProgramData/Microsoft/Search/Data/Applications/Windows$ du -sh *
1.6M    GatherLogs
904K    Projects
1.2G    Windows.db
2.2M    Windows.db-shm
4.0M    Windows.db-wal
41M     Windows-gather.db
32K     Windows-gather.db-shm
4.0M    Windows-gather.db-wal
2.4M    Windows-usn.db
32K     Windows-usn.db-shm
0       Windows-usn.db-wal
```

