# define a function to add all numbers given in the parameters
def adder(*args) -> int:
    result = 0
    # Loop over args tuple
    for num in args:
        result += num
    return result

print(adder(5, 6, 7, 76, 4, 34, 56))

# Create a function called multipler that takes an 
# unknown number of arguments and multiplies all of them
def multiplier(*args) -> int:
    result = 1
    for num in args:
        result *= num
    return result

print(multiplier(2, 4, 5, 76, 89, 34))


def create_user(*args):
    for i in args:  # Looping over the tuple
        for j in i:  # Looping over the dictionary
            print(j)
        
create_user({
    "Name": "John",
    "dob": "6 July 1976",
    "Phone": "+345566776544"
})
