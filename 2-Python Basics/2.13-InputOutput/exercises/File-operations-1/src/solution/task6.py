"""Iterate the lines with readline()."""

with open("../data/task6.txt") as file:
    line = file.readline()
    line_lengths = []
    while line:
        line_lengths.append(file.tell() - sum(line_lengths)) 
        # all characters and \n are counted 
        line = file.readline()
    print(line_lengths)
