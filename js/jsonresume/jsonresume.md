# jsonresume

- https://jsonresume.org/getting-started
  - 從 https://github.com/PeterDaveHello 的 Organization 看到的

## 測試 resumed CLI

- (2024-08-19 17:08:10)
- https://github.com/rbardini/resumed
- 測試環境：Github Codespace
```bash
@jazzwang ➜ /workspaces/snippet (master) $ cd js/jsonresume/
@jazzwang ➜ /workspaces/snippet/js/jsonresume (master) $ npm install -g resumed jsonresume-theme-even

added 26 packages in 2s

11 packages are looking for funding
  run `npm fund` for details

@jazzwang ➜ /workspaces/snippet/js/jsonresume (master) $ which resumed
/home/codespace/nvm/current/bin/resumed

@jazzwang ➜ /workspaces/snippet/js/jsonresume (master) $ resumed --help

  Usage
    $ resumed <command> [options]

  Available Commands
    render      Render resume
    init        Create sample resume
    validate    Validate resume

  For more info, run any command with the `--help` flag
    $ resumed render --help
    $ resumed init --help

  Options
    -v, --version    Displays current version
    -h, --help       Displays this message

@jazzwang ➜ /workspaces/snippet/js/jsonresume (master) $ ls
README.md
@jazzwang ➜ /workspaces/snippet/js/jsonresume (master) $ resumed init
Done! Start editing resume.json now, and run the render command when you are ready. 👍
@jazzwang ➜ /workspaces/snippet/js/jsonresume (master) $ ls
README.md  resume.json
@jazzwang ➜ /workspaces/snippet/js/jsonresume (master) $ code resume.json 
@jazzwang ➜ /workspaces/snippet/js/jsonresume (master) $ git add resume.json 
@jazzwang ➜ /workspaces/snippet/js/jsonresume (master) $ resumed render -t jsonresume-theme-even
You can find your rendered resume at resume.html. Nice work! 🚀
```
* 產生的 HTML 履歷截圖：
