from ymath.ylineq import *



def solve_ga(arrp):
    arr = np.array(arrp, dtype=np.float32)
    ga =gaussv2 (arr)
    print("equasion:")
    print(arr)
    print("solution")
    print(ga)
    

arrp = [[1,-1,7],[3,2,16]] # answers [6,-1]

solve_ga(arrp)


arrp = [[1,2,3,6],[4,5,6,9],[7,8,0,-6]] #  answers [-2, 1, 2]

solve_ga(arrp)

#-- least squares method 


# the experimets are : a1x1i+...+anxni = bi

arrp = [[4,2,8],[5,2,4],[2,6,2], [3,0,8]] # 1.6531165311653115 -0.30894308943089427


arr = np.array(arrp, dtype=np.float32)

lsm = to_lsmv2(arr)

print(lsm)

ga =gauss (lsm)


print(ga)
              