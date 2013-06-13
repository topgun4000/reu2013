#!/usr/bin/env python
from __future__ import division
import math as m

"""
    Solves a specific optimization problem for a class
    I forget what the exact problem was
"""

def f(x): # function
    return .5/m.sqrt(1+x*x) - m.sqrt(1+x*x)*(1-.5/(1+x*x)) + x

def fp(x): # derivative
    return (f(x+.001) - f(x-.001)) / .002

def fpp(x): # 2nd derivative
    return (f(x+.001) - 2*f(x) + f(x-.001)) / .000001

x1 = .6
i = 2
while(True):
    x2 = x1 - fp(x1) / fpp(x1)
    # Prints values at each step
    print 'x' + str(i) + ': ' + str(x2)
    print 'e' + str(i) + ': ' + str(fp(x2)) # error
    x1 = x2
    if abs(fp(x2)) < .01:
        break
    print '\n'
    i += 1
