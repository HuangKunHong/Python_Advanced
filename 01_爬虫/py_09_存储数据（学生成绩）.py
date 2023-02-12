import xlwt
import random

# 实例化workbook
workbook = xlwt.Workbook(encoding = "utf8")

#  添加sheet
sheet1 = workbook.add_sheet('sheet1')
sheet2 = workbook.add_sheet('爬虫成绩')

# 输入数据
sheet1.write(0,0, "name")
sheet1.write(0,1, "chinese")
sheet1.write(0,2, "math")
sheet1.write(0,3, "english")

for row in range(1, 51, 1):
    for col in range(1,4,1):
        sheet1.write(row,col, random.randint(50, 100))

# 保存EXCEL
workbook.save(r'D:\Users\Administrator\Desktop\期末成绩.xls')
