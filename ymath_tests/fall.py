import matplotlib.pyplot as plt
import numpy as np




must = 300.0

ist = 2000.0

#time = 20

steps = 50



yy = []
sps = []




#gxb = 6*diff / steps **3

#ax  = 0

def yield_smooth_p2(ist, must, steps):
    diff = must - ist
    axb =  2*diff / steps**2
    y = ist    
    speed = 0.0
    xx = []
    yy = []
    for x in range(steps):        
        #yield (x,y)
        xx.append(x)
        yy.append(y)
        #sps.append(speed1)        
        ax = axb *[-1,1][x < steps/2]        
        #ax += axb *[-1,1][n < steps/2]        
        speed += 2*ax         
        #speed1 += ax * [-1,1][n < steps/2]    
        y += speed 
        #x = n/(steps-2)
    return xx,yy
    
   
xx,yy = yield_smooth_p2(ist, must, steps)    


plt.plot(xx,yy)
plt.show()

