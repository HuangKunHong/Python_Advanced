from openpyxl import Workbook

wb = Workbook()

ws1 = wb.active

print(ws1.title)

print(wb.sheetnames)