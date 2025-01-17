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

## 16/01/2025 number system, variable size, relational operators

- bits and bytes 
- Measure variable size
- Number system: binary vs. decimal
- similarities and differences between binary and decimal
- relational operators:
    1. boolean logic and logical operators

### Bits and Bytes 

**Bit:**

- a bit is the smallest unit of storage
- Stores just a 0 or 1.
- On the computer its just 0's and 1's
- A bit is too small to be of much use
- Group 8 bits together to make a 1 byte

**Byte:**

- Collection of 8 bits e.g `01011010`
- One byte can store one character e.g 'A', 'x', '$'
- 8 bits they can make 256 different patterns
- one byte can hold a number between 0 and 255 
- All storage is measured in bytes
- Kilobyte(KB)- about 1 thousand bytes
- Megabyte(MB) - about 1 million bytes
- Gigabyte(GB) - about 1 billion bytes
- Terabyte(TB) - about 1 trillion bytes

### Measuring variable size 

- To check a variables memory size we use the `getsizeof()` function from the `sys`
- This function gives the number of bytes of memory space consumed by a variable

    1. Import the `sys` module at the top of the file

        ```python
        import sys
        ```

    2. Use the `getsizeof()` function to measure a variables memory size

        ```python
        a = 1

        sys.getsizeof(a)
        ```

### Number System

- A number system is defined as a system to express numbers.
- It is mathematical notation used to represent numbers of a given set by using digits or other symbols in a predefined/consistent manner.

There are 4 types of common Number Systems:

1. Decimal number system (base-10): 0,1,2,3,4,5,6,7,8,9
2. Binary Number System (base-2): 0,1
3. Octal Number System (base-8): 0,1,2,3,4,5,6,7
4. Hexadecimal Number system (base-16): 0,1,2,3,4,5,6,7,a,b,c,d,e,f,g,h

#### Binary Number system

- Represented using the base-2 numeral system.
- Consists of only 0 and 1
- Each digit in binary is called a bit.

**Binary to Decimal Manual Conversion Example:**

to convert the binary `1010` to decimal we do the following these steps:

1. We assign each digit a weight based on its position from right to left. The rightmost digit has a weight of 2^0, the next digit has a weight of 2^1, then 2^2 and lastly 2^3.

2. Multiply each digit by its corresponding weight, meaning we go from right to left. We have 0 at the extreme right of the binary number so we will multiply 0 by 2^0 after that we have 1 in the binary number so we will multiply 1 by 2^1 and so on

3. Sum up the results: (0 * 2^0) + (1 * 2^1) + (0 * 2^2) + (1 * 2^3)
= 0 + 2 + 0 + 8 = 10

4. Therefore the binary number `1010` is equal to the decimal number 10.

**Python Approach: Decimal to Binary Conversion:**

- The `bin()` function is used to convert decimal numbers to binary.
- The result will be the binary form of a given number

    ```python
    decimal_num = 10
    binary_num = bin(decimal_num)
    print(binary_num)  # Result: 0b1010
    ```

    > `Ob` is a prefix written to indicate that the following number is a binary number. It serves as a visual indicator to differentiate binary numbers from other numerical representations.


**Python Approach: Binary to Decimal Conversion:**

- you can convert a binary to an integer using the `int()` function and specifying base 2.
- Base 2 corresponds to the binary number

    ```python
    binary_num = "1010"
    decimal_num = int(binary_num, 2)
    print(decimal_num)  # Result: 10
    ```

**Similarities and Differences between binary and decimal:**

| Criteria | Decimal Number System | Binary Number System |
|----------|-----------------------|----------------------|
| Definition | The number which has a whole number and the fractional part separated by a decimal point. | A number that expresses a representation in terms 0 and 1. |
| Base | 10 | 2 |
| Digits Used | 0,1,2,3,4,5,6,7,8,9 | 0,1 |
| Usage | Everyday life and general arithmetic. | Computers and digital systems. |
| Number Representation | More compact for the same values due to base 10 | Longer due to base 2 |
| Calculation Method | Standard arithmetic operations | Binary arithmetic operations |


### Relational Operators

- Usually fall under:
    1. Logical operators
    2. Special operators:
        - Identity operators
        - Membership operators

1. Logical operators:

    - Used to check whether an expression is `True` or `False`.
    - They are usd in decision making.

    1. `and` - `Logical AND`

        - Only translates to `True` **if and only if** both operands are `True`

        ```python
        a = True
        b = False

        print(a and b) # Result: False

        c = True
        d = True 
        e = False

        print( c and d and e) # Result: False

        x = 3 > 2 # True
        y = 4 < 7 # True

        print(x and y) # Result: True
        ```

    2. `or` - `Logical OR`

        - Translates to `True` if **at least one** of the operands is True

        ```python
        a = True
        b = False

        print(a or b) # Result: True

        x = "hello" == "hello" # True
        y = "Java" == "Python" # False

        print(x or y) # Result: True

        c = False
        d = False

        print(c or d) # Result: False
        ```

    3. `not` - `Logical NOT`

        - Translates to `True` if the operand is `False` and vice-versa

        ```python
        a = True

        print(not a)  # Result: False
        ```        

2. Special Operators

    - Python offers some special operators like the identity operators and membership operators

    1. Identity operators:

        - In Python, `is` and `is not` are used to check if two values are located at the same memory location.

        1. `is` 

            - Translates to true if operands are identical(refer to the same object)

            ```python
            x = True

            print(x is True) # Result: True
            print(x is False) # Result: False
            ```

        2. `is not`

            - Translates to `True` if the operands are not identical (do not refer to the same object)

            ```python
            y = False

            print(y is not True) # Result: True
            print(y is not False) # Result: False
            ```

    2. Membership operators

        - In Python, `in` and `not in` are the membership operators.
        - They are used to test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary).

        1. `in`

            - Is `True` is a value/variable is found in the sequence

            ```python
            x = "a"

            print(x in "Python") # Result: False
            ```
        
        2. `not in`

            - Is `True` if a variable/value is not found in a sequence.

            ```python
            y = "c"

            print(y not in "JavaScript") # Result: False
            ```

##  17/07/2025 - Control Flow(Conditionals) and Intro to Functions

- if statements
- if else  statements
- Nested if statements
- for loop
- the break and continue statements
- Nested for loops
- while loop
- The pass statement
- Functions:
    - Creating a function
    - Calling a function

### `if` statement

- The `if` is a conditional statement.
- It isi used to execute a block of code only when a specific condition is met.

- For example:

    - Suppose we need to assign different grades to students based on their scores

        1. If a student scores above 90, assign grade A 
        2. If a student scores above 75, assign grade B 
        3. If a student scores above 65, assign grade C

**Syntax**

```python
if <condition>:
    # code to be executed
```

![If Statement](https://www.programiz.com/sites/tutorial2program/files/python-if.png)

- Condition is a statement that evaluates to a boolean result, either `True` or `False`
- If the condition evaluates to `True`, the body of the if statement will be executed.
- If the condition evaluates to `False` , the body of the if statement will be skipped from execution

### Indentation in Python

- Python uses indentation to define a block of code, such as the body of conditional statement, the body of a function, etc.
- We usually use 4 spaces for indentation in Python

### `if...else` statement

- An if statement can have an optional `else` clause.
- The `else` clause executes when the condition of the if statement evaluates to `False`

    **Syntax**

    ```python
    if <condition>:
        # body of if statement
    else: 
        # body of else statement
    ```

![If...Else](https://www.programiz.com/sites/tutorial2program/files/python-if-else.png)

### `if...elif...else` statement


- The `if...else` is used to execute a block of code among 2 alternatives
- The `if...elif...else` is used to execute a block of code wen there is more than 2 alternatives

    **Syntax**

    ```python
    if <condition1>:
        # code block 1

    elif <condition2>:
        # code block 2

    else:
        # code block 3
    ```

![If...elif...else](https://www.programiz.com/sites/tutorial2program/files/python-elif.png)

### Nested `if` statements

- Including an if statement inside another if statement

For example:

- You have a party and you only want guest who are on your guest list. If they are on the guest list they must be wearing. If they are on the guest list and wearing white they must also bring a drink

    ```python
    guest_list = "Peter, John, Lucy, Mary, Max"

    guest_name = input("What is your name?: ")

    # outer if statement
    if guest_name in guest_list:
        print("Welcome!")
        wearing_white = bool(input("Are you wearing white? (enter 'True' or 'False'):"))

        # inner if statement 1
        if wearing_white:
            print("Thank you for sticking to the dress code!")
            has_a_drink = bool(input("Did you bring a drink? (enter 'True' or 'False'):"))

            # inner if statement 2
            if has_a_drink:
                print("Enjoy the party!")

            # inner else statement 2
            else:
                print("Maybe bring a drink next time")

        # inner else statement 1
        else:
            print("Respect the dress code next time")

    # outer else statement
    else:
        print("Sorry! Not on the list.")
    ```

    ![Nested if](https://www.programiz.com/sites/tutorial2program/files/python-nested-if.png)

### Loops

- Repeat a block of code as long as a certain condition is met or has not been broken.

1. `for` loop
2. `while` loop

#### 'for' loop

- This is used to iterate over sequences such as strings, lists, dictionaries, etc.

    **Syntax:**

    ```python 
    for value in sequence:
        # run this code
    ```

    - The `for loop iterates over elements of a sequence in order, and in each iteration, the body of the loop is executed.
    - The loop ends after the body of the loop is executed for the last time.

    ```python
    word = "Python"

    # access each letter one by one
    for letter in word:
        print(letter)
    ```

    **`for` Loop with Python `range()`**

    - `range(start, stop)` returns a sequence of numbers
    - `start` - is the the number the sequence begins with
    - `stop` - is the first number to not be included

        ```python
        # generate numbers from 0 to 3
        values = range(0, 4)
        ```

    - We can use the `range()` function to iterate over a sequence of numbers

        ```python
        # iterate from i = 0 to i = 5
        for i in range(0, 6):
            print(i)
        ```

#### The break and continue statements

1. `break`

    - Terminates a loop immediately before loops through all the items

    ```python
    # Break the loop if the number is equal to 3
    for i in range(0, 6):
        if i == 3:
            break
        print(i)
    ```

    ![Break Statement](https://www.programiz.com/sites/tutorial2program/files/working-break-statement-python.png)

2. `continue`

    - Skips the current iteration of the loop and goes to the next iteration.

    ```python
    # Skip the number 4 and print the rest
    for i in range(6):
        if i == 4:
            continue
        print(i)
    ```

    ![Continue Statement](https://www.programiz.com/sites/tutorial2program/files/working-continue-statement-python.png)

#### Nested `for` loops

- A lop can contain another loop making them nested

```python
# Print all the different combinations of numbers and letter
# They must go in sequence

letters = "abcde"
numbers = "12345"

for letter in letters:
    for number in numbers:
        print(letter, number)

    # This is outside the inner loop
    print("-----")
```

##### Using a `for` loop without accesing sequence items

- If we don't intend to use items of a sequence inside the body of a loop, it's clearer to use the `_` (underscore) as the loop variable.

```python
# iterate from i = 0 to i = 3
for _ in range(4):
    print("hi")
```

#### 'while` loop

- Repeats a block of code until a certain condition is met.

    **Syntax:**

    ```python
    while condition:
        # body of the while loop
    ```

    1. The `while` loop evaluates the condition, which is a boolean expression.
    2. If the condition is `True`, the body of the while loop is executed. The condition is evaluated agin.
    3. The process continues until the condition is `False`
    4. Once the condition evaluates to `False`, the loop terminates.

    > Tip: We should update the variable used in the condition inside the loop so that eventually it evaluates to `False`. Otherwise we would create an infinite loop.

    ```python
    # print the current loop number
    number = 0

    while number <= 5:
        print(number)
        number += 1
    ```

    **Flowchart of a `while` loop:**

    ![Flowchart of while loop](https://www.programiz.com/sites/tutorial2program/files/python-while-loop-flowchart.png)

### The `pass` statement

- The pass statement is a null statement that can be used as a placeholder for future code
- Suppose we have a loop of function that is not implemented yet, but will be added in the future. We can use the pass statement for this

    **Syntax:**

    ```python
    pass
    ```

    **For example:**

    ```python
    n = 7
    if n > 5:
        pass
    ```

### Functions

- A block of code that performs a a specific task
- It allows the reuse of code throughout the program

#### Declaring a function

- to declare a function we use the keyword `def` (define) followed by the name of the function and parentheses and a full colon

```python
def <function-name>():
    # Function body
```

- Create a function called `greet` that prints the string "Hello World"

    ```python
    def greet():
        print("Hello World")
    ```

#### Calling a function

- Declaring a function does not make the function run. Meaning if the code is executed nothing will happen.
- to utilize the function we would need to make a function call

    ```python
    greet()
    ```
