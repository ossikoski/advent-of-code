with open('./2023/day5/input.txt', 'r') as file:
    input = file.read()

# Parse input to maps variable
rows = input.split('\n')[:-1]

maps = []
phase = 0  # Phase is e.g. seed-to-soil = 1
new_phase = True
for r in rows:
    if 'seeds' in r:
        nums = r.split(': ')[-1].split(' ')
        maps.append(list(map(int, nums)))
    elif r == '':
        new_phase = True
    elif new_phase:
        phase += 1
        maps.append([])
        new_phase = False
    else:
        nums = r.split(' ')
        maps[phase].append(list(map(int, nums)))

def find_loc(phase, num):
    """
    Recursive function finding the correspondence and calling the next
    phase with that correspondence.
    In the last phase returns the location.
    """
    for row in maps[phase]:
        if num > row[1] and num < row[1] + row[2]:
            diff = row[0] - row[1]
            if phase == 7:
                return num + diff
            return find_loc(phase=phase+1, num=num + diff)
    if phase == 7:
        return num
    return find_loc(phase=phase+1, num=num)

# Loop seeds and find corresponding location:
locs = []
for seed in maps[0]:
    locs.append(find_loc(1, seed))

print(min(locs))
