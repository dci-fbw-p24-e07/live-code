#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "first_name",
    metavar="FIRST_NAME",
    type=str,
    nargs="?",
    help="Your first name",
    default="Larry",
)
parser.add_argument(
    "last_name",
    metavar="LAST_NAME",
    type=str,
    nargs="?",
    help="Your last name",
    default="Hanson",
)
parser.add_argument(
    "age", metavar="AGE", type=int, nargs="?", help="Your age", default=100
)

parser.add_argument(
    "--fast", action="store_true"
)
args = parser.parse_args()

if args.fast:
    print("fast mode enabled")

print(
    (
        f"Hello {args.first_name} {args.last_name}! "
        f"I see that you have had {args.age + 1} birthdays."
    )
)
