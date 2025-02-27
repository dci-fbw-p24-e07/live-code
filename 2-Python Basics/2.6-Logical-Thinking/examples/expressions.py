a = True
b = True
c = False 

if a and b:
    print("Both conditions are met")
    
if b or c:
    print("One of the conditions was met")

logged_in = False  # user has not logged in

# if user is not logged in redirect to login page
if not logged_in:
    print("Maybe you should log in first")

x = 3
y = 7

while x < 5 and y < 10:
    x += 1
    y += 1
    
print(x)

# 1st loop: x=3 and y=7
# 2nd loop: x=4 and y=8
# 3rd loop: x=5 and y=9

# prints 5