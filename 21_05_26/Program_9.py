import openpyxl

wb = openpyxl.load_workbook(r"C:\Users\Akash\Desktop\01_IPS\21_05_26\sales data.xlsx")

worksheet = wb.active
total = 0

for row in worksheet.iter_rows(values_only=True,max_row=10,min_row=2):
    if row[8] =="Tablet":
        total += row[2]

print(total)