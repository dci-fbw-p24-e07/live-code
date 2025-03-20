""" 
Encapsulation sample code
"""
from random import randint


class Product:
    
    def __init__(self):
        self.__max_price = 1000
        self._discount = 0.1
    
    def sell(self):
        if self._discount:
            price = self.__max_price - (self.__max_price * self._discount)
            print(f"We are selling for {price}")
            
        else:
            print(f"We are selling for {self.__max_price}")
    
    # Setter methods
    def set_max_price(self, new_price):
        self.__max_price = new_price
        
    def set_discount(self, new_discount):
        self._discount = new_discount
        
        
radio = Product()

radio.sell()

# Using the setter function
radio.set_max_price(2000)
radio.sell()

#### 20.03.25


class Employee:
    
    hybrid = True
    
    def __init__(self, name):
        self.name = name

    # Instance method
    def greet(self):
        print(f"Hi, my name is {self.name} and I am new.")
        
    # Class method
    @classmethod
    def get_hybrid(cls):
        return cls.hybrid
    
    @classmethod
    def set_hybrid(cls):
        cls.hybrid = False
        
    # Static method
    @staticmethod
    def generate_passcode():
        return randint(1000, 9999999)

    
lisa = Employee("Lisa")
lisa.greet()
lisa.set_hybrid()
print(lisa.get_hybrid())

print(lisa.generate_passcode())

## Getters and Setters

class Rectangle:
    
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        
    @property
    def height(self):
        return self.__height
    
    # Creating a setter
    @height.setter
    def height(self, new_height):
        self.__height = new_height
    
    @property
    def width(self):
        return self.__width
    
    @width.getter
    def width(self):
        return f"The width is {self.__width}"
        
rectangle_1 = Rectangle(10, 6)
print(rectangle_1.height)
rectangle_1.height = 8
print(rectangle_1.height)
print(rectangle_1.width)


