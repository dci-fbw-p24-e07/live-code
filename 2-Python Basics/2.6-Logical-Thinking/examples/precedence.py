a = 7 
b = 2


def is_even(num):
    if num % 2 == 0: 
        return True
    else:
        return False
    
    
while (a < 9 and is_even(b) and b < 10):
    a += 1
    b += 1

print(a, b)

while (a < 9 and b < 10 or not is_even(b)):
    a += 1
    b += 1

print(a, b)
# 1st loop: True
# 2nd loop: True
# 3rd loop: False
    
