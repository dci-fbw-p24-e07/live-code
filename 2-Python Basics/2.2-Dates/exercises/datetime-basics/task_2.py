"""
Using the variable called some_date, print out the current week day
"""

from datetime import datetime

some_date = datetime.now()
print(some_date.weekday())
