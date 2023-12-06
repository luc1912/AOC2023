target_colors = {"red": 12, "green": 13, "blue": 14}
id_sum = 0

for line in open("./input.txt"):
    line = line.strip().split(":")
    game = int(line[0][5:])
    game_possible = True

    sets = line[1].replace(",", ";").split(";")
    for subset in sets:
        subset = subset.strip().split()
        color = subset[-1]
        count = int(subset[0])

        if color == 'red':
            if count > target_colors['red']:
                game_possible = False
        elif color == 'green':
            if count > target_colors['green']:
                game_possible = False
        elif color == 'blue':
            if count > target_colors['blue']:
                game_possible = False

    if game_possible:
        id_sum += game

print("Sum of IDs:", id_sum)
