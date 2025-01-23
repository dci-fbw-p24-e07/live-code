""" 
Create a variable called text to store the 
data: 'Berlin is surrounded by the State of Brandenburg and 
contiguous with Potsdam, Brandenburg's capital.' . 
Your task is to check if the word capital is included in the text, 
if so, print the index of the location inside the text string.
"""

text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."

if text.find("capital"):
    print("capital: ", text.find("capital"))

# OR

if "capital" in text:
    print("capital: ", text.find("capital"))
