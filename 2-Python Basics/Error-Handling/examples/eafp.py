"""
Program to delete a file
"""
import os

file_path = "/home/mk16/Documents/Source Files/DCI/P24-E07/live-code/2-Python Basics/Error-Handling/dummy.txt"


def greeting(name):
    return "Hello, " + name


try:
    # attempt file deletion
    os.remove(file_path)
    print(greeting("Michael"))
    
except OSError as err_1:
    print(f"Error occurred: {err_1}")
except NameError as err_2:
    print(f"Error occurred: {err_2}")
except:
    print("Error occured")

