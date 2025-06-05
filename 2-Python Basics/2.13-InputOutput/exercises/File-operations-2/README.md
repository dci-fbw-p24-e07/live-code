# File I/O

## Description

In this exercise, we will focus on opening files for reading and writing purposes.

##

## Tasks

###

### Task 1

Convert the text file [src/data/task1.txt](src/data/task1.txt) to a binary file `task1.bin`.

> Hint: open two files, one as the source for text reading and the other one as the target for binary writing.

###

### Task 2

Create a file for each dictionary in the following list:

```
files = [
    {
        "name": "todos.txt",
        "content": ["My ToDos:", "", "Go shopping", "Finish module"]
    },
    {
        "name": "bookmarks.txt",
        "content": ["My links:", "", "https://google.com", "https://digitalcareerinstitute.org"]
    }
]
```

**The file should only be created once. If the file already exists it should throw an exception.**

> Pay attention to line breaks.
>
> Create the files as text files.

- The script should create two different files:

**File 1**: todos.txt
```
My ToDos:

Go shopping
Finish module

```

**File 2**: bookmarks.txt
```
My links:

https://google.com
https://digitalcareerinstitute.org

```

- Executing the code again should produce the following exception:

```
FileExistsError: [Errno 17] File exists: 'todos.txt'
```

###

### Task 3

With the files produced in the previous task, now take the following list and add the new content at the end of each file.

```
additions = [
    {
        "name": "todos.txt",
        "content": ["Call mom", "Walk the dog"]
    },
    {
        "name": "bookmarks.txt",
        "content": ["https://python.org", "https://www.djangoproject.com/"]
    }
]
```

> Hint: use a method that guarantees the content is only added to the file and the previous content will remain untouched.

- After executing your script, the files should look like this:

**File 1**: todos.txt
```
My ToDos:

Go shopping
Finish module
Call mom
Walk the dog

```

**File 2**: bookmarks.txt
```
My links:

https://google.com
https://digitalcareerinstitute.org
https://python.org
https://www.djangoproject.com/

```

###

### Task 4

We already called mom and we don't need to bookmark Google, so now replace "Called mom" with "Clean up house" and replace the link "https://google.com" with "https://www.w3resource.com".

Use the following list of changes:

```
changes = [
    {
        "name": "todos.txt",
        "change": ("Call mom", "Clean up house")
    },
    {
        "name": "bookmarks.txt",
        "change": ("https://google.com", "https://www.w3resource.com")
    }
]
```

> You are NOT allowed to use the `replace` method of the string object.
>
> Since the replacing strings have different lengths, you may want to store the content after the changing line and add it to your writing.

- After executing your code, the files should look like this:


**File 1**: todos.txt
```
My ToDos:

Go shopping
Finish module
Clean up house
Walk the dog

```

**File 2**: bookmarks.txt
```
My links:

https://www.w3resource.com
https://digitalcareerinstitute.org
https://python.org
https://www.djangoproject.com/

```

###

### Task 5

Our `todos.txt` is going to be highly confidential and we want to store a version of it, named `todos.secret`, that is not human readable.

The `secret` file will have 1 character per row and instead of the character, it will be a decimal integer representing the Unicode code value.

Your first task consists in writing a Python code that reads the file `todos.txt` and creates the file `todos.secret` according to the specifications.

Once you have created the `todos.secret` file, you should create another piece of code to read the `secret` file and print the decoded and human readable version of it.

> Hint: you can use the `ord` and `chr` [built-in functions](https://docs.python.org/3/library/functions.html).

- The contents of the file `todos.secret` should look like this:

```
77
121
32
84
111
68
111
115
58
10
10
71
111
32
115
...
```

- Reading this file with your decoding code should produce this:

```
My ToDos:

Go shopping
Finish module
Clean up house
Walk the dog

```
