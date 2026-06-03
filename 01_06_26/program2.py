# Constructor : Constructor is a special methods in oops which is automatically call when object is declare with the class and construct memory or allocate memory for attirbutes.. 
# we have 3 type of construtor in python: 
'''
a. default constructor 
b. parameterized constructor 
c. copy constructor 
'''
class Student:
    def __init__(self):
        self.name  = str(input("Enter the name of student : "))
        self.email   = str(input("Enter the email of student : "))
        self.address = str(input("Enter the address of student : "))
    def outputDetails(self):
        print("Name of student : ",self.name)
        print("Email of student : ",self.email)
        print("Address of student : ",self.address)

try:
    # create object 
    Stud1 = Student()

except AttributeError as e:
    print(e)