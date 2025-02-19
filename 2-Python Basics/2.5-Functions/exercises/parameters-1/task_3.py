""" 
Multiple keyword arguments of different types
"""
import datetime


def greet(name: str, date: datetime.datetime) -> str:
    """Greets a user according to the time of day

    Args:
        name (str): name of the user
        date (datetime.datetime): time of day

    Returns:
        str: A string greeting the user
    """
    if date.hour < 12:
        return f"Good Morning, {name}!"
    else:
        return f"Good Afternoon, {name}!"
    

print(greet(
    name="John",
    date=datetime.datetime(2021, 5, 7, 11, 59, 59)
    ))
print(greet(
    date=datetime.datetime(2021, 5, 7, 12, 0, 1),
    name="John"
    ))
