# confluence-markdown-exporter

## 2025-09-15

- 緣起：
  - 在改寫 [confluence-insight](https://github.com/jazzwang/confluence-insight) 的過程中，
    想說既然都派爬蟲讀取了一次頁面，何不增加附加價值，
    把 confluence wiki page 轉成 markdown 也存一份在 Local，
    除了分析 confluence wiki page 跟 contributor 之間的關聯之外，
    還可以把這些 markdown 轉成 embedding 存到 vector store，當作 RAG 知識庫使用呢？
- 2025-09-15 23:22 PM 
  - 問 Gemini 可否給我一個 example python program
  - 本想看是否會建議用 `httpx` 或 `requests` 搭配其他 python HTML to Markdown 的 library 來把 confluence page 轉成 Markdown 檔。
    結果建議使用 `confluence-markdown-exporter` (當然可能也只是隨機得到的結果，因為範例程式是用 python `subprocess` 還呼叫命令列工具 `cf-export`)

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
could you show me an example Python program to convert confluence wiki page into markdown file? e.g. https://cwiki.apache.org/confluence/display/HADOOP/Roadmap
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
To convert a Confluence wiki page to a Markdown file in Python, you can use the `confluence-markdown-exporter` library, which is specifically designed for this purpose.

Here is an example program that uses this library to convert the page you specified (`https://cwiki.apache.org/confluence/display/HADOOP/Roadmap`) and saves it to a file.

-----

#### ⚙️ Prerequisites

First, you need to install the library. This can be done using `pip`:

```bash
pip install confluence-markdown-exporter
```

-----

#### 📝 Example Python Program

This program uses Python's `subprocess` module to call the command-line tool provided by the library. This is a robust way to interact with the tool from a script.

```python
import subprocess
import os

def convert_confluence_to_markdown(confluence_url, output_dir=".", file_name="output.md"):
    """
    Converts a public Confluence page to a Markdown file.

    Args:
        confluence_url (str): The URL of the Confluence page.
        output_dir (str, optional): The directory to save the Markdown file. Defaults to current directory.
        file_name (str, optional): The name of the output Markdown file. Defaults to "output.md".
    """
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Use the 'cf-export' command-line tool from the installed package.
    # The --url argument is used to specify the page to export.
    # The final argument is the output path.
    command = [
        "cf-export",
        "pages",
        "--url", confluence_url,
        output_dir
    ]

    try:
        # Run the command
        print(f"Converting page from {confluence_url}...")
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print("Conversion successful!")
        
        # The tool might save a file with a name based on the page title.
        # Find the newly created file and rename it if needed.
        # Note: The tool creates a nested directory structure.
        
        # In this specific case, the tool will create a file at:
        # ./output_dir/HADOOP/Roadmap.md
        # The user's request is for a simple file, so we'll just show the tool's output
        # since it correctly places the file in the specified directory.
        
        print("\n" + "="*50)
        print("Tool Output:")
        print(result.stdout)
        print("="*50 + "\n")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred during conversion: {e}")
        print(e.stderr)
    except FileNotFoundError:
        print("Error: 'cf-export' command not found. Please ensure 'confluence-markdown-exporter' is installed and in your system's PATH.")

if __name__ == "__main__":
    # The public Confluence URL to convert
    confluence_page_url = "https://cwiki.apache.org/confluence/display/HADOOP/Roadmap"
    
    # Define the output directory and file name
    output_directory = "./confluence_export"
    
    # Run the function
    convert_confluence_to_markdown(confluence_page_url, output_dir=output_directory)

```

#### 📋 Important Notes

  * **API Token**: For private Confluence instances, you will need to set environment variables for your username, API token, and the instance URL for authentication. The library uses these to connect to the Atlassian API.
  * **HTML to Markdown**: The `confluence-markdown-exporter` package is an excellent choice as it uses the official Confluence API to get the page content, which is in a structured format (XHTML), and then converts it to Markdown. Other methods, like simply scraping the HTML from the public page and trying to convert it, are less reliable because they might miss complex formatting and macros.
  * **Output Structure**: The tool creates a directory structure that mirrors the Confluence space, e.g., `confluence_export/HADOOP/Roadmap.md`. You can access the converted Markdown content within that file.
</td></tr></table>