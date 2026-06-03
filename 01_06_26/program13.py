# abstraction
# hide implementation and show neccessary details
from abc import ABC,abstractmethod
class Area(ABC):
    @abstractmethod
    def area(self,l,b):
        return l*b
    
class RA(Area):
    def area(self, l, b):
        return super().area(l, b)  
 
A = RA()
print(A.area(10,20))