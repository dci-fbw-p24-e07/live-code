"""
Your task is to write a Python program to find whether 
a given number (prompted from the user) is even or odd. 
Print out an appropriate message to the user.
"""

number = int(input("Number to check: "))
mod = number % 2

if mod > 0:
    print(number, "is an odd number!")
else:
    print(number, "is an even number!")
