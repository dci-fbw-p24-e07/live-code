# Guess the meaning of life
number = 0

while number != 42:
    number = int(input("What is the meaning of life?: "))
    
# Guess the name
name = "Michael"
guess = input("I'm thinking of a name. Guess what it is: ")
guesses = 0 

while (guess != name) and (guesses < len(name) - 1):
    print("Nope, that's not it. Hint: ")
    print(f" Letter {guesses + 1} is {name[guesses]}")
    guess = input("Guess again: ")
    guesses += 1
    
if (guesses == len(name) - 1) and (name != guess):
    print(f"Too bad, you didn't get it. The name was {name}")
else:
    print(f"Great, you got it in {guesses + 1} tries!")
