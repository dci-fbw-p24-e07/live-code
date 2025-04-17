# 17.04.25 - `pytest` Basics

- What is `pytest`?
- Key features of pytest
- Basic usage
- Advantages of `pytest` over `unittest`
- Implementing `pytest` in place of `unittest`

## What is `pytest`?

- Easy to use 3rd party testing framework for Python.
- It offers a comprehensive suite of features to make testing easier and more ideal for both simple unit tests and complex functional testing.
- It allows you to write more concise and readable test cases using Python's familiar syntax
- Pytest has an ecosystem of plugins that boost its capabilities and allows you to create customized testing workflows.

### Key Features

1. **Simple syntax:** offers an easy approach to writing tests, making it accessible for beginners.
2. **Assertion introspection:** provides easier debugging by highlighting the exact point of failure.
3. **Compatibility:** Seamlessly integrates with existing unittest and nose test suites, allowing you to migrate to pytest without rewriting tests.
4. **Plugin-based architecture:** The frameworks extensibility through plugins supports customization and enhancement of core functionalities.

### Basic Usage

#### Installation of `pytest`

1. Create a project folder and navigate into it:

    ```shell
    mkdir <project-name>

    cd <project-name>
    ```

2. Create and activate the virtual environment:

    ```shell
    # Create
    python3 -m venv .venv --prompt="<venv-name>"

    # Activate
    source .venv/bin/activate
    ```

3. Install `pytest` using the `pip` command:

    ```shell
    pip install pytest
    ```

    - This command will install the package in the currently activated virtual environment

4. Keep track of the packages installed in the virtual environment:

    ```shell
    pip freeze > requirements.txt
    ```

    - This will create a file that has all the currently installed packages for that virtual environment including the current version.
    - This will allow someone to install all required packages using the command `pip install -r requirements.txt`

#### Creating test cases with `pytest`

1. Import import `pytest`:

    ```python
    import pytest
    ```

2. Define a test method:

    ```python
    def test_pay_success():
        wallet = Wallet(100)
        wallet.pay(10)
        assert wallet.balance == 90
    ```

**Using fixtures:**

1. Create the fixture method:

    ```python
    @pytest.fixture
    def empty_wallet():
        return Wallet()

    @pytest.fixture
    def wallet():
        return Wallet(200)
    ```

2. Use the fixtures on test methods:

    ```python
    def test_default_initial_amount(empty_wallet):
        assert empty_wallet.balance == 0

    def test_wallet_initial_balance_success(wallet):
        assert wallet.balance == 200
    ```

- You first define the fixture using the `pytest.fixture` decorator
- The function name given will now be used as the fixture throughout testing.
- To use the fixture on a test method it needs to be passed as a parameter

#### Running tests with `pytest`

1. ```shell
    pytest
    ```

