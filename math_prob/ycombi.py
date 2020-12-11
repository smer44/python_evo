# x gets too big

import matplotlib.pyplot as plt 

def cn(n,k):
    if k> n-k:
        k = n-k
    x = 1.0
    for m in range(k):
        x*= (n-m)/(k-m)
    return x




def binn_old(n,k,p):
    return cn(n,k) * p**k * (1.0-p) ** (n-k)


def binn(n,k,p):
    loop_k = min(k,n-k)
    
    x = cn(n,k)
    for _ in range(loop_k):
        x *= p *(1.0-p)
    
    if k > n-k: 
        x*= p**(k - loop_k)
    else:
        x*= (1.0-p)**(n-k - loop_k)

    return x 

"""p = 1.2*10**(-8)
n = 6.4*10**9
k = 39 

b = binn(n,k,p)"""


n = 100
p = 60.0/100

x = [i for i in range(40,75)]
y = [1000*binn(n,k,p) for k in x]

plt.plot(x, y)

plt.show()

