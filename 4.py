#!/usr/bin/python3

import sys

def isPalindrome(n):
    temp=n
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    if(temp==rev):
        return True
    else:
        return False

maxP = 0
for i in range(1000):
    for j in range(1000):
        if (isPalindrome(i*j)):
            if (i * j > maxP):
                maxP = i * j
print(maxP)
# print(isPalindrome(int(sys.argv[1])))
