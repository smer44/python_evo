import matplotlib.pyplot as plt
import numpy as np
import scipy.special


#xx = np.arange(110,154,0.1)

xx = np.arange(70,110,0.1)

n = 180#  180 because of few 1-s left? # 200  * 190//168 no it does not work

k1 = 30

k2 = 150

p = (k1+k2)/ 2 / n 



print("n : " , n, " k = "  , (k1, k2) , "p =" , p)
yy3 = [scipy.special.binom(n, x) * p**x * (1-p) **(n-x)  for x in xx]

plt.plot(xx, yy3 )




plt.show()
