"""
Your task is to write a program which asks the user 
for a number and prints if it is even and divisible by 3.
"""

num = int(input("Enter number: "))

if (num % 2 == 0) and (num % 3 == 0):
    print(num, "is even and divisible by 3")
else:
    print(num, "is not even and divisible by 3")
