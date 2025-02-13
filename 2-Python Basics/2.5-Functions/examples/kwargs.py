# Define a function to capture user information
def user_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} is {value}")

user_details(first_name="Susan", l_name="Franklin")
user_details(first_name="John", l_name="Jones", age=36, country="New Guinea")


# Function capture employee info
def get_emp_details(*args, **kwargs):
    details = {}
    for key, value in kwargs.items():
        details[key] = value
        
    details["projects"] = []
    for i in args:
        details["projects"].append(i)

    return details

print(get_emp_details("Oculus", "Elephant", "Meyer", first_name="Louis", last_name="Baker", age=45, email="lbaker@mail.com"))
