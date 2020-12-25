
#14: argsort tutorial:

import numpy as np
import pprint as pp



arr = np.array([[50,60],[-20, -10], [ 70, 80],[30, 40],[10,20]])

fintesses = np.array([5,-2,7,3,1])

survive = 0.6

positions = np.argsort(fintesses)#[0: int(len(fintesses)*survive) ]
print(positions)


print(fintesses)


# massiv[massiv]
sarg = arr[positions]

print(arr)
print(sarg)

