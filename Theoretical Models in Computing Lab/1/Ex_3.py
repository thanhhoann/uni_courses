# Ex_3

import numpy as np
import math as m


def func(t):
    return m.pow(t, 4) * np.exp((-3) * m.pow(t, 2))


print("True value: %.10f" % (func(0.5)))


def first_deri(t):
    return (4*m.pow(t, 3) - m.pow(t, 5)*6)*np.exp((-3)*m.pow(t, 2))


def first_taylor(x, a):
    return (func((a) + first_deri(a)*(x-a)))


def e_t(x, a):
    return (func(x)-first_taylor(x, a)) / func(x)


print("First-order Taylor series has value: %.10f" % (first_taylor(0.5, 1)))
print("True error is: %10.f" % (e_t(0.5, 1)))
