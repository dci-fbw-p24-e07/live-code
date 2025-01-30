""" 
Store the letters p, e, n, g, u, i, n in a list. 
Combine those letters into a single string penguin. 
Capitalize that string and print it to the screen.
"""

letters = ['p', 'e', 'n', 'g', 'u', 'i', 'n']
word = ''

for letter in letters:
    word = word + letter

word = word.capitalize()
print(word)
