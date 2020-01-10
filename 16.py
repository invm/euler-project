#!/usr/bin/python3

# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 21000?


def count_sum_of_digits(num):
    n = num
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


print(count_sum_of_digits(pow(2, 1000)))
