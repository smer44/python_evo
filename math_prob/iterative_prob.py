

h = {(0,0): 1.0}

def iterprob(n,k,t=0,s=0):
    known = h.get((t,s), None)
    if known:
        return known 
    value =  iterprob(n,k, t-1,s-1) * (k-s) / (n-t) + iterprob(n,k, t-1,s) * (n-t) - (k-s) / (n-t)
    h[(t,s)] = value 
    return value





ip = iterprob(100,60,)

print(ip)