// 1. Select the target node (the DOM subtree you want to observe)
const targetNode = document.querySelector("[data-tid='closed-caption-v2-window-wrapper']");

if (!targetNode) {
    console.error("Error: Target node for closed captions not found. MutationObserver cannot be initialized.");
}
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
    const newlyAddedNodes = targetNode.querySelectorAll("div.newly-added");
    const count = newlyAddedNodes.length - 1;

    for (let i = 0; i < count; i++) {
        const transcriptItem = newlyAddedNodes[i];

        const authorElement = transcriptItem.querySelector('[data-tid="author"]');
        const Name = authorElement ? authorElement.innerText.trim() : "Unknown Author";

        const textElement = transcriptItem.querySelector('[data-tid="closed-caption-text"]');
        const Text = textElement ? textElement.innerText.trim() : "No Text Found";

        const Time = transcriptItem.getAttribute('data-time');

        console.log({Time, Name, Text});
        transcriptItem.classList.remove("newly-added");
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

// 6. Start observing the target node for configured mutations, only if targetNode was found
if (targetNode) {
    observer.observe(targetNode, config);
    console.warn("MutationObserver started for MS Teams live captions.");
} else {
    console.error("MutationObserver not started because the target node was not found.");
}
