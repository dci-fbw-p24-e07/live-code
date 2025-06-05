"""Get the reading position."""

with open("../data/task5.txt") as file:
    print(file.readline())
    print(file.tell() - 1)  # Minus the line break.
