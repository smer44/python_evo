import numpy as np

#--- LU decomposition

def lu_decompose(arr):
    """makes LU decomposition of a given square matrix 
    input is equasion system turned to matrix like that:
    a1x + a2x2+ ... anax = b => [a1,a2...an] (without b )
    TODO - check cases with zeros in the matrix 
    TODO - and generally how does float != 0 works
    
    returns L, U  (modifies input matrix as U)
    
    
    """
    
    ln = arr.shape[0]
    assert len(arr.shape) == 2 and ln == arr.shape[1]
    L = np.eye(ln,dtype = np.float64)
    
    for n in range(ln ):
        div = arr[n,n]
        row = arr[n,n+1:]
        if div != 0:
            for m in range(n+1, ln):
                div2 = arr[m,n]              
                if div2 != 0:
                    factor = div2/div
                    #this goes on [n,m] position in L matrix:
                    L[m,n] = factor  
                    #scale row by the factor 
                    row_mod= row * factor
                    # at the m,n place of U-matrix must be zero after substraction:
                    arr[m,n] = 0.0
                    #substract the scaled row from the next row:
                    arr[m,n+1:] -= row_mod
                    
    return L, arr 
    
def triangle_solve(arr,b, low = False ):
    """
    Solves the equasion Ax = b , where
    A is a low or high triange square matrix and 
    b is a vector of constants
    
    returns xx a vector of solutions 
    """
    ln = arr.shape[0]
    assert len(arr.shape) == 2 and ln == arr.shape[1] and len(b.shape) == 1 and  ln == b.shape[0] \
    and (True if low else arr[-1,-1])
    xx = np.zeros(ln)
    if low:
        xx[0] = b[0]
        for i in range(1,ln,1):
            xx[i] = (b[i] - np.sum(arr[i,0:i]*xx[0:i])) 
        
    else:
        xx[-1] = b[-1]/arr[-1,-1]
        for i in range(ln-2,-1,-1):
            xx[i] = (b[i] - np.sum(arr[i,i+1:]*xx[i+1:])) / arr[i,i]
    return xx
        

def gaussv2(arr):
    """solves linear equasion system by gauss method 
    of a given square matrix 
    input is equasion system turned to matrix like that:
    a1x + a2x2+ ... anax = b => [a1,a2...an,b]
    
    TODO - check cases with zeros in the matrix 
    TODO - and generally how does float != 0 works
    
    returns triange matrix is modified input matix
    
    
    """
    
    ln = arr.shape[0]
    assert len(arr.shape) == 2 and ln == (arr.shape[1] -1) 
    xx = np.zeros(ln)    
    for n in range(ln ):
        div = arr[n,n]
        row = arr[n,n+1:]
        if div != 0:
            for m in range(n+1, ln):
                div2 = arr[m,n]              
                if div2 != 0:
                    factor = div2/div
                    row_mod= row * factor
                    # at the m,n place of U-matrix must be zero after substraction:
                    arr[m,n] = 0.0
                    #substract the scaled row from the next row:
                    arr[m,n+1:] -= row_mod
    #get variables from triangle matrix:
    xx[-1] = arr[-1,-1]/arr[-1,-2]
    for i in range(ln-2,-1,-1):
        xx[i] = (arr[i,-1] - np.sum(arr[i,i+1:-1]*xx[i+1:]))/arr[i,i]
                    
    return xx 


#input - equasion a1x + a2x2+ ... anax = b => [a1,a2...an,b]
# TODO - test for zeros
def gauss_old(arr):
    # create triangle matrix: 
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
    #get variables from triangle matrix:
    xx[-1] = arr[-1,-1]
    for i in range(ln-2,-1,-1):
        xx[i] = arr[i,-1] - np.sum(arr[i,i+1:-1]*xx[i+1:])
         
    
    return xx




 
def to_lsm(arr):
    mmax = arr.shape[1]
    nmax = mmax-1
    
    lsm = np.zeros( (nmax,mmax),  dtype=np.float32)
    for n in range(nmax):
        for m in range(mmax):
            lsm[n,m] = np.sum(arr[:,n] * arr[:,m])#can be optimized because lsm[n,m] = lsm[m,n]
    return lsm 


# it is the same as matrix mult transposed arr without last column to the array:
def to_lsmv2(arr):
    return arr[:,:-1].T @ arr

      
            
            
        
        
    


