"""
Your task is to write a Python program which accepts 
(prompts) the float radius of a circle from the user 
and compute its area.
Round the result to two decimals!
Print out an appropriate message to the user.
"""
from math import pi

radius = float(input("Input the radius of the circle : "))
area = round(pi * radius**2, 2)  # rounding to two decimals
print("The area of the circle with radius ", radius, " is: ", area)
