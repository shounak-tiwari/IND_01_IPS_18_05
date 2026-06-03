class datapackets:
    def __init__(self,x):
        self.__dataRef = x
    def getRef(self):
        return self.__dataRef

obj = datapackets(1000)
print(obj.getRef())