import sys

# Integer
# Create a variable
a = 10

# Calculate the size of the variable
size_of_a = sys.getsizeof(a)

print(size_of_a)

# Float
decimal = 10.01

print("The size of  a float variable is:", sys.getsizeof(decimal), "bytes")

# String

c = ""

print("The size of an empty string is:", sys.getsizeof(c), "bytes")

d = "f"

print("The size of a string with 1 char is:", sys.getsizeof(d), "bytes")

# Boolean

e = True

print("The size of a boolean is:", sys.getsizeof(e), "bytes")