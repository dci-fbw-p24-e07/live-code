""" 
Script to copy contents of one file into another.

Usage: 
`python3 file.py <name-of-input-file> -o/--output <name-of-output-file>`
"""
import argparse


# Initialize the ArgumentParser object
parser = argparse.ArgumentParser(
    description="Copy contents of one file into another."
    )

# Define the input argument
parser.add_argument(
    "input", 
    help="The name/filepath of input file to be processed"
)

# Define the output argument
parser.add_argument(
    "-o", "--output",
    help="The name/file path of the out put file",
    required=True  # Makes optional arguments required
)

# Parse the command line arguments
args = parser.parse_args()

# Process the input file
with open(args.input, "r") as input_file:
    data = input_file.read()

# Write the processed data to the output file
with open(args.output, "w") as output_file:
    output_file.write(data)
    
print(f"Data from {args.input} has been copied to {args.output}")
