class Animal:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    
    def output(self):
        print("The name of Animal : ",self.name)
        print("The age of Animal : ",self.age)
    
objAnimal = Animal("Koko","9 months")
objAnimal.output()