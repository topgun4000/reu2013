#!/usr/bin/env python
from __future__ import division
import numpy as np

def sum_multiples(multis, max_num):
    """
        A function that sums up the multiples of elements in multis
        which are less than max_num

        Inputs:
        -multis: a numpy array of integers
        -max_num: an integer

        Returns:
        -sum: the sum of multiples of elements in multis less than max_num
    """
    sum = 0
    for i in range(max_num):
        flag = 0
        for multiple in multis:
            if i % multiple == 0 and flag == 0:
                sum += i
                flag = 1
    return sum

print(sum_multiples(np.array([3,5]), 1000))
