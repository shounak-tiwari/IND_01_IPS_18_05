class ParentClass:
    def show(self):
        print("Hey I'm base class ")

class ChildClass(ParentClass):
    def show(self):
        super().show()
        print("Hey I'm Child Class")


chdObj = ChildClass()
chdObj.show()