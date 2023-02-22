import numpy as np
import matplotlib.pyplot as plt
from cmath import *

# initialization
lower, upper = -2, 2
res = 400  # this should be made higher for better resolution
x1d = np.linspace(lower, upper, res)
y1d = np.linspace(lower, upper, res)
x, y = np.meshgrid(x1d, y1d)
z = x + 1j*y


# I just chose 14 sig digs for target accuracy
def NR_iterate_z(z, err=10**-14, max_iter=20):
    i = 0
    while np.abs(z - (2/3 * z + 1/(3*z**2))) > err and i < max_iter:
        z = 2/3 * z + 1/(3*z**2)
        i += 1
    return z, i


z, i = np.vectorize(NR_iterate_z)(z)
z = np.vectorize(phase)(z)

i_max = np.max(i)
pixel_colorings = np.zeros((res, res, 3))
pixel_colorings[:,:,0] = 1 - i/i_max

# making plot
fig = plt.figure(figsize=(9,5))
gs = fig.add_gridspec(1,2, wspace=0)
fig.suptitle('Approximation of cube roots of unity')
fig.supxlabel('Re(z)')
fig.supylabel('Im(z)')

ax1, ax2 = gs.subplots(sharex=True, sharey=True)
ax1.set(title='Basins of attraction')
ax2.set(title='Convergence rate of N-F iterations')

ax1.imshow(z, extent=(lower, upper, lower, upper))
ax2.imshow(pixel_colorings, extent=(lower, upper, lower, upper))

for ax in fig.get_axes():
    plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')

plt.show()
