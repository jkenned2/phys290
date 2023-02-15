import numpy as np

n = 2.


def FA(x):
    return .2*x+.8*n/x


def FB(x):
    return .5*(x+n/x)


def FC(x):
    Num = x*(x**2+3*n)
    Den = 3*x**2+n
    return Num/Den


def iterate(f, x, err, imax=1000):
    if err <= 0 or imax < 1:
        print('Invalid parameters')
        return
    i = 1
    while i <= imax:
        current_err = np.abs(x - f(x))
        if current_err < err:
            return x, current_err, i
        x = f(x)
        i += 1
    print('Maximum iterations reached')
    return


x0 = 0.1
tol = 10**-12
for f in FA, FB, FC:
    x, err, i = iterate(f, x0, tol)
    print(f'Used fcn. {f.__name__} to approximate sqrt(2) to 12 digits. '
          f'Got value {x} with estimated error {err} in {i} iterations')
