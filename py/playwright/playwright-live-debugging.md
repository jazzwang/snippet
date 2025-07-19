# Playwright Live Debugging

## 2025-07-18

- July 18 at 1:42 PM - Gemini 2.5 Flash 

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
could you give me a playwright Python live debugging example using VS Code?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Live debugging Playwright with Python in VS Code is a powerful way to understand and fix issues in your automation scripts. Here's a comprehensive example and guide:

**Prerequisites:**

1.  **Python Installed:** Make sure you have Python installed on your system.
2.  **VS Code Installed:** Download and install Visual Studio Code.
3.  **Playwright Python Library:**
    ```bash
    pip install playwright
    playwright install
    ```
4.  **VS Code Extensions:**
      * **Python extension:** (Microsoft) Essential for Python debugging.
      * **Playwright Test for VSCode extension:** (Microsoft) This extension greatly enhances the experience by providing test explorer integration, direct debug options, and the Playwright Inspector.

**Example Scenario: Debugging a simple login test**

Let's imagine you have a test file `test_login.py` that tries to log into a website.

**1. Project Setup:**

Create a new folder for your project (e.g., `playwright_debug_example`).
Inside this folder, create a file named `test_login.py`:

```python
# test_login.py
import pytest
from playwright.sync_api import Page, expect

def test_successful_login(page: Page):
    page.goto("https://www.example.com/login") # Replace with a real login page URL if you have one

    # Fill in username and password
    page.locator("#username").fill("myuser")
    page.locator("#password").fill("mypassword")

    # Click the login button
    page.locator("#login-button").click()

    # Assert that we are on the dashboard or a success page
    expect(page).to_have_url("https://www.example.com/dashboard") # Replace with your success URL
    expect(page.locator("h1")).to_have_text("Welcome to Dashboard") # Replace with a success message element
```

**Important:** For a real example, replace `"https://www.example.com/login"` and `"https://www.example.com/dashboard"` with actual URLs of a login page and a successful login destination. Similarly, replace `#username`, `#password`, `#login-button`, and `h1` with the correct CSS selectors for your target website.

**2. Setting a Breakpoint:**

Open `test_login.py` in VS Code. To set a breakpoint, click in the gutter (the space to the left of the line numbers) next to the line of code where you want the execution to pause. A red dot will appear, indicating a breakpoint.

For instance, you might set a breakpoint on the line:
`page.locator("#login-button").click()`

**3. Debugging Options in VS Code:**

With the Playwright Test for VSCode extension installed, you have a few convenient ways to debug:

  * **Using the Testing Sidebar:**

    1.  Click on the Test Icon in the VS Code Activity Bar (the icon that looks like a beaker).
    2.  You should see your `test_login.py` file listed under "Tests". Expand it to see `test_successful_login`.
    3.  Hover over `test_successful_login` and click the **green play button with a bug icon** (Run Test with Debugger). This is the easiest way.

  * **From the Editor:**

    1.  Open `test_login.py`.
    2.  Right-click next to the `def test_successful_login(page: Page):` line.
    3.  Select "Debug Test".

  * **Adding `page.pause()`:**
    For more controlled pauses, especially when you want to interact with the browser during debugging, you can add `page.pause()` directly in your test code:

    ```python
    # test_login.py
    import pytest
    from playwright.sync_api import Page, expect

    def test_successful_login(page: Page):
        page.goto("https://www.example.com/login")

        page.locator("#username").fill("myuser")
        page.locator("#password").fill("mypassword")

        # Pause execution here to inspect the page or try locators
        page.pause() # <--- Add this line for an intentional pause

        page.locator("#login-button").click()

        expect(page).to_have_url("https://www.example.com/dashboard")
        expect(page.locator("h1")).to_have_text("Welcome to Dashboard")
    ```

    When you run a test with `page.pause()` in debug mode, it will open the Playwright Inspector, allowing you to interact with the browser, pick locators, and then resume execution.

**4. The Debugging Experience:**

When you start debugging:

  * **Browser Window:** A browser window will open (in headed mode by default during debugging).
  * **Playwright Inspector:** The Playwright Inspector window will often pop up. This is a powerful tool that shows you:
      * **Action Log:** A step-by-step log of Playwright actions.
      * **Pick Locator:** A tool to select elements in the browser and automatically generate locators.
      * **Live Edit Locators:** You can modify locators in the Inspector and see them highlight in the browser in real-time.
  * **VS Code Debug Controls:**
      * The execution will pause at your breakpoint (or at `page.pause()`).
      * The **Debug Toolbar** will appear at the top of VS Code with controls like:
          * **Continue (F5):** Resume execution until the next breakpoint or end of the script.
          * **Step Over (F10):** Execute the current line and move to the next line of code, stepping over function calls.
          * **Step Into (F11):** Step into a function call to debug its internal logic.
          * **Step Out (Shift+F11):** Step out of the current function and continue execution.
          * **Restart (Ctrl+Shift+F5):** Restart the debugging session.
          * **Stop (Shift+F5):** Terminate the debugging session.
  * **VS Code Debug Panels:**
      * **Variables:** Inspect the values of variables in the current scope.
      * **Watch:** Add expressions to watch their values as the code executes.
      * **Call Stack:** See the sequence of function calls that led to the current point.
      * **Breakpoints:** Manage your breakpoints (add, remove, enable/disable).
      * **Debug Console:** Interact with your Python code directly, execute commands, and view `print()` statements.

**5. Interacting During Debugging:**

  * **Stepping Through Code:** Use "Step Over" to move through your Playwright actions line by line.
  * **Inspecting Elements:** While paused at a breakpoint, you can go to the browser window opened by Playwright. Use the "Pick Locator" tool in the Playwright Inspector to click on elements and get their locators. You can copy these and paste them into your code.
  * **Live Editing Locators:** If you're debugging a locator issue, you can edit the locator in the Playwright Inspector's "Pick Locator" field and see the elements highlighted in the browser in real-time, helping you find the correct locator.
  * **Using `PWDEBUG=1` (Alternative for general debugging/Inspector):**
    You can also launch your tests with the `PWDEBUG=1` environment variable. This will open the browser in headed mode and launch the Playwright Inspector.
    In your terminal:
    ```bash
    set PWDEBUG=1 # Windows
    export PWDEBUG=1 # macOS/Linux
    pytest -s test_login.py
    ```
    While `PWDEBUG=1` is useful, the VS Code extension's direct "Debug Test" option usually provides a more integrated experience with breakpoints.

**Troubleshooting:**

  * **Breakpoints not hit:**
      * Ensure you have the Python extension installed.
      * Make sure your `launch.json` (if you have one) is correctly configured for Python debugging (though the Playwright extension often handles this automatically for tests).
      * If using `pytest-cov`, try adding `"env": {"PYTEST_ADDOPTS": "--no-cov"}` to your debug configuration in `launch.json` or disable `pytest-cov` during debugging.
  * **Browser not opening:**
      * Ensure the "Show Browser" option is checked in the Playwright sidebar in VS Code's Testing view.
      * When debugging, Playwright typically runs in headed mode by default.
  * **Playwright Inspector not appearing:**
      * Ensure you're running in debug mode.
      * Adding `page.pause()` explicitly forces the Inspector to appear.

By following these steps, you can effectively live debug your Playwright Python tests within VS Code, significantly speeding up your test development and troubleshooting process.
</td></tr></table>

## 2025-07-19

- 緣起：
  - 以前用 Selenium 可以透過 ipython 即時跟瀏覽器互動（e.g. 查 DOM 跟跑 BeautifulSoup 的結果），有點類似用 REPL 的方式寫程式。但改用 Playwright 以後就沒這種彈性了。雖然曾經查過 async 語法，但仍舊無法成功在 ipython 環境下透過 Playwright 開啟瀏覽器後，一步一步慢慢把步驟弄起來。當然好處是 Playwright 可以錄製步驟，變成程式碼，但仍舊喪失了即時互動的彈性。
  - 跟 QE 同事聊了一下，建議我評估一下 Live Debugging 的作法，先查一下文件，可能得做點實驗，會比較有感覺。
- 參考：
  - https://playwright.dev/python/docs/running-tests
  - https://playwright.dev/python/docs/debug