#!/usr/bin/python3

n = 600851475143
maxFact = 0
div = 2
while (n != 0):
    if (n % div != 0):
        div += 1
    else: 
        maxFact = n
        print(f'{maxFact}')
        n = n/div
        if (n == 1):
            print(f"{maxFact} is the prime")

print(f"{maxFact} is the prime")
exit()
