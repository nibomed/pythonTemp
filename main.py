from datetime import datetime

file = open("data.txt", "r")
 
data = []
for line in file:
    line = line.strip('\n')
    elements = line.split(";")
    dateStr = elements[0]
    class element:
        date = datetime.strptime(elements[0], "%Y%m%d %H%M%S %f0");
        value = float(elements[1]);
    data.append(element);
   
for element in data:
    print(element.date, ">", element.value)
