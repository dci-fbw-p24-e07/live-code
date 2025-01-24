""" 
Write a Python program to determine whether the year 2021 is a leap year
"""

import calendar

year = int(input("Enter a year: "))

if calendar.isleap(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
