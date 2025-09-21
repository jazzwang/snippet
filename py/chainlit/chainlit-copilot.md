# Chainlit Copilot Application

- 2025-07-29 15:11 PM
- By Google Gemini 2.5 Flash

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
could you give me a step-by-step command line instruction to create a Python Chainlit Copilot app?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
A Chainlit Copilot app is essentially a Chainlit application designed to be embedded within an existing website or web application. It functions as a floating chatbot widget that can interact with your website's elements and send/receive data.

Here's a step-by-step command-line guide to create a basic Python Chainlit Copilot app.

**Prerequisites:**

  * **Python 3.9+:** Ensure you have a compatible Python version installed.
  * **pip:** Python package installer.
  * **A web server to host your HTML file:** For local testing, Python's built-in HTTP server or a simple tool like `live-server` (if you have Node.js) will work. For production, you'd use a more robust web server.

-----

### Step 1: Set Up Your Chainlit Project

1.  **Create a project directory:**

    ```bash
    mkdir my-copilot-app
    cd my-copilot-app
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install Chainlit:**

    ```bash
    pip install chainlit
    ```

4.  **Create `app.py`:**
    Create a file named `app.py` in your `my-copilot-app` directory. This will be your Chainlit backend. The key difference for a Copilot is how you handle messages, especially when interacting with the host website.

    ```python
    import chainlit as cl

    @cl.on_chat_start
    async def start():
        await cl.Message(
            content="Welcome to the Chainlit Copilot! I can assist you with your queries."
        ).send()

    @cl.on_message
    async def main(message: cl.Message):
        # Check if the message is coming from the Copilot widget
        if cl.context.session.client_type == "copilot":
            # This is where your Copilot-specific logic goes.
            # You can call functions on the host website, or simply respond.

            # Example: If the user sends a message, echo it back
            # or if a function call from the host app is received
            if message.type == "user_message":
                await cl.Message(
                    content=f"Copilot received: '{message.content}'. How else can I help?"
                ).send()
            elif message.type == "system_message":
                # This could be a message sent from your host application
                # to provide context to the Copilot.
                await cl.Message(
                    content=f"System message received by Copilot: {message.content}"
                ).send()

            # Example of calling a function on the host website
            # Let's say your host website has a JavaScript function called 'updateUI'
            # and you want to call it with some arguments.
            if "update ui" in message.content.lower():
                fn = cl.CopilotFunction(
                    name="updateUI",
                    args={"data": "Hello from Chainlit Copilot!"}
                )
                res = await fn.acall()
                await cl.Message(content=f"Called 'updateUI' on host. Result: {res}").send()

        else:
            # Standard Chainlit chat logic for the full web app interface
            await cl.Message(
                content=f"Hello! You're interacting with the full Chainlit app. Received: {message.content}"
            ).send()

    ```

5.  **Create `requirements.txt`:**

    ```
    chainlit
    ```

6.  **Configure Chainlit for Copilot (Optional but Recommended for CORS):**
    If your Copilot and the host website are on different domains (which they often will be, especially during development when one is `localhost:8000` and the other is `localhost:5500`), you'll need to configure Cross-Origin Resource Sharing (CORS).

    Create a `.chainlit` directory in your project root, and inside it, create a `config.toml` file:

    ```bash
    mkdir .chainlit
    ```

    Then, create `.chainlit/config.toml` with the following content:

    ```toml
    [features]
    copilot = true # Enable copilot features

    [web]
    cors_allow_origins = ["*"] # Be specific with your origins in production, e.g., ["http://localhost:5500", "https://your-website.com"]
    # If using authentication with Copilot on different domains, also add:
    # cookie_samesite = "none"
    ```

    **Important:** For `cors_allow_origins`, `"*"` is good for development, but in production, **always replace `*` with the specific origins (domains) where your Copilot will be embedded.** For example, `["https://your-website.com"]`.

-----

### Step 2: Create a Sample Host HTML File

Now, let's create a simple HTML file that will host your Chainlit Copilot widget.

1.  **Create `index.html`:**
    Create a file named `index.html` in your `my-copilot-app` directory.

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My Website with Chainlit Copilot</title>
        <style>
            body {
                font-family: sans-serif;
                margin: 20px;
                background-color: #f0f0f0;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
                background-color: white;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #333;
            }
            p {
                line-height: 1.6;
                color: #555;
            }
            button {
                padding: 10px 15px;
                background-color: #007bff;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
                margin-top: 20px;
            }
            button:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to My Awesome Website!</h1>
            <p>This is some content on your website. Imagine this is your product page, documentation, or any web application where you want to embed an AI assistant.</p>
            <p>The Chainlit Copilot will appear as a floating button on the bottom right of this page.</p>

            <button onclick="sendContextToCopilot()">Send Context to Copilot</button>
            <button onclick="toggleCopilot()">Toggle Copilot</button>

            <p id="copilotResponse"></p>
        </div>

        <script src="http://localhost:8000/copilot/index.js"></script>
        <script>
            // This function configures and mounts the Chainlit Copilot widget
            window.mountChainlitWidget({
                chainlitServer: "http://localhost:8000", // Replace with your Chainlit server URL in production
                // theme: "dark", // Optional: "light" or "dark"
                // accessToken: "YOUR_AUTH_TOKEN_IF_AUTHENTICATION_ENABLED", // If your Chainlit app requires auth
            });

            // Example: Function to listen for calls from the Copilot (from app.py)
            window.addEventListener("chainlit-call-fn", (e) => {
                const { name, args, callback } = e.detail;
                console.log(`Received call from Copilot: function=${name}, args=`, args);

                if (name === "updateUI") {
                    document.getElementById("copilotResponse").innerText = `Copilot updated UI: ${args.data}`;
                    callback("UI updated successfully!"); // Send result back to Chainlit
                } else {
                    callback("Unknown function called from Copilot.");
                }
            });

            // Example: Function to send a "system_message" to the Copilot
            async function sendContextToCopilot() {
                // Ensure the copilot is mounted before trying to send messages
                if (window.chainlitClient) {
                    await window.chainlitClient.sendSystemMessage("User is currently on the product page viewing 'Product X'.");
                    alert("Context sent to Copilot!");
                } else {
                    alert("Chainlit Copilot not yet loaded. Please wait a moment.");
                }
            }

            // Example: Function to programmatically toggle the Copilot visibility
            function toggleCopilot() {
                if (window.toggleChainlitCopilot) {
                    window.toggleChainlitCopilot();
                } else {
                    alert("Chainlit Copilot not yet loaded.");
                }
            }

        </script>
    </body>
    </html>
    ```

-----

### Step 3: Run Your Chainlit Copilot App

1.  **Start your Chainlit backend:**
    In your terminal, navigate to the `my-copilot-app` directory and run:

    ```bash
    chainlit run app.py -h --port 8000
    ```

      * `-h`: This runs Chainlit in "headless" mode, meaning it won't try to open a browser window, which is ideal for server-side deployments or when embedding.
      * `--port 8000`: Specifies the port for the Chainlit server.
      * If you added `cors_allow_origins` in `config.toml`, make sure the host you use for `index.html` is included there.

2.  **Serve your `index.html` file:**
    Open a **new terminal window** (keep the Chainlit server running in the first one). Navigate to your `my-copilot-app` directory.

      * **Using Python's built-in HTTP server:**

        ```bash
        python -m http.server 5500
        ```

        This will serve the `index.html` file on `http://localhost:5500`.

      * **Using `live-server` (if you have Node.js and installed it globally: `npm install -g live-server`):**

        ```bash
        live-server --port=5500
        ```

        This is often more convenient as it automatically reloads the browser on file changes.

3.  **Open your browser:**
    Navigate to `http://localhost:5500`.

    You should see your "My Awesome Website\!" content, and a small, floating Chainlit button (usually a chat icon) in the bottom right corner. Click this button to open the Chainlit Copilot widget.

      * Try typing messages in the Copilot.
      * Click the "Send Context to Copilot" button to see how your website can send system messages to the Copilot.
      * Type "update ui" in the copilot and see the effect on the host page, demonstrating `cl.CopilotFunction` calls.

-----

**Explanation of Copilot-Specific Elements:**

  * **`@cl.on_message` with `cl.context.session.client_type == "copilot"`:**
    This allows your `app.py` logic to differentiate between messages coming from the full Chainlit web UI and those coming from the embedded Copilot widget. This is crucial for tailoring responses or actions based on the client type.

  * **`cl.CopilotFunction`:**
    This class allows your Python backend to call JavaScript functions defined on the host website where the Copilot is embedded. This enables your AI assistant to take actions on behalf of the user within the host application (e.g., fill a form, navigate to a page, display information).

  * **`window.mountChainlitWidget({ chainlitServer: "http://localhost:8000" })`:**
    This JavaScript function, provided by Chainlit's `index.js` script, initializes and mounts the Copilot widget. The `chainlitServer` parameter tells the widget where to find your Chainlit backend.

  * **`window.addEventListener("chainlit-call-fn", ...)`:**
    This JavaScript event listener on your host page allows your website to receive calls from `cl.CopilotFunction` executed by your Chainlit backend. You can then define logic in JavaScript to handle these calls.

  * **`window.chainlitClient.sendSystemMessage()`:**
    This allows your host website to programmatically send messages to the Chainlit Copilot. These are often "system messages" that provide context to the AI (e.g., "The user is currently on the checkout page," "The user just clicked 'Add to Cart'").

  * **`window.toggleChainlitCopilot()`:**
    A utility function to programmatically open or close the Copilot widget.

This setup provides a robust foundation for building interactive AI copilots that seamlessly integrate with your existing web applications. Remember to adjust the CORS settings and server URLs for your production environment.
</td></tr></table>