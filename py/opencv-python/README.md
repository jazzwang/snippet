## 2024-04-14

### 緣起

> 因應小學生書包減重，小孩又常忘記把課本帶回家，為了避免考前需要查課文內容，原本是靠 Microsoft 365 的 Application 一頁一頁做圖片邊緣辨識、梯形校正，但手機應用程式用起來比較不順手，而且想要先大量拍照再做梯形校正。所以問了 ChatGPT，得到一些 macOS 的應用程式 [1]：
> * OpenCV
> * ScanTailor [2]
> * Paperwork [3]
> 
> 可惜 ScanTailor 已經很久沒更新了。查 Linux 套件 Debian 10 才有。
> Paperwork 也是處於 public archive 狀態。
> 暫時沒找到其他合用的工具，所以來玩玩 OpenCV python 版本的實作。

[1] https://chat.openai.com/share/e1390740-aec8-4428-ad2a-1457fb810b5a
[2] https://github.com/scantailor/scantailor
[3] https://github.com/paperwork/paperwork

### 參考

* https://github.com/andrewdcampbell/OpenCV-Document-Scanner
    * 這個 Python 實作有 GUI 可以視覺化邊界該怎麼切
* https://learnopencv.com/automatic-document-scanner-using-opencv/
* https://github.com/topics/document-scanner?l=python
    * 一些 Python OpenCV 掃描文件的 repo
    * https://github.com/danielgatis/docscan