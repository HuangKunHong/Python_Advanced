from openpyxl import Workbook
wb = Workbook()
ws = wb.active
print(ws.title)

wb.save(r"C:\Users\黄坤宏\Documents\Python\Python_Advanced\02_办公自动化\test.xlsx")