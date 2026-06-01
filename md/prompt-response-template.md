<table><tr style="background-color:lightyellow;"><td>Q:</td><td>
</td></tr><tr style="background-color:lightgreen;"><td>Tool:</td><td>
</td></tr><tr><td>A:</td><td>
</td></tr>
</table>

備忘：

* Google Deep Research 結果
  用 `Markdown Paste` 貼上 `VS Code` 以後，
  需要用到的幾個正規表示法取代：
  - **取代 #1** (把「參考資料」的部份，拿掉網站 favicon )
    - From:
        ```
        \[!\[\](.*).*\n
        ```
    - To:
        ```
        \n- [
        ```
  - **取代 #2**
    - From:
        ```
        \n\nOpens in a new window\]
        ```
    - To:
        ```
        ]
        ```