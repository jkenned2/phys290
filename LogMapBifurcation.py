import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# define logistic map
def F(x, a):
    return a*x*(1 - x)


# parameters (resolution and frame_num can be made higher for better results)
a0, a1 = 0,4
x0, x1 = 0,1

a_res = 1000
x_res = a_res

frame_num = 100
dpi = 1000

# set up graph
fig = plt.figure()
ax = plt.axes(xlim=(a0,a1), ylim=(x0,x1))
ax.set(title='Orbits of x under F=ax(1-x) vs. a', xlabel='a', ylabel='x')

scatter = ax.scatter([], [], s=400/(a_res*x_res), color='k', alpha=0.3)  # size scaling is kind of arbitrary
it_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)


# initialize big array
def initializeArray(a0, a1, a_res, x0, x1, x_res):
    a1d = np.linspace(a0, a1, a_res)
    x1d = np.linspace(x0, x1, x_res)
    a, x = np.meshgrid(a1d, x1d, indexing='xy')
    return np.array([a.flatten(), x.flatten()])


AX = initializeArray(a0, a1, a_res, x0, x1, x_res)


# init function
def init():
    scatter.set_offsets([])
    it_text.set_text('')
    return scatter, it_text


# animation function
def animate(i):
    AX[1,:] = F(AX[1,:], AX[0,:])
    scatter.set_offsets(np.c_[AX[0,:], AX[1,:]])
    it_text.set_text(f'depth = {i}')
    return scatter, it_text


# call animator
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=frame_num, interval=20, blit=True)
anim.save('logistic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'], dpi=dpi)

plt.show()
