'''
Oops is a way of wrting program by using classes and objects , object are represent the real thingd and attributes and methods, and the classes is a blue print of program 

a. Organizes code using classes and object 
b. Keeps related data and actions tgether 
c. one classes use features of another. 
d. allows the same methods to work in different ways 


Piller of oops 
Major pillers 
a. Encapsulation  
b. Inheritance 
c. Polymorphisms 
d. Abstraction 

Minor pillers 
a. class & objects 
b. Message Passing and Dynamic Binding 
c. Modularity and Reusability 

Advance oops based on 5 design principles  
    SOLID 
S - Single responsibility principle 
    A class should have one respobility 
    Student : Class stores students data.
    StudentReport : Class generated reports.
O - Open/Closed Princial (OCP): 
    Software entities should be one for extesion but closed for modifications
    Add a new payment method by creating new classes instead of changing existing payment code 
L : Liskov Substitution principle : 
    if dog inherits from animal, dog should behave like an animal whereever animal is expected 
I : Interfce Segregation principle ( ISP)
 Clients sould not be forced t depend on methods they do not use . 
    Use small , specific interfaces instead of one large interface with many unnecessary methods 
D : Dependency Inversion Priciple (DIP)
Depend on abstractions , not concreate classes 
'''

# Class : it is blueprints for creating objects , it is consists from attributes and methods, python classes is creating using class keywords , in python scope of methods and attributes are always oublic 

# creating a class 
class Student:
    studentName = input("Enter the name : ")
# object in a class 
Stud = Student
