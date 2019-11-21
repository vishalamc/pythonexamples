import pandas as pd
from pandas import ExcelWriter
#create dataframe which hold some data
df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})

writer = ExcelWriter('simple.xlsx')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Save the Excel file 
writer.save()
print("Excel File has created")
