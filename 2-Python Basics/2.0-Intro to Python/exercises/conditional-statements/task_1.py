""" 
Your task is to write a Python program to calculate the sum of 
three integers given (prompted) by user.
If the values are equal then calculate triple value of their sum.
Print out an appropriate message to the user.
"""

first = int(input("First number: "))
second = int(input("Second number: "))
third = int(input("Third number: "))

result = first + second + third

if first == second and second == third:
    result = 3 * result
    print("The triple sum is: ", result)
else:
    print("The sum is: ", result)
