""" 
You are given a list and two indizes. Implement a method (or function) swap 
that takes the list and the two indizes as arguments, swaps the values 
at the given indizes and returns the list.
"""

def swap(swap_list, x, y):
    swap_list[x], swap_list[y] = swap_list[y], swap_list[x]
    return swap_list

list_1 = [1, 2, 3, 4, 5]

print(swap(list_1, 2, 4))
