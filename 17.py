#!/usr/bin/python3

tens = [
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen',
]
singles = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
]
doubles = [
    'ten',
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety'
]


def print_in_words(num):
    n = f'{num}'
    num_in_words = ""
    if (len(n) == 4):
        num_in_words += 'onethousand'
        print(num_in_words)
        return len(num_in_words)
    if (len(n) == 3):
        if (int(n) % 100 == 0):
            num_in_words = singles[int(n) // 100 % 10 - 1] + 'hundred'
            print(num_in_words)
            return len(num_in_words)
        else:
            num_in_words += singles[int(n) // 100 % 10 - 1] + 'hundredand'
        if (int(n) % 100 // 10 == 0):
            n = n[2:]
        else:
            n = n[1:]
    if (len(n) == 2):
        if int(n) >= 11 and int(n) <= 19:
            num_in_words += tens[int(n) % 10 - 1]
            print(num_in_words)
            return len(num_in_words)
        else:
            num_in_words += doubles[int(n) // 10 - 1]
            if (int(n) % 10 == 0):
                print(num_in_words)
                return len(num_in_words)
        n = n[1:]
    if (len(n) == 1):
        num_in_words += singles[int(n) - 1]
    print(num_in_words)
    return len(num_in_words)


total = 0

for i in range(1, 1001):
    total += print_in_words(i)

print(total)
