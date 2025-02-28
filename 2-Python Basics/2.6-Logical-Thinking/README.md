# Logical Thinking

- What is Logical Thinking?
- Terms commonly used in Logic
- Defining the basic logical operators
- Defining logical expressions
- Predicates
- Evaluation precedence/Order of evaluation

## What is Logical Thinking?

- The ability to break down a problem into smaller parts and then design a step by step solution (algorithm) by applying reasoning and logical steps to achieve the correct outcome.
- The framework for problem-solving, algorithm design and **decision-making** in programming.
- The main tool/concept used in logical thinking is the `if` statement because of its boolean evaluation properties.

### Commonly used terms in logical thinking

| Term | Definition |
|------|------------|
| Boolean | A data type that has two possibilities: `True`/`False` |
| Predicate | An expression that returns a Boolean |
| Logical operator | A symbol that performs a logical operation between the predicates on either side of it (binary operators) or to its right (unary operators). |
| Logical expression | A set of predicates and operators that produce a single Boolean |
| Evaluation | The result of executing an expression or predicate |

### Defining Logical Operators

- There are 3 main Logical operators in programming:

1. `AND` - Evaluates to `True` **if and only if both predicates are True**.
2. `OR` - Evaluates to `True` **if at least one of the predicates is True**.
3. `NOT` - Evaluates to the **opposite of the predicate.**

### Examples of Logical Expressions

```python
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
```

### Predicates

- Anything that evaluates to `True` or `False` can be a predicate.
- Predicates can either be known as Truthy or Falsy
- Many operators and predicates can be added to the same logical expression.

```python 
a = True
b = 2


def is_even(num):
    if num % 2 == 0: 
        return True
    else:
        return False


while a and b < 10 and is_even(b):
    b += 1
    
# 1st loop: True, True, True
# 2nd loop: True, True, False
    
print(b)
```

- A predicate can also be another logical expression

```python
a = True
b = 2


def is_even(num):
    if num % 2 == 0: 
        return True
    else:
        return False


while a and (b < 10 or is_even(b)):
    b += 1
    print(b)
    
print(b)
```

- Non Boolean values can be used as predicates
- Empty variables are determined as Falsy and evaluate to False

```python
c = 0
d = ""
e = []
f = {}
g = None

if c or d or e or f or g:
    print("One of them is not empty")
else:
    print("All are empty")
```

- Non-empty values are considered Truthy and therefore evaluate to True

```python
c = 1  # True
d = "Hello"  # True
e = ["Cars"]  # True
f = {}  # False
g = None  # False

if c or d or e or f or g:
    print("One of them is not empty")
else:
    print("All are empty")
```

- Non-boolean values can always be forced into boolean using the built-in `bool()` function.



### Evaluation precedence / Order of Evaluation

1. Short-Circuit Evaluation: the execution or evaluation of the next part of an expression is skipped because the previous part meets the required conditions.

```python
a = 7 
b = 2


def is_even(num):
    if num % 2 == 0: 
        return True
    else:
        return False
    
    
while (a < 9 and is_even(b) and b < 10):
    a += 1
    b += 1

print(a, b)
# 1st loop: True, True, True
# 2nd loop: True, False
```

- Operators have different priorities on the evaluation of an expression.

1. `NOT`
2. `AND` 
3. `OR`

## 28.02.25 - Truth tables, Advanced Operators and Complex Expressions

- What is truth table?
- How to create a truth table:
    1. AND
    2. OR
    3. NOT
- Advanced Operators:
    1. XOR
    2. NAND
    3. NOR
    4. XNOR
- Evaluating complex expressions
- Grouping predicates 

### What is a truth table?

- A table that lists all the possible combinations of inputs and their corresponding outputs.
- It shows how the out put of the logic changes with different combinations of inputs.
- A systematic representation of all values in a logical expressions.
- Truth tables help us to evaluate if a logical does what we think it does.

### Building a Truth Table

- The truth table values are built according the operator(s) being used in the logical expression

1. `AND`

    - Take the following Python code for example

    ```python
    a = 1
    b = 2

    while a < 7 and b < 14:
        b += 1
        a += 1

    print(b)
    ```

    - The Truth Table would look something like:

    | a < 7 | b < 14 | _Evaluation_ |
    |-------|--------|------------|
    | True | True | True |
    | True | False | False |
    | False | True* | False (short-curcuit)|
    | False | False* | False (short-curcuit)|

2. `OR`

    - Take the following Python code for example

    ```python
    a = 1
    b = 2

    while a < 7 or b < 14:
        b += 1
        a += 1

    print(b)
    ```

    - The truth table could look like this

    | a < 7 | b < 14 | _Evaluation_ |
    |-------|--------|--------------|
    | True | True* | True (short-curcuit)|
    | True | False* | True (short-curcuit)|
    | False | True | True |
    | False | False | False |

3. `AND OR`

- Consider the following Python code:

    ```python
    a = True
    b = 2


    def is_even(num):
        if num % 2 == 0: 
            return True
        else:
            return False


    while (a and b < 10) or is_even(b):
        b += 1
        print(b)
        
    print(b)
    ```

    - The truth table might look something like this:

    | a | b < 10 | is_even(b) | _Evaluation_ |
    |---|--------|------------|--------------|
    | True | True | True* | True |
    | True | True | False* | True |
    | True | False | True | True |
    | True | False | False | False |
    | False | True | True | True |
    | False | True | False | False |
    | False | False | True | True |
    | False | False | False | False |

### Advanced Operators

- there are advanced operators that are not natively built-in to Python.
- These however can still be implemented using the basic operators in Python

1. `XOR` - Exclusive OR

    - It returns True when **exactly 1 of its inputs is True**
    - With multiple inputs XOR is True if the number of True inputs is odd.
    - If both inputs are False or both are True, the output is False.
    - We use the `!=` (not equal to) operator to implement this in Python.

    **Example Code:**
    ```python
    a = "Hello"
    b = "World"

    if a != b:
        print(a)

    ```

    **TRUTH TABLE:**

    | a | b | Evaluation |
    |---|---|------------|
    | True | True | False |
    | True | False | True |
    | False | True | True |
    | False | False | False |

2. `NAND` - Not AND

    - Combines the `not` and `and` operators
    - Process the And evaluation and the inverts it
    - The output is True if at least on of the inputs is False
    - The output is False if both/all inputs are True

    **Example Code:**
    ```python
    a = 2
    b = True

    if not (a and b):
        print("Using the NAND gate")
    ```

    **Truth Table:**

    | a | b | _Evaluation_ |
    |---|---|--------------|
    | True | True | False |
    |True | False | True |
    | False | True | True |
    | False | False | True |

3. `NOR` - Not OR

    - Outputs True only when both outputs are False
    - It is a combination of `not` and `or`
    - If at least one input is True, the output will be False
    - Essentially an OR with an inverted output.

    **Example Code:**
    ```python
    a = 5
    b = 6

    if not (a or b):
        print("Using the NOR gate")
    ```

    **Truth Table:**

    | a | b | _Evaluation_ |
    |---|---|--------------|
    | True | True | False |
    | True | False | False |
    | False | True | False |
    | False | False | True |

4. `XNOR` - Exclusive Not OR

    - Only produces a True when all inputs are False or all inputs are True
    - We use the `==` (equal to) operator to implement it in Python

    **Example Code:**

    ```python
    a = "TGIF"
    b = "Enjoy the weekend"

    if a == b:
        print("XNOR is a glorified equality comparison")
    ```

    **Truth Table:**

    | a | b | _Evaluation_ |
    |---|---|--------------|
    | True | True | True |
    | True | False | False |
    | False | True | False |
    | False | False | True |

### Handling Complex Expressions

1. Naming predicates

    - Ensure you use names that describe the predicate accurately

    **Example Code:**

    ```python
    """
    Program to check if a user is logged in, their age is an even number and has a middle name
    """

    logged_in = True
    middle_name = ""
    user_age = 35

    def is_age_even(age):
        if age % 2 == 0:
            return True
        else:
            return False
        
    if logged_in and is_age_even(user_age) and middle_name:
        print("Welcome to our gambling site")
    ```

2. Group predicates

    - Grouping helps to make a complex expression smaller
    - We can group various expressions/predicates inside a function

    ```python
    """
    Program that keeps generates a lucky number as long as the 
    counter is below 10 or is an even number and the lucky number is below 0.9
    """
    import random

    lucky = random.random() # generates a random number between 0 and 1
    counter = 0

    def is_even(num):
        if num % 2 == 0:
            return True
        else:
            return False

    while (counter < 10 or is_even(counter)) and lucky < 0.9:
        print(lucky)


    def lucky_num():
        return random.random() < 0.9

    def limit_not_reached(counter):
        return counter < 10 or is_even(counter)

    while limit_not_reached(counter) and lucky_num():
        print(counter)
    ```
