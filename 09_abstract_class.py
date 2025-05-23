# 9. Abstract Classes and Methods

# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().
from abc import abstractmethod, ABC

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Reactangle(Shape):
    def __init__(self,width, height):
        self.width= width
        self.height= height

    def area(self):
        return self.width * self.height
    
rect = Reactangle(4,5)
print(rect.area())
