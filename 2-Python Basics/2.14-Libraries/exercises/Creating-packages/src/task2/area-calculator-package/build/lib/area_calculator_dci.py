from math import pi 


def welcome():
    print('Hello, welcome to area calculator package!')

def square(a):
    return a * a

def rectangle(a, b):
    return a * b

def triangle(a, h):
    return 0.5 * a * h

def rhombus_with_diagonals(e, f):
    return 0.5 * e * f

def parallelogram(a, h):
    return a * h

def trapezoid(a, b, h):
    return 0.5 * (a + b)/2

def circle(r):
    return pi * r**2
