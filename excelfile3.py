import openpyxl 
from openpyxl.chart import BarChart,Reference

wb = openpyxl.Workbook() 
sheet = wb.active

sheet['A1'] = 'Name'
sheet['A2'] = 'Amit'
sheet['A3'] = 'Rahul'
sheet['A4'] = 'Rohit'
sheet['A5'] = 'Ajit'


sheet['B1'] = 'Age'
sheet['B2'] = 35
sheet['B3'] = 32
sheet['B4'] = 37
sheet['B5'] = 40




wb.save("barchart.xlsx") 
print('Excel File has created')
