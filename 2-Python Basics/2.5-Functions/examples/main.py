# Create a function with no parameters
def greet():
    print("Hello world!")

  
greet()


# Create a function with parameters
def greeting(first_name, last_name):
    print("Hello,", first_name, last_name)

greeting("Michael", "Brown")  # Positional args

fname = "Peter"
lname = "Sanders"
greeting(fname, lname)  # Postional arguments

greeting(last_name="Jones", first_name="Susan")  # Keyworded arguments


# Using the return statement

def greets(name):
    text = "Hello, " + name
    return text

new_greet = greets("Ollie")
print(new_greet)

# Function to find the square of a number
def find_square(num):
    result = num**2
    return result

sq_of_4 = find_square(4)
print(sq_of_4)