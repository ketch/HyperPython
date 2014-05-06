import matplotlib.pyplot as plt
from matplotlib import animation
from clawpack.visclaw.JSAnimation import IPython_display

def ianimate(xc,q,bounds=(0,1,-0.1,1.1)):
    fig = plt.figure(figsize=(8,4))
    ax = plt.axes()
    im, = ax.plot([], [],linewidth=2)
    plt.axis(bounds)

    def fplot(i):
        im.set_data(xc, q[i])
        return im,

    return animation.FuncAnimation(fig, fplot, frames=len(q))
