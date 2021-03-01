import numpy as np


def v3(a,b):
    return (a[1]*b[2] - a[2]*b[1], 
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0])
    
    
    
def m2_inv(mx):
    d = 1.0/( mx[0,0]*mx[1,1] - mx[0,1] * mx[1,0])
    
    return d* np.array([[mx[1,1], - mx[0,1]] , [-mx[1,0] , mx[0,0] ]])

    
    
    
res = v3([1,2,3] , [3,2,1])

print(res)

assert res == (-4,8,-4)
    
    
res = v3([4,1,6] , [2,3,5])   

print(res)

assert res == (-13, -8, 10)


mx = np.array([5,3,6,4]).reshape(2,-1)

print(mx)

mx = m2_inv(mx)

print(mx)


mx2 = np.array([1,4,2,6]).reshape(2,-1)

print(mx @ mx2)