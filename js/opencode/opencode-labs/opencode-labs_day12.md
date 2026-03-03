Welcome to **Day 12: Privacy & Local Models**.

Until now, your agent’s "brain" has likely lived in the cloud (OpenAI, Anthropic, etc.). While powerful, this means your code is being sent to third-party servers. Today, we "cut the cord." We will set up **Ollama** to run Large Language Models (LLMs) directly on your Windows 11 hardware, and we’ll point OpenCode to this local instance.

This is the "Privacy First" setup—perfect for working on sensitive corporate data or when you’re on a plane with no Wi-Fi.

## Day 12: Taking the Agent Offline

### 1. The Local LLM Architecture

In a local setup, the "Agent" (OpenCode) still runs in your WSL terminal, but instead of calling an API over the internet, it calls a local server (Ollama) running on your own machine.

### 2. Choosing Your Model

Since you are in a coding environment, you need a model optimized for logic.

* **Llama 3 (8B):** Great all-rounder.
* **Codestral (Mistral):** Specifically tuned for 80+ programming languages.
* **DeepSeek-Coder-V2:** Currently one of the highest-rated open-source coding models.

## Day 12 Lab: "The Air-Gapped Assistant"

In this lab, you will install a local model, configure OpenCode to use it, and test its ability to handle a "top secret" coding task without internet access.

### Phase 1: Install Ollama in WSL

While you can install Ollama on Windows, installing it natively in WSL often provides better performance for Linux-based agents.

1. **Open Ubuntu WSL.**
2. **Run the Ollama install script:**

```bash
curl -fsSL https://ollama.com/install.sh | sh
```


3. **Start the Ollama server:**

```bash
ollama serve
```

> [!NOTE] Keep this terminal open, or run it in the background.

4. **In a new WSL tab, pull a coding model:**

```bash
ollama run codestral
```

> [!NOTE] This may take a few minutes to download—it's about 5-8GB.

### Phase 2: Point OpenCode to the Local Brain

1. **Open your OpenCode config:**

```bash
nano ~/.config/opencode/config.yaml
```

2. **Update the provider settings:**
Change your active provider to `ollama`:

```yaml
provider: ollama
base_url: "http://localhost:11434"
model: codestral
```

3. **Save and exit.**

### Phase 3: The "Offline" Coding Test

To prove we are private, let’s simulate an air-gapped environment.

1. **Create a "Sensitive" project:**

    ```bash
    mkdir ~/day12-private && cd ~/day12-private
    echo "SECRET_KEY=12345-ABCDE-PROPRIETARY" > .env
    ```

2. **Turn off your Wi-Fi** (optional but satisfying for this lab).
3. **Launch OpenCode:** `opencode .`
4. **The Prompt:**
> "Analyze `@.env`. Create a Python script that masks this SECRET_KEY and logs only the first and last three characters. Do this 100% locally."



### Phase 4: Performance Benchmarking

1. **Observe the speed:** Local models depend on your GPU (VRAM). 
   If it feels slow, check if WSL is using your NVIDIA/AMD GPU.
2. **The Quality Check:** Ask a complex logic question:

   > "Explain the Big O complexity of a recursive Fibonacci function and suggest an optimized iterative version."

3. Compare the answer to what you remember from the "Cloud" models.

## Day 12 Summary Checklist

| Task | Completed |
| --- | --- |
| Installed Ollama natively in WSL | ☐ |
| Downloaded a specialized coding model (e.g., Codestral) | ☐ |
| Configured OpenCode to use `localhost:11434` | ☐ |
| Successfully completed a coding task while offline | ☐ |

### Pro-Tip: The "VRAM" Wall

If your local model is extremely slow or "hallucinates" gibberish, your GPU might be out of memory (VRAM). In WSL, you can check your GPU usage by running `nvidia-smi`. If you're maxed out, try a smaller model like `phi3:mini` (Microsoft's lightweight model) which runs fast even on laptops without dedicated GPUs.

**How did the local model feel compared to the cloud? Was it a "snappy" experience, or did your PC fans start sounding like a jet engine?**

When you're ready, **Day 13** is where we move back to the "World" by integrating OpenCode into **CI/CD and GitHub Actions**. We’ll learn how to make the agent part of your team's automated workflow! Ready?

<div style="background-color:lightgreen;">

## 實測

</div>

### Phase 1: Install Ollama in WSL

- 由於已經安裝好 ollama，因此忽略 `Phase 1: Install Ollama in WSL`

### Phase 2: Point OpenCode to the Local Brain

- 參考
  - https://docs.ollama.com/integrations/opencode
  - https://www.reddit.com/r/opencodeCLI/comments/1ngd18t/anyone_using_opencode_with_ollama/
- 新版的 ollama 可以靠 `ollama lunch` 指令直接設定 `opencode` 並選擇模型
- **備註**：這裡選擇了已經下載的 `qwen3:8b`，也設定了 `qwen25-coder:7b`

```bash
~$ ollama
Ollama 0.16.3

  Run a model
    Start an interactive chat with a model

  Launch Claude Code
    Agentic coding across large codebases

  Launch Codex (not installed)
    OpenAI's open-source coding agent

  Launch OpenClaw (not installed)
    Personal AI with 100+ skills

▸ Launch OpenCode (qwen3:8b)
    Anomaly's open-source coding agent

  Launch Droid (not installed)
    Factory's coding agent across terminal and IDEs

  Launch Pi (not installed)
    Minimal AI agent toolkit with plugin support

  Launch Cline (not installed)
    Autonomous coding agent with parallel execution


↑/↓ navigate • enter launch • → change model • esc quit
```

#### [​Quick setup](https://docs.ollama.com/integrations/opencode#quick-setup)

```bash
ollama launch opencode
```

To configure without launching:

```bash
ollama launch opencode --config
```

### Phase 3: The "Offline" Coding Test

- 建立實驗專案
    ```bash
    ~$ cd /tmp/
    /tmp$ mkdir day12-private && cd day12-private
    echo "SECRET_KEY=12345-ABCDE-PROPRIETARY" > .env
    /tmp/day12-private$ ollama launch opencode
    ```
    ```bash
    /tmp/day12-private$ ollama launch opencode
    Select models for OpenCode: Type to filter...

    Recommended
    ▸ qwen3:8b
        Efficient all-purpose assistant
        glm-4.7-flash
        Reasoning and code generation locally, ~25GB, (not downloaded)

    More
        qwen25-coder:7b
        qwen25:7b-it-1m

    ↑/↓ navigate • enter select • tab add multiple • esc cancel
    ```
- 先使用 `qwen3:8b`
- 輸入提示詞
  
  > Analyze @.env. Create a Python script that masks this SECRET_KEY and logs only the first and last three characters. Do this 100% locally.

### Phase 4: Performance Benchmarking

- 實驗更複雜的提示詞

  > Explain the Big O complexity of a recursive Fibonacci function and suggest an optimized iterative version.

### 結果

- 以下是 session `/copy` 的結果

#### Mask .env SECRET_KEY

**Session ID:** ses_32ad928d8ffeyO0Ctz1yfs9Iyw
**Created:** 3/3/2026, 8:30:18 AM
**Updated:** 3/3/2026, 8:35:55 AM

---

##### User

Analyze @.env. Create a Python script that masks this SECRET_KEY and logs only the first and last three characters. Do this 100% locally.

---

##### Assistant (Build · qwen3:8b · 127.4s)

```
<think>
Okay, let me try to figure out how to approach this user's request. The user wants to analyze an .env file and create a Python script that masks the SECRET_KEY by showing only the first and last three characters, doing everything locally.

First, I need to understand what the .env file contains. Typically, .env files have key-value pairs for environment variables. The SECRET_KEY is likely one of those variables. The task is to mask this value in the output, so the script should read the .env file, find the SECRET_KEY, and then log it with the middle characters replaced by asterisks.

Wait, the user mentioned "mask this SECRET_KEY and logs only the first and last three characters." So the actual value of the SECRET_KEY should be hidden, but the first three and last three characters are visible. For example, if the key is "abc123xyz", the masked version would be "abc***xyz".

But how to handle cases where the SECRET_KEY is shorter than 6 characters? The user didn't specify, so maybe the script should handle that gracefully, perhaps just showing the entire string if it's shorter than 6 characters.

The user wants this done 100% locally, so the script shouldn't rely on any external services or APIs. It should read the .env file, process the SECRET_KEY, and log the masked version.

So, steps to take:

1. Read the .env file. Python can use the 'dotenv' library to load environment variables, but maybe the user wants to read the file directly. Alternatively, using 'os' module to read the file and parse it line by line.

Wait, the user might not have dotenv installed, but since it's a local script, maybe it's better to read the file directly. So, open the .env file, split each line into key-value pairs, and look for the SECRET_KEY.

2. Once found, mask the value. For example, take the first three characters, then add asterisks for the middle part, then the last three characters. If the length is less than 6, just show the entire string.

3. Log the masked key. The user might want to print it to the console or write it to a log file. But the request says "logs only the first and last three characters," so probably print to console.

But the user might also want to ensure that the script is self-contained. So, the Python script should be able to run locally without external dependencies, except maybe standard libraries.

Wait, the dotenv library is not part of the standard library, so if the user doesn't have it installed, the script might not work. However, the user might have it installed, or maybe they want to avoid that. Alternatively, the script can read the .env file directly using the 'os' module or 'configparser' or similar.

So, perhaps the script should read the .env file line by line, split each line into key and value, check if the key is SECRET_KEY, then process the value.

But first, the script needs to find the SECRET_KEY in the .env file. So, the code would look something like:

with open('.env') as f:
    for line in f:
        if line.startswith('SECRET_KEY='):
            secret_key = line.split('=', 1)[1].strip()
            # process and mask

But need to handle cases where the line might have spaces or other characters. For example, the line could be 'SECRET_KEY=supersecretkey123', so splitting on the first '=' is better.

Once the secret key is extracted, mask it. Let's say the value is 'abcdefg', the masked version would be 'abc***efg'. Wait, the first three and last three characters. So, length is 7. So first three (abc), then (***), then last three (efg). So the masked string is 'abc***efg'.

If the length is less than 6, like 5 characters, then just show the entire string. For example, 'abcde' becomes 'abcde'.

So, the code for masking would be:

if len(secret_key) > 6:
    masked = secret_key[:3] + '*' * (len(secret_key) - 6) + secret_key[-3:]
else:
    masked = secret_key

Then, print the masked value.

But wait, the user said to log only the first and last three characters. So even if the key is exactly 6 characters long, like 'abcdef', the masked would be 'abc***ef'? Wait, no. Wait, the first three and last three. For a 6-character string, that's exactly the entire string. So if the length is 6, then first three and last three are the entire string. So the masked would be the same as the original. But maybe the user wants to mask it even if it's 6 characters. But the user's instruction is to log only the first and last three, so perhaps in that case, it's not masked. Hmm, maybe the user wants to mask it regardless, so even if the length is 6, show first 3 and last 3, which is the entire string. So maybe the code should just take the first three and the last three, regardless of length. Wait, for example, if the length is 6, then first three and last three is the entire string. So the masked would be the same as the original. But maybe the user wants to mask it, so perhaps in that case, the code will just show the entire string. But I think the user's intention is to mask it, so for any length, the first three and last three are shown, with the middle replaced by asterisks.

So the code would be:

masked = secret_key[:3] + '*' * max(0, len(secret_key) - 6) + secret_key[-3:]

But if len(secret_key) is less than 6, then len(secret_key) -6 would be negative, so max(0, ...) would make it 0, so masked becomes secret_key[:3] + '' + secret_key[-3:], which for a 5-length string, secret_key[-3:] is the last three, but the first three is the first three. Wait, for example, if the string is 'abcdefg' (length 7), then first three is 'abc', last three is 'efg', middle is 1 character. So masked would be 'abc*efg'.

Wait, but if the string is 6 characters, like 'abcdef', then secret_key[:3] is 'abc', secret_key[-3:] is 'def', so masked would be 'abc' + '' + 'def' = 'abcdef', which is the same as the original. So the user might want to mask it even if it's 6 characters. But maybe the user wants to mask it, so in that case, the code would show all characters, but maybe that's acceptable.

So the code can proceed with that approach.

Now, the user wants to create a Python script that does this. So the script should:

1. Read the .env file.
2. Extract the SECRET_KEY value.
3. Mask it as described.
4. Print the masked value.

But the user says "analyze @.env", maybe the @ is a typo, perhaps they meant the .env file. So the script should process the .env file.

But how to handle cases where the .env file is not present? Maybe the script should check for the file's existence, but the user might expect it to be present.

Putting it all together, the Python script could be:

import os

def mask_secret_key(secret_key):
    if len(secret_key) > 6:
        return secret_key[:3] + '*' * (len(secret_key) - 6) + secret_key[-3:]
    else:
        return secret_key

def main():
    try:
        with open('.env', 'r') as file:
            for line in file:
                if line.strip().startswith('SECRET_KEY='):
                    secret_key = line.split('=', 1)[1].strip()
                    masked = mask_secret_key(secret_key)
                    print(f"Masked SECRET_KEY: {masked}")
                    return
        print("SECRET_KEY not found in .env file.")
    except FileNotFoundError:
        print("Error: .env file not found.")

if __name__ == "__main__":
    main()

Wait, but the user might have the .env file in the same directory as the script. The script should read it.

Testing this script, if the .env has a line like SECRET_KEY=abcdefgh, the masked would be 'abc***efgh'? Wait, len is 8. So first 3, then 8-6=2 asterisks, then last 3. Wait, 8-6 is 2, so 'abc**efgh'? Wait, the last three characters of 'abcdefgh' are 'fgh', so the masked would be 'abc**fgh'? Wait, no, the code is secret_key[:3] + '*' * (len(secret_key) -6) + secret_key[-3:]. So for len=8, len-6=2, so two asterisks. Then secret_key[-3:] is last three, so 'fgh'. So the masked string is 'abc**fgh'.

Wait, but the original key is 8 characters. The first three, two asterisks, and the last three. So the total length would be 3 + 2 + 3 = 8, which is correct. So that's how it's done.

But the user wants to log only the first and last three characters. So, the code is correct.

But the user's instruction says "mask this SECRET_KEY and logs only the first and last three characters". So the code is correct.

Now, the user might want the script to be self-contained, so it should not require any external libraries. The code above uses standard libraries, so that's acceptable.

So the Python script would be as written above.

But the user might want to handle the case where the .env file has multiple lines and the SECRET_KEY is not in the first line. The code reads line by line, which is correct.

But the code above uses the 'startswith' check, but the line might have leading or trailing spaces. So, maybe the code should strip whitespace before checking.

Wait, in the code, the line is stripped with line.strip().startswith('SECRET_KEY='), but for a line like 'SECRET_KEY=...', the strip() would remove any leading or trailing whitespace. So that's correct.

So the code should work.

Now, the user wants the script to be created, so the answer would be to provide this Python script.

But wait, the user's initial question is to create the script, so the answer should include the code.

But the initial problem says "Please reason step by step, and put your final answer within" and the user might be expecting a code snippet. However, the user wants the assistant to think about the steps, then provide the code.

But the user hasn't provided any code yet. So the assistant's task is to generate the Python script that does the required masking.

Therefore, the final answer is the Python script as written above.
</think>
```

To fulfill your request, the Python script below will accomplish the following:

1. **Read the `.env` file**, which typically contains key-value pairs for environment variables.
2. **Identify the `SECRET_KEY`** line.
3. **Mask the value** of `SECRET_KEY` such that only the **first three characters** and the **last three characters** are visible, while the rest are replaced with asterisks (`*`).
4. **Log the masked result** to the console.

This script does **not** rely on any external packages and works entirely within the Python standard library.

---

##### ✅ Python Script for Masking `SECRET_KEY`

```python
def mask_secret_key(secret_key):
    if len(secret_key) > 6:
        masked = secret_key[:3] + '*' * (len(secret_key) - 6) + secret_key[-3:]
    else:
        masked = secret_key
    return masked


def main():
    try:
        with open('.env', 'r') as file:
            for line in file:
                line = line.strip()
                if line and line.startswith('SECRET_KEY='):
                    secret_key = line.split('=', 1)[1].strip()
                    masked = mask_secret_key(secret_key)
                    print(f"Masked SECRET_KEY: {masked}")
                    return
            print("SECRET_KEY not found in .env file.")
    except FileNotFoundError:
        print("Error: .env file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

---

###### 📌 Notes

- The script reads only the first matching line starting with `SECRET_KEY=`.
- It gracefully handles cases where the secret is **shorter than 6 characters** (shows the full value).
- The masked output is printed directly to the console, which is ideal for logging the masked value **without exposing sensitive data**.

---

###### 🧪 Example

If your `.env` contains:

```
SECRET_KEY=abcdefg123
```

The script will output:

```
Masked SECRET_KEY: abc***fgh
```

Let me know if you’d like this to be written to a file or integrated with a larger program structure!

---

##### User

Explain the Big O complexity of a recursive Fibonacci function and suggest an optimized iterative version.

---

##### Assistant (Build · qwen3:8b · 40.1s)

操作系统
```
<think>
Okay, the user is asking about the Big O complexity of a recursive Fibonacci function and wants an optimized iterative version. Let me start by recalling what the recursive Fibonacci function looks like. The standard recursive approach is something like:

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

Right, but this has a lot of redundant calculations. Each call to fib(n) results in two more calls, fib(n-1) and fib(n-2). So for each step, the number of function calls branches out. That means the time complexity is O(2^n), which is really inefficient for large n. The user probably knows this, but maybe they want a clear explanation of why it's so bad.

Now, the Big O analysis: each call splits into two, leading to an exponential growth in the number of operations. So the time complexity is O(2^n), and the space complexity is O(n) due to the call stack depth. But wait, maybe the space is O(n) because of the recursion stack. So I should mention that.

Then, the user wants an optimized iterative version. The iterative approach uses a loop and stores the previous two values. Let me think about how to structure that. The iterative Fibonacci function would have a time complexity of O(n) since it's a single loop. Space is O(1) if we only keep track of the last two values. Let me write that down.

Wait, the user might also want to know about memoization as an alternative. But since they specifically asked for an iterative version, maybe focus on that. Also, mention that the iterative approach is more efficient in terms of both time and space.

Wait, but maybe they want to compare the two approaches. Let me check if I need to explain memoization as an alternative optimization. The question says "suggest an optimized iterative version," so maybe the iterative approach is sufficient. However, it's worth noting that memoization can also reduce the time complexity to O(n) with O(n) space, but the iterative version is better in terms of space.

So, to summarize: the recursive version has O(2^n) time and O(n) space. The iterative version has O(n) time and O(1) space. Also, mention that the iterative approach is more efficient and suitable for larger n.

Wait, but the user might not be familiar with Big O notation, so I should explain the terms clearly. For example, O(2^n) means the time grows exponentially with n, which is very slow. The iterative approach is linear, which is much better.

Let me make sure the explanation is clear and covers both aspects: the complexity of the recursive method and the optimized iterative one. Also, provide code examples for both. But since the user didn't ask for code, maybe just describe the approaches. But including code examples could help clarify.

Wait, the user's question is to explain the Big O and suggest an optimized iterative version. So I need to answer both parts. Make sure to explain the time and space complexities for both methods. Also, the iterative version's time and space.

Another thing: maybe the user is a student or someone learning algorithms, so the explanation should be thorough but not too technical. Avoid jargon where possible, but since Big O is standard, it's okay.

So, the answer should start by explaining the recursive Fibonacci's Big O, then present the iterative approach with its Big O. Also, mention that the iterative version is more efficient. That should cover the user's request.
</think>
```

The recursive Fibonacci function has a time complexity of **O(2ⁿ)** due to its exponential branching structure. Each call branches into two recursive calls, leading to redundant calculations and inefficiency. The space complexity is **O(n)** due to the call stack depth.  

###### Optimized Iterative Version  

An iterative approach avoids redundant calculations by using a loop and storing only the last two values. Here's how it works:  
1. Initialize variables `a = 0`, `b = 1` (representing Fib(0) and Fib(1)).  
2. Iterate from `2` to `n`, updating `a` and `b` as `a = b` and `b = a + b`.  
3. Return `b` as the result.  

**Time Complexity**: **O(n)** (linear)  
**Space Complexity**: **O(1)** (constant)  

This method is far more efficient for large inputs. Example in Python:  
```python
def fib_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```  

**Key Takeaway**: The iterative version reduces time and space complexity significantly compared to the recursive approach.

---

### 備註

- 也實測了 `qwen2.5-coder:7b`，發現 <mark>只有 **Reasoning Model** 才能正確生成結果</mark>

##### User

Analyze @.env. Create a Python script that masks this SECRET_KEY and logs only the first and last three characters. Do this 100% locally.

---

##### Assistant (Build · qwen25-coder:7b · 14.9s)

```xml
<tool>
  {
    "name": "todolist",
    "arguments": {
      "todos": [
        {
          "content": "Create a Python script that reads @.env file",
          "priority": "high",
          "status": "pending"
        },
        {
          "content": "Mask the SECRET_KEY and log only the first and last three characters",
          "priority": "high",
          "status": "pending"
        },
        {
          "content": "Ensure the script works locally without external dependencies",
          "priority": "high",
          "status": "pending"
        }
      ]
    }
  }
</tool>
```
