"""
Your task is to write a Python program to get the 
difference between a two given numbers (prompted by user).
If the first number is greater than second then calculate 
double difference between numbers.
Otherwise calculate the absolute difference between numbers.
Print out an appropriate message to the user.
"""

first = int(input("First number: "))
second = int(input("Second number: "))

if first > second:
    result = 2 * (first - second)
else:
    result = abs(first - second)

print("The result of calculation is ", result)
