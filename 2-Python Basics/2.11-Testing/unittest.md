# Unit Testing in Python - `unittest` module

## 10.04.25 - Understanding the`unittest` module

- What is unit testing?
- The Python `unittest` module
- Setting up an environment for unit testing in Python
- Define test cases
- Assert methods for Unit Testing
- Best Practices

### What is Unit Testing?

- Involves testing individual units or components of code to ensure they function properly.
- It aims to validate that each unit, function or method, works as intended and produces the expected output.

### The Python `unittest` module

- This is a built-in module that comes as part of Pythons standard library
- The primary is to facilitate the creation of test cases and test suites to verify the behaviour and correctness of your code.
- The unittest module offers a class-based approach to define test cases. You create a test case class that inherits from the `unittest.TestCase` class
- within the test case class there methods that are defined where each method tests/represents a specific scenario/angle.
- Test methods are named starting with the prefix `test_` to allow for discovery by the testing framework.

**Advantages of the `unittest` module:**

1. Built-in framework: comes as part of the Python standard library, making it readily accessible without needing extra installations. Also makes it compatible across different Python environments.
2. Simple and Familiar syntax: It utilizes a class based approach, where test cases are defined as classes that inherit from `unittest.TestCase`.
3. Assertion Methods: it provides a wide range of assertion methods to compare expected and actual results.
4. Test Discovery: supports automated test discovery, which enables the discovery and execution of all test cases within a directory or module.
5. Test Fixtures: Within the unittest test cases you can define the `setUp()` and `tearDown()` methods. These will allow you to set up the necessary environment before executing each test and clean up any resources afterwards.
6. Test Suites: unittest supports the craetion of test suites, allowing you to group related test cases together.
7. Integration with Test Runners: it integrates wih test runners that are responsible for discovering and executing tests.
8. Extensibility: Developers can subclass `unittest.TestCase` to create test cases with additional functionality or override existing methods.

### Setting up an environment for unit testing in Python

1. Create a project directory: This will serve as the root directory for your program code and tests.

2. Create a virtual environment: This will allow you to isolates any of your projects dependencies.

    ```shell
    python3 -m venv .venv --prompt=<project-name>
    ```

    - This will create a virtual named `.venv` in your project directory.

3. Activate the virtual environment: 

    ```shell
    # For MasOS/Linux
    source .venv/bin/activate

    # For Windows
    .venv\Scripts\activate
    ```

    - Once activated your command should show the name of your virtual environment or the prompt you created

4. Create test files: In your project directory create a separate folder called tests. Inside the tests directory, create Python files with names starting with `test_` (e.g `test_calculator.py`) These files will contain your unit tests

- Your folder structure may look something like this:

        calculator
        ├── tests/
        │   ├── __init__.py
        │   └── test_calculator.py
        └── calculator.py

### Defining Tests using `unittest`

1. import the unittest Module:

    ```python
    import unittest
    ```

2. Create a test case class: Define a test case class that inherits from `unittest.TestCase`. This class will contain the test methods.

    - The class name should be prefixed with `Test`

    ```python
    class TestCalculator(unittest.TestCase):
        pass
    ```

3. Define test methods: define individual methods. Each method should start with the prefix `test_` to be discovered by the testing framework

    ```python
    class TestCalculator(unittest.TestCase):

        def test_add_returns_integer(self):
            pass
    ```

4. Write Assertions: Inside each test method, write assertions to check the expected behaviour of the function being tested.  Assertions compare the actual output of the function vs the expected output.

    ```python
    class TestCalculator(unittest.TestCase):

        def test_add_returns_integer(self):
            result = add(45, 15)
            self.assertEqual(result, <expected_result>, <error-message>)
    ```

    - You can use various assertions provided by unittest like `assertEqual`, `assertTrue`, `assertIsNone`, etc

- In order to run your tests you can use any of the following commands in your terminal from the root of your project folder:

    ```shell
    # Auto discovery
    python3 -m unittest

    # Make the test output verbose
    python3 -m unittest -v

    # Direct to a specific file
    python3 -m unittest tests.test_calculator

    # Run a specific test case(class)
    python3 -m unittest tests.test_calculator.TestCalculator

    # Run a specific test method
    python3 -m unittest tests.test_calculator.TestCalculator.test_add_returns_integer
    ```

### Assert Methods for Unit Testing in Python

Here are 10 commonly used assertion methods for Python functions using the unittest module:

1. `assertEqual(a, b)`: Checks if a and b are equal.

    ```python
    self.assertEqual(10, add(5, 5))  # Passes if add(5, 5) equals 10
    ```

2. `assertTrue(x)`: Checks if x evaluates to True.

    ```python
    self.assertTrue(result) # Passes if result is True
    ```

3. `assertFalse(x)`: Checks if x evaluates to False.

    ```python
    self.assertFalse(error)  # Passes if error is False
    ```

4. `assertIs(a, b)`: Checks if a is the same object as b.

    ```python
    self.assertIs(result, expected_result)  # Passes if result is expected_result (same object)
    ```

5. `assertIsNone(x)`: Checks if x is None.

    ```python
    self.assertIsNone(result)  # Passes if result is None
    ```

6. `assertIsNotNone(x)`: Checks if x is not None.

    ```python
    self.assertIsNotNone(result)  # Passes if result is not None
    ```

7. `assertIn(a, b)`: Checks if a is present in b.

    ```python
    self.assertIn(item, my_list)  # Passes if item is present in my_list
    ```

8. `assertNotIn(a, b)`: Checks if a is not present in b.

    ```python
    self.assertNotIn(item, my_list)  # Passes if item is not present in my_list
    ```

9. `assertRaises(exception, callable, *args, **kwargs)`: Checks if calling callable raises exception.

    ```python
    self.assertRaises(ValueError, divide, 10, 0)  # Passes if calling divide(10, 0) raises ValueError
    ```

10. `assertAlmostEqual(a, b, places)`: Checks if a and b are approximately equal up to a specified number of decimal places.

    ```python
    self.assertAlmostEqual(result, expected_result, places=2)  # Passes if result and expected_result are approximately equal up to 2 decimal places
    ```

These are just a few examples of commonly used assertion methods provided by unittest.
You can find more assert methods here: [https://docs.python.org/3/library/unittest.html](https://docs.python.org/3/library/unittest.html)

### Best Practices for Python Unit Testing

When writing unit tests in Python, it’s important to follow best practices to ensure effective and maintainable tests. Here are some best practices for Python unit testing:

1. **Test Readability and Maintainability**: Write clear, concise, and readable test cases. Use descriptive names for test methods and provide meaningful comments when necessary.
2. **One Assertion per Test**: Aim to have only one assertion per test method. This helps in isolating failures and makes it easier to identify the specific condition that caused the failure.
3. **Test Independence**: Ensure that each test is independent and does not rely on the state or results of other tests. Avoid sharing state between tests, as it can lead to unexpected dependencies and make test failures harder to diagnose.
4. **Test Coverage**: Strive for comprehensive test coverage by testing different scenarios, including typical cases, edge cases, and error conditions. Aim to cover all branches and possible execution paths of your code.
5. **Test Isolation**: Ensure that tests are isolated from external dependencies, such as databases, web services, or file systems. Use techniques like mocking or dependency injection.
6. **Test Documentation**: Good documentation helps other developers understand the tests quickly and facilitates test maintenance and future enhancements.
7. **Continuous Integration (CI)**: Integrate your unit tests into a continuous integration (CI) system that automatically runs the tests whenever changes are made to the codebase. This helps catch regressions early and ensures that the tests are executed consistently and regularly.
8. **Regular Test Maintenance**: Update and maintain your tests as your code evolves. Review and revise tests periodically to ensure their effectiveness and relevance.

