with open('./2022/day3/input.txt', 'r') as file:
    input = file.read()

input = input.split('\n')


def get_prio(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 65 + 27

prios = 0
for sack in input:
    # print(list(set(sack[:int(len(sack)/2)]).intersection(set(sack[int(len(sack)/2):])))[0])
    try:
        prios += get_prio(list(set(sack[:int(len(sack)/2)]).intersection(set(sack[int(len(sack)/2):])))[0])
    except IndexError:
        continue
print(prios)
