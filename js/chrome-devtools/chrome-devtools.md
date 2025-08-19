# Development Notes

> https://developer.chrome.com/docs/devtools 會是個好的起點！ 


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

## 2024-10-30 - O'Reilly Cookie

- 緣起：有時候為了一些自動化流程，我們需要把網站的 cookie 存起來。這裡以 https://learning.oreilly.com/ 為例。
- ( 2024-10-30 10:35:08 )
- 參考：https://g.co/gemini/share/0cd3d5865fe5
- 以下是 Google Gemini 給的參考程式碼：
```js
function getCookie(name) {
  const cookies = document.cookie.split(';');
  for (let i = 0; i < cookies.length; i++) {
    const cookie = cookies[i].trim();
    if (cookie.startsWith(name + '=')) {
      return cookie.substring(name.length + 1);
    }
  }
  return null;
}
```
- 這個範例是要查指定 `name` 為 key 的 cookie value
- 若想要將全部的 cookie 存成 JSON 格式，首先我們可以先用 `document.cookie.split(';')` 取得完整列表。
- 拿 O'Reilly 當例子，是因為發現 cookie value 裡包含字元 `=` 所以如果用 `cookie.split('=')` 會得到錯誤的結果。
- 參考：
- 以下是 給的 `splitOnFirstEqual()`，也就是只針對第一個分隔字元去回傳 (key, value) pair
```js
function splitOnFirstEqual(str) {
    const index = str.indexOf('=');
    if (index === -1) {
        return [str]; // 如果沒有找到 `=`，返回整個字符串
    }
    const beforeEqual = str.substring(0, index);
    const afterEqual = str.substring(index + 1);
    return [beforeEqual, afterEqual];
}
```
- 這行 lambda 就需要想一下了 :)
  - `console.log(...data)` : 輸出最後的 JSON 字串到 DevTools Console
  - `JSON.stringify(value, ?replacer, ?space)` : 將 `value` 陣列，轉成 JSON 字串。
  - `document.cookie.split(';')` - 將全部的 cookie 轉成 `Array(string)`
  - `document.cookie.split(';').map(c => splitOnFirstEqual(c))` - 是把每一個 string 從第一個 `=` 斷開成 Array(2) ([ key , value ])。所以結果會是 `Array(Array(2))`
  - `.map(i => [i[0].trim(), i[1].trim()])` - 將 `key` (即 `i[0]`) 跟 `value` (即 `i[1]`) 的字串**前後空白**移除。結果維持是 `Array(Array(2))`
  - `.reduce((r, i) => {r[i[0]] = i[1]; return r;},{})` - 還好學過 mapreduce，
```js
console.log(JSON.stringify(document.cookie.split(';').map(c => splitOnFirstEqual(c)).map(i => [i[0].trim(), i[1].trim()]).reduce((r, i) => {r[i[0]] = i[1]; return r;}, {})))
```

## 2024-11-26

- 在找怎麼讓 Chrome DevTools 可以觸發 save as MHTML 的事件，找到這個連結。
- [Edit and save files in a workspace](https://developer.chrome.com/docs/devtools/workspaces)
- 看了一下內容，比較像是在 Local 做開發，然後可以讓 DevTools 即時反應 CSS/HTML/JavaScript 異動的範例。
- 不過如果想要熟悉 Chrome DevTools 的用法，https://developer.chrome.com/docs/devtools 會是個好的起點。

## 2025-08-19

- 需求：在 Windows 上模擬 macOS Safari 瀏覽器的行為
- 嘗試：
  - Windows + WSL + KVM + KVM-OpenCore + Docker + macOS installer image
    - https://github.com/sickcodes/Docker-OSX?tab=readme-ov-file#id-like-to-run-docker-osx-on-windows
  - 直接在 Edge 或 Chrome 瀏覽器中修改 `User-Agent` header string
    - 2025-06-30: [Microsoft Learn][Microsoft Edge] Override the user agent string
      - https://learn.microsoft.com/en-us/microsoft-edge/devtools/device-mode/override-user-agent
      - Press Ctrl+Shift+P (Windows, Linux) or Command+Shift+P (macOS) to open the Command Menu.
      ![](https://learn.microsoft.com/en-us/microsoft-edge/devtools/device-mode/override-user-agent-images/device-mode-console-command-menu.png)
      - Type `network conditions`, select Show Network conditions, and then press Enter to open the Network conditions tool.
      ![](https://learn.microsoft.com/en-us/microsoft-edge/devtools/device-mode/override-user-agent-images/device-mode-console-command-menu-network-conditions.png)
      - In the User agent section, clear the Use browser default checkbox.
      ![](https://learn.microsoft.com/en-us/microsoft-edge/devtools/device-mode/override-user-agent-images/clear-use-browser-default-checkbox.png)
  - User-Agent Switcher
    - (Chrome) https://chromewebstore.google.com/detail/user-agent-switcher-for-c/djflhoibgkdhkhhcedjiklpkjnoahfmg
    - (Firefox) https://addons.mozilla.org/en-US/firefox/addon/uaswitcher/
    - (Edge) https://microsoftedge.microsoft.com/addons/detail/npjnioaeoicmjokbdpfiecnbildopjad