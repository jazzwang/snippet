# 人工產生寄發信件的腳本

## 緣起

- 2024-06-19 22:21:38

> 由於想要辦線上投票，希望可以一人一個專屬的 Google 表單已經預填好「票證驗證碼」、「會員編號」、「姓名」三個欄位，並且透過縮網址服務產生 1-to-1 縮網址。然後寄送給每個會員。

## 實作

- `gen-prefill-link.py` - Google 表單網址是寫死的，若要用在其他表單上，需要自行產生 prefill 的範本網址，並把欄位內容改以 "{}" 取代。
- 跑法：
```bash
jazzwang:~/git/snippet/python/urllib$ python3 gen-prefill-link.py sample_input.csv 

https://docs.google.com/forms/d/e/1FAIpQLScxin7cEvC-G6TpBTDNS4a3TMWC2IZXJiH_Qel15jdKMQgV-w/viewform?usp=pp_url&entry.246220059=a113c33d-9791-4eea-9678-ce83a9045105&entry.510881599=P0001&entry.136181766=%E7%8E%8B%E8%80%80%E8%81%B0
```
- `gen-mail-html.py` 
    - `SURL` 欄位是手動上傳到 https://picsee.io/bulk 產生的結果。
    - 輸入：
        - `mail_subject` 檔：如果是中文信件主旨，需要用 urlencode 轉換過
        - `mail_template.tpl` 檔：信件本文，需要變數取代的部分用 {} 標記。會在程式中用 format() 把變數取代進去。
        - `sample_input.csv` 檔：範本輸入，必須保留第一行標題 Header，因為程式碼要用到 Header 的名稱來取出變數。
    - 輸出到 STDOUT，所以若要用，得導向到 HTML 檔
- 跑法：
```bash
jazzwang:~/git/snippet/python/urllib$ python3 gen-mail-html.py sample_input.csv | tee output.html
<html><body><ol>
<li><a target='_blank' href='mailto:jazzwang@example.com?subject=%E7%A4%BE%E5%9C%98%E6%B3%95%E4%BA%BA%E8%87%BA%E7%81%A3%E8%B3%87%E6%96%99%E5%B7%A5%E7%A8%8B%E5%8D%94%E6%9C%83%E7%AC%AC%E4%BA%8C%E5%B1%86%E7%90%86%E7%9B%A3%E4%BA%8B%E9%81%B8%E8%88%89%20--%202024-06-27%20%28%E5%9B%9B%29%2013%3A00%20%E6%88%AA%E6%AD%A2%0A&body=%E7%8E%8B%E8%80%80%E8%81%B0%EF%BC%8C%E6%82%A8%E5%A5%BD%EF%BC%9A%0A%0A%E7%85%A9%E4%BD%BF%E7%94%A8%E6%82%A8%E5%B0%88%E5%B1%AC%E7%9A%84%E9%80%A3%E7%B5%90%E9%80%B2%E8%A1%8C%E6%8A%95%E7%A5%A8%EF%BC%9A%0Ahttps%3A//pse.is/64653m%0A%E6%AD%A4%E9%80%A3%E7%B5%90%E5%B7%B2%E6%9B%BF%E6%82%A8%E5%A1%AB%E5%85%A5%E6%9C%83%E5%93%A1%E7%B7%A8%E8%99%9F%E8%88%87%E5%A7%93%E5%90%8D%EF%BC%8C%0A%E8%8B%A5%E5%A7%93%E5%90%8D%E4%B8%8D%E6%AD%A3%E7%A2%BA%EF%BC%8C%E8%AB%8B%E5%9B%9E%E8%A6%86%E7%B5%A6%E6%88%91%E5%B9%AB%E6%82%A8%E9%87%8D%E6%96%B0%E7%A2%BA%E8%AA%8D%E3%80%82%0A%0A%E6%84%9F%E8%AC%9D%E5%90%84%E4%BD%8D%E6%9C%83%E5%93%A1%E9%81%8E%E5%8E%BB%E7%9A%84%E6%94%AF%E6%8C%81%EF%BC%8C%E5%8D%94%E6%9C%83%E5%9B%A0%E6%96%B0%E5%86%A0%E8%82%BA%E7%82%8E%E7%96%AB%E6%83%85%E5%81%9C%E6%93%BA%E4%B8%89%E5%B9%B4%EF%BC%8C%0A%E6%9C%AA%E8%83%BD%E5%A6%82%E6%9C%9F%E9%80%B2%E8%A1%8C%E7%AC%AC%E4%BA%8C%E5%B1%86%E7%90%86%E7%9B%A3%E4%BA%8B%E6%94%B9%E9%81%B8%E3%80%82%0A%E7%82%BA%E7%A2%BA%E4%BF%9D%E5%90%84%E9%A0%85%E6%AC%8A%E7%9B%8A%EF%BC%8C%E6%82%A8%E7%9A%84%E6%9C%83%E7%B1%8D%E5%B9%AB%E5%90%84%E4%BD%8D%E5%BB%B6%E9%95%B7%E8%87%B3%202024-12-31%E3%80%82%0A%0A%E5%85%B6%E6%AC%A1%EF%BC%8C%E5%8D%94%E6%9C%83%E7%A8%85%E7%B1%8D%E9%9C%80%E8%AE%8A%E6%9B%B4%E7%99%BB%E8%A8%98%E6%9C%83%E5%9D%80%EF%BC%8C%E5%9B%A0%E6%AD%A4%E6%88%91%E5%80%91%E9%9C%80%E8%A6%81%E5%84%98%E9%80%9F%E5%AE%8C%E6%88%90%E7%90%86%E7%9B%A3%E4%BA%8B%E6%94%B9%E9%81%B8%EF%BC%8C%0A%E4%B8%A6%E6%96%BC%E9%80%81%E4%BA%A4%E5%85%A7%E6%94%BF%E9%83%A8%E7%99%BB%E8%A8%98%E7%AC%AC%E4%BA%8C%E5%B1%86%E7%90%86%E7%9B%A3%E4%BA%8B%E5%BE%8C%EF%BC%8C%0A%E6%96%BC%E4%B8%83%E6%9C%88%E5%BA%95%E5%89%8D%E5%90%91%E5%9C%8B%E7%A8%85%E5%B1%80%E5%AE%8C%E6%88%90%E5%8D%94%E6%9C%83%E6%9C%83%E5%9D%80%E8%AE%8A%E6%9B%B4%E3%80%82%0A%E7%A4%99%E6%96%BC%E6%99%82%E7%A8%8B%EF%BC%8C%E6%8E%A1%E7%B7%9A%E4%B8%8A%E8%A8%98%E5%90%8D%E6%8A%95%E7%A5%A8%E6%96%B9%E5%BC%8F%E9%80%B2%E8%A1%8C%EF%BC%8C%E7%9B%B8%E4%BF%A1%E4%B9%9F%E6%AF%94%E8%BC%83%E4%B8%8D%E6%9C%83%E6%9C%89%E7%A5%A8%E6%95%B8%E7%88%AD%E8%AD%B0%E3%80%82%0A%0A%E6%8A%95%E7%A5%A8%E6%99%82%E9%96%93%EF%BC%9A2024-06-19%20%28%E4%B8%89%29%20~%202024-06-27%20%28%E5%9B%9B%29%2013%3A00%20GMT%2B8%0A%0A%E8%8B%A5%E6%9C%89%E4%BB%BB%E4%BD%95%E7%96%91%E7%BE%A9%E6%88%96%E7%96%91%E5%95%8F%EF%BC%8C%E6%AD%A1%E8%BF%8E%E5%9B%9E%E8%A6%86%E7%B5%A6%E6%88%91%EF%BC%8C%E8%AC%9D%E8%AC%9D%EF%BD%9E%0A%0A%E7%8E%8B%E8%80%80%E8%81%B0%20%E6%95%AC%E4%B8%8A%0A%E5%8F%B0%E7%81%A3%E8%B3%87%E6%96%99%E5%B7%A5%E7%A8%8B%E5%8D%94%E6%9C%83%20%0A%E7%99%BC%E8%B5%B7%E4%BA%BA%E6%9A%A8%E7%AC%AC%E4%B8%80%E5%B1%86%E7%90%86%E4%BA%8B%E9%95%B7%0A'>王耀聰</a></li>
</ol></body></html>
```
- 用法：如果預設的信件處理是瀏覽器，而瀏覽器的 `mailto` handler 設為 Gmail 的話，點選每個會員姓名的連結，就會產生一封新的信。確認內容後，手動需手動寄送。