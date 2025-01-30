""" 
Store the colors cyan, magenta, green, yellow, black 
and white in a list called colors. Remove the colors 
green and white. Print the remaining colors to the screen.
"""

colors = ['cyan', 'magenta', 'green', 'yellow', 'black', 'white']
colors.remove('green')
colors.remove('white')

for color in colors:
    print(color)