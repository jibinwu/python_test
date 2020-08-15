import xlrd
#获取一个excel对象
file=r'C:\Users\Administrator\Desktop\测试添加车辆接口.xls'
data=xlrd.open_workbook(file)
sheet_names=data.sheet_names()
print(sheet_names)
print(sheet_names[0])

sheet1=data.sheet_by_index(0)
# print(sheet1)
# data.sheet_by_name('三要素')
# print(sheet1)
rows=sheet1.nrows
print(rows)
columns=sheet1.ncols
print(columns)

row_data_1=sheet1.row_values(0)
print(row_data_1)
col_data_1=sheet1.col_values(0)
print(col_data_1)

for t in range(1,rows):
    row_value=sheet1.row_values(t)
    print(row_value)

cell_value1=sheet1.cell_value(1,0)
print(cell_value1)