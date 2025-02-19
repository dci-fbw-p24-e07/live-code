""" 
Packing and unpacking positional arguments
"""


def sum_all(*num_lists) -> int:  # packing
    result = 0
    for num_list in num_lists:
        result += sum(num_list)
    return result

test1 = [[0, 2, 4, 5]]
test2 = [
    [0, 2, 4, 5],
    [6],
    [0, 2, 4, 5, 1, 4, 3, 2]
]

print(sum_all(*test1))  # unpacking
print(sum_all(*test2))
