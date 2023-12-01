with open('./2022/day1/input.txt', 'r') as file:
    cals = file.read()

cals = cals.split('\n')
print(cals)

all_cals = []
elf_cals = 0
for c in cals:
    if c == '':
        all_cals.append(elf_cals)
        elf_cals = 0
        continue
    elf_cals += int(c)

print("Max cals:", max(all_cals))