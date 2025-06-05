# Unittest Mocking

## Task1

Write a test to check if the `rm` function in `src/app.py` will delete a file.

## Task2

Write a test to check if the `rm` function in `src/app.py` will call the `os.remove` function if the file exists - without deleting the file. Use `unittest.mock` for this purpose.

## Task3

Write a test to make sure that the `rm` function in `src/app.py` will **NOT** call the `os.remove` function if the file **DOES NOT** exist. Use `unittest.mock` for this purpose.

## Task4

Fix the `rm` function in `src/app.py` so that it will raise a **FileNotFoundError** error if the file does not exist.

## Task5

Write a test to check if the `rm` function in `src/app.py` will raise a **FileNotFoundError** error if the file **DOES NOT** exist. Use `unittest.mock` for this purpose.

## Objectives:
- Learn about unittest.mock.
- Learn about mock usage.
- Simulate mock fail cases.

> **Hint:** Run the tests by executing:

    python3 mock_test.py

    python3 no_mock_test.py

> Or run the test with more details by executing:

    python3 -m unittest -v mock_test.py

    python3 -m unittest -v no_mock_test.py
