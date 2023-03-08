import numpy as np
import matplotlib.pyplot as plt

# parameters
nLinks = 1000
flexibility = .1
trials = 1000

# initialization
thetaRelative = np.random.normal(0., flexibility, nLinks)
thetaAbs = np.cumsum(thetaRelative)
x = np.cumsum(np.cos(thetaAbs))
y = np.cumsum(np.sin(thetaAbs))

# make sample plot
fig1, ax = plt.subplots()
ax.set(title=f'Sample polymer with {nLinks} links of flex. {flexibility}', xlabel='x', ylabel='y')
ax.plot(x, y)


# writing functions
def polymerSpan(nLinks, flexibility):
    thetaRelative = np.random.normal(0., flexibility, nLinks)
    thetaAbs = np.cumsum(thetaRelative)
    x = np.cumsum(np.cos(thetaAbs))
    y = np.cumsum(np.sin(thetaAbs))
    distance = np.sqrt((x[-1]-x[0])**2 + (y[-1]-y[0])**2)
    return distance


def typicalPolymerSize(nLinks, flexibility, trials):
    polymerSpans = []
    for i in range(trials):
        polymerSpans.append(polymerSpan(nLinks, flexibility))
    return np.mean(polymerSpans)


# plotting mean distance vs. flexibility
flexibilityRange = np.linspace(0.01, 2.*np.pi, 100)
sizeRange = np.vectorize(typicalPolymerSize)(nLinks, flexibilityRange, trials)

fig2, ax = plt.subplots()
ax.set(title=f'Typical size of {nLinks}-link polymer over {trials} trials vs. flexibility',
       xlabel='flexibility', ylabel='mean size')
ax.plot(flexibilityRange, sizeRange, '-o', markersize=3)

plt.show()
