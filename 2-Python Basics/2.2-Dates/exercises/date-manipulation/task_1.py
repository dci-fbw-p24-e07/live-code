""" 
Using the variable called current_datetime, 
subtract 15 days from the current time.
"""

from datetime import datetime, timedelta


current_datetime = datetime.now()

current_datetime = current_datetime - timedelta(days=15)
print(current_datetime.strftime("%Y-%m-%d"))
