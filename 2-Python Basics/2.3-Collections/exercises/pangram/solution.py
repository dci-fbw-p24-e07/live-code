""" 
Pangrams are sentences (i.e. strings) that contain all characters of the 
alphabet. Implement a method is_pangram that takes one argument as input 
and checks if the given string is a pangram and then returns the result as a boolean value.
"""
import string


def is_pangram(text):    
    # check if text contains all letter of alphabet
    # An alphabet to compare against
    letters = set(string.ascii_lowercase)
    return letters - set(text.lower()) == set([])
