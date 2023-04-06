from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np

# parameters
nGroups = 32
maxIterations = 10

# reading image
Im = imread('image.jpg')  # desired image should be put in same directory with this name
nY, nX, nChannels = np.shape(Im)
nPoints = np.size(Im[:, :, 0])
pointsR = np.reshape(Im[:, :, 0], nPoints)
pointsG = np.reshape(Im[:, :, 1], nPoints)
pointsB = np.reshape(Im[:, :, 2], nPoints)

# setup
meansR = np.random.uniform(0, 255, nGroups)
meansG = np.random.uniform(0, 255, nGroups)
meansB = np.random.uniform(0, 255, nGroups)

pointAssn = np.zeros_like(pointsR, dtype='int')


def colorDistance(r, g, b, cr, cg, cb):
    return np.sqrt((r - cr) ** 2 + (g - cg) ** 2 + (b - cb) ** 2)


pointDist = np.zeros((nPoints, nGroups))

# k-means clustering
for i in range(maxIterations):
    print(f'Iter. {i + 1}/{maxIterations}')
    for groupIndex in range(nGroups):
        pointDist[:, groupIndex] = colorDistance(pointsR, pointsG, pointsB,
                                                 meansR[groupIndex], meansG[groupIndex], meansB[groupIndex])
    pointAssn = np.argmin(pointDist, axis=1)
    for groupIndex in range(nGroups):
        if len(pointsR[pointAssn == groupIndex]) == 0:
            randomIndex = np.random.randint(0, nPoints)
            meansR[groupIndex] = pointsR[randomIndex]
            meansG[groupIndex] = pointsG[randomIndex]
            meansB[groupIndex] = pointsB[randomIndex]
        else:
            meansR[groupIndex] = np.mean(pointsR[pointAssn == groupIndex])
            meansG[groupIndex] = np.mean(pointsG[pointAssn == groupIndex])
            meansB[groupIndex] = np.mean(pointsB[pointAssn == groupIndex])

# 3d plot of k-means clustering
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(pointsR[::1000], pointsG[::1000], pointsB[::1000], c=pointAssn[::1000], cmap='jet')
# ax.scatter(meansR, meansG, meansB, color='k', s=500, marker='+')
# plt.show()

# redrawing image
cPixelsR = np.zeros_like(pointsR)
cPixelsG = np.zeros_like(pointsG)
cPixelsB = np.zeros_like(pointsB)

for i in range(nPoints):
    assn = pointAssn[i]
    cPixelsR[i] = meansR[assn]
    cPixelsG[i] = meansG[assn]
    cPixelsB[i] = meansB[assn]

cIm = np.full(np.shape(Im), 1, dtype=np.uint8)
cIm[:, :, 0] = cPixelsR.reshape((nY, nX))
cIm[:, :, 1] = cPixelsG.reshape((nY, nX))
cIm[:, :, 2] = cPixelsB.reshape((nY, nX))

# image is saved to directory
plt.imsave('compressed-image.jpg', cIm)

# show algorithm chosen colors
dTheta = 2. * np.pi / nGroups
colorWheelRes = 500
colorWheelIm = np.zeros((colorWheelRes, colorWheelRes, 3), dtype='int')

for i in range(colorWheelRes):
    for j in range(colorWheelRes):
        theta = np.pi + np.arctan2(j - .5 * colorWheelRes, i - .5 * colorWheelRes)
        groupIndex = int(theta / dTheta)
        if groupIndex == nGroups:
            groupIndex = nGroups - 1
        colorWheelIm[j, i, 0] = meansR[groupIndex]
        colorWheelIm[j, i, 1] = meansG[groupIndex]
        colorWheelIm[j, i, 2] = meansB[groupIndex]

plt.imshow(colorWheelIm)
plt.show()
