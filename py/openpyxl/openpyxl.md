# openpyxl

- PyPI
  - https://pypi.org/project/openpyxl/
- Git Repo
  - https://foss.heptapod.net/openpyxl/openpyxl
- Homepage
  - https://openpyxl.readthedocs.io/en/stable/

## 2025-03-31

- 緣起：
  - 用 pandas 處理 TSV (Tab 分隔) 檔案，問 Gemini 可否將 DataFrame 存成 Excel。看起來 `df.to_excel(excel_file, index=False)` 可以辦得到，但是需要裝 `openpyxl` 套件。
  - `df.to_excel(excel_file, index=False)` writes the DataFrame to an Excel file. The `index=False` argument prevents the DataFrame index from being written to the Excel file.

- https://g.co/gemini/share/25434a5296ba

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->

Can Python openpyxl create multiple worksheets?

</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->

Yes, the Python `openpyxl` library is fully capable of creating and managing multiple worksheets within an Excel (.xlsx) file. Here's a breakdown of how it works:

**Key Functionality:**

* **`Workbook.create_sheet()`:**
    * This method is used to add new worksheets to an existing or newly created workbook.
    * You can specify the title of the new worksheet, and also its position within the workbook's tab order.
* **Accessing Worksheets:**
    * You can access existing worksheets by their names or by their index within the workbook.
* **Workbook.sheetnames:**
    * This attribute provides a list of all the sheet names within the workbook.

**Example Code:**

```python
from openpyxl import Workbook

# Create a new workbook
wb = Workbook()

# Create multiple worksheets
ws1 = wb.create_sheet("Sheet1")
ws2 = wb.create_sheet("Sheet2")
ws3 = wb.create_sheet("Summary", 0) #insert sheet at the begining of the workbook.

# Optionally, you can add data to the worksheets
ws1["A1"] = "Data in Sheet1"
ws2["B2"] = "Data in Sheet2"
ws3["C3"] = "Summary Data"

# Get a list of sheet names
print(wb.sheetnames)

# Save the workbook
wb.save("multiple_sheets.xlsx")
```

**Explanation:**

1.  **`Workbook()`:** Creates a new Excel workbook.
2.  **`wb.create_sheet("Sheet1")`:** Creates a new worksheet named "Sheet1".
3.  **`wb.create_sheet("Summary", 0)`:** creates a new sheet named "Summary" and places it at the first index position within the workbook.
4.  **`wb.sheetnames`:** prints a list of the sheet names that are contained within the workbook.
5.  **`wb.save("multiple_sheets.xlsx")`:** Saves the workbook with all the created worksheets.

Therefore, `openpyxl` is well-suited for tasks that require generating Excel files with multiple worksheets, such as:

* Reporting
* Data organization
* Creating dashboards

</td></tr></table>

-https://g.co/gemini/share/87a167649555

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->

how can pandas write to different worksheet using openpyxl?

</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->

When using Pandas to write data to different worksheets in an Excel file, you leverage the `ExcelWriter` class, specifying the `openpyxl` engine. This method allows you to control which DataFrames go to which sheets.

Here's a breakdown of how to achieve this:

**Key Concepts:**

* **`pd.ExcelWriter`:**
    * This class is essential for writing multiple DataFrames to an Excel file.
    * It acts as a context manager, ensuring that the Excel file is properly saved and closed.
* **`to_excel()`:**
    * The DataFrame's `to_excel()` method is used to write the DataFrame's content to a specific sheet within the Excel file.
    * You specify the `ExcelWriter` object and the `sheet_name` argument to control where the data goes.
* **`openpyxl` Engine:**
    * By specifying `engine='openpyxl'`, you ensure that Pandas uses the `openpyxl` library to handle the Excel file, which is necessary for more advanced Excel operations.

**Example Code:**

```python
import pandas as pd

# Create sample DataFrames
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})
df3 = pd.DataFrame({'E': [13, 14, 15], 'F': [16, 17, 18]})

# Create an ExcelWriter object
with pd.ExcelWriter('multiple_sheets.xlsx', engine='openpyxl') as writer:
    # Write each DataFrame to a different sheet
    df1.to_excel(writer, sheet_name='Sheet1', index=False)
    df2.to_excel(writer, sheet_name='Sheet2', index=False)
    df3.to_excel(writer, sheet_name='Summary', index=False)

print("Excel file with multiple sheets created successfully!")
```

**Explanation:**

1.  **Import Pandas:**
    * Imports the Pandas library.
2.  **Create DataFrames:**
    * Creates sample DataFrames to write to the Excel file.
3.  **Create ExcelWriter:**
    * Creates an `ExcelWriter` object, specifying the output file name and the `openpyxl` engine.
4.  **Write DataFrames:**
    * Uses the `to_excel()` method to write each DataFrame to a different sheet within the Excel file.
    * `index=False` prevents the index from being written to the excel sheet.
5.  **File Saving:**
    * The `with` statement ensures that the Excel file is properly saved and closed when the block of code is finished.

This approach provides a clean and efficient way to write multiple DataFrames to separate worksheets in an Excel file using Pandas and `openpyxl`.

</td></tr></table>