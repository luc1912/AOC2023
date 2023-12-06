lines = open("input.txt").readlines()
total_sum = 0


def find_number(line, char):
    left = char
    right = char
    while left >= 0 and lines[line][left].isdigit():
        if lines[line][left].isdigit():
            left -= 1

    while right < len(lines[line]) and lines[line][right].isdigit():
        if lines[line][right].isdigit():
            right += 1

    number = lines[line][left+1:right]


    return int(number)


for line in range(len(lines)):
    for char in range(len(lines[line])):
        if not lines[line][char].isdigit() and not lines[line][char] == '.':
            numbers = []

            if line != 0 and line != len(lines)-1 and char != 0 and char != len(lines[line])-1:

                if lines[line][char - 1].isdigit():
                    if find_number(line, char - 1) not in numbers:
                        numbers.append(find_number(line, char - 1))
                        total_sum += find_number(line, char - 1)

                if lines[line][char + 1].isdigit():
                    if find_number(line, char + 1) not in numbers:
                        numbers.append(find_number(line, char + 1))
                        total_sum += find_number(line, char + 1)

                if lines[line - 1][char].isdigit():
                    if find_number(line - 1, char) not in numbers:
                        numbers.append(find_number(line - 1, char))
                        total_sum += find_number(line - 1, char)

                if lines[line + 1][char].isdigit():
                    if find_number(line + 1, char) not in numbers:
                        numbers.append(find_number(line + 1, char))
                        total_sum += find_number(line + 1, char)

                if lines[line + 1][char + 1].isdigit():
                    if find_number(line + 1, char + 1) not in numbers:
                        numbers.append(find_number(line + 1, char + 1))
                        total_sum += find_number(line + 1, char + 1)

                if lines[line + 1][char - 1].isdigit():
                    if find_number(line + 1, char - 1) not in numbers:
                        numbers.append(find_number(line + 1, char - 1))
                        total_sum += find_number(line + 1, char - 1)

                if lines[line - 1][char + 1].isdigit():
                    if find_number(line - 1, char + 1) not in numbers:
                        numbers.append(find_number(line - 1, char + 1))
                        total_sum += find_number(line - 1, char + 1)

                if lines[line - 1][char - 1].isdigit():
                    if find_number(line - 1, char - 1) not in numbers:
                        numbers.append(find_number(line - 1, char - 1))
                        total_sum += find_number(line - 1, char - 1)

for i in numbers:
    print(i)
print("Total sum:", total_sum)