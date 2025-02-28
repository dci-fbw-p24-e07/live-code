""" 
Task 4
"""

users = [
    {
        "name": "Holly",
        "password": "hunter"
    },
    {
        "name": "Peter",
        "password": "pan"
    },
    {
        "name": "Janis",
        "password": "joplin"
    }
]


def get_user(username: str, password: str):
    curr_user = None
    
    for user in users:
        if user["name"] == username and user["password"] == password:
            curr_user = user
            
    return curr_user


username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
user = get_user(username, password)

if not user:
    print("An error occurred. You are not authorized.")
    
