# Reverse Engineering of MS Teams Meeting Live Caption Saver

> ### aider chat started at 2025-06-17 10:44:22
> You can skip this check with --no-gitignore  
> Add .aider* to .gitignore (recommended)? (Y)es/(N)o [Yes]: y  
> Added .aider* to .gitignore  
> C:\Users\jazzw\.local\bin\aider --model ollama/qwen25-coder-7b:q4_k_m --no-auto-commits --auto-lint Capture-Teams-Captrions - JSON.js  
> Aider v0.76.1.dev0+gc838f9bf.d20250509  
> Model: ollama/qwen25-coder-7b:q4_k_m with whole edit format  
> Git repo: ..\..\..\..\.git\modules\js\chrome-extensions\ms-teams-live-caption-saver with 26 files  
> Repo-map: using 4096.0 tokens, auto refresh  
> Added Standalone-scripts\Capture-Teams-Captrions - JSON.js to the chat.  
> Note: in-chat filenames are always relative to the git working dir, not the current working dir.  
> Cur working dir: C:\Users\jazzw\git\snippet\js\chrome-extensions\ms-teams-live-caption-saver\Standalone-scripts  
> Git working dir: C:\Users\jazzw\git\snippet\js\chrome-extensions\ms-teams-live-caption-saver  
>
> #### /model gemini/gemini-2.5-flash-preview-05-20  
> Aider v0.76.1.dev0+gc838f9bf.d20250509  
> Main model: gemini/gemini-2.5-flash-preview-05-20 with whole edit format  
> Weak model: ollama/qwen25-coder-7b:q4_k_m  
> Git repo: ..\..\..\..\.git\modules\js\chrome-extensions\ms-teams-live-caption-saver with 26 files  
> Repo-map: using 4096.0 tokens, auto refresh  
> Added Standalone-scripts\Capture-Teams-Captrions - JSON.js to the chat.  

> #### /ask could you explain the logic written in `Capture-Teams-Captrions - JSON.js`?  

The `Standalone-scripts\Capture-Teams-Captrions - JSON.js` script is designed to capture live captions from Microsoft Teams meetings and save them as a JSON file. It's a standalone script, likely intended to be run directly in the browser's developer console within a Teams meeting.

Here's a breakdown of its logic:

1.  **Initialization and Data Storage:**
    *   `localStorage.removeItem("transcripts");`: When the script starts, it first clears any previously stored captions in `localStorage` under the key "transcripts". This ensures a fresh capture session.
    *   `const transcriptArray = JSON.parse(localStorage.getItem("transcripts")) || [];`: It initializes an empty array `transcriptArray` (or loads existing data if, for some reason, `localStorage` wasn't cleared or the script was re-run without a full page reload). This array will hold all the captured caption objects.
    *   `let transcriptIdCounter = 0;`: A simple counter is used to generate unique IDs for captured captions, as the script notes that native Teams IDs are not reliable for this purpose.

2.  **`checkTranscripts()` Function - The Core Capture Logic:**
    *   **Locating Captions:**
        *   `const closedCaptionsContainer = document.querySelector("[data-tid='closed-captions-renderer']")`: It first tries to find the main container element for closed captions using a specific `data-tid` attribute, which is a common way Teams identifies its UI components.
        *   If this container isn't found, the function returns, implying that live captions are not active or the UI structure has changed.
        *   `const transcripts = closedCaptionsContainer.querySelectorAll('.fui-ChatMessageCompact');`: Once the container is found, it queries for individual caption items within it, using the class `.fui-ChatMessageCompact`.
    *   **Extracting Data:**
        *   It iterates through each found `transcript` element.
        *   `authorElement = transcript.querySelector('[data-tid="author"]')`: It extracts the speaker's name from an element with `data-tid="author"`.
        *   `textElement = transcript.querySelector('[data-tid="closed-caption-text"]')`: It extracts the caption text from an element with `data-tid="closed-caption-text"`.
        *   `Time = new Date().toISOString().replace('T', ' ').slice(0, -1);`: It generates a timestamp for when the caption was captured.
    *   **Duplicate Detection:**
        *   `const recentTranscripts = transcriptArray.slice(-10);`: To avoid capturing the same caption multiple times (which can happen with DOM mutations), it checks only the last 10 entries in `transcriptArray`.
        *   `const isDuplicate = recentTranscripts.some(t => t.Name === Name && t.Text === Text);`: It marks a caption as a duplicate if both the `Name` and `Text` match any of the recent entries. This is a pragmatic approach given the lack of reliable native IDs.
    *   **Storing New Captions:**
        *   `if (!isDuplicate && Text.length > 0)`: If the caption is not a duplicate and has actual text content, it's considered new.
        *   `const ID = `caption_${transcriptIdCounter++}`;`: A unique ID is assigned.
        *   `transcriptArray.push({ Name, Text, Time, ID });`: The new caption object is added to the `transcriptArray`.
    *   **Persisting Data:**
        *   `localStorage.setItem('transcripts', JSON.stringify(transcriptArray));`: After processing all current captions, the entire `transcriptArray` is saved back to `localStorage` as a JSON string.

3.  **Monitoring for Changes (MutationObserver & Interval):**
    *   **MutationObserver:**
        *   `const observer = new MutationObserver(checkTranscripts);`: A `MutationObserver` is set up to call `checkTranscripts` whenever changes occur in the DOM.
        *   `if (captionsContainer) { observer.observe(captionsContainer, { childList: true, subtree: true, characterData: true }); }`: If the specific captions container is found, the observer focuses on it, watching for additions/removals of child nodes (`childList`), changes within its descendants (`subtree`), and changes to text content (`characterData`). This is the primary mechanism for real-time caption capture.
        *   `else { observer.observe(document.body, { childList: true, subtree: true }); }`: As a fallback, if the specific container isn't immediately available, it observes the entire `document.body`. This is less efficient but ensures some level of monitoring.
    *   **Initial Check & Interval:**
        *   `checkTranscripts();`: The `checkTranscripts` function is called immediately when the script runs to capture any captions already present.
        *   `setInterval(checkTranscripts, 10000);`: A `setInterval` is also used to call `checkTranscripts` every 10 seconds. This acts as a safeguard in case the `MutationObserver` somehow misses an event or if captions are updated in a way that doesn't trigger the observer (e.g., if the entire container is re-rendered).

4.  **`downloadJSON()` Function - Exporting Data:**
    *   **Retrieving Data:**
        *   `let transcripts = JSON.parse(localStorage.getItem('transcripts'));`: It retrieves the captured captions from `localStorage`.
        *   It checks if any captions were captured; if not, it alerts the user.
    *   **Data Transformation:**
        *   `transcripts = transcripts.map(({ ID, ...rest }) => rest);`: Before saving, it removes the internally generated `ID` property from each caption object, as these IDs are only for internal tracking and not relevant for the final output.
        *   `const prettyTranscripts = JSON.stringify(transcripts, null, 2);`: The array of caption objects is converted into a human-readable JSON string with 2-space indentation.
    *   **Filename Generation:**
        *   `let title = document.title.replace("__Microsoft_Teams", '').replace(/[^a-z0-9 ]/gi, '');`: It attempts to create a clean filename using the current page's title, removing "Microsoft_Teams" and non-alphanumeric characters.
        *   `const fileName = "transcript - " + title.trim() + ".json";`: The final filename is constructed.
    *   **Download Mechanism:**
        *   It creates a data URL (`text/json;charset=utf-8,...`) containing the JSON string.
        *   It dynamically creates an `<a>` (anchor) HTML element, sets its `href` to the data URL and its `download` attribute to the generated filename.
        *   `document.body.appendChild(downloadAnchorNode);` (required for Firefox) and `downloadAnchorNode.click();` simulate a click on this hidden link, triggering the browser's download prompt.
        *   `downloadAnchorNode.remove();`: The temporary link element is then removed from the DOM.

5.  **Console Messages:**
    *   The script provides helpful messages in the browser's developer console, indicating that it's running and how to manually trigger the download function (`downloadJSON()`).

In essence, this script acts as a "caption logger" for Microsoft Teams, continuously monitoring the DOM for new caption text, storing it locally, and providing a way to export the collected data as a structured JSON file.

> #### /ask translate the explanation into traditional chinese, thanks.    

`Standalone-scripts\Capture-Teams-Captrions - JSON.js` 腳本旨在擷取 Microsoft Teams 會議中的即時字幕，並將其儲存為 JSON 檔案。這是一個獨立的腳本，可能旨在直接在 Teams 會議中的瀏覽器開發者控制台中執行。

以下是其邏輯的詳細說明：

1.  **初始化與資料儲存：**
    *   `localStorage.removeItem("transcripts");`：當腳本啟動時，它首先清除 `localStorage` 中鍵為 "transcripts" 的任何先前儲存的字幕。這確保了新的擷取會話。
    *   `const transcriptArray = JSON.parse(localStorage.getItem("transcripts")) || [];`：它初始化一個空的陣列 `transcriptArray`（或者如果 `localStorage` 未被清除或腳本在沒有完全重新載入頁面的情況下重新執行，則載入現有資料）。這個陣列將儲存所有擷取到的字幕物件。
    *   `let transcriptIdCounter = 0;`：一個簡單的計數器用於為擷取到的字幕生成唯一的 ID，因為腳本指出 Teams 的原生 ID 不可靠。

2.  **`checkTranscripts()` 函數 - 核心擷取邏輯：**
    *   **定位字幕：**
        *   `const closedCaptionsContainer = document.querySelector("[data-tid='closed-captions-renderer']")`：它首先嘗試使用特定的 `data-tid` 屬性找到閉路字幕的主要容器元素，這是 Teams 識別其 UI 組件的常用方式。
        *   如果找不到此容器，函數將返回，表示即時字幕未啟用或 UI 結構已更改。
        *   `const transcripts = closedCaptionsContainer.querySelectorAll('.fui-ChatMessageCompact');`：一旦找到容器，它會查詢其中的個別字幕項目，使用類別 `.fui-ChatMessageCompact`。
    *   **提取資料：**
        *   它遍歷每個找到的 `transcript` 元素。
        *   `authorElement = transcript.querySelector('[data-tid="author"]')`：它從具有 `data-tid="author"` 的元素中提取說話者的姓名。
        *   `textElement = transcript.querySelector('[data-tid="closed-caption-text"]')`：它從具有 `data-tid="closed-caption-text"` 的元素中提取字幕文本。
        *   `Time = new Date().toISOString().replace('T', ' ').slice(0, -1);`：它生成字幕擷取時的時間戳。
    *   **重複檢測：**
        *   `const recentTranscripts = transcriptArray.slice(-10);`：為避免多次擷取相同的字幕（這可能發生在 DOM 變動時），它只檢查 `transcriptArray` 中最後 10 個條目。
        *   `const isDuplicate = recentTranscripts.some(t => t.Name === Name && t.Text === Text);`：如果 `Name` 和 `Text` 都與最近的任何條目匹配，則將字幕標記為重複。考慮到缺乏可靠的原生 ID，這是一種實用的方法。
    *   **儲存新字幕：**
        *   `if (!isDuplicate && Text.length > 0)`：如果字幕不是重複的且具有實際文本內容，則將其視為新字幕。
        *   `const ID = `caption_${transcriptIdCounter++}`;`：分配一個唯一的 ID。
        *   `transcriptArray.push({ Name, Text, Time, ID });`：新的字幕物件被添加到 `transcriptArray` 中。
    *   **持久化資料：**
        *   `localStorage.setItem('transcripts', JSON.stringify(transcriptArray));`：處理完所有當前字幕後，整個 `transcriptArray` 會以 JSON 字串的形式儲存回 `localStorage`。

3.  **監控變更（MutationObserver 和 Interval）：**
    *   **MutationObserver：**
        *   `const observer = new MutationObserver(checkTranscripts);`：設置一個 `MutationObserver`，以便在 DOM 發生變化時呼叫 `checkTranscripts`。
        *   `if (captionsContainer) { observer.observe(captionsContainer, { childList: true, subtree: true, characterData: true }); }`：如果找到特定的字幕容器，觀察者會將焦點放在其上，監控其子節點的添加/刪除 (`childList`)、其後代內部的變化 (`subtree`) 以及文本內容的變化 (`characterData`)。這是即時字幕擷取的主要機制。
        *   `else { observer.observe(document.body, { childList: true, subtree: true }); }`：作為備用方案，如果特定的容器沒有立即可用，它會觀察整個 `document.body`。這效率較低，但確保了某種程度的監控。
    *   **初始檢查和間隔：**
        *   `checkTranscripts();`：腳本運行時立即呼叫 `checkTranscripts` 函數，以擷取任何已存在的字幕。
        *   `setInterval(checkTranscripts, 10000);`：還使用 `setInterval` 每 10 秒呼叫一次 `checkTranscripts`。這作為一種保障，以防 `MutationObserver` 遺漏了事件，或者字幕以不觸發觀察者的方式更新（例如，如果整個容器被重新渲染）。

4.  **`downloadJSON()` 函數 - 匯出資料：**
    *   **檢索資料：**
        *   `let transcripts = JSON.parse(localStorage.getItem('transcripts'));`：它從 `localStorage` 中檢索擷取到的字幕。
        *   它檢查是否擷取到任何字幕；如果沒有，則會提醒用戶。
    *   **資料轉換：**
        *   `transcripts = transcripts.map(({ ID, ...rest }) => rest);`：在儲存之前，它從每個字幕物件中刪除內部生成的 `ID` 屬性，因為這些 ID 僅用於內部追蹤，與最終輸出無關。
        *   `const prettyTranscripts = JSON.stringify(transcripts, null, 2);`：字幕物件陣列被轉換為帶有 2 個空格縮排的人類可讀 JSON 字串。
    *   **檔案名稱生成：**
        *   `let title = document.title.replace("__Microsoft_Teams", '').replace(/[^a-z0-9 ]/gi, '');`：它嘗試使用當前頁面的標題創建一個乾淨的檔案名稱，刪除 "Microsoft_Teams" 和非字母數字字符。
        *   `const fileName = "transcript - " + title.trim() + ".json";`：構建最終的檔案名稱。
    *   **下載機制：**
        *   它創建一個包含 JSON 字串的資料 URL (`text/json;charset=utf-8,...`)。
        *   它動態創建一個 `<a>`（錨點）HTML 元素，將其 `href` 設置為資料 URL，並將其 `download` 屬性設置為生成的檔案名稱。
        *   `document.body.appendChild(downloadAnchorNode);`（Firefox 需要）和 `downloadAnchorNode.click();` 模擬點擊此隱藏連結，觸發瀏覽器的下載提示。
        *   `downloadAnchorNode.remove();`：然後從 DOM 中刪除臨時連結元素。

5.  **控制台訊息：**
    *   腳本在瀏覽器的開發者控制台中提供有用的訊息，指示其正在運行以及如何手動觸發下載函數 (`downloadJSON()`)。

總之，這個腳本充當 Microsoft Teams 的「字幕記錄器」，持續監控 DOM 以獲取新的字幕文本，將其本地儲存，並提供一種將收集到的資料匯出為結構化 JSON 檔案的方法。

> #### /ask could you draw a sequence diagram of `Capture-Teams-Captrions - JSON.js` using mermaid.js syntax? try to capture detail if possible.  

```mermaid
sequenceDiagram
    participant User
    participant Script as Capture-Teams-Captions-JSON.js
    participant BrowserDOM as Browser DOM
    participant LocalStorage as localStorage

    User->>Script: Load script (e.g., paste into browser console)

    activate Script
    Note over Script: Script Initialization
    Script->>LocalStorage: Clear "transcripts" (localStorage.removeItem)
    Script->>Script: Initialize transcriptArray = [] (from localStorage or empty)
    Script->>Script: Initialize transcriptIdCounter = 0

    Script->>Script: Call checkTranscripts() (initial run)
    activate Script
    Script->>BrowserDOM: Query for closed captions container ([data-tid='closed-captions-renderer'])
    alt Captions Container Found
        BrowserDOM-->>Script: Returns container element
        Script->>BrowserDOM: Query for individual caption items (.fui-ChatMessageCompact)
        BrowserDOM-->>Script: Returns list of caption elements
        loop For each caption element found
            Script->>BrowserDOM: Extract Author Name ([data-tid="author"])
            Script->>BrowserDOM: Extract Caption Text ([data-tid="closed-caption-text"])
            Script->>Script: Generate current Time (ISO string)
            Script->>Script: Check last 10 entries in transcriptArray for duplicates (Name + Text)
            alt Not a duplicate AND Text is not empty
                Script->>Script: Generate unique ID (caption_counter++)
                Script->>Script: Add {Name, Text, Time, ID} to transcriptArray
                Script->>User: Log captured caption to console
            end
        end
        Script->>LocalStorage: Save JSON.stringify(transcriptArray)
    else Captions Container Not Found
        Script-->>Script: Return (no captions to process)
    end
    deactivate Script

    Note over Script: Setup Continuous Monitoring
    Script->>BrowserDOM: Observe closed captions container (MutationObserver: childList, subtree, characterData)
    alt Fallback if container not found initially
        Script->>BrowserDOM: Observe document.body (MutationObserver: childList, subtree)
    end
    Script->>Script: Set setInterval(checkTranscripts, 10000ms)
    Script->>User: Log "Teams Caption Capture (JSON) is running!" to console
    Script->>User: Log "To download captured captions, run: downloadJSON()" to console

    loop Continuous Monitoring (triggered by MutationObserver or setInterval)
        BrowserDOM->>Script: DOM changes (e.g., new caption appears)
        activate Script
        Script->>Script: checkTranscripts() triggered
        Script->>BrowserDOM: Query for closed captions container
        alt Captions Container Found
            BrowserDOM-->>Script: Returns container element
            Script->>BrowserDOM: Query for individual caption items
            BrowserDOM-->>Script: Returns list of caption elements
            loop For each new/updated caption element
                Script->>BrowserDOM: Extract Author Name, Caption Text
                Script->>Script: Generate current Time
                Script->>Script: Check transcriptArray for duplicates
                alt Not a duplicate AND Text is not empty
                    Script->>Script: Add new caption to transcriptArray
                end
            end
            Script->>LocalStorage: Save JSON.stringify(transcriptArray)
        else Captions Container Not Found
            Script-->>Script: Return
        end
        deactivate Script
    end

    User->>Script: Call downloadJSON() (e.g., from console)
    activate Script
    Script->>LocalStorage: Get "transcripts"
    LocalStorage-->>Script: Returns JSON string
    Script->>Script: Parse JSON string to array
    alt No captions captured
        Script->>User: Alert "No captions captured yet..."
        deactivate Script
    end
    Script->>Script: Map array to remove 'ID' property from each object
    Script->>Script: Stringify array to pretty-printed JSON (JSON.stringify(..., null, 2))
    Script->>BrowserDOM: Get document.title
    BrowserDOM-->>Script: Returns page title
    Script->>Script: Generate clean filename (e.g., "transcript - MeetingTitle.json")
    Script->>Script: Create data URL
    Script->>BrowserDOM: Create temporary <a> element
    Script->>BrowserDOM: Set <a>.href = data URL, <a>.download = filename
    Script->>BrowserDOM: Append <a> to document.body
    Script->>BrowserDOM: Simulate click on <a>
    BrowserDOM->>User: Initiate file download (e.g., "transcript - MyMeeting.json")
    Script->>BrowserDOM: Remove <a> element from document.body
    deactivate Script
```

> #### /ask are those transcript from DOM duplicated based on the logic?  

No, the script's logic is specifically designed to **prevent** duplicate entries from the DOM being added to its internal `transcriptArray` for most common scenarios.

Here's how it works:

1.  **Internal Storage:** The script maintains a `transcriptArray` in `localStorage` which stores all the captions it has *already captured and processed*.

2.  **Duplicate Check Logic:**
    *   When `checkTranscripts()` runs, it iterates through the caption elements *currently present in the DOM*.
    *   For each DOM caption, it extracts the `Name` (speaker) and `Text` (caption content).
    *   It then performs a duplicate check against the `transcriptArray`:
        ```javascript
        const recentTranscripts = transcriptArray.slice(-10); // Check last 10 entries
        const isDuplicate = recentTranscripts.some(t =>
            t.Name === Name && t.Text === Text
        );
        ```
    *   This means it looks at the **last 10 entries** that were *already added* to `transcriptArray`. If the current `Name` and `Text` from the DOM element match any of these recent entries, it considers it a duplicate.

3.  **Conditional Addition:**
    *   `if (!isDuplicate && Text.length > 0)`: Only if the extracted caption is **not** found as a duplicate in the `recentTranscripts` and has actual text content, will it be added to the `transcriptArray`.

**Potential Edge Case for Duplication:**

While effective for preventing immediate or near-immediate duplicates (which often occur due to DOM re-renders or slight updates), there's a theoretical edge case:

*   If the **exact same phrase from the exact same speaker** appears, then more than 10 *other unique captions* are spoken, and then the original phrase is repeated, the script *would* add it again. This is because the original instance of that phrase would have "fallen out" of the `recentTranscripts.slice(-10)` window, making the new instance appear as non-duplicate.

However, for the typical flow of a conversation where captions are continuously added, this `slice(-10)` heuristic is generally sufficient to prevent redundant entries caused by the dynamic nature of the Teams DOM. The primary goal is to capture *new* distinct caption events, not necessarily to ensure absolute uniqueness across an entire, potentially very long, transcript if the same exact phrase is repeated much later.

> Tokens: 7.1k sent, 516 received. Cost: $0.0014 message, $0.0062 session.  
