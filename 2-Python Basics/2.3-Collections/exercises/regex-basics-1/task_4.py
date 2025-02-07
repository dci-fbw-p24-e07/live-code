""" 
Create a variable called text to store the data: 
Berlin is a city of culture. . Search if the phrase 
in appears inside the string. Print the output of the 
regex function.
"""
import re

text = "Berlin is a city of culture."
pattern = "in"

result = re.search(pattern, text)
print(result)