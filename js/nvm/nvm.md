# `nvm` - Node Version Manager

- Git Repo
  - https://github.com/nvm-sh/nvm

## 2025-06-25

- 緣起：本來想要在 Windows 11 上安裝 `nodejs-lts` 但用 scoop 裝好之後沒有 `npm`，所以改裝 `nvm` ，因為官網強力建議用 Node Version Manager 安裝。
- 參考：https://docs.npmjs.com/downloading-and-installing-node-js-and-npm
> **We strongly recommend using a Node version manager like [nvm](https://github.com/nvm-sh/nvm) to install Node.js and npm.**

- 模型： Ollama + Qwen 2.5 Coder 7B
<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
could you guide me how to install nvm using scoop?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Certainly! Installing `nvm` (Node Version Manager) using Scoop is a straightforward process. Here’s a step-by-step guide:

1. **Install Scoop**:
   If you haven't already installed Scoop, you can do so by running the following command in your PowerShell or Command Prompt:

   ```powershell
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
   Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')
   ```

2. **Install nvm**:
   Once Scoop is installed, you can install `nvm` by running the following command in your PowerShell or Command Prompt:

   ```powershell
   scoop install nvm
   ```

3. **Verify Installation**:
   After installation, you can verify that `nvm` has been installed correctly by checking its version:

   ```powershell
   nvm --version
   ```

4. **Using nvm**:
   - To list available Node.js versions, use:

     ```powershell
     nvm ls-remote
     ```

   - To install a specific version of Node.js, use:

     ```powershell
     nvm install <version>
     ```

   - To switch to a specific version of Node.js, use:

     ```powershell
     nvm use <version>
     ```

   - To set a default Node.js version that gets used when you open a new terminal session, use:

     ```powershell
     nvm alias default <version>
     ```

That's it! You should now have `nvm` installed and ready to use on your system. If you encounter any issues or need further assistance, feel free to ask.
</td></tr>
<tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
how can I find npm after installed nvm?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->

After installing `nvm`, you will also have `npm` (Node Package Manager) available because it comes bundled with Node.js. Here’s how you can verify that `npm` is installed and check its version:

1. **Check if Node.js is Installed**:
   First, ensure that a version of Node.js is installed using `nvm`. You can list the installed versions and switch to one if needed:

   ```powershell
   nvm ls
   nvm use <version>
   ```

2. **Verify npm Installation**:
   Once you have a version of Node.js active, you can check if `npm` is installed by running:

   ```powershell
   npm --version
   ```

3. **Using npm**:
   - To install packages globally, use:

     ```powershell
     npm install -g <package-name>
     ```

   - To install packages locally in your project, navigate to your project directory and run:

     ```powershell
     npm install <package-name>
     ```

   - To update a package, use:

     ```powershell
     npm update <package-name>
     ```

   - To uninstall a package, use:

     ```powershell
     npm uninstall <package-name>
     ```

If you encounter any issues or need further assistance with `npm`, feel free to ask!
</td></tr></table>

### 實測

```
~$ neofetch
                                     jazzw@JazzBook
################  ################   --------------
################  ################   OS: Windows 11 Home x86_64
################  ################   Host: ASUSTeK COMPUTER INC. ASUS TUF Gaming A15 FA507NV_FA507NV
################  ################   Kernel: 10.0.26100
################  ################   Uptime: 4 days, 40 mins
################  ################   Packages: 21 (scoop)
################  ################   Shell: bash 5.2.37
                                     Resolution: 1920x1080, 1920x1080
################  ################   DE: Aero
################  ################   WM: DWM.exe
################  ################   Terminal: Windows Terminal
################  ################   CPU: AMD Ryzen 7 7735HS with Radeon Graphics (16) @ 3.200GHz
################  ################   GPU: AMD Radeon(TM) Graphics
################  ################   GPU: NVIDIA GeForce RTX 4060 Laptop GPU
################  ################   Memory: 13903MiB / 31994MiB
```
- 安裝:
```bash
~$ scoop install nvm
'nvm' (1.2.2) was installed successfully!
Notes
-----
You'll need to restart powershell/cmd to have it reload Environment Variables so nvm will work correctly
```
- 注意：安裝以後必須關閉 Terminal 或開新視窗才會生效。
- 確認：
```bash
~$ which nvm
/c/Users/jazzw/scoop/apps/nvm/current/nvm
```
- 使用：
```bash
~$ nvm list

No installations recognized.
~$ nvm -h
"-h" is not a valid command.

Running version 1.2.2.

Usage:

  nvm arch                     : Show if node is running in 32 or 64 bit mode.
  nvm current                  : Display active version.
  nvm debug                    : Check the NVM4W process for known problems (troubleshooter).
  nvm install <version> [arch] : The version can be a specific version, "latest" for the latest current version, or "lts" for the
                                 most recent LTS version. Optionally specify whether to install the 32 or 64 bit version (defaults
                                 to system arch). Set [arch] to "all" to install 32 AND 64 bit versions.
                                 Add --insecure to the end of this command to bypass SSL validation of the remote download server.
  nvm list [available]         : List the node.js installations. Type "available" at the end to see what can be installed. Aliased as ls.
  nvm on                       : Enable node.js version management.
  nvm off                      : Disable node.js version management.
  nvm proxy [url]              : Set a proxy to use for downloads. Leave [url] blank to see the current proxy.
                                 Set [url] to "none" to remove the proxy.
  nvm node_mirror [url]        : Set the node mirror. Defaults to https://nodejs.org/dist/. Leave [url] blank to use default url.
  nvm npm_mirror [url]         : Set the npm mirror. Defaults to https://github.com/npm/cli/archive/. Leave [url] blank to default url.
  nvm uninstall <version>      : The version must be a specific version.
  nvm upgrade                  : Update nvm to the latest version. Manual rollback available for 7 days after upgrade.
  nvm use [version] [arch]     : Switch to use the specified version. Optionally use "latest", "lts", or "newest".
                                 "newest" is the latest installed version. Optionally specify 32/64bit architecture.
                                 nvm use <arch> will continue using the selected version, but switch to 32/64 bit mode.
  nvm reinstall <version>      : A shortcut method to clean and reinstall a specific version.
  nvm root [path]              : Set the directory where nvm should store different versions of node.js.
                                 If <path> is not set, the current root will be displayed.
  nvm subscribe [--]<topic>    : Subscribe to desktop notifications.
                                 Valid topics: lts, current, nvm4w, author
  nvm unsubscribe [--]<topic>  : Unsubscribe from desktop notifications.
                                 Valid topics: lts, current, nvm4w, author
  nvm [--]version              : Displays the current running version of nvm for Windows. Aliased as v.
```
- 安裝：
  - 這裡使用 `lts` (Long Term Support) 版本
```bash
~$ nvm install lts
Downloading node.js version 22.17.0 (64-bit)...
Extracting node and npm...
Complete
Installation complete.
If you want to use this version, type:

nvm use 22.17.0
```
- 強制使用 `lts` 版本: 照上面建議，可以打版號。但看起來也可以用 `lts` 當作 alias
```bash
~$ nvm use 22.17.0
```
```bash
~$ nvm use lts
Now using node v22.17.0 (64-bit)
```
- 列舉可用的版本
```
~$ nvm list available

|   CURRENT    |     LTS      |  OLD STABLE  | OLD UNSTABLE |
|--------------|--------------|--------------|--------------|
|    24.3.0    |   22.17.0    |   0.12.18    |   0.11.16    |
|    24.2.0    |   22.16.0    |   0.12.17    |   0.11.15    |
|    24.1.0    |   22.15.1    |   0.12.16    |   0.11.14    |
|    24.0.2    |   22.15.0    |   0.12.15    |   0.11.13    |
|    24.0.1    |   22.14.0    |   0.12.14    |   0.11.12    |
|    24.0.0    |   22.13.1    |   0.12.13    |   0.11.11    |
|   23.11.1    |   22.13.0    |   0.12.12    |   0.11.10    |
|   23.11.0    |   22.12.0    |   0.12.11    |    0.11.9    |
|   23.10.0    |   22.11.0    |   0.12.10    |    0.11.8    |
|    23.9.0    |   20.19.3    |    0.12.9    |    0.11.7    |
|    23.8.0    |   20.19.2    |    0.12.8    |    0.11.6    |
|    23.7.0    |   20.19.1    |    0.12.7    |    0.11.5    |
|    23.6.1    |   20.19.0    |    0.12.6    |    0.11.4    |
|    23.6.0    |   20.18.3    |    0.12.5    |    0.11.3    |
|    23.5.0    |   20.18.2    |    0.12.4    |    0.11.2    |
|    23.4.0    |   20.18.1    |    0.12.3    |    0.11.1    |
|    23.3.0    |   20.18.0    |    0.12.2    |    0.11.0    |
|    23.2.0    |   20.17.0    |    0.12.1    |    0.9.12    |
|    23.1.0    |   20.16.0    |    0.12.0    |    0.9.11    |
|    23.0.0    |   20.15.1    |   0.10.48    |    0.9.10    |

This is a partial list. For a complete list, visit https://nodejs.org/en/download/releases
```
- 預設安裝路徑
```bash
~$ nvm root

Current Root: C:\Users\jazzw\scoop\persist\nvm\nodejs
```
- 確認 `npm` 與 `node` 路徑與版本
```bash
~$ which npm
/c/Users/jazzw/scoop/apps/nvm/current/nodejs/nodejs/npm
~$ which node
/c/Users/jazzw/scoop/apps/nvm/current/nodejs/nodejs/node
~$ npm --version
10.9.2
~$ node --version
v22.17.0
```