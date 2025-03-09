# CLI for Microsoft 365

> Manage Microsoft 365 and SharePoint Framework projects on any platform

- Website
  - https://aka.ms/cli-m365
  - https://pnp.github.io/cli-microsoft365/
- Git Repo
  - https://github.com/pnp/cli-microsoft365

## Install

```
npm install -g @pnp/cli-microsoft365
```

## 2025-03-09

```bash
jazzw@JazzBook:~/git/snippet/js/cli-microsoft365$ pnpm install @pnp/cli-microsoft365
Packages: +316
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Progress: resolved 316, reused 316, downloaded 0, added 316, done

dependencies:
+ @pnp/cli-microsoft365 10.4.0

╭ Warning ───────────────────────────────────────────────────────────────────────────────────╮
│                                                                                            │
│   Ignored build scripts: protobufjs.                                                       │
│   Run "pnpm approve-builds" to pick which dependencies should be allowed to run scripts.   │
│                                                                                            │
╰────────────────────────────────────────────────────────────────────────────────────────────╯

Done in 16.8s using pnpm v10.6.1
jazzw@JazzBook:~/git/snippet/js/cli-microsoft365$ ls
cli-microsoft365.md  node_modules  package.json  pnpm-lock.yaml
jazzw@JazzBook:~/git/snippet/js/cli-microsoft365$ cd node_modules/
.bin/                       .modules.yaml               .pnpm/                      .pnpm-workspace-state.json  @pnp/
jazzw@JazzBook:~/git/snippet/js/cli-microsoft365$ cd node_modules/
.bin/                       .modules.yaml               .pnpm/                      .pnpm-workspace-state.json  @pnp/
jazzw@JazzBook:~/git/snippet/js/cli-microsoft365$ cd node_modules/.bin/
acorn             acorn.ps1         m365.CMD          m365_chili        m365_chili.ps1    m365_comp.CMD     microsoft365      microsoft365.ps1
acorn.CMD         m365              m365.ps1          m365_chili.CMD    m365_comp         m365_comp.ps1     microsoft365.CMD
jazzw@JazzBook:~/git/snippet/js/cli-microsoft365$ export PATH=$PATH:~/git/snippet/js/cli-microsoft365/node_modules/.bin/
jazzw@JazzBook:~/git/snippet/js/cli-microsoft365$ m365
'node' is not recognized as an internal or external command,
operable program or batch file.
jazzw@JazzBook:~/git/snippet/js/cli-microsoft365$ scoop install nodejs-lts
Installing 'nodejs-lts' (22.14.0) [64bit] from 'main' bucket
node-v22.14.0-win-x64.7z (20.8 MB) [==============================================================================================================] 100%
Checking hash of node-v22.14.0-win-x64.7z ... ok.
Extracting node-v22.14.0-win-x64.7z ... done.
Linking ~\scoop\apps\nodejs-lts\current => ~\scoop\apps\nodejs-lts\22.14.0
Adding ~\scoop\apps\nodejs-lts\current\bin to your path.
Adding ~\scoop\apps\nodejs-lts\current to your path.
Persisting bin
Persisting cache
Running post_install script...done.
'nodejs-lts' (22.14.0) was installed successfully!
jazzw@JazzBook:~/git/snippet/js/cli-microsoft365$ m365
'node' is not recognized as an internal or external command,
operable program or batch file.
```
- open new terminal and test again
```bash
jazzw@JazzBook:~$ export PATH=$PATH:~/git/snippet/js/cli-microsoft365/node_modules/.bin/
jazzw@JazzBook:~$ m365
 ERR_PNPM_NO_IMPORTER_MANIFEST_FOUND  No package.json (or package.yaml, or package.json5) was found in "C:\Users\jazzw".
jazzw@JazzBook:~$ cd git/snippet/js/cli-microsoft365/
jazzw@JazzBook:~/git/snippet/js/cli-microsoft365$ ls
cli-microsoft365.md  node_modules  package.json  pnpm-lock.yaml
jazzw@JazzBook:~/git/snippet/js/cli-microsoft365$ m365

CLI for Microsoft 365 v10.4.0
Manage Microsoft 365 and SharePoint Framework projects on any platform

Commands:

  docs [options]     Returns the CLI for Microsoft 365 docs webpage URL
  login [options]    Log in to Microsoft 365
  logout [options]   Log out from Microsoft 365
  request [options]  Executes the specified web request using CLI for Microsoft 365
  search [options]   Uses the Microsoft Search to query Microsoft 365 data
  setup [options]    Sets up CLI for Microsoft 365 based on your preferences
  status [options]   Shows Microsoft 365 login status
  version [options]  Shows CLI for Microsoft 365 version

Commands groups:

  adaptivecard *  1 command
  app *           4 commands
  booking *       2 commands
  cli *           12 commands
  connection *    4 commands
  context *       5 commands
  entra *         113 commands
  exo *           1 command
  external *      8 commands
  file *          5 commands
  flow *          19 commands
  graph *         7 commands
  onedrive *      8 commands
  onenote *       3 commands
  outlook *       20 commands
  pa *            13 commands
  planner *       31 commands
  pp *            35 commands
  purview *       21 commands
  search *        5 commands
  skype *         3 commands
  spe *           6 commands
  spfx *          9 commands
  spo *           366 commands
  spp *           4 commands
  teams *         70 commands
  tenant *        24 commands
  todo *          10 commands
  util *          1 command
  viva *          27 commands

jazzw@JazzBook:~/git/snippet/js/cli-microsoft365$
```
