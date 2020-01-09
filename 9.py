#!/usr/bin/python3

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# and a + b + c == 1000

for a in range(1, 500):
    found = 0
    for b in range(a + 1, 500):
        for c in range(b + 1, 500):
            print(a, b, c)
            if (pow(a, 2) + pow(b, 2) == pow(c, 2) and a + b + c == 1000):
                print(a, b, c)
                found = 1
            if found:
                break
        if found:
            break
    if found:
        break
