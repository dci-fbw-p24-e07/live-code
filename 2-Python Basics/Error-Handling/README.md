# Error and Error handling in Python

- What is an error?
- Python stacktrace and how to interpret it
- Common errors and exceptions classes
- The Basics in the Error handling:
    1. Look Before You Leap - LBYL
    2. Easier to Ask Forgiveness the Permission - EAFP
- `try ....except` block 

## What is an error?

- Is an issue that prevents a program from completing its task or running completely.
- Exceptions are conditions that interrupt the normal flow of the program.
- both errors and exceptions are type of runtime error, meaning they occur during the execution of a program. 
- An error is a critical issue that a normal application should not catch e.g `IndentationError`
- An exception is a condition that a program should catch e.g `IndexError`, `DoesNotExist`

## Stacktrace or Traceback

```python
# Code has an error resulting in a stacktrace

def greeting(name):
    return "Hello, " + nam

greeting("Michael")
```

```shell
Traceback (most recent call last):
  File "/home/mk16/Documents/Source Files/DCI/P24-E07/live-code/2-Python Basics/Error-Handling/examples/stack-trace.py", line 6, in <module>
    greeting("Michael")
  File "/home/mk16/Documents/Source Files/DCI/P24-E07/live-code/2-Python Basics/Error-Handling/examples/stack-trace.py", line 4, in greeting
    return "Hello, " + nam
                       ^^^
NameError: name 'nam' is not defined. Did you mean: 'name'?
```

## Common Errors/Exceptions

| Error/Exception | Cause |
|-----------------|-------|
| `KeyError` | Raised when a key is not found in a dictionary |
| `NameError` | Raised when a variable is not found in local or global scope |
| `SyntaxError` | Raised by the parser when the wrong/erroneous is encountered |
| `TypeError` | Raised when a function or operation is applied to an object of incorrect type |

## The Basics Paths of Error Handling in Python

1. **Look Before You Leap**:

    - An error handling pattern that insists you should check that the conditions for performing an action/task that can fail are proper before triggering the action/task itself.

        ```python
        """
        Program to delete a file
        """
        import os

        file_path = "P24-E07/live-code/2-Python Basics/Error-Handling/dummy.txt"

        # Check if file actually exists
        if os.path.exists(file_path):
            # Delete te file
            os.remove(file_path)
        else:
            # Let the user know that something went wrong
            print(f"Error: file {file_path} does not exist.")
        ```

    - This method can be useful in scenarios where the execution is quite simple.
    - It is quite to write robust logic because you have to know all the possible ways that a function can fail and sometimes there are just too many.
    - Race conditions may make execution difficult as conditions may change in a small window of time between when checks are made and when the action/task is executed.

2. Easier to Ask Forgiveness than Permission:

    - It means you should attempt to perform the action first and the deal with any errors afterwards.

        ```python
        import os

        file_path = "/home/mk16/Documents/Source Files/DCI/P24-E07/live-code/2-Python Basics/Error-Handling/dummy.txt"

        try:
            # attempt file deletion
            os.remove(file_path)
        except OSError as error:
            print(f"Error deleting file: {error}")
        ```

    - While it is possible to catch all errors it is bad practice to do so.
    - Catching and silencing all errors may prevent discovery of any bugs in your code that need to be fixed.
    - Catch the smallest possible list of exception classes and when it makes sense don't catch any exceptions at all.

## `try...except` block

- Used to handle exceptions in Python

    **Syntax:**

    ```python
    try:
        # Code that may cause an exception
        # task/action to be attempted
    except:
        # code to run when an exception occurs
    ```

- For  each `try` block there can 1 or more except blocks.
- Multiple except blocks allows us to handle each exception differently.
- The argument of each except block indicates the kind of error that can be handled by it.

    ```python
    even_numbers = [2, 4, 6, 8, 10, 12, 14]

    try:
        print(even_numbers[9])
    except ZeroDivisionError:
        print("Denominator cannot be 0.")
    except IndexError as error:
        print(f"Error: {error}")
    ```

### `try` with `else` clause

- We might want to run a certain block of code if the code inside the try block runs without any errors

    **Syntax:**
    ```python
    try:
        # code to be attempted
    except:
        # Code to run in case of errors/exceptions
    else:
        # Code to be run if try is successful
    ```

    ```python
    # program to print the reciprocal of even numbers 
    try:
        num = int(input("Enter a number: "))
        assert num % 2 == 0
    except:
        print("Not an even number")
    else:
        reciprocal = 1 / num
        print(reciprocal)

### `try...finally`

![Catch errors](https://images.datacamp.com/image/upload/v1677232088/Exception%20and%20error%20handling%20in%20Python.png)

- the `finally` block is executed no matter whether there is an exception or not.
- The finally block is optional.
- for each try block there can only be on finally block.

    **Syntax:**
    ```python
    try:
        # Code to be attempted 
    except:
        # Code to run in case of error/exception
    finally:
        # Code that runs no matter what
    ```

    ```python
    # Function to divide

    def divide(numerator, denominator):
        try:
            result = numerator / denominator
        except ZeroDivisionError:
            print("Denominator cannot be zero.")
        else:
            print(result)
        finally:
            print("This is the finally block")

        
    x = int(input("Enter numerator: "))
    y = int(input("Enter denominator: "))

    divide(x, y)
    ```
