from datetime import datetime
import matplotlib.pyplot as plt

file = open("data.txt", "r")
 
plotingX = [];
plotingY = [];
for line in file:
    line = line.strip('\n')
    elements = line.split(";")
    dateStr = elements[0]
    plotingX.append(datetime.strptime(elements[0], '%Y%m%d %H%M%S %f0'))
    plotingY.append(float(elements[1]))
   
plt.plot(plotingX, plotingY, 'r.')
plt.show();
