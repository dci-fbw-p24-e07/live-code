# Check if a a number that has been input 
# by a user is greater than 0

number = int(input("Enter a number: "))

if number > 0:
    print("Your number is a positive number")
    
print("This is outside the if statement")

# Check if a users age is above 18
# If not tell them to kick rocks

age = int(input("Enter your age: "))

if age > 18:
    print("Welcome to the club")   
else:
    print("You need to leave")
    
print("This statement always executes")

# Check if a number is positive or negative
# if the number is greater than zero print "positive"
# if the number is less than 0 print "negative"
# if the number is equal to 0 print "zero"

num1 = 15
num2 = -6

if num1 > 0 and num2 > 0:
    print("Positive")

elif num1 < 0 and num2 < 0:
    print("negative")

elif num1 == 0 and num2 == 0:
    print("Zero")
    
else:
    print("What number did you input")
    
# Print each letter from the word one by one
    
word = "Python Rocks!"

# access each letter one by one
for letter in word:
    print(letter)

# using range() with for loop
# iterate from i = 0 to i = 5
for i in range(0, 6):
    print(i)
    
# Break the loop if the number is equal to 3
for i in range(0, 6):
    if i == 3:
        break
    print(i)
    
# Skip the number 4 and print the rest
for i in range(6):
    if i == 4:
        continue
    print(i)

# Print all the different combinations of numbers and letter
# They must go in sequence

letters = "abcde"
numbers = "12345"

for letter in letters:
    for number in numbers:
        print(letter, number)

    # This is outside the inner loop
    print("-----")

# print the current loop number
number = 0

while number <= 5:
    print(number)
    number += 1

