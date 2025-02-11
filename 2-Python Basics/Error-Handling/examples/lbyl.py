"""
Program to delete a file
"""
import os

file_path = "/home/mk16/Documents/Source Files/DCI/P24-E07/live-code/2-Python Basics/Error-Handling/dummy.txt"

# Check if file actually exists
if os.path.exists(file_path):
    # Delete te file
    os.remove(file_path)
else:
    # Let the user know that something went wrong
    print(f"Error: file {file_path} does not exist.")
