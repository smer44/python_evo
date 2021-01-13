from math import log, exp


def log_fact(n):
    return log_an(n,1)
#    s = 0
#    for x in range(2,n+1):
#        s += log(x)
#    return s

def log_an(n,k):
    s = 0
    for x in range(k+1,n+1):
        s += log(x)
    return s




def log_cn(n,k):
    return log_an(n,k) - log_fact(n-k)


def log_bin(n,k,p ):
    return log_cn(n,k) + k*log(p) + (n-k) * log(1-p)



def log_poi(nxp, k):
    return log(nxp)*k - nxp- log_fact(k)



def log_hyp(x,n, takes, k):
    
    variants_taking_ones =  log_cn(takes, x)
    variants_taking_zeroes = log_cn(n- takes, k-x)
    variants_all =  log_cn(n, k)
    return variants_taking_ones + variants_taking_zeroes - variants_all


    
    
    
    

    