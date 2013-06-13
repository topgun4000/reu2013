#!/usr/bin/env python

"""
    A script solve Euler problem 1
"""

sum = 0
for i in range(1000):
    if i%3 == 0:
        sum = sum + i
    if i%5 ==0:
        sum = sum + i
    if i%15==0:
        sum = sum - i

print(sum)

 
