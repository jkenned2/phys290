import numpy as np


def bisect(f, a, b, err, imax=1000):
    if a >= b or imax < 1 or err <= 0:
        print('Invalid parameters')
        return
    i = 1
    while i <= imax:
        c = (b + a)/2
        if f(c) == 0 or (b - a)/2 < err:
            return c
        i += 1
        if np.sign(f(c)) == np.sign(f(a)):
            a = c
        else:
            b = c
    print('Maximum iterations reached')
    return


print(f'Actual value of pi is {np.pi}')
print(f'Approximated value of pi to 12 digits is {bisect(np.sin, 3, 4, 10**-12)}')
