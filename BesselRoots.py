import numpy as np
import matplotlib.pyplot as plt
from scipy.special import *

# finding rough values of first 20 positive roots of j0(x)
rough_roots = []
step = 0.1
x = 0
while len(rough_roots) < 20:
    if np.sign(j0(x)*j0(x - step)) == -1:
        rough_roots.append(x)
    x += step


# applying 10 N-R iterations
# I just chose 14 sig digs for target accuracy
def NR_iterate_j0(x, err=10**-14, max_iter=20):
    i = 0
    while np.abs(j0(x)/j1(x)) > err and i < max_iter:
        x += j0(x)/j1(x)
        i += 1
    return x


polished_roots = np.vectorize(NR_iterate_j0)(rough_roots)

# plotting roots
fig, ax = plt.subplots()
ax.set(title='J_0(x) with approximated roots')
x = np.linspace(0, 70, 500)

ax.plot(x, j0(x), color='c', label='J_0(x)')
ax.scatter(rough_roots, j0(rough_roots), color='b', alpha=0.7, label='rough roots')
ax.scatter(polished_roots, j0(polished_roots), color='r', alpha=0.7, label='polished roots')
ax.legend()

plt.show()
