from __future__ import division
import numpy as np
import math as m

def sum_to_n(n, size, limit=None):
    """
        Helper function, wrapped in function below to return as numpy array
    
        Produce all lists of `size` positive integers in decreasing order
        that add up to `n`.
    """
    if size == 1:
        yield [n]
        return
    if limit is None:
        limit = n
    start = (n + size - 1) // size
    stop = min(limit, n - size + 1) + 1
    for i in range(start, stop):
        for tail in sum_to_n(n - i, size - 1, i):
            yield [i] + tail

def gen_degrees(n, size, limit=None):
    """
        A function to generate the degree sequences of size summing to n
    """
    return np.array([seq for seq in sum_to_n(n, size, limit)])

def choose(n, k):
    """
        A helper function to compute n choose k
    """
    choose = m.factorial(n)
    choose = choose / (m.factorial(k) * m.factorial(n-k))
    return choose

def check_valid(seq, m):
    """
        A helper function to check if a sequence is theoretically 
        possible
    """
    valid = True
    for i in xrange(2, len(seq)):
        if np.sum(seq[:i]) > m + choose(i, 2):
            valid = False
    return valid

def weed_seqs(deg_seqs, m):
    """
        A function to weed out the impossible degree sequences
    """
    valid_seqs = np.array([])
    for seq in deg_seqs:
        if check_valid(seq, m):
            if len(valid_seqs) == 0:
                valid_seqs = np.array([seq])
            else:
                valid_seqs = np.concatenate((valid_seqs, np.array([seq])))
    return valid_seqs
