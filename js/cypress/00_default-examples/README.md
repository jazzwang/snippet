# [JS] Learning Cypress

[TOC]

- 官方網站 - https://www.cypress.io/
- ( 2022-02-22 22:15:20 )
- 與其他框架不同的地方 - https://www.cypress.io/how-it-works/

## 2022-02-22

### 測試一：本機測試

- ( 2022-02-22 21:58:59 )
- 測試環境：macOS Big Sur Version 11.6.4 - MacBook Air (13-inch, 2017)
```
~$ uname -a
Darwin local.local 20.6.0 Darwin Kernel Version 20.6.0: Wed Jan 12 22:22:42 PST 2022; root:xnu-7195.141.19~2/RELEASE_X86_64 x86_64
```
- ( 2022-02-22 22:03:30 )
- 安裝：
```
~$ brew install npm
~$ cd /tmp
/tmp$ mkdir playground
/tmp$ cd playground/
/tmp/playground$ npm install cypress --save-dev

added 165 packages, and audited 166 packages in 17s

27 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
```
- ( 2022-02-22 22:08:13 )
- 開啟 Cypress IDE 產生預設範例的目錄結構
```
/tmp/playground$ node_modules/.bin/cypress open
```
- ( 2022-02-22 22:09:11 )
- 預設 Cypress 專案目錄結構
```
/tmp/playground$ tree cypress
cypress
├── fixtures
│   └── example.json
├── integration
│   ├── 1-getting-started
│   │   └── todo.spec.js
│   └── 2-advanced-examples
│       ├── actions.spec.js
│       ├── aliasing.spec.js
│       ├── assertions.spec.js
│       ├── connectors.spec.js
│       ├── cookies.spec.js
│       ├── cypress_api.spec.js
│       ├── files.spec.js
│       ├── local_storage.spec.js
│       ├── location.spec.js
│       ├── misc.spec.js
│       ├── navigation.spec.js
│       ├── network_requests.spec.js
│       ├── querying.spec.js
│       ├── spies_stubs_clocks.spec.js
│       ├── traversal.spec.js
│       ├── utilities.spec.js
│       ├── viewport.spec.js
│       ├── waiting.spec.js
│       └── window.spec.js
├── plugins
│   └── index.js
└── support
    ├── commands.js
    └── index.js

6 directories, 24 files
```

### 測試二：Cloud Shell 測試

- ( 2022-02-22 22:37:37 )
- 改在 https://shell.cloud.google.com/ 上測試
```
~/snippet/js/cypress/00_default-examples$ npm install

added 165 packages, and audited 166 packages in 7s

27 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
~/snippet/js/cypress/00_default-examples$ node_modules/.bin/cypress info
Your system is missing the dependency: Xvfb

Install Xvfb and run Cypress again.

Read our documentation on dependencies for more information:

https://on.cypress.io/required-dependencies

If you are using Docker, we provide containers with all required dependencies installed.

----------

Error: spawn Xvfb ENOENT

----------

Platform: linux-x64 (Debian - 11)
Cypress Version: 9.5.0
```
- ( 2022-02-22 22:38:56 )
- 安裝 xvfb
```
~/snippet/js/cypress/00_default-examples$ sudo apt-get -y install xvfb
~/snippet/js/cypress/00_default-examples$ node_modules/.bin/cypress info
/home/jazzwang/.cache/Cypress/9.5.0/Cypress/Cypress: error while loading shared libraries: libgtk-3.so.0: cannot open shared object file: No such file or directory

Proxy Settings: none detected
Environment Variables: none detected

Application Data: /home/jazzwang/.config/cypress/cy/development
Browser Profiles: /home/jazzwang/.config/cypress/cy/development/browsers
Binary Caches: /home/jazzwang/.cache/Cypress

Cypress Version: 9.5.0
System Platform: linux (Debian - 11)
System Memory: 16.8 GB free 14 GB
```
- ( 2022-02-22 22:40:50 )
- 說少了 shared libraries `libgtk-3.so.0`
```
~/snippet/js/cypress/00_default-examples$ apt-file search libgtk-3.so.0
libgtk-3-0: /usr/lib/x86_64-linux-gnu/libgtk-3.so.0
libgtk-3-0: /usr/lib/x86_64-linux-gnu/libgtk-3.so.0.2200.11
libgtk-3-0: /usr/lib/x86_64-linux-gnu/libgtk-3.so.0.2404.20

~/snippet/js/cypress/00_default-examples$ sudo apt-get -y install libgtk-3-0
```
- ( 2022-02-22 22:42:29 )
- 裝了 `libgtk-3-0` 以後，又說少了 `libgbm.so.1`
```
~/snippet/js/cypress/00_default-examples$ node_modules/.bin/cypress info
/home/jazzwang/.cache/Cypress/9.5.0/Cypress/Cypress: error while loading shared libraries: libgbm.so.1: cannot open shared object file: No such file or directory

Proxy Settings: none detected
Environment Variables: none detected

Application Data: /home/jazzwang/.config/cypress/cy/development
Browser Profiles: /home/jazzwang/.config/cypress/cy/development/browsers
Binary Caches: /home/jazzwang/.cache/Cypress

Cypress Version: 9.5.0
System Platform: linux (Debian - 11)
System Memory: 16.8 GB free 13.9 GB
```
- ( 2022-02-22 22:43:25 )
```
~/snippet/js/cypress/00_default-examples$ apt-file search libgbm.so.1
libgbm1: /usr/lib/x86_64-linux-gnu/libgbm.so.1
libgbm1: /usr/lib/x86_64-linux-gnu/libgbm.so.1.0.0

~/snippet/js/cypress/00_default-examples$ sudo apt-get -y install libgbm1
```
- ( 2022-02-22 22:45:19 )
- 看樣子必須要有 dbus 跟瀏覽器才行
```
~/snippet/js/cypress/00_default-examples$ node_modules/.bin/cypress info
[4569:0222/144429.077892:ERROR:bus.cc(392)] Failed to connect to the bus: Failed to connect to socket /run/dbus/system_bus_socket: No such file or directory
[4569:0222/144429.161482:ERROR:bus.cc(392)] Failed to connect to the bus: Could not parse server address: Unknown address type (examples of valid types are "tcp" and on UNIX "unix")
[4569:0222/144429.161526:ERROR:bus.cc(392)] Failed to connect to the bus: Could not parse server address: Unknown address type (examples of valid types are "tcp" and on UNIX "unix")
[4746:0222/144429.372507:ERROR:gpu_init.cc(453)] Passthrough is not supported, GL is swiftshader, ANGLE is
Displaying Cypress info...

Detected no known browsers installed


Proxy Settings: none detected
Environment Variables: none detected

Application Data: /home/jazzwang/.config/cypress/cy/development
Browser Profiles: /home/jazzwang/.config/cypress/cy/development/browsers
Binary Caches: /home/jazzwang/.cache/Cypress

Cypress Version: 9.5.0
System Platform: linux (Debian - 11)
System Memory: 16.8 GB free 13.8 GB
```
- ( 2022-02-22 22:53:21 )
- 沒有裝瀏覽器，還是可以跑 Cypress 測試
```
~/snippet/js/cypress/00_default-examples$ node_modules/.bin/cypress run -s cypress/integration/1-getting-started/todo.spec.js
It looks like this is your first time using Cypress: 9.5.0

✔  Verified Cypress! /home/jazz_innova18/.cache/Cypress/9.5.0/Cypress

Opening Cypress...
[5000:0222/144847.871539:ERROR:bus.cc(392)] Failed to connect to the bus: Failed to connect to socket /run/dbus/system_bus_socket: No such file or directory
[5000:0222/144847.874681:ERROR:bus.cc(392)] Failed to connect to the bus: Could not parse server address: Unknown address type (examples of valid types are "tcp" and on UNIX "unix")
[5000:0222/144847.874735:ERROR:bus.cc(392)] Failed to connect to the bus: Could not parse server address: Unknown address type (examples of valid types are "tcp" and on UNIX "unix")
[5178:0222/144847.899457:ERROR:gpu_init.cc(453)] Passthrough is not supported, GL is swiftshader, ANGLE is

====================================================================================================

  (Run Starting)

  ┌────────────────────────────────────────────────────────────────────────────────────────────────┐
  │ Cypress:        9.5.0                                                                          │
  │ Browser:        Electron 94 (headless)                                                         │
  │ Node Version:   v12.14.1 (/usr/local/nvm/versions/node/v12.14.1/bin/node)                      │
  │ Specs:          1 found (1-getting-started/todo.spec.js)                                       │
  │ Searched:       cypress/integration/1-getting-started/todo.spec.js                             │
  └────────────────────────────────────────────────────────────────────────────────────────────────┘


────────────────────────────────────────────────────────────────────────────────────────────────────

  Running:  1-getting-started/todo.spec.js                                                  (1 of 1)
[5000:0222/144852.234549:ERROR:bus.cc(392)] Failed to connect to the bus: Could not parse server address: Unknown address type (examples of valid types are "tcp" and on UNIX "unix")
Browserslist: caniuse-lite is outdated. Please run:
npx browserslist@latest --update-db

Why you should do it regularly:
https://github.com/browserslist/browserslist#browsers-data-updating


  example to-do app
    ✓ displays two todo items by default (1698ms)
    ✓ can add new todo items (712ms)
    ✓ can check off an item as completed (444ms)
    with a checked task
      ✓ can filter for uncompleted tasks (619ms)
      ✓ can filter for completed tasks (702ms)
      ✓ can delete all completed tasks (537ms)


  6 passing (7s)


  (Results)

  ┌────────────────────────────────────────────────────────────────────────────────────────────────┐
  │ Tests:        6                                                                                │
  │ Passing:      6                                                                                │
  │ Failing:      0                                                                                │
  │ Pending:      0                                                                                │
  │ Skipped:      0                                                                                │
  │ Screenshots:  0                                                                                │
  │ Video:        true                                                                             │
  │ Duration:     7 seconds                                                                        │
  │ Spec Ran:     1-getting-started/todo.spec.js                                                   │
  └────────────────────────────────────────────────────────────────────────────────────────────────┘


  (Video)

  -  Started processing:  Compressing to 32 CRF
  -  Finished processing: /home/jazz_innova18/snippet/js/cypress/00_default-examples/    (2 seconds)
                          cypress/videos/1-getting-started/todo.spec.js.mp4


====================================================================================================

  (Run Finished)


       Spec                                              Tests  Passing  Failing  Pending  Skipped
  ┌────────────────────────────────────────────────────────────────────────────────────────────────┐
  │ ✔  1-getting-started/todo.spec.js           00:07        6        6        -        -        - │
  └────────────────────────────────────────────────────────────────────────────────────────────────┘
    ✔  All specs passed!                        00:07        6        6        -        -        -

~/snippet/js/cypress/00_default-examples$
```
- ( 2022-02-22 22:55:05 )
- 看了一下產生的錄影 VIDEO，測試沒有辦法跑起來，因為找不到 Chrome 瀏覽器