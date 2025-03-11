#!/usr/bin/env python3
"""
Calculator functions
"""
import pdb


def calculate(func, x, y):
    return func(x, y)


def add(x, y):
    """Returns the sum of x and y"""
    return x + y 


def subtract(x, y):
    """Returns the difference of x and y"""
    return x - y

pdb.set_trace()
calculate(add, 10, 7)
calculate(subtract, 17, 55)
