# html2pdf.js

> Client-side HTML-to-PDF rendering using pure JS.

- Website:
  - https://ekoopmans.github.io/html2pdf.js/
- Git Repo:
  - https://github.com/eKoopmans/html2pdf.js

## 2025-01-06

- 參考： 2020-10-03 -- html2pdf.js如何輸出百頁pdf，看這篇就對了
  - https://ithelp.ithome.com.tw/articles/10248430?sc=pt
- 實作：
  - 根據 https://ekoopmans.github.io/html2pdf.js/#console 使用 Chrome DevTool Console 的作法，先做第一種實驗。
- 打開 
- 狀況一：如何將生成的 PDF 真的下載下來？
  - 不管直接呼叫 `html2pdf(document.body)` 或產生 `worker` 物件，都沒有觸發下載檔案。
```javascript
function addScript(url) {
     var script = document.createElement('script');
     script.type = 'application/javascript';
     script.src = url;
     document.head.appendChild(script);
 }
 addScript('https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js');

html2pdf(document.body)
var worker = html2pdf().from(element).save();
```
 - 參考 https://ithelp.ithome.com.tw/articles/10248430?sc=pt
```javascript
function addScript(url) {
     var script = document.createElement('script');
     script.type = 'application/javascript';
     script.src = url;
     document.head.appendChild(script);
}

addScript('https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js');

const opt = {
    margin: 1,
    filename: 'demo.pdf',
    image: { type: "jpg", quality: 0.9 },
    html2canvas: { dpi: 96, letterRendering: true, useCORS: true },
    jsPDF: { unit: 'pt', format: 'A3', orientation: 'portrait' }
};

let doc = html2pdf().from(document.body).set(opt).toPdf()
doc.save().then(() => console.dir('done'));
```
- ( 2025-01-06 20:30:35 )
- 還是 <span style="background-color: #ff0000; border-color: #ff0000; color: #ffffff; padding: 3px;">失敗</span>