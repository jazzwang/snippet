# java.time.format.DateTimeFormatter

## 2025-09-11

- 緣起：
  - 同仁生成的 export file 檔案命名時間戳記呈現 `202509253` 的格式，理論上應該是 `20250910` 才對。
  - 懷疑是格式字串寫錯，畢竟 `%d` 跟 `%D` 意義是不同的。
- 求證：
  - 2025-09-11 20:30 PM
  - By Google Gemini

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
create a Java program to show 2025-09-11 using two different format "yyyyMMdd", "yyyyMMDD"
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
```java
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class DateFormatterExample {

    public static void main(String[] args) {
        // Define the target date: September 11, 2025
        LocalDate date = LocalDate.of(2025, 9, 11);

        // Format the date using "yyyyMMdd"
        DateTimeFormatter formatter1 = DateTimeFormatter.ofPattern("yyyyMMdd");
        String formattedDate1 = date.format(formatter1);

        // Format the date using "yyyyMMDD"
        DateTimeFormatter formatter2 = DateTimeFormatter.ofPattern("yyyyMMDD");
        String formattedDate2 = date.format(formatter2);

        // Print the results
        System.out.println("Date formatted as \"yyyyMMdd\": " + formattedDate1);
        System.out.println("Date formatted as \"yyyyMMDD\": " + formattedDate2);
    }
}
```

This Java program demonstrates the use of **`DateTimeFormatter`** to display a specific date in two different formats. It highlights the distinction between lowercase 'd' and uppercase 'D' in the format string.

-----

### Explanation of Format Patterns

The difference between the two format patterns lies in the interpretation of the 'd' and 'D' characters.

  * **`yyyyMMdd`**: This is a common pattern for representing a date.

      * **`yyyy`**: Represents the **year** with all four digits (e.g., 2025).
      * **`MM`**: Represents the **month** of the year (e.g., 09 for September).
      * **`dd`**: Represents the **day of the month** (e.g., 11). This pattern yields the expected date string **"20250911"**.

  * **`yyyyMMDD`**: This pattern is a bit different because of the uppercase 'D'.

      * **`yyyy`**: Represents the **year** with all four digits.
      * **`MM`**: Represents the **month** of the year.
      * **`DD`**: Represents the **day of the year**. The 11th of September is the **254th day** of a non-leap year. This pattern results in the string **"202509254"**.

The `java.time` package, introduced in Java 8, is the modern API for handling dates and times. It provides robust and clear classes like `LocalDate` and `DateTimeFormatter`, which are generally preferred over the older `java.util.Date` and `java.text.SimpleDateFormat`.
</td></tr></table>