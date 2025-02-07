""" 
Create a variable called text to store the data: 
Berlin is a city of culture. . Replace the spaces with a hyphen.
"""
import re 

text = "Berlin is a city of culture."
pattern = " "  # \s 
replacement = "-"

result = re.sub(pattern, replacement, text)
print(result)