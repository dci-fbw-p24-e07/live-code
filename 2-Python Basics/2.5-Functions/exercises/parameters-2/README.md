# Variables, arguments and scope

## Description

In this exercise, we will focus on managing variables, arguments and scopes.

*In each function created throughout these exercises the body of the function must contain a **dosctring** (a first line with a string explaining what the function does).*

##

## Tasks

###

### Task 1

Define a global variable named `settings` as a dictionary with a key `title` that contains a string of your choice, then create a function named `change_site_title` that takes one argument of type String and assigns it to the key `title` in the global variable `settings`.

Use this test case:

```
print(settings)
change_site_title("A new fancy title")
print(settings)
```

- Your result should look like this:

```
{'title': 'My original title'}
{'title': 'A new fancy title'}
```

###

### Task 2

Keep the previous code and define now a global variable named `default_settings` as a dictionary with a key `title`, then create a function named `get_title` that takes one argument as a dictionary that defaults to `default_settings` and returns the content of the key `title` in the given dictionary.

Use this test case:

```
print(get_title(settings))
print(get_title())
change_site_title("A new fancy title")
print(get_title(settings))
print(get_title())
```

- Your result should look like this:

```
My original title
My original title
A new fancy title
My original title
```

###

### Task 3: Default and non default arguments combined

Add a key `pages` to your previous `settings` and `default_settings` dictionaries.

Now, define two functions named `get_pages` and `add_page`. They will both have a parameter `settings` that will default to `default_settings`.

The function `get_pages` will simply return the list stored in the key `pages` of the given `settings` dictionary.

The function `add_page` will have an additional positional argument that will be the page as a dictionary. The function will append this argument to the `pages` key of the given `settings` dictionary.

Use this test case:

```
home = {"title": "Home", "path": "/"}
add_page(home)
print(get_pages())
print(get_pages(settings))
about = {"title": "About", "path": "/about/"}
add_page(about, settings)
print(get_pages())
print(get_pages(settings))
```

- Your result should look like this:

```
[{'title': 'Home', 'path': '/'}]
[]
[{'title': 'Home', 'path': '/'}]
[{'title': 'About', 'path': '/about/'}]
```

###

### Task 4:

Create a new function named `print_user_profile` that will take 4 parameters:

- **gender**: a String indicating the gender of the user. The values available should be `male` and `female`. *The default value should be `female`.*
- **first**: a String with the first name of the user. *The default value should be **John** if the gender is `male` but it should be **Jane** if the gender is `female`.*
- **last**: a String with the last name of the user. *The default value should be **Doe**.*
- **pictures**: a List of strings with the name of the picture files. *The default value should be an empty list.*

This function will add a common header picture to all profiles and then it will print on screen the name of the person and its list of pictures (including the common header). Example:

```
The user {first} {last} has the following pictures:
common_header.png
{user_picture1.png}
{user_picture2.png}
```

If the user has no pictures it should print only the `common_header.png` file name.

Use this test cases:

```
test_data1 = {
    "gender": "male",
    "last": "Brown",
    "pictures": ["holidays1.png", "easter_grandma.png"]
}
test_data2 = {
    "first": "Alicia",
    "last": "Schmidt"
}
test_data3 = {
    "last": "Korkov",
    "pictures": ["sunset.png"]
}
print_user_profile(**test_data1)
print_user_profile(**test_data2)
print_user_profile(**test_data3)
print_user_profile(**test_data2)

```

- Your result should look like this:

```
The user John Brown has the following pictures:
common_header.png
holidays1.png
easter_grandma.png
The user Alicia Schmidt has the following pictures:
common_header.png
The user Jane Korkov has the following pictures:
common_header.png
sunset.png
The user Alicia Schmidt has the following pictures:
common_header.png
```
