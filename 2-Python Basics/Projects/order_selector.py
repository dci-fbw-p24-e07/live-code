import random

# groups = ["Group 1", "Group 2", "Group 3", "Group 4"]
# random.shuffle(groups)
# print(groups)

def order_selector(num_of_groups: int) -> list:
    order = []
    
    for i in range(num_of_groups):
        order.append(i + 1)
    print(order)
    
    random.shuffle(order)
    
    return order

print(order_selector(4))
