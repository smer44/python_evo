from ymath.ylineq import *


def solveuv(arrp,b):
    arr = np.array(arrp, dtype=np.float32)
    b = np.array(b)
    l,u = lu_decompose(arr)
    y = triangle_solve(l, b, low = True)
    x = triangle_solve(u, y)
    print(x)
    
    

arrp= [[1,2], [4,5]]

b = [2,1]

solveuv(arrp,b)

#arrp = [[1,2,3,6],[4,5,6,9],[7,8,0,-6]] #  answers [-2, 1, 2]

arrp=  [[1,2,3],[4,5,6],[7,8,0]]

b = [6,9,-6]

solveuv(arrp,b)

