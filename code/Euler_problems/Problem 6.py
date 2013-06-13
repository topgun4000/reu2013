#!/usr/bin/env python

"""
    A script solve Euler problem 6
"""

sum1 = 0
sum2 = 0
for i in range (101):
    sum1 = sum1 + i**2
    sum2 = sum2 + i

sum = sum1 - sum2**2
print(-sum)
    
    
    
