import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

import re
from matplotlib.animation import FuncAnimation



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
#creating a subplot 
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    # print(data)
    ax1.clear()
    ax1.set_ylim([20, 33])
    ax1.plot(getData())



ani = animation.FuncAnimation(fig, animate, interval=400)

plt.xlabel("Time (seconds)")
plt.ylabel("Temperature (celsius)")
plt.show()
