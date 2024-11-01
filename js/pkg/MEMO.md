# pkg

> Package your Node.js project into an executable

- https://npmjs.com/pkg
- Git repo: https://github.com/vercel/pkg

>    This repository has been archived by the owner on **Jan 14, 2024**. It is now read-only.

## 2024-10-31

- 緣起：
  - 先前研究過 `python -> executable` 。印象更早之前還有做過 `perl -> executable`。那麼 `node.js -> executable` 怎麼做呢？
  - 主要是想把 [`avantation`](https://github.com/anbuksv/avantation) 包起來，方便在不同環境使用(e.g. Google Cloud Shell, Github Codespace, etc)。
- 其他方案：
  - https://github.com/nexe/nexe
- 這個專案於 2024 年一月封存了，因為 node.js 已經支援 [Single Executable Application](https://nodejs.org/api/single-executable-applications.html#single-executable-application-creation-process)
  - [Compile a single executable from your Node app with Node.js 20 and ESBuild - DEV Community](https://dev.to/chad_r_stewart/compile-a-single-executable-from-your-node-app-with-nodejs-20-and-esbuild-210j)
  - [Transform Node.js: Single Executable | Medium](https://medium.com/@hizacharylee/simplify-node-js-distribution-converting-to-a-single-executable-with-pkg-fd1a298e7fb4)
  - 不過步驟看起來有點複雜。待找個標的來實驗看看。