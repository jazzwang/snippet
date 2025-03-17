# commander.js

> node.js command-line interfaces made easy

- Git Repo
  - https://github.com/tj/commander.js

## 2025-03-17

- [node-webvtt](../node-webvtt/node-webvtt.md) 的 README 提到這個函式庫，
  應該是 node.js 用來產生 CLI 工具的函式庫。
  類似 Python 的 [Click](../../py/click/)。

### Install

```bash
Packages: +1
+
Progress: resolved 1, reused 1, downloaded 0, added 1, done

dependencies:
+ commander 13.1.0

Done in 495ms using pnpm v10.6.1
```

### Quick Start

```bash
jazzw@JazzBook:~/git/snippet/js/commander.js$ cat > split.js << EOF
const { program } = require('commander');

program
  .option('--first')
  .option('-s, --separator <char>')
  .argument('<string>');

program.parse();

const options = program.opts();
const limit = options.first ? 1 : undefined;
console.log(program.args[0].split(options.separator, limit));
EOF
jazzw@JazzBook:~/git/snippet/js/commander.js$ node split.js -s / --fits a/b/c
error: unknown option '--fits'
(Did you mean --first?)
jazzw@JazzBook:~/git/snippet/js/commander.js$ node split.js -s / --first a/b/c
[ 'a/b/c' ]
```