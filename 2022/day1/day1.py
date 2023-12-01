with open('./2022/day1/input.txt', 'r') as file:
    cals = file.read()

cals = cals.split('\n')

all_cals = []
elf_cals = 0
for c in cals:
    if c == '':
        all_cals.append(elf_cals)
        elf_cals = 0
        continue
    elf_cals += int(c)

top3 = 0
all_cals.sort()
for c in all_cals[-3:]:
    top3 += c

print("Top3:", top3) 
