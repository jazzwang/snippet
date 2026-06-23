## 2025-07-07

底下這段還不 work

```js
$$("div.newly-added").forEach(transcript => {
    // Get author name
    const authorElement = transcript.querySelector('[data-tid="author"]');
    if (!authorElement) return; // Skip if no author found
    const Name = authorElement.innerText.trim();
    // Get caption text
    const textElement = transcript.querySelector('data-tid="closed-caption-text"]');
    if (!textElement) return; // Skip if no text found
    const Text = textElement.innerText.trim()
    const Time = transcript.getAttribute('data-time')
    console.log({Time, Name, Text})
}
```

目的是想要取得 "div.newly-added" (因為還有其他 "i.newly-added" 在 live caption 的 DOM 裡)
然後把 Author, transcript 跟 timestamp 拿出來，
最好取出後能把 `newly-added` class 拿掉，這樣就可以批次處理。
考量 corner case，可能需要忽略最後一筆，如果會議還在持續進行中。最後沒聲音的時候才全部取出來。
其次，觀察到 Live Caption 的 DOM 只會保留一定筆數。所以可能要在有物件被刪除時，觸發暫存的事件。

## 2025-07-09

```js
count = targetNode.querySelectorAll("div.newly-added").length - 1
transcript = targetNode.querySelectorAll("div.newly-added")
for (let i=0; i < count; i++) {
    authorElement = transcript[i].querySelector('[data-tid="author"]');
    Name = authorElement.innerText.trim();
    textElement = transcript[i].querySelector('[data-tid="closed-caption-text"]');
    Text = textElement.innerText.trim();
    Time = transcript[i].getAttribute('data-time');
    console.log({Time, Name, Text});
    transcript[i].classList.remove("newly-added");
}
```

## 2025-07-10

完成第一版 draft，可以正確產生上一筆（不再異動）的即時翻譯，並顯示在 `console.log()`

```js
// 1. Select the target node (the DOM subtree you want to observe)
const targetNode = document.querySelector("[data-tid='closed-caption-v2-window-wrapper']")
// 2. Configure the observer:
//    Set to true if you want to observe children of the targetNode as well.
//    Also set to true to observe when new nodes are added or removed.
const config = { childList: true, subtree: true };
// 3. define a function to handle newElement
function handleNewElement(element) {
    const timestamp = new Date().toISOString().replace('T', ' ').slice(0, -1);
    // Example: Add a class, attach an event listener, etc.
    element.classList.add('newly-added');
    element.setAttribute('data-time', timestamp);
}
function logTranscript() {
    count = targetNode.querySelectorAll("div.newly-added").length - 1
    transcript = targetNode.querySelectorAll("div.newly-added")
    for (let i=0; i < count; i++) {
        authorElement = transcript[i].querySelector('[data-tid="author"]');
        Name = authorElement.innerText.trim();
        textElement = transcript[i].querySelector('[data-tid="closed-caption-text"]');
        Text = textElement.innerText.trim();
        Time = transcript[i].getAttribute('data-time');
        console.log({Time, Name, Text});
        transcript[i].classList.remove("newly-added");
    }
}
// 4. Create a callback function to execute when mutations are observed
callback = function(mutationsList, observer) {
    for (const mutation of mutationsList) {
        if (mutation.type === 'childList') {
            // Check if nodes were added
            if (mutation.addedNodes.length > 0) {
                mutation.addedNodes.forEach(node => {
                    if (node.nodeType === Node.ELEMENT_NODE) { // Ensure it's an element
                        handleNewElement(node);
                        logTranscript();
                    }
                });
            }
        }
    }
};
// 5. Create an observer instance linked to the callback function
const observer = new MutationObserver(callback);
// 6. Start observing the target node for configured mutations
observer.observe(targetNode, config);
```

## 2025-08-15

- 微調 UI - 把 live caption 變小，方便
```diff
- <div data-tid="closed-caption-renderer-wrapper" aria-label="Live Captions">
+ <div data-tid="closed-caption-renderer-wrapper" aria-label="Live Captions" style="height: 100px;">
```

## 2025-10-16

- 近期使用上發現 MS Teams Live Caption 的行為又有一些變化，只能回捲短時間的歷史 Live Caption 即時字幕。
- 其次，也許觸發這段程式碼的時間點的關係，有時候會遇到 `transcriptItem.querySelector('[data-tid="author"]')` 是 null 的狀況。造成一直跳出 Error 累積了一堆 `newly-added` 的 DOM element 卻沒辦法靠 `logTranscript()` 函數寫到 DevTool Console.
- 有些改良的想法：
  - 學原本 `ms-teams-live-caption-saver` 的作法，把結果存在 `localStorage` 以免手誤太快關掉 DevTool，忘了另存成 log 純文字檔，就浪費了刻意打開
  - 參考 `Tactiq` 的實作，看能否把點選 `Live Caption` 的動作自動化，甚至可以參考如何查詢會議名稱，當作儲存 `localStorage` 的命名參考。

## 2026-05-13

- 紀錄一下改進的方向
  - 簡化 UI,
    - 移除：最上方有搜尋框的 Title Bar
    ```html
    <div data-tid="app-layout-area--title-bar">
    ```
    - 當有打開 Live Caption 時，會看到 Caption Renderer Wrapper，會想要把字幕區縮小，讓畫面分享等變大。
    ```html
    <div data-tid="closed-caption-renderer-wrapper">
    ```
    - 為了避免誤觸其他功能，我也會想要把左邊的 bar 移除。
    ```html
    <div data-tid="app-layout-area--nav">
    ```
  - 看能否註冊 onClose 或 onReload 的事件，提醒要先存檔
  - 如果能自動化關閉 notification 會有幫助專注在會議上
  - 想要自動取得會議名稱或會議連結，拿來做
  - 將 JSON 存到 Local Storage ，以免誤關視窗沒存到即時字幕
    - 如果想要做成更流暢的工作流（Workflow），是可以考慮存到其他位置集中管理。
  - 研究怎麼偵測上線人數（我是最後一個嗎？）

## 2026-05-28

<table><tr style="background-color:lightyellow;"><td>Q:</td><td>
how can I use JavaScript and Chrome DevTool to change heigh of div with data-tid="closed-caption-renderer-wrapper" to 50px?
</td></tr><tr style="background-color:lightgreen;"><td>Tool:</td><td>

- May 28 at 9:41 PM
- Google Gemini Apps
- Gemini 3.5 Flash | Thinking Level: Standard

</td></tr><tr><td>A:</td><td>
You can do this easily using the browser Console inside Chrome DevTools. Here is the quickest way to find that specific `div` and change its height to 50px.

### Step-by-Step Guide

1. **Open DevTools:** Right-click anywhere on the webpage and select **Inspect**, or press `F12` (`Cmd + Option + I` on Mac).
2. **Open the Console:** Click on the **Console** tab at the top of the DevTools panel.
3. **Run the Code:** Copy and paste the following JavaScript line into the console and press **Enter**:

```javascript
document.querySelector('div[data-tid="closed-caption-renderer-wrapper"]').style.height = "50px";
```

### How It Works

* `document.querySelector(...)`: This looks through the webpage's HTML to find the first element that matches the CSS selector you gave it.
* `div[data-tid="closed-caption-renderer-wrapper"]`: This is a specific CSS attribute selector. It tells the browser, *"Find a `div` that has an attribute named `data-tid` exactly equal to `closed-caption-renderer-wrapper`."*
* `.style.height = "50px"`: This directly modifies the element's inline CSS, forcing its height to become 50 pixels.

💡 **Quick Tip:** If the element's height doesn't seem to change, it might be overridden by other strict CSS rules (like a fixed `max-height`). If that happens, you can force it by adding `!important` using this alternative line:
```javascript
document.querySelector('div[data-tid="closed-caption-renderer-wrapper"]').style.setProperty('height', '50px', 'important');
```

</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
can I remove div with data-tid="app-layout-area--title-bar"?
</td></tr><tr><td>A:</td><td>
Yes, absolutely. You can completely remove that element from the webpage using a very similar approach in the Chrome DevTools Console.

Here is the JavaScript line to delete it:

```javascript
document.querySelector('div[data-tid="app-layout-area--title-bar"]').remove();
```

### How to do it:

1. Open your Chrome DevTools (**F12** or right-click -> **Inspect**).
2. Click on the **Console** tab.
3. Paste the code above and press **Enter**.

### What this does:

* `document.querySelector(...)` locates that specific title bar `div`.
* `.remove()` completely deletes the element from the current page's DOM (the HTML structure).

> ⚠️ **Note:** This change is temporary. It only affects your local view of the page. If you refresh or navigate away, the title bar will come right back!
</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
how can I make it invisible instead of remove it?
</td></tr><tr><td>A:</td><td>
If you want to hide the title bar without completely deleting it from the HTML structure, you have two great options. Making it invisible is often better because it keeps the page layout intact or allows you to bring it back easily later.

You can use either of these lines in your Chrome DevTools Console:

### Option 1: Hide it completely (Collapses the space)

This is usually what people want. It hides the element and sucks up the empty space it was occupying, as if it isn't there.

```javascript
document.querySelector('div[data-tid="app-layout-area--title-bar"]').style.display = 'none';
```

* **To undo this later without refreshing:** Change `'none'` to `''` (an empty string) or `'block'`.

### Option 2: Make it transparent (Keeps the space)

This makes the element completely invisible, but it still physically occupies space on the screen. The layout of the rest of the page won't shift.

```javascript
document.querySelector('div[data-tid="app-layout-area--title-bar"]').style.visibility = 'hidden';
```

* **To undo this later without refreshing:** Change `'hidden'` to `'visible'`.

### 💡 Pro Tip: How to "Toggle" it with a click

If you want an easy way to hide and unhide it while you are working on the page, you can paste this code into your console. It will hide it if it's visible, and show it if it's hidden:

```javascript
const titleBar = document.querySelector('div[data-tid="app-layout-area--title-bar"]');
if (titleBar) {
    titleBar.style.display = titleBar.style.display === 'none' ? '' : 'none';
}
```
</td></tr>
</table>

## 2026-06-24

- 在 DOM 中，有代表目前與會人數的區塊
```html
<span dir="auto" class="..." aria-hidden="true" data-tid="roster-button-tile" style="width: 2ch;">11</span>
```
- 在 DOM 中，結束會議的按鈕是
```html
<button type="button" 
        data-track-action-gesture="click" 
        data-track="true" 
        aria-keyshortcuts="Ctrl+Shift+H" 
        aria-label="Leave" 
        id="hangup-button"
        >
```
- 可能有機會拿來當自動關閉/結束會議的條件
