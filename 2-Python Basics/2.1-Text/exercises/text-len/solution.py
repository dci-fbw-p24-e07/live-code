""" 
Write a program that detects if a string has 
an even/odd number of characters and prints "even" 
or "odd" accordingly.
"""

text = input("Enter some text: ")

text_length = len(text)

if text_length % 2 == 0:
    print("even")
else:
    print("odd")
