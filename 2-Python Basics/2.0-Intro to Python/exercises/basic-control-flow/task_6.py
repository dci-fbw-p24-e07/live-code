"""
Your task is to write a program which asks
the user for a number and prints if a number 
is positive, odd and divisible by 7
"""

num = int(input("Enter number: "))

if (num > 0) and (num % 2 != 0) and (num % 7 == 0):
    print(num, "is positive, odd and divisible by 7")
else:
    print(num, "is not positive, odd and divisible by 7.")
    