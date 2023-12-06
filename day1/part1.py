total_sum = 0

with open('./input.txt', 'r') as file:
    for line in file.readlines():
        digits = []
        for char in line:
            if char.isdigit():
                digits.append(int(char))

        if len(digits) >= 2:
            first_digit = digits[0]
            last_digit = digits[-1]
            total_sum += first_digit * 10 + last_digit
        else:
            total_sum += digits[0] * 10 + digits[0]

print(total_sum)
