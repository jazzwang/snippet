# aider

> aider is AI pair programming in your terminal

- Website:
  - https://aider.chat/
- Git Repo:
  - https://github.com/Aider-AI/aider

## 2024-11-10

- ( 2024-11-06 22:26:22 )
- 在 [Aider & Cline + Github Models FREE API : AI Coding with GPT-4O for FULLY FREE IS AMAZING!](https://www.youtube.com/watch?v=Y4UuCmZFJZo) 看到 Aider 的運作情形。
- ( 2024-11-10 22:21:36 )
- 或許跟先前測試過的 [CodeStory](https://codestory.ai/) [Aide](https://aide.dev) 名字太相近，所以造成混淆。特別是兩個都有在 [SWE-bench](https://www.swebench.com/) 的 Leaderboard。也算是先前觀察名單裡（e.g. [Aide](https://aide.dev) 跟 [OpenHands](https://github.com/All-Hands-AI/OpenHands)）的一個。
  - https://github.com/Aider-AI/aider-swe-bench

## 2024-11-14

- ( 2024-11-14 14:56:09 )
- 參考：https://aider.chat/docs/llms/gemini.html
- 安裝：
```bash
jazzw@JazzBook:~/git/snippet/python/aider$ gh cs ssh
? Choose codespace: jazzwang/snippet (master*): snippet
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 6.5.0-1025-azure x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro
Last login: Wed Nov 13 16:25:08 2024 from ::1
@jazzwang ➜ /workspaces/snippet (master) $ 
@jazzwang ➜ /workspaces/snippet (master) $ pip3 install -U aider-chat

... 略 ...

Successfully installed aider-chat-0.63.0 anyio-4.6.2.post1 attrs-24.2.0 certifi-2024.8.30 cffi-1.17.1 charset-normalizer-3.4.0 configargparse-1.7 diff-match-patch-20241021 diskcache-5.6.3 filelock-3.16.1 flake8-7.1.1 fsspec-2024.10.0 grep-ast-0.3.3 httpcore-1.0.6 httpx-0.27.2 idna-3.10 importlib-metadata-7.2.1 importlib-resources-6.4.5 jinja2-3.1.4 json5-0.9.25 jsonschema-specifications-2024.10.1 litellm-1.51.2 markupsafe-3.0.2 mccabe-0.7.0 mixpanel-4.10.1 monotonic-1.6 openai-1.53.0 packaging-24.1 pillow-10.4.0 posthog-3.7.0 prompt-toolkit-3.0.48 psutil-6.1.0 pycodestyle-2.12.1 pydub-0.25.1 pyflakes-3.2.0 pygments-2.18.0 pypandoc-1.14 pyperclip-1.9.0 pyyaml-6.0.2 referencing-0.35.1 regex-2024.9.11 rich-13.9.3 rpds-py-0.20.1 scipy-1.13.1 sounddevice-0.5.1 soundfile-0.12.1 soupsieve-2.6 tokenizers-0.19.1 tqdm-4.66.6 tree-sitter-0.21.3 tree-sitter-languages-1.10.2 urllib3-2.2.3
```
- 設定 Gemini API KEY
```bash
@jazzwang ➜ /workspaces/snippet (master) $ export GEMINI_API_KEY="AIza**********xkZtBnE7ihABF**********8A"
@jazzwang ➜ /workspaces/snippet (master) $ cd python/requests/cloudskillsboost/
@jazzwang ➜ .../snippet/python/requests/cloudskillsboost (master) $ aider --model gemini/gemini-1.5-pro-latest dump_transcript.py
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Add .aider*, .env to .gitignore (recommended)? (Y)es/(N)o [Yes]:
Added .aider*, .env to .gitignore
Aider v0.63.0
Model: gemini/gemini-1.5-pro-latest with diff-fenced edit format
Git repo: ../../../.git with 1,010 files
Warning: For large repos, consider using --subtree-only and .aiderignore
See: https://aider.chat/docs/faq.html#can-i-use-aider-in-a-large-mono-repo
Repo-map: using 1024 tokens, auto refresh
Added python/requests/cloudskillsboost/dump_transcript.py to the chat.
Use /help <question> for help, run "aider --help" to see cmd line args
Note: in-chat filenames are always relative to the git working dir, not the current working dir.
Cur working dir: /workspaces/snippet/python/requests/cloudskillsboost
Git working dir: /workspaces/snippet
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
python/requests/cloudskillsboost/dump_transcript.py
>
```
- 實驗是否可以幫忙 code review 昨天寫的 `dump_transcript.py`
```bash
python/requests/cloudskillsboost/dump_transcript.py
> could you do code review of dump_transcript.py?

Initial repo scan can be slow in larger repos, but only happens once.
Scanning repo:   0%|                                                                                                               | 0/1008 [00:00<?, ?it/s]Repo-map can't include /workspaces/snippet/c#/c-sharp-basics
Has it been deleted from the file system but not from git?
Repo-map can't include /workspaces/snippet/go/go-workshop-practical
Has it been deleted from the file system but not from git?
Scanning repo:  59%|██████████████████████████████████████████████████████████▊                                         | 593/1008 [00:01<00:00, 441.75it/s]Repo-map can't include /workspaces/snippet/scala/nyc-taxi-schema/nyc-tlc
Has it been deleted from the file system but not from git?
Scanning repo: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████| 1008/1008 [00:01<00:00, 598.42it/s]

Here's a code review with some improvements for dump_transcript.py:

 1 Add a docstring explaining what the script does.
 2 Use a constant for the base URL.
 3 Use f-strings for URL construction.
 4 Extract transcript extraction logic into a function.
 5 Use a main function to encapsulate the main logic.
 6 Use a more descriptive variable name for the list of transcripts.
 7 Add error handling for HTTP requests.
 8 Add a shebang line.


 python/requests/cloudskillsboost/dump_transcript.py
 <<<<<<< SEARCH
 # coding: utf-8
 import json
 import requests
 from bs4 import BeautifulSoup

 base_url = "https://www.cloudskillsboost.google"
 path_id = 9
 learn_paths = requests.get(base_url + "/paths/" + str(path_id))
 =======
 #!/usr/bin/env python3
 # coding: utf-8
 """Downloads and prints transcripts from Cloud Skills Boost learning paths."""

 import json
 import requests
 from bs4 import BeautifulSoup

 BASE_URL = "https://www.cloudskillsboost.google"

 def extract_transcript(video_url):
     """Extracts the transcript from a given video URL."""
     try:
         response = requests.get(video_url)
         response.raise_for_status()  # Raise an exception for bad status codes
         soup = BeautifulSoup(response.text, "lxml")
         transcript_data = json.loads(soup.find('ql-youtube-video').attrs["transcript"])
         transcript_lines = [item["text"] for item in transcript_data]
         return " ".join(transcript_lines)
     except requests.exceptions.RequestException as e:
         print(f"Error fetching transcript: {e}")
         return None

 def main():
     path_id = 9
     learn_paths_url = f"{BASE_URL}/paths/{path_id}"
     try:
         learn_paths_response = requests.get(learn_paths_url)
         learn_paths_response.raise_for_status()
         soup = BeautifulSoup(learn_paths_response.text, "lxml")
         course_hrefs = soup.find_all('a', {"class": 'activity-link'})
         course_links = [f"{BASE_URL}{url.get('href')}" for url in course_hrefs]

         for course_link in course_links:
             try:
                 course_response = requests.get(course_link)
                 course_response.raise_for_status()
                 outline = json.loads(BeautifulSoup(course_response.text, "lxml").find('ql-course-outline').attrs["modules"])
                 hrefs = []
                 for section in outline:
                     for step in section.get("steps"):
                         hrefs.append(step.get("activities")[0].get("href"))

                 video_urls = [href for href in hrefs if href and 'video' in href]
                 all_transcripts = []
                 for href in video_urls:
                     video_url = f"{BASE_URL}{href}"
                     transcript = extract_transcript(video_url)
                     if transcript:
                         all_transcripts.append(transcript)

                 for transcript in all_transcripts:
                     print(transcript)

             except requests.exceptions.RequestException as e:
                 print(f"Error fetching course: {e}")

     except requests.exceptions.RequestException as e:
         print(f"Error fetching learning paths: {e}")


 if __name__ == "__main__":
     main()
 >>>>>>> REPLACE



 python python/requests/cloudskillsboost/dump_transcript.py



Tokens: 3.6k sent, 693 received. Cost: $0.01 message, $0.01 session.
Applied edit to python/requests/cloudskillsboost/dump_transcript.py
Commit e96a220 refactor: Improve transcript downloader with error handling and functions

# Fix any errors below, if possible.

## Running: /home/codespace/.python/current/bin/python3 -m flake8 --select=E9,F821,F823,F831,F406,F407,F701,F702,F704,F706 --show-source --isolated
python/requests/cloudskillsboost/dump_transcript.py

python/requests/cloudskillsboost/dump_transcript.py:64:30: F821 undefined name 'learn_paths'
course_hrefs = BeautifulSoup(learn_paths.text,"lxml").find_all('a', {"class": 'activity-link'})
                             ^
python/requests/cloudskillsboost/dump_transcript.py:65:18: F821 undefined name 'base_url'
course_links = [ base_url + url.get("href") for url in course_hrefs ]
                 ^

## See relevant lines below marked with █.

python/requests/cloudskillsboost/dump_transcript.py:
...⋮...
 61│
 62│if __name__ == "__main__":
 63│    main()
 64█course_hrefs = BeautifulSoup(learn_paths.text,"lxml").find_all('a', {"class": 'activity-link'})
 65█course_links = [ base_url + url.get("href") for url in course_hrefs ]
 66│for course_link in course_links:
 67│    course = requests.get(course_link)
 68│    outline = json.loads(BeautifulSoup(course.text, "lxml").find('ql-course-outline').attrs["modules"])
...⋮...


Attempt to fix lint errors? (Y)es/(N)o [Yes]:
The errors are because the lines after the if __name__ == "__main__": block are not indented and are using variables (learn_paths, base_url) that are only
defined inside the main function.  Those lines look like they were probably meant to be part of the main function.


 python/requests/cloudskillsboost/dump_transcript.py
 <<<<<<< SEARCH
 if __name__ == "__main__":
     main()
 course_hrefs = BeautifulSoup(learn_paths.text,"lxml").find_all('a', {"class": 'activity-link'})
 course_links = [ base_url + url.get("href") for url in course_hrefs ]
 for course_link in course_links:
     course = requests.get(course_link)
     outline = json.loads(BeautifulSoup(course.text, "lxml").find('ql-course-outline').attrs["modules"])
     hrefs = []
     for section in outline:
         for step in section.get("steps"):
             hrefs.append(step.get("activities")[0].get("href"))

     video_urls = [ href for href in hrefs if href and 'video' in href ]
     for href in video_urls:
         video = requests.get("https://www.cloudskillsboost.google" + href)
         transcripts = json.loads(BeautifulSoup(video.text, "lxml").find('ql-youtube-video').attrs["transcript"])
         srt = [ text["text"] for text in transcripts ]
         print(" ".join(string for string in srt))
 =======
 if __name__ == "__main__":
     main()
 >>>>>>> REPLACE



 python python/requests/cloudskillsboost/dump_transcript.py



Tokens: 5.9k sent, 345 received. Cost: $0.02 message, $0.03 session.
Applied edit to python/requests/cloudskillsboost/dump_transcript.py
Commit 7ce6de0 fix: Correct indentation and variable scoping in main function

python python/requests/cloudskillsboost/dump_transcript.py
Run shell command? (Y)es/(N)o/(D)on't ask again [Yes]:

Running python python/requests/cloudskillsboost/dump_transcript.py
python: can't open file '/workspaces/snippet/python/requests/cloudskillsboost/python/requests/cloudskillsboost/dump_transcript.py': [Errno 2] No such file or directory
Add command output to the chat? (Y)es/(N)o/(D)on't ask again [Yes]:
```
- ( 2024-11-14 15:32:42 )
- 重覆跑了幾次 `aider` 以後，發現它已經幫我 commit 了好幾次
```bash
2024-11-14 15:27 +0800 jazzwang (aider)    o [master] fix: Correct indentation error for all_transcripts initialization
2024-11-14 15:27 +0800 jazzwang (aider)    o refactor: Extract course outline parsing into separate function
2024-11-14 15:19 +0800 jazzwang (aider)    o fix: Remove duplicate code block and logic
2024-11-14 15:15 +0800 jazzwang (aider)    o fix: Add error handling for missing HTML elements
2024-11-14 15:14 +0800 jazzwang            o chore: Update .gitignore to include .aider* and .env
2024-11-14 15:12 +0800 jazzwang (aider)    o feat: Add CLI arguments for path ID and output file
2024-11-14 15:08 +0800 jazzwang (aider)    o fix: Correct indentation and variable scoping in main function
2024-11-14 15:08 +0800 jazzwang (aider)    o refactor: Improve transcript downloader with error handling and functions
2024-11-14 00:24 +0800 jazzwang            o {origin/master} {origin/HEAD} feat: [py][requests] dump_transcript.py - dump cloudskillsboost learning path tra
```
- 心得：
  - 要正確執行，直接在 git repo 的根目錄下 `aider --model gemini/gemini-1.5-pro-latest` 再特別指定要討論的程式碼是那一個。
  - `aider` 有用 `conventional commits` 格式幫我 commit
  - 必須要在花點時間學一下細部的指令 `/code`, `/architect`, `/commit`, `/save` 各別的意義是什麼。
- ( 2024-11-14 16:03:53 )
```bash
@jazzwang ➜ /workspaces/snippet (master) $ aider --model gemini/gemini-1.5-pro-latest
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────Aider v0.63.0
Model: gemini/gemini-1.5-pro-latest with diff-fenced edit format
Git repo: .git with 1,010 files
Warning: For large repos, consider using --subtree-only and .aiderignore
See: https://aider.chat/docs/faq.html#can-i-use-aider-in-a-large-mono-repo
Repo-map: using 1024 tokens, auto refresh
Use /help <question> for help, run "aider --help" to see cmd line args
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────> python/requests/cloudskillsboost/dump_transcript.py

Add python/requests/cloudskillsboost/dump_transcript.py to the chat? (Y)es/(N)o/(D)on't ask again [Yes]:
Repo-map can't include /workspaces/snippet/c#/c-sharp-basics
Has it been deleted from the file system but not from git?
Repo-map can't include /workspaces/snippet/go/go-workshop-practical
Has it been deleted from the file system but not from git?
Repo-map can't include /workspaces/snippet/scala/nyc-taxi-schema/nyc-tlc
Has it been deleted from the file system but not from git?
You have a few minor issues that could be improved in the code.

 1 The transcript field is not always present in the ql-youtube-video element, leading to a KeyError.  We should handle this case gracefully.
 2 There might be cases where the "steps" or "activities" fields are missing in the course outline. The code should handle these cases without raising an
   exception.
 3 The extract_transcript function could be more robust by handling potential JSONDecodeError exceptions.


 python/requests/cloudskillsboost/dump_transcript.py
 <<<<<<< SEARCH
             transcript_data = json.loads(video_element.attrs["transcript"])
             transcript_lines = [item["text"] for item in transcript_data]
             return " ".join(transcript_lines)
 =======
             transcript_data = video_element.attrs.get("transcript")
             if transcript_
                 try:
                     transcript_data = json.loads(transcript_data)
                     transcript_lines = [item["text"] for item in transcript_data]
                     return " ".join(transcript_lines)
                 except json.JSONDecodeError as e:
                     print(f"Error decoding transcript  {e}")
                     return None
             else:
                 print(f"Transcript data not found for {video_url}")
                 return None

 >>>>>>> REPLACE



 python/requests/cloudskillsboost/dump_transcript.py
 <<<<<<< SEARCH
                     for step in section.get("steps", []):
                         for activity in step.get("activities", []):
                             href = activity.get("href")
                             if href:
                                 hrefs.append(href)
 =======
                     for step in section.get("steps", []):  # Handle missing "steps"                                                                                                 for activity in step.get("activities", []): # Handle missing "activities"
                             href = activity.get("href")
                             if href:
                                 hrefs.append(href)
 >>>>>>> REPLACE



 python3 python/requests/cloudskillsboost/dump_transcript.py <path_id>



Tokens: 4.1k sent, 406 received. Cost: $0.01 message, $0.01 session.
The LLM did not conform to the edit format.
https://aider.chat/docs/troubleshooting/edit-errors.html

# 1 SEARCH/REPLACE block failed to match!

## SearchReplaceNoExactMatch: This SEARCH block failed to exactly match lines in python/requests/cloudskillsboost/dump_transcript.py
<<<<<<< SEARCH
                    for step in section.get("steps", []):
                        for activity in step.get("activities", []):
                            href = activity.get("href")
                            if href:
                                hrefs.append(href)
=======
                    for step in section.get("steps", []):  # Handle missing "steps"
                        for activity in step.get("activities", []): # Handle missing "activities"
                            href = activity.get("href")
                            if href:
                                hrefs.append(href)
>>>>>>> REPLACE

Did you mean to match some of these actual lines from python/requests/cloudskillsboost/dump_transcript.py?

```
        if outline_element:
            try:
                outline = json.loads(outline_element.attrs["modules"])
                hrefs = []
                for section in outline:
                    for step in section.get("steps", []):  # Handle missing "steps"
                        for activity in step.get("activities", []): # Handle missing "activities"
                            href = activity.get("href")
                            if href:
                                hrefs.append(href)
                return hrefs
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error processing course outline for {course_link}: {e}")
                return []
        else:
```

Are you sure you need this SEARCH/REPLACE block?
The REPLACE lines are already in python/requests/cloudskillsboost/dump_transcript.py!

The SEARCH section must exactly match an existing block of lines including all white space, comments, indentation, docstrings, etc

# The other 1 SEARCH/REPLACE block were applied successfully.
Don't re-send them.
Just reply with fixed versions of the block above that failed to match.

Commit 86d43ee fix: Handle missing transcript data and JSON decode errors
You are absolutely right! My apologies.  The SEARCH block didn't match the existing code, and the intended changes are already present in the file. There's
no need for the second code block I previously suggested.  I've removed it.


Tokens: 5.0k sent, 51 received. Cost: $0.02 message, $0.03 session.

python3 python/requests/cloudskillsboost/dump_transcript.py <path_id>
Run shell command? (Y)es/(N)o/(D)on't ask again [Yes]:

Running python3 python/requests/cloudskillsboost/dump_transcript.py <path_id>
/bin/bash: -c: line 0: syntax error near unexpected token `newline'
/bin/bash: -c: line 0: `python3 python/requests/cloudskillsboost/dump_transcript.py <path_id>'
Add command output to the chat? (Y)es/(N)o/(D)on't ask again [Yes]:
You can use /undo to undo and discard each aider commit.
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
python/requests/cloudskillsboost/dump_transcript.py
> /diff

Diff since 2632648...
diff --git a/python/requests/cloudskillsboost/dump_transcript.py b/python/requests/cloudskillsboost/dump_transcript.py
index 834bba9..2337238 100644
--- a/python/requests/cloudskillsboost/dump_transcript.py
+++ b/python/requests/cloudskillsboost/dump_transcript.py
@@ -16,9 +16,18 @@ def extract_transcript(video_url):
         soup = BeautifulSoup(response.text, "lxml")
         video_element = soup.find('ql-youtube-video')
         if video_element:
-            transcript_data = json.loads(video_element.attrs["transcript"])
-            transcript_lines = [item["text"] for item in transcript_data]
-            return " ".join(transcript_lines)
+            transcript_data = video_element.attrs.get("transcript")
+            if transcript_
+                try:
+                    transcript_data = json.loads(transcript_data)
+                    transcript_lines = [item["text"] for item in transcript_data]
+                    return " ".join(transcript_lines)
+                except json.JSONDecodeError as e:
+                    print(f"Error decoding transcript  {e}")
+                    return None
+            else:
+                print(f"Transcript data not found for {video_url}")
+                return None
         else:
             return None
     except (requests.exceptions.RequestException, json.JSONDecodeError, KeyError) as e:
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
python/requests/cloudskillsboost/dump_transcript.py
> /quit

@jazzwang ➜ /workspaces/snippet (master) $
```
- 不過很明顯是改錯了，因為 `if transcript_` 這一行應該命名錯誤了。實際跑，果然錯在這一行。下 `/undo` 沒用。只好手動用 `git reset --hard HEAD^` 取消掉這個修改。

## 2024-11-26

- 在 https://www.youtube.com/watch?v=wTzZg7CKLsw 學到 `aider --browser` 的指令。原來還可以在瀏覽器中使用 aider :)
- https://www.youtube.com/watch?v=ag-KxYS8Vuw - 做了一些比較複雜的指令示範。
  - 啟動語法 `aider --no-auto-commits` 可以限制 aider 不要自動 commit
  - 指令 `/tokens` 檢查把檔案加入以後，input token 的量（所以初步猜測 `repository map` 裡面應該是存 embedding）
    - 如果讓 aider 一次把全部的目錄都讀進來，感覺 token total 會有點多。
    - 我挑 `gemini-1.5-pro-latest` 可能也不是最划算的選擇，得算一下性價比，或者同一個 repo 換用 OpenAI API Key 讓它算算看成本。
```
@jazzwang ➜ /workspaces/snippet (master) $ aider --model gemini/gemini-1.5-pro-latest
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Aider v0.64.1
Model: gemini/gemini-1.5-pro-latest with diff-fenced edit format
Git repo: .git with 1,024 files
Warning: For large repos, consider using --subtree-only and .aiderignore
See: https://aider.chat/docs/faq.html#can-i-use-aider-in-a-large-mono-repo
Repo-map: using 1024 tokens, auto refresh
Use /help <question> for help, run "aider --help" to see cmd line args
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
> /tokens

Repo-map can't include /workspaces/snippet/c#/c-sharp-basics
Has it been deleted from the file system but not from git?
Repo-map can't include /workspaces/snippet/go/go-workshop-practical
Has it been deleted from the file system but not from git?
Repo-map can't include /workspaces/snippet/scala/nyc-taxi-schema/nyc-tlc
Has it been deleted from the file system but not from git?
Approximate context window usage for gemini/gemini-1.5-pro-latest, in tokens:

$ 0.0062    1,780 system messages
$ 0.0063    1,813 repository map  use --map-tokens to resize
==================
$ 0.0126    3,593 tokens total
         1,044,983 tokens remaining in context window
         1,048,576 tokens max context window size
```
  - 改用 OpenAI 4o-mini 計算的話，便宜很多：(根據 Aider Leader Board 來說 GPT-4 跟 Claude 的表現還是比較好）
```bash
@jazzwang ➜ /workspaces/snippet (master) $ aider --mini
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Aider v0.64.1
Model: gpt-4o-mini with whole edit format
Git repo: .git with 1,024 files
Warning: For large repos, consider using --subtree-only and .aiderignore
See: https://aider.chat/docs/faq.html#can-i-use-aider-in-a-large-mono-repo
Repo-map: disabled
Use /help <question> for help, run "aider --help" to see cmd line args
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
> /tokens

Approximate context window usage for gpt-4o-mini, in tokens:

$ 0.0001      542 system messages
==================
$ 0.0001      542 tokens total
          127,458 tokens remaining in context window
          128,000 tokens max context window size
```
- 這些示範提醒我該再仔細研究一下 `aider` 的 options -- https://aider.chat/docs/config/options.html

## 2024-11-28

- 繼續專研 `aider` 的一些底層設計。
- 首先，嘗試了解一下 `aider` 的 local cache 機制：
```bash
@jazzwang ➜ /workspaces/snippet (master) $ cd .aider.tags.cache.v3/
@jazzwang ➜ /workspaces/snippet/.aider.tags.cache.v3 (master) $ ls
cache.db
@jazzwang ➜ /workspaces/snippet/.aider.tags.cache.v3 (master) $ sqlite3 cache.db
SQLite version 3.45.3 2024-04-15 13:34:05
Enter ".help" for usage hints.
sqlite> .schema
CREATE TABLE Settings ( key TEXT NOT NULL UNIQUE, value);
CREATE TABLE Cache ( rowid INTEGER PRIMARY KEY, key BLOB, raw INTEGER, store_time REAL, expire_time REAL, access_time REAL, access_count INTEGER DEFAULT 0, tag BLOB, size INTEGER DEFAULT 0, mode INTEGER DEFAULT 0, filename TEXT, value BLOB);
CREATE UNIQUE INDEX Cache_key_raw ON Cache(key, raw);
CREATE INDEX Cache_expire_time ON Cache (expire_time);
CREATE INDEX Cache_store_time ON Cache (store_time);
CREATE TRIGGER Settings_count_insert AFTER INSERT ON Cache FOR EACH ROW BEGIN UPDATE Settings SET value = value + 1 WHERE key = "count"; END;
CREATE TRIGGER Settings_count_delete AFTER DELETE ON Cache FOR EACH ROW BEGIN UPDATE Settings SET value = value - 1 WHERE key = "count"; END;
CREATE TRIGGER Settings_size_insert AFTER INSERT ON Cache FOR EACH ROW BEGIN UPDATE Settings SET value = value + NEW.size WHERE key = "size"; END;
CREATE TRIGGER Settings_size_update AFTER UPDATE ON Cache FOR EACH ROW BEGIN UPDATE Settings SET value = value + NEW.size - OLD.size WHERE key = "size"; END;
CREATE TRIGGER Settings_size_delete AFTER DELETE ON Cache FOR EACH ROW BEGIN UPDATE Settings SET value = value - OLD.size WHERE key = "size"; END;
sqlite> .tables
Cache     Settings
sqlite> .mode table
sqlite> select * from Settings;
+----------------------+-----------------------+
|         key          |         value         |
+----------------------+-----------------------+
| count                | 1031                  |
| size                 | 0                     |
| hits                 | 0                     |
| misses               | 0                     |
| statistics           | 0                     |
| tag_index            | 0                     |
| eviction_policy      | least-recently-stored |
| size_limit           | 1073741824            |
| cull_limit           | 10                    |
| sqlite_auto_vacuum   | 1                     |
| sqlite_cache_size    | 8192                  |
| sqlite_journal_mode  | wal                   |
| sqlite_mmap_size     | 67108864              |
| sqlite_synchronous   | 1                     |
| disk_min_file_size   | 32768                 |
| disk_pickle_protocol | 5                     |
+----------------------+-----------------------+
sqlite> select * from Cache limit 10;
+-------+---------------------------------------------------------+-----+------------------+-------------+------------------+--------------+-----+------+------+----------+-------+
| rowid |                           key                           | raw |    store_time    | expire_time |   access_time    | access_count | tag | size | mode | filename | value |
+-------+---------------------------------------------------------+-----+------------------+-------------+------------------+--------------+-----+------+------+----------+-------+
| 1     | /workspaces/snippet/.devcontainer/devcontainer.json     | 1   | 1731568096.95317 |             | 1731568096.95317 | 0            |     | 0    | 4    |          | □      |
|       |                                                         |     |                  |             |                  |              |     |      |      |          | □      |
+-------+---------------------------------------------------------+-----+------------------+-------------+------------------+--------------+-----+------+------+----------+-------+
| 2     | /workspaces/snippet/.gitallowed                         | 1   | 1731568096.96604 |             | 1731568096.96604 | 0            |     | 0    | 4    |          | □      |
|       |                                                         |     |                  |             |                  |              |     |      |      |          | □      |
+-------+---------------------------------------------------------+-----+------------------+-------------+------------------+--------------+-----+------+------+----------+-------+
| 3     | /workspaces/snippet/.gitattributes                      | 1   | 1731568096.96638 |             | 1731568096.96638 | 0            |     | 0    | 4    |          | □      |
|       |                                                         |     |                  |             |                  |              |     |      |      |          | □      |
+-------+---------------------------------------------------------+-----+------------------+-------------+------------------+--------------+-----+------+------+----------+-------+
| 4     | /workspaces/snippet/.github/workflows/git-extras.yml    | 1   | 1731568096.96698 |             | 1731568096.96698 | 0            |     | 0    | 4    |          | □      |
|       |                                                         |     |                  |             |                  |              |     |      |      |          | □      |
+-------+---------------------------------------------------------+-----+------------------+-------------+------------------+--------------+-----+------+------+----------+-------+
| 5     | /workspaces/snippet/.github/workflows/manual.yml        | 1   | 1731568096.96725 |             | 1731568096.96725 | 0            |     | 0    | 4    |          | □      |
|       |                                                         |     |                  |             |                  |              |     |      |      |          | □      |
+-------+---------------------------------------------------------+-----+------------------+-------------+------------------+--------------+-----+------+------+----------+-------+
| 6     | /workspaces/snippet/.github/workflows/mtr-win64.yml     | 1   | 1731568096.96751 |             | 1731568096.96751 | 0            |     | 0    | 4    |          | □      |
|       |                                                         |     |                  |             |                  |              |     |      |      |          | □      |
+-------+---------------------------------------------------------+-----+------------------+-------------+------------------+--------------+-----+------+------+----------+-------+
| 7     | /workspaces/snippet/.github/workflows/pip-package.yml   | 1   | 1731568096.96778 |             | 1731568096.96778 | 0            |     | 0    | 4    |          | □      |
|       |                                                         |     |                  |             |                  |              |     |      |      |          | □      |
+-------+---------------------------------------------------------+-----+------------------+-------------+------------------+--------------+-----+------+------+----------+-------+
| 8     | /workspaces/snippet/.github/workflows/plow-win64.yml    | 1   | 1731568096.96805 |             | 1731568096.96805 | 0            |     | 0    | 4    |          | □      |
|       |                                                         |     |                  |             |                  |              |     |      |      |          | □      |
+-------+---------------------------------------------------------+-----+------------------+-------------+------------------+--------------+-----+------+------+----------+-------+
| 9     | /workspaces/snippet/.github/workflows/scoop-package.yml | 1   | 1731568096.96831 |             | 1731568096.96831 | 0            |     | 0    | 4    |          | □      |
|       |                                                         |     |                  |             |                  |              |     |      |      |          | □      |
+-------+---------------------------------------------------------+-----+------------------+-------------+------------------+--------------+-----+------+------+----------+-------+
| 10    | /workspaces/snippet/.github/workflows/screenshot.yml    | 1   | 1731568096.96858 |             | 1731568096.96858 | 0            |     | 0    | 4    |          | □      |
|       |                                                         |     |                  |             |                  |              |     |      |      |          | □      |
+-------+---------------------------------------------------------+-----+------------------+-------------+------------------+--------------+-----+------+------+----------+-------+
sqlite> .exit
@jazzwang ➜ /workspaces/snippet/.aider.tags.cache.v3 (master) $ cd ..
@jazzwang ➜ /workspaces/snippet (master) $
```

## 2024-12-02

```bash
@jazzwang ➜ /workspaces/snippet (master) $ aider
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Aider v0.66.0
Main model: claude-3-5-sonnet-20241022 with diff edit format, infinite output
Weak model: claude-3-5-haiku-20241022
Git repo: .git with 1,029 files
Warning: For large repos, consider using --subtree-only and .aiderignore
See: https://aider.chat/docs/faq.html#can-i-use-aider-in-a-large-mono-repo
Repo-map: using 1024 tokens, auto refresh


https://aider.chat/HISTORY.html#release-notes
Would you like to see what's new in this version? (Y)es/(N)o [Yes]:
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
> /tokens

Repo-map can't include /workspaces/snippet/c#/c-sharp-basics
Has it been deleted from the file system but not from git?
Repo-map can't include /workspaces/snippet/go/go-workshop-practical
Has it been deleted from the file system but not from git?
Repo-map can't include /workspaces/snippet/scala/nyc-taxi-schema/nyc-tlc
Has it been deleted from the file system but not from git?

Approximate context window usage for claude-3-5-sonnet-20241022, in tokens:

$ 0.0053    1,780 system messages
$ 0.0054    1,816 repository map  use --map-tokens to resize
==================
$ 0.0108    3,596 tokens total
          196,404 tokens remaining in context window
          200,000 tokens max context window size
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
> /quit
```
