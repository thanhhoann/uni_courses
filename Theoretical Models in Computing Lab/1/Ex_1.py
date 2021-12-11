# Ex_1

import math
import numpy as np
import matplotlib.pyplot as p

real_value = np.exp(-5)

l1 = []
l2 = []


def first_approach(x, term):
    result = 0
    prev_result = 0
    e_t = 0
    e_a = 0
    print("The First Approach: ")
    print("%s%20s%20s%20s" % ("Iteration", "Approximation", "E_a", "E_t"))
    for n in range(0, term):
        # calc the value
        prev_result = result
        result += math.pow(-x, n) / math.factorial(n)
        l1.append(result)

        # true error
        e_t = (real_value - result) / real_value

        # approximate value
        e_a = (result - prev_result) / result

        # show all 3 calculations
        print("%9d%20.10f%20.10f%20.10f" % (n, result, e_a, e_t))


def second_approach(x, term):
    result = 0
    prev_result = 0
    e_t = 0
    e_a = 0
    print("The Second Approach: ")
    print("%s%20s%20s%20s" % ("Iteration", "Approximation", "E_a", "E_t"))
    for n in range(0, term):
        # calc the value
        prev_result = result
        if result != 0:
            flip_result = 1 / result
        else:
            flip_result = 0
        flip_result += (math.pow(x, n) / math.factorial(n))
        result = 1 / flip_result
        l2.append(result)

        # true error
        e_t = ((real_value - result) / real_value)

        # approximate relative error
        e_a = ((result - prev_result) / result)

        # show all 3 calculations
        print("%9d%20.10f%20.10f%20.10f" % (n, result, e_a, e_t))


first_approach(5, 21)
print("\n")
second_approach(5, 21)
p.subplot(2, 1, 1)
p.plot(l1)
p.title("First Approach-PhanDinhThanhHoan_Lab1_Ex1")

p.subplot(2, 1, 2)
p.plot(l2)
p.title("Second Approach-PhanDinhThanhHoan_Lab1_Ex1")

p.show()
