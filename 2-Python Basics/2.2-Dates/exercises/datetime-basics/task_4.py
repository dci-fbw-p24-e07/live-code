""" 
Your task is to convert a user provided string into a datetime object.
"""
from datetime import datetime

date = input("Enter a date, e.g 'Mar 16 2022 9:30PM': ")

converted_time = datetime.strptime(date, "%b %d %Y %I:%M%p")

print(converted_time)
