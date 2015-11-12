import csv
import matplotlib.animation as animation
'''
timestamo: data[11]
linearacceleration x,y,z[12,13,14]
'''

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def load_data(index):
    with open('signal'+str(index)+'_data.csv','rb') as f_in:
        reader = csv.reader(f_in)
        raw_data = list(reader)
    _ax=list()
    _ay=list()
    _az=list()
    _time=list()
    for index,data in enumerate(raw_data):
        if index==0:
            continue
        for index2,k in enumerate(data):
            raw_data[index][index2]=float(raw_data[index][index2])
        _ax.append(data[12])
        _ay.append(data[13])
        _az.append(data[14])
        _time.append(data[11])
    return _ax,_ay,_az,_time


if __name__=='__main__':
    number = 6
    _ax,_ay,_az,_time = load_data(number)
    print _ax
    fig = plt.figure(figsize=(8,6),dpi=100)

    ax = fig.add_subplot(3,1,1)
    ax.scatter(_time,_ax)
    ay = fig.add_subplot(3,1,2)
    ay.scatter(_time,_ay)
    az = fig.add_subplot(3,1,3)
    az.scatter(_time,_az)
    ax.set_title('signal '+str(number))
    plt.show()
