"""
Your task is to write a program which prints 
all the divisors of a number. 
The number comes from the user's input.
"""

num = int(input("Enter number: "))

for i in range(2, num + 1):
    if num % i == 0:
        print(i)
