# Coding Standards 

- PEP8 and PEP257
- Naming conventions
- Code layout
- Indentation
- Comments
- Tips and tricks to adhere to PEP8
- Linters and autoformatters

## PEP - Python Enhancement Proposal

- These documents primarily describe new features for the Python Language, but some PEPs also focus on design and style and aim to serve as a resource for the community.
- PEP 8 is one of the style guides.
- The main aim of PEP8 is to improve the readability of Python code.

## Naming conventions

- Choosing sensible names will save you time and energy later.
- A good name allows you (or other developers) to understand what your code does just from reading the name of the function, variable, class, module, etc. 

**Naming Styles:**

| Type | Naming Convention | Example |
|------|-------------------|---------|
| Function | Use lowercase word or words. Separate words using underscores to improve readability. This is called snake case. | `function`, `example_function` |
| Variable | Use a lowercase letter, word or words. separate words with underscores. Variables use snake  case | `x`, `name`, `date_of_birth` |
| Class | Start each  word with a capital letter. Don't separate words with underscores. This is called camel case of Pascal case. | `Model`, `Animals`, `MyPythonClass` | 
| Method | Use lowercase word or words. Separate words using underscores to improve readability. This is called snake case. | `my_method`, `speak`, `calculate_interest` |
| Constant | Use an uppercase letter, word or words. Separate words with underscores. | `X`, `MINIMUM_AGE`, `DEFAULT_COLOUR`, `CURRENCY` |
| Module | Use lowercase word or words. Separate words using underscores to improve readability. This is called snake case. | `module.py`, `calculator.py`, `weather_api.py` |
| Package | Use short, lowercase word or words. Don't separate words with underscores | `package`, `interestcalculator`, `pythonpackage` |

## Code Layout

**Blank Lines:**

- Surround top-level functions and classes with 2 blank lines

    ```python
    class FirstClass:
        pass


    class SecondClass:
        pass


    def top_level_function():
        pass
    ```

- Use blank lines sparingly inside functions to show/separate clear steps

    ```python
    def calculate_variance(numbers):
    sum_numbers = 0
    for number in numbers:
        sum_numbers = sum_numbers + number
    mean = sum_numbers / len(numbers)
    
    sum_squares = 0
    for number in numbers:
        sum_squares = sum_squares + number**2
    mean_squares = sum_squares / len(numbers)
    
    return mean_squares - mean**2
    ```

**Maximum Line Length and Line Breaking:**

- PEP 8 suggests that lines should be limited to 79 characters. 
- Lines of codes encased by parentheses can be broken into the next line as long as the new line starts at the point of the opening parentheses.
- If you need to break a line around binary operators, like + and *, then you should do so before the operator.

## Indentation

- PEP8 prefers spaces over tabs
- Use four consecutive spaces to indicate indentation

**Indenting after Line Breaks:**

1. Aligning with opening delimiter:
    
    ```python
    def function(arg_one: int, arg_two: list, arg_three: dict,
                 arg_four: set, arg_five: tuple):
        pass      
    ```

2. Hanging indentation:

    ```python
    def function(
            arg_one: int, arg_two: list, arg_three: dict,
            arg_four: set, arg_five: tuple):
        pass    
    ```

## Comments

- Limit the length of comments and docstring lines to 72 characters.
- Use complete sentences, starting with a capital letter.
- Make sure you update comments if you change your code.

1. Block comments
    - Indent block comments to the same level as the code they describe
    - Start each line with a `#` followed by a single space
    - Separate paragraphs by a line containing a single `#`

        ```python
        for number in range(0, 10):
            # Loop over `number` ten times and print out the value of `number`
            # followed by a newline character.
            print(number, "\n")
        ```

2. Inline comments
    - Use inline comments sparingly
    - Write inline comments on the same line as the statement they refer to.
    - Separate inline comments from the statement by two or more spaces.
    - Start inline comments with a `#` and a single space, like block comments
    - Don't use them to explain the obvious

        ```python
        RENTAL_DAYS = 3  # The default number of rental days
        ``` 

3. Docstrings

    - Documentation strings or docstrings are enclosed in triple double quotation marks (`"""`) or triple single quotation marks (`'''`)
    - They appear on the first line of a function, class, method or module.
    - You use docstring to document and explain a specific block of code.
    - They are an important part of Python, and you can access the docstring of an object using the `__doc__` attribute or the `help()` function

## Linters

- Linter are programs that analyze code and flag errors. 
- They also provide suggestions on how to fix each error. 
- These are particularly useful when installed as extensions on your code editor.

- There 3 commonly used linters in Python:

1. `pycodestyle`
2. `flake8`
3. `ruff`

**Installation:**

```shell
python3 -m pip install flake8
```

**Usage:**

```shell
flake8 <name-of-file>
```

## Autoformatters

- Are programs that refactor your code to conform with PEP8 automatically

**Installation:**

```shell
python3 -m pip install black
```

**Usage:**

```shell
black <name-of-file>
```
