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
