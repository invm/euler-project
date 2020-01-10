#!/usr/bin/python3


def check_length(num):
    chain = []
    chain.append(num)
    while num != 1:
        if num % 2:
            num = num * 3 + 1
        else:
            num //= 2
        chain.append(num)
    return len(chain)


num = 999999
max_num = 999999
max_length = 0
while num > 1:
    if check_length(num) > max_length:
        max_length = check_length(num)
        max_num = num
        print(num)
    num -= 1
print(f'Max number is {max_num} and the chain length is {max_length}')

# Max number is 837799 and the chain length is 525
