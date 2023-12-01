nums_total = 0

with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()

for l in lines:
    first_num = None
    last_num = None
    num = None
    for char in l:
        try:
            num = int(char)
        except Exception:
            continue
        if not first_num:
            first_num = num
    last_num = num
    nums_total += int(str(first_num) + str(last_num))

print(nums_total)
