#!/usr/bin/env python3

import sys

args = sys.argv[1:]

if "--help" in args:
    print(
        (
            "This is just a small help text. You can use the --fast option to "
            "make this program work faster."
        )
    )

if "--fast" in args:
    print("fast mode enabled")
else:
    print("slow mode enabled")
