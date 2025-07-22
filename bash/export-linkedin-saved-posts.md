# How to export LinkedIn Saved Posts for local search

## 2025-07-22

- 緣起：
  - 以前有試著用 Chrome DevTool 自動捲到下方把 LinkedIn Saved Post 通通列出來，然後把連結匯出成一個 txt 純文字檔
  - 有時候想到曾經看過某篇 LinkedIn 貼文，也應該有按 Save，但很難在茫茫清單中找到想要的文章。所以想說把這些貼文下載下來，看能否做本地備份跟索引。
- 工具：
  - curl 或 wget 或 `httpx`
<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
given 1000 url, how can I check each url with `wget` or `curl` but log url which return status code 404?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
You can achieve this by scripting with `wget` or `curl` and directing the output to a log file. Here's how you can do it for both tools, assuming you have your 1000 URLs in a file named `urls.txt`, with one URL per line.

### Method 1: Using `curl`

`curl` is generally preferred for its more detailed output and easier parsing of status codes.

```bash
#!/bin/bash

# Define the input file containing URLs
URL_FILE="urls.txt"

# Define the log file for 404 errors
LOG_FILE="404_urls.log"

# Clear the log file if it exists from a previous run
> "$LOG_FILE"

echo "Checking URLs for 404 status codes..."

while IFS= read -r url; do
    if [ -z "$url" ]; then
        continue # Skip empty lines
    fi

    echo "Checking: $url"

    # Use curl to get the HTTP status code
    # -o /dev/null: Discard the body of the response
    # -s: Silent mode (don't show progress meter or error messages)
    # -w "%{http_code}\n": Print only the HTTP status code followed by a newline
    http_code=$(curl -o /dev/null -s -w "%{http_code}\n" "$url")

    if [ "$http_code" == "404" ]; then
        echo "404 Not Found: $url" | tee -a "$LOG_FILE"
    fi
done < "$URL_FILE"

echo "Finished checking URLs. 404 errors logged in $LOG_FILE"
```

**Explanation:**

  * **`URL_FILE="urls.txt"`**: Specifies the file containing your URLs.
  * **`LOG_FILE="404_urls.log"`**: Specifies the file where 404 URLs will be logged.
  * **`> "$LOG_FILE"`**: Clears the `LOG_FILE` at the start.
  * **`while IFS= read -r url; do ... done < "$URL_FILE"`**: Reads each line (URL) from `urls.txt` into the `url` variable.
      * `IFS=` prevents leading/trailing whitespace issues.
      * `-r` prevents backslash escapes from being interpreted.
  * **`if [ -z "$url" ]; then continue; fi`**: Skips processing if a line is empty.
  * **`http_code=$(curl -o /dev/null -s -w "%{http_code}\n" "$url")`**: This is the core `curl` command.
      * `-o /dev/null`: Discards the downloaded content to prevent filling up your disk.
      * `-s`: Makes `curl` silent, so it doesn't show progress bars or verbose output.
      * `-w "%{http_code}\n"`: This is crucial. It tells `curl` to write *only* the HTTP status code followed by a newline to standard output, which is then captured by the `http_code` variable.
  * **`if [ "$http_code" == "404" ]; then ... fi`**: Checks if the obtained `http_code` is "404".
  * **`echo "404 Not Found: $url" | tee -a "$LOG_FILE"`**: If a 404 is found, it prints the message to the console (`tee`) and appends it to the `LOG_FILE` (`-a`).

### Method 2: Using `wget`

While `wget` can be used, it's a bit more cumbersome to extract just the status code directly compared to `curl`. `wget` is primarily for downloading. However, you can check its exit status or parse its output.

```bash
#!/bin/bash

# Define the input file containing URLs
URL_FILE="urls.txt"

# Define the log file for 404 errors
LOG_FILE="404_urls.log"

# Clear the log file if it exists from a previous run
> "$LOG_FILE"

echo "Checking URLs for 404 status codes..."

while IFS= read -r url; do
    if [ -z "$url" ]; then
        continue # Skip empty lines
    fi

    echo "Checking: $url"

    # Use wget to check the URL.
    # --spider: Don't download anything. Just check if the URL exists.
    # -q: Turn off Wget's output.
    # --server-response: Print HTTP server responses. We'll parse this.
    # --tries=1: Only try once to avoid long waits on unresponsive servers.
    wget --spider -q --server-response --tries=1 "$url" 2>&1 | grep "HTTP/" | head -n 1 | grep "404 Not Found" > /dev/null

    if [ $? -eq 0 ]; then
        echo "404 Not Found: $url" | tee -a "$LOG_FILE"
    fi
done < "$URL_FILE"

echo "Finished checking URLs. 404 errors logged in $LOG_FILE"
```

**Explanation:**

  * **`wget --spider -q --server-response --tries=1 "$url" 2>&1`**:
      * `--spider`: This is key for `wget` to only check the URL without downloading the content.
      * `-q`: Suppresses most of `wget`'s output.
      * `--server-response`: Makes `wget` print the HTTP headers sent by the server, which is where we'll find the status code.
      * `--tries=1`: Prevents `wget` from retrying multiple times on failures, speeding up the process.
      * `2>&1`: Redirects `stderr` (where `wget` often prints its messages, including server responses) to `stdout` so it can be piped.
  * **`| grep "HTTP/" | head -n 1 | grep "404 Not Found" > /dev/null`**: This is the parsing part.
      * `grep "HTTP/"`: Filters for lines containing "HTTP/", which usually indicates the status line.
      * `head -n 1`: Takes only the first matching line (in case there are redirects and multiple "HTTP/" lines).
      * `grep "404 Not Found"`: Checks if this line specifically contains "404 Not Found".
      * `> /dev/null`: Discards the output of this `grep` command itself, we only care about its exit status.
  * **`if [ $? -eq 0 ]; then ... fi`**: `$?` holds the exit status of the *last* executed command. If `grep "404 Not Found"` finds a match, its exit status will be `0`, indicating success. If it doesn't find "404 Not Found", its exit status will be `1`.

### How to use:

1.  **Create `urls.txt`**:
    Create a file named `urls.txt` in the same directory as your script. Each URL should be on a new line.
    Example `urls.txt`:

    ```
    https://www.google.com
    https://www.example.com/nonexistent-page-123
    https://www.github.com
    http://httpbin.org/status/404
    ```

2.  **Save the script**:
    Save one of the provided scripts (e.g., `check_urls.sh`).

3.  **Make the script executable**:
    `chmod +x check_urls.sh`

4.  **Run the script**:
    `./check_urls.sh`

After execution, a file named `404_urls.log` will be created in the same directory, listing all URLs that returned a 404 status code.

### Considerations for 1000 URLs:

  * **Rate Limiting**: Be mindful of hitting servers too frequently. If you're checking a lot of URLs on the same domain, you might get temporarily blocked or trigger anti-bot measures. You might consider adding a `sleep` command (e.g., `sleep 0.1` for 100ms delay) inside the loop for very large lists or sensitive servers.
  * **Concurrency**: For a very large number of URLs (e.g., tens of thousands or more), running them sequentially can be slow. You might consider using tools like GNU Parallel or writing a more complex script that processes URLs in batches concurrently. However, for 1000 URLs, a sequential script like these should be reasonably fast.
  * **Error Handling**: The scripts above are basic. For production use, you might want more robust error handling (e.g., what if a URL is malformed, or the DNS lookup fails?). `curl` usually provides more detailed error messages if you remove the `-s` flag or capture `stderr`.
  * **Network Stability**: Ensure a stable internet connection for the duration of the script.
</td></tr></table>

- 實作：
  - 將 Gemini 2.5 Flash 給的 `curl` 版本略做修改，讓 Bash 腳本讀入檔名，並且在判斷不會回傳 404 時，用 `curl` 指令去下載成 `html` 檔案。
- 實測：
  - 1273 筆網址貼文，有 26 筆可能需要 OAuth token 在 LinkedIn 登入狀態下才能讀取。
```bash
~/Downloads/linkedin-feed$ wc 2025-07-21_linkedin-saved-posts-full.txt 
 1273  1273 92929 2025-07-21_linkedin-saved-posts-full.txt
~/Downloads/linkedin-feed$ wc 2025-07-21_404_urls.log 
  26  104 2288 2025-07-21_404_urls.log
```
   - 但實測也發現 1247 筆 curl 可以成功抓取(沒有 `404`)的 html 檔案，有 269 筆是 0 Byte
```bash
~/Downloads/linkedin-feed$ for i in $(find . -size 0 -name "*.html"); do F=$(basename $i); echo "https://www.linkedin.com/feed/update/urn:li:activity:${F//.html}"; done | tee 2025-07-21_fetch_fail.txt 
~/Downloads/linkedin-feed$ wc 2025-07-21_fetch_fail.txt 
  269   269 19637 2025-07-21_fetch_fail.txt
```
- 可能還在查一下，或許是 rate limit，也許是 Authentication 權限問題。