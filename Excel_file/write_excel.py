# install openpyxl use command "pip install openpyxl"

from openpyxl import Workbook
wb = Workbook()

sheet = wb.active
'''
sheet['A1'] = "Anand"
sheet['A4'] = "Pratap"
sheet['A7'] = "Singh"
'''
testdata = [['Name','City'],['Anand','Gonda'],['Dhun','Lucknow']]
for data in testdata:
    sheet.append(data)
wb.save("abc.xlsx")