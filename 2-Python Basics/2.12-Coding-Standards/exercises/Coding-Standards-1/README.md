# Coding Standards - Flake8 plugins

## Description

In this exercise, we will use flake8 to explore some additional PEP8 and PEP257 recommendations.

You will need to have [flake8](https://pypi.org/project/flake8/) installed, ideally in a container or virtual environment.

> For this exercise we recommend you to use a standard simple text editor or your current editor with the Linter disabled.

##

## Tasks

###

### Task 1

Now add the `pep8-naming` plugin for `flake8`.

`pip install pep8-naming`

Create a new file and define a class that will be used to define **document folders**. Name it like that, in singular but with two words, and using the style you think appropriate.

Inside this class define two variable names that will be called **label name** and **label style**, choose your naming style. The **label name** will be assigned the text value "Folder name" and the **label style** will be assigned the text value "bold".

Define a global function named **get path** (choose your naming style) that will take a parameter called **label name** and will return the concatenation of a root path (any string you like) and the label name given.

Define a method in the **document folder** class named **get label** (two words) that returns a dictionary with the **label style** and **label path** (after a call to the global function **get path**). The keys of the dictionary may be named `style` and `path`.

Finally, instantiate the class and assign it to a variable's name of two words, **document folder**. Then print the result of calling the method **get label** of the instantiated object.

> Before you start typing you may want to read first about PEP8 naming conventions at [https://www.python.org/dev/peps/pep-0008/#prescriptive-naming-conventions](https://www.python.org/dev/peps/pep-0008/#prescriptive-naming-conventions).

Description in pseudo-code:
```
function GETPATH takes LABELNAME as text {
  return concatenate '/path' and LABELNAME
}
class DOCUMENTFOLDER {
  PROPERTIES {
    LABELNAME = "Folder name"
    LABELSTYLE = "bold"
  }
  METHODS {
    GETLABEL takes no argument {
      return DICT(path=GETPATH(LABELNAME), style=LABELSTYLE)
    }
  }
}
MYDOCUMENTFOLDER = DOCUMENTFOLDER()
print MYDOCUMENTFOLDER.GETLABEL()
```

Then check the style with flake8. If it produces any errors, fix them and run it again until it produces no error. Then compare your result with the solution.

###

### Task 2

Now add the following plugin:

`pip install flake8-docstrings`

This command will install a plugin that uses `pydocstyle`, a tool to check for PEP257 recommendations related to docstrings.

> Use simple one-line docstrings.
>
> You can find more information on [one-line](https://www.python.org/dev/peps/pep-0257/#one-line-docstrings) docstrings in the PEP257 documentation.

Now check the style of your code from the previous task with flake8. If it produces any errors, fix them and run it again until it produces no error.

###

### Task 3

Now change the docstring of the class to a [multi-line](https://www.python.org/dev/peps/pep-0257/#multi-line-docstrings) docstring.

Type a summary in the first line and then a description mentioning all the attributes and methods publicly available for this class.

Check the style with flake8. If it produces any errors, fix them and run it again until it produces no error.

###

### Task 4

Take a look at the file [src/data/task4.py](src/data/task4.py).

This is a fragment of an old version of a real project. The script is not functional because it has been ripped from its context and is missing many references, which have been mocked to by-pass some of the syntax tests of flake8 so that we can concentrate on the style.

The script comes from a Django view that takes some parameters from the HTTP request and sends a query to the database to produce a result, which is returned to the browser.

Go to the file's directory and execute the following flake8 command:

`flake8 task4.py`

Now fix all the error styles until the previous command produces no error.

> **Important!** do not spend time checking the code itself. The only aim of this exercise is to practice on how to transform a non-conformant code into a **PEP8** and **PEP257** conformant code, we don't need to make it work.
>
> **Even more important!!** do not just delete lines to remove the style error. Even though the code's execution can't be tested, the instructions must remain the same.

###

### Task 5

Now take a look at the file [src/data/task5.py](src/data/task5.py). This is another fragment of old code.

This time, the script comes from a Django view that processes the sending of notifications to users.

Go to the file's directory and execute the following flake8 command:

`flake8 --max-complexity 8 task5.py`

> This command modifies the standard behavior of flake8 and asks to produce an alert when the complexity level of any function is above the indicated level.

Now fix all the error styles until the previous command produces no error.

> **Important!** do not spend time checking the code itself. The only aim of this exercise is to practice on how to transform a non-conformant code into a **PEP8** and **PEP257** conformant code, we don't need to make it work.
>
> **Even more important!!** do not just delete lines to remove the style error. Even though the code's execution can't be tested, the instructions must remain the same.
>
> To remove the `C901` error (complexity too high), split the `save_notification` function into two meaningful functions.
