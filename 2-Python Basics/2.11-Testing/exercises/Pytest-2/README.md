# Python-testing-pytest2

In this exercise, you will be using [pytest](https://pytest.org) for testing.

For a very complicated application, you need to write a general function that
compares various other variables with the integer 7.
You are working in a setting of test driven development and all the tests have been
written for you already. You can find them in `src/test_app.py`.

It is now your job to write a function `compare_to_seven(input: Union[int, str, Callable])`
in the `src/app.py` file that makes all tests pass successfully.

Run the tests by executing **pytest** inside the `src/` folder.


> **Hint:** Take a look at [ord()](https://docs.python.org/3/library/functions.html#ord)
and [str.isnumeric()](https://docs.python.org/3/library/stdtypes.html#str.isnumeric) and
see if these can help you.
---
