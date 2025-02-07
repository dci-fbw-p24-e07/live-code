""" 
Create a variable called text to store the data: 
Berlin is a world city of culture, politics, media and 
science. . Then search for the first white 
space character in the string and print its location 
using the appropriate label.
"""
import re

text = "Berlin is a world city of culture, politics, media and science."
pattern = " "  # "\s"

result = re.search(pattern, text).start()  # .span()[0]
print("The first white-space character is located at position:", result)
