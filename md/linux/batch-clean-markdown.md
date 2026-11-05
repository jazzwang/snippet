# Batch Clean Markdown 筆記

**日期**: 2026-11-05  
**主題**: Vim 與 sed/awk 批次處理 markdown 分隔符號

---

## 問題背景

在 Vim 中想要取代多行模式：

```vim
"s#^\n^---\n##g
```

對應的 **sed** 和 **awk** 指令，並實現以下目標：

### 目標效果

**原始內容**（三行特徵）：
```
## 標題

---

---

---

## 內容
```

**處理後**（清除重複分隔符號）：
```
## 標題

---

## 內容
```

---

## Vim → sed 對應

### Vim 指令說明

```vim
:s#^\n^---\n##g
```

- `s` = substitute（取代）
- `#` = delimiter（分隔符）
- `^\n` = 行首 + 換行
- `^---\n` = 行首 `---` + 換行
- `g` = global（全域取代）

### sed 對應方法

#### 方法 1：基礎取代
```bash
sed 's/^---/\n/g' file
```

#### 方法 2：使用 `-z` 處理多行（推薦）
```bash
sed -z 's/^\n^---\n//g' file
```

#### 方法 3：全域取代
```bash
sed ':a;N;$!ba;s/\n---\n/\n/g' file
```

**說明**：
- `:a;N;$!ba` 讀取整個文件（逐行累積）
- `s/\n---\n/\n/g` 將 `---` 及其前後換行替換為單個換行

#### 方法 4：直接刪除
```bash
sed '/^---$/d' file
```

---

## Vim → awk 對應

### awk 方法 1：逐行處理（推薦）

```bash
awk '
/^---$/ {
    # 如果上一行也是 ---，則跳過這一行
    if (prev_is_dash) {
        next
    }
    prev_is_dash = 1
    print
    next
}
{
    prev_is_dash = 0
    print
}
' file
```

**優點**：
- 簡單易懂
- 逐行處理，效率好
- 可擴展（可加入更多條件）

### awk 方法 2：記錄分隔符（RS）

```bash
awk 'BEGIN { RS = "\n---\n"; ORS = "\n---\n" }
{
    gsub(/^$/,"", $0)
    gsub(/\n+$/, "", $0)
    print $0
}
' file
```

**說明**：
- `RS` = Record Separator（記錄分隔符）
- `ORS` = Output Record Separator（輸出記錄分隔符）

### awk 方法 3：使用 gsub

```bash
awk '{
    gsub(/^\n^---\n/, "", $0)
    gsub(/\n---\n/, "\n---\n", $0)
    print
}' file
```

### awk 方法 4：記錄合併

```bash
awk '
BEGIN { p1 = ""; p2 = "" }
{
    if (p1 == "---" && p2 == "" && $0 == "") {
        print ""
        p2 = p1
        p1 = $0
        next
    }
    
    if ($0 == "") {
        if (p1 == "") {
            print ""
        }
        p2 = p1
        p1 = $0
    } else {
        p2 = p1
        p1 = $0
        print
    }
}
END {
    if (p1 == "---" && p2 == "") print ""
}
' file
```

### awk 方法 5：使用 getline 讀取多行

```bash
awk '
/^---/ {
    getline nextline
    getline nextnextline
    print nextline
    next
}
{
    print
}
' file
```

---

## 三行特徵轉換為一行空白行

### 原始內容
```
## 標題

---

---

---

## 內容
```

### 目標結果
```
## 標題

---

## 內容
```

---

## 方法比較

| 工具 | 命令 | 特點 | 適用場景 |
|------|------|------|---------|
| **sed** | `sed -z 's/^\n^---\n//g' file` | 簡單直觀 | 快速處理 |
| **sed** | `sed ':a;N;$!ba;s/\n---\n/\n/g' file` | 全域取代 | 保留分隔符 |
| **perl** | `perl -0777 -pe 's/\n---\n/\n/g' file` | 一鍵完成 | 處理整個文件 |
| **awk** | 逐行處理 | 可擴展 | 複雜條件 |
| **awk** | 記錄分隔符 | 精確控制 | 多行模式 |

---

## 批次處理方法

### 方法 1：vim -es（ex 模式，非互動）

```bash
# 處理單一檔案
vim -es ':%s/模式/取代/g | wq' file.txt

# 處理多個檔案
for file in *.txt; do
    vim -es ':%s/模式/取代/g | wq' "$file"
done
```

**參數說明**：
- `-e` = ex mode（命令模式）
- `-s` = silent mode（靜音模式，不顯示提示）

### 方法 2：vim -e（命令模式）

```bash
for file in *.txt; do
    vim -e -c ':%s/模式/取代/g' -c 'w' -c 'q' "$file"
done
```

### 方法 3：find + xargs

```bash
# 處理所有 .txt 檔案
find . -name "*.txt" -exec vim -es ':%s/模式/取代/g | wq' {} +

# 處理所有檔案
find . -type f -exec vim -es ':%s/模式/取代/g | wq' {} +
```

### 方法 4：vim :argdo

```bash
vim +argdo %s/模式/取代/g +wq file1 file2 file3
```

### 方法 5：sed/awk 批次處理（推薦）

```bash
#!/bin/bash
# batch_cleanup.sh

for file in *.md; do
    echo "Processing: $file"
    sed ':a;N;$!ba;s/\n---\n/\n/g' "$file" > "$file.tmp"
    mv "$file.tmp" "$file"
done
```

### 方法 6：find + sed -i（就地修改）

```bash
find . -name "*.md" -exec sed -i ':a;N;$!ba;s/\n---\n/\n/g' {} +
```

### 方法 7：find + perl（一鍵完成）

```bash
find . -name "*.md" -exec perl -i -0777 -pe 's/\n---\n/\n/g' {} +
```

---

## 完整範例腳本

### batch_clean_markdown.sh

```bash
#!/bin/bash

# 批次處理 markdown 分隔符號

echo "開始批次處理 markdown 分隔符號..."

# 處理所有 .md 檔案
for file in *.md; do
    if [ -f "$file" ]; then
        echo "處理: $file"
        
        # 方法 1：使用 sed
        sed ':a;N;$!ba;s/\n---\n/\n/g' "$file" > "$file.tmp"
        mv "$file.tmp" "$file"
        
        # 方法 2：使用 vim
        # vim -es ':%s/^\n^---\n//g | wq' "$file"
        
        # 方法 3：使用 awk
        # awk '
        # /^---$/ {
        #     if (prev_is_dash) next
        #     prev_is_dash = 1
        #     print
        #     next
        # }
        # {
        #     prev_is_dash = 0
        #     print
        # }
        # ' "$file" > "$file.tmp"
        # mv "$file.tmp" "$file"
        
        echo "完成: $file"
    fi
done

echo "批次處理完成！"
```

**使用方式**：
```bash
# 1. 賦予執行權限
chmod +x batch_clean_markdown.sh

# 2. 執行
./batch_clean_markdown.sh
```

---

## 安全建議

### 1. 先測試（不修改）

```bash
# 測試 sed 效果（輸出到新文件）
sed ':a;N;$!ba;s/\n---\n/\n/g' file.txt > output.txt

# 比較差異
diff file.txt output.txt

# 使用 vim 測試模式
vim -es ':%s/模式/取代/g | wq!' file1 file2
```

### 2. 使用備份

```bash
# 自動備份
sed ':a;N;$!ba;s/\n---\n/\n/g' "$file" > "$file.tmp"
mv "$file.tmp" "$file"

# 或使用 cp
cp "$file" "$file.bak"
sed ':a;N;$!ba;s/\n---\n/\n/g' "$file" > "$file.tmp"
mv "$file.tmp" "$file"
```

### 3. 使用 -b 避免詢問

```bash
# 使用 -b 參數避免詢問
vim -es -b ':%s/模式/取代/g | wq' file1 file2

# sed 的 -i 參數（就地修改）
sed -i ':a;N;$!ba;s/\n---\n/\n/g' file.txt
```

### 4. 使用 find 限制範圍

```bash
# 只處理特定目錄
find /path/to/dir -name "*.md" -exec sed -i ... {} +

# 只處理特定大小的檔案
find . -name "*.md" -size +1k -exec ... {} +
```

---

## 工具比較

### sed
```
✅ 簡單直觀
✅ 速度快
✅ 一鍵完成
❌ 多行模式需要特殊處理
❌ 正則表達式功能較少
```

### perl
```
✅ 一鍵完成（-0777 讀取整個文件）
✅ 正則表達式功能強大
❌ 需額外安裝
❌ 某些系統可能沒預設
```

### awk
```
✅ 可擴展（可加入更多條件）
✅ 逐行處理，效率好
✅ 記錄分隔符功能
❌ 語法較複雜
❌ 學習曲線較陡
```

### vim -es
```
✅ 簡單直接
✅ 可保留 vim 設定
✅ 批次處理方便
❌ 需手動輸入命令
❌ 處理速度較慢
```

### 綜合推薦
| 需求 | 推薦工具 |
|------|---------|
| 快速處理 | sed |
| 複雜條件 | awk |
| 一鍵完成 | perl |
| 保留 vim 設定 | vim -es |
| 安全測試 | sed 先輸出 |

---

## 範例測試

### 原始檔案 `input.txt`：

```markdown
## 標題

---

---

---

## 內容

---

---

結束
```

### 處理後：

```markdown
## 標題

---

## 內容

---

結束
```

### 測試命令：

```bash
# 測試 sed
sed ':a;N;$!ba;s/\n---\n/\n/g' input.txt

# 測試 awk
awk '/^---$/ {
    if (prev_is_dash) next
    prev_is_dash = 1
    print
    next
}
{
    prev_is_dash = 0
    print
}' input.txt

# 測試 perl
perl -0777 -pe 's/\n---\n/\n/g' input.txt
```

---

## 常見問題

### Q1: sed 處理多行失敗？
```bash
# 使用 -z 選項
sed -z 's/^\n^---\n//g' file

# 或使用讀取整個文件方法
sed ':a;N;$!ba;s/\n---\n/\n/g' file
```

### Q2: 批次處理失敗？
```bash
# 使用 find 限制範圍
find . -name "*.md" -size +1k -exec ...

# 或逐個處理
for file in *.md; do ... done
```

### Q3: 需要備份？
```bash
# 自動備份
cp "$file" "$file.bak"
# 或
sed 's/模式/取代/g' "$file" > "$file.tmp"
mv "$file.tmp" "$file"
```

### Q4: perl 沒安裝？
```bash
# 改用 sed 或 awk
sed ':a;N;$!ba;s/\n---\n/\n/g' file
# 或
awk '逐行處理' file
```

---

## 快速捷徑

```bash
# 一鍵處理所有 .md 檔案
find . -name "*.md" -exec sed -i ':a;N;$!ba;s/\n---\n/\n/g' {} +

# 使用 perl（一鍵完成）
find . -name "*.md" -exec perl -i -0777 -pe 's/\n---\n/\n/g' {} +

# 使用 awk（逐行處理）
find . -name "*.md" -exec awk '/^---$/ {if (prev_is_dash) next; prev_is_dash = 1; print; next} {prev_is_dash = 0; print}' {} +
```

---

## 參考資源

- [GNU sed 官方文檔](https://www.gnu.org/software/sed/manual/sed.html)
- [GNU awk 官方文檔](https://www.gnu.org/software/gawk/manual/gawk.html)
- [Vim 官方文檔](https://vimdoc.sourceforge.net/)
- [perl 官方文檔](https://perldoc.perl.org/perlretut)

---

*最後更新：2026-11-05*

