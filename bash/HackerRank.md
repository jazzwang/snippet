# 2020-11-08

- https://www.hackerrank.com/domains/shell

## 數學運算式的精準度

- ( 2020-11-08 22:40:31 ) 這個問題蠻有趣的：
    - https://www.hackerrank.com/challenges/bash-tutorials---arithmetic-operations/problem
- 查了一下 `bc` 的 manpage 沒查到小數點進位的方式，不過倒是查到 `printf` 的進位方式
    - https://blog.xuite.net/jyoutw/xtech/214255233
    - “scale=2" 會讓 `bc` 精準到小數點後 2 位。"%.1f" 會讓 printf 四捨五入進位到小數點後 1 位。實測了一下，浮點運算的精準度要蠻小心的。

```bash
printf "%.1f\n" $(echo "scale=2;$TOTAL/86400"|bc)
```

## 字串處理 `cut`

- ( 2020-11-08 23:01:44 ) 查一下 `cut` 的 manpage
    - https://www.hackerrank.com/challenges/text-processing-cut-1/Tutorial

```
     The options are as follows:

     -b list
             The list specifies byte positions.

     -c list
             The list specifies character positions.

     -d delim
             Use delim as the field delimiter character instead of the tab character.

     -f list
             The list specifies fields, separated in the input by the field delimiter character (see the -d
             option.)  Output fields are separated by a single occurrence of the field delimiter character.

     -n      Do not split multi-byte characters.  Characters will only be output if at least one byte is selected,
             and, after a prefix of zero or more unselected bytes, the rest of the bytes that form the character
             are selected.

     -s      Suppress lines with no field delimiter characters.  Unless specified, lines with no delimiters are
             passed through unmodified.
```

- `-s` 的 case 蠻特別的，以前不常用到。

## 字串處理 `head`

- ( 2020-11-08 23:47:41 )
- `head` 的 manpage
```
SYNOPSIS
     head [-n count | -c bytes] [file ...]

DESCRIPTION
     This filter displays the first count lines or bytes of each of the specified files, or of the standard input
     if no files are specified.  If count is omitted it defaults to 10.

     If more than a single file is specified, each file is preceded by a header consisting of the string ``==> XXX
     <=='' where ``XXX'' is the name of the file.
```
- Tutorial 裡的說明
```
head [filename]
head -n 11 [filename]  -> First 11 lines  
head -c 20 [filename]  -> First 20 characters  
```
- 同理 `tail` 也是一樣的語法
```
tail -n 11 [filename]  # Last 11 lines  
tail -c 20 [filename]  # Last 20 characters
```

## 字串處理 `tr`

- https://www.thegeekstuff.com/2012/12/linux-tr-command/
    - Similarly you can convert multiple continuous spaces with a single space
```bash
$ echo "This  is  for testing" | tr -s [:space:] ' '
This is for testing
```

## 字串處理 `sort`

- ( 2020-11-09 00:37:31 ) 指定「跳格符號（Tab）」的方法
    ```bash
    $ sort -t $'\t' -k 3,3n a.txt
    ```
    - <ctrl>v<tab>代表先同時按下Ctrl和v鍵，然後鬆開，按下tab鍵。
    ```bash
    $ sort -t'<ctrl>v<tab>' -k3,3n a.txt>a.sort
    ```
    - 參考：https://www.itread01.com/content/1547940273.html
