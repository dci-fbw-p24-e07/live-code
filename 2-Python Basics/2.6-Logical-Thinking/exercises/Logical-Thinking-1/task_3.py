""" 
Task 3
"""
import datetime

username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
valid = {"username": "admin", "password": "admin"}
today = datetime.date(2021, 8, 6)

def is_weekend(date=datetime.datetime.now()) -> bool:
    weekday = date.weekday()
    return weekday == 5 or weekday == 6


if (username == valid["username"] and password == valid["password"]) or is_weekend(today):
    print(f"Welcome, {username}")
else:
    print("Credentials are invalid")
