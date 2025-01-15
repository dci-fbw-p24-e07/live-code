# Python Basics

## 15/01/2025 - input(), Console, operators

- Using the Python Console
- `print()` function
- Operators:
    1. Arithmetic operators
    2. Assignment operators
    3. Comparison operators
- `input()` function

### Python Console

- An interface for executing, debugging and getting immediate feedback on Python code.
- Can be run from the terminal
- Sometimes referred to as the Python interpreter
- Can be run from the terminal using the `python` or `python3` command (depends on Operating System)
- Exit the console by using the `exit()` function.

### `print()` function

- outputs a given object onto the standard output(terminal)
- The full syntax for `print()` is:

    ```python
    print(*objects, sep=" ", end='\n', file=sys.stdout, flush=False)
    ```

    1. `*objects` - objects to be printed. `*` specifies that there may be more than one object to be printed.
        ```python
        print("Hello", "World")
        ```

    2. `sep` - objects are separated by `sep`. **Default value: `' '`**

        ```python
        print("Hello", "World", sep="5")
        ```

    3. `end` - printed as the last object. **Default value: `'\n'`**

        ```python
        print("Python rocks", "Java sucks", end=">:3")
        ```

    4. `file` - must be an object with `write(string)` method. If omitted, `sys.stdout` will be used - which prints objects to the screen.

        ```python
        sourceFile = open('python.txt', 'w')
        print('Pretty cool, huh!', file = sourceFile)
        sourceFile.close()
        ```

    5. `flush` -  if `True`, the stream is forcibly flushed. **Default value: `False`**

        ```python
        print("Hello", "Programmers", flush=True)
        ```

### Operators

- operators are symbols that perform operations on variables and values

- There are different types:

    1. Arithmetic Operators
    2. Assignment Operators
    3. Comparison Operators
    4. Logical Operators
    5. Bitwise Operators
    6. Special Operators

#### Arithmetic Operators

- Are used to perform mathematical operations like addition, subtraction, multiplication, etc.
- The result is always going to be the the data type that can accommodate the original types of both values.

| Operator | Operation | Example |
|----------|-----------|---------|
| `+` | Addition | `6 + 4 = 10` |
| `-` | Subtraction | `11 - 3 = 8` |
| `*` | Multiplication | `2 * 3 = 6` |
| `/` | Division | `4 / 2 = 2` |
| `//` | Floor Division (Rounds down to the nearest integer) | `7 / 3 = 2` |
| `%` | Modulo (Remainder) | `5 % 2 = 1` |
| `**` | Power | `4 ** 2 = 16` |

#### Assignment operators

- Assignment operators are used to assign values to variables

    ```python
    x = 5
    ```

    > **NOTE: Assignment operators only work if the variable has already been initialized/created.**

1. Assignment Operator (`=`)

    ```python
    a = 7
    b = "Hello"
    c = True
    ```

2. **Addition Assignment (`+=`)**

    ```python
    a = 5

    # 1
    a = a + 1 # 6

    # 2 - using the addition assignment
    a += 1 # 7
    ```

3. **Subtraction Assignment (`-=`)**

    ```python
    b = 8

    # 1
    b = b - 3 # Result: 5

    # using the subtraction assignment
    a -= 2 # Result: 3
    ```

4. **Multiplication Assignment (`*=`)**

    ```python
    c = 6

    # 1 
    c = c * 5 # Result: 30

    # 2 - using the multiplication operator
    c *= 5 # Result: 150
    ```

5. **Division Assignment (`/=`)**

    ```python
    d = 15

    # 1
    d = d / 3 # Result: 5

    # 2 - using the division assignment
    d /= 5 # Result: 1
    ```

6. **Remainder Assignment (`%=`)**

    ```python
    e = 10 

    # 1
    e = e % 5 # Result: 0

    # 2 using the remainder assignment
    e %= 2 # Result: 0
    ```

7. **Exponent Assignment (`**=`)**

    ```python
    f = 15

    # 1 
    f = f ** 2 # Result: 225

    # 2 using the exponent assignment
    f **= 4 # Result: 2562890625
    ```

#### Comparison Operators

- Comparison operators compare two values/variables and return a boolean result: `True` or `False`

1. **Is Equal To (`==`)**

    ```python
    a = 5
    b = 3

    a == b  # False
    ```

2. **Not Equal To (`!=`)**

    ```python
    a = 5
    b = 3

    a != b # True
    ```

3. **Greater Than (`>`)**

    ```python
    3 > 5 # False
    ```

4. **Lesser Than (`<`)**

    ```python
    10 < 45 # True
    ```

5. **Greater Than or Equal To (`>=`)**

    ```python
    45 >= 50 # False
    ```

6. **Less Than or Equal To (`<=`)**

    ```python
    65 <= 70 # True
    ```

### `input()` function

- Takes input from the user and returns it.
- the syntax is :

    ```python
    input("<prompt>")
    ```

    ```python
    first_name = input("Enter your first name:")

    print(first_name)
    ```