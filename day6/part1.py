for line in open("input.txt"):
    if line.startswith("Time:"):
        line = line.strip().split(":")
        time = line[1].strip().split()

    elif line.startswith("Distance:"):
        line = line.strip().split(":")
        distance = line[1].strip().split()

counter = []
for i in range(len(time)):
    count = 0
    for j in range(int(time[i])):
        if (int(time[i]) - (j + 1)) * (j + 1) > int(distance[i]):
            count += 1
    counter.append(count)

result = 1
for element in counter:
    result = result*element


print(result)
