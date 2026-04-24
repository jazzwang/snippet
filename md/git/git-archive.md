# git archive

- 緣起：想把 remotion 範本生成的程式碼打包成 tar.gz
- 構想：如果有 git 做版控的話，印象可以用 `git archive` 指令生成 tar.gz 壓縮檔
- 參考： 
  - https://www.atlassian.com/git/tutorials/export-git-archive
- 範例：

> git archive --format=tar HEAD

> git archive --output=./example_repo_archive.tar --format=tar HEAD

> git archive --output=./example_repo_archive.tar.gz --format=tar HEAD ./build