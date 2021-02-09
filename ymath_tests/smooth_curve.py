import matplotlib.pyplot as plt
import numpy as np




must = 300.0

ist = 2000.0

#time = 20

steps = 50
speed1 = 0.0
xx = [ x for x in range(steps)]

yy = []
sps = []
y = ist

diff = must - ist

mid = (must + ist) / 2
for n in xx:
    ax = [1,-1][n< steps/2]
    
    yy.append(y)
    sps.append(speed1)
    speed1 += ax 

    y += speed1 * (mid-y)
    #x = n/(steps-2)
    
    
   
    

print(yy[-1])
print(sps[-1])
plt.plot(xx,yy)
plt.show()

plt.show()
