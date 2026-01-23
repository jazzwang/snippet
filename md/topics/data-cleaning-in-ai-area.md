# Data Cleaning Challenges in GenAI Era

## 2026-01-21

- 緣起：因為想要分析 Jira User Story 並根據語意進行分群，所以用 `jira-select run-query` 下載了 JSON 格式的結果當作 Latent Scope 拿來分群用的 Dataset
- 痛點：一開始沒特別注意，使用 Jira Web UI 匯出成 CSV 或 Excel 檔案，但不管怎麼整理，就是會遇到 charmap 的錯誤訊息
  - 例如：`UnicodeEncodeError: 'charmap' codec can't encode character '\U0001f917' in position 27: character maps to <undefined>`
```py
embedding 346 sentences in 3 batches
0%|          | 0/3 [00:00<?, ?it/s]
33%|███▎      | 1/3 [00:10<00:20, 10.40s/it]
67%|██████▋   | 2/3 [00:22<00:11, 11.21s/it]
100%|██████████| 3/3 [00:33<00:00, 11.42s/it]
4it [00:39,  9.25s/it]
4it [00:39,  9.94s/it]
Traceback (most recent call last):
File "<frozen runpy>", line 198, in _run_module_as_main
File "<frozen runpy>", line 88, in _run_code
File "C:\Users\jazzw\.local\bin\ls-embed.exe\__main__.py", line 10, in <module>
File "C:\Users\jazzw\AppData\Roaming\uv\tools\latentscope\Lib\site-packages\latentscope\scripts\embed.py", line 63, in main
embed(args.dataset_id, args.text_column, args.model_id, args.prefix, args.rerun, args.dimensions, args.batch_size, args.max_seq_length)
File "C:\Users\jazzw\AppData\Roaming\uv\tools\latentscope\Lib\site-packages\latentscope\scripts\embed.py", line 153, in embed
history_file.write(f"{datetime.now().isoformat()},{model_id}\n")
File "C:\Users\jazzw\scoop\apps\python\current\Lib\encodings\cp1252.py", line 19, in encode
return codecs.charmap_encode(input,self.errors,encoding_table)[0]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
UnicodeEncodeError: 'charmap' codec can't encode character '\U0001f917' in position 27: character maps to <undefined>
```

- 改用 `jira-select run-query` 以後，發現確實有很多 `\u` 開頭的特殊字元
- 在高鐵上網路不順，索性就靠 local 的 Ollama Qwen 2.5 Coder 7B 模型來了解這些特殊字元到底是什麼
  - 經調查，才知道是 emoji 或特殊 unicode 字元。
  - 回過頭比對 Jira 匯出的 Excel 裡面，確實包含這些特殊字元
- 關鍵洞察 Key Takeaway：
  - 2024 以後，開始有些人把 ChatGPT 或 M365 Copilot 生成的內容貼到 User Story 的 Description ，
    當然裡面就會藏了一些 emoji 或 unicode ( 像是"箭頭"或"加總"等符號 )
  - 這讓清洗跟分析一些 LinkedIn 貼文或 Jira / Confluence 等內容變得更困難了

```bash
~/Downloads$ ollama run qwen25-coder:7b
```

>>> what is "\u0394"?

"\u0394" represents the Greek letter Delta (Δ), which is used in various mathematical and scientific contexts. It can denote a change or difference
between two values, as well as being part of mathematical equations and formulas. Additionally, it's sometimes used to represent a triangular shape.

>>> what is "\u3001"?

"\u3001" represents the Chinese comma (，), also known as the "full-width comma" or "ideographic comma." It is used in modern written Chinese,
Japanese, and Korean to separate elements in a sentence without starting a new clause. Unlike the English comma, which typically acts as a pause or a
separation of ideas, the Chinese comma serves more like a slight pause between items in a list or before conjunctions in compound sentences.

>>> what is "\u2192"?

"\u2192" represents the rightwards arrow (→). This symbol is commonly used in various contexts:

1. **Mathematics and Logic**: It indicates a direction of implication or causation.

   Example: \( A \rightarrow B \) means "if A, then B."

2. **Computer Science and Programming**: It can denote a pointer or reference to an object.

3. **Chemistry**: Sometimes used in chemical equations to indicate the direction of a reaction.

4. **General Communication**: Used to indicate direction, progress, or movement towards something.

The arrow points from the left (origin) to the right (destination), which is why it's called a "rightwards" arrow.

>>> what is "\u2013"?

"\u2013" represents an em dash (—). This symbol is used in various contexts, such as:

1. **Emphasis**: To emphasize a point or break up a sentence.

   Example: I'm not sure if this was the best decision—maybe we should reconsider.

2. **Lists and Series**: In some styles of writing, em dashes can be used to introduce items in a series or list.

3. **Long Pauses**: To indicate long pauses or breaks in speech when transcribing dialogue.

4. **Subordinate Clauses**: Sometimes used before subordinate clauses to provide additional information.

The em dash is typically longer than the en dash (–) and is often used for its stronger break between ideas or a more emphatic pause than an ordinary
comma provides.

>>> what is "\u03a3"?

"\u03a3" represents the Greek capital letter Sigma (Σ). The sigma symbol is widely used in mathematics, particularly in summation notation. It
indicates that a series of values are to be added together.

For example:
\[ \sum_{i=1}^{n} i = 1 + 2 + 3 + \ldots + n \]

Here, the sigma (Σ) tells you to sum the values of \(i\) from 1 to \(n\).

Sigma is also used in other contexts such as in physics and engineering, where it can represent various concepts.

>>> what is "\ud83d"?

"\ud83d" is a high surrogate code point in the UTF-16 encoding scheme, which is often used to represent Unicode characters that require two 16-bit
units (surrogates) for their representation.

UTF-16 uses a system of variable-length encodings. For most Unicode characters, it uses one 16-bit unit (a code unit), but some characters use two
code units. The high surrogate is always in the range U+D800 to U+DBFF, and the low surrogate follows it and is in the range U+DC00 to U+DFFF.

If you see "\ud83d" alone, it's not a complete character; it needs to be followed by a low surrogate to form a valid UTF-16 code point. For example,
"\ud83d\udd25" represents the Unicode character for "white heart eye emoji."

To properly decode and display Unicode characters using UTF-16, you need both the high and low surrogates or the full 32-bit Unicode scalar value if
it fits into one code unit.

>>> what is "\ud83d\udd0d"?

"\ud83d\udd0d" represents a single Unicode character, which is the "heavy check mark emoji" (✅). This emoji is used to indicate approval or
confirmation. Here's how it looks when rendered:

✅

>>> what is "\ud83d\udea8"?

"\ud83d\udea8" represents a single Unicode character, which is the "thinking face emoji" (🤔). This emoji is used to indicate someone who is thinking
or in contemplation. Here's how it looks when rendered:

🤔

>>> what is "\u274c"?

"\u274c" represents a single Unicode character, which is the "cross mark" (❌). This emoji is used to indicate cancellation, rejection, or an error.
Here's how it looks when rendered:

❌

>>> what is "\ud83d\udcca"?

"\ud83d\udcca" represents a single Unicode character, which is the "crossed flags emoji" (🎌). This emoji typically depicts two crossed flags, often
used to represent nations or events. Here's how it looks when rendered:

🎌

>>> what is "\ud83d\udd0e"?

"\ud83d\udd0e" represents a single Unicode character, which is the "white heavy check mark emoji" (✔️). This emoji is used to indicate approval or
confirmation. Here's how it looks when rendered:

✔️

>>> what is "\u200b"?

"\u200b" represents a zero-width space (ZWSP) in Unicode. It is an invisible space that takes up no width and is used to separate characters or words
without creating visible spaces. ZWSPs are often used in text processing to control word breaks or to avoid certain types of rendering issues.

For example, two letters can be separated by a zero-width space like this: "H\u200bW" which will appear as "HW" without any visible space between the
'H' and 'W'.

ZWSPs are not usually visible to the human eye but can have significant effects on how text is processed in computing environments.

>>> what is "\u2019"?

"\u2019" represents a single Unicode character, which is the right single quotation mark (’). This symbol is used to denote the end of a direct speech
or thought within a sentence. Here's how it looks when rendered:

’

>>> what is "\u2753"?

"\u2753" represents a single Unicode character, which is the "envelope with upper half orange peel emoji" (📩). This emoji typically depicts an
envelope with one side colored orange and the other side white, often used to represent communication or notification. Here's how it looks when
rendered:

📩

>>> what is "\ud83d\udd17"?

"\ud83d\udd17" represents a single Unicode character, which is the "left-pointing magnifying glass emoji" (🔍). This emoji is used to indicate that
something is being searched for or investigated. Here's how it looks when rendered:

🔍

>>> what is "\ud83d\udcce"?
"\ud83d\udcce" represents a single Unicode character, which is the "lightning bolt with rounded sides emoji" (⚡️). This emoji depicts a lightning
bolt with smooth edges and is used to indicate something energetic, fast, or powerful. Here's how it looks when rendered:

⚡️

>>> what is "\u201c"?

"\u201c" represents a single Unicode character, which is the left double quotation mark (”).

This symbol is used to denote the beginning of a direct speech or thought within a sentence. Here's how it looks when rendered:

”

>>> what is "\u201d"?

"\u201d" represents a single Unicode character, which is the right double quotation mark (“).

This symbol is used to denote the end of a direct speech or thought within a sentence. Here's how it looks when rendered:

“

>>> what is "\u202f"?

"\u202f" represents a single Unicode character, which is the narrow no-break space (ＮＢＳ). This is an invisible space that does not break between
words, unlike regular spaces. It is often used to prevent line breaks in certain contexts where a space is required but should not allow wrapping.

For example:
```
Hello\u202fWorld
```
This will render as "Hello World" without any visible space between "Hello" and "World".

Narrow no-break spaces are useful in situations where precise spacing is critical, such as in URLs or technical text.

>>> what is "\u2260"?

"\u2260" represents a single Unicode character, which is the "not equal to" symbol (≠). This symbol is used to indicate that two values are not equal.
Here's how it looks when rendered:

≠

>>> what is "\ud83e\udde0"?

"\ud83e\udde0" represents a single Unicode character, which is the "face with rolling eyes emoji" (🙄). This emoji depicts a face with closed eyes and
a mouth that is forming an 'O', often used to indicate disbelief or frustration. Here's how it looks when rendered:

🙄

>>> what is "\u2611"?

"\u2611" represents a single Unicode character, which is the "check box with check mark emoji" (✔️). This symbol is used to indicate approval or
confirmation. Here's how it looks when rendered:

✔️

-----

以下是一些跟 Gemini 討論怎麼解決 Charmap 錯誤的紀錄：
<table>
<tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
how can I troubleshoot unicode decode error using `vi` ? 
here is the python error: 

```python
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa0 in position 193: invalid start byte
```

</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->

Dealing with a `UnicodeDecodeError` in Python usually means your file contains a character that doesn't belong in the encoding Python is expecting (UTF-8). The byte `0xa0` is a classic culprit—it's often a **non-breaking space** from a copy-paste job.

Here is how you can use `vi` (or `vim`) to find and fix that specific byte.

---

### 1. Highlight Non-ASCII Characters

The easiest way to find the "invisible" culprit is to tell `vi` to highlight any character that isn't part of the standard ASCII set.

1. Open your file: `vi your_script.py`
2. Enter command mode by typing `:`
3. Run the following command:

```vim
/ [^\x00-\x7f]
```


*This tells `vi` to search for any character **not** in the range of hex 00 to 7F.*

---

### 2. Locate the Exact Position

Since your error message gave you a specific location (position 193), you can jump to that approximate area.

* **Go to the line:** If you know the line number, type `:193` followed by `Enter`.
* **Show byte position:** You can check exactly where you are in the file by pressing `ga`.
* Look at the bottom of the screen. `vi` will show the decimal, hex, and octal value of the character under the cursor.
* Look for a character that displays something like `<a0>`.



---

### 3. Use "List" Mode to See Hidden Characters

You can force `vi` to show characters that are usually invisible (like trailing spaces or non-breaking spaces).

1. Type `:set list`
2. Non-breaking spaces often show up as `~` or a highlighted space depending on your colorscheme.
3. To turn it off later, type `:set nolist`.

---

### 4. Search and Destroy (The Fix)

If you want to find that specific `0xa0` byte and replace it with a standard space, you can use a search and replace command:

```vim
:%s/\%u00a0/ /g

```

* `%s`: Search the whole file.
* `\%u00a0`: This is the Vim syntax for the Unicode character `U+00A0` (the byte `0xa0`).
* `/ /g`: Replace it with a regular space globally.

---

### Summary of Useful `vi` Commands

| Command | Action |
| --- | --- |
| `ga` | Display the ASCII/Hex value of the character under the cursor. |
| `:set list` | Show hidden/special characters visually. |
| `/[^\x00-\x7f]` | Search for the next non-ASCII character. |
| `:%s/[^\x00-\x7f]//g` | **Extreme measure:** Delete every non-ASCII character in the file. |

---

**Would you like me to show you how to configure your `.vimrc` so that these "bad" characters are always highlighted in red whenever you open a file?**

</td></tr>
<tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
help me to resolve this error:
```
UnicodeEncodeError: 'charmap' codec can't encode character '\U0001f917' in position 27: character maps to <undefined>
```
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->

This error is the opposite of your previous one. While a `DecodeError` happens when **reading** a file, a `UnicodeEncodeError` happens when Python tries to **write or print** a character that the destination (your terminal, a file, or a Windows pipe) doesn't understand.

The character `\U0001f917` is the **"Hugging Face" emoji (🤗)**. The `'charmap'` codec error usually occurs on Windows because the default system encoding (often `cp1252`) cannot handle emojis.

---

### Solution 1: Force UTF-8 Encoding in Code

If you are writing to a file, you must explicitly tell Python to use `utf-8` instead of letting it guess the system default.

**Change this:**

```python
with open('output.txt', 'w') as f:
    f.write(my_string)
```

**To this:**

```python
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(my_string)
```

---

### Solution 2: Fix the Terminal Environment

If the error happens when you `print()`, your terminal environment isn't identifying itself as UTF-8 compatible. You can override this by setting an environment variable in your shell **before** running your script.

**On Windows (PowerShell):**

```powershell
$env:PYTHONIOENCODING='utf-8'
python your_script.py
```

**On Windows (Command Prompt):**

```cmd
set PYTHONIOENCODING=utf8
python your_script.py
```

---

### Solution 3: The "Ignore" or "Replace" Strategy

If you don't actually care about the emoji and just want the script to stop crashing, you can tell Python how to handle characters it can't encode.

```python
# Re-encode the string, dropping characters that aren't supported
clean_string = my_string.encode('ascii', 'ignore').decode('ascii')
print(clean_string)

# Or replace them with a placeholder like '?'
print(my_string.encode('cp1252', errors='replace').decode('cp1252'))
```

---

### How to find this in `vi`

If that emoji is hard-coded in your Python script and you want to find it using `vi`:

1. Open the file: `vi your_script.py`
2. Search for non-standard characters:

  ```vim
  /[^\x00-\x7f]
  ```

3. Once found, you can delete it or replace it with a text-based version like `":hugging_face:"`.

---

### Why this happens (The Logic)

Python 3 uses Unicode for all strings internally. However, when those strings leave the Python environment (to a disk or a screen), they must be converted into **bytes**. If the "map" (codec) chosen for that conversion doesn't have a slot for a specific emoji, it panics and throws this error.

**Would you like me to show you how to update your Python environment globally so you don't have to set these variables every time?**

</td></tr>
</table>