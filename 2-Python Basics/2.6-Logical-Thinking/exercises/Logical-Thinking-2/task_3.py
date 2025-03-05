""" 
Task 3
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

modules = [
    {
        "name": "Computer basics"
    },
    {
        "name": "Python basics",
        "requirement": "Computer basics"
    },
    {
        "name": "Django",
        "requirement": "Python basics"
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
        
    
def get_module(module_name):
    """Return the first module matching modulename."""
    return next(
        (module for module in modules
         if module["name"] == module_name), None)


def is_anonymous(user):
    """Return True if the user is anonymous."""
    return not user


def has_no_requirement(module):
    """Return true if the module has no requirement."""
    return module and "requirement" not in module


def module_completed(user, module_name):
    """Return the context of a completed module for a particular user."""
    return next(
        (m for m in user["modules"]
         if m["title"] == module_name and m["completed"]), None)


def meets_requirement(user, module):
    """Return True if the user meets the module's requirement."""
    return module and not module_registered(user, module["name"]) and (
        has_no_requirement(module)
        or module_completed(user, module["requirement"])
    )


def may_enroll(username, password, module_name):
    """Return True if the user is eligible for registration on the modulename."""
    user = get_user(username, password)
    module = get_module(module_name)
    return (is_anonymous(user) and has_no_requirement(module)
            or is_student(user) and meets_requirement(user, module))


# Test cases
username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
modulename = input("What module do you want to check? ")
show_registration(username, password, modulename)
has_completed_module(username, password, modulename)
if may_enroll(username, password, modulename):
    print(f"You may register to the module {modulename}.")
else:
    print(f"You may not register to the module {modulename}.")
