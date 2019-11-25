import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import numpy as np
import re
from matplotlib.animation import FuncAnimation
from matplotlib.colors import Normalize


def humanDetector():
    with open("detection.txt") as fp:
        line = fp.readline()
        humanPresent = 0
        humanNotPresent = 0
        while line:
            
            # Regex pattern to recognize needed data
            match = re.findall(pattern=('(\d)'), string=line)
            
            if len(match) > 0:
                if match[0] == "0":
                    humanNotPresent += 1
                else:
                    humanPresent += 1

            line = fp.readline()
        
    if humanPresent > humanNotPresent:
        return "Human detected"
    else:
        return "Human not detected"    
    

def getData():

    data = pd.DataFrame()
    # Regex pattern to recognize needed data
    filepath = "data.txt"

    with open(filepath) as fp:
        line = fp.readline()
        counter = 0

        while line:
            
            # Regex pattern to recognize needed data
            match = re.findall(pattern=('(\d+.\d+)'), string=line)
            if len(match) == 16:
                dataSeries = pd.Series(match ,dtype='float', name=counter)
                counter += 1
                data = data.append(dataSeries, sort=None)

            line = fp.readline()

    # Filter erronous data
    data = data[data < 40]
    data = data[data > 10]
    data = data.dropna()

    return data

    

# Animation

fig = plt.figure()
gs = fig.add_gridspec(2, 2)
#creating a subplot
eye2Ax = fig.add_subplot(gs[0, 0])
eye1Ax = fig.add_subplot(gs[0, 1])

histogramAx = fig.add_subplot(gs[1, :])

def eye1(data):
    data = data
    lastLine = np.array(data.tail(1))
    grid = np.reshape(lastLine, (4, 4))
    grid = np.flipud(grid)
    return grid

def animate(i):
    data = getData()

    # print(data)
    histogramAx.clear()
    eye1Ax.clear()
    eye2Ax.clear()

    histogramAx.set_title(humanDetector(), fontsize=50)
    histogramAx.set_ylim([20, 33])
    histogramAx.set_xlim([0, 112])
    
    histogramAx.plot(data)

    eye1Ax.imshow(eye1(data), norm=Normalize(vmin=20, vmax=33, clip=False))
    # eye2Ax.plot(data)




ani = animation.FuncAnimation(fig, animate, interval=400)

plt.xlabel("Time (seconds)")
plt.ylabel("Temperature (celsius)")
plt.show()


