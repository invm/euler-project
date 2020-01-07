#!/usr/bin/python3

import math

count = 0
num = 2
while (count < 10001):
    flag = 1
    div = 2
    while (div <= math.sqrt(num)):
        if (not num % div):
            flag = 0
            break
        if (not flag):
            break
        div += 1
    if (flag):
        print(num)
        count += 1
    num += 1
