#!/usr/bin/env python
from __future__ import division
from argparse import ArgumentParser
import numpy as np

"""
    A program to determine why the randomly generated matrix in the 
    6-6-3r case is not symetric

    This was used to find a bug way back when
"""

parser = ArgumentParser()

parser.add_argument("--input-matrix", action="store", help='the data file containing the offending matrix')
parser.add_argument("--output-file", action="store", help='the data file to put the output in')

args = parser.parse_args()

inmat = np.loadtxt(args.input_matrix)
outfile = file(args.output_file, 'w')
diff = inmat - np.transpose(inmat)
for A in xrange(diff.shape[0]):
    for B in xrange(diff.shape[0]):
        outfile.write(str(int(diff[A,B])))
        outfile.write(' ')
    outfile.write('\n')
