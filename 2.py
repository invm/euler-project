#!/usr/bin/python3

x = 0
y = 1
z = 1
sum = 0
while (z < 4000000):
	#print(z)
	x = y
	y = z
	z += x
	if (not z%2):
		sum += z
print(sum)
