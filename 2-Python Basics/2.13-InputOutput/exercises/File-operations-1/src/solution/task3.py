"""Iterate the lines of a file."""


def print_line(line):
    """Print a line without the extra line break."""
    print(line.replace("\n", ""))


with open("../data/task3.txt") as file:
    even = []
    for num, line in enumerate(file):
        if num % 2:
            even.append(line)
        else:
            print_line(line)
    for line in even:
        print_line(line)
