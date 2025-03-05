""" 
Task 2
"""

users = [
    {
        "name": "Holly",
        "type": "Student",
        "password": "hunter",
        "modules": [
            {
                "title": "Computer basics",
                "completed": True
            },
            {
                "title": "Python basics",
                "completed": False
            }
        ]
    },
    {
        "name": "Peter",
        "type": "Student",
        "password": "pan",
        "modules": [
            {
                "title": "Computer basics",
                "completed": False
            }
        ]
    },
    {
        "name": "Luke",
        "type": "Student",
        "password": "skywalker",
        "modules": [
            {
                "title": "Computer basics",
                "completed": True
            }
        ]
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
    return user and user["type"] == "Student"


def module_registered(user: dict, module_name: str):
    for module in user["modules"]:
        if module["title"] == module_name:
            return module
    return False


def show_registration(username: str, password: str, module_name: str):
    user = get_user(username, password)
    
    if is_student(user) and module_registered(user, module_name):
        print(f"You are registered to the module {module_name}")
    elif not user or is_student(user):
        print(f"You did not register to the module {module_name}")
    else:
        print("You are a teacher.")
        

def has_completed_module(username: str, password: str, module_name:str):
    user = get_user(username, password)
    if is_student(user):
        module = module_registered(user, module_name)
        if module and module["completed"]:
            print(f"You have completed the module {module_name}")
            return
    if not user or is_student(user):
        print(f"You did not complete the module {module_name}")

username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
modulename = input("What module do you want to check? ")
show_registration(username, password, modulename)
has_completed_module(username, password, modulename)
