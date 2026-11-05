# 'find' command

```bash
FIND(1)                                   General Commands Manual                                   FIND(1)

NAME
       find - search for files in a directory hierarchy

SYNOPSIS
       find [-H] [-L] [-P] [-D debugopts] [-Olevel] [starting-point...] [expression]
```

## 2025-05-26

- Model: Gemini 2.5 Flash
> [!NOTE]
> can I list empty files using linux command like find or ls?


Yes, you can definitely list empty files using Linux commands like `find` and `ls`.

Here's how:

### Using `find`

The `find` command is the most powerful and flexible tool for this. You can specify the size of the file.

* **To find empty files (size 0 bytes) in the current directory and its subdirectories:**

```bash
find . -type f -empty
```

* `.`: Starts the search in the current directory. You can replace this with any path (e.g., `/home/user`).
* `-type f`: Specifies that you are looking for files (not directories).
* `-empty`: This is the key option that specifically looks for empty files or directories.

* **To find empty files and then list them with more details (like `ls -l` output):**

```bash
find . -type f -empty -ls
```

* **To find empty files and then execute a command on them (e.g., remove them):**
* **Be extremely careful with `rm`! Always test with `-print` or `-ls` first.**

```bash
find . -type f -empty -exec rm {} \;
```

or, a safer alternative for `rm` with `find`:

```bash
find . -type f -empty -delete
```

(Note: `-delete` is generally safer as it avoids issues with filenames containing spaces or special characters that `-exec rm {} \;` might encounter if not handled carefully).

### Using `ls` and `awk` (or `grep`)

While `ls` itself doesn't have a direct option to filter for empty files, you can combine it with other commands like `awk` or `grep` to achieve this. This method is generally less efficient for large directories than `find`.

* **To list files and filter for those with size 0 using `ls -l` and `awk`:**

```bash
ls -l | awk '$5 == 0 && $1 ~ /^-/' {print $9}'
```

* `ls -l`: Lists files in long format, showing permissions, owner, size, etc.
* `awk '$5 == 0'`: `awk` processes the output of `ls -l`. `$5` refers to the fifth field in the `ls -l` output, which is the file size. This condition checks if the size is 0.
* `$1 ~ /^-/`: This is an important addition. In `ls -l` output, the first field indicates the file type and permissions. `^-` means it's a regular file (not a directory `d`, symbolic link `l`, etc.). This prevents `awk` from incorrectly identifying empty directories as empty files.
* `{print $9}`: Prints the ninth field, which is the filename.

* **To list files and filter for those with size 0 using `ls -s` and `grep` (less reliable as `ls -s` shows block size):**
This method is generally not recommended for precisely identifying 0-byte files, as `ls -s` shows allocated block size, not actual file size, and an empty file might still occupy a small block. However, if you're looking for files that consume 0 blocks:

```bash
ls -s | grep '^0 '
```

* `ls -s`: Lists files with their allocated block size.
* `grep '^0 '`: Filters for lines that start with "0 " (meaning 0 blocks).

**In summary, for finding empty files, `find . -type f -empty` is the most robust and recommended approach.**
---

## 2025-07-24

- Model: Gemini 2.5 Flash

> [!NOTE]
> how to use `find` command to fetch linux file that created on 2025-07-23


To find Linux files created on a specific date using the `find` command, you'll typically use the `-newermt` option (for "newer than modification time").

Here's how you would find files created on 2025-07-23:

```bash
find . -type f -newermt "2025-07-23 00:00:00" ! -newermt "2025-07-24 00:00:00"
```

Let's break down this command:

* **`find .`**: This tells `find` to start searching in the current directory (`.`) and its subdirectories. You can replace `.` with any other starting directory you wish to search (e.g., `/home/youruser`, `/var/log`).
* **`-type f`**: This limits the search to regular files only. If you want to include directories, symbolic links, etc., you can remove this option, or use other types (e.g., `d` for directories).
* **`-newermt "2025-07-23 00:00:00"`**: This finds files that were *modified* at or after the beginning of July 23, 2025.
* **`! -newermt "2025-07-24 00:00:00"`**: The `!` negates the next condition. This part ensures that you *exclude* files modified at or after the beginning of July 24, 2025.

By combining these two conditions, you effectively select files that have a modification timestamp within the 24-hour period of July 23, 2025.

**Important Considerations:**

* **Modification Time vs. Creation Time:** The `find` command primarily works with *modification time* (`mtime`), *access time* (`atime`), and *change time* (`ctime`). Linux filesystems generally do not store a true "creation time" in the same way some other operating systems do. When people refer to "created on," they often mean the last modification time.
* **Accuracy:** The timestamp accuracy depends on the filesystem.
* **Time Zone:** The timestamps used by `find` are typically based on the system's local time zone.
* **Alternative for Creation Time (if available and needed):** While `find` doesn't directly use creation time, some newer filesystems (like ext4 with the `CONFIG_EXT4_ENCRYPT` option enabled, or Btrfs, XFS) *do* store a creation timestamp (often called "birth time" or "btime"). If you absolutely need creation time, you might need to use a tool like `stat` in conjunction with `find` or use a more specialized utility if your system and filesystem support it. However, for most common scenarios, modification time is what's used.

For your request, assuming "created on" refers to the modification date, the command provided above is the standard and most effective way to achieve it with `find`.
---

## 2026-11-04

- TOOL: Google Search - AI Mode

> [!NOTE]
> 如何用 find 指令找出最近 12 小時有異動的檔案

要找出最近 12 小時內有異動（內容被修改）的檔案，最推薦且直覺的作法是使用 `-mmin` 參數（以分鐘為單位）。因為 12 小時等於 720 分鐘，所以在 `find` 指令中加入 `-mmin -720` 即可。 [1] (https://blog.longwin.com.tw/2017/08/linux-find-limit-date-time-file-2017/), [2] (https://random168.blogspot.com/2016/11/linux-find-02.html)
以下是完整的指令與說明：
```bash
find /path/to/search -type f -mmin -720
```

### 📋 參數拆解說明

• `/path/to/search`：你要搜尋的目標目錄路徑（例如：當前目錄可以用 .，系統日誌可以用 `/var/log`）。 [1] (https://www.ccc.tc/notes/18), [2] (https://ssorc.tw/939/find-command-finds-files-with-time-changes/)
• `-type f`：指定只尋找「一般檔案」，排除資料夾。 [1] (https://wiki.freedomstu.com/books/linux-%E7%B3%BB%E7%B5%B1%E8%A8%98%E9%8C%84/page/linux-find), [2] (https://www.ccc.tc/notes/18)
• `-mmin -720`：
	• `mmin` 代表 modification time (以分鐘為單位)。
	• `-720` 中的減號 - 代表「小於」，也就是 720 分鐘（12 小時）以內。 [1] (https://blog.longwin.com.tw/2017/08/linux-find-limit-date-time-file-2017/), [2] (https://random168.blogspot.com/2016/11/linux-find-02.html)

### 💡 補充：如果是權限或狀態異動？

Linux 的時間屬性分為三種，如果你說的「異動」不是指檔案內容，請依需求更換參數： [1] (https://ssorc.tw/939/find-command-finds-files-with-time-changes/)

• 內容被修改（最常用）：使用 `-mmin -720`（Modification Time）
• 權限、屬性、檔名被更改：使用 `-cmin -720`（Change Time）
• 檔案被讀取、存取：使用 `-amin -720`（Access Time） [1] (https://blog.longwin.com.tw/2017/08/linux-find-limit-date-time-file-2017/), [2] (https://random168.blogspot.com/2016/11/linux-find-02.html)

(註：部分 Linux 系統的 find 版本也支援以天為單位的 -mtime -0.5，但使用 -mmin 以分鐘計算在各平台最為通用且精準。) [1] (https://zhuanlan.zhihu.com/p/421825066), [2] (https://blog.longwin.com.tw/2017/08/linux-find-limit-date-time-file-2017/), [3] (https://random168.blogspot.com/2016/11/linux-find-02.html)

請問你接下來需要對這些找到的檔案進行其他操作嗎？例如：

• 想要列出詳細資訊（如修改時間、檔案大小）？
• 想要直接將它們複製、移動或刪除？
• 需要排除特定的子目錄或限制特定的擴充檔名？

