# Declare a global variable
message = "Hello"

def greet():
    # access the variable
    print("Local:", message)
    
greet()
print("Global:", message)
