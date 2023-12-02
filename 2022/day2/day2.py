with open('./2022/day2/input.txt', 'r') as file:
    input = file.read()

input = input.split('\n')

def calc_game(line):
    try:
        opp, me = line.split(' ')
    except ValueError:
        return 0

    win_points = 0  # 0, 3 or 6
    choice_points = 0
    if me == 'X':
        choice_points = 1
        if opp == 'A':
            win_points = 3
        elif opp == 'B':
            win_points = 0
        else:
            win_points = 6
    elif me == 'Y':
        choice_points = 2
        if opp == 'A':
            win_points = 6
        elif opp == 'B':
            win_points = 3
        else:
            win_points = 0
    else:
        choice_points = 3
        if opp == 'A':
            win_points = 0
        elif opp == 'B':
            win_points = 6
        else:
            win_points = 3

    return win_points + choice_points

points = 0
for line in input:
    points += calc_game(line)

print(points)
