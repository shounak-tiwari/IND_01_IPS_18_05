'''
Access specifiers :
1. public  or defult 
2. private 
3. protected 
'''
class AccessSpef:
    def __init__(self):
        # public : access everywere 
        self.Name = "ips"
        # protected  _ : access in same and their child 
        self._PhoneAdmin = "Null"
        # private  _ _ : not access from outside of class 
        self.__TotalIncome = "150cr"
        
Obj = AccessSpef()
print(Obj.Name)
print(Obj._PhoneAdmin)
print(Obj.__TotalIncome)