nums_total = 0
mapping = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

with open('./2023/day1/input.txt', 'r') as input_file:
    lines = input_file.read().split('\n')

for l in lines:
    first_num = None
    last_num = None
    num = None
    
    def get_indices_sorted(l):
        indices = []  # Indices of numbers represented with letters, tuple: (start, end)
        for m in mapping:
            found_i = l.find(m)
            if found_i == -1:
                continue
            indices.append((l.find(m), l.find(m) + len(m)))
            if l.find(m, found_i+len(m)) == -1:
                continue
            indices.append((l.find(m, found_i+len(m)), l.find(m, found_i+len(m)) + len(m)))
        
        indices.sort(key = lambda tup: tup[0])
        return indices

    if l == '1eight3fivesix87five':
        pass
        print(":D")
    indices = get_indices_sorted(l)
    if indices:
        numword1 = l[indices[0][0]:indices[0][1]]
        l = l[:indices[0][0]] + str(mapping.index(numword1) + 1) + l[indices[0][1]:]

    indices = get_indices_sorted(l)
    if indices:
        numword2 = l[indices[-1][0]:indices[-1][1]]
        l = l[:indices[-1][0]] + str(mapping.index(numword2) + 1) + l[indices[-1][1]:]
    
    # l = l.replace(m, str(mapping.index(m) + 1))  # replace with number
    for char in l:
        try:
            num = int(char)
        except Exception:
            continue
        if not first_num:
            first_num = num
    last_num = num
    try:
        print(int(str(first_num) + str(last_num)))
        nums_total += int(str(first_num) + str(last_num))
    except ValueError:
        continue

print(nums_total)
