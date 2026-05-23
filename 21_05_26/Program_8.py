import openpyxl
wb = openpyxl.load_workbook(r"C:\Users\Akash\Desktop\01_IPS\21_05_26\Book1.xlsx")
worksheet = wb.active
for row in worksheet.iter_rows(min_row=2,values_only=True):
    print(row[0])
