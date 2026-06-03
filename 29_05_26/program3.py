def decorator(x):
    def CubeX(Name):
        print(f"Hello : {Name} ")
        x()
    return CubeX

@decorator
def greet():
    print("Good Morning ")