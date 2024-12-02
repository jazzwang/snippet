import pandas as pd
import xlwings as xw
app = xw.App()
wb = app.books.add()
sheet = wb.sheets['Sheet1']
sheet.range('A1').value = [['ID', 'Name', 'Age'], [1, "Jazz", 45], [2, "Thomas", 38], [3, "John", 35]]
wb.save("lab2-input.xlsx")
df1 = sheet.range('A1').options(pd.Series, expand="table").value

ref = app.books.add()
ref.sheets[0].range('A1').value = [['ID', 'Name', 'Salary'], [1, "Jazz", 200], [2, "Thomas", 108], [3, "John", 135]]
ref.save("lab2-ref.xlsx")
df2 = ref.sheets[0].range('A1').options(pd.Series, expand="table").value

df3 = pd.merge(df1, df2, on="ID")

output = app.books.add()
output.sheets[0].range('A1').value = df3
output.save("lab2-output.xlsx")

output.close()
ref.close()
wb.close()

app.quit()