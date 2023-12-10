states = {}
counter = 0

for index, line in enumerate(open("input.txt")):

    if index == 0:
        path = line.strip()

    elif index >= 2:
        line = line.strip().split("=")
        lr = line[1].strip().replace("(", "").replace(")", "").split(",")
        lr[1] = lr[1].strip()
        state = line[0].strip()
        states[state] = lr

state = "AAA"

while True:
    for i in path:
        if i == "L":
            state = states[state][0]
            counter += 1
        else:
            state = states[state][1]
            counter += 1

        if state == "ZZZ":
            print(counter)
            exit(0)


