a = True
b = 2


def is_even(num):
    if num % 2 == 0: 
        return True
    else:
        return False


while a and b < 10 and is_even(b):
    b += 1
    
# 1st loop: True, True, True
# 2nd loop: True, True, False
    
print(b)
    

while a and (b < 10 or is_even(b)):
    b += 1
    
print(b)
    
"""
Using non boolean values
"""

c = 1  # True
d = "Hello"  # True
e = ["Cars"]  # True
f = {}  # False
g = None  # False

if c or d or e or f or g:
    print("One of them is not empty")
else:
    print("All are empty")
    

user = input("Username: ") and "Unknown"
print(user)
