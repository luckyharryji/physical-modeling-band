import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def data_gen():
    t = data_gen.t
    cnt = 0
    print "haha"
    while cnt < 10:
        cnt+=1
        t += 0.05
        # print "haha"
        yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)
data_gen.t = 0

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_ylim(-1.1, 1.1)
ax.set_xlim(0, 5)
ax.grid()
xdata, ydata = [], []
def run(data):
    # update the data
    t,y = data
    print t,y
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()
    print data_gen.t
    if t >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()
    # line.set_data(xdata, ydata)

    # return line,

ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=10,
    repeat=False)
plt.show()
