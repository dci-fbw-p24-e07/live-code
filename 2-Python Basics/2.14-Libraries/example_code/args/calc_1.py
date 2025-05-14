""" 
Script to calculate the numbers provided by the user from the 
command line.
Usage: `python3 calc_1.py <operation> <num1> <num2>`
"""
import sys

arguments = sys.argv  # List of arguments


num1 = int(arguments[2])
num2 = int(arguments[3])

# Check for the operation
if arguments[1] == "-multiply" or arguments[1] == "-m":
    print(num1 * num2)
elif arguments[1] == "-add":
    print(num1 + num2)
elif arguments[1] == "-subtract":
    print(num1 - num2)
elif arguments[1] == "-divide":
    print(num1 / num2)
    