#calculating with binominal formels:

from math_prob.ycombi import *        
        



p = 1.2*10**(-8)
n = 6.4*10**9


print("human_rates:")


for k in range(20,40):
    pk = binn(n,k,p)
    print("k = ", k , " : " , pk)
    
    
    
p_mice = 5.3 * 10 ** (-9)
n_mice = 5.4 * (10 ** 9)


print("mice_rates:")

for k in range(20,40):
    pk = binn(n_mice,k,p_mice)
    print("k = ", k , " : " , pk)

print("phu", p*n)
print("e_mice", p_mice *n_mice )


