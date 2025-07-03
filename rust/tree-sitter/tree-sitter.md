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