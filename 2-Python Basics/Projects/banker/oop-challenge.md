# The Bank Project

1. Create a parent class called Bank:

    a. Create a class attribute that stores all account details
        { `account_number` : [ `name`, `account_balance`, `account_type` ] }

    b. In the constructor method:

        i. Initialize `bank_name`: str
        ii. Initialize `name`: str
        iii. initialize `account_balance`: float
        iv. initialize `account_type`: str

    c. Create a method called `create_account` that takes name, `initial_deposit` and `account_type` as arguments and adds them to  accounts. Generate `account_number` using the random module.

    d. Create a method called `authenticate` that takes `name` and `account_number` as arguments and checks if they are in accounts.

    e. Create a method called `withdraw` that takes `withdraw_amount` as an argument and deducts it from the account balance. Return the final balance

    f. Create a method called `deposit `that takes `deposit_amount` as an argument and adds it to the account balance. Return the final balance

    g. Create a method called `check_balance` that takes `account_number` as an argument and returns the balance.

2. Using the above class create a command line program that:

    1. Prints the message `Welcome to {bank_name}` and gives the user options to either login or register. If they opt to register take them to the registration where they can enter their details. after they have registered immediately take them back to the Welcome menu where they can now opt to login.
    2. When a user logs in it must print `Welcome, {name}` and the user must be presented with 3 options:
        1. Withdraw - Here the user must simply enter the amount they wish to withdraw and it must be deducted from their current account balance. Display the final balance
        2. Deposit - Here the user must simply enter the amount they wish to deposit and it must be deducted from their current account balance. Display the final balance
        3. Check balance - Will simply display the users balance
        4. Logout - This will take them to the original menu(login/registration)

## Tips

- This is a standalone project so remember to create it in it's own folder.
- Make sure you create a virtual environment for the project
- a `.gitignore` file should also be included