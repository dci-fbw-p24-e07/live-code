""" 
Your task is to write a reminder message for a customer 
that is being sent out on 2020-01-01 to please pay in 25 
days. Create a string that stores a message to a customer 
called Friedrich, print out the message to the terminal.
"""

from datetime import datetime, timedelta

start_date = datetime(year=2020, month=1, day=1)
due_date = start_date + timedelta(days=25)
message = "Hello Friedrich, your rent of 199.00 € is due on {due_date}".format(
    due_date=due_date.strftime("%d %B, %Y"),
)
print(message)
