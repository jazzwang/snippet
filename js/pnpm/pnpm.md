# pnpm

> Fast, disk space efficient package manager

- Website:
  - https://pnpm.io/
- Git Repo:
  - https://github.com/pnpm/pnpm
- Document
  - https://pnpm.io/motivation
  - Installation - https://pnpm.io/installation

## 2025-03-09

- ( 2025-03-09 23:22:21 )
- 想安裝 CLI for Microsoft 365 但是 scoop 只有 pnpm 套件，找不到 npx 跟 npm

## 2025-03-10

- 備忘：https://pnpm.io/pnpm-cli#commands 有大致說明 `npm` 跟 `pnpm` 對應的指令。

### Commands[​](https://pnpm.io/pnpm-cli#commands "Direct link to Commands")

For more information, see the documentation for individual CLI commands. Here is a list of handy npm equivalents to get you started:

| npm command | pnpm equivalent |
| --- |  --- |
| `npm install` | [`pnpm install`](https://pnpm.io/cli/install) |
| `npm i <pkg>` | [`pnpm add <pkg>`](https://pnpm.io/cli/add) |
| `npm run <cmd>` | [`pnpm <cmd>`](https://pnpm.io/cli/run) |

When an unknown command is used, pnpm will search for a script with the given name, so `pnpm run lint` is the same as `pnpm lint`. If there is no script with the specified name, then pnpm will execute the command as a shell script, so you can do things like `pnpm eslint` (see [`pnpm exec`](https://pnpm.io/cli/exec)).

## 2025-06-16

### Installation

#### On Windows[​](https://pnpm.io/installation#on-windows "Direct link to On Windows")

- Using `PowerShell`:

```powershell
Invoke-WebRequest https://get.pnpm.io/install.ps1 -UseBasicParsing | Invoke-Expression
```

#### On POSIX systems[​](https://pnpm.io/installation#on-posix-systems "Direct link to On POSIX systems")

```bash
curl -fsSL https://get.pnpm.io/install.sh | sh -
```
If you don't have curl installed, you would like to use wget:
```bash
wget -qO- https://get.pnpm.io/install.sh | sh -
```

#### Installing a specific version[​](https://pnpm.io/installation#installing-a-specific-version "Direct link to Installing a specific version")

Prior to running the install script, you may optionally set an env variable `PNPM_VERSION` to install a specific version of pnpm:
```
curl -fsSL https://get.pnpm.io/install.sh | env PNPM_VERSION=<version> sh -
```

#### Using Homebrew[​](https://pnpm.io/installation#using-homebrew "Direct link to Using Homebrew")

If you have the package manager installed, you can install pnpm using the following command:

```bash
brew install pnpm
```

#### Using winget[​](https://pnpm.io/installation#using-winget "Direct link to Using winget")

If you have winget installed, you can install pnpm using the following command:

```bash
winget install -e --id pnpm.pnpm

```

#### Using Scoop[​](https://pnpm.io/installation#using-scoop "Direct link to Using Scoop")

If you have Scoop installed, you can install pnpm using the following command:

```bash
scoop install nodejs-lts pnpm
```

#### Using Choco[​](https://pnpm.io/installation#using-choco "Direct link to Using Choco")

If you have Chocolatey installed, you can install pnpm using the following command:

```bash
choco install pnpm
```