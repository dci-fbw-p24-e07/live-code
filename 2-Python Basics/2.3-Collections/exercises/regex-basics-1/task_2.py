""" 
Create a variable called text to store the data: 
Berlin is surrounded by the State of Brandenburg 
and contiguous with Potsdam, Brandenburg's capital. . 
Then search for the word Frankfurt in the string
"""
import re

text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."

result = re.search("Frankfurt", text)
print(result)
