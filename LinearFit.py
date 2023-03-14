import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# parameters
nTrials = 100
nSize = 100


# pi approximation function
def Pi(N):
    x = np.random.uniform(0.,1.,N)
    return np.mean(4.*np.sqrt(1.-x**2))


def PiStdDev(N, nTrials):
    PiValues = []
    for i in range(nTrials):
        PiValues.append(Pi(N))
    return np.std(PiValues)


# calculating linear regression
Ns = np.logspace(0, 5, nSize).astype(int)
PiStdDevV = np.vectorize(PiStdDev)
PiStdDevs = PiStdDevV(Ns, nTrials)

x = np.log10(Ns)
y = np.log10(PiStdDevs)
m = (np.mean(np.multiply(x,y)) - np.mean(x)*np.mean(y))/(np.mean(x**2) - np.mean(x)**2)

# this would basically defeat the purpose of the assignment if I didn't already calculate the slope manually
X = x.reshape(-1, 1)
Y = y.reshape(-1, 1)
reg = LinearRegression().fit(X, Y)
b = reg.intercept_[0]

# plotting regression
fig, ax = plt.subplots()
ax.set(title=f'Linear regression with {nSize} points, {nTrials} trials per point',
       xlabel='log(N)', ylabel='log(sigma)')
ax.scatter(x, y, s=4)
ax.plot(x, m*x + b, label=f'slope={np.round(m,3)}, intercept={np.round(b,3)}')
plt.legend()

plt.show()
