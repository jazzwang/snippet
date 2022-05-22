import xlwings as xw
app = xw.App()
wb = app.books.add()
sheet = wb.sheets['Sheet1']
sheet.range('A1').value = [['Foo 1', 'Foo 2', 'Foo 3'], [10.0, 20.0, 30.0]]
import matplotlib.pyplot as plt
fig = plt.figure()
plt.plot([1, 2, 3, 4, 5])
sheet.pictures.add(fig, name='MyPlot', top=100, left=100, update=True)
wb.save("sample.xlsx")