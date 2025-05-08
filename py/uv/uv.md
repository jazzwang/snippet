# uv

`uv` - An extremely fast Python package and project manager, written in Rust.

- 緣起：前幾天在測試某個專案時，README 裡要我用 `uv` 安裝，而不是 `pip` 或者 [`poetry`](https://python-poetry.org/docs/)

- 文件：https://docs.astral.sh/uv
- 原始碼：https://github.com/astral-sh/uv

![](https://github.com/astral-sh/uv/assets/1309177/629e59c0-9c6e-4013-9ad4-adb2bcf5080d)

## 2025-03-26

### `uv tool`

- ( 2025-03-26 18:17:35 )
- 開始用 `uv` 來管理本地端 python 不同版本環境後，覺得 `uv tool` 跟先前找的 `py2exe` 或 [pyinstaller](../pyinstaller) 有點異曲同工之妙。
```bash
jazzw@JazzBook:~/git/snippet/py/click$ uv tool install -h
Install commands provided by a Python package

Usage: uv.exe tool install [OPTIONS] <PACKAGE>

Arguments:
  <PACKAGE>  The package to install commands from

Options:
      --with <WITH>                            Include the following extra requirements
      --with-requirements <WITH_REQUIREMENTS>  Run all requirements listed in the given `requirements.txt` files
  -e, --editable                               Install the target package in editable mode, such that changes in the package's source directory are reflected without reinstallation
      --with-editable <WITH_EDITABLE>          Include the given packages in editable mode
  -c, --constraints <CONSTRAINTS>              Constrain versions using the given requirements files [env: UV_CONSTRAINT=]
      --overrides <OVERRIDES>                  Override versions using the given requirements files [env: UV_OVERRIDE=]
      --force                                  Force installation of the tool

Index options:
      --index <INDEX>                        The URLs to use when resolving dependencies, in addition to the default index [env: UV_INDEX=]
      --default-index <DEFAULT_INDEX>        The URL of the default package index (by default: <https://pypi.org/simple>) [env: UV_DEFAULT_INDEX=]
  -i, --index-url <INDEX_URL>                (Deprecated: use `--default-index` instead) The URL of the Python package index (by default: <https://pypi.org/simple>) [env: UV_INDEX_URL=]
      --extra-index-url <EXTRA_INDEX_URL>    (Deprecated: use `--index` instead) Extra URLs of package indexes to use, in addition to `--index-url` [env: UV_EXTRA_INDEX_URL=]
  -f, --find-links <FIND_LINKS>              Locations to search for candidate distributions, in addition to those found in the registry indexes [env: UV_FIND_LINKS=]
      --no-index                             Ignore the registry index (e.g., PyPI), instead relying on direct URL dependencies and those provided via `--find-links`
      --index-strategy <INDEX_STRATEGY>      The strategy to use when resolving against multiple index URLs [env: UV_INDEX_STRATEGY=] [possible values: first-index, unsafe-first-match,
                                             unsafe-best-match]
      --keyring-provider <KEYRING_PROVIDER>  Attempt to use `keyring` for authentication for index URLs [env: UV_KEYRING_PROVIDER=] [possible values: disabled, subprocess]

Resolver options:
  -U, --upgrade                            Allow package upgrades, ignoring pinned versions in any existing output file. Implies `--refresh`
  -P, --upgrade-package <UPGRADE_PACKAGE>  Allow upgrades for a specific package, ignoring pinned versions in any existing output file. Implies `--refresh-package`
      --resolution <RESOLUTION>            The strategy to use when selecting between the different compatible versions for a given package requirement [env: UV_RESOLUTION=] [possible values: highest,
                                           lowest, lowest-direct]
      --prerelease <PRERELEASE>            The strategy to use when considering pre-release versions [env: UV_PRERELEASE=] [possible values: disallow, allow, if-necessary, explicit,
                                           if-necessary-or-explicit]
      --fork-strategy <FORK_STRATEGY>      The strategy to use when selecting multiple versions of a given package across Python versions and platforms [env: UV_FORK_STRATEGY=] [possible values:
                                           fewest, requires-python]
      --exclude-newer <EXCLUDE_NEWER>      Limit candidate packages to those that were uploaded prior to the given date [env: UV_EXCLUDE_NEWER=]
      --no-sources                         Ignore the `tool.uv.sources` table when resolving dependencies. Used to lock against the standards-compliant, publishable package metadata, as opposed to
                                           using any workspace, Git, URL, or local path sources

Installer options:
      --reinstall                              Reinstall all packages, regardless of whether they're already installed. Implies `--refresh`
      --reinstall-package <REINSTALL_PACKAGE>  Reinstall a specific package, regardless of whether it's already installed. Implies `--refresh-package`
      --link-mode <LINK_MODE>                  The method to use when installing packages from the global cache [env: UV_LINK_MODE=] [possible values: clone, copy, hardlink, symlink]
      --compile-bytecode                       Compile Python files to bytecode after installation [env: UV_COMPILE_BYTECODE=]

Build options:
  -C, --config-setting <CONFIG_SETTING>                          Settings to pass to the PEP 517 build backend, specified as `KEY=VALUE` pairs
      --no-build-isolation                                       Disable isolation when building source distributions [env: UV_NO_BUILD_ISOLATION=]
      --no-build-isolation-package <NO_BUILD_ISOLATION_PACKAGE>  Disable isolation when building source distributions for a specific package
      --no-build                                                 Don't build source distributions [env: UV_NO_BUILD=]
      --no-build-package <NO_BUILD_PACKAGE>                      Don't build source distributions for a specific package [env: UV_NO_BUILD_PACKAGE=]
      --no-binary                                                Don't install pre-built wheels [env: UV_NO_BINARY=]
      --no-binary-package <NO_BINARY_PACKAGE>                    Don't install pre-built wheels for a specific package [env: UV_NO_BINARY_PACKAGE=]

Cache options:
  -n, --no-cache                           Avoid reading from or writing to the cache, instead using a temporary directory for the duration of the operation [env: UV_NO_CACHE=]
      --cache-dir <CACHE_DIR>              Path to the cache directory [env: UV_CACHE_DIR=]
      --refresh                            Refresh all cached data
      --refresh-package <REFRESH_PACKAGE>  Refresh cached data for a specific package

Python options:
  -p, --python <PYTHON>                        The Python interpreter to use to build the tool environment. [env: UV_PYTHON=]
      --python-preference <PYTHON_PREFERENCE>  Whether to prefer uv-managed or system Python installations [env: UV_PYTHON_PREFERENCE=] [possible values: only-managed, managed, system, only-system]
      --no-python-downloads                    Disable automatic downloads of Python. [env: "UV_PYTHON_DOWNLOADS=never"]

Global options:
  -q, --quiet                                      Do not print any output
  -v, --verbose...                                 Use verbose output
      --color <COLOR_CHOICE>                       Control the use of color in output [possible values: auto, always, never]
      --native-tls                                 Whether to load TLS certificates from the platform's native certificate store [env: UV_NATIVE_TLS=]
      --offline                                    Disable network access [env: UV_OFFLINE=]
      --allow-insecure-host <ALLOW_INSECURE_HOST>  Allow insecure connections to a host [env: UV_INSECURE_HOST=]
      --no-progress                                Hide all progress outputs [env: UV_NO_PROGRESS=]
      --directory <DIRECTORY>                      Change to the given directory prior to running the command
      --project <PROJECT>                          Run the command within the given project directory
      --config-file <CONFIG_FILE>                  The path to a `uv.toml` file to use for configuration [env: UV_CONFIG_FILE=]
      --no-config                                  Avoid discovering configuration files (`pyproject.toml`, `uv.toml`) [env: UV_NO_CONFIG=]
  -h, --help                                       Display the concise help for this command
  -V, --version                                    Display the uv version
```
- ( 2025-03-26 18:23:57 )
- 問 Gemini 怎麼安裝本地的 Python package，畢竟一些小工具，也不好老是產生小專案到 PyPI 上。
- https://g.co/gemini/share/9f7bf5c43829
<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
can the PACKAGE of the following uv command be local package? if yes, could you provide a helloworld example?

```bash
Usage: uv.exe tool install [OPTIONS] <PACKAGE>
Arguments:
  <PACKAGE>  The package to install commands from
```
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Yes, indeed! The `<PACKAGE>` argument in `uv tool install` can absolutely be a local package. Let's walk through a "Hello, world!" example to show you how it works.

**1. Create a Simple Local Package**

First, let's create the structure for our local package. We'll call it `hello_tool`.

```
hello_tool/
├── pyproject.toml
└── hello_tool.py
```

**2. `pyproject.toml` (Package Metadata)**

This file tells `uv` (and other tools) about your package. Create a file named `pyproject.toml` inside the `hello_tool` directory with the following content:

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "hello-tool"
version = "0.1.0"
authors = [
  { name="Your Name", email="your.email@example.com" },
]
description = "A simple hello world tool"
requires-python = ">=3.7"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

[project.scripts]
hello = "hello_tool:main"
```

* **`[project.scripts]`**: This is the crucial part for `uv tool install`. It defines the command-line script `hello` that will be created and points it to the `main` function in our `hello_tool.py` file.

**3. `hello_tool.py` (The Tool's Code)**

Now, create a file named `hello_tool.py` inside the `hello_tool` directory with the following Python code:

```python
def main():
    print("Hello from the local tool!")

if __name__ == "__main__":
    main()
```

This is a very basic script with a `main` function that prints our greeting.

**4. Install the Local Tool using `uv`**

Now, open your terminal, navigate to the directory *containing* the `hello_tool` directory, and run the `uv tool install` command, pointing it to your local package directory:

```bash
uv tool install ./hello_tool
```

`uv` will recognize this as a local package, build it (if necessary), and install the `hello` command-line tool.

**5. Run Your Local Tool**

After the installation is successful, you should be able to run your `hello` command from your terminal:

```bash
hello
```

You should see the output:

```
Hello from the local tool!
```

**Explanation:**

* By providing the path to the local `hello_tool` directory to `uv tool install`, you told `uv` where to find the package definition (`pyproject.toml`).
* `uv` read the `[project.scripts]` section of `pyproject.toml` and created an executable script named `hello` that, when run, will execute the `main` function in your `hello_tool.py` file.

So, yes, installing local packages as tools with `uv` is definitely possible and quite useful for developing and testing your command-line utilities!
</td></tr></table>

- ( 2025-03-26 18:34:46 )
- 看起來用 `requirements.txt` 會比較麻煩。

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
could you give me another example using `requirements.txt`?

</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->

You got it! Let's create another "Hello, world!" example, this time using a `requirements.txt` file to define our local package for `uv tool install`.

**1. Create the Local Package Structure**

We'll keep a similar structure to the previous example:

```
hello_tool_req/
├── hello_tool.py
└── requirements.txt
```

**2. `hello_tool.py` (The Tool's Code)**

The Python code for our tool remains the same. Create `hello_tool.py` inside the `hello_tool_req` directory:

```python
def main():
    print("Hello from the local tool using requirements.txt!")

if __name__ == "__main__":
    main()
```

**3. `requirements.txt` (Defining the Local Package)**

Now, create a `requirements.txt` file inside the `hello_tool_req` directory. For a local package that you want to install as a tool, the simplest way to define it here is using the `-e` flag (for editable install) followed by the path to the current directory (`.`). This tells `uv` that the current directory represents an installable package.

```
-e .
```

**Important Note:** While `requirements.txt` is typically used to list dependencies to be downloaded from PyPI, the `-e .` line tells the installer (like `pip` or `uv`) to treat the local directory as a package for installation.

**4. Install the Local Tool using `uv`**

Open your terminal, navigate to the directory *containing* the `hello_tool_req` directory, and run the `uv tool install` command, pointing it to your local `requirements.txt` file:

```bash
uv tool install ./hello_tool_req/requirements.txt
```

`uv` will read the `requirements.txt` file, see the `-e .` entry, and treat the `hello_tool_req` directory as a package to install tools from.

**5. How to Make the Tool Executable (Without `pyproject.toml`'s `[project.scripts]`)**

Since we're not using `pyproject.toml` with `[project.scripts]`, we need a slightly different approach to make our `main` function executable as a command. One common way is to create a simple script in your system's `PATH` that calls the Python interpreter on your `hello_tool.py` file.

However, `uv tool install` with a `requirements.txt` like this primarily focuses on installing the *package* as a dependency. It doesn't automatically create command-line scripts based on the contents of your Python files in the same way `setuptools` and `pyproject.toml` do with `[project.scripts]`.

**Alternative Approach (Still using `requirements.txt` for installation):**

You could install the local package using `uv pip install`:

```bash
uv pip install -e ./hello_tool_req
```

This would install your local package in editable mode. Then, to run your `main` function as a command, you'd typically invoke the Python interpreter directly:

```bash
python -m hello_tool
```

Or, if you add a shebang line (`#!/usr/bin/env python3`) at the beginning of `hello_tool.py` and make it executable (`chmod +x hello_tool_req/hello_tool.py`), you could potentially run it directly (depending on your system's configuration):

```bash
./hello_tool_req/hello_tool.py
```

**Key Takeaway:**

While you can use `uv tool install` with a `requirements.txt` that points to a local package (`-e .`), it doesn't automatically create command-line scripts in the same way as when `uv tool install` processes a package with a `pyproject.toml` file defining entry points in `[project.scripts]`.

The `requirements.txt` approach with `-e .` is more about making the local package installable as a dependency. To create runnable command-line tools more directly, `pyproject.toml` with `[project.scripts]` is the more conventional and straightforward method when using tools like `uv`.

If your goal is solely to install the local package so its modules can be imported and used by other Python code, then `uv pip install -e ./hello_tool_req` (using `requirements.txt` to define the local package) works perfectly. However, for directly creating and installing command-line tools, the `pyproject.toml` method is generally preferred with `uv tool install`.

</td></tr></table>

## 2025-05-08

- 緣起：
  - 最近因為 aider 0.76.1 版本遇到 `aiohttp==3.11.13 was yanked`[(see link)](https://github.com/aio-libs/aiohttp/issues/10617) 的問題，現在沒辦法裝了。
  - 可是 Qwen 2.5 跟 Qwen 2.5 Coder 都沒辦法正常在最新的 aider `0.82.2` 版本正常運行。
- 思路：有什麼辦法要求 aider 0.76.1 版本安裝新的 `aiohttp` 呢？
```bash
~$ uv tool install aider-chat@0.76.1
  × No solution found when resolving dependencies:
  ╰─▶ Because aiohttp==3.11.13 was yanked (reason: Regression: https://github.com/aio-libs/aiohttp/issues/10617) and aider-chat==0.76.1 depends on
      aiohttp==3.11.13, we can conclude that aider-chat==0.76.1 cannot be used.
      And because you require aider-chat==0.76.1, we can conclude that your requirements are unsatisfiable.
```
- 問了 Gemini
  - https://g.co/gemini/share/b87c2397ec74 但答案看起來不合理（幻覺）
- 嘗試一： `uv tool --with` or `uvx --with`
  - 用搜尋反而找到 https://docs.astral.sh/uv/concepts/tools/#upgrading-tools 是使用 `--with`
```bash
~/git/snippet$ uvx --with aiohttp>3.11.13 aider-chat@0.76.1
  × No solution found when resolving tool dependencies:
  ╰─▶ Because aider-chat==0.76.1 depends on aiohttp==3.11.13 and aiohttp==3.11.13 was yanked (reason: Regression:
      https://github.com/aio-libs/aiohttp/issues/10617), we can conclude that aider-chat==0.76.1 cannot be used.
      And because you require aider-chat==0.76.1, we can conclude that your requirements are unsatisfiable.
```
- 嘗試二：下載 aider 原始碼，修改 `requirements.txt`
```bash
~/git$ git clone git@github.com:Aider-AI/aider.git
~/git$ cd aider
~/git/aider$ git checkout v0.76.2 -b 0.76.2
~/git/aider$ vi requirements.txt
~/git/aider$ git diff
diff --git a/requirements.txt b/requirements.txt
index 346a3c05..8197067d 100644
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
~/git$ uv tool install ./aider
Resolved 97 packages in 4.73s
      Built aider-chat @ file:///C:/Users/jazzw/git/aider
      Built pyperclip==1.9.0
⠼ Preparing packages... (94/97)
tree-sitter-language-pack ------------------------------ 12.12 MiB/12.37 MiB 
```
- 看起來少了在 Windows 底下編譯 Fortran 的環境（為了 scipy 1.13.1 版本）
```bash
~/git$ uv tool install --with scipy==1.13.1 ./aider
Resolved 97 packages in 51ms
  × Failed to build `scipy==1.13.1`
  ├─▶ The build backend returned an error
  ╰─▶ Call to `mesonpy.build_wheel` failed (exit code: 1)

      [stdout]
      + meson setup C:\Users\jazzw\AppData\Local\uv\cache\sdists-v9\pypi\scipy\1.13.1\kro4RrKeRiklyNKEbpGX9\src
      C:\Users\jazzw\AppData\Local\uv\cache\sdists-v9\pypi\scipy\1.13.1\kro4RrKeRiklyNKEbpGX9\src\.mesonpy-p07dwow7
      -Dbuildtype=release -Db_ndebug=if-release -Db_vscrt=md
      --native-file=C:\Users\jazzw\AppData\Local\uv\cache\sdists-v9\pypi\scipy\1.13.1\kro4RrKeRiklyNKEbpGX9\src\.mesonpy-p07dwow7\meson-python-native-file.ini
      The Meson build system
      Version: 1.8.0
      Source dir: C:\Users\jazzw\AppData\Local\uv\cache\sdists-v9\pypi\scipy\1.13.1\kro4RrKeRiklyNKEbpGX9\src
      Build dir: C:\Users\jazzw\AppData\Local\uv\cache\sdists-v9\pypi\scipy\1.13.1\kro4RrKeRiklyNKEbpGX9\src\.mesonpy-p07dwow7
      Build type: native build
      Project name: scipy
      Project version: 1.13.1
      C compiler for the host machine: gcc (gcc 13.2.0 "gcc (GCC) 13.2.0")
      C linker for the host machine: gcc ld.bfd 2.41
      C++ compiler for the host machine: g++ (gcc 13.2.0 "g++ (GCC) 13.2.0")
      C++ linker for the host machine: g++ ld.bfd 2.41
      Cython compiler for the host machine: cython (cython 3.0.12)
      Host machine cpu family: x86_64
      Host machine cpu: x86_64
      Program python found: YES (C:\Users\jazzw\AppData\Local\uv\cache\builds-v0\.tmp3qqS9S\Scripts\python.exe)
      Run-time dependency python found: YES 3.13
      Program cython found: YES (C:\Users\jazzw\AppData\Local\uv\cache\builds-v0\.tmp3qqS9S\Scripts\cython.EXE)
      Compiler for C supports arguments -Wno-unused-but-set-variable: YES
      Compiler for C supports arguments -Wno-unused-function: YES
      Compiler for C supports arguments -Wno-conversion: YES
      Compiler for C supports arguments -Wno-misleading-indentation: YES
      Library m found: YES

      ..\meson.build:78:0: ERROR: Unknown compiler(s): [['ifort'], ['gfortran'], ['flang-new'], ['flang'], ['pgfortran'], ['g95']]
      The following exception(s) were encountered:
      Running `ifort --help` gave "[WinError 2] The system cannot find the file specified"
      Running `ifort --version` gave "[WinError 2] The system cannot find the file specified"
      Running `ifort -V` gave "[WinError 2] The system cannot find the file specified"
      Running `gfortran --help` gave "[WinError 2] The system cannot find the file specified"
      Running `gfortran --version` gave "[WinError 2] The system cannot find the file specified"
      Running `gfortran -V` gave "[WinError 2] The system cannot find the file specified"
      Running `flang-new --help` gave "[WinError 2] The system cannot find the file specified"
      Running `flang-new --version` gave "[WinError 2] The system cannot find the file specified"
      Running `flang-new -V` gave "[WinError 2] The system cannot find the file specified"
      Running `flang --help` gave "[WinError 2] The system cannot find the file specified"
      Running `flang --version` gave "[WinError 2] The system cannot find the file specified"
      Running `flang -V` gave "[WinError 2] The system cannot find the file specified"
      Running `pgfortran --help` gave "[WinError 2] The system cannot find the file specified"
      Running `pgfortran --version` gave "[WinError 2] The system cannot find the file specified"
      Running `pgfortran -V` gave "[WinError 2] The system cannot find the file specified"
      Running `g95 --help` gave "[WinError 2] The system cannot find the file specified"
      Running `g95 --version` gave "[WinError 2] The system cannot find the file specified"
      Running `g95 -V` gave "[WinError 2] The system cannot find the file specified"

      A full log can be found at
      C:\Users\jazzw\AppData\Local\uv\cache\sdists-v9\pypi\scipy\1.13.1\kro4RrKeRiklyNKEbpGX9\src\.mesonpy-p07dwow7\meson-logs\meson-log.txt

      hint: This usually indicates a problem with the package or the build environment.
```
- https://github.com/Aider-AI/aider/issues/3699