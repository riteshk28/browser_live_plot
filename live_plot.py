


import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import pandas as pd
import numpy as np
import time
import matplotlib as mpl
mpl.use('WebAgg')



fig = plt.figure("Temp")
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    data = pd.read_csv('test.csv')
    #the below option for tail 20 is to get latest 20 data points
    x,y = data.x.tail(20), data.y.tail(20)
    ax1.clear()
    #time.sleep(5)
    ax1.plot(x,y)




ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()



