# test MutationObserver() and setInterval()

- https://g.co/gemini/share/0560f79f0706
- Created with 2.5 Flash June 19, 2025 at 01:41 PM
Published July 4, 2025 at 12:38 AM

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
could you give me a step-by-step instruction to write a small project and test MutationObserver() and setInterval() using Chrome DevTool?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
I can certainly help you with that! We'll create a simple HTML page with some JavaScript that uses both `MutationObserver` and `setInterval`. Then, I'll guide you through testing them in Chrome DevTools.

Here's the HTML and JavaScript code for your project:

### Step-by-Step Instructions to Test in Chrome DevTools:

1.  **Save the Code:**

    -   Copy the entire code block above (from `<!DOCTYPE html>` to `</html>`).

    -   Open a plain text editor (like Notepad, VS Code, Sublime Text, etc.).

    -   Paste the code into the editor.

    -   Save the file as `mutation_interval_test.html` (or any name ending with `.html`).

2.  **Open the HTML File in Chrome:**

    -   Locate the saved `mutation_interval_test.html` file on your computer.

    -   Double-click the file. It should open automatically in your Chrome browser.

3.  **Open Chrome DevTools:**

    -   Once the page is loaded in Chrome, right-click anywhere on the page.

    -   Select "Inspect" from the context menu.

    -   Alternatively, you can press `F12` (on Windows/Linux) or `Cmd + Option + I` (on macOS).

4.  **Navigate to the Console Tab:**

    -   In the DevTools window, make sure you are on the **"Console"** tab. This is where you'll see all the `console.log` messages from our JavaScript code.

5.  **Observe `setInterval` in Action:**

    -   As soon as the page loads, you'll see messages like "setInterval started..." in the console.

    -   Every 3 seconds, you'll see a new message: "setInterval: Content automatically updated to..."

    -   You'll also notice the text inside the dashed box on the web page changing automatically.

6.  **Observe `MutationObserver` in Action:**

    -   Alongside the `setInterval` messages, you'll also see "DOM Mutation Detected!" messages. These are coming from your `MutationObserver`.

    -   Click on the arrow next to "DOM Mutation Detected!" to expand the group and see the details of the mutation (e.g., `characterData` change for text, `attributes` change for `data-update-count`).

    -   When you click the "Manually Change Content" button, you'll see another "DOM Mutation Detected!" log, indicating that the observer caught your manual change.

7.  **Manually Stop `setInterval` using DevTools Console:**

    -   In the **Console** tab, type `clearInterval(autoChangeIntervalId);` and press Enter.

    -   You should see `undefined` as the output (meaning the command executed).

    -   Go back to the web page. The automatic content changes should now stop.

    -   **Explanation:** We stored the ID returned by `setInterval` in the global variable `autoChangeIntervalId`. By typing this command in the console, you're directly interacting with the running JavaScript environment of the page and telling it to stop that specific interval.

8.  **Manually Disconnect `MutationObserver` using DevTools Console:**

    -   In the **Console** tab, type `domObserver.disconnect();` and press Enter.

    -   Again, you'll see `undefined` as the output.

    -   Now, try clicking the "Manually Change Content" button on the web page, or if `setInterval` is still running, let it run.

    -   **Observation:** You will *not* see any new "DOM Mutation Detected!" messages in the console.

    -   **Explanation:** By calling `disconnect()` on the `domObserver` instance, you've told it to stop listening for any further DOM changes.

9.  **Experiment with the Buttons:**

    -   Use the "Stop Auto Changes (setInterval)" button to stop the `setInterval` via the UI.

    -   Use the "Disconnect Observer" button to stop the `MutationObserver` via the UI.

    -   You can refresh the page (`F5` or `Cmd + R`) to reset everything and start over.

This exercise provides a hands-on way to see how `MutationObserver` and `setInterval` work, how they interact, and how you can control them both programmatically and directly from the Chrome DevTools console.
</td></tr></table>