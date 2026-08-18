# sed

## 2026-08-17

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI Mode
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
有 awk 或 sed 指令可以在現存的文字檔第一行前面插入一行新的字串?
</td></tr><tr><td>A:</td><td>

有的，sed 和 awk 都可以非常輕鬆地達成這個需求。 [1, 2] 
以下為您整理這兩種工具的指令寫法。

## 1. 使用 sed 指令（最推薦，最精簡）

sed 提供了 i（Insert）動作，可以直接指定在第 1 行前面插入字串。 [2, 3] 

* 僅預覽結果（不更動原檔案）：

```bash
sed '1i 新的字串內容' filename.txt
```

* 直接修改並儲存檔案（加上 -i 參數）：

```bash
sed -i '1i 新的字串內容' filename.txt
```

(註：如果您使用的是 macOS，-i 後面必須多加一個空字串，寫法為 sed -i '' '1i 新的字串內容' filename.txt) [4] 

## 2. 使用 awk 指令

awk 的邏輯是在處理第一行（NR==1，意即 Number of Record 為 1）之前，先印出你想加入的新字串，隨後再依序印出原本的每一行內容。 [1, 5] 

* 輸出新結果到新檔案：

```bash
awk 'BEGIN{print "新的字串內容"} {print}' filename.txt > newfile.txt
```

或者利用 NR==1 的寫法：

```bash
awk 'NR==1{print "新的字串內容"} {print}' filename.txt > newfile.txt
```

* 直接修改原檔案（GNU awk 4.1.0 以上版本支援 -i inplace）：

```bash
awk -i inplace 'BEGIN{print "新的字串內容"} {print}' filename.txt
```

## 💡 快速總結與建議

如果你想要直接修改原本的檔案，最快且最普遍的指令是：

```bash
sed -i '1i 你的字串' filename.txt
```

若您有需要將這個指令應用在 大量檔案 或 特定格式（如 CSV 標頭） 的處理中，歡迎告訴我，我可以為您提供對應的批次處理（Shell Loop）語法！

[1] [https://ithelp.ithome.com.tw](https://ithelp.ithome.com.tw/m/articles/10055946)
[2] [https://blog.csdn.net](https://blog.csdn.net/gsjthxy/article/details/118905770)
[3] [https://www.fooish.com](https://www.fooish.com/linux/sed.html)
[4] [https://myapollo.com.tw](https://myapollo.com.tw/blog/sed-insert-a-line-to-a-specific-position/)
[5] [https://www.cs.nccu.edu.tw](https://www.cs.nccu.edu.tw/~lien/UNIX/AWK/hardcopy.htm)

</td></tr>
</table>