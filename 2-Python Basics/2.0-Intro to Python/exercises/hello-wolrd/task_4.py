""" 
our task is a slightly modification of task 3. 
Instead printing True or False modify your code 
to get readable information about the type of your value.
"""

# Integer
print("Is", 123, "an instance of int?:", isinstance(123, int))

# Float
print("Is 43.23 an instance of float?:", isinstance(43.23, float))

# Complex
print("Is (4-1j) an instance of complex?:", isinstance(4-1j, complex))

# String
print("Is 'How are you?' an instance of str?:", isinstance("How are you?", str))

# Boolean
print("Is True an instance of bool?:", isinstance(True, bool))
