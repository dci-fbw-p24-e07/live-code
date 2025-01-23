""" 
You need to find the word "Nemo" in a given 
string and return its position in that string
"""

text = input("Enter some text: ")

if "Nemo" in text:
    print(f"I found Nemo at {text.find('Nemo')}!")
else:
    print("I can't find Nemo:(")
    