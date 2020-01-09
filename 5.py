#!/usr/bin/python3

# this is the answer
# num = 232792560
num = 20
while (True):
    flag = 1
    for i in range(1, 21):
        if (num % i):
            flag = 0
            print(num)
            break
    if (flag):
        print(num)
        break
    else:
        num += 10
