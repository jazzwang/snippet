# RequestsCookieJar

- 2025-09-15 21:11 PM
- By Google Gemini 2.5 Flash

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
if I have a "storage_state.json" saved by Playwright, how can I use Python requests to read it and load `cookies` from it?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
You can read the `storage_state.json` file saved by Playwright and load the cookies into a Python `requests.Session` object. The `storage_state.json` file is a JSON object that contains cookies, local storage, and other data. The `cookies` key holds a list of dictionaries, where each dictionary represents a single cookie.

Here's how to do it:

### The `storage_state.json` Format

A typical `storage_state.json` file looks like this:

```json
{
  "cookies": [
    {
      "name": "session_id",
      "value": "12345",
      "domain": "example.com",
      "path": "/",
      "expires": 1672531199,
      "httpOnly": true,
      "secure": true,
      "sameSite": "Lax"
    },
    {
      "name": "user_id",
      "value": "user_1",
      "domain": "example.com",
      "path": "/",
      "expires": -1,
      "httpOnly": false,
      "secure": false,
      "sameSite": "Strict"
    }
  ],
  "origins": [
    {
      "origin": "https://example.com",
      "localStorage": [
        {
          "name": "auth_token",
          "value": "abcdefg"
        }
      ]
    }
  ]
}
```

The relevant part for `requests` is the `"cookies"` array, which contains the list of cookies.

-----

### Reading the File and Loading Cookies

To load these cookies into a `requests.Session`, you'll first read the JSON file, then iterate through the list of cookie dictionaries to set them on the session. Using a `requests.Session` is the best approach, as it persists cookies and other settings across multiple requests.

```python
import json
import requests
from requests.cookies import RequestsCookieJar

def load_cookies_from_playwright_state(file_path):
    """
    Reads a Playwright storage_state.json file and returns a
    RequestsCookieJar object containing the cookies.
    """
    try:
        with open(file_path, 'r') as f:
            storage_state = json.load(f)
            cookies = storage_state.get('cookies', [])

        jar = RequestsCookieJar()
        for cookie in cookies:
            jar.set(
                name=cookie['name'],
                value=cookie['value'],
                domain=cookie['domain'],
                path=cookie['path']
            )
        return jar

    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from {file_path}.")
        return None
    except KeyError as e:
        print(f"Error: Missing key in cookie data: {e}")
        return None

# Example usage:
session = requests.Session()
cookie_jar = load_cookies_from_playwright_state('storage_state.json')

if cookie_jar:
    session.cookies.update(cookie_jar)
    
    # Now you can use the session for authenticated requests
    response = session.get('https://example.com/protected_page')
    print(response.text)
else:
    print("Could not load cookies. Skipping authenticated requests.")
```

**Breakdown of the Code:**

1.  **Read the JSON file:** The code opens and reads the `storage_state.json` file into a Python dictionary.
2.  **Extract the `cookies` list:** It accesses the `cookies` key from the dictionary.
3.  **Create a `RequestsCookieJar`:** This is a special `requests` object designed to manage cookies. It's more robust than a simple dictionary for setting cookies, as it handles attributes like `domain` and `path`.
4.  **Set cookies in the jar:** The code iterates through each cookie dictionary from the JSON file and uses the `jar.set()` method to add it to the `RequestsCookieJar`.
5.  **Load the cookies into a `requests.Session`:** Finally, `session.cookies.update(cookie_jar)` merges the cookies from the jar into your `requests` session, so all subsequent requests made with this session will automatically include them.
</td></tr></table>