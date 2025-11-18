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
