class Student:
    def inputDetails(self):
        self.name  = str(input("Enter the name of student : "))
        self.email   = str(input("Enter the email of student : "))
        self.address = str(input("Enter the address of student : "))
    def outputDetails(self):
        print("Name of student : ",self.name)
        print("Email of student : ",self.email)
        print("Address of student : ",self.address)
try:
    # creating object of class 
    StudObj = Student()
    # calling of input details function
    StudObj.inputDetails()
    # calling of output details function
    StudObj.outputDetails()
# when attributes is not found in memory / or it is not in scope 
except AttributeError as e:
    print(e)
# custom exceptions
except:
    print("May me some errors but not able to found ")