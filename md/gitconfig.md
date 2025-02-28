# gitconfig

## 2025-02-028

### credential.helper

```bash
jazzw@JazzBook:~/git/snippet$ git-credential-helper-selector.exe
```
若修改預設使用 credential manager，設定檔會多
```
credential.helperselector.selected=manager
credential.helper=manager
```

```bash
jazzw@JazzBook:~/git/snippet$ git-credential-manager.exe diagnose
Running diagnostics...

 [ OK ] Environment
 [ OK ] File system
 [ OK ] Networking
 [ OK ] Git
 [ OK ] Credential storage
 [ OK ] Microsoft authentication (AAD/MSA)
 [ OK ] GitHub API

Diagnostic summary: 7 passed, 0 skipped, 0 failed.
Log files:
  C:\Users\jazzw\git\snippet\gcm-diagnose.log

Caution: Log files may include sensitive information - redact before sharing.
```

### core.symlinks

- 先前注意到 git for windows 如果用 symlink (ln -s) 在 Linux 機器上 checkout 不是正確的 link
- 後來在 Linux 底下修正 symlink 重新 commit，在 windows checkout 卻變成純文字檔，內容是目標路徑。
- 想要讓跨平台的 git repo 都呈現一樣的結果，因為剛好跑 `git-credential-manager.exe diagnose` 才發現 git for windows 預設 core.symlinks 是 false
- 改一下預設值，再觀察一下 Windows 跟 Linux 兩邊的行為。

```bash
jazzw@JazzBook:~/git/snippet$ git config set --global core.symlinks true
```