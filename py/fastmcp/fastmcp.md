# FastMCP

- Git Repo
  - https://github.com/jlowin/fastmcp
- Website
  - https://gofastmcp.com/

## 2025-11-21

> \# aider chat started at 2025-11-21 08:12:07

> C:\Users\jazzw\.local\bin\aider --no-auto-commits --no-gitignore --model gemini/gemini-2.5-flash --chat-history-file fastmcp.md  
> Aider v0.86.1  
> Model: gemini/gemini-2.5-flash with diff-fenced edit format  
> Git repo: ..\..\.git with 1,545 files  
> Warning: For large repos, consider using --subtree-only and .aiderignore  
> See: https://aider.chat/docs/faq.html#can-i-use-aider-in-a-large-mono-repo  
> Repo-map: using 4096 tokens, auto refresh  
> Note: in-chat filenames are always relative to the git working dir, not the current working dir.  
> Cur working dir: C:\Users\jazzw\git\snippet\py\fastmcp  
> Git working dir: C:\Users\jazzw\git\snippet  

> ##### /ask could you give me a step-by-step command line instruction to build a local file search MCP server using python fastmcp library?  

> Repo-map can't include C:\Users\jazzw\git\snippet\c#\c-sharp-basics  
> Has it been deleted from the file system but not from git?  
> Repo-map can't include C:\Users\jazzw\git\snippet\go\go-workshop-practical  
> Has it been deleted from the file system but not from git?  
> Repo-map can't include C:\Users\jazzw\git\snippet\js\chrome-extensions\ms-stream-transcript-extractor  
> Has it been deleted from the file system but not from git?  
> Repo-map can't include C:\Users\jazzw\git\snippet\js\chrome-extensions\ms-teams-live-caption-saver  
> Has it been deleted from the file system but not from git?  
> Repo-map can't include C:\Users\jazzw\git\snippet\py\playwright\docker-playwright-vnc  
> Has it been deleted from the file system but not from git?  

I do not see any files in the provided summaries that indicate the use of a `python fastmcp` library. However, I see files (`py\fastapi\main.py`, `py\fastapi\pet.py`, `py\fastapi\pet2.py`) that suggest the use of `FastAPI`.

Could you clarify if you meant `FastAPI`?

> py\fastapi\pet.py  
> Add file to the chat? (Y)es/(N)o/(D)on't ask again [Yes]: n  

> ##### /ask could you give me a step-by-step command line instruction to build a local file search MCP server using python fastmcp https://github.com/jlowin/fastmcp?  

> Add URL to the chat? (Y)es/(N)o/(D)on't ask again [Yes]: y  
> Scraping https://github.com/jlowin/fastmcp?...  
> For the best web scraping, install Playwright:

> Install playwright? (Y)es/(N)o [Yes]: n  
> Unable to initialize playwright.  

Here are the step-by-step command line instructions to build a local file search MCP server using the `fastmcp` library:

**Step 1: Install `fastmcp`**

Open your terminal or command prompt and install the `fastmcp` library. It is recommended to use `uv` if you have it installed, otherwise `pip`.

```bash
uv pip install fastmcp
# OR
pip install fastmcp
```

**Step 2: Create the server file**

Create a Python file named `server.py` in your desired directory with the following content:

```python
import os
import fnmatch
from typing import List
from fastmcp import FastMCP

# Initialize the FastMCP server
mcp = FastMCP("File Search Server")

@mcp.tool
def search_local_files(query: str, root_dir: str = ".") -> List[str]:
    """
    Searches for files matching a given pattern in the specified directory and its subdirectories.

    Args:
        query (str): The filename pattern to search for (e.g., "*.txt", "report.pdf").
        root_dir (str): The root directory to start the search from. Defaults to the current directory.

    Returns:
        List[str]: A list of full paths to the files that match the query.
    """
    matching_files = []
    # Ensure the root_dir is valid
    if not os.path.isdir(root_dir):
        print(f"Warning: Directory '{root_dir}' not found. Returning empty list.")
        return []

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in fnmatch.filter(filenames, query):
            matching_files.append(os.path.join(dirpath, filename))
    return matching_files

if __name__ == "__main__":
    # Run the FastMCP server, by default it uses the STDIO transport.
    mcp.run()
```

**Step 3: Run the MCP server**

Navigate to the directory containing `server.py` in your terminal and execute the following command:

```bash
fastmcp run server.py
```

Your `fastmcp` server for local file search is now running, listening for requests via STDIO.

> ##### /run touch fastmcp-server.py  
> Add 0.0k tokens of command output to the chat? (Y)es/(N)o [Yes]: n  

> ##### /add fastmcp-server.py  
> Added fastmcp-server.py to the chat  

> ##### build a local file search MCP server using python fastmcp https://github.com/jlowin/fastmcp  
> https://github.com/jlowin/fastmcp  
> Add URL to the chat? (Y)es/(N)o/(D)on't ask again [Yes]: y  
> Scraping https://github.com/jlowin/fastmcp...  
> For the best web scraping, install Playwright:
> Install playwright? (Y)es/(N)o [Yes]: n  
> Unable to initialize playwright.  

Here are the *SEARCH/REPLACE* blocks to create the `fastmcp-server.py` file:

```python
fastmcp-server.py
<<<<<<< SEARCH
=======
import os
import fnmatch
from typing import List
from fastmcp import FastMCP

# Initialize the FastMCP server
mcp = FastMCP("Local File Search Server")

@mcp.tool
def search_local_files(query: str, root_dir: str = ".") -> List[str]:
    """
    Searches for files matching a given pattern in the specified directory and its subdirectories.

    Args:
        query (str): The filename pattern to search for (e.g., "*.txt", "report.pdf").
        root_dir (str): The root directory to start the search from. Defaults to the current directory.

    Returns:
        List[str]: A list of full paths to the files that match the query.
    """
    matching_files = []
    # Ensure the root_dir is valid
    if not os.path.isdir(root_dir):
        # Using print for warning as ctx.info() is not available outside a tool call context
        print(f"Warning: Directory '{root_dir}' not found or is not a directory. Returning empty list.")
        return []

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in fnmatch.filter(filenames, query):
            matching_files.append(os.path.join(dirpath, filename))
    return matching_files

if __name__ == "__main__":
    # Run the FastMCP server. By default, it uses the STDIO transport,
    # which is suitable for local command-line interaction.
    mcp.run()
>>>>>>> REPLACE
```

Once you've applied these changes, follow these steps in your command line:

1.  **Install the `fastmcp` library**:
    ```bash
    uv pip install fastmcp
    ```
    (If `uv` is not installed, you can use `pip install fastmcp` instead.)

2.  **Run the `fastmcp` server**:
    ```bash
    fastmcp run fastmcp-server.py
    ```

Your local file search MCP server will then be running and ready to accept calls via standard input/output.

> Applied edit to fastmcp-server.py  
> uv pip install fastmcp  
> Run shell command? (Y)es/(N)o/(S)kip all/(D)on't ask again [Yes]: y  
> Running uv pip install fastmcp  
> Add command output to the chat? (Y)es/(N)o/(D)on't ask again [Yes]: y  
> Added 2 lines of output to the chat.  
> fastmcp run fastmcp-server.py  
> Run shell command? (Y)es/(N)o/(S)kip all/(D)on't ask again [Yes]: y  
> Running fastmcp run fastmcp-server.py  
> Add command output to the chat? (Y)es/(N)o/(D)on't ask again [Yes]: y  
> Added 3 lines of output to the chat.  

> ##### /run pip install fastmcp  
> Add 5.2k tokens of command output to the chat? (Y)es/(N)o [Yes]: y  
> Added 126 lines of output to the chat.  

> ##### /run which fastmcp  
> Add 0.0k tokens of command output to the chat? (Y)es/(N)o [Yes]: y  
> Added 1 line of output to the chat.  

> ##### /run fastmcp run fastmcp-server.py  
> ^C again to exit  

> ##### /ask how to validate fastmcp-server.py?  

To validate `fastmcp-server.py`, you can use a `fastmcp.Client` to interact with it.

**Step 1: Create a client script**

Create a new Python file named `fastmcp-client.py` in the same directory as `fastmcp-server.py` with the following content:

```python
import asyncio
from fastmcp import Client

async def main():
    # Connect via in-memory transport to the server script
    # The client can directly interact with the FastMCP instance
    # if it's running as a script with mcp.run() (default STDIO transport)
    async with Client("./fastmcp-server.py") as client:
        print("Connected to FastMCP server.")

        # List available tools to confirm server is working
        tools = await client.list_tools()
        print(f"Available tools: {tools}")

        # Call the search_local_files tool
        # Replace 'YOUR_QUERY' with a file pattern (e.g., "*.py", "fastmcp-server.py")
        # Replace 'YOUR_ROOT_DIR' with a directory to search, or keep "." for current directory
        query = "*.py" # Example: search for all Python files
        root_dir = "." # Example: search in the current directory

        print(f"\nCalling tool 'search_local_files' with query='{query}' and root_dir='{root_dir}'...")
        try:
            result = await client.call_tool("search_local_files", {"query": query, "root_dir": root_dir})
            print(f"Tool call result: {result.content}")
        except Exception as e:
            print(f"Error calling tool: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```

**Step 2: Run the client script**

Open your terminal or command prompt, navigate to the directory where you saved both `fastmcp-server.py` and `fastmcp-client.py`, and run the client script:

```bash
python fastmcp-client.py
```

This command will execute the client, which will connect to your `fastmcp-server.py`, list its tools, and then attempt to call the `search_local_files` tool. The output will show if the connection was successful and the results of the tool call.

> ##### /drop  
> Dropping all files from the chat session.  

> ##### create fastmcp-client.py to validate fastmcp-server.py  

Here is the *SEARCH/REPLACE* block to create `fastmcp-client.py`:

```python
fastmcp-client.py
<<<<<<< SEARCH
=======
import asyncio
from fastmcp import Client

async def main():
    # Connect via in-memory transport to the server script
    # The client can directly interact with the FastMCP instance
    # if it's running as a script with mcp.run() (default STDIO transport)
    async with Client("./fastmcp-server.py") as client:
        print("Connected to FastMCP server.")

        # List available tools to confirm server is working
        tools = await client.list_tools()
        print(f"Available tools: {tools}")

        # Call the search_local_files tool
        # Replace 'YOUR_QUERY' with a file pattern (e.g., "*.py", "fastmcp-server.py")
        # Replace 'YOUR_ROOT_DIR' with a directory to search, or keep "." for current directory
        query = "*.py" # Example: search for all Python files
        root_dir = "." # Example: search in the current directory

        print(f"\nCalling tool 'search_local_files' with query='{query}' and root_dir='{root_dir}'...")
        try:
            result = await client.call_tool("search_local_files", {"query": query, "root_dir": root_dir})
            print(f"Tool call result: {result.content}")
        except Exception as e:
            print(f"Error calling tool: {e}")

if __name__ == "__main__":
    asyncio.run(main())
>>>>>>> REPLACE
```

After applying this change, you can run the client script using the following command:

```bash
python fastmcp-client.py
```

> fastmcp-client.py  
> Create new file? (Y)es/(N)o [Yes]: y  
> Applied edit to fastmcp-client.py  
> python fastmcp-client.py  
> Run shell command? (Y)es/(N)o/(D)on't ask again [Yes]: y  
> Running python fastmcp-client.py  
> Add command output to the chat? (Y)es/(N)o/(D)on't ask again [Yes]: y  
> Added 29 lines of output to the chat.  

> ##### /quit  

- 原本測試 `python fastmcp-client.py` 會報錯，但看 code 覺得 STDIO 的 local server 也不可能是連線 `fastmcp-server.py` ，越看越怪。
- 參考了 https://gofastmcp.com/getting-started/quickstart
- 把 `fastmcp-client.py` 改成連線 `http://localhost:8000/mcp`
```diff
diff --git a/py/fastmcp/fastmcp-client.py b/py/fastmcp/fastmcp-client.py
index 6ceafa8..82c9e70 100644
--- a/py/fastmcp/fastmcp-client.py
+++ b/py/fastmcp/fastmcp-client.py
@@ -5,7 +5,7 @@ async def main():
     # Connect via in-memory transport to the server script
     # The client can directly interact with the FastMCP instance
     # if it's running as a script with mcp.run() (default STDIO transport)
-    async with Client("./fastmcp-server.py") as client:
+    async with Client("http://localhost:8000/mcp") as client:
         print("Connected to FastMCP server.")

         # List available tools to confirm server is working
```
- 把執行 MCP Server 的命令改成
```bash
fastmcp run fastmcp-server.py --transport http --port 8000
```
```bash
~/git/snippet/py/fastmcp$ fastmcp run fastmcp-server.py --transport http --port 8000


                                      ╭──────────────────────────────────────────────────────────────────────────────╮
                                      │                                                                              │
                                      │                         ▄▀▀ ▄▀█ █▀▀ ▀█▀ █▀▄▀█ █▀▀ █▀█                        │
                                      │                         █▀  █▀█ ▄▄█  █  █ ▀ █ █▄▄ █▀▀                        │
                                      │                                                                              │
                                      │                                FastMCP 2.13.1                                │
                                      │                                                                              │
                                      │                                                                              │
                                      │                  🖥  Server name: Local File Search Server                    │
                                      │                                                                              │
                                      │                  📦 Transport:   HTTP                                        │
                                      │                  🔗 Server URL:  http://127.0.0.1:8000/mcp                   │
                                      │                                                                              │
                                      │                  📚 Docs:        https://gofastmcp.com                       │
                                      │                  🚀 Hosting:     https://fastmcp.cloud                       │
                                      │                                                                              │
                                      ╰──────────────────────────────────────────────────────────────────────────────╯


[11/21/25 15:30:11] INFO     Starting MCP server 'Local File Search Server' with transport 'http' on http://127.0.0.1:8000/mcp                server.py:2055
INFO:     Started server process [12972]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:59637 - "POST /mcp HTTP/1.1" 200 OK
INFO:     127.0.0.1:59640 - "POST /mcp HTTP/1.1" 202 Accepted
INFO:     127.0.0.1:59641 - "GET /mcp HTTP/1.1" 200 OK
INFO:     127.0.0.1:59643 - "POST /mcp HTTP/1.1" 200 OK
INFO:     127.0.0.1:54348 - "POST /mcp HTTP/1.1" 200 OK
INFO:     127.0.0.1:54350 - "DELETE /mcp HTTP/1.1" 200 OK
```

- 這樣就測通了!!
```bash
~/git/snippet/py/fastmcp$ python fastmcp-client.py
Connected to FastMCP server.
Available tools: [Tool(name='search_local_files', title=None, description='Searches for files matching a given pattern in the specified directory and its subdirectories.\n\nArgs:\n    query (str): The filename pattern to search for (e.g., "*.txt", "report.pdf").\n    root_dir (str): The root directory to start the search from. Defaults to the current directory.\n\nReturns:\n    List[str]: A list of full paths to the files that match the query.', inputSchema={'properties': {'query': {'type': 'string'}, 'root_dir': {'default': '.', 'type': 'string'}}, 'required': ['query'], 'type': 'object'}, outputSchema={'properties': {'result': {'items': {'type': 'string'}, 'type': 'array'}}, 'required': ['result'], 'type': 'object', 'x-fastmcp-wrap-result': True}, icons=None, annotations=None, meta={'_fastmcp': {'tags': []}})]

Calling tool 'search_local_files' with query='*.py' and root_dir='.'...
Tool call result: [TextContent(type='text', text='[".\\\\fastmcp-client.py",".\\\\fastmcp-server.py"]', annotations=None, meta=None)]
```