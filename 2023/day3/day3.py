import numpy as np


with open('./2023/day3/input.txt', 'r') as file:
    input = file.read()

shape = (140, 140)
# shape = (10, 10)

input_list = list(filter(('\n').__ne__, list(input)))
matrix = np.array(input_list).reshape(shape)

def get(i, j):
    """
    Get symbols from matrix
    Return the symbol if it is one, otherwise return None
    """
    if i < 0 or j < 0 or i >= shape[0] or j >= shape[1]:
        return None
    item = matrix[i, j]
    try:  # If it is int
        int(item)
        return None
    except ValueError:
        if item != '.':
            return item

parts_sum = 0

flag = False
num = ''
for i in range(shape[0]):
    if flag and num:  # Start of a new row
        parts_sum += int(num)
        flag = False
        num = ''
    for j in range(shape[1]):
        item = matrix[i, j]
        try:
            int(item)
            num += item
            if any([get(i-1,j-1),get(i-1,j),get(i-1,j+1),get(i,j-1),get(i,j+1),get(i+1,j-1),get(i+1,j),get(i+1,j+1)]):
                flag = True
        except ValueError:  # Not an int
            if flag and num:
                parts_sum += int(num)
            num = ''
            flag = False

print(parts_sum)
