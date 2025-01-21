"""
Your task is to write a program which asks the 
user five times for a number and prints the 
maximum of those numbers.
"""

maximum = None

for i in range(5):
    num = int(input("Enter number: "))

    if maximum == None:
        maximum = num
    elif num > maximum:
        maximum = num

print(f"Maximum of the numbers: {maximum}")
