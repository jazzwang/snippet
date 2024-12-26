# React.js

- Getting Started
  - https://create-react-app.dev/docs/getting-started/

# 2024-10-14

- ( 2024-10-14 09:04:02 )
- 實驗產生 `TypeScript` 的 React.js App
- 參考 https://create-react-app.dev/docs/getting-started/ 的範例，在 Github CodeSpace 裡面實驗如下指令：
```bash
@jazzwang ➜ /workspaces/snippet (master) $ cd js/react.js/
@jazzwang ➜ /workspaces/snippet/js/react.js (master) $ npx create-react-app lab1 --template typescript
Need to install the following packages:
create-react-app@5.0.1
Ok to proceed? (y) y
npm WARN deprecated uid-number@0.0.6: This package is no longer supported.
npm WARN deprecated inflight@1.0.6: This module is not supported, and leaks memory. Do not use it. Check out lru-cache if you want a good and tested way to coalesce async requests by a key value, which is much more comprehensive and powerful.
npm WARN deprecated rimraf@2.7.1: Rimraf versions prior to v4 are no longer supported
npm WARN deprecated fstream-ignore@1.0.5: This package is no longer supported.
npm WARN deprecated glob@7.2.3: Glob versions prior to v9 are no longer supported
npm WARN deprecated fstream@1.0.12: This package is no longer supported.
npm WARN deprecated tar@2.2.2: This version of tar is no longer supported, and will not receive security updates. Please upgrade asap.

Creating a new React app in /workspaces/snippet/js/react.js/lab1.

Installing packages. This might take a couple of minutes.
Installing react, react-dom, and react-scripts with cra-template-typescript...


added 1478 packages in 1m

262 packages are looking for funding
  run `npm fund` for details

Installing template dependencies using npm...

added 41 packages, removed 1 package, and changed 2 packages in 5s

262 packages are looking for funding
  run `npm fund` for details

We detected TypeScript in your project (src/App.test.tsx) and created a tsconfig.json file for you.

Your tsconfig.json has been populated with default values.

Removing template package using npm...


removed 1 package, and audited 1518 packages in 3s

262 packages are looking for funding
  run `npm fund` for details

8 vulnerabilities (2 moderate, 6 high)

To address all issues (including breaking changes), run:
  npm audit fix --force

Run `npm audit` for details.

Success! Created lab1 at /workspaces/snippet/js/react.js/lab1
Inside that directory, you can run several commands:

  npm start
    Starts the development server.

  npm run build
    Bundles the app into static files for production.

  npm test
    Starts the test runner.

  npm run eject
    Removes this tool and copies build dependencies, configuration files
    and scripts into the app directory. If you do this, you can’t go back!

We suggest that you begin by typing:

  cd lab1
  npm start

Happy hacking!
@jazzwang ➜ /workspaces/snippet/js/react.js (master) $ 
```
- ( 2024-10-14 09:14:19 )
- 執行 `npm start` 啟動 http://localhost:3000 來做預覽
```bash
@jazzwang ➜ /workspaces/snippet/js/react.js (master) $ cd lab1/
@jazzwang ➜ .../snippet/js/react.js/lab1 (master) $ npm start

> lab1@0.1.0 start
> react-scripts start

Compiled successfully!

You can now view lab1 in the browser.

  Local:            http://localhost:3000
  On Your Network:  http://10.0.0.149:3000

Note that the development build is not optimized.
To create a production build, use npm run build.

webpack compiled successfully
Files successfully emitted, waiting for typecheck results...
Issues checking in progress...
No issues found.
^C
```
- ( 2024-10-14 09:24:24 )
- 範例目錄結構：
```bash
@jazzwang ➜ .../snippet/js/react.js/lab1 (master) $ rm package-lock.json node_modules/ -rf
@jazzwang ➜ .../snippet/js/react.js/lab1 (master) $ tree
.
├── README.md
├── package.json
├── public
│   ├── favicon.ico
│   ├── index.html
│   ├── logo192.png
│   ├── logo512.png
│   ├── manifest.json
│   └── robots.txt
├── src
│   ├── App.css
│   ├── App.test.tsx
│   ├── App.tsx
│   ├── index.css
│   ├── index.tsx
│   ├── logo.svg
│   ├── react-app-env.d.ts
│   ├── reportWebVitals.ts
│   └── setupTests.ts
└── tsconfig.json

2 directories, 18 files
```

## 2024-12-26

- 新增 `lab2` 範例，詳見 [lab2/MEMO.md](./lab2/MEMO.md)
- 心得：既然 https://web.lmarena.ai/ 可以用 Prompt 來產生 UI, 那應該也可以用 [OpenHands](https://github.com/All-Hands-AI/OpenHands) 做到類似的效果。