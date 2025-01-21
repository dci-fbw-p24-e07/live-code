"""
Your task is to write a Python program to guess a number 
between 1 to 10.

Note : User is prompted to enter a guess. 
If the user guesses wrong then the prompt
appears again until the guess is correct,
on successful guess, user will get a "Well guessed!" 
message, and the program will exit.

Hint: you don't know the random module yet, 
so set your number to guess hard-coded in your program.
"""

target_num = 7  # hard-coded version
guess_num = None
while target_num != guess_num:
    guess_num = int(
        input('Guess a number between 1 and 10 until you get it right : '))
print('Well guessed!')
