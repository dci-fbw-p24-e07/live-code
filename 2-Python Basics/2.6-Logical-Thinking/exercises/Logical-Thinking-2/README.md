# Python logical expressions

## Description

In this exercise, we will practice on more complex logical expressions including
various predicates and operators.

##

## Collection Basic

## List

A list is a built-in data structure that represents an ordered collection of items. Lists can be stored in variables just like Strings can. For example to store a list of car brands you could create a variable `car_brands` with a list of brands like `'BMW'`, `'Audi'`, and `'Volkswagen'`. This translates to the following code:

```python
car_brands = ['BMW', 'Audi', 'Volkswagen']
```

Elements in this list can be accessed by zero-based, numbered indices. For example `car_brands[0]` would return `BMW`.

To work with all elements in a list you can loop over its elements and for example print them like this:

```python
for brand in car_brands:
  print(brand)
```

Lists can also be altered. Elements can be added using the `append` method:

```python
car_brands.append('Volvo')
```

Using indices elements can also be removed from a list again using the `pop` method:

```python
car_brands.pop(0)
```


## Dictionary

A dictionary is a built-in data structure that represents a collection of key-value pairs. Dictionaries (also called dicts) of course can also be stored in variables. For example let's store fruits, grouped by their color:

```python
fruits = {
  'red': ['apple', 'cherry', 'strawberry'],
  'orange':['orange', 'mango', 'peach'],
  'yellow': ['banana', 'lemon']
}
```

Elements in this dictionary can be accessed by keys which are Strings. For example all red fruits can be accessed using `fruits['red']`. The nested value `apple` could be accessed using `fruits['red'][0]`.

To add an element to or update one in a dictionary you can use the key syntax as well or use the `update` method:

```python
fruits['green'] = ['watermelon']
fruits.update({'green': ['watermelon']})
```

To remove an element from a dictionary one can use the `pop` method with a specified key. For example to remove all yellow fruits:

```python
fruits.pop('yellow')
```

You can also loop over dictionaries like you can loop over lists using the `items` method:

```python
for color, colored_fruits in fruits.items()
  print(color + ' fruits:')
  for fruit in colored_fruits:
    print('- ' + fruit)
```


##

## Tasks

###

### Task 1:

Let's consider the following list of users:

```
users = [
    {
        "name": "Holly",
        "type": "Student",
        "password": "hunter",
        "modules": [
            {
                "title": "Computer basics",
                "completed": True
            },
            {
                "title": "Python basics",
                "completed": False
            }
        ]
    },
    {
        "name": "Peter",
        "type": "Student",
        "password": "pan",
        "modules": [
            {
                "title": "Computer basics",
                "completed": False
            }
        ]
    },
    {
        "name": "Luke",
        "type": "Student",
        "password": "skywalker",
        "modules": [
            {
                "title": "Computer basics",
                "completed": True
            }
        ]
    },
    {
        "name": "Janis",
        "type": "Teacher",
        "password": "joplin"
    }
]
```

Using the concepts, and some code from the previous exercises, define a function named `show_registration` that checks if a user is registered to a specific module.

The function will accept three input arguments:

- **username**. `String`
- **password**. `String`
- **modulename**. `String`

The function may print any of the following messages:

- `You are registered to the module {modulename}`.
It will print this message if the user is a student and in his `modules` key has a module with a `title` equal to the argument `modulename`
- `You did not register to the module {modulename}`
It will print this message if the user is anonymous or is a student and in his `modules` key DOES NOT have a module with the given title.
- `You are a teacher`
It will print this message if the username is a teacher.

> You may use additional functions to filter or store logical expressions to use in your `show_registration` function.

> You may use more than one conditional.

Use the following code to test:

```
username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
modulename = input("What module do you want to check? ")
show_registration(username, password, modulename)
```
- Your result should look like this:

```
What is your username? Peter
Type the password for username Peter: pan
What module do you want to check? Computer basics
You are registered to the module Computer basics.
```
```
What is your username? Luke
Type the password for username Luke: skywalker
What module do you want to check? Python basics
You did not register to the module Python basics.
```
```
What is your username? Janis
Type the password for username Janis: joplin
What module do you want to check? Django
You are a teacher.
```
```
What is your username? Anonymous
Type the password for username Anonymous: empty
What module do you want to check? Computer basics
You did not register to the module Computer basics.
```

# Task 2

Now add another function named `has_completed_module` similar to `show_registration` with the same input arguments and the following differences:

- This time, the function will do nothing if the user is valid and a teacher.
- It will check if, besides having a particular module in the user's list, the module has the key `completed` set to `True`.

Use the following code to test:

```
username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
modulename = input("What module do you want to check? ")
show_registration(username, password, modulename)
has_completed_module(username, password, modulename)
```
- Your result should look like this:

```
What is your username? Peter
Type the password for username Peter: pan
What module do you want to check? Computer basics
You are registered to the module Computer basics.
You did not complete the module Computer basics.
```
```
What is your username? Luke
Type the password for username Luke: skywalker
What module do you want to check? Computer basics
You are registered to the module Computer basics.
You have completed the module Computer basics.
```
```
What is your username? Janis
Type the password for username Janis: joplin
What module do you want to check? Django
You are a teacher.
```
```
What is your username? Anonymous
Type the password for username Anonymous: password
What module do you want to check? Django
You did not register to the module Django.
You did not complete the module Django.
```

# Task 3

Now we are given this list of modules:

```
modules = [
    {
        "name": "Computer basics"
    },
    {
        "name": "Python basics",
        "requirement": "Computer basics"
    },
    {
        "name": "Django",
        "requirement": "Python basics"
    }
]
```

Add a new function named `may_enroll` with three input parameters:

- **username**. `String`
- **password**. `String`
- **modulename**. `String`

This function should return `True` in the following cases:

- The user is anonymous and the module has no requirement (they can always register).
- The user is a student and:
    - The user is not already registered to that module.
    - The module has no requirement or it has one and the user meets the requirement (is also registered to the requirement and its `completed` flag is set to `True`).

In any other case, the function should return `False`.

> Keep the code from previous exercises.

> A teacher cannot register to any module.

> An anonymous user will only be allowed to register if the module has no requirement. If that happens, the script should not execute any other logical expression.

> Use as many functions as needed to keep the logical expressions easy to read. Use semantic names for those functions to improve the readability. Example: is_anonymous(), has_no_requirement(), meets_requirement(), ...

> Use any concept learned on the slides: short-circuiting, grouping,...

Use the following code to test:

```
username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
modulename = input("What module do you want to check? ")
show_registration(username, password, modulename)
has_completed_module(username, password, modulename)
if may_enroll(username, password, modulename):
    print(f"You may register to the module {modulename}.")
else:
    print(f"You may not register to the module {modulename}.")
```
- Your result should look like this:

```
What is your username? Peter
Type the password for username Peter: pan
What module do you want to check? Computer basics
You are registered to the module Computer basics.
You did not complete the module Computer basics.
You may not register to the module Computer basics.
```

```
What is your username? Peter
Type the password for username Peter: pan
What module do you want to check? Python basics
You did not register to the module Python basics.
You did not complete the module Python basics.
You may not register to the module Python basics.
```

```
What is your username? Luke
Type the password for username Luke: skywalker
What module do you want to check? Python basics
You did not register to the module Python basics.
You did not complete the module Python basics.
You may register to the module Python basics.
```

```
What is your username? Janis
Type the password for username Janis: joplin
What module do you want to check? Django
You are a teacher.
You may not register to the module Django.
```

```
What is your username? Anonymous
Type the password for username Anonymous: password
What module do you want to check? Computer basics
You did not register to the module Computer basics.
You did not complete the module Computer basics.
You may register to the module Computer basics.
```

```
What is your username? Anonymous
Type the password for username Anonymous: password
What module do you want to check? Django
You did not register to the module Django.
You did not complete the module Django.
You may not register to the module Django.
```

```
What is your username? Peter
Type the password for username Peter: pan
What module do you want to check? PHP
You did not register to the module PHP.
You did not complete the module PHP.
You may not register to the module PHP.
```
