# Collections in Python

- What are collections?
- Types of collections
- Linear vs Associative collections
- Lists

## What are collections?

- Collections in Python are container data structures.
- They allow grouping of different elements together.
- These elements can be of different data types.

### Types of collections

- Collections have different characteristics based on declaration and usage.

1. **List:**

    - is declared in square brackets `[]`
    - it is mutable
    - stores duplicate values
    - elements can be accessed using indexing

    **Syntax:**

    ```python
    # declare empty list
    list_1 = []
    list_2 = list() # Result: []

    # declare list with elements
    my_list = [12, "twelve", 12.5, True]
    ```

2. **Dictionary:**

    - is declared using curly braces `{}`
    - has key-value pairs
    - each key is unique and acts as an identifier
    - values are mutable

    **Syntax:**

    ```python
    # Declaring an empty dictionary
    dict_1 = {}
    dict_2 = dict() # Result: {}

    # Declaring a dictionary with elements
    my_dict = {
        "key": "value",
        1: True,
        "two": [],
    }
    ```

    > **NOTE: when declaring a key it either has to be an integer or a string**

3. **Tuple:**

    - is declared using parentheses `()`
    - allows duplicate entries
    - is unordered
    - it is immutable
    - elements can be accessed using indexing

    **Syntax:**

    ```python
    # Declaring a tuple 
    my_tuple = (1, 2, -5)
    my_tuple_2 = tuple(("Jack", "Mary", "Paul", "Sophia"))  # Result: ("Jack", "Mary", "Paul", "Sophia")
    ```

4. **Set:**

    - is declared using curly braces `{}`
    - is unordered
    - is not indexed
    - is is mutable

    **Syntax:**

    ```python
    # Declare an empty set
    my_set = set()

    # Declare a set with with elements
    my_set = {112, 34, "fifteen", True}
    ```

### Linear vs Associative

1. Linear

    - A linear data structure is one in which elements are arranged sequentially or linearly
    - where each element is attached to its previous and next adjacent elements
    - For example: array, stack, queue, linked list, etc

2. Associative

    - Data structure where elements are not placed sequentially or linearly.
    - aka Non-linear data structures.
    - Elements cannot be traversed in a single run only
    - For example: trees and graphs

> To learn more about the different data structures: [https://www.adservio.fr/post/data-structure-types-operations](https://www.adservio.fr/post/data-structure-types-operations)



