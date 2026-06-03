# polymorphisms : polymorphisms is laten greek word which divide poly and morphisms , poly means many and morphisms means forms , we have two types of poly morphisms 
# a. compile time polymorphisms : Python does not support true compile-time polymorphism (also known as static polymorphism or method overloading) because it is a dynamically typed, interpreted language. In languages like C++ or Java, the compiler looks at a method's parameters at compile time to bind it to a specific signature. In Python, if you define multiple methods with the exact same name, the final definition simply overrides all previous ones

    # 1. Function/method overloading : is refers to multiple methods with same and different parameters 
    # 2. Operator Overloading 
# b. run time polymorphisms : it works on runtime
    # 1. method overriding  : in method overriding the method of parent class is define or redefine in child class 
from multipledispatch import dispatch
# Function overloading 
class Poly:
    @dispatch(int)
    def intro(self, x):
        return x
    @dispatch(int,int)
    def intro(self, x,y):
        return x+y
    @dispatch(int,int,int)   
    def intro(self, x,y,z):
        return x+y+z
PolyObj = Poly()
print(PolyObj.intro(10))