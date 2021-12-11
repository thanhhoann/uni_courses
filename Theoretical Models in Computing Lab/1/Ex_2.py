# Ex_2

import math as m
import numpy as np
import sys


def printf(format, *args):
    sys.stdout.write(format % args)


r = 0
k = 0.3 * np.pi
con = m.pow(10, -8)
true_value = np.cos(k)


def term(x, n):
    return m.pow(-1, n) * m.pow(x, 2 * n) / m.factorial(2 * n)


for i in range(100):
    r += term(k, i)
    print(r)
    if abs(r - true_value) < con:
        print("We need %d terms." % (i + 1))
        break
