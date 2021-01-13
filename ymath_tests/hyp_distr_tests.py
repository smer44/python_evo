from ymath.ymath import * 
import numpy as np 

import matplotlib.pyplot as plt


n = 150

takes =  30 

k = 150 

xx = np.arange(70,110)

yy = np.exp(np.array([log_hyp(x,n,takes,k)  for x in xx  ]  )  )



plt.plot(xx,yy, color = "green")

plt.show()