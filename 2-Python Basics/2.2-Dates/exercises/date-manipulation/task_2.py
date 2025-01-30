""" 
Using the variable called current_datetime, 
add 7 days to your current day.
"""

from datetime import datetime, timedelta

current_datetime = datetime.now()
current_datetime += timedelta(days=7)
print(current_datetime.strftime("%Y-%m-%d"))
