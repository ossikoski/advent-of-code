with open('./2023/day2/input.txt', 'r') as file:
    input = file.read()

input = input.split('\n')

powers = 0

for game in input:
    game = game.split(': ')[1]
    red_max = 0
    green_max = 0
    blue_max = 0
    for cubeset in game.split('; '):
        for color_cubes in cubeset.split(', '):
            num, color = color_cubes.split(' ')
            if color == 'green' and int(num) > green_max:
                green_max = int(num)
            elif color == 'blue' and int(num) > blue_max:
                blue_max = int(num)
            elif color == 'red' and int(num) > red_max:
                red_max = int(num)

    powers += red_max*green_max*blue_max

print(powers)
