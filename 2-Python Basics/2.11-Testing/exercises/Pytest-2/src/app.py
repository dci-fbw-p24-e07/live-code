#!/usr/bin/env python
from typing import Union, Callable


def compare_to_seven(input: Union[int, str, Callable]) -> str:
    if isinstance(input, str):
        if input.isnumeric():
            number = int(input)
        elif len(input) != 1:
            number = 0
        else:
            number = ord(input)
    elif isinstance(input, int):
        number = input
    else:
        number = 0
    if number < 7:
        return f"{input} is lower than 7."
    elif number > 7:
        return f"{input} is higher than 7."
    return f"{input} is 7."


if __name__ == "__main__":
    compare_to_seven(8)
