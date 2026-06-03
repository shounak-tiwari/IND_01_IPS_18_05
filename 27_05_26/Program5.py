# variable length args 

def add(*x):
    total = 0
    for i in x:
        total +=i
    return total

print(add(10,20,30,40,50,60,70))