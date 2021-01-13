from ymath.ymath import *
from math import *
import matplotlib.pyplot as plt
#exists in python:
#math.comb(n, k)
#math.factorial(n)


nl = exp(log_fact(10))

print(nl)


print(factorial(10))

n = 100
k = 2
p = 0.001

print(exp(log_cn(n,k)))


print(factorial(n) / factorial(k)/ factorial(n-k)) 


print(exp(log_bin(n,k,p)))
print(factorial(n) / factorial(k)/ factorial(n-k) * p**k * (1-p)**(n-k) ) 

print(exp(log_poi(n*p,k)))



nl = exp(log_fact(1))

print(nl)


nl = exp(log_fact(0))

print(nl)


nxp = 9000 //2

k = 500//2


xx = [k for k in range(nxp-k,nxp+k)]
yy = [exp(log_poi(nxp,k))  for k in xx]

plt.plot(xx,yy)

plt.show()

