# Developer Notes

## 2023-09-04

- ( 2023-09-04 15:15:18 )
- create gitpod workspace with repo https://github.com/jazzwang/snippet.git
```bash
gitpod /workspace/snippet (master) $ cd c#/.net/
gitpod /workspace/snippet/c#/.net (master) $ mkdir codespace
gitpod /workspace/snippet/c#/.net (master) $ cd codespace/
gitpod /workspace/snippet/c#/.net/codespace (master) $ mkdir .vscode
gitpod /workspace/snippet/c#/.net/codespace (master) $ cd .vscode/
gitpod /workspace/snippet/c#/.net/codespace/.vscode (master) $ touch settings.json
gitpod /workspace/snippet/c#/.net/codespace/.vscode (master) $ cd ..
gitpod /workspace/snippet/c#/.net/codespace (master) $ code codespace.md
gitpod /workspace/snippet/c#/.net/codespace (master) $ git remote -v
origin  https://github.com/jazzwang/snippet.git (fetch)
origin  https://github.com/jazzwang/snippet.git (push)
gitpod /workspace/snippet/c#/.net/codespace (master) $ git add .
gitpod /workspace/snippet/c#/.net/codespace (master) $ git commit -a
gitpod /workspace/snippet/c#/.net/codespace (master) $ git push
```

## 2023-09-05

- ( 2023-09-05 02:30:54 )
```
gitpod /workspace/snippet (master) $ cd c#/.net/codespace/
gitpod /workspace/snippet/c#/.net/codespace (master) $ code .
gitpod /workspace/snippet/c#/.net/codespace (master) $ mkdir sbin
gitpod /workspace/snippet/c#/.net/codespace (master) $ code sbin/install-dotnet
gitpod /workspace/snippet/c#/.net/codespace (master) $ chmod a+x sbin/install-dotnet
gitpod /workspace/snippet/c#/.net/codespace (master) $ sbin/install-dotnet
gitpod /workspace/snippet/c#/.net/codespace (master) $ code .gitignore
gitpod /workspace/snippet/c#/.net/codespace (master) $ code sbin/enable-dotnet
gitpod /workspace/snippet/c#/.net/codespace (master) $ source sbin/enable-dotnet
gitpod ~ (master) $ code codespace.md
gitpod ~ (master) $ git add .
gitpod ~ (master) $ git commit -a
gitpod ~ (master) $ git push
```