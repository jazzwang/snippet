# MetaGPT

- Git Repo
  - https://github.com/geekan/MetaGPT
- Paper
  - https://openreview.net/forum?id=VtmBAGCN7o

## 2025-03-22

### Install 安裝

```bash
jazzw@JazzBook:~/git/snippet/py/metagpt$ uv tool install --force --python python3.12 metagpt
Resolved 62 packages in 195ms                                                                                                                                           
  × Failed to build `tiktoken==0.3.3`
  ├─▶ The build backend returned an error
  ╰─▶ Call to `setuptools.build_meta.build_wheel` failed (exit code: 1)

    [stdout]
    running bdist_wheel
    running build
    running build_py                                                                                                                                                  
    copying tiktoken\core.py -> build\lib.win-amd64-cpython-312\tiktoken
    copying tiktoken\load.py -> build\lib.win-amd64-cpython-312\tiktoken
    copying tiktoken\model.py -> build\lib.win-amd64-cpython-312\tiktoken
    copying tiktoken\registry.py -> build\lib.win-amd64-cpython-312\tiktoken
    copying tiktoken\__init__.py -> build\lib.win-amd64-cpython-312\tiktoken
    copying tiktoken_ext\openai_public.py -> build\lib.win-amd64-cpython-312\tiktoken_ext
    running egg_info
    writing tiktoken.egg-info\PKG-INFO
    writing dependency_links to tiktoken.egg-info\dependency_links.txt
    writing requirements to tiktoken.egg-info\requires.txt
    writing top-level names to tiktoken.egg-info\top_level.txt
    reading manifest file 'tiktoken.egg-info\SOURCES.txt'
    reading manifest template 'MANIFEST.in'
    adding license file 'LICENSE'
    writing manifest file 'tiktoken.egg-info\SOURCES.txt'
    copying tiktoken\py.typed -> build\lib.win-amd64-cpython-312\tiktoken
    running build_ext
    running build_rust

    [stderr]
    C:\Users\jazzw\AppData\Local\uv\cache\builds-v0\.tmpQ3sivF\Lib\site-packages\setuptools\config\_apply_pyprojecttoml.py:82: SetuptoolsDeprecationWarning:
    `project.license` as a TOML table is deprecated
    !!

            ********************************************************************************
            Please use a simple string containing a SPDX expression for `project.license`. You can also use `project.license-files`.

            By 2026-Feb-18, you need to update your project and remove deprecated calls
            or your builds will no longer be supported.

            See https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#license for details.
            ********************************************************************************

    !!
    corresp(dist, value, root_dir)
    warning: no files found matching 'Makefile'
    error: can't find Rust compiler

    If you are using an outdated pip version, it is possible a prebuilt wheel is available for this package but pip is not able to install from it. Installing from   
    the wheel would avoid the need for a Rust compiler.

    To update pip, run:

        pip install --upgrade pip

    and then retry package installation.

    If you did intend to build this package from source, try installing a Rust compiler from your system package manager and ensure it is on the PATH during
    installation. Alternatively, rustup (available at https://rustup.rs) is the recommended way to download and update the Rust compiler toolchain.

    hint: This usually indicates a problem with the package or the build environment.

help: `tiktoken` (v0.3.3) was included because `metagpt` (v0.1) depends on `tiktoken`
```
- 因為錯誤訊息是缺少 Rust compiler，裝裝看好了～
```bash
jazzw@JazzBook:~/git/snippet/py/metagpt$ scoop install rust
```
- 不知道卡在哪裡，根據說明，改裝 `rustup`
```bash
jazzw@JazzBook:~/git/snippet/py/metagpt$ scoop info rust

Name        : rust
Description : A language empowering everyone to build reliable and efficient software. (MSVC toolchain)
Version     : 1.85.1
Bucket      : main
Website     : https://www.rust-lang.org
License     : MIT|Apache-2.0
Updated at  : 3/19/2025 4:27:43 AM
Updated by  : github-actions[bot]
Binaries    : bin\rustc.exe | bin\rustdoc.exe | bin\cargo.exe
Notes       : Use the rustup package instead for easier management of multiple toolchains, including beta/nightly releases.
              According to https://doc.rust-lang.org/book/ch01-01-installation.html#installing-rustup-on-windows
              Microsoft C++ Build Tools is needed and can be downloaded here: https://visualstudio.microsoft.com/visual-cpp-build-tools/
              When installing build tools, these two components should be selected:
              - MSVC - VS C++ x64/x86 build tools
              - Windows SDK

jazzw@JazzBook:~/git/snippet/py/metagpt$ scoop info rustup

Name        : rustup
Description : Manage multiple rust installations with ease
Version     : 1.27.1
Bucket      : main
Website     : https://rustup.rs
License     : MIT|Apache-2.0
Updated at  : 5/31/2024 2:16:03 AM
Updated by  : Tai Zeming
Environment : CARGO_HOME = $persist_dir\.cargo
              RUSTUP_HOME = $persist_dir\.rustup
Path Added  : <root>\.cargo\bin
Notes       : This package defaults to using the MSVC toolchain in new installs; use "rustup set default-host" to configure it
              (existing installs may be using the GNU toolchain by default)
              According to https://doc.rust-lang.org/book/ch01-01-installation.html#installing-rustup-on-windows
              Microsoft C++ Build Tools is needed and can be downloaded here: https://visualstudio.microsoft.com/visual-cpp-build-tools/
              When installing build tools, these two components should be selected:
              - MSVC - VS C++ x64/x86 build tools
              - Windows SDK
```
```bash
jazzw@JazzBook:~/git/snippet/py/metagpt$ scoop install rustup
Installing 'rustup' (1.27.1) [64bit] from 'main' bucket
rustup-init.exe (8.5 MB) [=====================================================================================================================================================================] 100%
Checking hash of rustup-init.exe ... ok.
Running installer script...warning: installing msvc toolchain without its prerequisites
info: profile set to 'default'
info: default host triple is x86_64-pc-windows-msvc
info: syncing channel updates for 'stable-x86_64-pc-windows-msvc'
info: latest update on 2025-03-18, rust version 1.85.1 (4eb161250 2025-03-15)
info: downloading component 'cargo'
  6.9 MiB /   6.9 MiB (100 %)   2.0 MiB/s in  3s ETA:  0s
info: downloading component 'clippy'
  2.6 MiB /   2.6 MiB (100 %)   2.0 MiB/s in  1s ETA:  0s
info: downloading component 'rust-docs'
 18.2 MiB /  18.2 MiB (100 %)   1.9 MiB/s in  9s ETA:  0s
info: downloading component 'rust-std'
 20.2 MiB /  20.2 MiB (100 %)   1.9 MiB/s in 10s ETA:  0s
info: downloading component 'rustc'
 64.1 MiB /  64.1 MiB (100 %)   1.9 MiB/s in 33s ETA:  0s
info: downloading component 'rustfmt'
info: installing component 'cargo'
info: installing component 'clippy'
info: installing component 'rust-docs'
 18.2 MiB /  18.2 MiB (100 %)   1.6 MiB/s in 10s ETA:  0s
info: installing component 'rust-std'
 20.2 MiB /  20.2 MiB (100 %)  10.2 MiB/s in  1s ETA:  0s
info: installing component 'rustc'
 64.1 MiB /  64.1 MiB (100 %)  11.3 MiB/s in  5s ETA:  0s
info: installing component 'rustfmt'
info: default toolchain set to 'stable-x86_64-pc-windows-msvc'

  stable-x86_64-pc-windows-msvc installed - (timeout reading rustc version)


Rust is installed now. Great!

To get started you need Cargo's bin directory (C:\Users\jazzw\scoop\persist
\rustup\.cargo\bin) in your PATH
environment variable. This has not been done automatically.
done.
Linking ~\scoop\apps\rustup\current => ~\scoop\apps\rustup\1.27.1
Adding ~\scoop\apps\rustup\current\.cargo\bin to your path.
Persisting .cargo
Persisting .rustup
'rustup' (1.27.1) was installed successfully!
Notes
-----
This package defaults to using the MSVC toolchain in new installs; use "rustup set default-host" to configure it
(existing installs may be using the GNU toolchain by default)
According to https://doc.rust-lang.org/book/ch01-01-installation.html#installing-rustup-on-windows
Microsoft C++ Build Tools is needed and can be downloaded here: https://visualstudio.microsoft.com/visual-cpp-build-tools/
When installing build tools, these two components should be selected:
- MSVC - VS C++ x64/x86 build tools
- Windows SDK
```
- 再裝一次 metagpt
```bash
jazzw@JazzBook:~/git/snippet/py/metagpt$ uv tool install --force --python python3.12 metagpt
Resolved 62 packages in 1.01s
  × Failed to build `tiktoken==0.3.3`
  ├─▶ The build backend returned an error
  ╰─▶ Call to `setuptools.build_meta.build_wheel` failed (exit code: 1)

      [stdout]
      running bdist_wheel
      running build
      running build_py                                                                                                                                                                                   
      copying tiktoken\core.py -> build\lib.win-amd64-cpython-312\tiktoken
      copying tiktoken\load.py -> build\lib.win-amd64-cpython-312\tiktoken
      copying tiktoken\model.py -> build\lib.win-amd64-cpython-312\tiktoken
      copying tiktoken\registry.py -> build\lib.win-amd64-cpython-312\tiktoken
      copying tiktoken\__init__.py -> build\lib.win-amd64-cpython-312\tiktoken
      copying tiktoken_ext\openai_public.py -> build\lib.win-amd64-cpython-312\tiktoken_ext
      running egg_info
      writing tiktoken.egg-info\PKG-INFO
      writing dependency_links to tiktoken.egg-info\dependency_links.txt
      writing requirements to tiktoken.egg-info\requires.txt
      writing top-level names to tiktoken.egg-info\top_level.txt
      reading manifest file 'tiktoken.egg-info\SOURCES.txt'
      reading manifest template 'MANIFEST.in'
      adding license file 'LICENSE'
      writing manifest file 'tiktoken.egg-info\SOURCES.txt'
      copying tiktoken\py.typed -> build\lib.win-amd64-cpython-312\tiktoken
      running build_ext
      running build_rust

      [stderr]
      C:\Users\jazzw\AppData\Local\uv\cache\builds-v0\.tmp9mfHq9\Lib\site-packages\setuptools\config\_apply_pyprojecttoml.py:82: SetuptoolsDeprecationWarning: `project.license` as a TOML table is      
      deprecated
      !!

              ********************************************************************************
              Please use a simple string containing a SPDX expression for `project.license`. You can also use `project.license-files`.

              By 2026-Feb-18, you need to update your project and remove deprecated calls
              or your builds will no longer be supported.

              See https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#license for details.
              ********************************************************************************

      !!
        corresp(dist, value, root_dir)
      warning: no files found matching 'Makefile'
      error: can't find Rust compiler

      If you are using an outdated pip version, it is possible a prebuilt wheel is available for this package but pip is not able to install from it. Installing from the wheel would avoid the need     
      for a Rust compiler.

      To update pip, run:

          pip install --upgrade pip

      and then retry package installation.

      If you did intend to build this package from source, try installing a Rust compiler from your system package manager and ensure it is on the PATH during installation. Alternatively, rustup       
      (available at https://rustup.rs) is the recommended way to download and update the Rust compiler toolchain.

      hint: This usually indicates a problem with the package or the build environment.
  help: `tiktoken` (v0.3.3) was included because `metagpt` (v0.1) depends on `tiktoken`
jazzw@JazzBook:~/git/snippet/py/metagpt$ 
```
- 好吧，乖乖用 `venv` 吧～
