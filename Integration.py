import numpy as np
import matplotlib.pyplot as plt


def RectIntegral(f, xmin, xmax, N):
    x = np.linspace(xmin, xmax, N)
    dx = x[1] - x[0]
    x_mapped = f(x[:-1]) * dx
    integral = np.sum(x_mapped)
    return integral


def TrapIntegral(f, xmin, xmax, N):
    x = np.linspace(xmin, xmax, N)
    dx = x[1] - x[0]
    x_mapped = .5 * (f(x[:-1]) + f(x[1:])) * dx
    integral = np.sum(x_mapped)
    return integral


fig, ax = plt.subplots()
ax.set(title='Integration error vs. # of gridpoints',
       xlabel='# of gridpoints', ylabel='|1 - Integral|',
       xscale='log', yscale='log')

Ns = np.linspace(100, 1000000, 10).astype(int)
doRectInt = np.vectorize(RectIntegral)
doTrapInt = np.vectorize(TrapIntegral)

RectIntErrors = np.abs(1 - doRectInt(np.sin, 0., np.pi/2, Ns))
TrapIntErrors = np.abs(1 - doTrapInt(np.sin, 0., np.pi/2, Ns))

rectSlope, rectIntercept = np.polyfit(np.log(Ns), np.log(RectIntErrors), 1)
trapSlope, trapIntercept = np.polyfit(np.log(Ns), np.log(TrapIntErrors), 1)

ax.plot(Ns, RectIntErrors, label=f'RectIntegral (log-log slope = {np.round(rectSlope, 3)})')
ax.plot(Ns, TrapIntErrors, label=f'TrapIntegral (log-log slope = {np.round(trapSlope, 3)})')
ax.legend()

plt.show()
