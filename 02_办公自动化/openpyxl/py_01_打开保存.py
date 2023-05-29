from openpyxl import Workbook, load_workbook

# wb = Workbook()
wb = load_workbook(r"C:\Users\黄坤宏\Documents\Python\Python_Advanced\02_办公自动化\openpyxl\test.xlsx")
ws = wb.active
print(ws.title)

wb.save(r"C:\Users\黄坤宏\Documents\Python\Python_Advanced\02_办公自动化\openpyxl\test.xlsx")