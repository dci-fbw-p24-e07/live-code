#!usr/bin/env python3
import math


def circle_area(radius):
    return math.pi * radius**2


def rectangle_area(width, height):
    return width * height


def main():
    shape = int(input("Enter 1 for circle, 2 for rectangle: "))

    if shape == 1:
        radius = int(input("Enter the radius: "))
        result = circle_area(radius)
        print(f"The area of the circle is: {result}")
    
    elif shape == 2:
        width = int(input("Enter the width: "))
        height = int(input("Enter the height: "))
        result = rectangle_area(width, height)
        print(f"The area of this rectangle is: {result}") 


if __name__ == "__main__":
    main() 
