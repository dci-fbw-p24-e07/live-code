# Amazon expenses tracker project

## Topics covered
- Regular expressions
- datetime
- conditional statements
- loops
- strings 
- Prints and formatting. 
- logical operators
- basic math functions
- functions
- Command Line Interface
- Collections

## Description
This project would be designed to help users track their Amazon expenses. It would allow users to enter the details of each purchase they make, such as the date, item, cost, quantity and any other pertinent information. 
The project would then use this data to generate reports that show the user’s total spending on Amazon, as well as the average cost.

## Objectives: 

1. Create an application that allows users to enter the details of their Amazon purchases. 
2. Generate reports that show the user’s total spending on Amazon, as well as the average cost. 
3. Incorporate features that make the application easy to use and intuitive. 
4. Encapsulate specific logics in functions.

## Success Criteria: 

1. Users should be able to successfully and accurately add and view their Amazon purchase data.
2. Reports should accurately reflect the user’s spending data. 
3. The application should be easy to use and intuitive. 

## Instructions
Create a python program named **amazon_expenses_tracker.py**.

1. The program should accept username and password from the terminal for registration
2. Check the validity of the password using the following criteria:
    - Should have at least one number.
    - Should have at least one uppercase and one lowercase character.
    - Should have at least one special symbol.
    - Should be between 6 to 20 characters long. 
    - If the password is not valid the user will be ask to try again with a valid password, then exit the program. 
3. Ask the user to input his phone number(It should be a valid german mobile number). Prompt the user to input this number until he gets it right.
4. Ask the user to login. Print a message if the login was successful or print Invalid Username or password and ask again to enter username and password. If the user for three times input an incorrect username or password tell the user that he has used all the attempts and ask the user to try again after 5 seconds(Delay your app for 5 seconds). If after that 5 seconds he enters an incorrect username or password, ask the user to register again and exit the program. 
5. After the user has entered a valid password, he should be welcomed with the message ---> `Welcome to the Amazon Expense Tracker!`
6. Now you are ready to prompt user for input. A menu should be printed out showing 3 options: 
- `1. Enter a purchase`, 
- `2. Generate a report` (If this option is selected without entering any purchase, tell the user to enter at least one purchase and show the menu)
- `3. Quit.`
7. The user is asked to pick a choice using the numeric values associated. 
8. If the user picked `1`, the user should input 
   - The date of the purchase (accept the following formats: MM/DD/YYYY, MM-DD-YYYY) but save the date as MM/DD/YYYY, 
   - The item purchased (should be a string of at least 3 characters), 
   - The total cost of the item (should be an integer or a float - including charges on delivery), 
   - The weight of the item( should be a float, and in kg)
   - The quantity purchased (should be an integer from 1 and above).
9. If any of the condition for the inputs in step 8 is not met, prompt the user to re-enter the right value.

10. Save the purchases. Either in a list or dictionary(preferred).
11.  The user should be prompted again to the menu where he can choose `1` again if he needs to enter more items or he can choose other options.
12. If the user picked `2`, the script should generate a report: 
   - Calculate the total charges for delivery. Amazon charges `1 EURO` per `1 kg`
   - Calculate costs of the items, excluding delivery charges
   - Calculate the most and least expensive orders
   - Calculate the avarage cost with respect to the total number of orders
   - Calculate if the user has exceeded a fixed speding limit e.g. 500 Euro.
13. Finally print your report and when the report has been generated. (**hint** you can play with the the sleep() function here)
14. If the user picked `3`, the script should do nothing else, just print a goodbye message and quit. e.g. Display a final message thanking the user for the visit, using their name typed at the beginning.
15. If the user types anything different than `1`, `2` or `3` it should show an error message indicating the operation entered is not valid and instruct the user to select from the available options.

> **IMPORTANT**
>
> Do not forget to push all the changes to the remote repository once you are done. Commit the changes with a meaningful description.

> **Not enough?**
> You could enter multiple items in one session. 
> You have to try to make it as easy and functional as you can.
> `you could implement a way to categorize expenses for easy tracking and reporting.`
> `add a feature that allows users to set remeinders for upcoming payments.`
> Do you have other ideas? Try to iplement them after you have done the tasks with high priority.


## Sample outputs
You can use these samples to get a better idea of what the script should do. The text does not need to be exactly as it appears here. This is your project and you can adapt it as you wish, but the general flow should be as described.

**This is just an example**
`python3 amazon_expenses_tracker.py Federica TxelLci#2@8`
```
Registration successful!

---------------------
| Welcome to Amazon! |
---------------------

Please enter phone number to continue: +4930901820

Hello, Federica! Welcome to the Amazon Expense Tracker!
What would you like to do?
1. Enter a purchase
2. Generate a report
3. Quit
Enter your choice (1/2/3): 1
...
Enter the date of the purchase (MM/DD/YYYY): 02/10/2023
...
Enter the item purchased: book
...
Enter the cost of the item in Euro: 10
...
Enter the weight of the item in kg: 2
...
Enter the quantity purchased: 2
...

Purchase saved.
...
What would you like to do?
1. Enter a purchase
2. Generate a report
3. Quit
Enter your choice (1/2/3): 2
...
Generating report... [**bonus**: You can sleep for 2 seconds]
...
                 -------------------------
                 | Amazon Expense Report |
                 -------------------------
name: Federica    password: ***      Tel: +49***20      Date: 03/12/2023
----------------------------------
DELIVERY CHARGES       TOTAL ITEM COST             
  4 EURO                 16 EURO
  
MOST EXPENSIVE        LEAST EXPENSIVE
name: book            name: book
cost: 8 EURO          cost: 8 EURO

AVERAGE COST OF ITEM PER ORDER: 10 EURO
PURCHASE DATE RANGE: 02/10/2023 to 02/10/2023
--------
Note: You have not exceeded the spending limit of 500 EURO

...
What would you like to do?
1. Enter a purchase
2. Generate a report
3. Quit
Enter your choice (1/2/3): 3
...
Quitting program.. [**bonus**: You can sleep for 1 seconds]
Thank you for your visit, Federica. Goodbye!
```
