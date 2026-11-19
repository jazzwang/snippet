# Linux 逐行計算字元數

## 基本方法

### 1. `awk` - 逐行計算字元數（推薦）
```bash
awk '{print NR, length($0)}' filename.txt
```
顯示每行的行號與該行的字元數。

若需要排版對齊，可搭配 `column -t`：
```bash
awk '{print NR, length($0)}' filename.txt | column -t
```

### 2. `wc -c` - 計算總字元數 / 總位元組數
```bash
wc -c filename.txt
```
> **注意**：`wc -c` 計算的是檔案的總位元組數（byte count），若要計算總字元數請使用 `wc -m`。

### 3. `sed` - 檢查行內容與長度
```bash
sed -n 'l' filename.txt
```

## 範例

```bash
echo -e "Hello World\nHello Linux" | awk '{print NR, length($0)}'
```
輸出結果：
```text
1 11
2 12
```

## 進階應用

### 統計每行字元數的出現頻率分佈
```bash
awk '{count[length($0)]++} END {for (n in count) print n, count[n]}' filename.txt | sort -n
```

### 找出長度最長的一行
```bash
awk '{if (length($0) > max) {max = length($0); line = $0}} END {print max, line}' filename.txt
```

### 找出長度最短的一行
```bash
awk '{if (length($0) < min || NR == 1) {min = length($0); line = $0}} END {print min, line}' filename.txt
```

### 篩選字元數大於指定長度的行（例如大於 10 個字元）
```bash
awk 'length($0) > 10' filename.txt
```

### 計算平均行長度
```bash
awk '{sum += length($0); count++} END {print (count ? sum/count : 0)}' filename.txt
```

### 排除空白行後計算字元數
```bash
grep -v '^$' filename.txt | awk '{print NR, length($0)}'
```

## 常見情境速查表

| 需求 | 指令 |
|------|------|
| 逐行字元數（含行號） | `awk '{print NR, length($0)}' file.txt` |
| 僅印出字元數 | `awk '{print length($0)}' file.txt` |
| 統計字元數分佈 | `awk '{count[length($0)]++} END {for (n in count) print n, count[n]}' file.txt \| sort -n` |
| 找出最長行 | `awk '{if (length($0) > max) {max = length($0); line = $0}} END {print max, line}' file.txt` |
| 計算平均行長 | `awk '{sum += length($0); count++} END {print sum/count}' file.txt` |
