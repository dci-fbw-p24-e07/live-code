"""Task 5"""

users = [
    {
        "name": "Holly",
        "type": "Student",
        "password": "hunter"
    },
    {
        "name": "Peter",
        "type": "Student",
        "password": "pan"
    },
    {
        "name": "Janis",
        "type": "Teacher",
        "password": "joplin"
    }
]

def get_user(username: str, password: str):
    curr_user = None
    
    for user in users:
        if user["name"] == username and user["password"] == password:
            curr_user = user
            
    return curr_user

def is_student(user: dict) -> bool:
    return user["type"] == "Student"

def show_offers(username: str, password: str):
    curr_user = get_user(username, password)
    if not curr_user or is_student(curr_user):
        print("We have great courses to offer you!")
        
username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
show_offers(username, password)
