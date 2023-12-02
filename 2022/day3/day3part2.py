with open('./2022/day3/input.txt', 'r') as file:
    input = file.read()

input = input.split('\n')


def get_prio(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 65 + 27

prios = 0
i = 0
while i < len(input):
    try:
        prios += get_prio(list(set(input[i]).intersection(input[i+1]).intersection(input[i+2]))[0])
    except:
        continue
    i += 3

    
print(prios)
