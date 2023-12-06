cards_sum = 0
cards = []

for line in open("input.txt"):
    line = line.strip().split(":")

    card = int(line[0][5:])
    cards.append(card)

    sets = line[1]
    sets = sets.strip().split("|")

    winning = sets[0].strip().split()
    gotten = sets[-1].strip().split()

    common = len(set(winning) & set(gotten))

    tmp = card + 1
    while tmp <= (card+common):
        for i in range(cards.count(card)):
            cards.append(tmp)
        tmp += 1



print(len(cards))