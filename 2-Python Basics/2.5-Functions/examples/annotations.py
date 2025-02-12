# Define a type annotated function
def sum(x: int, y: int) -> int:
    result = x + y
    return result


print(sum(6, 8))

# Creates a list of users from a dictionary

def create_user_list(emp_dict: dict) -> list:
    user_list = []
    for emp in emp_dict.values():
        user_list.append(emp)
    return user_list


employees = {
    1: "John",
    2: "Susan",
    3: "Frank",
    4: "Mary"
}

print(create_user_list(employees))
