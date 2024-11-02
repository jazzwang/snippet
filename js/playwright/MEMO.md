# playwright

> Playwright enables reliable end-to-end testing for modern web apps.

- https://playwright.dev/
- Git Repo: https://github.com/microsoft/playwright

## 2024-11-02

- https://playwright.dev/docs/intro

### Installation

- 測試環境：Github Codespace
```bash
jazzw@JazzBook:~$ gh cs ssh
? Choose codespace: jazzwang/snippet (master*): snippet
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 6.5.0-1025-azure x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro
Last login: Thu Oct 31 13:15:55 2024 from ::1
@jazzwang ➜ /workspaces/snippet (master) $ cd /tmp/
@jazzwang ➜ /tmp $
```
- 先從文件的安裝指令開始：
```bash
@jazzwang ➜ /tmp $ npm init playwright@latest lab1
Need to install the following packages:
create-playwright@1.17.134
Ok to proceed? (y) y
Getting started with writing end-to-end tests with Playwright:
Initializing project in 'lab1'
✔ Do you want to use TypeScript or JavaScript? · JavaScript
✔ Where to put your end-to-end tests? · tests
✔ Add a GitHub Actions workflow? (y/N) · false
✔ Install Playwright browsers (can be done manually via 'npx playwright install')? (Y/n) · true
✔ Install Playwright operating system dependencies (requires sudo / root - can be done manually via 'sudo npx playwright install-deps')? (y/N) · false
Initializing NPM project (npm init -y)…
Wrote to /tmp/lab1/package.json:

{
  "name": "lab1",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}


Installing Playwright Test (npm install --save-dev @playwright/test)…

added 3 packages, and audited 4 packages in 2s

found 0 vulnerabilities
Installing Types (npm install --save-dev @types/node)…

added 2 packages, and audited 6 packages in 841ms

found 0 vulnerabilities
Writing lab1/playwright.config.js.
Writing lab1/tests/example.spec.js.
Writing lab1/tests-examples/demo-todo-app.spec.js.
Writing lab1/package.json.
Downloading browsers (npx playwright install)…
Downloading Chromium 130.0.6723.31 (playwright build v1140) from https://playwright.azureedge.net/builds/chromium/1140/chromium-linux.zip
164.5 MiB [====================] 100% 0.0s
Chromium 130.0.6723.31 (playwright build v1140) downloaded to /home/codespace/.cache/ms-playwright/chromium-1140
Downloading FFMPEG playwright build v1010 from https://playwright.azureedge.net/builds/ffmpeg/1010/ffmpeg-linux.zip
2.3 MiB [====================] 100% 0.0s
FFMPEG playwright build v1010 downloaded to /home/codespace/.cache/ms-playwright/ffmpeg-1010
Downloading Firefox 131.0 (playwright build v1465) from https://playwright.azureedge.net/builds/firefox/1465/firefox-ubuntu-20.04.zip
86.7 MiB [====================] 100% 0.0s
Firefox 131.0 (playwright build v1465) downloaded to /home/codespace/.cache/ms-playwright/firefox-1465
Downloading Webkit 18.0 (playwright build v2083) from https://playwright.azureedge.net/builds/webkit/2083/webkit-ubuntu-20.04.zip
137.7 MiB [====================] 100% 0.0s
Webkit 18.0 (playwright build v2083) downloaded to /home/codespace/.cache/ms-playwright/webkit-2083
Playwright Host validation warning:
╔══════════════════════════════════════════════════════╗
║ Host system is missing dependencies to run browsers. ║
║ Please install them with the following command:      ║
║                                                      ║
║     sudo npx playwright install-deps                 ║
║                                                      ║
║ Alternatively, use apt:                              ║
║     sudo apt-get install libwoff1\                   ║
║         libwebpdemux2\                               ║
║         libharfbuzz-icu0\                            ║
║         libenchant-2-2\                              ║
║         libhyphen0\                                  ║
║         libegl1\                                     ║
║         libgudev-1.0-0\                              ║
║         libevdev2\                                   ║
║         libgles2                                     ║
║                                                      ║
║ <3 Playwright Team                                   ║
╚══════════════════════════════════════════════════════╝
    at validateDependenciesLinux (/tmp/lab1/node_modules/playwright-core/lib/server/registry/dependencies.js:216:9)
    at process.processTicksAndRejections (node:internal/process/task_queues:95:5)
    at async Registry._validateHostRequirements (/tmp/lab1/node_modules/playwright-core/lib/server/registry/index.js:707:43)
    at async Registry._validateHostRequirementsForExecutableIfNeeded (/tmp/lab1/node_modules/playwright-core/lib/server/registry/index.js:805:7)
    at async Registry.validateHostRequirementsForExecutablesIfNeeded (/tmp/lab1/node_modules/playwright-core/lib/server/registry/index.js:794:43)
    at async t.<anonymous> (/tmp/lab1/node_modules/playwright-core/lib/cli/program.js:119:7)
✔ Success! Created a Playwright Test project at /tmp/lab1

Inside that directory, you can run several commands:

  npx playwright test
    Runs the end-to-end tests.

  npx playwright test --ui
    Starts the interactive UI mode.

  npx playwright test --project=chromium
    Runs the tests only on Desktop Chrome.

  npx playwright test example
    Runs the tests in a specific file.

  npx playwright test --debug
    Runs the tests in debug mode.

  npx playwright codegen
    Auto generate tests with Codegen.

We suggest that you begin by typing:

    cd lab1
  npx playwright test

And check out the following files:
  - ./lab1/tests/example.spec.js - Example end-to-end test
  - ./lab1/tests-examples/demo-todo-app.spec.js - Demo Todo App end-to-end tests
  - ./lab1/playwright.config.js - Playwright Test configuration

Visit https://playwright.dev/docs/intro for more information. ✨

Happy hacking! 🎭
```
- 先跑一下範例：執行 `npx playwright test`
```bash
@jazzwang ➜ /tmp $ cd lab1/
@jazzwang ➜ /tmp/lab1 $ ls
node_modules  package-lock.json  package.json  playwright.config.js  tests  tests-examples
@jazzwang ➜ /tmp/lab1 $ npx playwright test

Running 6 tests using 1 worker
  1) [webkit] › example.spec.js:4:1 › has title ────────────────────────────────────────────────────

    Error: browserType.launch:
    ╔══════════════════════════════════════════════════════╗
    ║ Host system is missing dependencies to run browsers. ║
    ║ Please install them with the following command:      ║
    ║                                                      ║
    ║     sudo npx playwright install-deps                 ║
    ║                                                      ║
    ║ Alternatively, use apt:                              ║
    ║     sudo apt-get install libwoff1\                   ║
    ║         libwebpdemux2\                               ║
    ║         libharfbuzz-icu0\                            ║
    ║         libenchant-2-2\                              ║
    ║         libhyphen0\                                  ║
    ║         libegl1\                                     ║
    ║         libgudev-1.0-0\                              ║
    ║         libevdev2\                                   ║
    ║         libgles2                                     ║
    ║                                                      ║
    ║ <3 Playwright Team                                   ║
    ╚══════════════════════════════════════════════════════╝

  2) [webkit] › example.spec.js:11:1 › get started link ────────────────────────────────────────────

    Error: browserType.launch:
    ╔══════════════════════════════════════════════════════╗
    ║ Host system is missing dependencies to run browsers. ║
    ║ Please install them with the following command:      ║
    ║                                                      ║
    ║     sudo npx playwright install-deps                 ║
    ║                                                      ║
    ║ Alternatively, use apt:                              ║
    ║     sudo apt-get install libwoff1\                   ║
    ║         libwebpdemux2\                               ║
    ║         libharfbuzz-icu0\                            ║
    ║         libenchant-2-2\                              ║
    ║         libhyphen0\                                  ║
    ║         libegl1\                                     ║
    ║         libgudev-1.0-0\                              ║
    ║         libevdev2\                                   ║
    ║         libgles2                                     ║
    ║                                                      ║
    ║ <3 Playwright Team                                   ║
    ╚══════════════════════════════════════════════════════╝

  2 failed
    [webkit] › example.spec.js:4:1 › has title ─────────────────────────────────────────────────────
    [webkit] › example.spec.js:11:1 › get started link ─────────────────────────────────────────────
  4 passed (14.5s)

  Serving HTML report at http://localhost:9323. Press Ctrl+C to quit.
  ```