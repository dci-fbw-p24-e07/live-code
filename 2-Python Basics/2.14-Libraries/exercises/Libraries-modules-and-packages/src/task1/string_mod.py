def con(str1: str, str2: str) -> str:
    return str1 + str2

def string_from_list(my_list: list) -> str:
    return ''.join(my_list)

def check_digit(str1: str) -> bool:
    for character in str1:
        if character.isdigit():
            print("There is a digit in your string!")
            return True
    
    print("No digits!")
    return False
