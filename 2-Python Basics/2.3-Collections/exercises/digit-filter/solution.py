""" 
You are given a list of strings. Some of those strings may contain integers, 
for example `Digital Car33r Institute`. Implement a method `digit_filter` 
that takes a list of strings as an argument and only returns those strings 
that don't contain a number.
"""

def digit_filter(og_list):
    new = []
    
    for x in og_list:
        if any(char for char in x if char.isdigit()):
            continue
        else:
            new.append(x)
                
    return new

l33t = ['Digital Car33r Institute', 'DCI', 'Digital', 'Career', 'Inst1tut3']

print(digit_filter(l33t))
