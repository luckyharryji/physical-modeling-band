import csv
import matplotlib.animation as animation
'''
timestamo: data[11]
linearacceleration x,y,z[12,13,14]
'''

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def randrange(n, vmin, vmax):
    return (vmax-vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# n = 100
# for c, m, zl, zh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
#     xs = randrange(n, 23, 32)
#     ys = randrange(n, 0, 100)
#     zs = randrange(n, zl, zh)
#     ax.scatter(xs, ys, zs, c=c, marker=m)

# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')
#
# plt.show()




with open('signal1_data.csv','rb') as f_in:
    reader = csv.reader(f_in)
    raw_data = list(reader)

# print data[0]


for index,data in enumerate(raw_data):
    if index==0:
        continue
    for index2,k in enumerate(data):
        raw_data[index][index2]=float(raw_data[index][index2])

v_x=0
v_y=0
v_z=0
s_x=0
s_y=0
s_z=0

sports_result=list()
sports_x=[]
sports_y=[]
sports_z=[]
moving_time=[]
a_x=[]
a_y=[]
a_z=[]
v_x_list=[]
v_y_list=[]
v_z_list=[]

for index,data in enumerate(raw_data):
    if index==0 or index==1:
        continue
    time=data[11] if index==1 else data[11]-raw_data[index-1][11]
    time_x=s_x+v_x*time+(0.5)*raw_data[index-1][12]*(time**2)
    time_y=s_y+v_y*time+(0.5)*raw_data[index-1][13]*(time**2)
    time_z=s_z+v_z*time+(0.5)*raw_data[index-1][14]*(time**2)
    sports_result.append([data[11],time_x,time_y,time_z])

    a_x.append(raw_data[index-1][12])
    a_y.append(raw_data[index-1][13])
    a_z.append(raw_data[index-1][14])

    v_x_list.append(v_x)
    v_y_list.append(v_y)
    v_z_list.append(v_z)

    sports_x.append(time_x*10)
    sports_y.append(time_y*10)
    sports_z.append(time_z*10)
    moving_time.append(data[11])
    # if time_x<s_x or time_y<s_y or time_z<s_z:
    #     print "yes"
    s_x=time_x
    s_y=time_y
    s_z=time_z
    v_x+=raw_data[index-1][12]*time
    v_y+=raw_data[index-1][13]*time
    v_z+=raw_data[index-1][14]*time
    # v_x=0
    # v_y=0
    # v_z=0
# print moving_time

def data_gen():
    t = data_gen.t
    cnt = 0
    while cnt < len(sports_x):
        cnt+=1
        t += 0.05
        print "postion of x, y, z: ",sports_x[cnt],sports_y[cnt],sports_z[cnt]
        print "time: ",moving_time[cnt]
        print "x accrleration: ",a_x[cnt]," y accrleration: ",a_y[cnt]," z accrleration: ",a_z[cnt]
        print "x speed: ",v_x_list[cnt]," y speed: ",v_y_list[cnt]," z speed: ",v_z_list[cnt]
        yield sports_x[cnt],sports_y[cnt],sports_z[cnt]
    print "end"
data_gen.t = 0

xdata=[]
ydata=[]
zdata=[]

def run(data):
    # update the data
    x,y,z = data
    # xdata.append(x)
    # ydata.append(y)
    # zdata.append(z)
    # line.set_data(xdata, ydata)
    ax.scatter([x],[y],[z],color='blue')

# ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=1,
#     repeat=False)
# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')
# plt.show()


ax.scatter(sports_x, sports_y, sports_z,color='blue')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
# print "end"
# print sports_result
# import json
# out_put={'data':sports_result}
#
# with open('moving_track_1.json','wb') as f_out:
#     f_out.write(json.dumps(out_put))
