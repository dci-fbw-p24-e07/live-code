# Functions

## 12.02.25 - Basics

- What is a function?
- Creating a function
- Calling a function
- Function parameters
- Adding arguments to functions
- The return statement
- Type annotation 
- Parameters with default values 
- Arbitrary arguments

### What is a function?

- A block of reusable code that performs a specific task, usually taking input values (called parameters) and producing an output (called a return value).

1. Reusability
    - The main benefit is that it allows to use the same piece of code in multiple different areas in your program. Improving readability and organization.
2. Parameters
    - Functions can accept input values which can be used withn the function to perform tasks/actions.
3. Return value
    - A function usually returns a single output value after completing its task. This value can be used in other parts of the program.
4. Function call
    - To use a function you must call it by writing its name followed by parentheses, making sure to include any arguments inside the parentheses.

### Creating a function

**Syntax:**

```python
# Function without parameters
def <function-name>():
    # Code to be executed

# Function with parameters
def <function-name>(par_1, par_2, par_3....):
    # Code to be executed
```

**Example:**

```python
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
```

### The `return` statement

- Any function can have a return value
- This is basically the final output of the function
- We use the `return` statement to produce that output

    **Syntax:**

    ```python
    def <function-name>(<parameters>):
        # Code to be executed
        # .... 
        return <final-output>
    ```

    **Examples:**
    ```python
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
    ```

### Type annotations/hinting

- Type annotations/hints are used to indicate the data types of variables and inputs/outputs of functions and methods.

**Syntax:**
```python
def <function-name>(par_1: <data-type>, par_2: <data-type>) -> <output-data-type>:
    # code to be run
    return <output-value>
```

**Examples:**

```python
# Define a type annotated function
def sum(x: int, y: int) -> int:
    result = x + y
    return result


print(sum(6, 8))

# Creates a list of users from a dictionary

def create_user_list(emp_dict: dict) -> list:
    user_list = []
    for emp in emp_dict.values():
        user_list.append(emp)
    return user_list


employees = {
    1: "John",
    2: "Susan",
    3: "Frank",
    4: "Mary"
}

print(create_user_list(employees))
```

- type annotations make the code more readable and understandable. 
- they serve as a quick way to validate the actual data type of the variable or arguments that are being passed to functions.
- Having the wrong type may lead to an error.

> **NOTE:** Type annotations are never going to raise an error if the given variable or argument doesn't have the correct type because these are just **hinters** and aren't enforced types

### Parameters with default values

- In Python we can determine default values for a function parameters.
- We use `=` operator to do so

**Syntax:**
```python
def <function-name>(par_1=<default-value>, par_2=<default-value>):
    # Code to be executed
    return <output-value>
```

**Examples:**
```python
# Function with default values
def sum(x=3, y=4):
    result = x + y
    return result

# function call with 2 arguments
print(sum(16, 8))

# function call with 1 argument
print(sum(16))

# function call with no arguments
print(sum())

# function with different data types from default values
print(sum("28", "14"))

# Function to generate user password

def generate_password(username: str = "John") -> str:
    password = str(username + "1234" + "secure")
    return password

print(generate_password("Elen"))
```

## 13.02.25 - Advanced Functions & Scope

- Arbitrary Arguments:
    1. Positional `*args`
    2. Keyworded `**kwargs`
- Utilizing `*args` and `**kwargs` in the same function
- Variable Scope
- `global` keyword
- Functions as a variable

### Arbitrary Arguments

1. **Positional:**

    - Defined by putting the arguments in the correct order in which they are defined in the function.
    - Python allows us to utilize unlimited arguments in cases where the exact number of arguments may not be known.
    - We use the `*args` variable to define these.

    **Syntax:**
    ```python
    def <function-name>(*args):
        # Code to be executed
        return <output-value>
    ```

    **Examples:**
    ```python
    # define a function to add all numbers given in the parameters
    def adder(*args) -> int:
        result = 0
        # Loop over args tuple
        for num in args:
            result += num
        return result

    print(adder(5, 6, 7, 76, 4, 34, 56))

    # Create a function called multipler that takes an 
    # unknown number of arguments and multiplies all of them
    def multiplier(*args) -> int:
        result = 1
        for num in args:
            result *= num
        return result

    print(multiplier(2, 4, 5, 76, 89, 34))

    # Passing an iterable as an argument
    def create_user(*args):
    for i in args:  # Looping over the tuple
        for j in i:  # Looping over the dictionary
            print(j)
        
    create_user({
        "Name": "John",
        "dob": "6 July 1976",
        "Phone": "+345566776544"
    })
    ```

    - `*args` allows us to pass a variable number of nonkeyworded(positional) arguments
    - These arguments will be stored as a tuple and can be evaluated in the function as a tuple.
    - When utilizing the variable inside the function it is called without the `*` asterisk.

2. **Keyworded:**

    - Defined by assigning a value directly to the parameter name when calling the function.
    - Python allows us to utilize unlimited arguments in cases where the exact number of arguments may not be known.
    - We use the `**kwargs` variable to define these.

    **Examples:**
    ```python
    # Define a function to capture user information
    def user_details(**kwargs):
        for key, value in kwargs.items():
            print(f"{key} is {value}")

    user_details(first_name="Susan", l_name="Franklin")
    user_details(first_name="John", l_name="Jones", age=36, country="New Guinea")
    ```

#### Utilizing `*args` and `**kwargs` in the same function

```python

# Function capture employee info
def get_emp_details(*args, **kwargs):
    details = {}
    for key, value in kwargs.items():
        details[key] = value
        
    details["projects"] = []
    for i in args:
        details["projects"].append(i)

    return details

print(get_emp_details("Oculus", "Elephant", "Meyer", first_name="Louis", last_name="Baker", age=45, email="lbaker@mail.com"))
```

- The `*args` should come first before the `**kwargs`
- Positional arguments cannot be placed after a keyworded argument has already been stated

### Variable Scope

- Variable scope defines a region where we can access a variable
- In  Python we define variables with 3 different scopes:
    1. Local
    2. Global
    3. Nonlocal

1. Local Variables
    - When we declare a variable inside a function, these variables will have a local scope(within the function). We cannot access them outside the function.

    ```python
    def greet():
    
        # local variable
        message = "Hello"
        print("Local:", message)
        
    greet()

    # Try to access outside of the function
    print(message)  # Produces a NameError
    ```

2. Global Variables

    - If we define a variable outside of function or in global scope it is known as a global variable.
    - This means the variable cane be accessed inside or outside the function.

    ```python
    # Declare a global variable
    message = "Hello"

    def greet():
        # access the variable
        print("Local:", message)
        
    greet()
    print("Global:", message)
    ```

3. Nonlocal variables
    - In Python we use the `nonlocal` keyword inside a nested function to indicate that a variable is not local to the inner function, but rather belongs to an enclosing functions scope
    - This allows you to modify a variable from the outer function within the nested function, while still keeping it distinct from global variables

    ```python
    # outside function 
    def outer():
        message = "local"
        
        # nested function
        def inner():
            
            # declare the nonlocal variable 
            nonlocal message
            
            message = "nonlocal"
            print("inner func:", message)
        
        inner()
        print("outer func:", message)
        
    outer()
    ```

## 18.02.25 - Decorators

- What is a decorator?
- Nested Functions
- Passing functions as an argument
- Usage of a decorator
- Creating a decorator
- Use cases for decorators

### What is a decorator?

-  a decorator is a design pattern that allows a user to add new functionality to an existing object. 
- Decorators are typically applied to functions, and they enhance/modify the behaviour of functions.
- Functions in Python support operations such as being passed as an argument, returned from a function, modified and being assigned to a variable.

