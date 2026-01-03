# Gemini Compute Use

## 2025-01-03

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
could you give a step-by-step instructions how to use gemini "compute use" ?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->

Gemini's **Computer Use** (officially part of the Gemini 2.5/3 series) is a specialized capability that allows the AI to interact with a computer interface—specifically a web browser—just as a human would. It doesn't just "read" a page; it can click, type, scroll, and navigate through multi-step workflows.

As of early 2026, this feature is primarily available to developers via the **Gemini API** and **Vertex AI**. Below are the step-by-step instructions to set it up.

---

## 1. Prerequisites & Setup

Before you can run the model, you need a developer environment and an API key.

1. **Get an API Key:** Go to [Google AI Studio](https://aistudio.google.com/) and generate a Gemini API key.
2. **Install the SDK:** Use the latest Google Gen AI Python library.
```bash
pip install -U google-genai playwright
playwright install chromium

```


3. **Model Selection:** Currently, you must use the specialized preview model: `gemini-2.5-computer-use-preview-10-2025` (or the latest Gemini 3 equivalent if specified in your dashboard).

---

## 2. Understanding the "Agentic Loop"

Unlike a standard chatbot, Computer Use requires a **loop**. The model cannot "click" a button directly; instead, it tells *your code* where to click, and your code reports back the result.

1. **Input:** You send a prompt + a screenshot of the current screen.
2. **Model Decision:** The model returns a `function_call` (e.g., `click_at(x=450, y=300)`).
3. **Action:** Your local script (using Playwright) executes that click.
4. **Feedback:** Your script takes a *new* screenshot and sends it back to the model.
5. **Repeat:** This continues until the task is finished.

---

## 3. Implementation Steps (Python)

### Step A: Initialize the Client

```python
from google import genai
from google.genai import types

client = genai.Client(api_key="YOUR_API_KEY")
model_id = 'gemini-2.5-computer-use-preview-10-2025'

```

### Step B: Configure the Computer Use Tool

You must explicitly enable the `computer_use` tool in your configuration.

```python
config = types.GenerateContentConfig(
    tools=[
        types.Tool(
            computer_use=types.ComputerUse(
                # Currently optimized for browser environments
                environment=types.Environment.ENVIRONMENT_BROWSER 
            )
        )
    ]
)

```

### Step C: Start the Interaction

When you send the first prompt, the model will likely ask to "navigate" or "click" based on the UI it sees.

```python
response = client.models.generate_content(
    model=model_id,
    contents="Go to Google Shopping, find a 4K monitor under $300, and add the cheapest one to the cart.",
    config=config
)

# The response will contain a 'function_call' such as 'navigate' or 'type_text_at'
print(response.candidates[0].content.parts[0].function_call)

```

---

## 4. Key Actions Supported

The model uses a specific coordinate system (0-1000 scale for x and y) to interact with the screen. Common commands include:

| Action | Description |
| --- | --- |
| `Maps` | Opens a specific URL in the browser. |
| `click_at` | Clicks a specific pixel coordinate. |
| `type_text_at` | Types a string into a field at a specific coordinate. |
| `scroll_document` | Scrolls the page up or down. |
| `drag_and_drop` | Moves an element from one coordinate to another. |

---

## 5. Using the Consumer "Gemini Agent"

If you are not a developer and just want to use this feature as an end-user:

1. Open the **Gemini App** or web interface.
2. Look for the **"Agent"** or **"Deep Research"** mode (available to Gemini Advanced/Ultra subscribers).
3. Give a multi-step instruction like *"Find a flight to Tokyo in May, then find a hotel near Shibuya and put the details in a draft email."*
4. The agent will open a small browser window on your screen and you will see it clicking and typing in real-time.

> [!IMPORTANT]
> **Safety First:** For sensitive actions (like "Buy Now" or "Send Email"), the model is designed to pause and ask for your manual confirmation before proceeding.

**Would you like me to provide a complete Python script template that handles the full automation loop for you?**
</td></tr>
<tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
yes, could you provide a complete Python script template?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->

This script provides a foundational "Agentic Loop." It uses **Playwright** to control a browser and the **Google Gen AI SDK** to process screenshots and decide on actions.

### 1. Prerequisites

You will need to install the necessary libraries and the Chromium browser:

```bash
pip install -U google-genai playwright
playwright install chromium

```

---

### 2. The Complete Python Script

This script implements a basic loop that allows Gemini to navigate, click, and type based on visual feedback.

```python
import os
import asyncio
from google import genai
from google.genai import types
from playwright.async_api import async_playwright

# 1. Setup Configuration
API_KEY = "YOUR_GEMINI_API_KEY"
MODEL_ID = "gemini-2.0-flash-exp" # Or the latest 'computer-use' enabled model

client = genai.Client(api_key=API_KEY)

async def run_computer_use_loop(prompt: str):
    async with async_playwright() as p:
        # Launch browser - headless=False lets you watch the AI work
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()

        # Initialize conversation history
        messages = [types.Content(role="user", parts=[types.Part.from_text(prompt)])]

        print(f"🚀 Starting task: {prompt}")

        for i in range(15):  # Limit steps to prevent infinite loops
            # 1. Capture current state (Screenshot)
            screenshot_bytes = await page.screenshot(type="png")
            
            # 2. Add screenshot to the last message for context
            # In a real loop, you'd append the result of the previous action here
            messages[-1].parts.append(types.Part.from_bytes(data=screenshot_bytes, mime_type="image/png"))

            # 3. Call Gemini
            response = client.models.generate_content(
                model=MODEL_ID,
                contents=messages,
                config=types.GenerateContentConfig(
                    tools=[types.Tool(computer_use=types.ComputerUse(
                        environment=types.Environment.ENVIRONMENT_BROWSER
                    ))]
                )
            )

            # 4. Parse the response
            response_part = response.candidates[0].content.parts[0]
            messages.append(response.candidates[0].content)

            # Check if the model wants to call a tool
            if response_part.function_call:
                call = response_part.function_call
                name = call.name
                args = call.args

                print(f"🤖 Action {i+1}: {name} | Args: {args}")

                # 5. Execute the Tool (Mapping Gemini actions to Playwright)
                result = await execute_tool(page, name, args)
                
                # 6. Feed the result back to the model
                messages.append(types.Content(
                    role="user",
                    parts=[types.Part.from_function_response(name=name, response={"result": result})]
                ))
            else:
                print("✅ Task completed or model provided a final text answer.")
                print(f"Final Response: {response.text}")
                break

        await browser.close()

async def execute_tool(page, name, args):
    """Maps Gemini's coordinate-based commands to Playwright actions."""
    # Gemini uses a 0-1000 scale. We map it to our 1280x800 viewport.
    width, height = 1280, 800
    
    if name == "navigate":
        await page.goto(args['url'])
        return f"Navigated to {args['url']}"
    
    elif name == "click_at":
        x = (args['x'] / 1000) * width
        y = (args['y'] / 1000) * height
        await page.mouse.click(x, y)
        return f"Clicked at {x}, {y}"
    
    elif name == "type_text_at":
        x = (args['x'] / 1000) * width
        y = (args['y'] / 1000) * height
        await page.mouse.click(x, y)
        await page.keyboard.type(args['text'])
        return f"Typed '{args['text']}' at {x}, {y}"
    
    elif name == "scroll_document":
        direction = args.get('direction', 'down')
        await page.evaluate("window.scrollBy(0, 500)" if direction == "down" else "window.scrollBy(0, -500)")
        return f"Scrolled {direction}"

    return "Unknown action"

# Run the script
if __name__ == "__main__":
    asyncio.run(run_computer_use_loop("Search for the latest news on SpaceX on Google and tell me the title of the first result."))

```

---

### 3. Critical Implementation Details

* **Coordinate Scaling:** Gemini doesn't know your screen resolution. It operates on a **normalized 0-1000 scale**. You must multiply its output by your actual window width/height (as shown in the `execute_tool` function).
* **Token Usage:** Every step sends a full screenshot back to the model. This can consume many tokens quickly. It is best to use **Gemini 2.0 Flash** for this to keep costs low and speed high.
* **The "Wait" Factor:** After clicking or navigating, a real browser takes time to load. In a production script, you should add `await page.wait_for_load_state("networkidle")` after actions to ensure the next screenshot isn't of a blank loading screen.

---

### 4. Safety & Limitations

* **CAPTCHAs:** Gemini will generally fail or get stuck if it hits a CAPTCHA.
* **Sensitive Data:** Avoid letting the agent navigate to pages with saved credit cards or passwords unless you are monitoring it in "non-headless" mode.

**Would you like me to show you how to add a "Human-in-the-loop" confirmation step so the AI asks for your permission before clicking "Buy" or "Send"?**
</td></tr></table>