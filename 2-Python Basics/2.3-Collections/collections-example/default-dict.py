from collections import defaultdict

reg_dict = {"three": 3}

# Initialise the dictionary with a default value
new_dict = defaultdict()

# Accessing a missing key
print(reg_dict["missing"])  # Produces KeyError
print(new_dict["missing"])  # Output: []
