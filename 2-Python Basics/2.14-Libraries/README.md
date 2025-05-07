# Libraries

## 07.05.25 - Scripting, modules and packages

- What is a script?
- How to build a Python script
- Python driver code
- What is a module?
- Using the `import` statement
- What is a package?
- Package structure

### What is a script?

- Scripting refers to writing small programs to automate tasks, manipulate data or control other programs.
- A script is a file containing a sequence of instructions that will be executed to complete a specific task.
- Scripts usually have 3 benefits: automation, simplicity and flexibility.

### Building a Python Script

- A Python script consists of 4 main sections:

1. Shebang line:

    - You can add a shebang at the top of your script on Unix-based systems like macOS or Linux.
    - The shebang tells the system which interpreter to use when running a script.
    - There are at least 2 different ways to define the interpreter path

        1. Provide the absolute path to the interpreter:

            ```python
            #!/usr/bin/python3
            ```

            - This approach is less portable because not all Unix systems place the Python Interpreter in the same directory.

        2. Using the operating systems `env` command to point to the interpreter:

            ```python
            #!usr/bin/env python3
            ```

            - This approach is much safer and more portable. It invokes the `env` command to find out where the interpreter lives.

2. Module imports:

    - Python allows us to import pre-written code(called modules) to extend the functionality of our script.
    - These can be Python built-in modules or external libraries you have installed

        1. Importing the full module:

            ```python
            import datetime
            ```

        2. Import specific functions from a module:

            ```python
            from datetime import date
            ```

3. Functions definitions/general logic:

    - In this section we organize our code into functions and write the general logic for our script

        ```python
        def greet(name: str) -> str:
            return f"Hello, {name}"
        ```

4. Driver code/main program block:

    - It's common to include a special `if __name__ == "__main__":` block to run our script when executed directly, not when imported as a module into another script.

        ```python
        if __name__ == "__main__":
            print("This script is running directly")
        ```

    - If the code is always meant to be run as a script then this block is not necessary.

### Modules

- A module is a file that contains code to perform a specific task. It may contain variables, functions, classes, etc.
- Instead of putting everything in a single file, we can use modules to separate code into separate files as per its functionality.
- Making our code organized and easier to maintain.

**Example:**

```python
#!usr/bin/env python3
import math


def circle_area(radius):
    return math.pi * radius**2


def rectangle_area(width, height):
    return width * height
```

### The `import` statement

- We can import definitions inside a module into another module
- To do this we use the `import` keyword in Python

1. Implicit import

    - This does not import the names of the functions defined in a module
    - It only imports the module name

    ```python
    import datetime
    ```

    **Usage:**

    ```python
    curr_date = datetime.datetime.now()
    ```

2. Explicit import

    - We can import specific names from a modules without import the module as a whole
    - To do this we use the `from...import` statement
    - You can import as many names as possible form a module by separating each name using a comma(`,`)

    ```python
    from datetime import date, time
    ```

    **Usage:**

    ```python
    my_date = date(2026, 9, 14)
    ```

3. Import all

    - We can import all names from a module
    - This is done using an asterisk(`*`) to represent all names
    - We use the `from...import` statement
    - This allows us to call the names directly as if they were imported explicitly

    ```python
    from datetime import *
    ```

    **Usage:**

    ```python
    my_time = time(11, 45, 35)
    ```

    - This is not a good programming practice
    - This can lead to duplicate definitions for an identifier. 
    - It also hampers the readability of our code

4. Import with rename

    - We can also import a module and give it an alias or rename it
    - We use the `import...as` statement

    ```python
    import datetime as dt
    ```

    **Usage:**

    ```python
    curr_date = dt.datetime.today()
    ```

### Packages

- A package is a container with various functions, variables, names, modules, etc to perform specific tasks.
- We can separate code from a large program by putting into different files but under the same package.
- In order for python to recognize your code as as package you should include a `__init__.py` in the folder.
- The initialization file can be kept empty but generally any code that needs to be initialized for that package can be placed in that file.

**Example of a package structure:**

![Package Structure](example_imgs/packages.png)

#### Importing module from a package

- We can use dot notation to import modules from packages

- to import the start module:

    ```python
    import game.level.start
    ```

    **Usage:**

    ```python
    game.level.start.select_difficulty(10)
    ```

    - import without a prefix

        ```python
        from game.level import start
        ```

        **Usage:**

        ```python
        start.select_difficulty(10)
        ```






