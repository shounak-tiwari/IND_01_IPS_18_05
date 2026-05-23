'''
cat : Furniture
state : california
calulcate total profit, quantity  , sales 
'''

stateList = [] 
# import required library 
import openpyxl
# load workbook 
wb = openpyxl.load_workbook(r"C:\Users\Akash\Desktop\IPS_DATA\Superstore-1.xlsx")
sheet = wb["Orders"]

totalsales  =0 
totalprofit =0 
totalquantity =0
for data in sheet.iter_rows(min_row=1, values_only=True):
    if data[14] == "Furniture" and data[10]=="California":
        totalsales += data[17]
        totalquantity += data[18]
        totalprofit += data[20]
    #     if data[10] not in stateList:
    #         stateList.append(data[10])
# for state in stateList:
#     print(state)
# print(len(stateList))
print("Total sales ",totalsales)
print("Total quanity ",totalquantity)
print("Total profit ",totalprofit)