# Improvement Idea to export MS Teams Live Caption

## 2025-06-19

- https://g.co/gemini/share/a8a7452803ee
- Created with 2.5 Flash June 19, 2025 at 10:46 PM

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
Is it possible to call a function when DOM subtree added new element?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Yes, it's absolutely possible to call a function when a new element is added to a DOM subtree. The primary way to achieve this in modern JavaScript is by using the **MutationObserver API**.

The `MutationObserver` provides a way to react to changes in the DOM. It's much more efficient and robust than older methods like polling or using deprecated `DOMNodeInserted` events.

Here's how you can use it:

```javascript
// 1. Select the target node (the DOM subtree you want to observe)
const targetNode = document.getElementById('myContainer'); // Or document.body, etc.

// 2. Configure the observer:
//    Set to true if you want to observe children of the targetNode as well.
//    Also set to true to observe when new nodes are added or removed.
const config = { childList: true, subtree: true };

// 3. Create a callback function to execute when mutations are observed
const callback = function(mutationsList, observer) {
    for (const mutation of mutationsList) {
        if (mutation.type === 'childList') {
            // Check if nodes were added
            if (mutation.addedNodes.length > 0) {
                console.log('A child node has been added to the DOM subtree!');
                console.log('Added nodes:', mutation.addedNodes);

                // You can iterate over addedNodes to work with the new elements
                mutation.addedNodes.forEach(node => {
                    if (node.nodeType === Node.ELEMENT_NODE) { // Ensure it's an element
                        console.log('New element added:', node);
                        // Call your specific function here
                        handleNewElement(node);
                    }
                });
            }

            // You can also check for removed nodes if needed
            // if (mutation.removedNodes.length > 0) {
            //     console.log('A child node has been removed from the DOM subtree!');
            //     console.log('Removed nodes:', mutation.removedNodes);
            // }
        }
        // You can add more checks for other mutation types if configured
        // else if (mutation.type === 'attributes') { ... }
        // else if (mutation.type === 'characterData') { ... }
    }
};

// 4. Create an observer instance linked to the callback function
const observer = new MutationObserver(callback);

// 5. Start observing the target node for configured mutations
observer.observe(targetNode, config);

// --- Your custom function to handle new elements ---
function handleNewElement(element) {
    console.log('Custom function called for new element:', element.tagName);
    // Example: Add a class, attach an event listener, etc.
    element.classList.add('newly-added');
}

// --- Example of adding elements to trigger the observer ---
document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('myContainer');

    // Add an element after a short delay
    setTimeout(() => {
        const newDiv = document.createElement('div');
        newDiv.textContent = 'I am a new div!';
        container.appendChild(newDiv);
        console.log('--- Appended newDiv ---');

        // Add another element inside a newly created element
        setTimeout(() => {
            const innerSpan = document.createElement('span');
            innerSpan.textContent = 'I am an inner span!';
            newDiv.appendChild(innerSpan);
            console.log('--- Appended innerSpan ---');
        }, 1000);

        // Add an element to a different part of the DOM not observed by this observer
        // This will NOT trigger the observer if not within 'myContainer'
        const bodyDiv = document.createElement('div');
        bodyDiv.textContent = 'I am a body div!';
        document.body.appendChild(bodyDiv);
        console.log('--- Appended bodyDiv (outside observed target) ---');


    }, 2000);

    // Add an element directly to the body (will not trigger if targetNode is 'myContainer')
    setTimeout(() => {
        const anotherDiv = document.createElement('div');
        anotherDiv.textContent = 'Another div in the body.';
        document.body.appendChild(anotherDiv);
        console.log('--- Appended anotherDiv directly to body ---');
    }, 4000);
});

// To stop observing later if needed:
// observer.disconnect();
```

**Explanation:**

1.  **`targetNode`**: This is the DOM element you want to watch for changes within. If you want to watch the entire document, you can use `document.body` or `document.documentElement`.
2.  **`config`**: This object specifies which types of mutations the observer should react to.
    * `childList: true`: This is crucial. It tells the observer to report when child nodes are added or removed.
    * `subtree: true`: This means the observer will not only watch the immediate children of `targetNode` but also all their descendants. This is what makes it observe a "DOM subtree."
    * You can also include `attributes: true` (to observe attribute changes on the target node and its descendants) or `characterData: true` (to observe changes to text content).
3.  **`callback` Function**: This function is executed every time a mutation matching your `config` occurs.
    * It receives `mutationsList` (an array of `MutationRecord` objects) and the `observer` instance itself.
    * Each `MutationRecord` object contains details about a single change (e.g., `type`, `target`, `addedNodes`, `removedNodes`, `attributeName`, etc.).
    * You iterate through `mutationsList` and check the `type` to identify what kind of mutation occurred. For new elements, you're primarily interested in `mutation.type === 'childList'` and then checking `mutation.addedNodes`.
4.  **`MutationObserver(callback)`**: This creates a new observer instance, passing your callback function.
5.  **`observer.observe(targetNode, config)`**: This starts the observation process. The observer will now listen for changes on `targetNode` according to the `config`.
6.  **`handleNewElement(element)`**: This is your custom function that gets called for each newly added element. You can put any logic here that you want to execute when a new element appears.

**When to Use `MutationObserver`:**

* **Dynamically loaded content:** When content is loaded via AJAX or inserted by third-party scripts.
* **Single-page applications (SPAs):** Where large parts of the DOM are frequently manipulated.
* **Integrating with external libraries:** When you need to react to changes made by a library you don't control.
* **Performance monitoring:** Tracking when elements are added or removed for performance analysis.

This `MutationObserver` API is the recommended and most performant way to detect and react to DOM subtree additions.
</td></tr></table>

- 想法：根據 [ms-teams-live-caption-saver.md](./ms-teams-live-caption-saver.md) 的逆向工程，其實可以把邏輯做一些修改：
  1. 觀察新 append 的 DOM
  2. 有新 append 事件發生時，產生一個 Time stamp
  3. 將上一個 append 的 Live Caption 內容存到 `Local Storage`，並加入上一次事件的 Time stamp。
- 這樣就不用產生自己的 tag ID，也不用想辦法去除重複的 Live Caption (因為 Live Caption 偶爾會隨著後續的發言而修正即時轉譯的詞彙)
- 根據日常的觀察，偶爾 Live Caption 會修改前一兩行的翻譯（可能基於後面發言的內容發現前面有翻錯），所以可能也要註冊觀察 DOM modified 事件，但這個事件可能會同步抓到正在轉譯的那一行，所以先實驗用 append 的結果準確度好不好，再評估是否要額外觀測 modified 事件。