def convert(number):
    digits = [int(digit) for digit in str(number)]
    digits.sort(reverse=True)
    return digits

print(convert(429563))  # [9, 6, 5, 4, 3, 2]
print(convert(324))     # [4, 3, 2]