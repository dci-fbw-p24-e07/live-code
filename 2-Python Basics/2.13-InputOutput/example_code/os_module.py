import os
import shutil

# Change the current working directory
os.chdir("../")

# Get the Current Working Directory
curr_dir = os.getcwd()
print(curr_dir)

# Create a new directory
os.mkdir("example_dir")

# List the contents of the current working directory
print(os.listdir())

# Remove a file
os.remove("example.txt")

# Delete an empty directory
os.rmdir("example_dir")

# Delete a non-empty directory
shutil.rmtree("dummy")

print(os.listdir())