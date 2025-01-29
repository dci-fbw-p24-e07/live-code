# Task 1

fruits = []
fruits.append('Apples')
fruits.append('Cherries')
fruits.append('Strawberries')

for fruit in fruits:
    print(fruits)
    
for i in range(0, 3):
    print(fruits[i])
    
    

# Task 2

cities = ['London', 'Paris', 'Berlin', 'Amsterdam']
print('The capital city of Germany is: ' + cities[2])

# Task 3

colors = ['cyan', 'magenta', 'green', 'yellow', 'black', 'white']
colors.remove('green')
colors.remove('white')

for color in colors:
    print(color)

# Task 4

letters = ['p', 'e', 'n', 'g', 'u', 'i', 'n']
word = ''

for letter in letters:
    word = word + letter

word = word.capitalize()
print(word)