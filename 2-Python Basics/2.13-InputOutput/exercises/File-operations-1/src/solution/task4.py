"""Change the reading position."""

with open("../data/task4.txt") as file:
    file.seek(1622)
    print(file.read(13))
