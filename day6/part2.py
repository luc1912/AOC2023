for line in open("input.txt"):
    if line.startswith("Time:"):
        line = line.strip().split(":")
        time = line[1].strip().replace(" ", "")

    elif line.startswith("Distance:"):
        line = line.strip().split(":")
        distance = line[1].strip().replace(" ", "")

counter = 0
for i in range(int(time)):
    if (int(time) - (i+1))*(i+1) > int(distance):
        counter += 1

print(counter)
