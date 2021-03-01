
import numpy as np
import matplotlib.pyplot as plt 

data= \
[180.5,
178.8,
176.2,
177.1,
178.75,
179.25,
175.4,
178.2,
177.25,
177.5,
179.9,
180.8,
177.75,
179.5,
179.25,
178.5,
178.8,
178.5,
176.5,
178.76,
181.6]

arr = np.array(data)

mean = np.sum(arr)/arr.shape[0]

print(mean)

median = np.sort(arr)[int(arr.shape[0]/2)]


print(median)
#1.539

stddev = np.sqrt(np.sum((arr - mean)**2) /  (arr.shape[0]-1))

print(stddev)
#print(np.sum((arr-mean)**2))

histo = np.histogram(arr, bins = 12)

plt.bar(histo[1][:-1],histo[0])

plt.show()




