# Data Cleaning Challenges in GenAI Era

## 2026-01-21

- 緣起：因為想要分析 Jira User Story 並根據語意進行分群，所以用 `jira-select run-query` 下載了 JSON 格式的結果當作 Latent Scope 拿來分群用的 Dataset
- 痛點：一開始沒特別注意，使用 Jira Web UI 匯出成 CSV 或 Excel 檔案，但不管怎麼整理，就是會遇到 charmap 的錯誤訊息
```
```
- 改用 `jira-select run-query` 以後，發現確實有很多 emoji 或特殊 unicode 字元
- 在高鐵上網路不順，索性就靠 local 的 Ollama Qwen 2.5 Coder 7B 模型來了解這些特殊字元到底是什麼
- 關鍵洞察 Key Takeaway：
  - 2024 以後，開始有些人把 ChatGPT 或 M365 Copilot 生成的內容貼到 User Story 的 Description ，
    當然裡面就會藏了一些 emoji 或 unicode (像是"箭頭"或"加總"等符號）
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

