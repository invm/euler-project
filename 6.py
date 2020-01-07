#!/usr/bin/python3

sum = 0
num = 0
for i in range(101):
    sum += i * i

for i in range(101):
    num += i

print(num * num - sum)
