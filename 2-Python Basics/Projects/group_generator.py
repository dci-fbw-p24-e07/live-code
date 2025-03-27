import random


def generate_groups(names_list: list, num_of_groups: int):
    
    # Further shuffle the list of names
    random.shuffle(names_list)
    
    # Get maximum number of members per group
    members_limit = len(names_list) // num_of_groups
    
    # Initialize groups dictionary
    groups = {}
    
    # Run loop for the number of groups to be created
    for i in range(num_of_groups):
        
        # Initialize current group list
        curr_grp = []
        
        # Run loop while group is not full
        while len(curr_grp) < members_limit:
            # Select random name from list
            name = random.choice(names_list)
            # Add name to current group
            curr_grp.append(name)
            # Remove name from original list
            names_list.remove(name)
        
        # Add group for groups dictionary
        groups[i + 1] = curr_grp
        
    # Return the generated groups
    return groups
    
    
p24_e07 = [
    "Eden",
    "Alex",
    "Wimpie",
    "Nico",
    "Thomas",
    "Britta",
    "Shafi",
    "Roman",
    "Uliana",
    "Daniel",
    "Padma",
    "Vadim"
]
print(generate_groups(p24_e07, 4))
    