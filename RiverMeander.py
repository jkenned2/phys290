import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# parameters
nSteps = 40
b = 10
theta0 = 110*np.pi/180
sigma = 17*np.pi/180
trials = int(1e6)
dpi = 500
interp = 3  # increase this for slower animation
nStepsInterp = nSteps*interp - interp + 1
frameNum = nStepsInterp

# initialization
pathArrayX = np.zeros((0, nStepsInterp))
pathArrayY = np.zeros((0, nStepsInterp))


# linear interpolation function
def linearInterpolate(arr, interp):
    size, = np.shape(arr)
    sizeInterp = size*interp - interp + 1
    arrInterp = np.zeros(sizeInterp)
    for i in range(sizeInterp-1):
        t = (i % interp)/interp
        arrInterp[i] = arr[int(i/interp)]*(1 - t) + arr[int(i/interp+1)]*t
    arrInterp[-1] = arr[-1]
    return arrInterp


# making paths
print('Making paths')
for i in range(trials):
    if i % (trials/10) == 0:
        print(f'{int(100*i/trials)}% done')
    thetaRelative = np.random.normal(0., sigma, nSteps)
    thetaAbs = np.cumsum(thetaRelative)
    thetaAbs += theta0 - thetaAbs[0]
    x = np.cumsum(np.cos(thetaAbs))
    y = np.cumsum(np.sin(thetaAbs))
    if (x[-1] - b)**2 + y[-1]**2 < 1:
        x = linearInterpolate(x, interp)
        y = linearInterpolate(y, interp)
        pathArrayX = np.vstack([pathArrayX, x])
        pathArrayY = np.vstack([pathArrayY, y])
print('100% Done')

# analysis and graphing
print('Making animation')
nPaths, nS = np.shape(pathArrayX)
meanX = np.mean(pathArrayX, axis=0)
meanY = np.mean(pathArrayY, axis=0)

# this is done to easily animate the mean line along with the rest of the lines
pathArrayX = np.vstack([pathArrayX, meanX])
pathArrayY = np.vstack([pathArrayY, meanY])

xMin, xMax = np.min(pathArrayX), np.max(pathArrayX)
yMin, yMax = np.min(pathArrayY), np.max(pathArrayY)

fig, ax = plt.subplots()
ax.set(title=f'{nPaths} meandering river paths ({trials} trials)', xlabel='x', ylabel='y',
       xlim=(xMin-1, xMax+1), ylim=(yMin-1, yMax+1))

lines = []
for i in range(nPaths):
    lines.append(ax.plot([], [], lw=.1)[0])
lines.append(ax.plot([], [])[0])


# init function
def init():
    for line in lines:
        line.set_data([], [])
    return lines


# animation function
def animate(i):
    for lNum, line in enumerate(lines):
        line.set_data(pathArrayX[lNum,:i], pathArrayY[lNum,:i])
    return lines


# call animator
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=frameNum, interval=20, blit=True)
anim.save('RiverMeander.mp4', fps=60, extra_args=['-vcodec', 'libx264'], dpi=dpi)

plt.show()
