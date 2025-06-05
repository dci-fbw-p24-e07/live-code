# Exercise 1

# Store data in a file
import json
new_file = open("files/newData.txt", mode="w", encoding="utf-8")
# save the data
new_file.write("Welcome to DCI python course \n")
new_file.write("Here you see database overview lecture \n")
# close/finish saving
new_file.close()


# ---------------------------------------------------------------
# Exercise 02: How read data from File-System disk/your computer
# -------------------------------------------------------------

# Read a existing text file, please check file path.
# if file path is wrong or not readble you will see this error "FileNotFoundError"
get_file = open("files/data.txt", mode='r')
print(get_file.read())


# ---------------------------------------------------------------
# Exercise 03: How to create and store json object to a file
# -------------------------------------------------------------
student_data = {"name": "arif", "role": "teacher"}
# convert python object to json string
json_string = json.dumps(student_data)
json_file = open("files/student.json", mode="w")
json_file.write(json_string)
json_file.close()


# ---------------------------------------------------------------
# Exercise 04: How to Read json data
# you must have existing data before
# -------------------------------------------------------------
json_file = open("files/student.json", mode="r")
print(json_file.read())

# ---------------------------------------------------------------
# Exercise 05: No code is required for this exercise, execute the helper functions and observe time (with a time clock).
# -------------------------------------------------------------
