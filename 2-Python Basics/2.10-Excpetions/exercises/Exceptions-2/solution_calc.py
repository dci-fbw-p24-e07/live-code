# create a new exception class called "MathematicalError" from 
# BaseException class
class MathematicalError(Exception):
    pass

# write a function called parse_input that parses all the user 
# input according to rules list defined in the exercise text
def parse_input(user_input):
    eq_input = user_input.split(" ")
    
    if len(eq_input) != 3:
        raise MathematicalError("Input does not consist of three elements")
    
    num1, op, num2 = eq_input
    
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        raise MathematicalError("The first and third inputs must be numbers")
    
    if op not in ["+", "-", "/", "*"]:
        raise MathematicalError("Invalid operator. Can only use '+', '-', '/', '*'")
    
    return num1, op, num2

# function calculate takes 2 integers and an operation type as an argument
def calculate(n1, op, n2):
    if op == '+':
        return n1 + n2
    if op == '-':
        return n1 - n2
    if op == '*':
        return n1 * n2
    if op == '/':
        return n1 / n2

while True:
    user_input = input('>>> ')
    if user_input == 'quit':
        break
    
    n1, op, n2 = parse_input(user_input)
    result = calculate(n1, op, n2)
    print(result)
  