""" 
two simple functions is_odd and is_even that each 
take a single Integer and return a Boolean indicating 
whether the passed value is odd or is even.
"""


def is_odd(x: int) -> bool:
    """Checks if a number is is odd

    Args:
        x (int): an value of type int

    Returns:
        bool: A True or False
    """
    return bool(x % 2 != 0)


def is_even(x: int) -> bool:
    """Checks is a number is even

    Args:
        x (int): a value of type int

    Returns:
        bool: A True or False
    """
    return bool(x % 2 == 0)


print(is_odd(1), is_even(1))
print(is_odd(657842), is_even(657842))
print(is_odd(0), is_even(0))
