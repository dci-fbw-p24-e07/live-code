""" 
Creating abstract base classes in Python
"""
# Import the abc module
from abc import ABC, abstractmethod


# Create an abstract class
class Shape(ABC):  # inherit ABC class
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    # Concrete method
    def shape_name(self):
        print("I am a shape")
        

class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.142 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.142 * self.radius
    
        
circle_1 = Circle(10.7)
circle_1.shape_name()
print(circle_1.perimeter())

class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    # Missing area and perimeter implementation
    
    
# This will raise an error      
rectangle_1  = Rectangle(10.4, 5.7)
