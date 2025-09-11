# Create an abstract class Shape that defines:
 
# An abstract method area() (no implementation).
# Create two child classes that inherit from Shape:
# Rectangle → has attributes length, breadth, and implements area().
# Circle → has attribute radius, and implements area().
# Task:
# Define the abstract class Shape using the abc module.
# Implement Rectangle and Circle classes by providing their own version of area().
# Create one object of Rectangle and one of Circle, then display their areas.
 
from abc import ABC, abstractmethod
 
# Abstract class
class Shape(ABC):
 
    @abstractmethod           # Abstract method
    def area(self):
        pass 
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,breadth):
        super().__init__()
        self.length = length
        self.breadth = breadth
    def area(self):
        super().area()
        return self.length*self.breadth
class Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.radius = radius
    def area(self):
        super().area()
        return 3.14*self.radius*self.radius
r = Rectangle(3,4)
print(f"Rectangle area: {r.area()}")
c = Circle(5)
print(f"Circle area: {c.area()}")
