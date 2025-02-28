""" 
Task 2
"""
import datetime


def is_weekend(date=datetime.datetime.now()) -> bool:
    weekday = date.weekday()
    return weekday == 5 or weekday == 6


print(is_weekend(datetime.date(2021, 8, 6)))
print(is_weekend(datetime.date(2021, 8, 7)))
print(is_weekend(datetime.date(2021, 8, 8)))
print(is_weekend(datetime.date(2021, 8, 9)))
