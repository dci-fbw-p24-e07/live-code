import math

from check import print_rectangle_properties

class Rectangle:
    
    def __init__(self, width: float, height: float):
        self.width = float(width)
        self.height = float(height)
        
    def get_area(self) -> float:
        return self.width * self.height
    
    def get_perimeter(self) -> float:
        return (2 * self.width) + (2 * self.height)
    
    def get_diagonal(self) -> float:
        width_sq = math.pow(self.width, 2)
        height_sq = math.pow(self.height, 2)
        return math.sqrt(width_sq + height_sq)
    
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
        

def main():
    rectangle1 = Rectangle(10.4, 15)
    print_rectangle_properties(rectangle1)
    
    rectangle2 = Rectangle(18, 45.6)
    print_rectangle_properties(rectangle2)
    
    rectangle3 = Rectangle(14.9, 36.2)
    print_rectangle_properties(rectangle3)
    

if __name__ == "__main__":
    main()
