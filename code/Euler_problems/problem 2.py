#!/usr/bin/env python

"""
    A script solve Euler problem 2
"""

sum = 0
f1 = 1
f2 = 1
while f2 <= 4000000:
    if f2%2 ==0:
        sum = sum + f2
    f3 = f1 + f2
    f1 = f2
    f2 = f3

print (sum)
    
