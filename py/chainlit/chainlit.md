# Chainlit

> Build Conversational AI in minutes ⚡️

- Git Repo
  - https://github.com/Chainlit/chainlit
- Document
  - https://docs.chainlit.io/get-started/overview
- Website
  - https://chainlit.io/

## 2025-07-29

- 緣起：
  - 原本做過 Hospital Price Transparency Chatbot，就是用 Chainlit
    - see [Building Hospital Price Transparency Chatbot with OpenAI, LangChain and Chainlit](https://jazzwang.github.io/cv/talks/2024-02-20_CGU_HPT_Chatbot.html)
  - 最近需要整合 Databricks Apps 到現有產品，想說可否用 Chainlit Copilot 來達成展示給產品經理看 POC 比較有感覺。
- 嘗試：
  - https://g.co/gemini/share/32e7bdb816f2
<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
could you give me a step-by-step command line instructions to create a Chainlit sample app, make it a docker image and deploy huggingface space?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
This guide will walk you through creating a simple Chainlit application, containerizing it with Docker, and deploying it to Hugging Face Spaces.

**Prerequisites:**

  * **Python 3.9+:** Make sure you have a compatible Python version installed.
  * **pip:** Python package installer.
  * **Docker:** Docker Desktop installed and running.
  * **Hugging Face Account:** You'll need an account to create a Space.
  * **Git:** Installed on your system.
  * **Hugging Face CLI (optional but recommended):** `pip install huggingface_hub` and `huggingface-cli login` to authenticate.

-----

### Step 1: Create a Chainlit Sample App

1.  **Create a project directory:**

    ```bash
    mkdir my-chainlit-app
    cd my-chainlit-app
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
    Create a file named `app.py` in your `my-chainlit-app` directory and add the following basic Chainlit code:

    ```python
    import chainlit as cl

    @cl.on_message
    async def main(message: cl.Message):
        # Your custom logic goes here...
        # For this example, we'll just echo the message
        await cl.Message(
            content=f"Received: {message.content}. This is a sample Chainlit app!"
        ).send()

    @cl.on_chat_start
    async def start():
        await cl.Message(
            content="Welcome to the Chainlit sample app! Type something to get started."
        ).send()
    ```

5.  **Create `requirements.txt`:**
    Create a file named `requirements.txt` in your `my-chainlit-app` directory. This file lists your Python dependencies.

    ```
    chainlit
    ```

6.  **Test your Chainlit app locally:**

    ```bash
    chainlit run app.py -w
    ```

    Open your browser and navigate to `http://localhost:8000`. You should see the Chainlit UI. Type a message and see the app respond. Press `Ctrl+C` in your terminal to stop the application.

-----

### Step 2: Dockerize the Chainlit App

1.  **Create a `Dockerfile`:**
    Create a file named `Dockerfile` (no extension) in your `my-chainlit-app` directory.

    ```dockerfile
    # Use an official Python runtime as a parent image
    FROM python:3.9-slim-buster

    # Set the working directory in the container
    WORKDIR /app

    # Install system dependencies if any (none needed for this simple app)
    # RUN apt-get update && apt-get install -y --no-install-recommends \
    #     && rm -rf /var/lib/apt/lists/*

    # Copy the requirements file into the working directory
    COPY requirements.txt .

    # Install the Python dependencies
    RUN pip install --no-cache-dir -r requirements.txt

    # Copy the application code into the container
    COPY . .

    # Expose the port Chainlit runs on
    EXPOSE 8000

    # Command to run the Chainlit application
    # --host 0.0.0.0 makes it accessible from outside the container
    # --port 8000 is the default Chainlit port
    # -h is recommended for production deployments to prevent browser window opening server-side
    CMD ["chainlit", "run", "app.py", "--host", "0.0.0.0", "--port", "8000", "-h"]
    ```

2.  **Build the Docker image:**
    Navigate to your `my-chainlit-app` directory in the terminal and run:

    ```bash
    docker build -t my-chainlit-app:latest .
    ```

    This command builds a Docker image named `my-chainlit-app` with the tag `latest`.

3.  **Test the Docker image locally:**

    ```bash
    docker run -p 8000:8000 my-chainlit-app:latest
    ```

    Open your browser to `http://localhost:8000`. You should see your Chainlit app running from within the Docker container. Press `Ctrl+C` in your terminal to stop the container.

-----

### Step 3: Deploy to Hugging Face Spaces

Hugging Face Spaces uses Git for deployment. You'll create a new Space, clone its Git repository, add your Dockerized Chainlit app files, and push them.

1.  **Create a new Hugging Face Space:**

      * Go to [Hugging Face Spaces](https://huggingface.co/spaces).
      * Click on "Create new Space".
      * Fill in the details:
          * **Space name:** Choose a unique name (e.g., `my-chainlit-demo`). This will be part of your Space URL.
          * **License:** (Optional) Choose a license.
          * **Space Hardware:** Start with the "CPU Basic" (Free) option.
          * **SDK:** Select **"Docker"**. This is crucial for Docker deployments.
          * **Visibility:** Choose "Public" or "Private" as desired.
      * Click "Create Space".

2.  **Clone your new Hugging Face Space repository:**
    After creating the Space, you'll be redirected to its page. You'll see instructions to clone the repository. It will look something like this:

    ```bash
    git clone https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME
    ```

    Replace `YOUR_USERNAME` and `YOUR_SPACE_NAME` with your actual Hugging Face username and the name you chose for your Space. Execute this command in your terminal.

3.  **Copy your Chainlit app files into the Space repository:**
    Navigate into the cloned Space directory:

    ```bash
    cd YOUR_SPACE_NAME
    ```

    Now, copy the `app.py`, `requirements.txt`, and `Dockerfile` from your `my-chainlit-app` directory into this `YOUR_SPACE_NAME` directory.

    ```bash
    cp ../my-chainlit-app/app.py .
    cp ../my-chainlit-app/requirements.txt .
    cp ../my-chainlit-app/Dockerfile .
    ```

    *(If you're already inside `my-chainlit-app` and then `cd` into `YOUR_SPACE_NAME`, adjust the `../` accordingly.)*

4.  **Configure `README.md` for Docker (Important\!):**
    Your Hugging Face Space automatically creates a `README.md`. You need to ensure it's configured for Docker. Open the `README.md` file in the `YOUR_SPACE_NAME` directory and make sure the YAML header at the top looks like this (add or modify if necessary):

    ```markdown
    ---
    title: My Chainlit App
    emoji: 🐳
    colorFrom: purple
    colorTo: gray
    sdk: docker
    app_port: 8000 # This is the port your Chainlit app is exposed on in the Dockerfile
    ---

    # My Chainlit Sample App

    This is a sample Chainlit application deployed on Hugging Face Spaces using Docker.
    ```

    The `sdk: docker` and `app_port: 8000` lines are critical.

5.  **Commit and push to Hugging Face Spaces:**
    Now, add your files to the Git repository, commit them, and push.

    ```bash
    git add .
    git commit -m "Add Chainlit app and Dockerfile"
    git push
    ```

    You might be prompted to enter your Hugging Face username and a User Access Token. Generate a token with "write" access from your Hugging Face settings: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens).

6.  **Monitor deployment:**
    Go back to your Hugging Face Space page in your browser. You should see the Space status change to "Building" and then "Running". You can also view the build logs to troubleshoot any issues.

Once the status is "Running", your Chainlit app will be live on your Hugging Face Space\! You can access it via the URL provided on your Space page (e.g., `https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME`).

**Troubleshooting Tips:**

  * **Logs:** Always check the "Logs" tab on your Hugging Face Space page for any errors during the build or runtime.
  * **Port:** Ensure the `EXPOSE` port in your `Dockerfile` matches the `app_port` in your `README.md` and the `--port` argument in your `CMD` command.
  * **Dependencies:** Double-check your `requirements.txt` to ensure all necessary Python packages are listed.
  * **Authentication:** If `git push` fails, ensure you have correctly authenticated with Hugging Face, either via the CLI (`huggingface-cli login`) or by providing your username and a write-access token when prompted.
  * **Chainlit `-h` flag:** For production environments like Hugging Face Spaces, always include the `-h` (headless) flag in your `chainlit run` command within the `Dockerfile`'s `CMD` instruction to prevent a browser window from opening server-side.
</td></tr></table>
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

- 需求：
  - 實驗過程中，遇到幾個狀況
    1. 應該是 `CQRS` 問題，也就是如果瀏覽器直接開 `file:///C:/Users/jazzw/git/my-chainlit-app/copilot.html`，會無法載入 JavaScript。
    2. 發現 Chainlit Copilot 找不到 Logo
- 解法：
  1. 改用 `python3 -m http.server 8088` (因為預設剛好都是 `8000` 連線埠) 來開 `copilot.html`，就沒遇到 `CQRS` 問題（因為同樣都是 `localhost`）
  2. 參考「使用客製化 Logo」的文件，簡單做就是在 Public 底下放 `logo_{dark|light}.png`
    - https://docs.chainlit.io/customisation/custom-logo-and-favicon
    - https://github.com/Chainlit/cookbook/tree/main/custom-logo
- 實驗：

```bash
~/git/my-chainlit-app$ tree
.
├── app.py
├── chainlit.md
├── copilot.html
├── Public
│   ├── logo_dark.png
│   └── logo_light.png
└── requirements.txt
~/git/my-chainlit-app$ cat app.py
```
- `app.py` 內容
```python
import chainlit as cl

@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...
    # For this example, we'll just echo the message
    await cl.Message(
        content=f"Received: {message.content}. This is a sample Chainlit app!"
    ).send()

@cl.on_chat_start
async def start():
    await cl.Message(
        content="Welcome to the Chainlit sample app! Type something to get started."
    ).send()
```
- `copilot.html`
```html
<head>
  <meta charset="utf-8" />
</head>
<body>
  <!-- ... -->
  <script src="http://localhost:8000/copilot/index.js"></script>
  <script>
    window.addEventListener("chainlit-call-fn", (e) => {
      const { name, args, callback } = e.detail;
      callback("You sent: " + args.msg);
    });
  </script>
  <script>
    window.mountChainlitWidget({
      chainlitServer: "http://localhost:8000",
    });
  </script>
</body>
```
- 後記：
  - 後來在 Cookbook 看到可以整合 React.js Frontend，那就更有彈性了！
    - https://github.com/Chainlit/cookbook/tree/main/custom-frontend

<video autoplay="" loop="" muted="" playsinline="" preload="metadata">
    <source src="https://github.com/Chainlit/cookbook/assets/13104895/5cc20490-2150-44da-b016-7e0e2e12dd52" type="video/mp4">
    Your browser does not support the video tag.
</video>

- 感想：
  - 一如 Chainlit 的創作初衷<mark>「Build Conversational AI in minutes ⚡️」</mark>，這個套件還是比較適合拿來做「對話聊天」的應用。其他比較複雜的界面就感覺相對不合適。目前暫時沒有想到如果對話是發生在不同 UI 元件時，該怎麼呈現。