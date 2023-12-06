power_sum = 0

for line in open("./input.txt"):
    line = line.strip().split(":")
    game = int(line[0][5:])
    red = []
    green = []
    blue = []

    sets = line[1].replace(",", ";").split(";")
    for subset in sets:
        subset = subset.strip().split()
        color = subset[-1]
        count = int(subset[0])

        if color == 'red':
            red.append(count)
        elif color == 'green':
            green.append(count)
        elif color == 'blue':
            blue.append(count)

    power_sum += max(red)*max(green)*max(blue)


print("Sum of powers:", power_sum)
