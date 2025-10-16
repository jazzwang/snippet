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
- <div class="fui-Flex ___1xriypo f22iagw f1vx9l62 fprs0cq f419p8h for4qjf fgmr9yd f12xb3oj f1yj8dow f1nkf6f4 f1h3a8gf f1g31g83 fyxfkj9" data-tid="closed-caption-renderer-wrapper" aria-label="Live Captions">
+ <div class="fui-Flex ___1xriypo f22iagw f1vx9l62 fprs0cq f419p8h for4qjf fgmr9yd f12xb3oj f1yj8dow f1nkf6f4 f1h3a8gf f1g31g83 fyxfkj9" data-tid="closed-caption-renderer-wrapper" aria-label="Live Captions" style="height: 100px;">
```

## 2025-10-16

- 近期使用上發現 MS Teams Live Caption 的行為又有一些變化，只能回捲短時間的歷史 Live Caption 即時字幕。
- 其次，也許觸發這段程式碼的時間點的關係，有時候會遇到 `transcriptItem.querySelector('[data-tid="author"]')` 是 null 的狀況。造成一直跳出 Error 累積了一堆 `newly-added` 的 DOM element 卻沒辦法靠 `logTranscript()` 函數寫到 DevTool Console.
- 有些改良的想法：
  - 學原本 `ms-teams-live-caption-saver` 的作法，把結果存在 `localStorage` 以免手誤太快關掉 DevTool，忘了另存成 log 純文字檔，就浪費了刻意打開
  - 參考 `Tactiq` 的實作，看能否把點選 `Live Caption` 的動作自動化，甚至可以參考如何查詢會議名稱，當作儲存 `localStorage` 的命名參考。