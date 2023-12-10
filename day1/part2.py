total_sum = 0

digit_mapping = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

with open('./input.txt', 'r') as file:
    for line in file.readlines():
        digits = []
        for char in range(len(line)):
            if line[char].isdigit():
                digits.append(int(line[char]))
            elif line[char].isalpha():
                current_number = line[char:char + 3]
                if current_number in digit_mapping:
                    digits.append(digit_mapping[current_number])
                else:
                    current_number = line[char:char + 4]
                    if current_number in digit_mapping:
                        digits.append(digit_mapping[current_number])
                    else:
                        current_number = line[char:char + 5]
                        if current_number in digit_mapping:
                            digits.append(digit_mapping[current_number])

        if len(digits) >= 2:
            first_digit = digits[0]
            last_digit = digits[-1]
            total_sum += first_digit * 10 + last_digit
        else:
            total_sum += digits[0] * 10 + digits[0]

print(total_sum)
