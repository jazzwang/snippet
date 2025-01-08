# mirror of a repository

## 2025-01-08

- 緣起：
  - 先前就有注意到 ASF 在 Github 的 Repo 顯示為 Mirror
  - 今天想要把 HuggingFace 的 App mirror 到 Github 試試看，所以找了一下作法
- 參考文件：
  - https://docs.github.com/en/repositories/creating-and-managing-repositories/duplicating-a-repository
- 實作：
  - 拿  https://huggingface.co/spaces/Salesforce/GIFT-Eval 來做個小實驗。
  - 先用 Github CLI `gh` 建立一個 `gift-eval` repo
  ```bash
  jazzw@JazzBook:~/git$ gh repo create gift-eval --disable-issues --disable-wiki -h https://huggingface.co/spaces/Salesforce/GIFT-Eval -d "Mirror of GIFT-Eval" --public
  ✓ Created repository jazzwang/gift-eval on GitHub
    https://github.com/jazzwang/gift-eval
  ```
  - 根據文件內容，先做 bare git repo 從源頭下載下來
  ```bash
  jazzw@JazzBook:~/git$ git clone --bare https://huggingface.co/spaces/Salesforce/GIFT-Eval gift-eval.git
  Cloning into bare repository 'gift-eval.git'...
  remote: Enumerating objects: 1034, done.
  remote: Counting objects: 100% (445/445), done.
  remote: Compressing objects: 100% (417/417), done.
  Rremote: Total 1034 (delta 151), reused 0 (delta 0), pack-reused 589 (from 1)
  Receiving objects: 100% (1034/1034), 457.70 KiB | 661.00 KiB/s, done.
  Resolving deltas: 100% (523/523), done.
  ```
  - 進到源頭舊的 repo 目錄，用 `git push --mirror` 推上去目標 Github Repo
  ```bash
  jazzw@JazzBook:~/git/gift-eval.git$ git push --mirror git@github.com:jazzwang/gift-eval.git
  ```
  - 這樣就算 mirror 完成。
- **問題**：
  - <span style='color: red; background-color: lightyellow; padding: 3px;'>怎麼做到持續更新？</span>
    - 因為跨站，且不是 fork，後續要拉新的 update，看起來就得 git fetch upstream-repo, 然後 git push --mirror destination-repo <span style='background-color: blue; padding: 3px; color: white;'> [ 待測試 ] </span>
  - CI/CD (Github Action) 整合 -- 當可以做到持續更新以後，就能做同步。
    - 參考：這裡有一個 git push 到 Github 時，同步到 HuggingFace 的 Github Action 範例
      - https://github.com/gabrielchua/open-notebooklm/blob/main/.github/workflows/sync_with_hf.yml
    - HuggingFace 也有文件說明：
      - https://huggingface.co/docs/hub/spaces-github-actions
      - 提到要注意檔案大小，太大的話，要改用 Git LFS，所以有另一個檢查 file size 的 Github Action 範例