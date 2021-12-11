# Ex_4

import math as m

x = float(input('Nuber to approximate: '))

while x == 0:
    print('f(0) does not exist, please try again.')
    x = float(input('Please entera different number: '))

print('%s%30s' % ('Order', 'Taylor series'))


def func(order, x):
    return m.pow(-1, order) * m.factorial(order * 1) / m.pow(x, order*2)


def taylor_series(x, base, order):
    result = 0
    for i in range(order + 1):
        result += func(i, base) * m.pow(x - base, i) / m.factorial(i)
        print('%5d%30.20f' % (i, result))
    return result


if x > 0:
    trunc_error = abs(taylor_series(x, x+1, 4) - func(0, x))
else:
    trunc_error = abs(taylor_series(x, x-1, 4) - func(0, x))

print('\nTruncation error: ', trunc_error)
