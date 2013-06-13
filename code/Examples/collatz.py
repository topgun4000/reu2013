#!/usr/bin/env python
""" This is just me remembering how to use Python.
    To run use Run/Run Module option

    Alternatively, in terminal find directory with this program,
    use commands:
    cat collatz.py
    python collatz.py

    Better yet, give executable permission
    $ chmod a+x collatz.py
    then just run
    $ ./collatz.py
"""
def collatz(n):
    print(int(n))
    if n == 1:
        print('success!')
    elif n % 2 == 0:
        collatz(n / 2)
    else:
        collatz(3 * n + 1)


collatz(3)
