# Loops

- Concept of loops
- `for` vs `while` loops
- Usage of `for` loops
- Usage of `while` loops
- Iterables vs Iterators
- Looping over collections
- Using the `else` clause in `for` and `while` loops

## What are loops?

- These are programming mechanisms used to repeat execution of code **while a certain condition is true** or **for a specified number of iterations**
- These are widely used in the decision making process of a program
- They form the base of most algorithms
- These flows are called loops because they loop back around to the top after each iteration.

## `for` vs `while` loops

| `for` | `while`|
|-------|--------|
| Used when you know in advance how many times you want to execute a block of code | Used when you don't know how many times you want to execute a block of code. |
| Iterates over a sequence (a list, tuple, string, dictionary or range) and executes the block of code for each item in the sequence | Runs as long as a specified condition is True. |
| The loop variable takes the value of each item in the sequence during each iteration(loop) | It's important to make sure that the condition eventually becomes false otherwise the loop will indefinitely - infinite loop. |

## Usage of `for` loops

- Used to process each item in a sequence.
- Used with strings, lists, tuples, dictionaries and `range()`
- Each item is re-assigned to the loop variable, and the body of the loop is executed

    ```
    for <LOOP-VARIABLE> in <SEQUENCE>:
        STATEMENTS/BODY
    ```

- The loop variable is created when the `for` statement runs, no need to create it before hand.
- Each iteration assigns the loop variable to the next element in the sequence and then executes the statements in the body.
- The `for` loop terminates when the the body is executed for the last element in the sequence.

    **Examples:**

    ```python
    # Generate an invite for each friend in the list

    for friend in ["Marvin", "Louisa", "Jack", "Sonic"]:
        invitation = "Hi " + friend + ". Please come to my party!"
        print(invitation)

    # Get the employee name for each of the employees

    employees = {
        "Manager": "Jack",
        "Developer": "Ross",
        "DB Engineer": "Mary",
        "Network Admin": "Louisa"
    }

    for emp in employees:
        print(employees[emp])

    for emp in employees.values():
        print(emp)

    # Generate a countdown timer

    for i in range(100):  # Generates variables from 0 to 9
        print("I will always do my homework")
        
    # print out the numbers 1 - 12 with their squares - 7^2
    for x in range(1, 13):
        print(x, x**2)

    ```

## Usage of `while` loops

- a `while` executes for as long as the boolean expression evaluates to True.
- It executes an unknown number of times and therefore must be forcibly terminated.

```
while <BOOLEAN-EXPRESSION>:
    STATEMENTS/BODY
```

- A boolean expression is something that evaluates to either True or False

    **Examples:**

    ```python
    # Guess the meaning of life
    number = 0

    while number != 42:
        number = int(input("What is the meaning of life?: "))
        
    # Guess the name
    name = "Michael"
    guess = input("I'm thinking of a name. Guess what it is: ")
    guesses = 0 

    while (guess != name) and (guesses < len(name) - 1):
        print("Nope, that's not it. Hint: ")
        print(f" Letter {guesses + 1} is {name[guesses]}")
        guess = input("Guess again: ")
        guesses += 1
        
    if (guesses == len(name) - 1) and (name != guess):
        print(f"Too bad, you didn't get it. The name was {name}")
    else:
        print(f"Great, you got it in {guesses + 1} tries!")
    ```
