""" 
Create a variable called text to store the data: The 
rain in Spain.. Count how many times the subphrase ai 
appears in the string. Print the results on the screen.
"""
import re

text = "The rain in Spain."
pattern = "ai"

result = re.findall(pattern, text)
print(len(result))
