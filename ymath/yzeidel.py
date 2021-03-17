
import numpy as np 







"""print(a)

d = np.diag(a)

# if init x zeros for step 0, the indexes of step 1 will be :
x = b / d 

print(x)

print(d.reshape(1,-1).T )

a = a/d.reshape(1,-1).T 

print(a)"""






def zeidel_iter_step(a,x,b,n):
    
    for i in range(n):
        #print(f"- x[{i}] = {b[i]} - {a[i,:i]} * {x[:i]} - {a[i,i+1:]}* {x[i+1:]}")
        x[i] = b[i] - np.sum(a[i,:i] * x[:i]) - np.sum(a[i,i+1:]*x[i+1:])
        
def zeidel_iter(a,b, steps =10):    
    d = np.diag(a)
    b = b/d
    x = np.zeros_like(b)
    a = a/d.reshape(1,-1).T 
    print(f"zeidel_iter")
    
    print(a)
    print(b)
    n = len(x)
    for i in range(steps):
        #print(f"zeidel_iter_step : {i}")
        zeidel_iter_step(a,x,b,n)
    print(x)
        
    return x 



        
    
        
    
    
    