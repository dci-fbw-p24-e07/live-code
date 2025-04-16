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

## 11.04.25 - TDD and Fixtures

- Using TDD to document code
- Using the `setUp()` and `tearDown()` methods
- Testing OOP

### The Aquarium 

- A company has tasked with creating a program to manage their aquarium. The aquarium has various tanks that can hold multiple type of fish. Each tank is only supposed a maximum of 10 fish. But you can have different kinds of fish in the same tank. The owner also wants the program to give them alerts on when a tank is full of water or it is empty. Tanks must always have water, the program should be able to trigger the refilling of a tank. The main thing that program should be able to track is when fish are being added to a tank

Requirements:

1. add_fish_to_tank(list_of_fish) - maximum fish should be 10 per tank, if it exceeds raise exception
2. fiill_with_water() - set attribute has water to True

## 16.04.25 - Mocking and Stubbing

- What is mocking?
- What is stubbing?
- Key differences between mocking and stubbing
- Implementing Mocking using the `unittest` module
- Mock vs MagicMock

### What is mocking?

- Mocking is a technique used to replace the real object or functions with mock objects or functions during testing.
- This allows us to simulate the behaviour of the code blocks without actually making permanent changes or side effects on the program. 
- Mocking allows you to isolate the code under test and control the behaviour of external dependencies, such as external services, databases or functions that have side effects, without actually invoking them.

### What is stubbing?

- Stubs take the place of the code in the unit that is being tested.
- It allows the developer to manipulate the response or result so that the unit can be safely tested in various contexts.

#### Mocking vs Stubbing

|     | Stubs | Mocks |
|-----|-------|-------|
| Primary Purpose | Mimic behaviour of real components with predetermined responses. | Record and validate interactions between the object under test and its collaborators | 
| Characteristics | <li>Predictable outcomes</li> <li> Don't throw exceptions</li> <li>Simulate specific situations</li> | <li> Observers and validators</li> <li>Raise excptions for unexpected calls</li> <li>Verifies method call order and frequency</li> |
| Use Cases | Testing outcomes without considering interactions | Ensuring method calls and interactions occur as expected |
| Testing Focus | State Testing: Focusing on outcomes | Behaviour Testing: Emphasizing component interactions. |

### Implementing Mocking using the `unittest` module

1. Import the `unittest` module

    ```python 
    import unittest

    # Or 

    from unittest import Mock, MagicMock
    ```

2. Create mock objects

    ```python
    # Created a basic mock object
    mock_obj = Mock()

    # Creating a MagicMock object that behaves like a real object
    magic_mock_obj = unittest.MagicMock()
    ```

**Example:**

- We have a program that mainly interacts with files. It creates, updates, deletes and can any other manipulations like copying or moving the files. 
- In this scenario we want to test whether or not the deletion function (`rm`) actually works but we want to avoid the side effect of actual files being deleted.

### Mock vs MagicMock

|   | Mock | MagicMock |
|---|------|-----------|
| Magic/Dunder methods | Does not include implementations for magic methods by default. You have to define the explicitly | Includes the default implementations for most magic methods. |
| Usage | Use when mocking regular methods and attributes | Use when you want to mock an object that relies heavily on the magic methods |
| When to use | <li>You are testing interactions with standard methods and attributes</li> <li>You want more control over what is mocked and avoid unintended behaviour from automatically mocked magic methods</li> | <li>You need to mock an object that uses magic methods extensively(e.g objects implementing custom behaviour for operations like `__add__`, `__str__`,`__getitem__`, etc)</li> <li>You prefer convenience and reduced boilerpalte for setting up such mocks</li> |



