with open('./2023/day4/input.txt', 'r') as file:
    input = file.read()

rows = input.split('\n')[:-1]

def eval_no_raise(char):
    if char == ' ':
        return 0
    try:
        return eval(char)
    except (NameError, SyntaxError):
        return 0

def points(m):
    if m < 1:
        return 0
    if m == 1:
        return 1
    return pow(2, m-1)

copies = {}
def add_copy(card, multiplier):
    try:
        copies[card] += multiplier
    except KeyError:
        copies[card] = multiplier

corrs = set()
my = set()
for card, r in enumerate(rows):
    card += 1
    add_copy(card, 1)
    multiplier = copies[card]

    c, m = r.split(' | ')
    corrs = {eval_no_raise(i) for i in c.split(' ')}
    corrs = set(filter(lambda x: x, corrs))
    my = {eval_no_raise(i) for i in m.split(' ')}

    matches = len(list(corrs.intersection(my)))
    for m in range(1, matches + 1):
        add_copy(card + m, multiplier)
    corrs = set()
    my = set()

print(sum(copies.values()))
