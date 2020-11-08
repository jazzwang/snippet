# 2020-11-08

## 數學運算式的精準度

- ( 2020-11-08 22:40:31 ) 這個問題蠻有趣的：
    - https://www.hackerrank.com/challenges/bash-tutorials---arithmetic-operations/problem
- 查了一下 `bc` 的 manpage 沒查到小數點進位的方式，不過倒是查到 `printf` 的進位方式
    - https://blog.xuite.net/jyoutw/xtech/214255233
    - “scale=2" 會讓 `bc` 精準到小數點後 2 位。"%.1f" 會讓 printf 四捨五入進位到小數點後 1 位。實測了一下，浮點運算的精準度要蠻小心的。

```bash
printf "%.1f\n" $(echo "scale=2;$TOTAL/86400"|bc)
```
