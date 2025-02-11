import re


def check_math(expression):
    pattern = "[0-9.]+ [\+\*\-\%\/]{1} [0-9.]+"
    match = re.match(pattern, expression)
     
    # if match:
    #     return True
    # else:
    #     return False
    return bool(match)

  
print(check_math("5 + 2"))
print(check_math("9 * 1"))
print(check_math("hello world"))
print(check_math("123"))
print(check_math("5 + foo"))
print(check_math("76.6 + 298.76"))
