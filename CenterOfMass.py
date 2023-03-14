from scipy.special import j0
import numpy as np

# parameters
nSamples = int(1e5)
integralMin, integralMax = -1., 1.
volume = (integralMax - integralMin)**3


# density function
def rho(x,y,z):
    return 4 + x**3 + 3*y*j0(z)


# calculating COM
x = np.random.uniform(integralMin, integralMax, nSamples)
y = np.random.uniform(integralMin, integralMax, nSamples)
z = np.random.uniform(integralMin, integralMax, nSamples)

rhoV = np.vectorize(rho)
M = volume/nSamples * np.sum(rhoV(x, y, z))
comX = volume/nSamples * np.sum(x * rhoV(x, y, z)) / M
comY = volume/nSamples * np.sum(y * rhoV(x, y, z)) / M
comZ = volume/nSamples * np.sum(z * rhoV(x, y, z)) / M

print(f'Total mass {M}, center of mass {comX, comY, comZ}')
