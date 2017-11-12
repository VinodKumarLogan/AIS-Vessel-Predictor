import time
import random
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

from sklearn.neighbors import KNeighborsClassifier
import warnings
warnings.filterwarnings('ignore')
df = pd.read_csv('Zone1_2014_01.csv')
 
#ysample = random.sample(range(-50, 50), 100)
xdata = []
ydata = [] 
Xdata = df['latitude']
Ydata = df['longitude']
plt.show()
 
axes = plt.gca()
axes.set_xlim(45, 55)
axes.set_ylim(-180, -170)
line, = axes.plot(xdata, ydata, 'r-')
  

 
for i in range(50000):
    xdata.append(Xdata[i])
    ydata.append(Ydata[i])
    line.set_xdata(xdata)
    line.set_ydata(ydata)
    plt.draw()
    plt.pause(1e-17)
    time.sleep(0.1)
 
# add this if you don't want the window to disappear at the end
plt.show()