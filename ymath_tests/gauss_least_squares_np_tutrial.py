import numpy as np



#input - equasion a1x + a2x2+ ... anax = b => [a1,a2...an,b]
# TODO - test for zeros
def gauss(arr):
     
    ln = arr.shape[0]
    assert len(arr.shape) == 2 and ln == (arr.shape[1] -1) 
    xx = np.zeros(ln)
    for n in range(ln ):
        div = arr[n,n]
        if div != 0:
            arr[n,n] = 1.0
            arr[n,n+1:] = arr[n,n+1:]/div
            #print(f"Normalized n {n}\n" , arr)
            for m in range(n+1, ln):
                div2 = arr[m,n]
                
                if div2 != 0:
                    arr[m,n] = 1.0
                    arr[m,n+1:] = arr[m,n+1:]/div2
                    #print(f"Normalized m {m}\n" , arr)
                    arr[m,n:] = arr[m,n:] - arr[n,n:]
    xx[-1] = arr[-1,-1]
    for i in range(ln-2,-1,-1):
        xx[i] = arr[i,-1] - np.sum(arr[i,i+1:-1]*xx[i+1:])
         
    
    return xx







arrp = [[1,-1,7],[3,2,16]] #[6,-1]

arrp = [[1,2,3,6],[4,5,6,9],[7,8,0,-6]] # [2, -1, 2]

arr = np.array(arrp, dtype=np.float32)

ga =gauss (arr)

print(arr)
print(ga)


#-- least squares method 


# the experimets are : a1x1i+...+anxni = bi

arrp = [[4,2,8],[5,2,4],[2,6,2], [3,0,8]] # 1.6531165311653115 -0.30894308943089427

 
def to_lsm(arr):
    mmax = arr.shape[1]
    nmax = mmax-1
    
    lsm = np.zeros( (nmax,mmax),  dtype=np.float32)
    for n in range(nmax):
        for m in range(mmax):
            lsm[n,m] = np.sum(arr[:,n] * arr[:,m])#can be optimized because lsm[n,m] = lsm[m,n]
    return lsm 


# it is matrix mult transposed arr without last column to the array:
def to_lsmv2(arr):
    return arr[:,:-1].T @ arr

arr = np.array(arrp, dtype=np.float32)

lsm = to_lsmv2(arr)

print(lsm)

ga =gauss (lsm)


print(ga)
                    
            
            
        
        
    


