# har2requests

> Generate Python Requests code from your browser activity 🤖

- PyPI
  - https://pypi.org/project/har2requests/
- Git Repo
  - https://github.com/louisabraham/har2requests

## Features

-   Automatic requests code generation from a [HAR file](https://en.wikipedia.org/wiki/.har)
-   Detection of the headers common to all requests and code factorization
-   Clever inference on the origin of authorization headers
-   Code formatting using [black](https://github.com/ambv/black)

## 2025-09-11

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
given a HAR network traffic export file, is it possible to convert it into python program using requests?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Yes, it is possible to convert a **HAR (HTTP Archive)** network traffic export file into a Python program using the **`requests`** library. A HAR file is essentially a JSON-formatted log of a web browser's interaction with a website. By parsing this JSON data, you can extract the necessary information—such as the URLs, headers, and request bodies—to reconstruct the network requests in Python.

-----

## How the Conversion Works

The conversion process involves several key steps:

1.  **Parsing the HAR file:** First, you need to read the HAR file and parse its JSON content. This can be done using Python's built-in `json` library. The relevant data is usually found within the `log.entries` array, where each entry represents a single HTTP request and its corresponding response.

2.  **Extracting Request Details:** For each entry in the HAR file, you'll need to extract the following information:

      * **URL:** The URL of the request.
      * **Method:** The HTTP method (e.g., GET, POST).
      * **Headers:** A dictionary of the request headers.
      * **Request Body:** If it's a POST request, the request body (e.g., form data or JSON payload).
      * **Cookies:** While cookies are often included in the headers, they can also be handled separately.

3.  **Constructing the Python Code:** With the extracted details, you can then dynamically generate Python code using the `requests` library. You would typically create a function for each request, or a loop that iterates through the entries, making a `requests.get()`, `requests.post()`, or other method call with the appropriate parameters.

### Example

For a simple GET request, the generated Python code might look something like this:

```python
import requests

url = "http://example.com/api/data"
headers = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
print(response.status_code)
print(response.json())
```

For a POST request, you would include the `data` or `json` parameter:

```python
import requests

url = "http://example.com/api/login"
headers = {
    "Content-Type": "application/json"
}
payload = {
    "username": "user123",
    "password": "password123"
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code)
print(response.text)
```

-----

## Tools for Conversion

While you can write a script from scratch to perform this conversion, several tools and libraries exist that automate this process, making it much easier. Some popular ones include:

  * **`har2requests`:** This is a dedicated Python library designed specifically for converting HAR files into `requests` scripts.
  * **`curl-converter`:** Although primarily used for converting `cURL` commands, some versions and online tools based on this library can also handle HAR files and generate Python code.
  * **Custom Scripts:** For more control or specific use cases, writing a simple Python script to parse the HAR file and generate the code is a common approach.

</td></tr></table>

## 2025-11-12

- 補測試紀錄
- 安裝：
```bash
~$ uv tool install har2requests
Resolved 12 packages in 3.15s
Prepared 12 packages in 1.37s
Installed 12 packages in 70ms
 + black==25.11.0
 + click==8.3.0
 + colorama==0.4.6
 + har2requests==0.2.3
 + mypy-extensions==1.1.0
 + packaging==25.0
 + pathspec==0.12.1
 + platformdirs==4.5.0
 + python-dateutil==2.9.0.post0
 + pytokens==0.3.0
 + six==1.17.0
 + tqdm==4.67.1
Installed 1 executable: har2requests.exe
```
- 驗證
```bash
~$ which har2requests
/c/Users/jazzw/scoop/apps/python/current/Scripts/har2requests

~$ har2requests.exe --help
Usage: har2requests [OPTIONS] SRC

Options:
  --unsafe
  --no-infer
  --hide-result
  --include-options
  --generate-assertions
  --exclude-cookie-headers
  --debug-requests
  --help                    Show this message and exit.
```
- 用 https://petstore.swagger.io/ 的測試 HAR 當範例
```bash
~/git/snippet/py/har2requests$ har2requests.exe --no-infer ~/Downloads/sample.har > har2requests-sample.py
```
- 加上 `--no-infer` 會比較快
- 加上 `--hide-result` 會忽略結果
```bash
~/git/snippet/py/har2requests$ har2requests.exe --no-infer --hide-result ~/Downloads/sample.har > har2requests-sample.py
```