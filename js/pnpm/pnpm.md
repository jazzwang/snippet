# pnpm

> Fast, disk space efficient package manager

- Website:
  - https://pnpm.io/
- Git Repo:
  - https://github.com/pnpm/pnpm

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