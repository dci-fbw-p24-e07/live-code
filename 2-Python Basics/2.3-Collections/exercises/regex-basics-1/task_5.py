""" 
Use the text variable from the previous task. 
Create a regular expression to look for any word 
that starts with an upper case "B". Print the position 
(start- and end-position) of the first match occurrence.
"""
import re 

text = "Berlin is a city of culture."
pattern = "B[a-zA-Z]+"

result = re.search(pattern, text).span()
print(result)
