#!/usr/bin/env python
from __future__ import division
import numpy as np
from argparse import ArgumentParser
import aux_func as aux

"""
    A script to test Zarankiewicz numbers
"""

parser = ArgumentParser()

parser.add_argument("--n", action="store",
                    help='the size of the smaller partition')
parser.add_argument("--m", action="store",
                    help='the size of the larger partition')
parser.add_argument("--z", action="store",
                    help='the expected Zarankiewicz number')

args = parser.parse_args()

deg_seqs = aux.gen_degrees(int(args.z), int(args.n), int(args.m))

valid_seqs = aux.weed_seqs(deg_seqs, int(args.m))

#
# TODO:
# -weed out impossible sequences
# -check if viable sequences are achievible
#

for seq in valid_seqs:
    print(seq)

print('number of sequences: ', len(valid_seqs))
