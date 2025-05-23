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

## 2024-12-19

- ( 2024-12-19 16:16:12 )
- 來實驗一下新的 `--watch-files` 參數
```
Aider v0.69.0

     * Watch files improvements:
          + Use # ... AI? comments to trigger aider and ask questions about your code.
          + Now watches all files, not just certain source files.
          + Use # AI comments, // AI comments, or -- AI comments to give aider instructions in any text file.
     * Full support for Gemini Flash 2.0 Exp:
          + aider --model flash or aider --model gemini/gemini-2.0-flash-exp
     * New --multiline flag and /multiline-mode command makes ENTER a soft newline and META-ENTER send the message, by @miradnanali.
     * /copy-context <instructions> now takes optional “instructions” when copying code context to the clipboard.
```
```bash
@jazzwang ➜ /workspaces/snippet/py/aider (master) $ aider --help | grep -i watch
             [--skip-sanity-check-repo] [--watch-files | --no-watch-files]
  --watch-files, --no-watch-files
                        Enable/disable watching files for ai coding comments
                        AIDER_WATCH_FILES]
```
- 說明： https://aider.chat/docs/usage/watch.html
- 實驗：用 `get-readmoo-wishlist.py` 做實驗
```bash
@jazzwang ➜ /workspaces/snippet (master) $ cd py/requests/readmoo-wishlist/
@jazzwang ➜ .../snippet/py/requests/readmoo-wishlist (master) $ code get-readmoo-wishlist.py
@jazzwang ➜ .../snippet/py/requests/readmoo-wishlist (master) $ aider --mini --watch-files get-readmoo-wishlist.py
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Aider v0.69.1
Model: gpt-4o-mini with whole edit format
Git repo: ../../../.git with 1,061 files
Warning: For large repos, consider using --subtree-only and .aiderignore
See: https://aider.chat/docs/faq.html#can-i-use-aider-in-a-large-mono-repo
Repo-map: disabled
Added py/requests/readmoo-wishlist/get-readmoo-wishlist.py to the chat.
Note: in-chat filenames are always relative to the git working dir, not the current working dir.
Cur working dir: /workspaces/snippet/py/requests/readmoo-wishlist
Git working dir: /workspaces/snippet
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
py/requests/readmoo-wishlist/get-readmoo-wishlist.py
> /tokens

Approximate context window usage for gpt-4o-mini, in tokens:

$ 0.0001      542 system messages
$ 0.0001      702 py/requests/readmoo-wishlist/get-readmoo-wishlist.py /drop to remove
==================
$ 0.0002    1,244 tokens total
          126,756 tokens remaining in context window
          128,000 tokens max context window size
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
py/requests/readmoo-wishlist/get-readmoo-wishlist.py
>
... 略 ...
py/requests/readmoo-wishlist/get-readmoo-wishlist.py
>
Processing your request...
```

> The comment you highlighted asks whether the way the code handles the error case is better for readability.
>
> In this context, the code assigns default values to multiple variables in a single line when an `IndexError` occurs. While this approach can be concise, it may reduce readability for some developers, especially those who prefer clarity over brevity.
>
> ### Suggestions for Improved Readability:
> 1. **Separate Assignments**: Instead of assigning multiple variables in one line, you could assign them one by one. This makes it clearer what each variable represents and can be easier to read:
```python
book_category = "已下架"
book_subcategory = "已下架"
book_title = "已下架"
book_price = "0"
readmoo_id = "0"
```
>
> 2. **Commenting**: Adding a comment explaining why these default values are being assigned can also enhance readability. For example:
```python
# Assign default values if book information is not available
```
>
> 3. **Use of Constants**: If "已下架" and "0" are used in multiple places, consider defining them as constants at the top of your file. This way, if you need to change them later, you only have to do it in one place.
>
> In summary, while the current approach is functional, separating the assignments and adding comments can improve readability and maintainability of the code.

## 2025-03-18

- DRAFT! Navigating Large Codebases: Aider's Read-Only Stub Solution
  - https://www.youtube.com/watch?v=XE6v_RGe0-U
  - https://github.com/Aider-AI/aider/pull/3056
- Draft: New /export-context Command for NotebookLM Integration #3476
  - https://github.com/Aider-AI/aider/pull/3476
  - https://www.youtube.com/watch?v=WNdEX9IAbDo 這個影片示範了一個很有趣的概念：把整個龐大的 codebase 轉成 context 切成適當的 chunk 然後餵給 Google NotebookLM
- Aider Integration with Copilot Proxy: Expanding Language Model Access
  - https://www.youtube.com/watch?v=i1I2CAPOXHM
  - 這個應該類似用 liteLLM 來當 OpenAI compatible API 打到 Github Copilot 的公開 Model

## 2025-03-19

- 參考: [sha256sum.md](../../md/linux/sha256sum.md)
- 遇到奇怪的狀況，ollama 0.6.0 以後因為導入 Gemma 3 模型的支援，原本用起來效果不錯，沒動過檔案的 Qwen2.5 Coder 7B 模型突然變笨了，不管問什麼都回答一樣的句子。
- 嘗試降版到 `ollama 0.5.13`，仍舊沒有用。

```markdown
# aider chat started at 2025-03-18 16:56:47

> You can skip this check with --no-gitignore
> Add .aider* to .gitignore (recommended)? (Y)es/(N)o [Yes]: y
> Added .aider* to .gitignore
> C:\Users\jazzw\.local\bin\aider --model ollama/qwen2.5-coder:latest
> Aider v0.77.1
> Model: ollama/qwen2.5-coder:latest with whole edit format
> Git repo: .git with 37 files
> Repo-map: using 4096.0 tokens, auto refresh

#### /add sample_feed.sh
> Added sample_feed.sh to the chat

#### /ask could you draw a sequence diagram of sample_feed.sh using mermaid.js

#### could you draw a sequence diagram of sample_feed.sh using mermaid.js

Great! If you have any questions or need assistance with the code in your Git repository, feel free to ask. I'm here to help!

> Tokens: 634 sent, 29 received.

#### /quit
```

- 後來發現升級 `aider 0.77.1` 以後，隱藏目錄原本只有 `.aider.tags.cache.v3` 現在多了 `.aider.tags.cache.v4`

```bash
jazzw@JazzBook:~/git/sample$ tree .aider.*
.aider.chat.history.md  [error opening dir]
.aider.input.history  [error opening dir]
.aider.tags.cache.v3
├── cache.db
├── cache.db-shm
└── cache.db-wal
.aider.tags.cache.v4
└── cache.db

2 directories, 6 files
```

- 所以找方法降版 `aider`
- 先到 https://pypi.org/project/aider-chat/#history 查版本歷史。
- 我相信這一切跟 Google Gemma 3 有點關係，所以挑 3/12 以前的版本

| Version | Date |
|---------|------|
| 0.76.2 | Mar 12, 2025 |
| 0.76.1 | Mar 11, 2025 |
| 0.76.0 | Mar 10, 2025 |
| 0.75.2 | Mar 5, 2025 |

- ( 2025-03-20 19:37:33 )
- 解法：
  - 根據 aider 安裝的步驟，裡面可以最方便降版的應該是用 `uv`
  - https://aider.chat/docs/install.html#install-with-uv
```bash
jazzw@JazzBook:~/git/snippet$ uv tool install --force --python python3.12 aider-chat@0.75.2
```
  - 用這個指令降版後，確認版號是 `0.75.2`
```bash
jazzw@JazzBook:~/git/sample$ uv tool install --force --python python3.12 aider-chat@0.75.2
Resolved 94 packages in 1.23s
Prepared 19 packages in 11.40s
Uninstalled 22 packages in 1.35s
Installed 19 packages in 660ms
 - aider-chat==0.77.1
 + aider-chat==0.75.2
 - aiohappyeyeballs==2.6.1
 + aiohappyeyeballs==2.4.8
 - aiohttp==3.11.14
 + aiohttp==3.11.13
 - anyio==4.9.0
 + anyio==4.8.0
 - attrs==25.3.0
 + attrs==25.1.0
 - filelock==3.18.0
 + filelock==3.17.0
 - fsspec==2025.3.0
 + fsspec==2025.2.0
 - grep-ast==0.8.1
 + grep-ast==0.6.1
 - huggingface-hub==0.29.3
 + huggingface-hub==0.29.1
 - jinja2==3.1.6
 + jinja2==3.1.5
 - jiter==0.9.0
 + jiter==0.8.2
 - litellm==1.63.11
 + litellm==1.62.1
 - multidict==6.2.0
 + multidict==6.1.0
 - openai==1.66.3
 + openai==1.65.2
 - pillow==11.1.0
 + pillow==10.4.0
 - posthog==3.21.0
 + posthog==3.18.1
 - tokenizers==0.21.1
 + tokenizers==0.19.1
 - tree-sitter==0.24.0
 + tree-sitter==0.21.3
 - tree-sitter-c-sharp==0.23.1
 - tree-sitter-embedded-template==0.23.2
 - tree-sitter-language-pack==0.6.1
 + tree-sitter-languages==1.10.2
 - tree-sitter-yaml==0.7.0
Installed 1 executable: aider.exe
jazzw@JazzBook:~/git/sample$ which aider
/c/Users/jazzw/.local/bin/aider
jazzw@JazzBook:~/git/sample$ aider --version
aider 0.75.2
```
- 一樣的指令 `aider --model ollama/qwen2.5-coder:latest`
```bash
jazzw@JazzBook:~/git/sample$ aider --model ollama/qwen2.5-coder:latest *.sh
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Aider v0.75.2
Model: ollama/qwen2.5-coder:latest with whole edit format
Git repo: .git with 67 files
Repo-map: using 4096.0 tokens, auto refresh
```
- 一樣的 Prompt 就又有跟先前一樣的結果了！
- 結論：
  - 初步我在懷疑 Google Gemma3 因為必須使用特殊的 `Transformers`，而不管是 `ollama` 或 `aider` 社群都在瘋追 `Gemma 3` 模型的支援性，結果就造成了一些其他舊的模型無法正常運作。
  - 當然也可能是改變 repo map 的新做法 (`.aider.tags.cache.v4`?) 造成。

> ### Usage
> 
> Below, there are some code snippets on how to get quickly started with running the model. First, install the Transformers library with the version made for Gemma 3:
> 
> ```
> $ pip install git+https://github.com/huggingface/transformers@v4.49.0-Gemma-3
> ```
>
> Then, copy the snippet from the section that is relevant for your use case.

- ( 2025-03-20 19:45:14 )
- 這個作法看起來可以方便切換不同版本做測試 :)
```bash
jazzw@JazzBook:~/git/snippet$ uv tool install --force --python python3.12 aider-chat@0.76.1
Resolved 97 packages in 1.99s
Prepared 17 packages in 13.81s
Uninstalled 14 packages in 740ms
Installed 17 packages in 575ms
 - aider-chat==0.75.2
 + aider-chat==0.76.1
 - aiohappyeyeballs==2.4.8
 + aiohappyeyeballs==2.5.0
 - fsspec==2025.2.0
 + fsspec==2025.3.0
 - grep-ast==0.6.1
 + grep-ast==0.7.2
 - huggingface-hub==0.29.1
 + huggingface-hub==0.29.2
 - jinja2==3.1.5
 + jinja2==3.1.6
 - jiter==0.8.2
 + jiter==0.9.0
 - litellm==1.62.1
 + litellm==1.63.5
 - openai==1.65.2
 + openai==1.65.5
 - pillow==10.4.0
 + pillow==11.1.0
 - posthog==3.18.1
 + posthog==3.19.1
 - tokenizers==0.19.1
 + tokenizers==0.21.0
 - tree-sitter==0.21.3
 + tree-sitter==0.24.0
 + tree-sitter-c-sharp==0.23.1
 + tree-sitter-embedded-template==0.23.2
 + tree-sitter-language-pack==0.6.0
 - tree-sitter-languages==1.10.2
 + tree-sitter-yaml==0.7.0
Installed 1 executable: aider.exe
jazzw@JazzBook:~/git/snippet$ aider --version
aider 0.76.1
```

## 2025-04-14

- 緣起：在 `scoop update` 時注意到這個專案
- https://github.com/hotovo/aider-desk
  - VS Code extension
    - https://marketplace.visualstudio.com/items?itemName=hotovo-sk.aider-desk-connector

## 2025-04-22

- 紀錄一下 2025-03-15 ~ 2025-03-18 看到的 Aider MCP 相關討論
  - https://github.com/Aider-AI/aider/issues/3314
  - https://www.reddit.com/r/ChatGPTCoding/comments/1hwn6qd/35_sonnet_mcp_aider_complete_game_changer/
  - https://github.com/lutzleonhardt/mcpm-aider/blob/main/docs/MCP.md
  - https://www.youtube.com/watch?v=WNdEX9IAbDo

## 2025-04-26

- 根據 Clean Code 寫的 CONVENTION 規則，讓 Aider 可以生成原始碼時，參考這些原則：
  - https://github.com/Aider-AI/conventions/blob/main/functional-programming/CONVENTIONS.md

## 2025-05-04

- 為了測試最新的 Qwen3，試著安裝最新的 aider 版本。
```bash
jazzw@JazzBook:~$ uv tool install --force --python python3.12 aider-chat
jazzw@JazzBook:~$ uv tool install --force --python python3.12 aider-chat
Uninstalled 1 package in 50ms
Installed 1 package in 89ms
 ~ aider-chat==0.82.2
Installed 1 executable: aider.exe
jazzw@JazzBook:~$ aider --version
aider 0.82.2
```
```markdown
# aider chat started at 2025-05-04 21:53:45

> C:\Users\jazzw\.local\bin\aider --model ollama/qwen3-8b:q4_k_m --no-auto-commits --auto-lint  
> Aider v0.82.2  
> Model: ollama/qwen3-8b:q4_k_m with whole edit format  
> Git repo: .git with 23 files  
> Repo-map: using 4096.0 tokens, auto refresh  
> https://aider.chat/HISTORY.html#release-notes  
> Would you like to see what's new in this version? (Y)es/(N)o [Yes]: y  

#### /ask could you give me a high-level overview of this git repository?  

#### could you give me a high-level overview of this git repository?  

<think>
Okay, the user has a git repository with several Perl files and some shell scripts. They mentioned files like AppointmentGenerator.pm, SalesLogic.pm, and various .sh scripts. My task is to act as an expert code analyst, so I need to be ready to answer questions about the code.

First, I should note that the user might have questions about the structure of the code, specific functionalities, or potential issues. Since they mentioned they're working with me on the code, they might need help understanding how different modules interact, or maybe troubleshooting errors.

The presence of multiple .pm files suggests a modular Perl application, possibly with different components for appointments, sales, services, and logic overrides. The .sh scripts are likely for deployment, data feeding, or recovery processes. The user might be dealing with deployment issues, data processing problems, or integration between Perl modules and shell scripts.

I should be prepared to ask for specific code snippets if needed. For example, if they ask about a particular function in AppointmentLogic.pm, I need to see that file to provide an accurate analysis. Similarly, if they have a question about the Makefile, I should check its contents to understand the build process.

The user might also be looking for best practices, like how to structure their Perl modules, optimize scripts, or handle error recovery. They could be facing issues with dependencies, module loading, or script execution. I need to be ready to guide them through these aspects based on the code they provide.

Since the user hasn't asked a specific question yet, my response should be to prompt them to ask their questions or request specific files if needed. I should make sure to communicate in the same language they're using, which in this case is English. I'll keep the tone helpful and collaborative, encouraging them to provide more details so I can assist effectively.
</think>

I'm ready to help analyze your code! Please ask your questions about the code structure, functionality, or any specific issues you're encountering. If you need me to examine a particular file or compare changes between versions, just let me know and I'll request the necessary files.

> Tokens: 276 sent, 431 received.
```
- 看起來新的 Qwen3 確實類似 DeepSeek R1 一樣，屬於推論模型。再來就是再實測看看程式寫作能力好不好，理論上應該要比 Qwen2.5 Coder 厲害才對。

## 2025-05-08

- 降版 0.76.1 失敗
```bash
~$ uv tool install aider-chat@0.76.1
  × No solution found when resolving dependencies:
  ╰─▶ Because aiohttp==3.11.13 was yanked (reason: Regression: https://github.com/aio-libs/aiohttp/issues/10617) and aider-chat==0.76.1 depends on
      aiohttp==3.11.13, we can conclude that aider-chat==0.76.1 cannot be used.
      And because you require aider-chat==0.76.1, we can conclude that your requirements are unsatisfiable.
```

## 2025-05-09

- 後來一直沒辦法正常安裝 aider-chat，即便用 `uv tool install aider-chat@latest` 還是會卡在 `scipy` 編譯錯誤的問題。感覺是少 Fortran 語言的編譯器，像是 `g95`
- 只好改用 `python -m pip install aider-install`
```
~$ python -m pip install aider-install
Requirement already satisfied: aider-install in c:\users\jazzw\scoop\apps\python\current\lib\site-packages (0.1.3)
Requirement already satisfied: uv>=0.5.0 in c:\users\jazzw\scoop\apps\python\current\lib\site-packages (from aider-install) (0.7.2)
~$ aider-install
Resolved 115 packages in 2.60s
      Built pyperclip==1.9.0
Prepared 115 packages in 1m 22s
Installed 115 packages in 642ms
 + aider-chat==0.82.3
 + aiohappyeyeballs==2.6.1
 + aiohttp==3.11.18
 + aiosignal==1.3.2
 + annotated-types==0.7.0
 + anyio==4.9.0
 + attrs==25.3.0
 + backoff==2.2.1
 + beautifulsoup4==4.13.4
 + cachetools==5.5.2
 + certifi==2025.4.26
 + cffi==1.17.1
 + charset-normalizer==3.4.2
 + click==8.1.8
 + colorama==0.4.6
 + configargparse==1.7
 + diff-match-patch==20241021
 + diskcache==5.6.3
 + distro==1.9.0
 + filelock==3.18.0
 + flake8==7.2.0
 + frozenlist==1.6.0
 + fsspec==2025.3.2
 + gitdb==4.0.12
 + gitpython==3.1.44
 + google-ai-generativelanguage==0.6.15
 + google-api-core==2.24.2
 + google-api-python-client==2.169.0
 + google-auth==2.40.0
 + google-auth-httplib2==0.2.0
 + google-generativeai==0.8.5
 + googleapis-common-protos==1.70.0
 + grep-ast==0.8.1
 + grpcio==1.71.0
 + grpcio-status==1.71.0
 + h11==0.16.0
 + httpcore==1.0.9
 + httplib2==0.22.0
 + httpx==0.28.1
 + huggingface-hub==0.30.2
 + idna==3.10
 + importlib-metadata==7.2.1
 + importlib-resources==6.5.2
 + jinja2==3.1.6
 + jiter==0.9.0
 + json5==0.12.0
 + jsonschema==4.23.0
 + jsonschema-specifications==2025.4.1
 + litellm==1.68.0
 + markdown-it-py==3.0.0
 + markupsafe==3.0.2
 + mccabe==0.7.0
 + mdurl==0.1.2
 + mixpanel==4.10.1
 + multidict==6.4.3
 + networkx==3.2.1
 + numpy==1.26.4
 + openai==1.75.0
 + packaging==24.2
 + pathspec==0.12.1
 + pexpect==4.9.0
 + pillow==11.2.1
 + pip==25.1.1
 + posthog==4.0.1
 + prompt-toolkit==3.0.51
 + propcache==0.3.1
 + proto-plus==1.26.1
 + protobuf==5.29.4
 + psutil==7.0.0
 + ptyprocess==0.7.0
 + pyasn1==0.6.1
 + pyasn1-modules==0.4.2
 + pycodestyle==2.13.0
 + pycparser==2.22
 + pydantic==2.11.4
 + pydantic-core==2.33.2
 + pydub==0.25.1
 + pyflakes==3.3.2
 + pygments==2.19.1
 + pypandoc==1.15
 + pyparsing==3.2.3
 + pyperclip==1.9.0
 + python-dateutil==2.9.0.post0
 + python-dotenv==1.1.0
 + pyyaml==6.0.2
 + referencing==0.36.2
 + regex==2024.11.6
 + requests==2.32.3
 + rich==14.0.0
 + rpds-py==0.24.0
 + rsa==4.9.1
 + scipy==1.13.1
 + six==1.17.0
 + smmap==5.0.2
 + sniffio==1.3.1
 + socksio==1.0.0
 + sounddevice==0.5.1
 + soundfile==0.13.1
 + soupsieve==2.7
 + tiktoken==0.9.0
 + tokenizers==0.21.1
 + tqdm==4.67.1
 + tree-sitter==0.24.0
 + tree-sitter-c-sharp==0.23.1
 + tree-sitter-embedded-template==0.23.2
 + tree-sitter-language-pack==0.7.2
 + tree-sitter-yaml==0.7.0
 + typing-extensions==4.13.2
 + typing-inspection==0.4.0
 + uritemplate==4.1.1
 + urllib3==2.4.0
 + watchfiles==1.0.5
 + wcwidth==0.2.13
 + yarl==1.20.0
 + zipp==3.21.0
Installed 1 executable: aider.exe
Executable directory C:\Users\jazzw\.local\bin is already in PATH
```
- 這樣居然就裝好最新版本的 aider
```bash
~$ uv tool list
aider-chat v0.82.3
- aider.exe
playwright v1.51.0
- playwright.exe
readmoo v0.1.0
- readmoo.exe
webvtt-to-json v0.2
- webvtt-to-json.exe
yt-dlp v2025.3.26
- yt-dlp.exe
```
- 看了一下原始碼 https://github.com/Aider-AI/aider-install/blob/main/aider_install/main.py
- 實際上是執行 `uv tool install --force --python python3.12 aider-chat@latest`
- 那這樣強迫指定舊版呢？
```bash
~$ uv tool install --force --python python3.12 aider-chat@0.76.1
  × No solution found when resolving dependencies:
  ╰─▶ Because aiohttp==3.11.13 was yanked (reason: Regression: https://github.com/aio-libs/aiohttp/issues/10617) and aider-chat==0.76.1 depends on
      aiohttp==3.11.13, we can conclude that aider-chat==0.76.1 cannot be used.
      And because you require aider-chat==0.76.1, we can conclude that your requirements are unsatisfiable.
```
- 還是不行。所以試著用 local 安裝法
```bash
~/git$ git clone git@github.com:Aider-AI/aider.git
~/git$ cd aider
~/git/aider$ git co v0.76.0 -b 0.76.0
~/git/aider$ vi requirements.txt
~/git/aider$ git diff
diff --git a/requirements.txt b/requirements.txt
index c77588a2..e0d8a570 100644
--- a/requirements.txt
+++ b/requirements.txt
@@ -4,7 +4,7 @@ aiohappyeyeballs==2.5.0
     # via
     #   -c requirements/common-constraints.txt
     #   aiohttp
-aiohttp==3.11.13
+aiohttp==3.11.18
     # via
     #   -c requirements/common-constraints.txt
     #   litellm
~/git/aider$ cd ..
~/git$ uv tool install --force --python python3.12 ./aider
```
- 這樣居然就成功了，不過版本怪怪的
```bash
~/git$ uv tool list
aider-chat v0.76.1.dev0+gc838f9bf.d20250509
- aider.exe
~/git$ aider --version
aider 0.76.1.dev0+gc838f9bf.d20250509
```
- 至少這樣要跑 Qwen 2.5 Coder 就不會笨笨的了！