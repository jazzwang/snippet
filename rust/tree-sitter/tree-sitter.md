# tree-sitter

> An incremental parsing system for programming tools

> Tree-sitter is a parser generator tool and an incremental parsing library.

- Git Repo
  - https://github.com/tree-sitter/tree-sitter
- Document
  - https://tree-sitter.github.io/

## 2025-07-04

- 2023-12-16
  - Tree-sitter 101: A Leaf-to-Root Beginner's Guide
  - https://www.gautamshetty.com/blog/tree-sitter-101
- 安裝:
```bash
~/git/snippet/rust/tree-sitter$ npm install -g tree-sitter-cli
```
- 驗證：
```bash
~/git/snippet/rust/tree-sitter$ which tree-sitter
/c/Users/jazzw/scoop/apps/nvm/current/nodejs/nodejs/tree-sitter
~/git/snippet/rust/tree-sitter$ tree-sitter --version
tree-sitter 0.25.6 (bf655c0beaf4943573543fa77c58e8006ff34971)
```
- 設定：
```bash
~/git/snippet/rust/tree-sitter$ tree-sitter init-config
Saved initial configuration to C:\Users\jazzw\AppData\Roaming\tree-sitter\config.json
```
- 設定 `"parser-directories"` 到 `~/src`
```bash
~/git/snippet/rust/tree-sitter$ code C:\Users\jazzw\AppData\Roaming\tree-sitter\config.json
```
- 縱使有抓 Python 跟 Perl 到 `~/src`
```bash
~/src$ ls
tree-sitter-perl  tree-sitter-python
```
- 雖然參考 https://tree-sitter.github.io/tree-sitter/creating-parsers/1-getting-started.html 試過 `tree-sitter generate`
```bash
~$ mkdir src
~$ cd src
~/src$ git clone https://github.com/tree-sitter/tree-sitter-python
~/src$ git clone https://github.com/tree-sitter-perl/tree-sitter-perl
~/src$ cd tree-sitter-python/
~/src/tree-sitter-python$ tree-sitter init
~/src/tree-sitter-python$ tree-sitter generate
~/src/tree-sitter-python$ git st
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   src/grammar.json
        modified:   src/node-types.json
        modified:   src/parser.c
        modified:   src/tree_sitter/parser.h

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        bindings/c/tree_sitter/

no changes added to commit (use "git add" and/or "git commit -a")
~/src/tree-sitter-python$ tree-sitter -h
tree-sitter 0.25.6 (bf655c0beaf4943573543fa77c58e8006ff34971)
Max Brunsfeld <maxbrunsfeld@gmail.com>
Amaan Qureshi <amaanq12@gmail.com>
Generates and tests parsers

Usage: tree-sitter.exe <COMMAND>

Commands:
  init-config     Generate a default config file
  init            Initialize a grammar repository
  generate        Generate a parser
  build           Compile a parser
  parse           Parse files
  test            Run a parser's tests
  version         Increment the version of a grammar
  fuzz            Fuzz a parser
  query           Search files using a syntax tree query
  highlight       Highlight a file
  tags            Generate a list of tags
  playground      Start local playground for a parser in the browser
  dump-languages  Print info about all known language parsers
  complete        Generate shell completions

Options:
  -h, --help     Print help
  -V, --version  Print version
~/src/tree-sitter-python$ tree-sitter build

thread 'main' panicked at cli\src\main.rs:848:18:
called `Result::unwrap()` on an `Err` value: Failed to execute the C compiler with the following command:
"cl.exe" "-nologo" "-MD" "-O2" "-Brepro" "-std:c11" "-I" "C:\\Users\\jazzw\\src\\tree-sitter-python\\src" "-W4" "-LD" "-utf-8" "C:\\Users\\jazzw\\src\\tree-sitter-python\\src\\parser.c" "C:\\Users\\jazzw\\src\\tree-sitter-python\\src\\scanner.c" "-link" "-out:C:\\Users\\jazzw\\src\\tree-sitter-python\\python.dll"

Caused by:
    program not found
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
~/src/tree-sitter-python$ tree-sitter dump-languages
scope: source.pm
parser: "C:\\Users\\jazzw\\src\\tree-sitter-perl\\."
highlights: Some(["queries/highlights.scm"])
file_types: ["pm", "pl", "t"]
content_regex: None
injection_regex: Some(Regex("(perl|pl)"))

scope: source.python
parser: "C:\\Users\\jazzw\\src\\tree-sitter-python\\."
highlights: Some(["queries/highlights.scm"])
file_types: ["py"]
content_regex: None
injection_regex: Some(Regex("py"))
```
- 不過看起來可能要安裝 Rust 然後跑 `tree-sitter build` 才會產生 `parser`
- 因為縱使 `tree-sitter dump-languages` 看到有判斷到 Perl 跟 Python 兩個語言，但實測 `tree-sitter parse test.py` 還是有錯誤訊息。
```bash
~/src/tree-sitter-python$ cd ..
~/src$ cat example.py 
import utils

def add_four(x):
  return x + 4

print(add_four(5))
~/src$ tree-sitter parse example.py 
Failed to load language for file name example.py

Caused by:
    0: Failed to execute the C compiler with the following command:
       "cl.exe" "-nologo" "-MD" "-O2" "-Brepro" "-std:c11" "-I" "C:\\Users\\jazzw\\src\\tree-sitter-python\\.\\src" "-W4" "-LD" "-utf-8" "C:\\Users\\jazzw\\src\\tree-sitter-python\\.\\src\\parser.c" "C:\\Users\\jazzw\\src\\tree-sitter-python\\.\\src\\scanner.c" "-link" "-out:C:\\Users\\jazzw\\AppData\\Local\\tree-sitter\\lib\\python.dll"
    1: program not found
```
- 紀錄一下 Bing 給的回答：
<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
py-tree-sitter perl
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Tree-sitter is a powerful tool for parsing and analyzing code, and while it supports many languages, Perl is not officially supported by the Tree-sitter organization as of now. However, there are community-driven efforts to create a Tree-sitter grammar for Perl. Here's how you can approach using Tree-sitter for Perl in Python:

1. **Check for a Perl Grammar**

Look for a community-maintained Tree-sitter grammar for Perl on GitHub. For example, you might find repositories like tree-sitter-perl that define the grammar for Perl.
Clone the repository and follow its instructions to build the grammar.

2. Install Tree-sitter Python Bindings

Install the Python bindings for Tree-sitter to interact with the parser:

```
pip install tree-sitter
```

3. **Use Tree-sitter with Perl Grammar**

Once you have the Perl grammar, you can use it in Python. Here's an example:

```python
from tree_sitter import Language, Parser

# Build the shared library for the Perl grammar
Language.build_library(
    'build/my-languages.so',  # Output path for the compiled library
    [
        'path/to/tree-sitter-perl'  # Path to the Perl grammar repository
    ]
)

# Load the Perl language
PERL_LANGUAGE = Language('build/my-languages.so', 'perl')

# Initialize the parser
parser = Parser()
parser.set_language(PERL_LANGUAGE)

# Parse some Perl code
perl_code = b'print "Hello, World!";'
tree = parser.parse(perl_code)

# Access the syntax tree
root_node = tree.root_node
print("Root node:", root_node)
```

4. Explore the Syntax Tree

The tree object contains the parsed syntax tree. You can traverse it to analyze or manipulate the Perl code.

Notes:
If no Perl grammar exists, you may need to create one, which requires defining the syntax rules for Perl in a grammar.js file. This can be complex due to Perl's flexible syntax.
Community grammars may not cover all edge cases of Perl, so testing is essential.

This approach allows you to leverage Tree-sitter's capabilities for Perl code analysis in Python. Let me know if you'd like further clarification!
</td></tr></table>