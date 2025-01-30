""" 
You are given two lists with an unknown amount of elements. 
Both of those lists may have some elements in common. 
Implement a method intersection that takes those two lists 
as arguments and returns a third list only with the elements t
hey have in common.
"""


def intersect(x, y):
    result = set(x).intersection(set(y))
    return list(result)


list_1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
list_2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]

print(intersect(list_1, list_2))
