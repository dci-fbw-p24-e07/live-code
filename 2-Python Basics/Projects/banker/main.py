""" 
Program to mimic a banking setup
"""
from random import randint


class Bank:
    
    visa_compliant = True
    
    def __init__(self, bank_name: str):
        self.bank_name = bank_name
        self.name = ""
        self.acc_num = None
        self.account_balance = 0.0
        self.account_type = ""
        self.accounts = {
            11111: ["John Mayor", 10000, "Savings"],
            11112: ["Lucy Green", 15000, "Checking"]
        }
        
    def create_account(self, name, initial_deposit, acc_type):
        """ 
        Returns an account number for the newly created account
        """
        new_acc_num = randint(1000, 99999)
        while new_acc_num in self.accounts.keys():
            new_acc_num = randint(1000, 99999)
        self.accounts[new_acc_num] = [name, initial_deposit, acc_type]
        return new_acc_num
    
    def authenticate(self, name, acc_num):
        """ 
        Authenticate a user with their account number and name
        """
        for acc, user_details in self.accounts.items():
            if acc == acc_num:
                if name == user_details[0]:
                    self.acc_num = acc_num
                    self.name = user_details[0]
                    self.account_balance = user_details[1]
                    self.account_type = user_details[2]
                    return True
        return False
    
    def withdraw(self, withdraw_amount):
        """ 
        Deducts money from account by the withdraw amount.
        """
        if withdraw_amount > self.account_balance:
            return "Account balance is too low"
        else:
            self.account_balance -= withdraw_amount
            self.accounts[self.acc_num][1] = self.account_balance 
            return self.account_balance
        
    def deposit(self, deposit_amount):
        """ 
        Adds money the account balance by the deposit amount
        """
        self.account_balance += deposit_amount
        self.accounts[self.acc_num][1] = self.account_balance
        return self.account_balance
    
    def check_balance(self, acc_num):
        return self.account_balance
        
            
p24_bank = Bank("P24 Bank")

run_bank = True

while run_bank:
    logged_in = False
    
    print(f"Welcome to {p24_bank.bank_name}")
    print("1. Login to your account")
    print("2. Register for account")
    option1 = input("Login or Register: ")
    
    if option1 == "1":
        # Login
        print("**Please provide your login details**")
        name = input("Enter your name: ")
        acc_num = int(input("Enter your Account Number: "))
        logged_in = p24_bank.authenticate(name, acc_num)
        
        while logged_in:
            print(f"**Welcome, {name}! What would you like to do today?**")
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Check Balance")
            print("4. Logout")
            option2 = input("Enter an option: ")
            
            if option2 == "1":
                amount = float(input("Enter your withdrawal amount: "))
                balance = p24_bank.withdraw(amount)
                print(f"New balance: {balance}")
            elif option2 == "2":
                amount = float(input("Enter your deposit amount: "))
                balance = p24_bank.deposit(amount)
                print(f"New balance: {balance}")
            elif option2 == "3":
                print(p24_bank.check_balance(acc_num))
            elif option2 == "4":
                logged_in = False
            
    elif option1 == "2":
        # Registration
        print("**Please provide your registration details**")
        name = input("Enter your name: ")
        initial_deposit = float(input("Enter you initial deposit: "))
        acc_type = input("Enter your desired Acc Type: ")
        acc_num = p24_bank.create_account(name, initial_deposit, acc_type)
        print(f"Your account number is: {acc_num}")
