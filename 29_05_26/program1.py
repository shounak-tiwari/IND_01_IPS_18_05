
def add(x:int,y:int)->int:
        if not (type(x) is int and type(y) is int):
            raise TypeError
        else:
            return x+y
                        


# calling of function 
print(add(10.90,15.90))
