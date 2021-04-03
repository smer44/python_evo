'''
splt digit on maximum distinkt summands


additional sopution possible

there is a arithm summ k(k+1)/2 of k first digits

@author: peter
'''

def split_sum(n):
    digit = 1 
    kk = [] 
    
    while (2*digit + 1 <= n):
        kk.append(digit)
        n = n-digit 
        digit = digit + 1 
    kk.append(n)
    return kk

print(split_sum(44843))