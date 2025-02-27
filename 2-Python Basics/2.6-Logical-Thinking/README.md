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