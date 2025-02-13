def greet():
    
    # local variable
    message = "Hello"
    print("Local:", message)
    
greet()

# Try to access outside of the function
print(message)  # Produces a NameError
