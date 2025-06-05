"""Count the lines of a file."""

with open("../data/task2.txt") as file:
    print(len(list(file)) - 2)
