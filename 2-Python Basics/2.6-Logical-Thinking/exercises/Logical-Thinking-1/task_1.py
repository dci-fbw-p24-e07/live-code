""" 
Task 1
"""

username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
valid = {
    "username": "admin",
    "password": "admin"
    }
# Your code here

if username == valid["username"]:
    if password == valid["password"]:
        print(f"Welcome, {username}")
else:
    print("Credentials are invalid")
