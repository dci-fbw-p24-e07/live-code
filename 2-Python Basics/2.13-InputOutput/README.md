# Input and Output - I/O

## 30.04.25 - File operations

- Opening files
- Reading files
- Writing to files
- Closing files
- Using `with...open` statement
- Different file modes
- `io` module and streams

## What is a file?

- A file is a named location used for storing data.
- The kind of data stored is dependent on the file extension(e.g `.txt`, `.py`, `.json`, etc)
- The kind of file it is may also influence the way we write data to it

### Opening Files

- Python provides the `open()` function to open files
- You can attach the open function to a variable name so in order to do further operations.

**Syntax:**

```python
file_1 = open("<filename/path>", "<mode>")
```

- Where mode is a single letter that specifies the operations that can be used to manipulate the file
- By default the open function uses `r` (read) mode

**Example:**

```python
file_1 = open("documents/main.py", "w")
```

**Different modes to open a file:**

| Mode | Description |
|------|-------------|
| `r` | Opening a file in read mode(default) |
| `w` | Opening a file in write mode. Overwrites existing file content |
| `a` | Opening a file in append mode. Adds content to the end of the file |
| `x` | Opening a file for exclusive creation |
| `t` | Opening a file in text mode(default) |
| `b` | Opening a file in binary mode |
| `+` | Opening a file in both read and write modes |

### Reading files

- After a file is opened we use the `read()` method on it to read its contents

**Syntax:**

```python
file_1 = open("<filename/filepath>")

# Read the file
contents = file_1.read()
```

**Example:**

```python
file_1 = open("documents/main.py")

contents = file_1.read()
print(contents)
```

### Writing files

- To write to a file in Python you need to specify the `w` mode when opening the file.
- This would then allow you to use the `write()` method to add contents to the file
- If the file does not exist it will be created
- The contents that you send to the file should match the expected file format to maintain consistency and not break files.

**Syntax:**

```python
file_1 = open("<filename/filepath>", "w")

# Write to the file
file_1.write("<contents-of-the-file">)
```

**Example:**

```python
file_1 = open("documents/main.py", "w")

# Write to the file
file_1.write("x = 15")
```

### Closing files

- The `open()` function does not automatically take care of closing the file
- We need to explicitly call the `close()` method on the file object after we are done performing operations on it.

**Syntax:**

```python
file_1 = open("<filename/filepath>", "+")

# Write to the file
file_1.write("<contents-of-the-file">)

# Read the file
contents = file_1.read()

# Close the file
file_1.close()
```

- This will free up any resources that are tied to the file.
- It is good programming practice to always close the file.

**Example:**

```python
file_2 = open("dummy.txt", "w")

file_2.write("We are going to have another 4 day weekend")

file_2.close()
```

### `with...open` statement

- This statement takes care of opening and closing the file.
- It performs whatever operations you have specified in the code block and then it closes the file immediately after

**Syntax:**

```python
with open("<filename/filepath>", "<mode>") as <alias>:
    # perform operations
    pass
```

**Example:**

```python
with open("dummy.txt", "w") as file:
    file.write("Checking out this cool shortcut!")
```

### Commonly used file methods

| Method | Description |
|--------|-------------|
| `close()` | Closes an opened file |
| `read(n)` | Reads the file content. Where `n` represents the number of characters |
| `tell()` | Returns an integer that represents the current position of the file's object | 
| `write(s)` | Writes string to a file. Where `s` represents the string to be written |
| `writelines(lines)` | writes a `list` of lines to the file |

## 06.05.25 - File manipulation with the `os` and `io` modules

- What is file manipulation?
- The `os` module
- File operations using the `os` module

**Self Study:**

- What is the `io` module?
- using the `StringIO` class of the `os` module
- using the `BytesIO` class of the `os` module

### What is file manipulation?

- This is changing the files properties(location, size, etc) or contents
- Files can be created, edited, opened, deleted, moved, copied, etc.

### The `os` module

- This module allows you to interact with your operating system in the form of Python code
- It can be used for more than just file manipulation and operations
- It is part of the Python standard library
- It independent of operating system - it can be utilised by MasOS, Linux or Windows.
- To use the `os` module we need simply import it to our source code

### File operations

1. Getting the current directory:

    ```python
    import os

    curr_dir = os.getcwd()
    ```

    - It returns the Current Working Directory in form of a string
    - It returns the full path of where you have run the command from

2. Changing the directory:

    ```python
    os.chdir("<path>")
    ```

    - It changes the Current Working Directory to the path you have specified
    - Does not return any value

3. List Directories and Files

    - all files and directories inside a directory can be retrieved using the `listdir()` method
    - This method also takes a path to represent the directory you want to list

    ```python
    os.listdir("<path>:optional")
    ```

    - It returns all files and directories as strings inside a list

4. Making a new directory:

    - The `mkdir()` method is used to create a new directory.
    - If the full path is not specified, the new directory will be created in the current working directory

    ```python
    os.mkdir("<new-directory-name>")
    ```

5. Removing a file or directory:

    1. To delete a file:

        - The `remove()` method can be used to delete file by giving the file path

        ```python
        os.remove("<filepath>")
        ```
    
    2. To delete an empty directory:

        - The `rmdir()` method is used to delete an empty directory with the specified path

        ```python
        os.rmdir("<path>")
        ```

    3. To delete a non-empty directory:

        - The `rmtree()` method from the `shutil` module can be used to delete a specified non-empty directory and all of its contents

        ```python
        import shutil

        shutil.rmtree("<path>")
        ```

