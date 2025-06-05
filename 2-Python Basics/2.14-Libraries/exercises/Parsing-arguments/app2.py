#!/usr/bin/env python3

import getopt, sys

args = getopt.getopt(sys.argv[1:], "hn:", ["help", "name="])[0]

name = False

for arg in args:
    if arg[0] in ["-h", "--help"]:
        print(
            (
                "This is a program to say good morning to someone. You can specify"
                " the recipient with --name/-n."
            )
        )
    if arg[0] in ["-n", "--name"]:
        name = arg[1]
if name:
    print(f"Good Morning {name}!")
else:
    print("Good Morning folks!")
