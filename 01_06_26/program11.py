# encapsulation is major piller of oops which refers to wrape the data into a single unit , and not able to direct call from objects or child's objects 
class info:
    def setData(self,x):
        self.__amount =x 
    def getData(self):
        return self.__amount

i  = info()
i.setData(100)
print(i.getData())