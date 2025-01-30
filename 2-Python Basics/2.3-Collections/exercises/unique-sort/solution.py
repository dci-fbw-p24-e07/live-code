""" 
You are given a list of strings. Implement a method 
unique_char_sort to sort the list of strings by the number 
of unique characters in the strings.
"""


# find the number of unique chars in each string
def unique_char_count(string):
    char_set = set(string)
    char_count = len(char_set)
    return char_count


# sort the strings in order of character count
def unique_char_sort(strings):
    strings.sort(key=unique_char_count)
    return strings


strings = ['Digital', 'Career', 'Institute', 'Lecture', 'Exercise']


print(unique_char_sort(strings))
