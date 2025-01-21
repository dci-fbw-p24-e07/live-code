""" 
Your task is to write a program which asks
the user three times for a number. 
If number is even print ‘Even number’, 
else print ‘Odd number’.
"""

# Using a for loop
for i in range(3):
    num = int(input("Enter number: "))
    
    if num % 2 == 0:
        print("Even number")
    else: 
        print("Odd number")
        
# Using a while loop
        
count = 0

while count < 3:
    num = int(input("Enter number: "))
    
    if num % 2 == 0:
        print("Even number")
    else: 
        print("Odd number")
        
    count += 1
