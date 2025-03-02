# gitconfig

## credential.helper

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

- Caching your GitHub credentials in Git
  - https://docs.github.com/en/enterprise-cloud@latest/get-started/git-basics/caching-your-github-credentials-in-git
- https://github.com/git-ecosystem/git-credential-manager
  - https://github.com/git-ecosystem/git-credential-manager/blob/release/docs/install.md

> If you're cloning GitHub repositories using **HTTPS**, we recommend you use <mark>GitHub CLI</mark> or <mark>Git Credential Manager (GCM)</mark> to remember your credentials.

## core.symlinks

- 先前注意到 git for windows 如果用 symlink (ln -s) 在 Linux 機器上 checkout 不是正確的 link
- 後來在 Linux 底下修正 symlink 重新 commit，在 windows checkout 卻變成純文字檔，內容是目標路徑。
- 想要讓跨平台的 git repo 都呈現一樣的結果，因為剛好跑 `git-credential-manager.exe diagnose` 才發現 git for windows 預設 core.symlinks 是 false
- 改一下預設值，再觀察一下 Windows 跟 Linux 兩邊的行為。

```bash
jazzw@JazzBook:~/git/snippet$ git config set --global core.symlinks true
```

- Reference:
  - https://github.com/git-for-windows/git/wiki/Symbolic-Links

## core.sshcommand

- 因為工作上用到 Github Enterprise，平常則用到個人的 Github 帳號。又綁定了不同的 SSH 金鑰，那如何控制 Github Enterprise 帳號用 Github Enterprise 的 SSH 私鑰，而個人的 Github 帳號用個人的 SSH 金鑰呢？
- 參考：
- 2022-09-17: How to Work With GitHub and Multiple Accounts
  - https://code.tutsplus.com/quick-tip-how-to-work-with-github-and-multiple-accounts--net-22574t
- 文章中用 `~/.ssh/config` 中設定兩組不同的「網域別名」
  ```bash
  ~$ cat ~/.ssh/config
  #Default GitHub 
  Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa
  Host github.com-work
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa_work
  ```
  然後在 git clone 的時候，刻意把 SSH 的 domain 換成別名，來達成採用不同 SSH 私鑰的目的。
  ```bash
  git remote add origin git@github.com-work:kaththy/Test.git
  ```
- 在 https://stackoverflow.com/a/58512735 看到有人改用 `git config core.sshCommand` 來避免搞混 `~/.ssh/config`
  ```bash
  git config core.sshCommand "ssh -i ~/.ssh/custom_id_rsa"
  ```