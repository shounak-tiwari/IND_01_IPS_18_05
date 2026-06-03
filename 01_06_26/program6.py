# Single level  inheritance 
class Student:
    def __init__(self):
        self.name = input("Enter the name : ")
        self.email = input("Enter the email : ")
        self.address =  input("Enter the address : ")    
    def output(self):
        print("Name of student : ",self.name)
        print("Email of student : ",self.email)
        print("Address of student : ",self.address)
class StudentRecord(Student):
    def __init__(self):
        super().__init__()
        self.grade = input("enter the grade : ")
        self.cgpa = input("enter the cgpa : ")
        self.sgpa = input("enter the sgpa : ")
    def output(self):
        super().output()
        print("Grade of student : ",self.grade)
        print("CGPA of student : ",self.cgpa)
        print("SGPA of student : ",self.sgpa)
studeObj = StudentRecord()
studeObj.output()