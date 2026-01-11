# how to make STDERR with highlight color

- 源起：
  - 最近寫了一些自動化的 Shell Script 並且把 STDOUT 回應用 `tee -a` 寫到 log 檔方便留存
  - 但是遇到一些特殊狀況，例如網路不明原因瞬斷，Shell Script 又不好寫 Exception Handling 或 Retry 機制
  - 想說至少先能把 STDERR 的 debug 資訊跟如果 CLI 指令錯誤的輸出顯示成紅色，好歹比較能追查問題
- 研究：
  - https://stackoverflow.com/questions/6841143/how-to-set-font-color-for-stdout-and-stderr/21320645#21320645
  - https://serverfault.com/questions/59262/bash-print-stderr-in-red-color
  - https://stackoverflow.com/questions/14451603/bash-wrapper-to-color-stderr-red
- 小結：
  - 多半靠 Unix-like 核心觀念 pipe file descriptor 來解決。

## 2026-01-11

- 看起來沒有太多好的解法，常見關鍵字是 `LD_PRELOAD` 跟 `stderrd`
  - https://github.com/ku1ik/stderred
- 參考：
  - https://erlangen-sheppy.medium.com/colour-linux-error-output-red-7923c0d7dd6e
  - https://www.linkedin.com/pulse/shell-tips-finally-colorized-stderr-stdout-john-boero
  - https://gist.github.com/cehoffman/1129908
  - https://serverfault.com/questions/59262/bash-print-stderr-in-red-color

    >  Method 1: Use process substitution directly:
    >  ```bash
    >  command 2> >(sed $'s,.*,\e[31m&\e[m,'>&2)
    >  ```
    >
    >  Method 2: Create a function in bash or zsh :
    >
    >  ```bash
    >  color()(set -o pipefail;"$@" 2> >(sed $'s,.*,\e[31m&\e[m,'>&2))
    >  export -f color
    >  ```
    >
    >  Use it like this:
    >
    >  ```bash
    >  $ color command
    >  ```
    >
    >  Both methods will show the command's `stderr` in red.
  - https://stackoverflow.com/questions/6841143/how-to-set-font-color-for-stdout-and-stderr
  - https://skinwalker.wordpress.com/2012/01/24/stderr-zsh/
    > 這段是 `.zshrc` 用的，
    > ```zsh
    > exec 2>>( while read X; do print "\e[91m${X}\e[0m" > /dev/tty; done & )
    > ```
  - https://www.reddit.com/r/zsh/comments/q4qsn/a_better_way_to_make_stderr_red/
  - https://superuser.com/questions/542074/how-can-i-customize-the-color-of-error-messages-in-bash