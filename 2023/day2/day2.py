with open('./2023/day2/input.txt', 'r') as file:
    input = file.read()

input = input.split('\n')

red_max = 12
green_max = 13
blue_max = 14

ids_sum = 0

for i, game in enumerate(input):
    game_id = i + 1
    game = game.split(': ')[1]
    possible = True
    for cubeset in game.split('; '):
        for color_cubes in cubeset.split(', '):
            num, color = color_cubes.split(' ')
            if color == 'green' and int(num) > green_max:
                possible = False
            elif color == 'blue' and int(num) > blue_max:
                possible = False
            elif color == 'red' and int(num) > red_max:
                possible = False
    if possible:
        ids_sum += game_id

print(ids_sum)
