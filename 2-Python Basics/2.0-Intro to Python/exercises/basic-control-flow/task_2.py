"""
Your task is to write a program which asks the user 
three times for a number and prints the sum of those numbers.
"""

# initialize result variable
total = 0
  
for i in range(3):
  
    num = int(input("Enter number: "))
    total += num 
    
print("Sum of the numbers: ", total)
