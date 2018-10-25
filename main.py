from datetime import datetime
import matplotlib.pyplot as plt
from numpy import *

file = open("big_data_cut.txt", "r")
 
plotingX = [];
plotingY = [];
nLine = 0
for line in file:
    line = line.strip('\n')
    nLine = nLine + 1
    elements = line.split(";")
    dateStr = elements[0]
    plotingX.append(datetime.strptime(elements[0], '%Y%m%d %H%M%S %f0'))
    plotingY.append(float(elements[1]))
    if (nLine % 100000 == 0):
        print(nLine)
		
lag1 = 2
lags = range(lag1, 20)
tau = [sqrt(std(subtract(plotingY[lag:], plotingY[:-lag]))) for lag in lags]
plt.figure(1)
plt.plot(lags, log(tau));
#plt.ion()

m = polyfit(lags, log(tau), 1)
hurst = m[0]*2
print ('hurst = ',hurst)

plt.figure(2)
plt.plot(plotingX, plotingY, 'r.')
plt.show();
