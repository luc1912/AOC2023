worth_sum = 0

for line in open("input.txt"):
    line = line.strip().split(":")

    card = int(line[0][5:])

    sets = line[1]
    sets = sets.strip().split("|")

    winning = sets[0].strip().split()
    gotten = sets[-1].strip().split()

    common = len(set(winning) & set(gotten))

    if common != 0:
        worth_sum += 2 ** (common - 1)


print(worth_sum)