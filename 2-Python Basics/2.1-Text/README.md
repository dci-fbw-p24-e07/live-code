# Text

## 21.01.25 Basics and String methods

- What a string is?
- How to declare a string
- Characters vs strings
- Basic string methods

### What is a string?

- Is a sequence of characters(letters, numbers and symbols).
- "hello1223%&" is a string
- A string is always encased in quotes.

- A character is a single element in the string sequence
- "h" - is a character.

### How to declare a string

- We use double or single quotes to represent a string in Python.

    ```python
    # Declare using double quotes
    string_1 = "Python Rocks!"

    # Declare using single quotes
    string_2 = 'Python Rocks!'

    # Declare using the str() method
    string_3 = str()  #  Declares an empty string
    ```

    **Declaring a Multiline string:**

    1. we can also use triple double quotes `"""` or triple single quotes `'''` to declare string

    ```python
    message = """
    This is a multiline string. 
    Its a fun way to keep text.
    """

    message_2 = '''
    This one uses single quotes.
    But its all text nonetheless
    '''+
    ```

### Accessing strings in Python

- We can access characters in a string using three ways:

    1. **Indexing**
        - Accessing a character using its position in the string sequence
        - Each character has a numeric position in the sequence
        - Index positions start from `0` 

        ```python
        message = "Hello World"

        # access the 3rd element
        message[2] # Result: "l"

        # access the 6th element 
        message[5] # Result: " "
        ```

    2. **Negative Indexing**

        - Access characters from right to left
        - Declared by putting a `-` before the index number for example `[-2]`
        - Starts counting from `-1`

        ```python
        message = "We love Python!"

        # access the last element 
        message[-1] # Result: "!"

        # access the 3rd from last character
        message[-3] # Result: "o"
        ```

    3. **Slicing**
        - Access a range of characters in a string by using the slicing operator `:`
        - Syntax: `[start:stop]`
        - `start` being the first index to be included
        - `stop` being the first index to not be included

        ```python
        message = "Python is the best"

        # access the 4th index to the 7th index
        message[4:8]
        ```

        > **NOTE:** If you try to access an index that is out of range or use numbers other than integers, there will be an `IndexError`.


### String Operations

1. Compare 2 strings:

    - We use the `==` operator to compare strings. 
    - If two strings are equal the operator returns `True`. Otherwise it returns `False`.

        ```python
        string_1 = "Hello, world"
        string_2 = "Java sucks"
        string_3 = "Hello, world"

        # Compare string_1 and string_2
        string_1 == string_2 # Result: False

        # compare string_1 and string_3
        string_1 == string_3  # Result: True
        ```

2. Join 2 or more strings 

    - We can use the `+` operator to concatenate 2 or more strings

        ```python
        greeting = "Hello, "
        name = "Johnny"

        # join the 2 strings 
        result = greeting + name # Result: "Hello, Johnny"
        ```

3. Iterate through a string

    - We can use a `for` loop to iterate through a string

        ```python
        message = "We love Python"

        for letter in message:
            print(letter)
        ```

4. Membership Test

    - We can check if substrings exist in string or not using the `in` or `not in` operators.

        ```python
        message = "We love Python!"

        print("a" in message) # Result: False
        print("x" not in message) # Result: True
        ```

### String Interpolation

- The process of substituting values of variables into the placeholders of a string.

1. **f-Strings**

    - We prefix a string with the letter `f` before the opening quote to format the text.
    - Syntax: `f'Hello, {name}'`
    - The placeholder is inside the `{}` curly braces.

        ```python
        name = "Maxwell"
        program = "Python"

        result = f"Hello, {name}! This is {program}"
        print(result)  # Result: 'Hello, Maxwell! This is Python'
        ```

        ```python
        a = 12
        b = 15

        print(f'12  multiplied by 15 is {a * b}') # Result: 12  multiplied by 15 is 180
        ```

2. `str.format()`

    - We use the `format()` function on string object and braces `{}`. 
    - The string object in the `format()` function is substituted in place of the braces
    - Is used for positional formatting.

    - Syntax: `"Hello, {}".format("Johnny")`

        ```python
        name = "Johnny"

        result = "Hello, {}".format(name)

        print(result) # Result: "Hello, Johnny"
        ```

        ```python
        name = "Johnny"
        program = "Python"
        message = "Hello, {}! This is {}."

        result = message.format(name, program)
        ```

### String Methods

1. `len()`

    - returns the number of unicode characters inside a string sequence
    - Input the string value or variable as an argument to the `len()` function 

        ```python
        message = "Hello, world!"

        print(len(message)) # Output: 13
        ```

        ```python
        message = "Hello, World!"
        msg_len = len(message)

        for i in range(0, msg_len):
            print(message[i])
        ```

2. `upper()`

    - Ir converts all lowercase characters in a string to uppercase and returns the resultant string.
    - The `upper()` method does not take in any arguments
    - It is attached to a string 

        ```python
        message = "Python is fun"

        print(message.upper())  # Output: "PYTHON IS FUN"
        ```

        ```python
        string_1 = "Programming IS aWeSoMe!"
        string_2 = "PROGRAMMING is awesome!"

        if (string_1.upper() == string_2.upper()):
            print("The strings are the same")
        else: 
            print("The strings are different")
        ```

3. `lower()`

    - It converts all uppercase characters in a string to lowercase and returns the resulting value.
    - Is attached to the end of a string
    - Does not take in any arguments

        ```python
        message = "Python is the best"

        print(message.lower()) # Output: "python is the best"
        ```

        ```python
        string_1 = "Programming IS aWeSoMe!"
        string_2 = "PROGRAMMING is awesome!"

        if (string_1.lower() == string_2.lower()):
            print("The strings are the same")
        else: 
            print("The strings are different")
        ```

    > You can use the `swapcase()` method to swap between lowercase and uppercase.

4. `find()`

    - Returns the **index** of the first occurrence of a substring(if found). 
    - If not found it returns `-1`.
    - Syntax: `string.find(substring)`

        ```python
        message = "Python is the best programming language out there"

        message.find("best")  # Output: 14
        ```

5. `replace()`

    - Replaces each matching occurrence of a substring with another string.
    - Returns the resulting value
    - syntax: `string.replace(<existing_substring>, <replacement_string>, optional:<num_of_occurrences)` 
    - The substring is case case sensitive

        ```python
        text = "bat ball ban band bath bait bar"

        #  replace "ba" with "ro"
        replaced_text = text.replace("ba", "ro")

        print(replaced_text) # Output: 'rot roll ron rond roth roit ror'
        ```

        ```python
        text = "Lorem ipsum. lorem ipsum. lorem ipsum, lorem ipsum"

        replaced_text = text.replace("lorem", "new", 2)

        print(replaced_text)  # Output: 'Lorem ipsum. new ipsum. new ipsum, lorem ipsum'
        ```

> Full list of Python string methods can be found at [https://www.w3schools.com/python/python_ref_string.asp](https://www.w3schools.com/python/python_ref_string.asp)