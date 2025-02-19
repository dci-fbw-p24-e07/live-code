""" 
single function getParity that does the same thing as 
the two functions in the previous task. This new function 
will accept a new positional argument of type String that 
will contain the type of parity we want to get (either odd 
or even).

If the argument parity is different than odd and even then 
it should output a string message Parity indicated is unknown.

Then design your own test cases to replicate the ones in 
the previous task but using the new function.
"""


def get_parity(x: int, parity: str) -> str | bool:
    """Checks if a given value is odd or even given the parity argument.

    Args:
        x (int): The value to be evaluated
        parity (str): The type of evaluation to be done

    Returns:
        str | bool: Indicating that the parity is possible and result of evaluation.
    """
    if parity == "odd":
        return bool(x % 2 != 0)
    elif parity == "even":
        return bool(x % 2 == 0)
    
    return "Parity indicated is unknown"


print(get_parity(1, "odd"), get_parity(1, "even"))
print(get_parity(657842, "odd"), get_parity(657842, "even"))
print(get_parity(0, "odd"), get_parity(0, "even"))
print(get_parity(-2, 'number'))
