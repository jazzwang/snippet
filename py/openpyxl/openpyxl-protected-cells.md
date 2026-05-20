- Google Search - AI Mode

> where can I find openpyxl cell Protection class?

You can find the cell Protection class in the openpyxl.styles.protection module. It is typically imported directly from the openpyxl.styles package. [1, 2] 

[python - how can i locked the specific columns in excel ...](https://stackoverflow.com/questions/77512999/how-can-i-locked-the-specific-columns-in-excel-using-openpyxl)
[Python×Excel】Formatting Cells(Alignment, Protection, Number ...](https://www.shibutan-bloomers.com/python_libraly_openpyxl-5_en/5294/)

## Importing the Class
To use the cell protection features, import the class like this: [2] 

from openpyxl.styles import Protection

## Basic Usage Example
In Excel, all cells are marked as "locked" by default, but this restriction is not active until you turn on sheet-level protection. [2, 3] 
The following example shows how to explicitly lock or unlock individual cells and enforce the rule: [2] 

```python
from openpyxl import Workbookfrom openpyxl.styles import Protection
wb = Workbook()ws = wb.active
# 1. Access a cellcell_a1 = ws['A1']cell_b1 = ws['B1']
# 2. Configure protection settings (locked or hidden formulas)
cell_a1.protection = Protection(locked=True, hidden=True)    # Fully protected
cell_b1.protection = Protection(locked=False, hidden=False)  # Editable by user
# 3. CRITICAL STEP: Turn on the worksheet's overall sheet protection
ws.protection.sheet = True
ws.protection.password = "your_secure_password" # Optional password

wb.save("protected_workbook.xlsx")
```

## Available Parameters
When initializing a Protection object, you can pass two boolean parameters: [1, 4] 

* locked (True/False): Restricts users from editing the cell data when the sheet is protected. Defaults to True.
* hidden (True/False): Hides cell formulas from displaying in the Excel formula bar when the sheet is protected. Defaults to False. [1, 2, 5, 6] 

If you would like to explore further, let me know if you need help with protecting entire columns at once or configuring advanced workbook-level safety settings. [3, 7] 

[1] [https://openpyxl.readthedocs.io](https://openpyxl.readthedocs.io/en/3.1/api/openpyxl.styles.protection.html)
[2] [https://groups.google.com](https://groups.google.com/g/openpyxl-users/c/fNtQ_WuqoqQ)
[3] [https://stackoverflow.com](https://stackoverflow.com/questions/75089393/python-openpyxl-want-to-protect-a-sheet-but-allow-filtering-sorting-on-all-co)
[4] [https://openpyxl.readthedocs.io](https://openpyxl.readthedocs.io/en/3.1/protection.html)
[5] [https://www.outsystems.com](https://www.outsystems.com/forums/discussion/91255/advanced-excel-remove-protection-of-cells-and-other-general-formatting-options/)
[6] [https://xinetzone.github.io](https://xinetzone.github.io/openpyxl/api/openpyxl.worksheet.protection.html)
[7] [https://stackoverflow.com](https://stackoverflow.com/questions/45220389/protecting-workbook-in-openpyxl)

> how to remove protection of given range, e.g. B23:F28

To unlock a specific range of cells in openpyxl, you must loop through every cell within that range, set its locked attribute to False, and ensure sheet protection is enabled.

## Python Code Example

```python
from openpyxl import Workbookfrom openpyxl.styles import Protection
wb = Workbook()ws = wb.active
# Fill some sample datafor row in ws.iter_rows(min_row=20, max_row=30, min_col=1, max_col=7, value="Data"):
    pass
# 1. Define the range you want to unlocktarget_range = ws['B23:F28']
# 2. Loop through every cell in that specific rangefor row in target_range:
    for cell in row:
        # Set locked to False to allow user edits
        cell.protection = Protection(locked=False)
# 3. CRITICAL: Enable sheet protection so the rest of the sheet remains locked
ws.protection.sheet = True
ws.protection.password = "your_password"

wb.save("unlocked_range.xlsx")
```

## Key Rules to Remember

* Excel's Default Behavior: Excel treats all cells as locked by default.
* The Mechanism: By explicitly setting locked=False on B23:F28, you turn off protection only for those cells. Everything else outside that block stays protected.
* The Toggle: If you omit ws.protection.sheet = True, Excel ignores individual cell restrictions, and the whole sheet remains editable.

If you are working with dynamic data, I can show you how to automatically detect the last row or how to unprotect entire columns based on header names. Let me know how you want to proceed!