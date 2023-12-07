import numpy as np


with open('./2023/day3/input.txt', 'r') as file:
    input = file.read()

shape = (140, 140)
# shape = (10, 10)

input_list = list(filter(('\n').__ne__, list(input)))
matrix = np.array(input_list).reshape(shape)

indices = []

def get(i, j):
    """
    Get number from matrix
    Recursively add to number string items to left and right
    Keep track of items that have been gone through in the variable indices

    Returns
    -------
    The number (str) if it is number, '' if not
    """
    if i < 0 or j < 0 or i >= shape[0] or j >= shape[1]:
        return ''
    item = matrix[i, j]
    try:  # If item is int
        int(item)
        if (i,j) in indices:
            return ''
        indices.append((i,j))
        item = get(i, j-1) + item  # Add to string numbers before this item
        item = item + get(i, j+1)  # Add to string numbers after this item
        return item
    except ValueError:
        return ''

gears_sum = 0
flag = False
num = ''
for i in range(shape[0]):
    for j in range(shape[1]):
        item = matrix[i, j]
        if item != '*':
            continue
        adjacents = ([get(i-1,j-1),get(i-1,j),get(i-1,j+1),get(i,j-1),get(i,j+1),get(i+1,j-1),get(i+1,j),get(i+1,j+1)])
        num_adj = 0
        gear_ratio = 1
        for a in adjacents:
            try:
                int(a)
                num_adj += 1
                gear_ratio *= int(a)
                
            except ValueError:
                continue
        if num_adj == 2:
            gears_sum += gear_ratio

print(gears_sum)
