# Function with default values
def sum(x=3, y=4):
    result = x + y
    return result

# function call with 2 arguments
print(sum(16, 8))

# function call with 1 argument
print(sum(16))

# function call with no arguments
print(sum())

# function with different data types from default values
print(sum("28", "14"))


# Function to generate user password

def generate_password(username: str = "John") -> str:
    password = str(username + "1234" + "secure")
    return password

print(generate_password("Elen"))
