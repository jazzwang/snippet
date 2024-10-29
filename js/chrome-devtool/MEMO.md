# Development Notes

[TDC]

## 2024-07-25

- 需求：為了一些自動化的需求，需要在 Island Browser 裡面透過 Chrome DevTool 開啟多個內網 URL
- 參考：How to Open URL in New Tab using JavaScript?
  - https://www.geeksforgeeks.org/how-to-open-url-in-new-tab-using-javascript/
- 解法：
  ```js
  window.open(URL, '_blank');
  ```

## 2024-10-29 - Island Browser 資料整理

- 實際實測之後，發現如果用迴圈去跑 `window.open(URL, '_blank')` 只會開一個分頁。
- 解法：前面加上 `await`
```js
const emp_ids = [
    '000000001',
    '000000013'
]

const base_url = 'https://example.com/Employee/Profile?employeeId='

for (let i = 0; i < emp_ids.length; i++) {
    await window.open(base_url + emp_ids[i], "_blank")
}
```

## 2024-10-29 - LinkedIn Saved Posts

- https://www.linkedin.com/my-items/saved-posts/ 必須捲動到最底下，才能看到更多內容。我想要取得全部儲存的 Saved Posts.
- 首先，用 DevTool 製造一堆捲動到最下方的事件，讓瀏覽器去觸發
```js
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

for ( let i = 1; i < 100; i++ ) {
    await sleep(1000); // sleep 1 second
    window.scrollTo(0, document.body.scrollHeight);
}
```
- 接著，用 inspect 找出需要的物件 css selector 長怎樣。
- 以下是取得 LinkedIn Saved Posts 的語法：
```js
// 先查一下最後有幾筆 Saved Posts
count = $$("div.mh4 a.app-aware-link").length

var links = []
for (let i=0; i < count; i++) {
    links.push($$("div.mh4 a.app-aware-link")[i].href.split('?')[0]);
}

var a = document.createElement('a');
var file = new Blob([ links.toString() ], { type: 'text/plain' });
a.href = URL.createObjectURL(file);
a.download = 'linkedin-saved-posts.txt';
a.click();
```
- 參考：[寫檔案] https://stackoverflow.com/a/43027178