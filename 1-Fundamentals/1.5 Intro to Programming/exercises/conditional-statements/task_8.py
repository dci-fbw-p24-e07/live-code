""" 
Your task is to write a Python program to get the 
Fibonacci series between 0 to 50.
"""

# declare 2 variables
n1, n2 = 0, 1
maximum = 50

# check if n1 is < 50
while n1 < 50:
    
    # add n1 + n2
    print(n1)

    # update the variables
    n1, n2 = n2, n2 + n1

